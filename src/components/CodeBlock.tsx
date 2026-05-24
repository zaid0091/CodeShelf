import { isValidElement, type ReactNode } from 'react'
import { CopyButton } from './CopyButton'

interface CodeBlockProps {
  language: string
  className?: string
  children?: ReactNode
}

export function extractCodeText(node: ReactNode): string {
  if (typeof node === 'string') return node
  if (typeof node === 'number') return String(node)
  if (Array.isArray(node)) return node.map(extractCodeText).join('')
  if (isValidElement<{ children?: ReactNode }>(node)) {
    return extractCodeText(node.props.children)
  }
  return ''
}

export function CodeBlock({ language, className, children }: CodeBlockProps) {
  const code = extractCodeText(children).replace(/\n$/, '')

  return (
    <div className="code-block group relative my-8 not-prose">
      <div className="code-block-header">
        <span className="text-eyebrow !normal-case text-shade-50">{language}</span>
        <CopyButton text={code} />
      </div>
      <pre className="code-block-pre">
        <code className={className}>{children}</code>
      </pre>
    </div>
  )
}
