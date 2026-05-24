import { Link, useParams } from 'react-router-dom'
import { ChevronLeft, ChevronRight } from 'lucide-react'
import { getPage, getTopics } from '@/lib/content'
import { MarkdownContent } from '@/components/MarkdownContent'
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
    <article>
      <header className="mb-10">
        <Link
          to={`/docs/${topic}/${pages[0]?.slug ?? slug}`}
          className="text-eyebrow !normal-case text-shade-50 hover:text-ink transition-colors"
        >
          {page.topicLabel}
        </Link>
        {page.tags.length > 0 && (
          <div className="flex flex-wrap gap-2 mt-4">
            {page.tags.map((tag) => (
              <Link
                key={tag}
                to={`/tags/${encodeURIComponent(tag)}`}
                className="text-eyebrow !normal-case px-3 py-1 rounded-pill bg-aloe text-ink hover:brightness-95 transition-all"
              >
                #{tag}
              </Link>
            ))}
          </div>
        )}
      </header>

      <MarkdownContent content={page.content} topic={page.topic} />

      {(prev || next) && (
        <nav className="mt-16 pt-8 border-t border-hairline-light flex justify-between gap-6">
          {prev ? (
            <Link
              to={prev.path}
              className="group flex flex-col gap-2 text-left max-w-[45%] p-4 -m-4 rounded-lg hover:bg-canvas-light transition-colors"
            >
              <span className="flex items-center gap-1 text-eyebrow !normal-case text-shade-50">
                <ChevronLeft size={14} strokeWidth={1.5} /> Previous
              </span>
              <span className="text-sm font-medium text-ink group-hover:underline underline-offset-2">
                {prev.title}
              </span>
            </Link>
          ) : (
            <span />
          )}
          {next ? (
            <Link
              to={next.path}
              className="group flex flex-col gap-2 text-right max-w-[45%] p-4 -m-4 rounded-lg hover:bg-canvas-light transition-colors ml-auto"
            >
              <span className="flex items-center justify-end gap-1 text-eyebrow !normal-case text-shade-50">
                Next <ChevronRight size={14} strokeWidth={1.5} />
              </span>
              <span className="text-sm font-medium text-ink group-hover:underline underline-offset-2">
                {next.title}
              </span>
            </Link>
          ) : (
            <span />
          )}
        </nav>
      )}
    </article>
  )
}
