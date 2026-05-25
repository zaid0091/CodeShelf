import { useState } from 'react'
import { NavLink, useLocation } from 'react-router-dom'
import { ChevronDown, Command, Sparkles } from 'lucide-react'
import { getTopics } from '@/lib/content'
import { TopicIcon } from '@/components/TopicIcon'
import { useSearchUI } from '@/contexts/SearchUIContext'

interface SidebarProps {
  onNavigate?: () => void
}

export function Sidebar({ onNavigate }: SidebarProps) {
  const topics = getTopics()
  const location = useLocation()
  const [collapsed, setCollapsed] = useState<Record<string, boolean>>({})
  const { openSearch } = useSearchUI()

  const totalNotes = topics.reduce((sum, t) => sum + t.pages.length, 0)

  const toggleTopic = (topicId: string) => {
    setCollapsed((prev) => ({ ...prev, [topicId]: !prev[topicId] }))
  }

  const isTopicActive = (topicId: string) =>
    location.pathname.startsWith(`/docs/${topicId}`)

  return (
    <div className="sidebar">
      <div className="sidebar__ambient" aria-hidden>
        <span className="sidebar__glow" />
        <span className="sidebar__beam" />
        <span className="sidebar__mesh" />
      </div>

      <header className="sidebar__header">
        <div className="sidebar__eyebrow">
          <Sparkles size={12} strokeWidth={1.5} className="sidebar__eyebrow-icon" aria-hidden />
          <span className="text-eyebrow">Library</span>
        </div>
        <p className="sidebar__title font-display">Documentation</p>
        <p className="sidebar__meta">
          <strong>{topics.length}</strong> tracks
          <span className="sidebar__meta-dot" aria-hidden />
          <strong>{totalNotes}</strong> notes
        </p>
      </header>

      <nav className="sidebar__nav" aria-label="Documentation">
        {topics.map((topic) => {
          const active = isTopicActive(topic.id)
          const isOpen =
            collapsed[topic.id] === undefined ? active : !collapsed[topic.id]

          return (
            <div
              key={topic.id}
              className={[
                'sidebar-topic',
                active ? 'sidebar-topic--active' : '',
                isOpen ? 'sidebar-topic--open' : '',
              ]
                .filter(Boolean)
                .join(' ')}
            >
              <button
                type="button"
                onClick={() => toggleTopic(topic.id)}
                className="sidebar-topic__btn"
                aria-expanded={isOpen}
              >
                <span className="sidebar-topic__rail" aria-hidden />
                <span className="sidebar-topic__icon-well" aria-hidden>
                  <TopicIcon topicId={topic.id} size={16} className="sidebar-topic__icon" />
                </span>
                <span className="sidebar-topic__label">{topic.label}</span>
                <span className="sidebar-topic__count" aria-hidden>
                  {topic.pages.length}
                </span>
                <ChevronDown
                  size={13}
                  strokeWidth={1.5}
                  className="sidebar-topic__chev"
                  aria-hidden
                />
              </button>

              <div
                className={[
                  'sidebar-pages-wrap',
                  isOpen ? 'sidebar-pages-wrap--open' : 'sidebar-pages-wrap--closed',
                ].join(' ')}
                aria-hidden={!isOpen}
              >
                <ul className="sidebar-pages">
                  <span className="sidebar-pages__rail" aria-hidden />
                  {topic.pages.map((page) => (
                    <li key={page.slug} className="sidebar-page-item">
                      <NavLink
                        to={page.path}
                        onClick={onNavigate}
                        className={({ isActive }) =>
                          [
                            'sidebar-page',
                            isActive ? 'sidebar-page--active' : '',
                          ]
                            .filter(Boolean)
                            .join(' ')
                        }
                      >
                        <span className="sidebar-page__dot" aria-hidden />
                        <span className="sidebar-page__title">{page.title}</span>
                      </NavLink>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          )
        })}
      </nav>

      <footer className="sidebar__foot">
        <button
          type="button"
          onClick={openSearch}
          className="sidebar__search-trigger"
          aria-label="Open search"
        >
          <Command size={13} strokeWidth={1.5} className="sidebar__search-icon" aria-hidden />
          <span className="sidebar__search-label">Quick search</span>
          <span className="sidebar__search-kbd">
            <kbd>Ctrl</kbd>
            <kbd>K</kbd>
          </span>
        </button>
      </footer>
    </div>
  )
}
