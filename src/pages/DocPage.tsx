import { useParams } from 'react-router-dom'
import { getPage, getTopics } from '@/lib/content'
import { MarkdownContent } from '@/components/MarkdownContent'
import { ScrollReveal } from '@/components/ScrollReveal'
import { DocPageHero } from '@/components/DocPageHero'
import { DocPageNav } from '@/components/DocPageNav'
import { DocPageToc } from '@/components/DocPageToc'
import { DocReadingProgress } from '@/components/DocReadingProgress'
import { NotFoundPage } from './NotFoundPage'

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

          <ScrollReveal animation="fade-up" delay={0.08} duration={0.9} distance={24}>
            <div className="doc-page__body">
              <MarkdownContent content={page.content} topic={page.topic} />
            </div>
          </ScrollReveal>

          <DocPageNav prev={prev} next={next} />
        </article>

        <DocPageToc contentKey={page.path} />
      </div>
    </div>
  )
}
