import { parseFrontmatter } from './frontmatter'
import { rankSearchPages } from './searchRank'
import type { DocPage, TopicGroup } from './types'

const TOPIC_LABELS: Record<string, { label: string }> = {
  typescript: { label: 'TypeScript' },
  javascript: { label: 'JavaScript' },
  react: { label: 'React' },
  nextjs: { label: 'Next.js' },
  python: { label: 'Python' },
  django: { label: 'Django' },
  drf: { label: 'Django REST Framework' },
  docker: { label: 'Docker & Containerization' },
  git: { label: 'Git & GitHub' },
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
    const meta = TOPIC_LABELS[topic] ?? { label: topic }

    return {
      slug,
      topic,
      topicLabel: meta.label,
      title: (data.title as string) ?? slug,
      description: data.description as string | undefined,
      order: (data.order as number) ?? 99,
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
    const meta = TOPIC_LABELS[id] ?? { label: id }
    return {
      id,
      label: meta.label,
      pages: topicPages.sort((a, b) => a.order - b.order),
    }
  })
}

export function getPage(topic: string, slug: string): DocPage | undefined {
  return allPages.find((p) => p.topic === topic && p.slug === slug)
}

export function getCourseStartPath(topicId: string): string {
  const overview = allPages.find(
    (p) => p.topic === topicId && p.slug === 'ch00-course-overview',
  )
  if (overview) return overview.path
  const first = allPages
    .filter((p) => p.topic === topicId)
    .sort((a, b) => a.order - b.order)[0]
  return first?.path ?? `/docs/${topicId}`
}

export function searchPages(query: string): DocPage[] {
  return rankSearchPages(allPages, query)
}
