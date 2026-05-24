import { Search } from 'lucide-react'
import { useSearchUI } from '@/contexts/SearchUIContext'

interface SearchBarProps {
  variant?: 'default' | 'premium'
}

export function SearchBar({ variant = 'default' }: SearchBarProps) {
  const isPremium = variant === 'premium'
  const { openSearch } = useSearchUI()

  return (
    <div className={`w-full ${isPremium ? 'search-bar--premium' : ''}`}>
      <button
        type="button"
        onClick={openSearch}
        className={[
          'search-bar__trigger group relative w-full text-left',
          isPremium ? 'search-bar__trigger--premium' : 'search-bar__trigger--default',
        ].join(' ')}
        aria-label="Open search"
      >
        {isPremium && <span className="search-bar__border" aria-hidden />}
        <Search
          size={16}
          strokeWidth={1.5}
          className="search-bar__trigger-icon text-shade-40 pointer-events-none"
          aria-hidden
        />
        <span className="search-bar__trigger-placeholder text-shade-40">Search notes...</span>
        <kbd
          className={[
            'search-bar__kbd absolute right-3 top-1/2 z-[1] -translate-y-1/2 hidden sm:inline-flex',
            isPremium
              ? 'border border-black/8 bg-white/60 text-shade-50'
              : 'border border-hairline-light bg-shade-30/50 text-shade-50',
          ].join(' ')}
        >
          Ctrl+K
        </kbd>
      </button>
    </div>
  )
}
