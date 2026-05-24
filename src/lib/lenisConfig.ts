import type { LenisOptions } from 'lenis'

/** Default Lenis easing — buttery deceleration curve */
export const lenisEasing = (t: number) => Math.min(1, 1.001 - Math.pow(2, -10 * t))

export function getLenisOptions(): LenisOptions {
  return {
    autoRaf: true,
    anchors: {
      offset: 80,
      duration: 1.2,
      easing: lenisEasing,
    },
    lerp: 0.08,
    duration: 1.35,
    easing: lenisEasing,
    smoothWheel: true,
    syncTouch: false,
    syncTouchLerp: 0.075,
    touchInertiaExponent: 1.7,
    touchMultiplier: 1.15,
    wheelMultiplier: 1,
    autoResize: true,
    overscroll: true,
    allowNestedScroll: false,
    prevent: (node) => node.closest('[data-lenis-prevent]') !== null,
  }
}
