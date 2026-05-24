import { useEffect, useRef, useState } from 'react'
import { createPortal } from 'react-dom'
import { Link, useLocation, useNavigate } from 'react-router-dom'
import { useTheme } from '@/hooks/useTheme'
import { ArrowRight, FileText, Search, X } from 'lucide-react'
import { useSearch } from '@/hooks/useSearch'

interface SearchCommandPaletteProps {
  open: boolean
  onClose: () => void
  onNavigate?: () => void
}

export function SearchCommandPalette({
  open,
  onClose,
  onNavigate,
}: SearchCommandPaletteProps) {
  const { query, setQuery, results, hasQuery } = useSearch()
  const inputRef = useRef<HTMLInputElement>(null)
  const listRef = useRef<HTMLUListElement>(null)
  const [activeIndex, setActiveIndex] = useState(0)
  const navigate = useNavigate()
  const location = useLocation()
  const { theme } = useTheme()
  const isDocsRoute =
    location.pathname === '/docs' || location.pathname.startsWith('/docs/')
  const themeClass = isDocsRoute && theme === 'dark' ? 'dark' : ''

  useEffect(() => {
    if (!open) return
    setActiveIndex(0)
    const id = requestAnimationFrame(() => inputRef.current?.focus())
    return () => cancelAnimationFrame(id)
  }, [open])

  useEffect(() => {
    setActiveIndex(0)
  }, [query])

  useEffect(() => {
    if (!open) return
    const previous = document.body.style.overflow
    document.body.style.overflow = 'hidden'
    return () => {
      document.body.style.overflow = previous
    }
  }, [open])

  useEffect(() => {
    if (!open) {
      setQuery('')
      return
    }

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        e.preventDefault()
        onClose()
        return
      }

      if (!hasQuery || results.length === 0) return

      if (e.key === 'ArrowDown') {
        e.preventDefault()
        setActiveIndex((i) => (i + 1) % results.length)
      } else if (e.key === 'ArrowUp') {
        e.preventDefault()
        setActiveIndex((i) => (i - 1 + results.length) % results.length)
      } else if (e.key === 'Enter') {
        e.preventDefault()
        const hit = results[activeIndex]
        if (hit) {
          onClose()
          onNavigate?.()
          navigate(hit.page.path)
        }
      }
    }

    document.addEventListener('keydown', handleKeyDown)
    return () => document.removeEventListener('keydown', handleKeyDown)
  }, [open, hasQuery, results, activeIndex, onClose, onNavigate, navigate, setQuery])

  useEffect(() => {
    const list = listRef.current
    if (!list) return
    const active = list.querySelector<HTMLElement>('[data-active="true"]')
    active?.scrollIntoView({ block: 'nearest' })
  }, [activeIndex])

  if (!open) return null

  return createPortal(
    <div
      className={['search-palette', themeClass].filter(Boolean).join(' ')}
      role="dialog"
      aria-modal="true"
      aria-label="Search documentation"
    >
      <button
        type="button"
        className="search-palette__backdrop"
        onClick={onClose}
        aria-label="Close search"
      />

      <div className="search-palette__panel" data-lenis-prevent>
        <div className="search-palette__input-wrap">
          <Search
            size={20}
            strokeWidth={1.5}
            className="search-palette__icon text-shade-40"
            aria-hidden
          />
          <input
            ref={inputRef}
            type="search"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search notes, topics, chapters..."
            className="search-palette__input"
            autoComplete="off"
            autoCorrect="off"
            spellCheck={false}
            aria-controls="search-palette-results"
            aria-activedescendant={
              hasQuery && results[activeIndex]
                ? `search-result-${activeIndex}`
                : undefined
            }
          />
          {query ? (
            <button
              type="button"
              onClick={() => setQuery('')}
              className="search-palette__clear"
              aria-label="Clear search"
            >
              <X size={16} strokeWidth={1.5} />
            </button>
          ) : (
            <kbd className="search-palette__kbd">Esc</kbd>
          )}
        </div>

        <div className="search-palette__body">
          {!hasQuery ? (
            <p className="search-palette__hint">
              Type to search across all topics. Use <kbd>↑</kbd> <kbd>↓</kbd> to navigate,{' '}
              <kbd>Enter</kbd> to open.
            </p>
          ) : results.length === 0 ? (
            <p className="search-palette__empty">No results for &ldquo;{query}&rdquo;</p>
          ) : (
            <ul id="search-palette-results" ref={listRef} className="search-palette__results">
              {results.map(({ page, snippet }, index) => {
                const isActive = index === activeIndex
                return (
                  <li key={page.path}>
                    <Link
                      id={`search-result-${index}`}
                      to={page.path}
                      data-active={isActive}
                      className={[
                        'search-palette__result',
                        isActive ? 'search-palette__result--active' : '',
                      ].join(' ')}
                      onClick={() => {
                        onClose()
                        onNavigate?.()
                      }}
                      onMouseEnter={() => setActiveIndex(index)}
                    >
                      <span className="search-palette__result-icon" aria-hidden>
                        <FileText size={16} strokeWidth={1.5} />
                      </span>
                      <span className="search-palette__result-text min-w-0">
                        <span className="search-palette__result-meta">{page.topicLabel}</span>
                        <span className="search-palette__result-title font-display">{page.title}</span>
                        <span className="search-palette__result-snippet">{snippet}</span>
                      </span>
                      <ArrowRight
                        size={16}
                        strokeWidth={1.5}
                        className="search-palette__result-arrow shrink-0"
                        aria-hidden
                      />
                    </Link>
                  </li>
                )
              })}
            </ul>
          )}
        </div>

        <footer className="search-palette__footer">
          <span>
            <kbd>Ctrl</kbd> <kbd>K</kbd> toggle
          </span>
          <span>
            <kbd>↑</kbd> <kbd>↓</kbd> move
          </span>
          <span>
            <kbd>↵</kbd> open
          </span>
        </footer>
      </div>
    </div>,
    document.body,
  )
}
