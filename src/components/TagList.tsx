import { Link } from 'react-router-dom'
import { getAllTags } from '@/lib/content'

export function TagList() {
  const tags = getAllTags()

  if (tags.length === 0) return null

  return (
    <div className="px-4 py-6 border-t border-hairline-light mt-auto">
      <p className="text-eyebrow text-shade-50 mb-3 px-1">Tags</p>
      <div className="flex flex-wrap gap-1.5">
        {tags.map((tag) => (
          <Link
            key={tag}
            to={`/tags/${encodeURIComponent(tag)}`}
            className="text-eyebrow !normal-case px-3 py-1 rounded-pill bg-shade-30 text-shade-60 hover:bg-aloe hover:text-ink transition-colors"
          >
            #{tag}
          </Link>
        ))}
      </div>
    </div>
  )
}
