import { Link } from 'react-router-dom'
import { ArrowUpRight } from 'lucide-react'
import { getTopics, getCourseStartPath } from '@/lib/content'
import { TopicIcon } from '@/components/TopicIcon'
import { ScrollReveal } from '@/components/ScrollReveal'
import { useSmoothCardGlow } from '@/hooks/useSmoothCardGlow'

function TopicCard({
  topicId,
  label,
  noteCount,
  index,
}: {
  topicId: string
  label: string
  noteCount: number
  index: number
}) {
  const { cardRef, onPointerEnter, onPointerMove, onPointerLeave } =
    useSmoothCardGlow<HTMLAnchorElement>()

  // Staggered cascade entrance — each card waits a touch longer than the previous
  const enterDelay = 0.06 + index * 0.07

  return (
    <ScrollReveal
      animation="tilt-in"
      duration={1.05}
      delay={enterDelay}
      distance={42}
      start="top 92%"
      className="h-full min-w-0"
    >
      <Link
        ref={cardRef}
        to={getCourseStartPath(topicId)}
        className="topic-card"
        onPointerEnter={onPointerEnter}
        onPointerMove={onPointerMove}
        onPointerLeave={onPointerLeave}
      >
        <span className="topic-card__border" aria-hidden />
        <span className="topic-card__spotlight" aria-hidden />
        <span className="topic-card__shine" aria-hidden />
        <span className="topic-card__noise" aria-hidden />

        <span className="topic-card__index" aria-hidden>
          {String(index + 1).padStart(2, '0')}
        </span>

        <div className="topic-card__icon-well">
          <TopicIcon topicId={topicId} size={36} className="topic-card__icon" />
        </div>

        <div className="topic-card__body">
          <h3 className="topic-card__title font-display">{label}</h3>
          <p className="topic-card__meta">
            <span className="topic-card__count">
              {noteCount} note{noteCount !== 1 ? 's' : ''}
            </span>
          </p>
        </div>

        <span className="topic-card__cta" aria-hidden>
          <ArrowUpRight size={18} strokeWidth={1.5} />
        </span>
      </Link>
    </ScrollReveal>
  )
}

export function TopicsSection() {
  const topics = getTopics()

  return (
    <section className="topics-section">
      <div className="topics-section__ambient" aria-hidden>
        <div className="topics-section__glow topics-section__glow--aloe" data-parallax-speed="-0.08" />
        <div className="topics-section__glow topics-section__glow--cool" data-parallax-speed="0.06" />
        <div className="topics-section__grid" />
        <div className="topics-section__fade" />
      </div>

      <div className="topics-section__inner">
        <header className="topics-header">
          <ScrollReveal animation="fade-up" duration={0.7} distance={18} start="top 90%">
            <div className="topics-header__rail" aria-hidden />
          </ScrollReveal>

          <ScrollReveal animation="fade-up" delay={0.05} duration={0.8} distance={22} start="top 92%">
            <div className="topics-eyebrow">
              <span className="topics-eyebrow__dot" aria-hidden />
              <p className="text-eyebrow text-link-cool-1 mb-0">Topics</p>
            </div>
          </ScrollReveal>

          <ScrollReveal
            as="h2"
            animation="text-chars"
            duration={1}
            stagger={0.02}
            delay={0.12}
            start="top 90%"
            className="topics-header__title font-display text-display-lg text-on-primary"
          >
            Everything you need to revise.
          </ScrollReveal>

          <ScrollReveal
            as="p"
            animation="blur-in"
            delay={0.35}
            duration={1}
            start="top 92%"
            className="topics-header__desc text-body-lg text-link-cool-2 max-w-xl"
          >
            Six curated tracks — structured notes you can open and revise in seconds.
          </ScrollReveal>
        </header>

        <div className="topics-grid">
          {topics.map((topic, index) => (
            <TopicCard
              key={topic.id}
              topicId={topic.id}
              label={topic.label}
              noteCount={topic.pages.length}
              index={index}
            />
          ))}
        </div>
      </div>
    </section>
  )
}
