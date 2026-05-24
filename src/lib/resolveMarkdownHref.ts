/**
 * Rewrites markdown file links (e.g. ./ch01-introduction-apis.md)
 * to in-app routes (/docs/drf/ch01-introduction-apis).
 */
export function resolveMarkdownHref(href: string, currentTopic: string): string {
  if (
    href.startsWith('http://') ||
    href.startsWith('https://') ||
    href.startsWith('mailto:') ||
    href.startsWith('#')
  ) {
    return href
  }

  if (href.startsWith('/docs/')) {
    return href
  }

  const crossTopic = href.match(/^\.\.\/([^/]+)\/([^/?#]+\.md)(?:#.*)?$/)
  if (crossTopic) {
    const slug = crossTopic[2].replace(/\.md$/, '')
    const hash = href.includes('#') ? href.slice(href.indexOf('#')) : ''
    return `/docs/${crossTopic[1]}/${slug}${hash}`
  }

  const sameTopic = href.match(/^(?:\.\/)?([^/?#]+\.md)(?:#.*)?$/)
  if (sameTopic) {
    const slug = sameTopic[1].replace(/\.md$/, '')
    const hash = href.includes('#') ? href.slice(href.indexOf('#')) : ''
    return `/docs/${currentTopic}/${slug}${hash}`
  }

  return href
}

export function isExternalHref(href: string): boolean {
  return (
    href.startsWith('http://') ||
    href.startsWith('https://') ||
    href.startsWith('mailto:')
  )
}
