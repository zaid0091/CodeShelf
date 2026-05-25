import { Link } from 'react-router-dom'
import { ArrowLeft, ArrowRight } from 'lucide-react'
import { ScrollReveal } from '@/components/ScrollReveal'
import type { DocPage } from '@/lib/types'

interface DocPageNavProps {
  prev: DocPage | null
  next: DocPage | null
}

function NavLink({
  page,
  direction,
}: {
  page: DocPage
  direction: 'prev' | 'next'
}) {
  const isPrev = direction === 'prev'
  return (
    <Link
      to={page.path}
      className={['doc-nav__card', isPrev ? 'doc-nav__card--prev' : 'doc-nav__card--next']
        .filter(Boolean)
        .join(' ')}
    >
      <span className="doc-nav__card-border" aria-hidden />
      <span className="doc-nav__card-shine" aria-hidden />

      <span className="doc-nav__card-eyebrow">
        {isPrev ? (
          <>
            <ArrowLeft size={13} strokeWidth={1.5} aria-hidden /> Previous
          </>
        ) : (
          <>
            Next <ArrowRight size={13} strokeWidth={1.5} aria-hidden />
          </>
        )}
      </span>

      <span className="doc-nav__card-title font-display">{page.title}</span>

      <span className="doc-nav__card-topic">{page.topicLabel}</span>
    </Link>
  )
}

export function DocPageNav({ prev, next }: DocPageNavProps) {
  if (!prev && !next) return null

  return (
    <ScrollReveal animation="fade-up" delay={0.08} duration={0.85} distance={20}>
      <nav className="doc-nav" aria-label="Chapter navigation">
        {prev ? <NavLink page={prev} direction="prev" /> : <span className="doc-nav__spacer" />}
        {next ? <NavLink page={next} direction="next" /> : <span className="doc-nav__spacer" />}
      </nav>
    </ScrollReveal>
  )
}
