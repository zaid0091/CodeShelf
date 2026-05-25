import { Link } from 'react-router-dom'
import { ArrowLeft, BookOpen, Clock, Hash } from 'lucide-react'
import { TopicIcon } from '@/components/TopicIcon'
import { ScrollReveal } from '@/components/ScrollReveal'
import { getCourseStartPath } from '@/lib/content'
import type { DocPage as DocPageData } from '@/lib/types'

interface DocPageHeroProps {
  page: DocPageData
  chapterIndex: number
  chapterCount: number
}

function calculateReadingTime(content: string): { minutes: number; words: number } {
  const words = content
    .replace(/```[\s\S]*?```/g, ' ')
    .replace(/[#*_`>\-[\](){}]/g, ' ')
    .split(/\s+/)
    .filter(Boolean).length
  const minutes = Math.max(1, Math.round(words / 220))
  return { minutes, words }
}

export function DocPageHero({ page, chapterIndex, chapterCount }: DocPageHeroProps) {
  const { minutes, words } = calculateReadingTime(page.content)
  const overviewPath = getCourseStartPath(page.topic)
  const chapterLabel = String(chapterIndex + 1).padStart(2, '0')
  const totalLabel = String(chapterCount).padStart(2, '0')

  return (
    <header className="doc-hero">
      <div className="doc-hero__ambient" aria-hidden>
        <span className="doc-hero__glow doc-hero__glow--aloe" />
        <span className="doc-hero__glow doc-hero__glow--warm" />
        <span className="doc-hero__mesh" />
      </div>

      <ScrollReveal
        animation="clip-up"
        duration={1.1}
        delay={0.05}
        start="top 95%"
        className="doc-hero__rail"
      >
        <span aria-hidden />
      </ScrollReveal>

      <div className="doc-hero__inner">
        <ScrollReveal
          animation="fade-up"
          delay={0.05}
          distance={20}
          duration={0.7}
          start="top 95%"
          className="doc-hero__topline"
        >
          <Link
            to={overviewPath}
            className="doc-hero__topic-chip"
            aria-label={`Back to ${page.topicLabel} overview`}
          >
            <span className="doc-hero__topic-chip-border" aria-hidden />
            <TopicIcon topicId={page.topic} size={16} className="doc-hero__topic-icon" />
            <span className="doc-hero__topic-name">{page.topicLabel}</span>
            <ArrowLeft size={12} strokeWidth={1.5} className="doc-hero__topic-arrow" aria-hidden />
          </Link>

          <span className="doc-hero__chapter-pill">
            <Hash size={11} strokeWidth={1.5} aria-hidden />
            <span className="doc-hero__chapter-current">{chapterLabel}</span>
            <span className="doc-hero__chapter-sep" aria-hidden>/</span>
            <span className="doc-hero__chapter-total">{totalLabel}</span>
          </span>
        </ScrollReveal>

        <ScrollReveal
          as="h1"
          animation="text-chars"
          duration={1}
          stagger={0.018}
          delay={0.18}
          start="top 95%"
          className="doc-hero__title font-display"
        >
          {page.title}
        </ScrollReveal>

        {page.description && (
          <ScrollReveal
            as="p"
            animation="blur-in"
            delay={0.4}
            duration={0.95}
            start="top 95%"
            className="doc-hero__desc"
          >
            {page.description}
          </ScrollReveal>
        )}

        <ScrollReveal
          animation="fade-up"
          delay={0.55}
          distance={16}
          duration={0.7}
          start="top 95%"
          className="doc-hero__meta"
        >
          <span className="doc-hero__meta-item">
            <Clock size={13} strokeWidth={1.5} className="doc-hero__meta-icon" aria-hidden />
            <span>
              <strong>{minutes}</strong> min read
            </span>
          </span>
          <span className="doc-hero__meta-dot" aria-hidden />
          <span className="doc-hero__meta-item">
            <BookOpen size={13} strokeWidth={1.5} className="doc-hero__meta-icon" aria-hidden />
            <span>
              <strong>{words.toLocaleString()}</strong> words
            </span>
          </span>
          <span className="doc-hero__meta-dot" aria-hidden />
          <span className="doc-hero__meta-item doc-hero__meta-item--muted">
            Chapter {chapterIndex + 1} of {chapterCount}
          </span>
        </ScrollReveal>
      </div>
    </header>
  )
}
