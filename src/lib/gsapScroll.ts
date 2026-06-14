import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { MotionPathPlugin } from 'gsap/MotionPathPlugin'
import type Lenis from 'lenis'

gsap.registerPlugin(ScrollTrigger, MotionPathPlugin)

let activeLenis: Lenis | null = null
let scrollListener: (() => void) | null = null

function initRevealAnimations(_scroller?: HTMLElement) {}
function initParallax(_scroller?: HTMLElement) {}
function initHeroExplode(_scroller?: HTMLElement) {}
function initLearningPath(_scroller?: HTMLElement) {}
function initHorizontalShowcase(_scroller?: HTMLElement) {}

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

export function setupGsapScroll(lenis: Lenis, scroller?: HTMLElement) {
  teardownGsapScroll()

  activeLenis = lenis

  if (scroller) {
    ScrollTrigger.scrollerProxy(scroller, {
      scrollTop(value) {
        if (arguments.length && value !== undefined) {
          lenis.scrollTo(value, { immediate: true })
        }
        return lenis.scroll
      },
      getBoundingClientRect() {
        return {
          top: 0,
          left: 0,
          width: scroller.clientWidth,
          height: scroller.clientHeight,
        }
      },
      pinType: scroller.style.transform ? 'transform' : 'fixed',
    })
  } else {
    ScrollTrigger.scrollerProxy(document.documentElement, {
      scrollTop(value) {
        if (arguments.length && value !== undefined) {
          lenis.scrollTo(value, { immediate: true })
        }
        return lenis.scroll
      },
      getBoundingClientRect() {
        return {
          top: 0,
          left: 0,
          width: window.innerWidth,
          height: window.innerHeight,
        }
      },
    })
  }

  scrollListener = () => ScrollTrigger.update()
  lenis.on('scroll', scrollListener)

  initRevealAnimations(scroller)
  initParallax(scroller)
  initHeroExplode(scroller)
  initLearningPath(scroller)
  initHorizontalShowcase(scroller)

  ScrollTrigger.refresh()
}

export function refreshScrollReveals(scroller?: HTMLElement) {
  ScrollTrigger.getAll().forEach((trigger) => {
    const el = trigger.trigger
    if (el instanceof HTMLElement && el.hasAttribute('data-scroll')) {
      trigger.kill()
    }
  })
  initRevealAnimations(scroller)
  ScrollTrigger.refresh()
}

export function teardownGsapScroll() {
  if (activeLenis && scrollListener) {
    activeLenis.off('scroll', scrollListener)
  }
  activeLenis = null
  scrollListener = null
  ScrollTrigger.getAll().forEach((trigger) => trigger.kill())
}
