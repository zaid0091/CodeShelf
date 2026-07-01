import { Link, useLocation, useParams } from 'react-router-dom'
import { ChevronRight, PanelLeftClose, PanelLeftOpen, Search } from 'lucide-react'
import { getPage, getCourseStartPath } from '@/lib/content'
import { SearchBar } from '@/components/SearchBar'
import { TopicIcon } from '@/components/TopicIcon'
import { DocsThemeToggle } from '@/components/DocsThemeToggle'
import { useTheme } from '@/hooks/useTheme'
import { useSearchUI } from '@/contexts/SearchUIContext'
import { NavbarButtonLink, NavbarIconButton } from '@/components/ui/NavbarButton'

interface DocsNavbarProps {
  scrolled: boolean
  sidebarOpen: boolean
  onToggleSidebar: () => void
}


function DocsBreadcrumb() {
  const location = useLocation()
  const { topic, slug } = useParams<{ topic?: string; slug?: string }>()
  const isDocsIndex =
    location.pathname === '/docs' || location.pathname === '/docs/'
  const isDashboard =
    location.pathname === '/dashboard' || location.pathname === '/dashboard/'

  if (isDashboard) {
    return (
      <nav className="docs-navbar__crumb" aria-label="Breadcrumb">
        <Link to="/dashboard" className="docs-navbar__crumb-link docs-navbar__crumb-link--current">
          <span className="docs-navbar__crumb-eyebrow text-eyebrow">Statistics</span>
          <span className="docs-navbar__crumb-title font-display">Dashboard</span>
        </Link>
      </nav>
    )
  }

  if (isDocsIndex) {
    return (
      <nav className="docs-navbar__crumb" aria-label="Breadcrumb">
        <Link to="/docs" className="docs-navbar__crumb-link docs-navbar__crumb-link--current">
          <span className="docs-navbar__crumb-eyebrow text-eyebrow">Documentation</span>
          <span className="docs-navbar__crumb-title font-display">All topics</span>
        </Link>
      </nav>
    )
  }

  if (!topic || !slug) return null

  const page = getPage(topic, slug)
  if (!page) return null

  const overviewPath = getCourseStartPath(topic)

  return (
    <nav className="docs-navbar__crumb" aria-label="Breadcrumb">
      <ol className="docs-navbar__crumb-list">
        <li className="docs-navbar__crumb-item docs-navbar__crumb-item--topic">
          <Link to={overviewPath} className="docs-navbar__crumb-link docs-navbar__crumb-link--topic min-w-0">
            <TopicIcon topicId={topic} size={18} className="docs-navbar__crumb-icon" />
            <span className="docs-navbar__crumb-topic truncate">{page.topicLabel}</span>
          </Link>
        </li>
        <li className="docs-navbar__crumb-sep" aria-hidden>
          <ChevronRight size={14} strokeWidth={1.5} />
        </li>
        <li className="docs-navbar__crumb-item docs-navbar__crumb-item--page min-w-0">
          <span className="docs-navbar__crumb-link docs-navbar__crumb-link--current min-w-0">
            <span className="docs-navbar__crumb-eyebrow text-eyebrow">Reading</span>
            <span className="docs-navbar__crumb-title font-display truncate">{page.title}</span>
          </span>
        </li>
      </ol>
    </nav>
  )
}

export function DocsNavbar({
  scrolled,
  sidebarOpen,
  onToggleSidebar,
}: DocsNavbarProps) {
  const { theme } = useTheme()
  const navTone = theme === 'dark' ? 'dark' : 'light'
  const { openSearch } = useSearchUI()

  return (
    <header
      className={[
        'docs-navbar',
        'navbar',
        'navbar--light',
        'navbar--premium-docs',
        'shrink-0',
        'z-60',
        'border-b',
        scrolled ? 'navbar--scrolled docs-navbar--scrolled' : 'navbar--transparent',
      ].join(' ')}
    >
      <span className="docs-navbar__beam" aria-hidden />
      <span className="docs-navbar__glow" aria-hidden />

      <div className="docs-navbar__inner">
        <div className="docs-navbar__start">
          <NavbarIconButton
            tone={navTone}
            onClick={(e) => {
              e.preventDefault()
              e.stopPropagation()
              onToggleSidebar()
            }}
            className="docs-navbar__menu-btn"
            aria-label={sidebarOpen ? 'Hide sidebar' : 'Show sidebar'}
            aria-expanded={sidebarOpen}
            aria-controls="docs-sidebar"
          >
            {sidebarOpen ? (
              <PanelLeftClose size={18} strokeWidth={1.5} />
            ) : (
              <PanelLeftOpen size={18} strokeWidth={1.5} />
            )}
          </NavbarIconButton>

          <Link to="/" className="docs-navbar__logo flex items-center">
            <img
              src={theme === 'dark' ? '/logo-light.png' : '/logo-dark.png'}
              alt="CodeShelf Logo"
              className="h-8 w-auto object-contain"
            />
          </Link>

          <span className="docs-navbar__divider" aria-hidden />

          <div className="docs-navbar__crumb-wrap">
            <DocsBreadcrumb />
          </div>
        </div>

        <div className="docs-navbar__search">
          <SearchBar variant="premium" />
        </div>

        <div className="docs-navbar__actions">
          <NavbarIconButton
            tone={navTone}
            onClick={openSearch}
            className="docs-navbar__mobile-search"
            aria-label="Open search"
          >
            <Search size={18} strokeWidth={1.5} />
          </NavbarIconButton>
          <NavbarButtonLink
            to="/dashboard"
            tone={navTone}
            emphasis="default"
            className="docs-navbar__dashboard mr-2"
          >
            Dashboard
          </NavbarButtonLink>
          <DocsThemeToggle />
          <NavbarButtonLink
            to="/"
            tone={navTone}
            emphasis="accent"
            className="docs-navbar__home"
          >
            Home
          </NavbarButtonLink>
        </div>
      </div>

      <div className="docs-navbar__mobile-crumb">
        <DocsBreadcrumb />
      </div>
    </header>
  )
}
