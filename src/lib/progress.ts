export interface CompletedChapters {
  [topicId: string]: string[]
}

const PROGRESS_KEY = 'codeshelf_progress'
const STREAK_KEY = 'codeshelf_streak'

export function getCompletedChapters(): CompletedChapters {
  if (typeof window === 'undefined') return {}
  const data = localStorage.getItem(PROGRESS_KEY)
  return data ? JSON.parse(data) : {}
}

export function markChapterCompleted(topicId: string, slug: string) {
  if (typeof window === 'undefined') return
  const progress = getCompletedChapters()
  
  if (!progress[topicId]) {
    progress[topicId] = []
  }
  
  if (!progress[topicId].includes(slug)) {
    progress[topicId].push(slug)
    localStorage.setItem(PROGRESS_KEY, JSON.stringify(progress))
    updateStreak()
    
    // Dispatch custom event to notify listeners (like navbar or dashboard) of updates
    window.dispatchEvent(new Event('codeshelf_progress_updated'))
  }
}

export function getStreak(): number {
  if (typeof window === 'undefined') return 0
  const streakData = localStorage.getItem(STREAK_KEY)
  if (!streakData) return 0
  
  try {
    const { currentStreak, lastReadDate } = JSON.parse(streakData)
    const today = new Date().toISOString().split('T')[0]
    
    const yesterday = new Date()
    yesterday.setDate(yesterday.getDate() - 1)
    const yesterdayStr = yesterday.toISOString().split('T')[0]
    
    if (lastReadDate === today || lastReadDate === yesterdayStr) {
      return currentStreak
    }
  } catch (e) {
    return 0
  }
  
  return 0
}

function updateStreak() {
  const streakData = localStorage.getItem(STREAK_KEY)
  const today = new Date().toISOString().split('T')[0]
  
  if (!streakData) {
    localStorage.setItem(STREAK_KEY, JSON.stringify({ currentStreak: 1, lastReadDate: today }))
    return
  }
  
  try {
    const { currentStreak, lastReadDate } = JSON.parse(streakData)
    
    if (lastReadDate === today) {
      // Already read a chapter today
      return
    }
    
    const yesterday = new Date()
    yesterday.setDate(yesterday.getDate() - 1)
    const yesterdayStr = yesterday.toISOString().split('T')[0]
    
    if (lastReadDate === yesterdayStr) {
      // Consecutive day read
      localStorage.setItem(
        STREAK_KEY,
        JSON.stringify({ currentStreak: currentStreak + 1, lastReadDate: today })
      )
    } else {
      // Break in streak, reset to 1
      localStorage.setItem(
        STREAK_KEY,
        JSON.stringify({ currentStreak: 1, lastReadDate: today })
      )
    }
  } catch (e) {
    localStorage.setItem(STREAK_KEY, JSON.stringify({ currentStreak: 1, lastReadDate: today }))
  }
}

export function clearAllProgress() {
  if (typeof window === 'undefined') return
  localStorage.removeItem(PROGRESS_KEY)
  localStorage.removeItem(STREAK_KEY)
  window.dispatchEvent(new Event('codeshelf_progress_updated'))
}
