import { useState, useEffect } from 'react'
import { useDocumentTitle } from '@/hooks/useDocumentTitle'
import { Link } from 'react-router-dom'
import { BookOpen, Calendar, Award, RefreshCw, ChevronRight } from 'lucide-react'
import { getTopics } from '@/lib/content'
import { TopicIcon } from '@/components/TopicIcon'
import { getCompletedChapters, getStreak, clearAllProgress } from '@/lib/progress'
import { ScrollReveal } from '@/components/ScrollReveal'
import confetti from 'canvas-confetti'



export function DashboardPage() {
  useDocumentTitle('Visual Progress Dashboard | CodeShelf')
  const topics = getTopics()
  const [completedMap, setCompletedMap] = useState(getCompletedChapters())
  const [streak, setStreak] = useState(getStreak())
  const [showConfirmReset, setShowConfirmReset] = useState(false)

  // Listen to changes in progress
  useEffect(() => {
    const handleUpdate = () => {
      setCompletedMap(getCompletedChapters())
      setStreak(getStreak())
    }
    window.addEventListener('codeshelf_progress_updated', handleUpdate)
    return () => {
      window.removeEventListener('codeshelf_progress_updated', handleUpdate)
    }
  }, [])

  // Trigger premium confetti explosion
  const triggerConfetti = () => {
    const duration = 2.5 * 1000
    const animationEnd = Date.now() + duration
    const defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 1000 }

    const randomInRange = (min: number, max: number) => {
      return Math.random() * (max - min) + min
    }

    const interval = setInterval(function () {
      const timeLeft = animationEnd - Date.now()

      if (timeLeft <= 0) {
        return clearInterval(interval)
      }

      const particleCount = 50 * (timeLeft / duration)
      
      confetti({
        ...defaults,
        particleCount,
        origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 }
      })
      confetti({
        ...defaults,
        particleCount,
        origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 }
      })
    }, 250)
  }

  // Check completed courses and milestones for celebrations
  useEffect(() => {
    if (typeof window === 'undefined') return

    let shouldCelebrate = false

    // 1. Check Course Completion Milestones (100% complete)
    const celebratedCoursesData = localStorage.getItem('codeshelf_celebrated_courses')
    let celebratedCourses: string[] = celebratedCoursesData ? JSON.parse(celebratedCoursesData) : []
    const updatedCelebratedCourses = [...celebratedCourses]

    topics.forEach((topic) => {
      const completedCount = completedMap[topic.id]?.length || 0
      const totalCount = topic.pages.length
      const percent = totalCount > 0 ? Math.round((completedCount / totalCount) * 100) : 0

      if (percent === 100 && !celebratedCourses.includes(topic.id)) {
        shouldCelebrate = true
        updatedCelebratedCourses.push(topic.id)
      }
    })

    if (updatedCelebratedCourses.length !== celebratedCourses.length) {
      localStorage.setItem('codeshelf_celebrated_courses', JSON.stringify(updatedCelebratedCourses))
    }

    // 2. Check Streak Milestones (7 days, 30 days)
    const celebratedMilestonesData = localStorage.getItem('codeshelf_celebrated_milestones')
    let celebratedMilestones: number[] = celebratedMilestonesData ? JSON.parse(celebratedMilestonesData) : []
    const updatedCelebratedMilestones = [...celebratedMilestones]

    const milestones = [7, 30]
    milestones.forEach((m) => {
      if (streak >= m && !celebratedMilestones.includes(m)) {
        shouldCelebrate = true
        updatedCelebratedMilestones.push(m)
      }
    })

    // Clean up milestones if streak drops below them
    const cleanedMilestones = updatedCelebratedMilestones.filter((m) => streak >= m)

    if (
      cleanedMilestones.length !== celebratedMilestones.length ||
      JSON.stringify(cleanedMilestones) !== JSON.stringify(celebratedMilestones)
    ) {
      localStorage.setItem('codeshelf_celebrated_milestones', JSON.stringify(cleanedMilestones))
    }

    // Fire confetti if any new milestone was reached
    if (shouldCelebrate) {
      triggerConfetti()
    }
  }, [completedMap, streak, topics])

  const totalChapters = topics.reduce((sum, t) => sum + t.pages.length, 0)
  
  const completedChaptersCount = Object.values(completedMap).reduce(
    (sum, slugs) => sum + slugs.length,
    0
  )
  
  const overallPercentage = totalChapters > 0 
    ? Math.round((completedChaptersCount / totalChapters) * 100) 
    : 0

  const handleReset = () => {
    clearAllProgress()
    localStorage.removeItem('codeshelf_celebrated_courses')
    localStorage.removeItem('codeshelf_celebrated_milestones')
    setShowConfirmReset(false)
  }

  return (
    <div className="docs-index dashboard-page">
      <div className="docs-index__ambient" aria-hidden>
        <div className="docs-index__glow docs-index__glow--aloe" />
        <div className="docs-index__glow docs-index__glow--warm" />
        <div className="docs-index__mesh" />
      </div>

      <header className="docs-index__hero">
        <div className="docs-index__hero-rail" aria-hidden />
        <div className="docs-index__eyebrow">
          <span className="docs-index__eyebrow-dot" aria-hidden />
          <p className="text-eyebrow text-shade-50 mb-0">Stats & Dashboard</p>
        </div>
        <h1 className="docs-index__title font-display text-display-lg text-ink">
          Your Progress Dashboard
        </h1>
        <p className="docs-index__desc text-body-lg text-shade-50 max-w-2xl">
          Track your reading stats, monitor consistency streaks, and review your completion levels across all tracks.
        </p>

        {/* Global Statistics Grid */}
        <div className="dashboard-stats-grid">
          <div className="dashboard-stat-card">
            <div className="dashboard-stat-card__icon-well">
              <Award size={20} className="text-aloe" />
            </div>
            <div className="dashboard-stat-card__content">
              <span className="dashboard-stat-card__label">Overall Completion</span>
              <strong className="dashboard-stat-card__value font-display">{overallPercentage}%</strong>
            </div>
          </div>

          <div className="dashboard-stat-card">
            <div className="dashboard-stat-card__icon-well">
              <BookOpen size={20} className="text-aloe" />
            </div>
            <div className="dashboard-stat-card__content">
              <span className="dashboard-stat-card__label">Chapters Completed</span>
              <strong className="dashboard-stat-card__value font-display">
                {completedChaptersCount} <span className="text-body-md text-shade-40">/ {totalChapters}</span>
              </strong>
            </div>
          </div>

          <div className="dashboard-stat-card">
            <div className="dashboard-stat-card__icon-well animate-pulse">
              <Calendar size={20} className="text-warm" />
            </div>
            <div className="dashboard-stat-card__content">
              <span className="dashboard-stat-card__label">Reading Streak</span>
              <strong className="dashboard-stat-card__value font-display">
                {streak} {streak === 1 ? 'day' : 'days'}
              </strong>
            </div>
          </div>
        </div>
      </header>

      {/* Topics Catalog Grid */}
      <section className="docs-index__catalog">
        <div className="docs-index__catalog-head">
          <h2 className="docs-index__catalog-title font-display">Tracks Overview</h2>
          <p className="docs-index__catalog-sub text-caption text-shade-50">
            Current status of each course module
          </p>
        </div>

        <ul className="docs-index__grid dashboard-grid">
          {topics.map((topic, index) => {
            const completedCount = completedMap[topic.id]?.length || 0
            const totalCount = topic.pages.length
            const percent = totalCount > 0 ? Math.round((completedCount / totalCount) * 100) : 0
            
            // SVG circular configuration
            const radius = 24
            const strokeWidth = 3.5
            const circumference = 2 * Math.PI * radius
            const strokeDashoffset = circumference - (percent / 100) * circumference

            return (
              <li
                key={topic.id}
                className="docs-index-card-wrap"
                style={{ animationDelay: `${0.06 + index * 0.05}s` }}
              >
                <div className="docs-index-card dashboard-card">
                  <span className="docs-index-card__border" aria-hidden />
                  <span className="docs-index-card__spotlight" aria-hidden />

                  <div className="dashboard-card__header">
                    <div className="docs-index-card__icon-well">
                      <TopicIcon topicId={topic.id} size={30} className="docs-index-card__icon" />
                    </div>
                    
                    {/* Circle SVG Progress Ring */}
                    <div className="dashboard-card__progress-ring">
                      <svg width="56" height="56" viewBox="0 0 56 56">
                        <circle
                          cx="28"
                          cy="28"
                          r={radius}
                          stroke="var(--color-surface-muted)"
                          strokeWidth={strokeWidth}
                          fill="transparent"
                        />
                        <circle
                          cx="28"
                          cy="28"
                          r={radius}
                          stroke="var(--color-aloe)"
                          strokeWidth={strokeWidth}
                          fill="transparent"
                          strokeDasharray={circumference}
                          strokeDashoffset={strokeDashoffset}
                          strokeLinecap="round"
                          transform="rotate(-90 28 28)"
                          style={{ transition: 'stroke-dashoffset 0.6s ease' }}
                        />
                      </svg>
                      <span className="dashboard-card__progress-text font-display">
                        {percent}%
                      </span>
                    </div>
                  </div>

                  <div className="docs-index-card__body">
                    <h2 className="docs-index-card__title font-display">{topic.label}</h2>
                    <p className="docs-index-card__meta">
                      <span className="docs-index-card__count text-caption">
                        {completedCount} of {totalCount} chapters read
                      </span>
                    </p>
                  </div>

                  <div className="dashboard-card__actions">
                    <Link
                      to={`/docs/${topic.id}/${topic.pages[0]?.slug}`}
                      className="dashboard-card__cta-btn"
                    >
                      <span>{completedCount > 0 ? 'Resume Stack' : 'Start Learning'}</span>
                      <ChevronRight size={14} />
                    </Link>
                  </div>
                </div>
              </li>
            )
          })}
        </ul>
      </section>

      {/* Dangerous Controls Panel */}
      <footer className="dashboard-footer">
        <ScrollReveal animation="fade-up" delay={0.15}>
          <div className="dashboard-danger-zone">
            <span className="dashboard-danger-zone__border" aria-hidden />
            <div className="dashboard-danger-zone__content">
              <h3 className="dashboard-danger-zone__title font-display text-ink">Reset Your Progress</h3>
              <p className="text-body-md text-shade-50 mb-0">
                This will delete your entire reading history, course completion percentages, and reading streaks. This action cannot be undone.
              </p>
            </div>
            
            {showConfirmReset ? (
              <div className="dashboard-danger-zone__confirm-group">
                <button
                  type="button"
                  onClick={handleReset}
                  className="danger-btn danger-btn--confirm"
                >
                  Yes, Clear Everything
                </button>
                <button
                  type="button"
                  onClick={() => setShowConfirmReset(false)}
                  className="danger-btn danger-btn--cancel"
                >
                  Cancel
                </button>
              </div>
            ) : (
              <button
                type="button"
                onClick={() => setShowConfirmReset(true)}
                className="danger-btn"
              >
                <RefreshCw size={14} />
                <span>Reset Progress</span>
              </button>
            )}
          </div>
        </ScrollReveal>
      </footer>
    </div>
  )
}
