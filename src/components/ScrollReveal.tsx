import type { CSSProperties, ElementType, ReactNode } from 'react'
import { useIsTouchDevice } from '@/hooks/useIsTouchDevice'
import { usePrefersReducedMotion } from '@/hooks/usePrefersReducedMotion'

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
  animation = 'fade-up',
  delay = 0,
  distance = 48,
  duration = 1,
  stagger,
  start,
  end,
  scrub,
  style,
  id,
  ariaLabel,
  ariaHidden,
}: ScrollRevealProps) {
  const reducedMotion = usePrefersReducedMotion()
  const isTouch = useIsTouchDevice()

  if (reducedMotion || isTouch) {
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

  return (
    <Tag
      className={className}
      style={style}
      id={id}
      aria-label={ariaLabel}
      aria-hidden={ariaHidden}
      data-scroll
      data-scroll-animation={animation}
      data-scroll-delay={delay}
      data-scroll-distance={distance}
      data-scroll-duration={duration}
      {...(stagger !== undefined ? { 'data-scroll-stagger': stagger } : {})}
      {...(start ? { 'data-scroll-start': start } : {})}
      {...(end ? { 'data-scroll-end': end } : {})}
      {...(scrub ? { 'data-scroll-scrub': 'true' } : {})}
    >
      {children}
    </Tag>
  )
}
