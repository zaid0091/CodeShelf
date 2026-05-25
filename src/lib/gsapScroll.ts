import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import type Lenis from 'lenis'
import { splitTextNodes } from '@/lib/splitText'

gsap.registerPlugin(ScrollTrigger)

let activeLenis: Lenis | null = null
let scrollListener: (() => void) | null = null

function getRevealTargets(scroller?: HTMLElement) {
  const root = scroller ?? document
  return gsap.utils.toArray<HTMLElement>('[data-scroll]', root)
}

function buildScrollTrigger(
  el: HTMLElement,
  scroller: HTMLElement | undefined,
  scrub: boolean,
): ScrollTrigger.Vars {
  return {
    trigger: el,
    scroller: scroller ?? undefined,
    start: el.dataset.scrollStart ?? (scrub ? 'top 92%' : 'top 88%'),
    end: el.dataset.scrollEnd ?? (scrub ? 'top 30%' : undefined),
    scrub: scrub ? 0.6 : false,
    toggleActions: scrub ? undefined : 'play none none none',
    once: !scrub,
  }
}

function animateBasicReveal(
  el: HTMLElement,
  animation: string,
  scroller: HTMLElement | undefined,
) {
  const delay = parseFloat(el.dataset.scrollDelay ?? '0')
  const distance = parseFloat(el.dataset.scrollDistance ?? '48')
  const duration = parseFloat(el.dataset.scrollDuration ?? '1')
  const scrub = el.dataset.scrollScrub === 'true'

  const from: gsap.TweenVars = { opacity: 0 }
  const to: gsap.TweenVars = {
    opacity: 1,
    duration,
    delay,
    ease: 'power3.out',
    x: 0,
    y: 0,
    scale: 1,
    rotate: 0,
    rotationX: 0,
    rotationY: 0,
    filter: 'blur(0px)',
    clipPath: 'inset(0% 0% 0% 0%)',
  }

  if (animation.includes('up')) from.y = distance
  if (animation.includes('down')) from.y = -distance
  if (animation.includes('left')) from.x = distance
  if (animation.includes('right')) from.x = -distance
  if (animation.includes('scale')) from.scale = 0.92

  if (animation === 'tilt-in') {
    Object.assign(from, {
      opacity: 0,
      y: 36,
      scale: 0.94,
      rotationX: 14,
      rotationY: -6,
      transformOrigin: '50% 50%',
    })
    Object.assign(to, { transformPerspective: 1000 })
  }

  if (animation === 'blur-in') {
    Object.assign(from, { opacity: 0, y: 24, filter: 'blur(18px)' })
  }

  if (animation === 'clip-up') {
    Object.assign(from, {
      opacity: 1,
      y: 0,
      clipPath: 'inset(0% 0% 100% 0%)',
    })
    Object.assign(to, { duration: duration * 1.1, ease: 'power4.out' })
  }

  if (animation === 'clip-right') {
    Object.assign(from, {
      opacity: 1,
      x: 0,
      clipPath: 'inset(0% 100% 0% 0%)',
    })
    Object.assign(to, { duration: duration * 1.1, ease: 'power4.out' })
  }

  gsap.fromTo(el, from, {
    ...to,
    onComplete: () => {
      if (!scrub) {
        el.classList.add('is-revealed')
        el.dataset.scrollRevealed = 'true'
      }
    },
    scrollTrigger: buildScrollTrigger(el, scroller, scrub),
  })
}

function animateTextReveal(
  el: HTMLElement,
  unit: 'chars' | 'words',
  scroller: HTMLElement | undefined,
) {
  if (el.dataset.scrollSplitDone === 'true') return

  const split = splitTextNodes(el)
  el.dataset.scrollSplitDone = 'true'

  const targets = unit === 'chars' ? split.chars : split.words
  if (targets.length === 0) return

  const delay = parseFloat(el.dataset.scrollDelay ?? '0')
  const duration = parseFloat(el.dataset.scrollDuration ?? '1')
  const stagger = parseFloat(
    el.dataset.scrollStagger ?? (unit === 'chars' ? '0.022' : '0.045'),
  )
  const scrub = el.dataset.scrollScrub === 'true'

  gsap.set(targets, {
    yPercent: 110,
    rotateX: -55,
    opacity: 0,
    transformOrigin: '50% 100%',
    transformPerspective: 600,
  })

  gsap.to(targets, {
    yPercent: 0,
    rotateX: 0,
    opacity: 1,
    duration,
    delay,
    stagger,
    ease: 'power3.out',
    onComplete: () => {
      if (!scrub) {
        el.classList.add('is-revealed')
        el.dataset.scrollRevealed = 'true'
      }
    },
    scrollTrigger: buildScrollTrigger(el, scroller, scrub),
  })
}

function initRevealAnimations(scroller?: HTMLElement) {
  const targets = getRevealTargets(scroller)
  if (targets.length === 0) return

  targets.forEach((el) => {
    const animation = el.dataset.scrollAnimation ?? 'fade-up'

    if (animation === 'text-chars') return animateTextReveal(el, 'chars', scroller)
    if (animation === 'text-words') return animateTextReveal(el, 'words', scroller)

    animateBasicReveal(el, animation, scroller)
  })
}

function initParallax(scroller?: HTMLElement) {
  gsap.utils
    .toArray<HTMLElement>('[data-parallax-speed]', scroller ?? document)
    .forEach((el) => {
      const speed = parseFloat(el.dataset.parallaxSpeed ?? '0.15')
      const rotate = parseFloat(el.dataset.parallaxRotate ?? '0')
      const scale = parseFloat(el.dataset.parallaxScale ?? '1')
      const skew = parseFloat(el.dataset.parallaxSkew ?? '0')

      const to: gsap.TweenVars = {
        yPercent: speed * 100,
        ease: 'none',
      }

      if (rotate) to.rotation = rotate
      if (scale && scale !== 1) to.scale = scale
      if (skew) to.skewY = skew

      gsap.to(el, {
        ...to,
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
