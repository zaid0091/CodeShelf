import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { MotionPathPlugin } from 'gsap/MotionPathPlugin'
import type Lenis from 'lenis'
import { splitTextNodes } from '@/lib/splitText'

gsap.registerPlugin(ScrollTrigger, MotionPathPlugin)

let activeLenis: Lenis | null = null
let scrollListener: (() => void) | null = null

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

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

// ---------------------------------------------------------------------------
// Premium animation: Hero 3-D card stack explode
// ---------------------------------------------------------------------------

function initHeroExplode(scroller?: HTMLElement) {
  const stage = document.querySelector<HTMLElement>('[data-hero-explode]')
  if (!stage) return

  const cards = gsap.utils.toArray<HTMLElement>('[data-hero-card]', stage)
  if (cards.length === 0) return

  // Set initial 3-D perspective on the parent
  gsap.set(stage, { perspective: 900 })

  // Stagger the cards with a scrubbed explode: they fan out then collapse back
  gsap.fromTo(
    cards,
    {
      rotationY: 0,
      rotationX: 0,
      z: 0,
      opacity: (i) => (i === 0 ? 1 : 0.5),
    },
    {
      rotationY: (i) => (i - Math.floor(cards.length / 2)) * 22,
      rotationX: -12,
      z: (i) => (i - Math.floor(cards.length / 2)) * 60,
      opacity: 1,
      stagger: 0.04,
      ease: 'power2.out',
      scrollTrigger: {
        trigger: stage,
        scroller: scroller ?? undefined,
        start: 'top 85%',
        end: 'bottom 40%',
        scrub: 1.2,
      },
    },
  )
}

// ---------------------------------------------------------------------------
// Premium animation: SVG learning-path draw-on
// ---------------------------------------------------------------------------

function initLearningPath(scroller?: HTMLElement) {
  const section = document.querySelector<HTMLElement>('[data-learning-path]')
  if (!section) return

  const paths = gsap.utils.toArray<SVGPathElement>('[data-path-draw]', section)
  const nodes = gsap.utils.toArray<HTMLElement>('[data-path-node]', section)
  const labels = gsap.utils.toArray<HTMLElement>('[data-path-label]', section)

  if (paths.length === 0) return

  // Draw each SVG path
  paths.forEach((path) => {
    const len = path.getTotalLength()
    gsap.set(path, { strokeDasharray: len, strokeDashoffset: len })
    gsap.to(path, {
      strokeDashoffset: 0,
      ease: 'power1.inOut',
      scrollTrigger: {
        trigger: section,
        scroller: scroller ?? undefined,
        start: 'top 75%',
        end: 'bottom 20%',
        scrub: 1,
      },
    })
  })

  // Fade in nodes and labels staggered with the path
  if (nodes.length) {
    gsap.fromTo(
      nodes,
      { scale: 0, opacity: 0 },
      {
        scale: 1,
        opacity: 1,
        stagger: 0.08,
        ease: 'back.out(1.6)',
        scrollTrigger: {
          trigger: section,
          scroller: scroller ?? undefined,
          start: 'top 70%',
          end: 'center 30%',
          scrub: 0.8,
        },
      },
    )
  }

  if (labels.length) {
    gsap.fromTo(
      labels,
      { x: -20, opacity: 0 },
      {
        x: 0,
        opacity: 1,
        stagger: 0.1,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: section,
          scroller: scroller ?? undefined,
          start: 'top 65%',
          end: 'center 25%',
          scrub: 0.8,
        },
      },
    )
  }
}

// ---------------------------------------------------------------------------
// Premium animation: Pinned horizontal showcase with staged card reveals
// ---------------------------------------------------------------------------

function initHorizontalShowcase(scroller?: HTMLElement) {
  const section = document.querySelector<HTMLElement>('[data-showcase]')
  if (!section) return

  const track = section.querySelector<HTMLElement>('[data-showcase-track]')
  if (!track) return

  const cards = gsap.utils.toArray<HTMLElement>('[data-showcase-card]', track)
  if (cards.length === 0) return

  // Pin the section and scrub the horizontal track
  const totalWidth = track.scrollWidth - section.clientWidth

  const tl = gsap.timeline({
    scrollTrigger: {
      trigger: section,
      scroller: scroller ?? undefined,
      start: 'top top',
      end: () => `+=${totalWidth + window.innerHeight}`,
      pin: true,
      scrub: 1,
      anticipatePin: 1,
    },
  })

  tl.to(track, { x: -totalWidth, ease: 'none' })

  // Staggered reveal for each card as it enters the viewport
  cards.forEach((card) => {
    gsap.fromTo(
      card,
      {
        opacity: 0,
        y: 60,
        scale: 0.92,
        rotationX: 12,
      },
      {
        opacity: 1,
        y: 0,
        scale: 1,
        rotationX: 0,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: card,
          containerAnimation: tl,
          start: 'left 90%',
          end: 'left 40%',
          scrub: 0.6,
        },
      },
    )

    // Glow / shimmer pulse on each card when fully in view
    const glowEl = card.querySelector<HTMLElement>('[data-card-glow]')
    if (glowEl) {
      gsap.fromTo(
        glowEl,
        { opacity: 0 },
        {
          opacity: 0.6,
          yoyo: true,
          repeat: -1,
          duration: 2,
          ease: 'sine.inOut',
          scrollTrigger: {
            trigger: card,
            containerAnimation: tl,
            start: 'left 60%',
            end: 'left 20%',
            toggleActions: 'play pause resume pause',
          },
        },
      )
    }
  })
}

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
