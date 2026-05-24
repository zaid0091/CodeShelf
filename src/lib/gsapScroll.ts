import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import type Lenis from 'lenis'

gsap.registerPlugin(ScrollTrigger)

let activeLenis: Lenis | null = null
let scrollListener: (() => void) | null = null

function getRevealTargets(scroller?: HTMLElement) {
  const root = scroller ?? document
  return gsap.utils.toArray<HTMLElement>('[data-scroll]', root)
}

function initRevealAnimations(scroller?: HTMLElement) {
  const targets = getRevealTargets(scroller)
  if (targets.length === 0) return

  targets.forEach((el) => {
    const delay = parseFloat(el.dataset.scrollDelay ?? '0')
    const distance = parseFloat(el.dataset.scrollDistance ?? '48')
    const duration = parseFloat(el.dataset.scrollDuration ?? '1')
    const animation = el.dataset.scrollAnimation ?? 'fade-up'

    const from: gsap.TweenVars = { opacity: 0 }
    const to: gsap.TweenVars = { opacity: 1, duration, delay, ease: 'power3.out' }

    if (animation.includes('up')) from.y = distance
    if (animation.includes('down')) from.y = -distance
    if (animation.includes('left')) from.x = distance
    if (animation.includes('right')) from.x = -distance
    if (animation.includes('scale')) from.scale = 0.92

    gsap.fromTo(el, from, {
      ...to,
      x: 0,
      y: 0,
      scale: 1,
      scrollTrigger: {
        trigger: el,
        scroller: scroller ?? undefined,
        start: el.dataset.scrollStart ?? 'top 88%',
        end: el.dataset.scrollEnd,
        toggleActions: 'play none none none',
        once: true,
      },
    })
  })
}

function initParallax(scroller?: HTMLElement) {
  gsap.utils.toArray<HTMLElement>('[data-parallax-speed]', scroller ?? document).forEach((el) => {
    const speed = parseFloat(el.dataset.parallaxSpeed ?? '0.15')
    gsap.to(el, {
      yPercent: speed * 100,
      ease: 'none',
      scrollTrigger: {
        trigger: el.closest('[data-parallax-container]') ?? el,
        scroller: scroller ?? undefined,
        start: 'top bottom',
        end: 'bottom top',
        scrub: 0.6,
      },
    })
  })
}

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
