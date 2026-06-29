import { useState, useMemo, useEffect } from 'react'
import { markChapterCompleted } from '@/lib/progress'
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
import { BookOpen, Brain, Printer, FileDown } from 'lucide-react'

export function DocPage() {
  const { topic, slug } = useParams<{ topic: string; slug: string }>()
  const page = topic && slug ? getPage(topic, slug) : undefined

  if (!page) return <NotFoundPage />

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
    </div>
  )
}

