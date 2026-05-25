import { useReadingProgress } from '@/hooks/useReadingProgress'

export function DocReadingProgress() {
  const progress = useReadingProgress()

  return (
    <div className="doc-progress" aria-hidden>
      <div
        className="doc-progress__fill"
        style={{ transform: `scaleX(${progress.toFixed(4)})` }}
      />
    </div>
  )
}
