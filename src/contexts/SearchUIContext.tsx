import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useRef,
  useState,
  type ReactNode,
} from 'react'
import { SearchCommandPalette } from '@/components/SearchCommandPalette'

interface SearchUIContextValue {
  open: boolean
  openSearch: () => void
  closeSearch: () => void
  registerOnNavigate: (fn: () => void) => () => void
}

const SearchUIContext = createContext<SearchUIContextValue | null>(null)

export function SearchUIProvider({ children }: { children: ReactNode }) {
  const [open, setOpen] = useState(false)
  const navigateListeners = useRef(new Set<() => void>())

  const openSearch = useCallback(() => setOpen(true), [])
  const closeSearch = useCallback(() => setOpen(false), [])

  const registerOnNavigate = useCallback((fn: () => void) => {
    navigateListeners.current.add(fn)
    return () => {
      navigateListeners.current.delete(fn)
    }
  }, [])

  const notifyNavigate = useCallback(() => {
    navigateListeners.current.forEach((fn) => fn())
  }, [])

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault()
        setOpen((isOpen) => !isOpen)
      }
    }
    document.addEventListener('keydown', handleKeyDown)
    return () => document.removeEventListener('keydown', handleKeyDown)
  }, [])

  return (
    <SearchUIContext.Provider
      value={{ open, openSearch, closeSearch, registerOnNavigate }}
    >
      {children}
      <SearchCommandPalette
        open={open}
        onClose={closeSearch}
        onNavigate={notifyNavigate}
      />
    </SearchUIContext.Provider>
  )
}

export function useSearchUI() {
  const ctx = useContext(SearchUIContext)
  if (!ctx) {
    throw new Error('useSearchUI must be used within SearchUIProvider')
  }
  return ctx
}

export function useRegisterSearchNavigate(onNavigate: () => void) {
  const { registerOnNavigate } = useSearchUI()

  useEffect(() => registerOnNavigate(onNavigate), [onNavigate, registerOnNavigate])
}
