import { Link } from 'react-router-dom'
import { ReactLenis } from 'lenis/react'
import { ArrowRight, Layers, Search, Zap, BookOpen, Code2, Sparkles } from 'lucide-react'
import { InstantSearchFeature } from '@/components/InstantSearchFeature'
import { getTopics } from '@/lib/content'
import { ButtonLink } from '@/components/ui/Button'
import { NavbarButtonLink } from '@/components/ui/NavbarButton'
import { TopicIcon } from '@/components/TopicIcon'
import { TopicsSection } from '@/components/TopicsSection'
import { SiteFooter } from '@/components/SiteFooter'
import { LenisScrollSetup } from '@/components/LenisScrollSetup'
import { ScrollReveal } from '@/components/ScrollReveal'
import { ScrollToTop } from '@/components/ScrollToTop'
import { useLenisScrolled } from '@/hooks/useLenisScrolled'
import { useIsTouchDevice } from '@/hooks/useIsTouchDevice'
import { usePrefersReducedMotion } from '@/hooks/usePrefersReducedMotion'
import { useWindowScrolled } from '@/hooks/useScrolled'
import { getLenisOptions } from '@/lib/lenisConfig'

function HomePageContent() {
  const topics = getTopics()
  const prefersReducedMotion = usePrefersReducedMotion()
  const lenisScrolled = useLenisScrolled(1)
  const windowScrolled = useWindowScrolled(1)
  const scrolled = prefersReducedMotion ? windowScrolled : lenisScrolled

  return (
    <div className="track-cinematic min-h-screen">
      <header
        className={`navbar navbar--dark fixed top-0 left-0 right-0 z-50 border-b transition-all duration-300 ${
          scrolled
            ? 'bg-neutral-950/45 border-white/10 backdrop-blur-xl'
            : 'bg-transparent border-transparent'
        }`}
      >
        <div className="max-w-[90rem] mx-auto px-4 sm:px-6 lg:px-10 py-4 sm:py-5 flex items-center justify-between gap-3 min-w-0">
          <Link
            to="/"
            className="flex items-center shrink-0"
          >
            <img
              src="/logo-light.png"
              alt="CodeShelf Logo"
              className="h-9 w-auto object-contain"
            />
          </Link>
          <div className="flex items-center gap-2 sm:gap-3 shrink-0">
            <NavbarButtonLink to="/docs" tone="dark">
              <span className="sm:hidden">Docs</span>
              <span className="hidden sm:inline">Browse docs</span>
            </NavbarButtonLink>
            <NavbarButtonLink
              to="/docs/drf/ch00-course-overview"
              tone="dark"
              emphasis="accent"
              className="hidden sm:inline-flex"
            >
              DRF course
            </NavbarButtonLink>
          </div>
        </div>
      </header>

      <section
        className="hero-section hero-section--advanced relative overflow-hidden border-b border-white/[0.06]"
        data-parallax-container
      >
        <div aria-hidden="true" className="hero-ambient">
          <div className="hero-mesh" data-parallax-speed="0.08" />
          <div className="hero-glow hero-glow--aloe" data-parallax-speed="0.18" />
          <div className="hero-glow hero-glow--cool" data-parallax-speed="0.12" />
          <div className="hero-glow hero-glow--accent" data-parallax-speed="0.22" />
          <div className="hero-grid" />
          <div className="hero-noise" />
          <div className="hero-beam" data-parallax-speed="0.05" />
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
                <ScrollReveal
                  as="h1"
                  animation="text-chars"
                  duration={1}
                  stagger={0.02}
                  delay={0.05}
                  start="top 95%"
                  className="hero-title font-display text-display-hero text-on-primary max-w-4xl mb-8"
                >
                  Your coding notes,
                  <br />
                  beautifully organized.
                </ScrollReveal>
              </div>
              <ScrollReveal
                as="p"
                animation="blur-in"
                delay={0.4}
                duration={0.9}
                start="top 95%"
                className="hero-desc text-body-lg text-link-cool-2 max-w-xl mb-12 leading-relaxed"
              >
                Quick revision for TypeScript, JavaScript, React, Python, Django, Django REST Framework, FastAPI, Web Security, and Design & Architecture.
              </ScrollReveal>
              <ScrollReveal
                animation="fade-up"
                delay={0.55}
                distance={20}
                duration={0.7}
                start="top 95%"
                className="hero-actions"
              >
                <ButtonLink
                  to="/docs"
                  variant="hero-cta"
                  className="!px-8 !py-3.5"
                >
                  Start learning
                  <ArrowRight size={18} strokeWidth={1.5} />
                </ButtonLink>
                <div className="hero-actions-glow" aria-hidden="true" />
              </ScrollReveal>
              <ScrollReveal
                animation="fade-up"
                delay={0.7}
                distance={14}
                duration={0.6}
                start="top 95%"
                className="hero-metrics"
                ariaHidden
              >
                {topics.map((topic) => (
                  <span key={topic.id} className="hero-metric">
                    <TopicIcon topicId={topic.id} size={18} />
                  </span>
                ))}
              </ScrollReveal>
            </div>

            <div aria-hidden="true" className="hero-visual hidden lg:block">
              <div className="hero-orbit hero-orbit--outer" data-parallax-speed="-0.04" />
              <div className="hero-orbit hero-orbit--inner" data-parallax-speed="-0.07" />
              {topics.slice(0, 4).map((topic, i) => (
                <div
                  key={topic.id}
                  className={`hero-float-badge hero-float-badge--${i + 1}`}
                  data-parallax-speed={(0.06 + i * 0.04).toString()}
                  data-parallax-rotate={(i % 2 === 0 ? -8 : 6).toString()}
                >
                  <TopicIcon topicId={topic.id} size={20} />
                </div>
              ))}
              <div className="hero-preview-stage">
                <div
                  className="hero-preview-float-wrap"
                  data-parallax-speed="-0.05"
                  data-parallax-rotate="-3"
                >
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

      <TopicsSection />

      <InstantSearchFeature />

      {/* ── Learning-path draw-on section ── */}
      <section
        className="learning-path-section"
        data-learning-path
        aria-label="Your learning journey"
      >
        <div className="learning-path-section__ambient" aria-hidden>
          <div className="learning-path-section__glow" />
        </div>

        <div className="learning-path-section__inner">
          <ScrollReveal
            animation="fade-up"
            duration={0.8}
            distance={22}
            start="top 88%"
            className="learning-path-section__header"
          >
            <div className="lp-eyebrow">
              <span className="lp-eyebrow__dot" aria-hidden />
              <p className="text-eyebrow text-link-cool-1 mb-0">Learning path</p>
            </div>
            <h2 className="font-display text-display-lg text-on-primary mt-3 mb-4">
              Go from zero to fluent.
            </h2>
            <p className="text-body-lg text-link-cool-2 max-w-lg mx-auto text-center">
              A structured path through every topic — so you always know what to learn next.
            </p>
          </ScrollReveal>

          {/* SVG path + milestone nodes */}
          <div className="lp-canvas" aria-hidden>
            <svg
              className="lp-svg"
              viewBox="0 0 900 420"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
              preserveAspectRatio="xMidYMid meet"
            >
              {/* Glowing track */}
              <path
                d="M 60 210 C 180 80 340 340 520 200 C 700 60 760 340 860 210"
                stroke="url(#lp-grad)"
                strokeWidth="2.5"
                strokeLinecap="round"
                data-path-draw
              />
              {/* Ghost track (dim) */}
              <path
                d="M 60 210 C 180 80 340 340 520 200 C 700 60 760 340 860 210"
                stroke="rgba(255,255,255,0.06)"
                strokeWidth="2.5"
                strokeLinecap="round"
              />
              <defs>
                <linearGradient id="lp-grad" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stopColor="#c1fbd4" />
                  <stop offset="50%" stopColor="#6ee7b7" />
                  <stop offset="100%" stopColor="#38bdf8" />
                </linearGradient>
              </defs>
            </svg>

            {/* Milestone nodes */}
            {[
              { x: '6.5%', y: '50%', Icon: BookOpen, label: 'Foundations' },
              { x: '33%', y: '16%', Icon: Code2, label: 'TypeScript' },
              { x: '57%', y: '52%', Icon: Layers, label: 'React' },
              { x: '84%', y: '20%', Icon: Zap, label: 'Django REST' },
              { x: '95%', y: '50%', Icon: Sparkles, label: 'Master' },
            ].map(({ x, y, Icon, label }) => (
              <div
                key={label}
                className="lp-node"
                style={{ left: x, top: y }}
                data-path-node
              >
                <span className="lp-node__ring" aria-hidden />
                <span className="lp-node__core">
                  <Icon size={14} strokeWidth={1.5} />
                </span>
                <span className="lp-node__label" data-path-label>
                  {label}
                </span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ── Feature showcase — 2-row grid ── */}
      <section
        className="showcase-section"
        data-showcase
        aria-label="Feature showcase"
      >
        <div className="showcase-section__inner">
          <ScrollReveal
            animation="fade-up"
            duration={0.8}
            distance={22}
            start="top 88%"
            className="text-center"
          >
            <div className="lp-eyebrow showcase-section__eyebrow">
              <span className="lp-eyebrow__dot" aria-hidden />
              <p className="text-eyebrow text-link-cool-1 mb-0">Features</p>
            </div>
            <h2 className="font-display text-display-lg text-on-primary mt-3 mb-2">
              Built for speed.
            </h2>
            <p className="text-body-lg text-link-cool-2 max-w-xl mx-auto mt-3 mb-0">
              Everything you need for fast, focused revision — right in your browser.
            </p>
          </ScrollReveal>

          <div className="showcase-grid">
            {/* Row 1 — 3 cards */}
            <div className="showcase-row showcase-row--top">
              {[
                {
                  icon: <Search size={26} strokeWidth={1.3} />,
                  title: 'Instant search',
                  body: 'Find any note across all topics in milliseconds — no server required.',
                  accent: '#c1fbd4',
                },
                {
                  icon: <Layers size={26} strokeWidth={1.3} />,
                  title: 'Curated tracks',
                  body: 'TypeScript · JavaScript · React · Python · Django · DRF — all in one place.',
                  accent: '#6ee7b7',
                },
                {
                  icon: <Code2 size={26} strokeWidth={1.3} />,
                  title: 'Syntax-highlighted code',
                  body: 'Every snippet rendered with rich syntax highlighting for fast scanning.',
                  accent: '#38bdf8',
                },
              ].map(({ icon, title, body, accent }, i) => (
                <ScrollReveal
                  key={title}
                  animation="tilt-in"
                  duration={0.95}
                  delay={0.05 + i * 0.08}
                  distance={36}
                  start="top 92%"
                >
                  <div
                    className="showcase-card"
                    style={{ '--card-accent': accent } as React.CSSProperties}
                  >
                    <span className="showcase-card__glow" aria-hidden />
                    <span className="showcase-card__border" aria-hidden />
                    <div className="showcase-card__icon-well">
                      <span style={{ color: accent }}>{icon}</span>
                    </div>
                    <h3 className="showcase-card__title font-display">{title}</h3>
                    <p className="showcase-card__body">{body}</p>
                  </div>
                </ScrollReveal>
              ))}
            </div>

            {/* Row 2 — 2 cards, centred */}
            <div className="showcase-row showcase-row--bottom">
              {[
                {
                  icon: <Zap size={26} strokeWidth={1.3} />,
                  title: 'Offline-ready',
                  body: 'Pure static site — no backend, no loading spinners, works anywhere.',
                  accent: '#818cf8',
                },
                {
                  icon: <BookOpen size={26} strokeWidth={1.3} />,
                  title: 'Structured chapters',
                  body: 'Notes grouped into chapters so revision feels like reading a real book.',
                  accent: '#fb7185',
                },
              ].map(({ icon, title, body, accent }, i) => (
                <ScrollReveal
                  key={title}
                  animation="tilt-in"
                  duration={0.95}
                  delay={0.05 + i * 0.08}
                  distance={36}
                  start="top 92%"
                >
                  <div
                    className="showcase-card"
                    style={{ '--card-accent': accent } as React.CSSProperties}
                  >
                    <span className="showcase-card__glow" aria-hidden />
                    <span className="showcase-card__border" aria-hidden />
                    <div className="showcase-card__icon-well">
                      <span style={{ color: accent }}>{icon}</span>
                    </div>
                    <h3 className="showcase-card__title font-display">{title}</h3>
                    <p className="showcase-card__body">{body}</p>
                  </div>
                </ScrollReveal>
              ))}
            </div>
          </div>
        </div>
      </section>

      <SiteFooter />
    </div>
  )
}

export function HomePage() {
  const prefersReducedMotion = usePrefersReducedMotion()
  const isTouch = useIsTouchDevice()

  if (prefersReducedMotion || isTouch) {
    return (
      <>
        <ScrollToTop />
        <HomePageContent />
      </>
    )
  }

  return (
    <ReactLenis root options={getLenisOptions()}>
      <LenisScrollSetup parallaxRoot />
      <ScrollToTop />
      <HomePageContent />
    </ReactLenis>
  )
}
