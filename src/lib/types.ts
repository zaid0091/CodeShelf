export interface DocFrontmatter {
  title: string
  description?: string
  order?: number
}

export interface DocPage {
  slug: string
  topic: string
  topicLabel: string
  title: string
  description?: string
  order: number
  content: string
  path: string
}

export interface TopicGroup {
  id: string
  label: string
  pages: DocPage[]
}

export interface SearchResult {
  page: DocPage
  snippet: string
}
