import { useState, useEffect, useMemo } from 'react'
import { 
  Brain, 
  RotateCw, 
  Sparkles, 
  Shuffle, 
  Lightbulb, 
  CheckCircle2, 
  XCircle, 
  RotateCcw, 
  ArrowLeft, 
  ArrowRight,
  BookOpen
} from 'lucide-react'
import { MarkdownContent } from './MarkdownContent'
import type { Flashcard } from '@/lib/flashcards'

interface FlashcardViewerProps {
  cards: Flashcard[]
  topic: string
  onBackToReading: () => void
}

type MasteryState = 'mastered' | 'practice' | null

export function FlashcardViewer({ cards, topic, onBackToReading }: FlashcardViewerProps) {
  const [shuffledCards, setShuffledCards] = useState<Flashcard[]>(() => [...cards])
  const [isShuffled, setIsShuffled] = useState(false)
  const [currentIndex, setCurrentIndex] = useState(0)
  const [isFlipped, setIsFlipped] = useState(false)
  const [showHint, setShowHint] = useState(false)
  
  // Track mastery locally in state to update count displays dynamically
  const [masteryMap, setMasteryMap] = useState<Record<string, MasteryState>>({})

  // Initialize shuffled cards and load mastery map from localStorage
  useEffect(() => {
    setShuffledCards([...cards])
    setCurrentIndex(0)
    setIsFlipped(false)
    setShowHint(false)
    setIsShuffled(false)
    const initialMastery: Record<string, MasteryState> = {}
    cards.forEach((card) => {
      const saved = localStorage.getItem(`codeshelf-mastery-${card.id}`) as MasteryState
      initialMastery[card.id] = saved || null
    })
    setMasteryMap(initialMastery)
  }, [cards])

  // Handle shuffling toggle
  const toggleShuffle = () => {
    setIsFlipped(false)
    setShowHint(false)
    if (isShuffled) {
      setShuffledCards([...cards])
      setIsShuffled(false)
    } else {
      const shuffled = [...shuffledCards].sort(() => Math.random() - 0.5)
      setShuffledCards(shuffled)
      setIsShuffled(true)
    }
    setCurrentIndex(0)
  }

  const currentCard = shuffledCards[currentIndex]

  // Keyboard navigation
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (currentIndex >= shuffledCards.length) return

      if (e.code === 'Space') {
        e.preventDefault()
        setIsFlipped((prev) => !prev)
      } else if (e.code === 'ArrowRight') {
        handleNext()
      } else if (e.code === 'ArrowLeft') {
        handlePrev()
      }
    }
    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [currentIndex, shuffledCards])

  const handleNext = () => {
    if (currentIndex < shuffledCards.length) {
      setIsFlipped(false)
      setShowHint(false)
      // Small timeout to allow flip animation to reset before changing content
      setTimeout(() => {
        setCurrentIndex((prev) => prev + 1)
      }, 150)
    }
  }

  const handlePrev = () => {
    if (currentIndex > 0) {
      setIsFlipped(false)
      setShowHint(false)
      setTimeout(() => {
        setCurrentIndex((prev) => prev - 1)
      }, 150)
    }
  }

  const markMastery = (cardId: string, state: 'mastered' | 'practice') => {
    localStorage.setItem(`codeshelf-mastery-${cardId}`, state)
    setMasteryMap((prev) => ({ ...prev, [cardId]: state }))
    handleNext()
  }

  const resetProgress = () => {
    if (window.confirm('Are you sure you want to reset study progress for this chapter?')) {
      cards.forEach((card) => {
        localStorage.removeItem(`codeshelf-mastery-${card.id}`)
      })
      const resetMap: Record<string, MasteryState> = {}
      cards.forEach((card) => {
        resetMap[card.id] = null
      })
      setMasteryMap(resetMap)
      setCurrentIndex(0)
      setIsFlipped(false)
      setShowHint(false)
    }
  }

  // Statistics calculation
  const stats = useMemo(() => {
    let masteredCount = 0
    let practiceCount = 0
    cards.forEach((card) => {
      const state = masteryMap[card.id]
      if (state === 'mastered') masteredCount++
      else if (state === 'practice') practiceCount++
    })
    return {
      mastered: masteredCount,
      practice: practiceCount,
      unstudied: cards.length - masteredCount - practiceCount,
    }
  }, [cards, masteryMap])

  // If there are no cards
  if (cards.length === 0) {
    return (
      <div className="study-empty">
        <Brain className="study-empty__icon" size={48} />
        <h3 className="study-empty__title font-display">No study cards in this chapter</h3>
        <p className="study-empty__desc">
          This chapter doesn't have any interview prep points or coding exercises yet. Read the chapter in reading mode to review!
        </p>
        <button onClick={onBackToReading} className="study-btn study-btn--primary">
          <BookOpen size={16} />
          <span>Back to Reading</span>
        </button>
      </div>
    )
  }

  // Summary screen
  if (currentIndex >= shuffledCards.length) {
    return (
      <div className="study-summary">
        <div className="study-summary__header">
          <Sparkles className="study-summary__sparkle" size={40} />
          <h2 className="study-summary__title font-display">Revision Complete!</h2>
          <p className="study-summary__desc">You have gone through all {cards.length} revision cards in this chapter.</p>
        </div>

        <div className="study-summary__grid">
          <div className="study-summary__stat study-summary__stat--mastered">
            <span className="study-summary__stat-label">Mastered</span>
            <span className="study-summary__stat-value">{stats.mastered}</span>
          </div>
          <div className="study-summary__stat study-summary__stat--practice">
            <span className="study-summary__stat-label">Needs Practice</span>
            <span className="study-summary__stat-value">{stats.practice}</span>
          </div>
          <div className="study-summary__stat study-summary__stat--unstudied">
            <span className="study-summary__stat-label">Not Rated</span>
            <span className="study-summary__stat-value">{stats.unstudied}</span>
          </div>
        </div>

        <div className="study-summary__progress-container">
          <div className="study-summary__progress-text">
            <span>Overall Mastery</span>
            <span>{Math.round((stats.mastered / cards.length) * 100)}%</span>
          </div>
          <div className="study-summary__progress-bar">
            <div 
              className="study-summary__progress-fill" 
              style={{ width: `${(stats.mastered / cards.length) * 100}%` }}
            />
          </div>
        </div>

        <div className="study-summary__actions">
          <button 
            onClick={() => { setCurrentIndex(0); setIsFlipped(false); }} 
            className="study-btn study-btn--primary"
          >
            <RotateCcw size={16} />
            <span>Restart Review</span>
          </button>
          <button 
            onClick={() => { setIsFlipped(false); toggleShuffle(); }} 
            className="study-btn study-btn--secondary"
          >
            <Shuffle size={16} />
            <span>Shuffle & Restart</span>
          </button>
          <button onClick={onBackToReading} className="study-btn study-btn--secondary">
            <BookOpen size={16} />
            <span>Back to Reading</span>
          </button>
        </div>
      </div>
    )
  }

  const currentMastery = masteryMap[currentCard.id]

  return (
    <div className="study-viewer">
      {/* Top dashboard / Progress Bar */}
      <div className="study-dashboard">
        <div className="study-progress-info">
          <span className="study-progress-badge">
            Card {currentIndex + 1} of {shuffledCards.length}
          </span>
          {isShuffled && <span className="study-shuffle-badge"><Shuffle size={12} /> Shuffled</span>}
        </div>
        <div className="study-progress-bar">
          <div 
            className="study-progress-fill" 
            style={{ width: `${((currentIndex) / shuffledCards.length) * 100}%` }}
          />
        </div>
        
        {/* Quick status dashboard */}
        <div className="study-status-row">
          <div className="study-status-item">
            <span className="study-status-dot study-status-dot--mastered" />
            <span>Mastered: <strong>{stats.mastered}</strong></span>
          </div>
          <div className="study-status-item">
            <span className="study-status-dot study-status-dot--practice" />
            <span>Practice: <strong>{stats.practice}</strong></span>
          </div>
          <button onClick={resetProgress} className="study-btn-reset" title="Reset all statuses for this chapter">
            <RotateCcw size={12} /> Reset Study Stats
          </button>
        </div>
      </div>

      {/* Main Flashcard Container */}
      <div className="study-card-wrapper">
        <div 
          className={`study-card ${isFlipped ? 'study-card--flipped' : ''}`}
          onClick={() => setIsFlipped((prev) => !prev)}
        >
          {/* Card Front */}
          <div className={`study-card__face study-card__face--front ${currentMastery ? `study-card__face--${currentMastery}` : ''}`}>
            <div className="study-card__badge-type">
              {currentCard.type === 'interview' ? '📌 Interview Prep' : '⭐ Exercise'}
            </div>
            
            <div className="study-card__main-content">
              <h3 className="study-card__title font-display">{currentCard.title}</h3>
              <div className="study-card__question">
                <MarkdownContent content={currentCard.question} topic={topic} />
              </div>
            </div>

            {/* Hint support for Exercises */}
            {currentCard.hint && (
              <div className="study-card__hint-container" onClick={(e) => e.stopPropagation()}>
                {!showHint ? (
                  <button onClick={() => setShowHint(true)} className="study-card__hint-trigger">
                    <Lightbulb size={13} />
                    <span>Reveal Hint</span>
                  </button>
                ) : (
                  <div className="study-card__hint-text">
                    <strong>Hint:</strong> {currentCard.hint}
                  </div>
                )}
              </div>
            )}

            <div className="study-card__footer">
              <span className="study-card__hint-flip">Click card or press Space to flip and reveal answer</span>
            </div>
          </div>

          {/* Card Back */}
          <div className={`study-card__face study-card__face--back ${currentMastery ? `study-card__face--${currentMastery}` : ''}`}>
            <div className="study-card__badge-type">
              {currentCard.type === 'interview' ? '📌 Answer' : '✅ Solution'}
            </div>

            <div className="study-card__main-content">
              <h3 className="study-card__title font-display">{currentCard.title} - Answer</h3>
              <div className="study-card__answer">
                <MarkdownContent content={currentCard.answer} topic={topic} />
              </div>
            </div>

            <div className="study-card__footer">
              <span className="study-card__hint-flip">Click card or press Space to flip back</span>
            </div>
          </div>
        </div>
      </div>

      {/* Action panel underneath card */}
      <div className="study-actions-panel">
        <div className="study-navigation-group">
          <button 
            onClick={handlePrev} 
            disabled={currentIndex === 0} 
            className="study-btn study-btn--icon" 
            title="Previous Card (ArrowLeft)"
          >
            <ArrowLeft size={18} />
          </button>
          
          <button 
            onClick={() => setIsFlipped((prev) => !prev)} 
            className="study-btn study-btn--secondary"
          >
            <RotateCw size={14} />
            <span>{isFlipped ? 'Show Question' : 'Show Answer'}</span>
          </button>

          <button 
            onClick={handleNext} 
            className="study-btn study-btn--icon" 
            title="Next Card (ArrowRight)"
          >
            <ArrowRight size={18} />
          </button>
        </div>

        {/* Self-Rating Mastery options (only show when flipped to encourage checking the answer first) */}
        {isFlipped && (
          <div className="study-mastery-rating animate-fade-in">
            <button 
              onClick={() => markMastery(currentCard.id, 'practice')} 
              className="study-btn-rate study-btn-rate--practice"
            >
              <XCircle size={16} />
              <span>Needs Practice</span>
            </button>
            <button 
              onClick={() => markMastery(currentCard.id, 'mastered')} 
              className="study-btn-rate study-btn-rate--mastered"
            >
              <CheckCircle2 size={16} />
              <span>Mastered!</span>
            </button>
          </div>
        )}

        <div className="study-config-row">
          <button 
            onClick={toggleShuffle} 
            className={`study-btn-config ${isShuffled ? 'study-btn-config--active' : ''}`}
          >
            <Shuffle size={12} />
            <span>Shuffle Cards</span>
          </button>
        </div>
      </div>
    </div>
  )
}
