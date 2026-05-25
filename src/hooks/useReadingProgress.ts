import { useEffect, useState } from 'react'

export function useReadingProgress(scrollSelector = '[data-docs-scroll]') {
  const [progress, setProgress] = useState(0)

  useEffect(() => {
    const el = document.querySelector<HTMLElement>(scrollSelector)
    if (!el) return

    let raf = 0

    const update = () => {
      const max = el.scrollHeight - el.clientHeight
      const pct = max > 0 ? Math.min(1, Math.max(0, el.scrollTop / max)) : 0
      setProgress(pct)
    }

    const onScroll = () => {
      if (raf) return
      raf = requestAnimationFrame(() => {
        raf = 0
        update()
      })
    }

    update()
    el.addEventListener('scroll', onScroll, { passive: true })
    window.addEventListener('resize', update)

    return () => {
      el.removeEventListener('scroll', onScroll)
      window.removeEventListener('resize', update)
      if (raf) cancelAnimationFrame(raf)
    }
  }, [scrollSelector])

  return progress
}
