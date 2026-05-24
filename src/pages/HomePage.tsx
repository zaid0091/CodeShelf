import { Link } from 'react-router-dom'
import { ArrowRight, Search } from 'lucide-react'
import { getTopics, getCourseStartPath } from '@/lib/content'
import { ButtonLink } from '@/components/ui/Button'
import { TopicIcon } from '@/components/TopicIcon'
import { useWindowScrolled } from '@/hooks/useScrolled'

export function HomePage() {
  const topics = getTopics()
  const scrolled = useWindowScrolled(1)

  return (
    <div className="track-cinematic min-h-screen">
      <header
        className={`navbar navbar--dark fixed top-0 left-0 right-0 z-50 border-b ${
          scrolled ? 'navbar--scrolled' : 'navbar--transparent'
        }`}
      >
        <div className="max-w-[90rem] mx-auto px-6 lg:px-10 py-5 flex items-center justify-between">
          <Link to="/" className="font-logo text-xl text-on-primary">
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

      <section className="hero-section hero-section--advanced relative overflow-hidden border-b border-white/[0.06]">
        <div aria-hidden="true" className="hero-ambient">
          <div className="hero-mesh" />
          <div className="hero-glow hero-glow--aloe" />
          <div className="hero-glow hero-glow--cool" />
          <div className="hero-glow hero-glow--accent" />
          <div className="hero-grid" />
          <div className="hero-noise" />
          <div className="hero-beam" />
          <div className="hero-vignette" />
        </div>

        <div className="hero-inner relative z-10 max-w-[90rem] mx-auto px-6 lg:px-10 w-full">
          <div className="grid lg:grid-cols-[minmax(0,1.05fr)_minmax(300px,440px)] xl:grid-cols-[minmax(0,1fr)_460px] gap-16 xl:gap-20 items-start lg:items-center">
            <div className="hero-copy min-w-0">
              <div className="hero-copy-rail" aria-hidden="true" />
              <div className="hero-eyebrow">
                <span className="hero-eyebrow-shine" aria-hidden="true" />
                <span className="hero-eyebrow-dot" />
                <p className="text-eyebrow text-link-cool-1 mb-0">Personal documentation</p>
              </div>
              <div className="hero-title-wrap">
                <h1 className="hero-title font-display text-display-hero text-on-primary max-w-4xl mb-8">
                  Your coding notes,
                  <br />
                  beautifully organized.
                </h1>
              </div>
              <p className="hero-desc text-body-lg text-link-cool-2 max-w-xl mb-12 leading-relaxed">
                Quick revision for TypeScript, JavaScript, React, Python, Django, and Django REST Framework.
                No backend — just your notes, ready when you are.
              </p>
              <div className="hero-actions">
                <ButtonLink
                  to="/docs/typescript/ch00-course-overview"
                  variant="hero-cta"
                  className="!px-8 !py-3.5"
                >
                  Start learning
                  <ArrowRight size={18} strokeWidth={1.5} />
                </ButtonLink>
                <div className="hero-actions-glow" aria-hidden="true" />
              </div>
              <div className="hero-metrics" aria-hidden="true">
                {topics.map((topic) => (
                  <span key={topic.id} className="hero-metric">
                    <TopicIcon topicId={topic.id} size={18} />
                  </span>
                ))}
              </div>
            </div>

            <div aria-hidden="true" className="hero-visual hidden lg:block">
              <div className="hero-orbit hero-orbit--outer" />
              <div className="hero-orbit hero-orbit--inner" />
              {topics.slice(0, 4).map((topic, i) => (
                <div key={topic.id} className={`hero-float-badge hero-float-badge--${i + 1}`}>
                  <TopicIcon topicId={topic.id} size={20} />
                </div>
              ))}
              <div className="hero-preview-stage">
                <div className="hero-preview-float-wrap">
                  <div className="hero-preview">
                    <div className="hero-preview-glow" />
                    <div className="hero-preview-card hero-preview-card--back" />
                    <div className="hero-preview-card hero-preview-card--mid" />
                    <div className="hero-preview-card hero-preview-card--front">
                      <div className="hero-preview-shine" />
                      <div className="hero-preview-chrome">
                        <span className="hero-preview-dot hero-preview-dot--red" />
                        <span className="hero-preview-dot hero-preview-dot--amber" />
                        <span className="hero-preview-dot hero-preview-dot--green" />
                        <span className="hero-preview-url" />
                      </div>
                      <div className="hero-preview-body">
                        <div className="hero-preview-sidebar">
                          <div className="hero-preview-search" />
                          <div className="hero-preview-sidebar-title" />
                          {topics.slice(0, 5).map((topic, index) => (
                            <div
                              key={topic.id}
                              className={`hero-preview-nav-item${index === 0 ? ' hero-preview-nav-item--active' : ''}`}
                            >
                              <TopicIcon topicId={topic.id} size={14} className="hero-preview-nav-icon" />
                              <span className="hero-preview-nav-line" />
                            </div>
                          ))}
                        </div>
                        <div className="hero-preview-main">
                          <div className="hero-preview-accent" />
                          <div className="hero-preview-line hero-preview-line--lg" />
                          <div className="hero-preview-line hero-preview-line--md" />
                          <div className="hero-preview-line hero-preview-line--sm" />
                          <div className="hero-preview-code">
                            <div className="hero-preview-code-line hero-preview-code-line--kw" />
                            <div className="hero-preview-code-line" />
                            <div className="hero-preview-code-line hero-preview-code-line--short" />
                            <div className="hero-preview-code-line hero-preview-code-line--accent" />
                            <span className="hero-preview-cursor" />
                          </div>
                        </div>
                      </div>
                    </div>
                    <div className="hero-preview-scanline" />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="hero-floor" aria-hidden="true">
          <div className="hero-floor-line" />
        </div>
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
              <TopicIcon topicId={topic.id} size={40} className="mb-6" />
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
