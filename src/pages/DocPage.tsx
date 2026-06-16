import { useState, useMemo } from 'react'
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
import { BookOpen, Brain } from 'lucide-react'

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

  const [isStudyMode, setIsStudyMode] = useState(false)
  const flashcards = useMemo(() => parseFlashcards(page.content), [page.content])

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

          {flashcards.length > 0 && (
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
          )}

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
              <div className="doc-page__body">
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

