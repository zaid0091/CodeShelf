import { useState } from 'react'
import { NavLink, useLocation } from 'react-router-dom'
import { ChevronDown, ChevronRight } from 'lucide-react'
import { getTopics } from '@/lib/content'

interface SidebarProps {
  onNavigate?: () => void
}

export function Sidebar({ onNavigate }: SidebarProps) {
  const topics = getTopics()
  const location = useLocation()
  const [collapsed, setCollapsed] = useState<Record<string, boolean>>({})

  const toggleTopic = (topicId: string) => {
    setCollapsed((prev) => ({ ...prev, [topicId]: !prev[topicId] }))
  }

  const isTopicActive = (topicId: string) =>
    location.pathname.startsWith(`/docs/${topicId}`)

  return (
    <nav className="flex flex-col gap-0.5 py-6 px-4">
      {topics.map((topic) => {
        const isOpen =
          collapsed[topic.id] === undefined ? isTopicActive(topic.id) : !collapsed[topic.id]

        return (
          <div key={topic.id} className="mb-2">
            <button
              onClick={() => toggleTopic(topic.id)}
              className={`flex w-full items-center gap-2.5 rounded-lg px-3 py-2.5 text-sm font-medium transition-colors ${
                isTopicActive(topic.id)
                  ? 'text-ink bg-aloe/40'
                  : 'text-shade-60 hover:text-ink hover:bg-shade-30/50'
              }`}
            >
              <span className="text-base leading-none">{topic.icon}</span>
              <span className="flex-1 text-left">{topic.label}</span>
              {isOpen ? (
                <ChevronDown size={14} strokeWidth={1.5} />
              ) : (
                <ChevronRight size={14} strokeWidth={1.5} />
              )}
            </button>

            {isOpen && (
              <ul className="mt-1 ml-4 pl-3 border-l border-hairline-light space-y-0.5">
                {topic.pages.map((page) => (
                  <li key={page.slug}>
                    <NavLink
                      to={page.path}
                      onClick={onNavigate}
                      className={({ isActive }) =>
                        `block rounded-pill px-3 py-2 text-sm transition-all duration-150 ${
                          isActive
                            ? 'bg-ink text-on-primary font-medium'
                            : 'text-shade-50 hover:text-ink hover:bg-shade-30/40'
                        }`
                      }
                    >
                      {page.title}
                    </NavLink>
                  </li>
                ))}
              </ul>
            )}
          </div>
        )
      })}
    </nav>
  )
}
