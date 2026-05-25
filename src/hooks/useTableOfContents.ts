import { useEffect, useState } from 'react'

export interface TocEntry {
  id: string
  text: string
  level: number
}

export function useTableOfContents(deps: ReadonlyArray<unknown> = []) {
  const [items, setItems] = useState<TocEntry[]>([])
  const [activeId, setActiveId] = useState<string | null>(null)

  useEffect(() => {
    const container = document.querySelector<HTMLElement>('.prose-docs')
    if (!container) {
      setItems([])
      setActiveId(null)
      return
    }

    const collect = () => {
      const nodes = Array.from(
        container.querySelectorAll<HTMLHeadingElement>('h2[id], h3[id]'),
      )
      const next = nodes.map((node) => ({
        id: node.id,
        text: node.textContent?.trim() ?? '',
        level: Number(node.tagName.slice(1)),
      }))
      setItems(next)
      if (next.length > 0) setActiveId((current) => current ?? next[0].id)
    }

    collect()

    const mutation = new MutationObserver(collect)
    mutation.observe(container, { childList: true, subtree: true })

    return () => {
      mutation.disconnect()
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps)

  useEffect(() => {
    if (items.length === 0) return

    const root = document.querySelector<HTMLElement>('[data-docs-scroll]')
    const headings = items
      .map((item) => document.getElementById(item.id))
      .filter((node): node is HTMLElement => node !== null)

    if (headings.length === 0) return

    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((a, b) => a.target.getBoundingClientRect().top - b.target.getBoundingClientRect().top)

        if (visible[0]) {
          setActiveId(visible[0].target.id)
          return
        }

        const above = headings
          .map((node) => ({ node, top: node.getBoundingClientRect().top }))
          .filter((entry) => entry.top < 120)
          .sort((a, b) => b.top - a.top)

        if (above[0]) setActiveId(above[0].node.id)
      },
      {
        root,
        rootMargin: '-96px 0px -65% 0px',
        threshold: [0, 1],
      },
    )

    headings.forEach((node) => observer.observe(node))
    return () => observer.disconnect()
  }, [items])

  return { items, activeId, setActiveId }
}
