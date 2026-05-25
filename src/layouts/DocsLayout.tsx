import { useEffect, useRef, useState, type RefObject } from 'react'
import { createPortal } from 'react-dom'
import { Outlet } from 'react-router-dom'
import { X } from 'lucide-react'
import { ReactLenis, useLenis } from 'lenis/react'
import { Sidebar } from '@/components/Sidebar'
import { DocsNavbar } from '@/components/DocsNavbar'
import { LenisScrollSetup } from '@/components/LenisScrollSetup'
import { ScrollToTop } from '@/components/ScrollToTop'
import { useIsTouchDevice } from '@/hooks/useIsTouchDevice'
import { useLenisScrolled } from '@/hooks/useLenisScrolled'
import { useMediaQuery } from '@/hooks/useMediaQuery'
import { usePrefersReducedMotion } from '@/hooks/usePrefersReducedMotion'
import { useElementScrolled } from '@/hooks/useScrolled'
import { useRegisterSearchNavigate } from '@/contexts/SearchUIContext'
import { useTheme } from '@/hooks/useTheme'
import { getLenisOptions } from '@/lib/lenisConfig'

function docsThemeClass(theme: 'light' | 'dark') {
  return theme === 'dark' ? 'dark' : ''
}

function defaultSidebarOpen() {
  if (typeof window === 'undefined') return true
  return window.matchMedia('(min-width: 1024px)').matches
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
      className="docs-main flex-1 min-w-0 min-h-0 overflow-y-auto overscroll-contain bg-canvas-cream"
    >
      <div className="w-full px-6 py-10 lg:px-10 xl:px-14 lg:py-14">{children}</div>
    </main>
  )
}

function DocsSidebarPanel({ open }: { open: boolean }) {
  return (
    <aside
      id="docs-sidebar"
      data-lenis-prevent
      aria-hidden={!open}
      className={[
        'docs-sidebar-panel',
        open ? 'docs-sidebar-panel--open' : 'docs-sidebar-panel--closed',
      ].join(' ')}
    >
      <div className="docs-sidebar-panel__inner">
        <Sidebar />
      </div>
    </aside>
  )
}

function DocsMobileSidebar({
  open,
  onClose,
  themeClass,
}: {
  open: boolean
  onClose: () => void
  themeClass: string
}) {
  useEffect(() => {
    if (!open) return
    const previous = document.body.style.overflow
    document.body.style.overflow = 'hidden'
    return () => {
      document.body.style.overflow = previous
    }
  }, [open])

  if (!open) return null

  return createPortal(
    <div
      className={['docs-mobile-sidebar lg:hidden', themeClass].filter(Boolean).join(' ')}
      role="dialog"
      aria-modal="true"
      aria-label="Navigation"
    >
      <button
        type="button"
        className="docs-mobile-sidebar__backdrop"
        onClick={onClose}
        aria-label="Close navigation"
      />
      <aside data-lenis-prevent className="docs-mobile-sidebar__panel">
        <div className="docs-mobile-sidebar__header">
          <span className="font-display text-ink">Navigation</span>
          <button
            type="button"
            onClick={onClose}
            className="docs-mobile-sidebar__close"
            aria-label="Close sidebar"
          >
            <X size={18} strokeWidth={1.5} />
          </button>
        </div>
        <Sidebar onNavigate={onClose} />
      </aside>
    </div>,
    document.body,
  )
}

function DocsLenisResizeOnSidebar({ sidebarOpen }: { sidebarOpen: boolean }) {
  const lenis = useLenis()

  useEffect(() => {
    if (!lenis) return
    const id = requestAnimationFrame(() => lenis.resize())
    return () => cancelAnimationFrame(id)
  }, [sidebarOpen, lenis])

  return null
}

function DocsLayoutShell({
  scrolled,
  main,
  lenisResize = false,
}: {
  scrolled: boolean
  main: React.ReactNode
  lenisResize?: boolean
}) {
  const isDesktop = useMediaQuery('(min-width: 1024px)')
  const [sidebarOpen, setSidebarOpen] = useState(defaultSidebarOpen)

  const toggleSidebar = () => setSidebarOpen((open) => !open)
  const closeSidebar = () => setSidebarOpen(false)

  useRegisterSearchNavigate(closeSidebar)

  const { theme } = useTheme()
  const themeClass = docsThemeClass(theme)

  const showDesktopSidebar = isDesktop && sidebarOpen
  const showMobileOverlay = !isDesktop && sidebarOpen

  return (
    <div
      className={[
        'track-light flex h-full min-h-0 flex-col overflow-hidden',
        showDesktopSidebar ? 'docs-layout--sidebar-open' : 'docs-layout--sidebar-closed',
      ].join(' ')}
    >
      {lenisResize && <DocsLenisResizeOnSidebar sidebarOpen={sidebarOpen} />}

      <DocsNavbar
        scrolled={scrolled}
        sidebarOpen={sidebarOpen}
        onToggleSidebar={toggleSidebar}
      />

      <DocsMobileSidebar
        open={showMobileOverlay}
        onClose={closeSidebar}
        themeClass={themeClass}
      />

      <div className="docs-layout__body flex min-h-0 flex-1">
        <DocsSidebarPanel open={showDesktopSidebar} />
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
        lenisResize
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
  const isTouch = useIsTouchDevice()
  const useNativeScroll = prefersReducedMotion || isTouch
  const { theme } = useTheme()
  const themeClass = docsThemeClass(theme)

  return (
    <div className={['track-light h-screen overflow-hidden', themeClass].filter(Boolean).join(' ')}>
      {useNativeScroll ? <DocsLayoutNativeScroll /> : <DocsLayoutSmooth />}
    </div>
  )
}
