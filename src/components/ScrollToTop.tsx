import { useEffect } from 'react'
import { useLocation } from 'react-router-dom'
import { useLenis } from 'lenis/react'

export function ScrollToTop() {
  const { pathname } = useLocation()
  const lenis = useLenis()

  useEffect(() => {
    if (lenis) {
      lenis.scrollTo(0, { immediate: true })
      return
    }
    const docsScroll = document.querySelector<HTMLElement>('[data-docs-scroll]')
    if (docsScroll) {
      docsScroll.scrollTo(0, 0)
      return
    }
    window.scrollTo(0, 0)
  }, [pathname, lenis])

  return null
}
