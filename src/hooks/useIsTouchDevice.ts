import { useEffect, useState } from 'react'

const POINTER_QUERY = '(hover: none) and (pointer: coarse)'

/**
 * Returns true only when the device is genuinely a touch-only device.
 *
 * Brave (and some fingerprint-resistant browsers) report `(hover: none)` and
 * `(pointer: coarse)` even on desktops, which would incorrectly disable smooth
 * scroll providers. We therefore cross-check with the user-agent string and
 * screen size so that desktop Brave is never treated as a touch device.
 */
function isMobileUA(): boolean {
  if (typeof navigator === 'undefined') return false
  return /android|iphone|ipad|ipod|mobile/i.test(navigator.userAgent)
}

function getInitial(): boolean {
  if (typeof window === 'undefined') return false
  const pointerCoarse = window.matchMedia(POINTER_QUERY).matches
  // Trust the media query only when the UA also indicates a mobile device
  // OR when the screen is narrow enough to be a phone (≤ 768 px).
  return pointerCoarse && (isMobileUA() || window.innerWidth <= 768)
}

export function useIsTouchDevice() {
  const [isTouch, setIsTouch] = useState<boolean>(getInitial)

  useEffect(() => {
    const mq = window.matchMedia(POINTER_QUERY)
    const onChange = () => {
      setIsTouch(mq.matches && (isMobileUA() || window.innerWidth <= 768))
    }
    mq.addEventListener('change', onChange)
    return () => mq.removeEventListener('change', onChange)
  }, [])

  return isTouch
}
