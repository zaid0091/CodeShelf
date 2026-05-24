import { Command, Search } from 'lucide-react'
import { useSearchUI } from '@/contexts/SearchUIContext'
import { ScrollReveal } from '@/components/ScrollReveal'
import { useSmoothCardGlow } from '@/hooks/useSmoothCardGlow'

export function InstantSearchFeature() {
  const { openSearch } = useSearchUI()
  const { cardRef, onPointerEnter, onPointerMove, onPointerLeave } =
    useSmoothCardGlow<HTMLElement>('search-feature--hover')

  return (
    <section className="search-feature" aria-labelledby="search-feature-title">
      <div className="search-feature__ambient" aria-hidden>
        <div className="search-feature__glow search-feature__glow--aloe" />
        <div className="search-feature__glow search-feature__glow--cool" />
        <div className="search-feature__mesh" />
        <div className="search-feature__beam-h" />
      </div>

      <div className="search-feature__inner">
        <ScrollReveal animation="fade-scale" duration={0.95} distance={28}>
          <article
            ref={cardRef}
            className="search-feature__card"
            onPointerEnter={onPointerEnter}
            onPointerMove={onPointerMove}
            onPointerLeave={onPointerLeave}
          >
            <span className="search-feature__border" aria-hidden />
            <span className="search-feature__spotlight" aria-hidden />
            <span className="search-feature__shine" aria-hidden />
            <span className="search-feature__noise" aria-hidden />
            <span className="search-feature__beam" aria-hidden />

            <div className="search-feature__layout">
              <div className="search-feature__main">
                <div className="search-feature__icon-well" aria-hidden>
                  <span className="search-feature__icon-ring" />
                  <Search size={22} strokeWidth={1.5} className="search-feature__icon" />
                </div>

                <div className="search-feature__copy">
                  <div className="search-feature__eyebrow">
                    <Command size={12} strokeWidth={1.5} aria-hidden />
                    <span className="text-eyebrow text-link-cool-1 mb-0">Command palette</span>
                  </div>

                  <h2 id="search-feature-title" className="search-feature__title font-display">
                    Instant search
                  </h2>

                  <p className="search-feature__desc text-caption text-link-cool-2">
                    Press{' '}
                    <span className="search-feature__kbd-group" aria-label="Control plus K">
                      <kbd className="search-feature__kbd">Ctrl</kbd>
                      <kbd className="search-feature__kbd search-feature__kbd--accent">K</kbd>
                    </span>{' '}
                    anywhere in the docs to jump across every note, topic, and chapter—in one
                    keystroke.
                  </p>

                  <div className="search-feature__chips" aria-hidden>
                    <span className="search-feature__chip">Fuzzy match</span>
                    <span className="search-feature__chip">Ranked results</span>
                    <span className="search-feature__chip">Keyboard first</span>
                  </div>

                  <button
                    type="button"
                    className="search-feature__cta"
                    onClick={(e) => {
                      e.stopPropagation()
                      openSearch()
                    }}
                  >
                    Try search now
                    <span className="search-feature__cta-kbd">Ctrl K</span>
                  </button>
                </div>
              </div>

              <div className="search-feature__preview" aria-hidden>
                <div className="search-feature__preview-panel">
                  <span className="search-feature__preview-border" />
                  <div className="search-feature__preview-bar">
                    <Search size={14} strokeWidth={1.5} className="text-link-cool-1" />
                    <span className="search-feature__preview-input">Search notes…</span>
                    <kbd className="search-feature__preview-kbd">Esc</kbd>
                  </div>
                  <ul className="search-feature__preview-results">
                    <li className="search-feature__preview-hit search-feature__preview-hit--active">
                      <span className="search-feature__preview-meta">DRF</span>
                      <span className="search-feature__preview-line">Pagination</span>
                    </li>
                    <li className="search-feature__preview-hit">
                      <span className="search-feature__preview-meta">Python</span>
                      <span className="search-feature__preview-line">Modules &amp; packages</span>
                    </li>
                    <li className="search-feature__preview-hit">
                      <span className="search-feature__preview-meta">React</span>
                      <span className="search-feature__preview-line">useEffect patterns</span>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </article>
        </ScrollReveal>
      </div>
    </section>
  )
}
