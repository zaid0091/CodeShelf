import { useCallback } from 'react'
import { ListTree } from 'lucide-react'
import { useLenis } from 'lenis/react'
import { useTableOfContents } from '@/hooks/useTableOfContents'

interface DocPageTocProps {
  contentKey: string
}

export function DocPageToc({ contentKey }: DocPageTocProps) {
  const { items, activeId, setActiveId } = useTableOfContents([contentKey])
  const lenis = useLenis()

  const onClick = useCallback(
    (event: React.MouseEvent<HTMLAnchorElement>, id: string) => {
      event.preventDefault()
      const target = document.getElementById(id)
      if (!target) return

      const scroller = document.querySelector<HTMLElement>('[data-docs-scroll]')

      if (lenis && scroller) {
        const offset = scroller.scrollTop + target.getBoundingClientRect().top -
          scroller.getBoundingClientRect().top - 80
        lenis.scrollTo(offset, { duration: 0.9 })
      } else if (scroller) {
        const offset = scroller.scrollTop + target.getBoundingClientRect().top -
          scroller.getBoundingClientRect().top - 80
        scroller.scrollTo({ top: offset, behavior: 'smooth' })
      } else {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' })
      }

      window.history.replaceState(null, '', `#${id}`)
      setActiveId(id)
    },
    [lenis, setActiveId],
  )

  if (items.length === 0) return null

  return (
    <aside className="doc-toc" aria-label="On this page">
      <div className="doc-toc__sticky">
        <header className="doc-toc__header">
          <ListTree size={14} strokeWidth={1.5} className="doc-toc__icon" aria-hidden />
          <span className="doc-toc__label">On this page</span>
        </header>

        <ol className="doc-toc__list">
          {items.map((item) => {
            const isActive = item.id === activeId
            return (
              <li
                key={item.id}
                className={[
                  'doc-toc__item',
                  item.level === 3 ? 'doc-toc__item--sub' : '',
                  isActive ? 'doc-toc__item--active' : '',
                ]
                  .filter(Boolean)
                  .join(' ')}
              >
                <a
                  href={`#${item.id}`}
                  className="doc-toc__link"
                  aria-current={isActive ? 'true' : undefined}
                  onClick={(e) => onClick(e, item.id)}
                >
                  <span className="doc-toc__link-rail" aria-hidden />
                  <span className="doc-toc__link-text">{item.text}</span>
                </a>
              </li>
            )
          })}
        </ol>
      </div>
    </aside>
  )
}
