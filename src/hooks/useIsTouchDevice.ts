import { useEffect, useState } from 'react'

const QUERY = '(hover: none) and (pointer: coarse)'

function getInitial(): boolean {
  if (typeof window === 'undefined') return false
  return window.matchMedia(QUERY).matches
}

export function useIsTouchDevice() {
  const [isTouch, setIsTouch] = useState<boolean>(getInitial)

  useEffect(() => {
    const mq = window.matchMedia(QUERY)
    const onChange = () => setIsTouch(mq.matches)
    mq.addEventListener('change', onChange)
    return () => mq.removeEventListener('change', onChange)
  }, [])

  return isTouch
}
