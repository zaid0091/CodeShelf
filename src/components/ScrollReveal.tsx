import type { CSSProperties, ElementType, ReactNode } from 'react'

type ScrollAnimation =
  | 'fade-up'
  | 'fade-down'
  | 'fade-left'
  | 'fade-right'
  | 'fade-scale'
  | 'tilt-in'
  | 'blur-in'
  | 'clip-up'
  | 'clip-right'
  | 'text-chars'
  | 'text-words'

interface ScrollRevealProps {
  as?: ElementType
  children: ReactNode
  className?: string
  animation?: ScrollAnimation
  delay?: number
  distance?: number
  duration?: number
  stagger?: number
  start?: string
  end?: string
  scrub?: boolean
  style?: CSSProperties
  id?: string
  ariaLabel?: string
  ariaHidden?: boolean
}

export function ScrollReveal({
  as: Tag = 'div',
  children,
  className,
  style,
  id,
  ariaLabel,
  ariaHidden,
}: ScrollRevealProps) {
  return (
    <Tag
      className={className}
      style={style}
      id={id}
      aria-label={ariaLabel}
      aria-hidden={ariaHidden}
    >
      {children}
    </Tag>
  )
}
