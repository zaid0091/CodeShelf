import { useMemo, useState } from 'react'
import { searchPages } from '@/lib/content'
import type { DocPage } from '@/lib/types'

export interface SearchHit {
  page: DocPage
  snippet: string
}

function buildSnippet(content: string, query: string): string {
  const lower = content.toLowerCase()
  const idx = lower.indexOf(query.toLowerCase())
  if (idx === -1) return content.slice(0, 120) + '...'

  const start = Math.max(0, idx - 40)
  const end = Math.min(content.length, idx + query.length + 80)
  const snippet = content.slice(start, end).replace(/\n/g, ' ')
  return (start > 0 ? '...' : '') + snippet + (end < content.length ? '...' : '')
}

export function useSearch() {
  const [query, setQuery] = useState('')

  const results = useMemo<SearchHit[]>(() => {
    const q = query.trim()
    if (!q) return []
    return searchPages(q).slice(0, 12).map((page) => ({
      page,
      snippet: buildSnippet(page.content, q),
    }))
  }, [query])

  return { query, setQuery, results, hasQuery: query.trim().length > 0 }
}
