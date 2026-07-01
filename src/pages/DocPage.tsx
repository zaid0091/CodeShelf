import { useState, useMemo, useEffect } from 'react'
import { markChapterCompleted, getCompletedChapters } from '@/lib/progress'
import { InteractiveRoadmap } from '@/components/InteractiveRoadmap'
import { useDocumentTitle } from '@/hooks/useDocumentTitle'
import { useParams } from 'react-router-dom'
import { getPage, getTopics } from '@/lib/content'
import { MarkdownContent } from '@/components/MarkdownContent'
import { ScrollReveal } from '@/components/ScrollReveal'
import { DocPageHero } from '@/components/DocPageHero'
import { DocPageNav } from '@/components/DocPageNav'
import { DocPageToc } from '@/components/DocPageToc'
import { DocReadingProgress } from '@/components/DocReadingProgress'
import { NotFoundPage } from './NotFoundPage'
import { parseFlashcards } from '@/lib/flashcards'
import { FlashcardViewer } from '@/components/FlashcardViewer'
import { BookOpen, Brain, Printer, FileDown, Notebook, X, Play, Trash2, Terminal } from 'lucide-react'

export function DocPage() {
  const { topic, slug } = useParams<{ topic: string; slug: string }>()
  const page = topic && slug ? getPage(topic, slug) : undefined

  if (!page) return <NotFoundPage />

  useDocumentTitle(`${page.title} | CodeShelf`)

  const topics = getTopics()
  const currentTopic = topics.find((t) => t.id === topic)
  const pages = currentTopic?.pages ?? []
  const currentIndex = pages.findIndex((p) => p.slug === slug)
  const prev = currentIndex > 0 ? pages[currentIndex - 1] : null
  const next = currentIndex < pages.length - 1 ? pages[currentIndex + 1] : null

  useEffect(() => {
    if (topic && slug) {
      markChapterCompleted(topic, slug)
    }
  }, [topic, slug])

  const [isStudyMode, setIsStudyMode] = useState(false)
  const flashcards = useMemo(() => parseFlashcards(page.content), [page.content])

  const [isNotesOpen, setIsNotesOpen] = useState(false)
  const [noteText, setNoteText] = useState('')

  const [viewMode, setViewMode] = useState<'roadmap' | 'text'>(() => {
    return (localStorage.getItem('codeshelf_view_pref') as 'roadmap' | 'text') || 'roadmap'
  })
  const [completedMap, setCompletedMap] = useState(() => getCompletedChapters())

  useEffect(() => {
    const handleUpdate = () => {
      setCompletedMap(getCompletedChapters())
    }
    window.addEventListener('codeshelf_progress_updated', handleUpdate)
    return () => window.removeEventListener('codeshelf_progress_updated', handleUpdate)
  }, [])

  // Read notes from localStorage when the page changes
  useEffect(() => {
    if (!page) return
    const savedNotes = localStorage.getItem('codeshelf_chapter_notes')
    if (savedNotes) {
      const notesMap = JSON.parse(savedNotes)
      setNoteText(notesMap[page.path] || '')
    } else {
      setNoteText('')
    }
  }, [page?.path])

  // Handle saving notes on text change
  const handleNotesChange = (text: string) => {
    if (!page) return
    setNoteText(text)
    const savedNotes = localStorage.getItem('codeshelf_chapter_notes')
    const notesMap = savedNotes ? JSON.parse(savedNotes) : {}
    notesMap[page.path] = text
    localStorage.setItem('codeshelf_chapter_notes', JSON.stringify(notesMap))
  }

  // Esc key to close notes drawer and console drawer
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        setIsNotesOpen(false)
        setIsConsoleOpen(false)
      }
    }
    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [])

  // Console State Variables
  const [isConsoleOpen, setIsConsoleOpen] = useState(false)
  const [consoleLang, setConsoleLang] = useState<'js' | 'py'>('js')
  const [consoleCode, setConsoleCode] = useState('')
  const [consoleOutput, setConsoleOutput] = useState<string[]>([])
  const [isLoadingPyodide, setIsLoadingPyodide] = useState(false)

  // Load draft code from localStorage when language or page changes
  useEffect(() => {
    const savedCode = localStorage.getItem(`codeshelf_console_code_${consoleLang}`)
    if (savedCode !== null) {
      setConsoleCode(savedCode)
    } else {
      setConsoleCode(
        consoleLang === 'js'
          ? '// Type JavaScript code here...\nconsole.log("Hello, JavaScript!");\n'
          : '# Type Python code here...\nprint("Hello, Python WASM!")\n'
      )
    }
  }, [consoleLang])

  // Save draft code to localStorage on change
  const handleCodeChange = (val: string) => {
    setConsoleCode(val)
    localStorage.setItem(`codeshelf_console_code_${consoleLang}`, val)
  }

  const loadPyodideScript = (): Promise<void> => {
    return new Promise((resolve, reject) => {
      if (document.getElementById('pyodide-script')) {
        resolve()
        return
      }
      const script = document.createElement('script')
      script.id = 'pyodide-script'
      script.src = 'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/pyodide.js'
      script.onload = () => resolve()
      script.onerror = () => reject(new Error('Failed to load Pyodide script'))
      document.head.appendChild(script)
    })
  }

  const runCode = async () => {
    setConsoleOutput(['Running...'])

    if (consoleLang === 'js') {
      const logs: string[] = []
      const originalLog = console.log
      console.log = (...args: any[]) => {
        logs.push(
          args.map(arg => typeof arg === 'object' ? JSON.stringify(arg) : String(arg)).join(' ')
        )
      }

      try {
        const runner = new Function(consoleCode)
        const result = runner()
        if (result !== undefined) {
          logs.push(`=> ${typeof result === 'object' ? JSON.stringify(result) : String(result)}`)
        }
      } catch (err: any) {
        logs.push(`Error: ${err.message}`)
      }

      console.log = originalLog
      setConsoleOutput(logs.length > 0 ? logs : ['Code executed successfully (no logs)'])
    } else {
      setIsLoadingPyodide(true)
      try {
        await loadPyodideScript()

        if (!(window as any).pyodide) {
          (window as any).pyodide = await (window as any).loadPyodide({
            indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/'
          })
        }

        const pyodide = (window as any).pyodide

        let stdoutBuffer = ''
        const decoder = new TextDecoder()
        pyodide.setStdout({
          write: (text: any) => {
            if (text instanceof Uint8Array || (text && text.buffer instanceof ArrayBuffer)) {
              const decoded = decoder.decode(text)
              stdoutBuffer += decoded
              return text.byteLength
            }
            const str = String(text)
            stdoutBuffer += str
            return str.length
          }
        })
        pyodide.setStderr({
          write: (text: any) => {
            if (text instanceof Uint8Array || (text && text.buffer instanceof ArrayBuffer)) {
              const decoded = decoder.decode(text)
              stdoutBuffer += decoded
              return text.byteLength
            }
            const str = String(text)
            stdoutBuffer += str
            return str.length
          }
        })

        const result = await pyodide.runPythonAsync(consoleCode)
        let outputLines = stdoutBuffer.split('\n').filter((line) => line !== '')

        if (result !== undefined && result !== null) {
          outputLines.push(`=> ${result}`)
        }

        setConsoleOutput(outputLines.length > 0 ? outputLines : ['Python code executed successfully (no prints)'])
      } catch (err: any) {
        setConsoleOutput([`Python Error: ${err.message}`])
      } finally {
        setIsLoadingPyodide(false)
      }
    }
  }

  const exportMarkdown = () => {
    const markdownContent = `---
title: ${page.title}
description: ${page.description || ''}
order: ${page.order}
---

# ${page.title}

${page.content}
`
    const blob = new Blob([markdownContent], { type: 'text/markdown;charset=utf-8;' })
    const url = URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.setAttribute('download', `${page.slug}.md`)
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
    URL.revokeObjectURL(url)
  }

  const exportPDF = async () => {
    const element = document.getElementById('print-content')
    if (!element) return

    // Dynamic import to keep bundler size minimal on initial loads
    const html2pdf = (await import('html2pdf.js')).default

    // Create an in-memory clone wrapper to style the PDF perfectly
    const wrapper = document.createElement('div')
    wrapper.className = 'codeshelf-pdf-wrapper'
    
    // Add custom inline styles for clean styling in the converted output
    wrapper.style.padding = '40px'
    wrapper.style.background = '#ffffff'
    wrapper.style.color = '#111111'
    wrapper.style.fontFamily = "'Manrope', system-ui, -apple-system, sans-serif"
    
    // Create a beautiful header card for the PDF
    const headerHtml = `
      <div style="margin-bottom: 30px; border-bottom: 2px solid #e2e8f0; padding-bottom: 20px;">
        <span style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #10b981; margin-bottom: 6px; display: inline-block;">
          ${page.topicLabel || 'Learning Chapter'}
        </span>
        <h1 style="font-size: 26px; font-weight: 800; color: #0f172a; line-height: 1.2; margin: 0 0 8px 0;">
          ${page.title}
        </h1>
        <p style="font-size: 14px; color: #475569; margin: 0; line-height: 1.5;">
          ${page.description || ''}
        </p>
      </div>
    `
    
    wrapper.innerHTML = headerHtml + `
      <div class="markdown-content">
        ${element.innerHTML}
      </div>
    `

    // Configure options for a high-quality crisp PDF output
    const opt = {
      margin:       0.6, // in inches
      filename:     `${page.slug}.pdf`,
      image:        { type: 'jpeg', quality: 0.98 },
      html2canvas:  { 
        scale: 2, 
        useCORS: true, 
        logging: false,
        backgroundColor: '#ffffff'
      },
      jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' },
      pagebreak:    { mode: ['css', 'legacy'] }
    }

    // Trigger html2pdf conversion and download
    html2pdf().set(opt as any).from(wrapper).save()
  }

  return (
    <div className="doc-page" key={page.path}>
      <DocReadingProgress />

      <div className="doc-page__layout">
        <article className="doc-page__article">
          <DocPageHero
            page={page}
            chapterIndex={currentIndex}
            chapterCount={pages.length}
          />

          <div className="doc-page__actions">
            {flashcards.length > 0 ? (
              <div className="doc-page__mode-toggle">
                <button
                  className={`mode-toggle-btn ${!isStudyMode ? 'mode-toggle-btn--active' : ''}`}
                  onClick={() => setIsStudyMode(false)}
                >
                  <BookOpen size={14} />
                  <span>Reading Mode</span>
                </button>
                <button
                  className={`mode-toggle-btn ${isStudyMode ? 'mode-toggle-btn--active' : ''}`}
                  onClick={() => setIsStudyMode(true)}
                >
                  <Brain size={14} />
                  <span>Study Mode ({flashcards.length})</span>
                </button>
              </div>
            ) : page.slug === 'ch00-course-overview' ? (
              <div className="roadmap-toggle-group">
                <button
                  type="button"
                  className={`roadmap-toggle-btn ${viewMode === 'roadmap' ? 'roadmap-toggle-btn--active' : ''}`}
                  onClick={() => {
                    setViewMode('roadmap')
                    localStorage.setItem('codeshelf_view_pref', 'roadmap')
                  }}
                >
                  Roadmap Graph
                </button>
                <button
                  type="button"
                  className={`roadmap-toggle-btn ${viewMode === 'text' ? 'roadmap-toggle-btn--active' : ''}`}
                  onClick={() => {
                    setViewMode('text')
                    localStorage.setItem('codeshelf_view_pref', 'text')
                  }}
                >
                  Classic List
                </button>
              </div>
            ) : (
              <div />
            )}

            {!isStudyMode && (
              <div className="doc-page__export-actions">
                <button
                  className="export-btn"
                  onClick={exportMarkdown}
                  title="Download Chapter as Markdown"
                >
                  <FileDown size={14} />
                  <span>Download MD</span>
                </button>
                <button
                  className="export-btn"
                  onClick={exportPDF}
                  title="Download Chapter as PDF"
                >
                  <Printer size={14} />
                  <span>Download PDF</span>
                </button>
              </div>
            )}
          </div>

          {isStudyMode ? (
            <div className="doc-page__body animate-fade-in">
              <FlashcardViewer
                cards={flashcards}
                topic={page.topic}
                onBackToReading={() => setIsStudyMode(false)}
              />
            </div>
          ) : page.slug === 'ch00-course-overview' && viewMode === 'roadmap' ? (
            <ScrollReveal animation="fade-up" delay={0.08} duration={0.9} distance={24}>
              <div className="doc-page__body">
                <InteractiveRoadmap
                  pages={pages}
                  completedPages={completedMap[page.topic] || []}
                />
              </div>
            </ScrollReveal>
          ) : (
            <ScrollReveal animation="fade-up" delay={0.08} duration={0.9} distance={24}>
              <div className="doc-page__body" id="print-content">
                <MarkdownContent content={page.content} topic={page.topic} />
              </div>
            </ScrollReveal>
          )}

          <DocPageNav prev={prev} next={next} />
        </article>

        {!isStudyMode && <DocPageToc contentKey={page.path} />}
      </div>

      {/* Floating Notes Toggle Button */}
      {!isStudyMode && (
        <button
          className="doc-page__notes-toggle"
          onClick={() => setIsNotesOpen(true)}
          title="Open Chapter Notes"
        >
          <Notebook size={16} />
          <span>Notes</span>
          {noteText.trim().length > 0 && <span className="notes-toggle-dot" />}
        </button>
      )}

      {/* Floating Console Toggle Button */}
      {!isStudyMode && (
        <button
          className={`doc-page__console-toggle ${isConsoleOpen ? 'doc-page__console-toggle--active' : ''}`}
          onClick={() => setIsConsoleOpen(!isConsoleOpen)}
          title="Toggle In-Browser Console"
        >
          <Terminal size={16} />
          <span>Console</span>
        </button>
      )}

      {/* Sidebar Summary Drawer */}
      {!isStudyMode && isNotesOpen && (
        <div className="notes-drawer">
          <div 
            className="notes-drawer__backdrop animate-fade-in" 
            onClick={() => setIsNotesOpen(false)}
          />
          <aside className="notes-drawer__panel animate-slide-in-right">
            <header className="notes-drawer__header">
              <div className="notes-drawer__header-titles">
                <h2 className="notes-drawer__title font-display text-ink">My Notes</h2>
                <p className="notes-drawer__subtitle text-caption truncate">{page.title}</p>
              </div>
              <button
                type="button"
                className="notes-drawer__close-btn"
                onClick={() => setIsNotesOpen(false)}
                aria-label="Close notes"
              >
                <X size={18} />
              </button>
            </header>

            <div className="notes-drawer__content">
              <textarea
                className="notes-drawer__textarea font-body"
                placeholder="Type your notes or summaries for this chapter here..."
                value={noteText}
                onChange={(e) => handleNotesChange(e.target.value)}
              />
            </div>

            <footer className="notes-drawer__footer">
              <span className="notes-drawer__status-text text-caption">
                {noteText.trim().length > 0 ? 'Saved in browser storage' : 'No notes written yet'}
              </span>
            </footer>
          </aside>
        </div>
      )}

      {/* Bottom Terminal Console Drawer */}
      {!isStudyMode && isConsoleOpen && (
        <div className="terminal-console animate-slide-in-up">
          <header className="terminal-console__header">
            <div className="terminal-console__langs">
              <button
                type="button"
                className={`terminal-console__lang-btn ${consoleLang === 'js' ? 'terminal-console__lang-btn--active' : ''}`}
                onClick={() => setConsoleLang('js')}
              >
                JavaScript
              </button>
              <button
                type="button"
                className={`terminal-console__lang-btn ${consoleLang === 'py' ? 'terminal-console__lang-btn--active' : ''}`}
                onClick={() => setConsoleLang('py')}
              >
                Python (WASM)
              </button>
            </div>

            <div className="terminal-console__actions">
              {isLoadingPyodide && <span className="terminal-console__loading text-caption animate-pulse">Initializing Python WASM...</span>}
              <button
                type="button"
                className="terminal-console__run-btn"
                onClick={runCode}
                disabled={isLoadingPyodide}
              >
                <Play size={12} />
                <span>Run Code</span>
              </button>
              <button
                type="button"
                className="terminal-console__clear-btn"
                onClick={() => setConsoleOutput([])}
              >
                <Trash2 size={12} />
                <span>Clear</span>
              </button>
              <button
                type="button"
                className="terminal-console__close-btn"
                onClick={() => setIsConsoleOpen(false)}
                aria-label="Close console"
              >
                <X size={16} />
              </button>
            </div>
          </header>

          <div className="terminal-console__body">
            <div className="terminal-console__input-panel">
              <textarea
                className="terminal-console__textarea font-code"
                placeholder={consoleLang === 'js' ? '// Type JavaScript code here...\nconsole.log("Hello, JavaScript!");' : '# Type Python code here...\nprint("Hello, Python WASM!")'}
                value={consoleCode}
                onChange={(e) => handleCodeChange(e.target.value)}
              />
            </div>
            <div className="terminal-console__output-panel font-code">
              {consoleOutput.length === 0 ? (
                <span className="terminal-console__placeholder">Terminal Output...</span>
              ) : (
                consoleOutput.map((line, idx) => (
                  <div 
                    key={idx} 
                    className={`terminal-console__line ${line.startsWith('Error') || line.startsWith('Python Error') ? 'terminal-console__line--error' : ''}`}
                  >
                    {line}
                  </div>
                ))
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

