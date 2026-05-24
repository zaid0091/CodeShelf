import { parseFrontmatter } from './frontmatter'
import type { DocPage, TopicGroup } from './types'

const TOPIC_LABELS: Record<string, { label: string; icon: string }> = {
  typescript: { label: 'TypeScript', icon: 'TS' },
  javascript: { label: 'JavaScript', icon: 'JS' },
  react: { label: 'React', icon: '⚛' },
  python: { label: 'Python', icon: '🐍' },
  django: { label: 'Django', icon: '🎸' },
  drf: { label: 'Django REST Framework', icon: '🔌' },
}

const modules = import.meta.glob('../../content/**/*.md', {
  query: '?raw',
  import: 'default',
  eager: true,
}) as Record<string, string>

function parseDocPath(filePath: string): { topic: string; slug: string } {
  const normalized = filePath.replace(/\\/g, '/')
  const match = normalized.match(/content\/([^/]+)\/([^/]+)\.md$/)
  if (!match) throw new Error(`Invalid content path: ${filePath}`)
  return { topic: match[1], slug: match[2] }
}

function buildPages(): DocPage[] {
  return Object.entries(modules).map(([path, raw]) => {
    const { topic, slug } = parseDocPath(path)
    const { data, content } = parseFrontmatter(raw)
    const meta = TOPIC_LABELS[topic] ?? { label: topic, icon: '📄' }

    return {
      slug,
      topic,
      topicLabel: meta.label,
      title: (data.title as string) ?? slug,
      description: data.description as string | undefined,
      order: (data.order as number) ?? 99,
      tags: (data.tags as string[]) ?? [],
      content: content.trim(),
      path: `/docs/${topic}/${slug}`,
    }
  })
}

const allPages = buildPages()

export function getAllPages(): DocPage[] {
  return [...allPages].sort((a, b) => {
    if (a.topic !== b.topic) return a.topic.localeCompare(b.topic)
    return a.order - b.order
  })
}

export function getTopics(): TopicGroup[] {
  const pages = getAllPages()
  const topicMap = new Map<string, DocPage[]>()

  for (const page of pages) {
    const existing = topicMap.get(page.topic) ?? []
    existing.push(page)
    topicMap.set(page.topic, existing)
  }

  return Array.from(topicMap.entries()).map(([id, topicPages]) => {
    const meta = TOPIC_LABELS[id] ?? { label: id, icon: '📄' }
    return {
      id,
      label: meta.label,
      icon: meta.icon,
      pages: topicPages.sort((a, b) => a.order - b.order),
    }
  })
}

export function getPage(topic: string, slug: string): DocPage | undefined {
  return allPages.find((p) => p.topic === topic && p.slug === slug)
}

export function getAllTags(): string[] {
  const tags = new Set<string>()
  for (const page of allPages) {
    for (const tag of page.tags) tags.add(tag)
  }
  return [...tags].sort()
}

export function getPagesByTag(tag: string): DocPage[] {
  return allPages.filter((p) => p.tags.includes(tag))
}

export function searchPages(query: string): DocPage[] {
  const q = query.toLowerCase().trim()
  if (!q) return []

  return allPages.filter((page) => {
    const haystack = [
      page.title,
      page.description ?? '',
      page.topicLabel,
      page.tags.join(' '),
      page.content,
    ]
      .join(' ')
      .toLowerCase()
    return haystack.includes(q)
  })
}
