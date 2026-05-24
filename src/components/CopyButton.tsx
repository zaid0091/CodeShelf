import { useState, useCallback } from 'react'
import { Check, Copy } from 'lucide-react'

interface CopyButtonProps {
  text: string
}

export function CopyButton({ text }: CopyButtonProps) {
  const [copied, setCopied] = useState(false)

  const handleCopy = useCallback(async () => {
    await navigator.clipboard.writeText(text)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }, [text])

  return (
    <button
      type="button"
      onClick={handleCopy}
      className="flex h-8 w-8 items-center justify-center rounded-pill text-shade-50 hover:bg-shade-30/60 hover:text-ink transition-colors"
      aria-label={copied ? 'Copied' : 'Copy code'}
      title={copied ? 'Copied!' : 'Copy code'}
    >
      {copied ? (
        <Check size={15} strokeWidth={1.5} className="text-ink" />
      ) : (
        <Copy size={15} strokeWidth={1.5} />
      )}
    </button>
  )
}
