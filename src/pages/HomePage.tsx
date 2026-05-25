import { Link } from 'react-router-dom'
import { ReactLenis } from 'lenis/react'
import { ArrowRight } from 'lucide-react'
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
        className={`navbar navbar--dark fixed top-0 left-0 right-0 z-50 border-b ${
          scrolled ? 'navbar--scrolled' : 'navbar--transparent'
        }`}
      >
        <div className="max-w-[90rem] mx-auto px-4 sm:px-6 lg:px-10 py-4 sm:py-5 flex items-center justify-between gap-3 min-w-0">
          <Link
            to="/"
            className="font-logo text-lg sm:text-xl text-on-primary shrink-0 min-w-0 truncate"
          >
            CodeShelf
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
                Quick revision for TypeScript, JavaScript, React, Python, Django, and Django REST Framework.
                No backend — just your notes, ready when you are.
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
