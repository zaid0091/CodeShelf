import { useState } from 'react'
import { Link, Outlet } from 'react-router-dom'
import { Menu, X } from 'lucide-react'
import { Sidebar } from '@/components/Sidebar'
import { SearchBar } from '@/components/SearchBar'
import { TagList } from '@/components/TagList'
import { ButtonLink } from '@/components/ui/Button'

export function DocsLayout() {
  const [sidebarOpen, setSidebarOpen] = useState(false)
  const closeSidebar = () => setSidebarOpen(false)

  return (
    <div className="track-light h-screen flex flex-col overflow-hidden">
      <header className="shrink-0 z-40 bg-canvas-light/90 backdrop-blur-md border-b border-hairline-light">
        <div className="flex items-center gap-4 px-5 py-4 lg:px-8">
          <button
            onClick={() => setSidebarOpen(true)}
            className="lg:hidden flex h-11 w-11 items-center justify-center rounded-pill border border-hairline-light text-shade-50 hover:bg-shade-30/40 transition-colors"
            aria-label="Open sidebar"
          >
            <Menu size={18} strokeWidth={1.5} />
          </button>

          <Link to="/" className="font-display text-lg text-ink shrink-0 tracking-wide">
            CodeShelf
          </Link>

          <div className="flex-1 flex justify-center max-w-xl mx-auto">
            <SearchBar onNavigate={closeSidebar} />
          </div>

          <ButtonLink to="/" variant="outline-on-light" className="!py-2 !px-4 text-sm hidden sm:inline-flex">
            Home
          </ButtonLink>
        </div>
      </header>

      <div className="flex flex-1 min-h-0 overflow-hidden">
        <aside className="hidden lg:flex w-72 shrink-0 flex-col bg-canvas-light border-r border-hairline-light overflow-y-auto">
          <Sidebar />
          <TagList />
        </aside>

        {sidebarOpen && (
          <div className="lg:hidden fixed inset-0 z-50 flex">
            <div className="absolute inset-0 bg-ink/40" onClick={closeSidebar} aria-hidden />
            <aside className="relative w-80 max-w-[88vw] flex flex-col bg-canvas-light border-r border-hairline-light overflow-y-auto shadow-card-light">
              <div className="flex items-center justify-between px-5 py-4 border-b border-hairline-light">
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
              <TagList />
            </aside>
          </div>
        )}

        <main className="flex-1 min-h-0 overflow-y-auto bg-canvas-cream w-full">
          <div className="w-full px-6 py-10 lg:px-10 xl:px-14 lg:py-14">
            <Outlet />
          </div>
        </main>
      </div>
    </div>
  )
}

