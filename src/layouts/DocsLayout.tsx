import { useRef, useState, type RefObject } from 'react'
import { Link, Outlet } from 'react-router-dom'
import { Menu, X } from 'lucide-react'
import { ReactLenis } from 'lenis/react'
import { Sidebar } from '@/components/Sidebar'
import { SearchBar } from '@/components/SearchBar'
import { ButtonLink } from '@/components/ui/Button'
import { LenisScrollSetup } from '@/components/LenisScrollSetup'
import { ScrollToTop } from '@/components/ScrollToTop'
import { useLenisScrolled } from '@/hooks/useLenisScrolled'
import { usePrefersReducedMotion } from '@/hooks/usePrefersReducedMotion'
import { useElementScrolled } from '@/hooks/useScrolled'
import { getLenisOptions } from '@/lib/lenisConfig'

function DocsNavbar({
  scrolled,
  onOpenSidebar,
  onNavigate,
}: {
  scrolled: boolean
  onOpenSidebar: () => void
  onNavigate: () => void
}) {
  return (
    <header
      className={`navbar navbar--light shrink-0 z-40 border-b ${
        scrolled ? 'navbar--scrolled' : 'navbar--transparent'
      }`}
    >
      <div className="flex items-center gap-4 px-5 py-4 lg:px-8">
        <button
          onClick={onOpenSidebar}
          className="lg:hidden flex h-11 w-11 items-center justify-center rounded-pill border border-hairline-light text-shade-50 hover:bg-shade-30/40 transition-colors"
          aria-label="Open sidebar"
        >
          <Menu size={18} strokeWidth={1.5} />
        </button>

        <Link to="/" className="font-logo text-xl text-ink shrink-0">
          CodeShelf
        </Link>

        <div className="flex-1 flex justify-center max-w-xl mx-auto">
          <SearchBar onNavigate={onNavigate} />
        </div>

        <ButtonLink to="/" variant="outline-on-light" className="!py-2 !px-4 text-sm hidden sm:inline-flex">
          Home
        </ButtonLink>
      </div>
    </header>
  )
}

function DocsMain({
  children,
  scrollRef,
}: {
  children: React.ReactNode
  scrollRef?: RefObject<HTMLElement | null>
}) {
  return (
    <main
      ref={scrollRef}
      data-docs-scroll
      className="flex-1 min-w-0 min-h-0 overflow-y-auto overscroll-contain bg-canvas-cream"
    >
      <div className="w-full px-6 py-10 lg:px-10 xl:px-14 lg:py-14">{children}</div>
    </main>
  )
}

function DocsSidebarPanel() {
  return (
    <aside
      data-lenis-prevent
      className="hidden lg:flex w-72 shrink-0 min-h-0 flex-col border-r border-hairline-light bg-canvas-light overflow-y-auto overscroll-contain"
    >
      <Sidebar />
    </aside>
  )
}

function DocsLayoutShell({
  scrolled,
  main,
}: {
  scrolled: boolean
  main: React.ReactNode
}) {
  const [sidebarOpen, setSidebarOpen] = useState(false)
  const closeSidebar = () => setSidebarOpen(false)

  return (
    <div className="track-light flex h-full min-h-0 flex-col overflow-hidden">
      <DocsNavbar scrolled={scrolled} onOpenSidebar={() => setSidebarOpen(true)} onNavigate={closeSidebar} />

      <div className="flex min-h-0 flex-1">
        <DocsSidebarPanel />

        {sidebarOpen && (
          <div className="lg:hidden fixed inset-0 z-50 flex">
            <div className="absolute inset-0 bg-ink/40" onClick={closeSidebar} aria-hidden />
            <aside
              data-lenis-prevent
              className="relative flex w-80 max-w-[88vw] flex-col overflow-y-auto overscroll-contain border-r border-hairline-light bg-canvas-light shadow-card-light"
            >
              <div className="flex items-center justify-between border-b border-hairline-light px-5 py-4">
                <span className="font-display text-ink">Navigation</span>
                <button
                  onClick={closeSidebar}
                  className="flex h-9 w-9 items-center justify-center rounded-pill text-shade-50 hover:bg-shade-30/50"
                  aria-label="Close sidebar"
                >
                  <X size={18} strokeWidth={1.5} />
                </button>
              </div>
              <Sidebar onNavigate={closeSidebar} />
            </aside>
          </div>
        )}

        {main}
      </div>
    </div>
  )
}

function DocsLayoutSmooth() {
  const scrolled = useLenisScrolled(1)

  return (
    <>
      <LenisScrollSetup />
      <ScrollToTop />
      <DocsLayoutShell
        scrolled={scrolled}
        main={
          <ReactLenis
            root="asChild"
            className="flex min-h-0 min-w-0 flex-1 flex-col overflow-hidden"
            options={getLenisOptions()}
          >
            <DocsMain>
              <Outlet />
            </DocsMain>
          </ReactLenis>
        }
      />
    </>
  )
}

function DocsLayoutNativeScroll() {
  const mainRef = useRef<HTMLElement>(null)
  const scrolled = useElementScrolled(mainRef, 1)

  return (
    <>
      <ScrollToTop />
      <DocsLayoutShell
        scrolled={scrolled}
        main={
          <DocsMain scrollRef={mainRef}>
            <Outlet />
          </DocsMain>
        }
      />
    </>
  )
}

export function DocsLayout() {
  const prefersReducedMotion = usePrefersReducedMotion()

  return (
    <div className="track-light h-screen overflow-hidden">
      {prefersReducedMotion ? <DocsLayoutNativeScroll /> : <DocsLayoutSmooth />}
    </div>
  )
}
