import { useEffect, useState } from 'react'
import { useLenis } from 'lenis/react'

export function useLenisScrolled(threshold = 1) {
  const [scrolled, setScrolled] = useState(false)
  const lenis = useLenis()

  useLenis(
    (instance) => {
      setScrolled(instance.scroll > threshold)
    },
    [threshold],
  )

  useEffect(() => {
    if (lenis) {
      setScrolled(lenis.scroll > threshold)
    }
  }, [lenis, threshold])

  return scrolled
}
