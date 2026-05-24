import { useEffect, useState, type RefObject } from 'react'

export function useWindowScrolled(threshold = 1) {
  const [scrolled, setScrolled] = useState(false)

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > threshold)

    onScroll()
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [threshold])

  return scrolled
}

export function useElementScrolled(
  ref: RefObject<HTMLElement | null>,
  threshold = 1,
) {
  const [scrolled, setScrolled] = useState(false)

  useEffect(() => {
    const el = ref.current
    if (!el) return

    const onScroll = () => setScrolled(el.scrollTop > threshold)

    onScroll()
    el.addEventListener('scroll', onScroll, { passive: true })
    return () => el.removeEventListener('scroll', onScroll)
  }, [ref, threshold])

  return scrolled
}
