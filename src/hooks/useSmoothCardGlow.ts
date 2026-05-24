import { useCallback, useEffect, useRef, type PointerEvent } from 'react'

const LERP = 0.11
const EPSILON = 0.5

export function useSmoothCardGlow() {
  const cardRef = useRef<HTMLAnchorElement>(null)
  const targetRef = useRef({ x: 0, y: 0 })
  const currentRef = useRef({ x: 0, y: 0 })
  const rafRef = useRef<number>(0)
  const hoveringRef = useRef(false)

  const applyGlow = useCallback((x: number, y: number) => {
    const el = cardRef.current
    if (!el) return
    el.style.setProperty('--spot-x', `${x}px`)
    el.style.setProperty('--spot-y', `${y}px`)
  }, [])

  const tick = useCallback(() => {
    const target = targetRef.current
    const current = currentRef.current

    current.x += (target.x - current.x) * LERP
    current.y += (target.y - current.y) * LERP

    applyGlow(current.x, current.y)

    const settled =
      Math.abs(target.x - current.x) < EPSILON &&
      Math.abs(target.y - current.y) < EPSILON

    if (settled && !hoveringRef.current) {
      rafRef.current = 0
      return
    }

    rafRef.current = requestAnimationFrame(tick)
  }, [applyGlow])

  const startLoop = useCallback(() => {
    if (rafRef.current) return
    rafRef.current = requestAnimationFrame(tick)
  }, [tick])

  const setTargetFromEvent = useCallback(
    (clientX: number, clientY: number) => {
      const el = cardRef.current
      if (!el) return
      const rect = el.getBoundingClientRect()
      targetRef.current = {
        x: clientX - rect.left,
        y: clientY - rect.top,
      }
      startLoop()
    },
    [startLoop],
  )

  const resetToCenter = useCallback(() => {
    const el = cardRef.current
    if (!el) return
    const rect = el.getBoundingClientRect()
    targetRef.current = { x: rect.width / 2, y: rect.height / 2 }
    startLoop()
  }, [startLoop])

  useEffect(() => {
    const el = cardRef.current
    if (!el) return
    const rect = el.getBoundingClientRect()
    const center = { x: rect.width / 2, y: rect.height / 2 }
    targetRef.current = center
    currentRef.current = { ...center }
    applyGlow(center.x, center.y)
  }, [applyGlow])

  useEffect(() => {
    return () => {
      if (rafRef.current) cancelAnimationFrame(rafRef.current)
    }
  }, [])

  const onPointerEnter = useCallback(() => {
    hoveringRef.current = true
    cardRef.current?.classList.add('topic-card--hover')
    startLoop()
  }, [startLoop])

  const onPointerLeave = useCallback(() => {
    hoveringRef.current = false
    cardRef.current?.classList.remove('topic-card--hover')
    resetToCenter()
  }, [resetToCenter])

  const onPointerMove = useCallback(
    (e: PointerEvent<HTMLAnchorElement>) => {
      setTargetFromEvent(e.clientX, e.clientY)
    },
    [setTargetFromEvent],
  )

  return { cardRef, onPointerEnter, onPointerMove, onPointerLeave }
}
