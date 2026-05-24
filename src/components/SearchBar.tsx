import { useEffect, useRef } from 'react'
import { Link } from 'react-router-dom'
import { Search, X } from 'lucide-react'
import { useSearch } from '@/hooks/useSearch'

interface SearchBarProps {
  onNavigate?: () => void
  variant?: 'default' | 'premium'
}

export function SearchBar({ onNavigate, variant = 'default' }: SearchBarProps) {
  const isPremium = variant === 'premium'
  const { query, setQuery, results, hasQuery } = useSearch()
  const inputRef = useRef<HTMLInputElement>(null)
  const containerRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault()
        inputRef.current?.focus()
      }
      if (e.key === 'Escape') {
        setQuery('')
        inputRef.current?.blur()
      }
    }
    document.addEventListener('keydown', handleKeyDown)
    return () => document.removeEventListener('keydown', handleKeyDown)
  }, [setQuery])

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (containerRef.current && !containerRef.current.contains(e.target as Node)) {
        setQuery('')
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [setQuery])

  return (
    <div
      ref={containerRef}
      className={`relative w-full ${isPremium ? 'search-bar--premium' : ''}`}
    >
      <div className="relative">
        {isPremium && <span className="search-bar__border" aria-hidden />}
        <Search
          size={16}
          strokeWidth={1.5}
          className="absolute left-4 top-1/2 z-[1] -translate-y-1/2 text-shade-40 pointer-events-none"
        />
        <input
          ref={inputRef}
          type="search"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search notes..."
          className={
            isPremium
              ? 'search-bar__input w-full rounded-pill py-2.5 pl-11 pr-20 text-body-md text-ink placeholder:text-shade-40'
              : 'w-full rounded-md border border-hairline-light bg-canvas-light py-2.5 pl-11 pr-20 text-body-md text-ink placeholder:text-shade-40 focus:outline-none focus:ring-2 focus:ring-ink/10 focus:border-shade-40 transition-all'
          }
        />
        {query && (
          <button
            onClick={() => setQuery('')}
            className="absolute right-12 top-1/2 -translate-y-1/2 text-shade-40 hover:text-ink"
            aria-label="Clear search"
          >
            <X size={14} strokeWidth={1.5} />
          </button>
        )}
        <kbd
          className={`absolute right-3 top-1/2 z-[1] -translate-y-1/2 hidden sm:inline-flex items-center rounded-xs px-1.5 py-0.5 text-[10px] font-mono ${
            isPremium
              ? 'search-bar__kbd border border-black/8 bg-white/60 text-shade-50'
              : 'border border-hairline-light bg-shade-30/50 text-shade-50'
          }`}
        >
          Ctrl+K
        </kbd>
      </div>

      {hasQuery && (
        <div
          data-lenis-prevent
          className={`absolute top-full left-0 right-0 mt-2 z-50 overflow-hidden max-h-80 overflow-y-auto ${
            isPremium
              ? 'search-bar__dropdown rounded-xl border border-black/8 bg-white/95 shadow-[0_16px_48px_rgba(0,0,0,0.12)] backdrop-blur-xl'
              : 'rounded-lg border border-hairline-light bg-canvas-light shadow-card-light'
          }`}
        >
          {results.length === 0 ? (
            <p className="px-5 py-4 text-caption text-shade-50">No results found.</p>
          ) : (
            <ul>
              {results.map(({ page, snippet }) => (
                <li key={page.path}>
                  <Link
                    to={page.path}
                    onClick={() => {
                      setQuery('')
                      onNavigate?.()
                    }}
                    className="block px-5 py-4 hover:bg-canvas-cream transition-colors border-b border-hairline-light last:border-0"
                  >
                    <span className="text-eyebrow !normal-case text-shade-60 mb-1.5 block">
                      {page.topicLabel}
                    </span>
                    <p className="text-sm font-medium text-ink">{page.title}</p>
                    <p className="text-caption text-shade-50 mt-1 line-clamp-2">{snippet}</p>
                  </Link>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}
    </div>
  )
}
