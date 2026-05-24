import type { DocPage } from './types'

function escapeRegex(value: string): string {
  return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
}

function wordBoundaryRegex(term: string): RegExp {
  return new RegExp(`\\b${escapeRegex(term)}\\b`, 'i')
}

function scoreTerm(page: DocPage, term: string): number {
  const title = page.title.toLowerCase()
  const slug = page.slug.toLowerCase()
  const desc = (page.description ?? '').toLowerCase()
  const topic = page.topicLabel.toLowerCase()
  const content = page.content.toLowerCase()

  const inTitle = title.includes(term)
  const inSlug = slug.includes(term)
  const inDesc = desc.includes(term)
  const inTopic = topic.includes(term)
  const inContent = content.includes(term)

  if (!inTitle && !inSlug && !inDesc && !inTopic && !inContent) {
    return -1
  }

  let score = 0
  const boundary = wordBoundaryRegex(term)

  if (title === term) {
    score += 1200
  } else if (boundary.test(page.title)) {
    score += 800
  } else if (title.startsWith(term)) {
    score += 500
  } else if (inTitle) {
    score += 350
  }

  if (slug === term || slug.endsWith(`-${term}`) || slug.startsWith(`${term}-`)) {
    score += 450
  } else if (inSlug) {
    score += 180
  }

  if (page.description && boundary.test(page.description)) {
    score += 120
  } else if (inDesc) {
    score += 70
  }

  if (inTopic) {
    score += boundary.test(page.topicLabel) ? 60 : 35
  }

  if (inContent) {
    const titleOrSlugHit = inTitle || inSlug
    score += titleOrSlugHit ? 8 : 30
    const mentions = content.split(term).length - 1
    if (mentions > 8) score -= Math.min(20, mentions - 8)
  }

  return score
}

export function rankSearchPages(pages: DocPage[], query: string): DocPage[] {
  const q = query.toLowerCase().trim()
  if (!q) return []

  const terms = q.split(/\s+/).filter(Boolean)

  const ranked = pages
    .map((page) => {
      let score = 0
      for (const term of terms) {
        const termScore = scoreTerm(page, term)
        if (termScore < 0) return { page, score: -1 }
        score += termScore
      }

      const title = page.title.toLowerCase()
      const slug = page.slug.toLowerCase()

      if (title.includes(q)) score += 200
      if (slug.includes(q.replace(/\s+/g, '-'))) score += 150
      if (title === q) score += 300

      return { page, score }
    })
    .filter((entry) => entry.score >= 0)
    .sort((a, b) => {
      if (b.score !== a.score) return b.score - a.score
      return a.page.title.localeCompare(b.page.title)
    })

  return ranked.map((entry) => entry.page)
}
