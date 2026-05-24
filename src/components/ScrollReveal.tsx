import type { CSSProperties, ElementType, ReactNode } from 'react'
import { usePrefersReducedMotion } from '@/hooks/usePrefersReducedMotion'

type ScrollAnimation = 'fade-up' | 'fade-down' | 'fade-left' | 'fade-right' | 'fade-scale'

interface ScrollRevealProps {
  as?: ElementType
  children: ReactNode
  className?: string
  animation?: ScrollAnimation
  delay?: number
  distance?: number
  duration?: number
  start?: string
  style?: CSSProperties
}

export function ScrollReveal({
  as: Tag = 'div',
  children,
  className,
  animation = 'fade-up',
  delay = 0,
  distance = 48,
  duration = 1,
  start,
  style,
}: ScrollRevealProps) {
  const reducedMotion = usePrefersReducedMotion()

  if (reducedMotion) {
    return (
      <Tag className={className} style={style}>
        {children}
      </Tag>
    )
  }

  return (
    <Tag
      className={className}
      style={style}
      data-scroll
      data-scroll-animation={animation}
      data-scroll-delay={delay}
      data-scroll-distance={distance}
      data-scroll-duration={duration}
      {...(start ? { 'data-scroll-start': start } : {})}
    >
      {children}
    </Tag>
  )
}
