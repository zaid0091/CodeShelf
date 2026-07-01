import { Link } from 'react-router-dom'
import { useDocumentTitle } from '@/hooks/useDocumentTitle'
import { ArrowUpRight, BookOpen, Layers, Search } from 'lucide-react'
import { getTopics, getCourseStartPath } from '@/lib/content'
import { TopicIcon } from '@/components/TopicIcon'
import { useSmoothCardGlow } from '@/hooks/useSmoothCardGlow'

function DocsIndexCard({
  topicId,
  label,
  noteCount,
  index,
}: {
  topicId: string
  label: string
  noteCount: number
  index: number
}) {
  const { cardRef, onPointerEnter, onPointerMove, onPointerLeave } =
    useSmoothCardGlow<HTMLAnchorElement>('docs-index-card--hover')

  return (
    <li
      className="docs-index-card-wrap"
      style={{ animationDelay: `${0.06 + index * 0.07}s` }}
    >
      <Link
        ref={cardRef}
        to={getCourseStartPath(topicId)}
        className="docs-index-card"
        onPointerEnter={onPointerEnter}
        onPointerMove={onPointerMove}
        onPointerLeave={onPointerLeave}
      >
        <span className="docs-index-card__border" aria-hidden />
        <span className="docs-index-card__spotlight" aria-hidden />
        <span className="docs-index-card__shine" aria-hidden />

        <span className="docs-index-card__index" aria-hidden>
          {String(index + 1).padStart(2, '0')}
        </span>

        <div className="docs-index-card__icon-well">
          <TopicIcon topicId={topicId} size={36} className="docs-index-card__icon" />
        </div>

        <div className="docs-index-card__body">
          <h2 className="docs-index-card__title font-display">{label}</h2>
          <p className="docs-index-card__meta">
            <span className="docs-index-card__count">
              {noteCount} note{noteCount !== 1 ? 's' : ''}
            </span>
          </p>
        </div>

        <span className="docs-index-card__cta" aria-hidden>
          <ArrowUpRight size={18} strokeWidth={1.5} />
        </span>
      </Link>
    </li>
  )
}



export function DocsIndexPage() {
  useDocumentTitle('All Topics | CodeShelf')
  const topics = getTopics()
  const totalNotes = topics.reduce((sum, t) => sum + t.pages.length, 0)

  return (
    <div className="docs-index">
      <div className="docs-index__ambient" aria-hidden>
        <div className="docs-index__glow docs-index__glow--aloe" />
        <div className="docs-index__glow docs-index__glow--warm" />
        <div className="docs-index__mesh" />
      </div>

      <header className="docs-index__hero">
        <div className="docs-index__hero-rail" aria-hidden />
        <div className="docs-index__eyebrow">
          <span className="docs-index__eyebrow-dot" aria-hidden />
          <p className="text-eyebrow text-shade-50 mb-0">Documentation</p>
        </div>
        <h1 className="docs-index__title font-display text-display-lg text-ink">
          Choose your track
        </h1>
        <p className="docs-index__desc text-body-lg text-shade-50 max-w-2xl">
          Curated revision paths — open a course overview, then dive into structured notes
          whenever you need a quick refresh.
        </p>

        <div className="docs-index__stats">
          <div className="docs-index__stat">
            <Layers size={18} strokeWidth={1.5} className="docs-index__stat-icon" />
            <span>
              <strong>{topics.length}</strong> topics
            </span>
          </div>
          <div className="docs-index__stat">
            <BookOpen size={18} strokeWidth={1.5} className="docs-index__stat-icon" />
            <span>
              <strong>{totalNotes}</strong> notes
            </span>
          </div>
          <div className="docs-index__stat docs-index__stat--hint">
            <Search size={18} strokeWidth={1.5} className="docs-index__stat-icon" />
            <span>
              Press <kbd className="docs-index__kbd">Ctrl+K</kbd> to search
            </span>
          </div>
        </div>
      </header>

      <section className="docs-index__catalog" aria-labelledby="docs-index-catalog-title">
        <div className="docs-index__catalog-head">
          <h2 id="docs-index-catalog-title" className="docs-index__catalog-title font-display">
            All topics
          </h2>
          <p className="docs-index__catalog-sub text-caption text-shade-50">
            Select a stack to begin
          </p>
        </div>

        <ul className="docs-index__grid">
          {topics.map((topic, index) => (
            <DocsIndexCard
              key={topic.id}
              topicId={topic.id}
              label={topic.label}
              noteCount={topic.pages.length}
              index={index}
            />
          ))}
        </ul>
      </section>

      <aside className="docs-index__tip">
        <span className="docs-index__tip-border" aria-hidden />
        <p className="docs-index__tip-text text-body-md text-shade-50 mb-0">
          <span className="text-ink font-medium">Tip:</span> Each track starts with a course
          overview — use the sidebar to jump between chapters anytime.
        </p>
      </aside>
    </div>
  )
}
