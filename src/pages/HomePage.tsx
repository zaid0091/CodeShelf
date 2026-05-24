import { Link } from 'react-router-dom'
import { ArrowRight, Search } from 'lucide-react'
import { getTopics, getAllTags, getCourseStartPath } from '@/lib/content'
import { ButtonLink } from '@/components/ui/Button'

export function HomePage() {
  const topics = getTopics()
  const tags = getAllTags()

  return (
    <div className="track-cinematic min-h-screen">
      <header className="sticky top-0 z-50 bg-canvas-night/80 backdrop-blur-md border-b border-white/5">
        <div className="max-w-[90rem] mx-auto px-6 lg:px-10 py-5 flex items-center justify-between">
          <Link to="/" className="font-display text-lg tracking-wide text-on-primary">
            CodeShelf
          </Link>
          <div className="flex items-center gap-3">
            <ButtonLink
              to="/docs/typescript/ch00-course-overview"
              variant="outline-on-dark"
              className="!py-2.5 !px-5 text-sm"
            >
              Browse docs
            </ButtonLink>
            <ButtonLink
              to="/docs/drf/ch00-course-overview"
              variant="outline-on-dark"
              className="!py-2.5 !px-5 text-sm hidden sm:inline-flex"
            >
              DRF course
            </ButtonLink>
          </div>
        </div>
      </header>

      <section className="max-w-[90rem] mx-auto px-6 lg:px-10 pt-24 pb-32 lg:pt-32 lg:pb-40">
        <p className="text-eyebrow text-link-cool-1 mb-8">Personal documentation</p>
        <h1 className="font-display text-display-hero text-on-primary max-w-4xl mb-8">
          Your coding notes,
          <br />
          beautifully organized.
        </h1>
        <p className="text-body-lg text-link-cool-2 max-w-xl mb-12 leading-relaxed">
          Quick revision for TypeScript, JavaScript, React, Python, Django, and Django REST Framework.
          No backend — just your notes, ready when you are.
        </p>
        <ButtonLink to="/docs/typescript/ch00-course-overview" variant="outline-on-dark">
          Start learning
          <ArrowRight size={18} strokeWidth={1.5} />
        </ButtonLink>
      </section>

      <section className="max-w-[90rem] mx-auto px-6 lg:px-10 pb-32">
        <p className="text-eyebrow text-link-cool-1 mb-4">Topics</p>
        <h2 className="font-display text-display-lg text-on-primary mb-16 max-w-2xl">
          Everything you need to revise.
        </h2>
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {topics.map((topic) => (
            <Link
              key={topic.id}
              to={getCourseStartPath(topic.id)}
              className="group relative bg-canvas-night-elevated border border-white/[0.08] rounded-xl p-8 transition-all duration-300 hover:border-white/15 hover:-translate-y-0.5"
              style={{
                boxShadow:
                  '0 1px 2px rgba(255,255,255,0.05), inset 0 1px 0 rgba(255,255,255,0.04)',
              }}
            >
              <span className="text-3xl mb-6 block">{topic.icon}</span>
              <h3 className="font-display text-2xl text-on-primary mb-2">{topic.label}</h3>
              <p className="text-caption text-link-cool-2">
                {topic.pages.length} note{topic.pages.length !== 1 ? 's' : ''}
              </p>
              <ArrowRight
                size={18}
                className="absolute bottom-8 right-8 text-link-cool-3 opacity-0 group-hover:opacity-100 transition-opacity"
                strokeWidth={1.5}
              />
            </Link>
          ))}
        </div>
      </section>

      {tags.length > 0 && (
        <section className="max-w-[90rem] mx-auto px-6 lg:px-10 pb-32">
          <p className="text-eyebrow text-link-cool-1 mb-4">Browse by tag</p>
          <div className="flex flex-wrap gap-2">
            {tags.slice(0, 20).map((tag) => (
              <Link
                key={tag}
                to={`/tags/${encodeURIComponent(tag)}`}
                className="text-eyebrow px-4 py-2 rounded-pill border border-white/20 text-on-primary hover:bg-white/5 transition-colors"
              >
                #{tag}
              </Link>
            ))}
          </div>
        </section>
      )}

      <section className="max-w-[90rem] mx-auto px-6 lg:px-10 pb-32">
        <div className="border border-white/[0.08] rounded-xl p-10 bg-canvas-night-elevated flex items-start gap-6">
          <Search size={22} className="text-link-cool-1 shrink-0 mt-1" strokeWidth={1.5} />
          <div>
            <h3 className="font-display text-xl text-on-primary mb-2">Instant search</h3>
            <p className="text-caption text-link-cool-2">
              Press{' '}
              <kbd className="px-2 py-0.5 rounded-md border border-white/15 bg-white/5 text-on-primary text-xs font-mono">
                Ctrl+K
              </kbd>{' '}
              anywhere in the docs to search across all your notes.
            </p>
          </div>
        </div>
      </section>

      <footer className="border-t border-white/5 py-16 px-6 lg:px-10">
        <div className="max-w-[90rem] mx-auto flex flex-col sm:flex-row items-start sm:items-center justify-between gap-6">
          <span className="font-display text-on-primary">CodeShelf</span>
          <p className="text-caption text-link-cool-3">
            Built for learning. Frontend-only. Always yours.
          </p>
        </div>
      </footer>
    </div>
  )
}
