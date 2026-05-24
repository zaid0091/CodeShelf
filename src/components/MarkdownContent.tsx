import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import rehypeHighlight from 'rehype-highlight'
import rehypeSlug from 'rehype-slug'
import { Link } from 'react-router-dom'
import { CodeBlock, extractCodeText } from './CodeBlock'
import { isExternalHref, resolveMarkdownHref } from '@/lib/resolveMarkdownHref'

interface MarkdownContentProps {
  content: string
  topic: string
}

export function MarkdownContent({ content, topic }: MarkdownContentProps) {
  return (
    <article className="prose-docs">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        rehypePlugins={[rehypeHighlight, rehypeSlug]}
        components={{
          pre({ children }) {
            return <>{children}</>
          },
          a({ href, children, ...rest }) {
            if (!href) {
              return <a {...rest}>{children}</a>
            }

            if (isExternalHref(href)) {
              return (
                <a href={href} target="_blank" rel="noopener noreferrer" {...rest}>
                  {children}
                </a>
              )
            }

            const to = resolveMarkdownHref(href, topic)

            if (to.startsWith('/')) {
              return (
                <Link to={to} {...rest}>
                  {children}
                </Link>
              )
            }

            return (
              <a href={to} {...rest}>
                {children}
              </a>
            )
          },
          code({ className, children, ...rest }) {
            const match = /language-(\w+)/.exec(className ?? '')
            const isBlock = Boolean(match) || extractCodeText(children).includes('\n')

            if (isBlock) {
              return (
                <CodeBlock language={match?.[1] ?? 'text'} className={className}>
                  {children}
                </CodeBlock>
              )
            }

            return (
              <code className={className} {...rest}>
                {children}
              </code>
            )
          },
        }}
      >
        {content}
      </ReactMarkdown>
    </article>
  )
}
