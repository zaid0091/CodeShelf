import { Link, useParams } from 'react-router-dom'
import { getPagesByTag } from '@/lib/content'
import { NotFoundPage } from './NotFoundPage'

export function TagPage() {
  const { tag } = useParams<{ tag: string }>()
  const decodedTag = tag ? decodeURIComponent(tag) : ''
  const pages = decodedTag ? getPagesByTag(decodedTag) : []

  if (!decodedTag || pages.length === 0) return <NotFoundPage />

  return (
    <div>
      <header className="mb-12">
        <p className="text-eyebrow text-shade-50 mb-3">Tagged notes</p>
        <h1 className="font-display text-display-lg text-ink">#{decodedTag}</h1>
        <p className="text-body-lg text-shade-50 mt-4">
          {pages.length} note{pages.length !== 1 ? 's' : ''} tagged with{' '}
          <span className="text-ink font-medium">#{decodedTag}</span>
        </p>
      </header>

      <ul className="space-y-4">
        {pages.map((page) => (
          <li key={page.path}>
            <Link
              to={page.path}
              className="block rounded-lg border border-hairline-light bg-canvas-light p-6 shadow-card-light hover:-translate-y-0.5 transition-all duration-200"
            >
              <span className="text-eyebrow !normal-case text-shade-50">{page.topicLabel}</span>
              <h2 className="font-display text-xl text-ink mt-2">{page.title}</h2>
              {page.description && (
                <p className="text-caption text-shade-50 mt-2">{page.description}</p>
              )}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  )
}
