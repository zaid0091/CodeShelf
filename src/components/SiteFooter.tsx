import { Link } from 'react-router-dom'
import { ArrowUpRight, GitBranch } from 'lucide-react'
import { getTopics, getCourseStartPath } from '@/lib/content'
import { TopicIcon } from '@/components/TopicIcon'
import { NavbarButtonLink } from '@/components/ui/NavbarButton'
import { ScrollReveal } from '@/components/ScrollReveal'

const GITHUB_URL = 'https://github.com/zaid0091/CodeShelf'

export function SiteFooter() {
  const topics = getTopics()
  const year = new Date().getFullYear()

  return (
    <footer className="site-footer">
      <div className="site-footer__ambient" aria-hidden>
        <div className="site-footer__glow site-footer__glow--aloe" />
        <div className="site-footer__glow site-footer__glow--cool" />
        <div className="site-footer__grid" />
      </div>

      <div className="site-footer__beam" aria-hidden />

      <ScrollReveal animation="fade-up" duration={0.95} distance={32}>
        <div className="site-footer__inner">
          <div className="site-footer__panel">
            <span className="site-footer__panel-border" aria-hidden />
            <span className="site-footer__panel-shine" aria-hidden />

            <div className="site-footer__main">
              <div className="site-footer__brand">
                <div className="site-footer__brand-rail" aria-hidden />
                <Link to="/" className="site-footer__logo font-logo">
                  CodeShelf
                </Link>
                <p className="site-footer__tagline text-body-lg text-link-cool-2">
                  Personal notes for fast revision — TypeScript to Django REST Framework,
                  beautifully organized and always offline-ready.
                </p>
                <div className="site-footer__topic-strip" aria-label="Topics">
                  {topics.map((topic) => (
                    <Link
                      key={topic.id}
                      to={getCourseStartPath(topic.id)}
                      className="site-footer__topic-chip"
                      title={topic.label}
                    >
                      <TopicIcon topicId={topic.id} size={18} />
                    </Link>
                  ))}
                </div>
                <NavbarButtonLink
                  to="/docs"
                  tone="dark"
                  emphasis="accent"
                  className="site-footer__cta"
                >
                  Start learning
                  <ArrowUpRight size={16} strokeWidth={1.5} />
                </NavbarButtonLink>
              </div>

              <div className="site-footer__nav">
                <div className="site-footer__col">
                  <p className="site-footer__col-title text-eyebrow text-link-cool-1">
                    Topics
                  </p>
                  <ul className="site-footer__links">
                    {topics.map((topic) => (
                      <li key={topic.id}>
                        <Link to={getCourseStartPath(topic.id)} className="site-footer__link">
                          <TopicIcon topicId={topic.id} size={16} className="site-footer__link-icon" />
                          <span>{topic.label}</span>
                          <ArrowUpRight
                            size={14}
                            strokeWidth={1.5}
                            className="site-footer__link-arrow"
                            aria-hidden
                          />
                        </Link>
                      </li>
                    ))}
                  </ul>
                </div>

                <div className="site-footer__col">
                  <p className="site-footer__col-title text-eyebrow text-link-cool-1">
                    Explore
                  </p>
                  <ul className="site-footer__links">
                    <li>
                      <Link to="/docs/typescript/ch00-course-overview" className="site-footer__link">
                        <span>Browse all docs</span>
                        <ArrowUpRight size={14} strokeWidth={1.5} className="site-footer__link-arrow" aria-hidden />
                      </Link>
                    </li>
                    <li>
                      <Link to="/docs/drf/ch00-course-overview" className="site-footer__link">
                        <span>DRF course</span>
                        <ArrowUpRight size={14} strokeWidth={1.5} className="site-footer__link-arrow" aria-hidden />
                      </Link>
                    </li>
                    <li>
                      <span className="site-footer__link site-footer__link--static">
                        <span>Search</span>
                        <kbd className="site-footer__kbd">Ctrl+K</kbd>
                      </span>
                    </li>
                  </ul>
                </div>
              </div>
            </div>

            <div className="site-footer__divider" aria-hidden />

            <div className="site-footer__bottom">
              <p className="site-footer__copyright text-caption text-link-cool-3">
                © {year} CodeShelf · Built for learning · Frontend-only · Always yours
              </p>
              <a
                href={GITHUB_URL}
                target="_blank"
                rel="noopener noreferrer"
                className="site-footer__github"
              >
                <GitBranch size={16} strokeWidth={1.5} />
                <span>View on GitHub</span>
                <ArrowUpRight size={14} strokeWidth={1.5} aria-hidden />
              </a>
            </div>
          </div>
        </div>
      </ScrollReveal>

      <div className="site-footer__wordmark" aria-hidden>
        <span className="site-footer__wordmark-text font-logo">CodeShelf</span>
      </div>

      <div className="site-footer__floor" aria-hidden>
        <div className="site-footer__floor-line" />
      </div>
    </footer>
  )
}
