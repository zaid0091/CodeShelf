import { useEffect } from 'react'
import { useLocation } from 'react-router-dom'
import { useLenis } from 'lenis/react'
import { refreshScrollReveals, setupGsapScroll, teardownGsapScroll } from '@/lib/gsapScroll'
import { usePrefersReducedMotion } from '@/hooks/usePrefersReducedMotion'

interface LenisScrollSetupProps {
  parallaxRoot?: boolean
}

function getLenisScroller(lenis: NonNullable<ReturnType<typeof useLenis>>) {
  const root = lenis.rootElement
  if (
    root instanceof HTMLElement &&
    root !== document.documentElement &&
    root !== document.body
  ) {
    return root
  }
  return undefined
}

export function LenisScrollSetup({ parallaxRoot = false }: LenisScrollSetupProps) {
  const lenis = useLenis()
  const { pathname } = useLocation()
  const reducedMotion = usePrefersReducedMotion()

  useEffect(() => {
    if (!lenis || reducedMotion) return

    setupGsapScroll(lenis, getLenisScroller(lenis))
    return () => teardownGsapScroll()
  }, [lenis, reducedMotion])

  useEffect(() => {
    if (!lenis || reducedMotion) return
    refreshScrollReveals(getLenisScroller(lenis))
  }, [pathname, lenis, reducedMotion])

  useLenis(
    (instance) => {
      if (!parallaxRoot || reducedMotion) return
      document.documentElement.style.setProperty('--scroll-y', `${instance.scroll}px`)
      document.documentElement.style.setProperty('--scroll-progress', `${instance.progress}`)
    },
    [parallaxRoot, reducedMotion],
  )

  return null
}
