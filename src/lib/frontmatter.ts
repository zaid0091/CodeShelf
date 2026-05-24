import { parse as parseYaml } from 'yaml'

export interface FrontmatterResult {
  data: Record<string, unknown>
  content: string
}

export function parseFrontmatter(raw: string): FrontmatterResult {
  const match = raw.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$/)

  if (!match) {
    return { data: {}, content: raw.trim() }
  }

  const [, yamlBlock, body] = match
  const data = (parseYaml(yamlBlock) as Record<string, unknown>) ?? {}

  return { data, content: body.trim() }
}
