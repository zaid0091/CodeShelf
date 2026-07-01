import { useNavigate } from 'react-router-dom'
import { Check, Lock, BookOpen } from 'lucide-react'
import type { DocPage } from '@/lib/types'

interface InteractiveRoadmapProps {
  pages: DocPage[]
  completedPages: string[]
}

export function InteractiveRoadmap({
  pages,
  completedPages,
}: InteractiveRoadmapProps) {
  const navigate = useNavigate()
  
  const cols = 3
  const paddingX = 100
  const paddingY = 80
  const colWidth = 300
  const rowHeight = 180

  const nodes = pages.map((p, idx) => {
    const row = Math.floor(idx / cols)
    let col = idx % cols
    const isReverse = row % 2 === 1
    if (isReverse) {
      col = (cols - 1) - col
    }
    return {
      x: paddingX + col * colWidth,
      y: paddingY + row * rowHeight,
      page: p,
      index: idx,
    }
  })

  // Find next target chapter (first uncompleted one)
  const nextUncompletedIndex = pages.findIndex(p => !completedPages.includes(p.slug))

  const connectionPaths = []
  for (let i = 0; i < nodes.length - 1; i++) {
    const n1 = nodes[i]
    const n2 = nodes[i + 1]
    const isCompleted = completedPages.includes(n1.page.slug) && completedPages.includes(n2.page.slug)
    
    let d = ''
    if (n1.y === n2.y) {
      d = `M ${n1.x} ${n1.y} L ${n2.x} ${n2.y}`
    } else {
      const isRight = n1.x > 500
      if (isRight) {
        d = `M ${n1.x} ${n1.y} C ${n1.x + 100} ${n1.y + 60}, ${n2.x + 100} ${n2.y - 60}, ${n2.x} ${n2.y}`
      } else {
        d = `M ${n1.x} ${n1.y} C ${n1.x - 100} ${n1.y + 60}, ${n2.x - 100} ${n2.y - 60}, ${n2.x} ${n2.y}`
      }
    }
    connectionPaths.push({ d, isCompleted })
  }

  const totalRows = Math.ceil(pages.length / cols)
  const svgHeight = paddingY + (totalRows - 1) * rowHeight + 150

  return (
    <div className="roadmap-container">
      <div className="roadmap-legend">
        <div className="roadmap-legend__item">
          <span className="roadmap-legend__indicator roadmap-legend__indicator--completed" />
          <span>Completed</span>
        </div>
        <div className="roadmap-legend__item">
          <span className="roadmap-legend__indicator roadmap-legend__indicator--active" />
          <span>Current Target</span>
        </div>
        <div className="roadmap-legend__item">
          <span className="roadmap-legend__indicator roadmap-legend__indicator--pending" />
          <span>Locked / Pending</span>
        </div>
      </div>

      <div className="roadmap-svg-wrapper">
        <svg
          viewBox={`0 0 800 ${svgHeight}`}
          width="100%"
          height="100%"
          className="roadmap-svg"
        >
          <defs>
            <filter id="glow-aloe" x="-25%" y="-25%" width="150%" height="150%">
              <feGaussianBlur stdDeviation="8" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
            <filter id="glow-gold" x="-25%" y="-25%" width="150%" height="150%">
              <feGaussianBlur stdDeviation="8" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
          </defs>

          {/* Connection Lines */}
          {connectionPaths.map((path, idx) => (
            <path
              key={idx}
              d={path.d}
              className={`roadmap-path ${path.isCompleted ? 'roadmap-path--completed' : ''}`}
            />
          ))}

          {/* Nodes */}
          {nodes.map((node) => {
            const isCompleted = completedPages.includes(node.page.slug)
            const isActive = node.index === nextUncompletedIndex
            const isLocked = node.index > nextUncompletedIndex && nextUncompletedIndex !== -1

            let statusClass = 'pending'
            if (isCompleted) statusClass = 'completed'
            else if (isActive) statusClass = 'active'

            return (
              <g 
                key={node.page.slug}
                className={`roadmap-node-group roadmap-node-group--${statusClass}`}
                onClick={() => navigate(node.page.path)}
              >
                {/* Node Connection Anchor Circle */}
                <circle
                  cx={node.x}
                  cy={node.y}
                  r={16}
                  className="roadmap-anchor-circle"
                  filter={isCompleted ? "url(#glow-aloe)" : isActive ? "url(#glow-gold)" : undefined}
                />
                
                {/* Embedded Lucide Icons */}
                <g transform={`translate(${node.x - 8}, ${node.y - 8})`} className="roadmap-icon-g">
                  {isCompleted ? (
                    <Check size={16} color="#ffffff" />
                  ) : isLocked ? (
                    <Lock size={16} color="var(--color-shade-40)" />
                  ) : (
                    <BookOpen size={16} color="var(--color-accent)" />
                  )}
                </g>

                {/* HTML Node Information Card */}
                <foreignObject
                  x={node.x - 90}
                  y={node.y + 24}
                  width={180}
                  height={110}
                  className="roadmap-foreign-object"
                >
                  <div className={`roadmap-card roadmap-card--${statusClass}`}>
                    <span className="roadmap-card__border" aria-hidden />
                    <span className="roadmap-card__badge">
                      Ch {node.index}
                    </span>
                    <h3 className="roadmap-card__title font-display">
                      {node.page.title.replace(/Ch \d+:\s*/, '').replace(/Overview/, '')}
                    </h3>
                  </div>
                </foreignObject>
              </g>
            )
          })}
        </svg>
      </div>
    </div>
  )
}
