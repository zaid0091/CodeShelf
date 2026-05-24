import { useMemo, useState } from 'react'
import { searchPages } from '@/lib/content'
import type { DocPage } from '@/lib/types'

export interface SearchHit {
  page: DocPage
  snippet: string
}

function buildSnippet(
  content: string,
  query: string,
  title?: string,
  description?: string,
): string {
  const q = query.toLowerCase()
  const sources = [
    { text: title ?? '', priority: 0 },
    { text: description ?? '', priority: 1 },
    { text: content, priority: 2 },
  ].sort((a, b) => a.priority - b.priority)

  for (const { text } of sources) {
    const lower = text.toLowerCase()
    const idx = lower.indexOf(q)
    if (idx === -1) continue

    const start = Math.max(0, idx - 40)
    const end = Math.min(text.length, idx + query.length + 80)
    const snippet = text.slice(start, end).replace(/\n/g, ' ')
    return (start > 0 ? '...' : '') + snippet + (end < text.length ? '...' : '')
  }

  return content.slice(0, 120).replace(/\n/g, ' ') + '...'
}

export function useSearch() {
  const [query, setQuery] = useState('')

  const results = useMemo<SearchHit[]>(() => {
    const q = query.trim()
    if (!q) return []
    return searchPages(q).slice(0, 10).map((page) => ({
      page,
      snippet: buildSnippet(page.content, q, page.title, page.description),
    }))
  }, [query])

  return { query, setQuery, results, hasQuery: query.trim().length > 0 }
}
