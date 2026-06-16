export interface Flashcard {
  id: string
  type: 'interview' | 'exercise'
  title: string
  question: string
  answer: string
  hint?: string
}

export function parseFlashcards(markdown: string): Flashcard[] {
  const cards: Flashcard[] = []
  const lines = markdown.split('\n')

  // 1. Parse Interview Points
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim()
    if (line.startsWith('>') && line.includes('📌')) {
      // Found an interview point blockquote
      // Collect the blockquote lines
      const blockquoteLines: string[] = []
      let j = i
      while (j < lines.length && lines[j].trim().startsWith('>')) {
        blockquoteLines.push(lines[j].trim().substring(1).trim())
        j++
      }

      const blockText = blockquoteLines.join('\n')
      const ipMatch = blockText.match(/\*\*📌\s*Interview\s*Point\s*(\d+):\s*(.*?)\*\*(?:\s*\n)?([\s\S]*)/i)

      if (ipMatch) {
        const num = ipMatch[1]
        const question = ipMatch[2].trim()
        let answer = ipMatch[3].trim()

        // If the blockquote did not contain the answer, look at the lines below it
        if (!answer) {
          const subsequentLines: string[] = []
          let k = j
          // Skip empty lines
          while (k < lines.length && !lines[k].trim()) {
            k++
          }
          // Collect lines until next blockquote, next header, or horizontal rule
          while (k < lines.length) {
            const subLine = lines[k].trim()
            if (subLine.startsWith('>') || subLine.startsWith('#') || subLine === '---') {
              break
            }
            subsequentLines.push(lines[k])
            k++
          }
          answer = subsequentLines.join('\n').trim()
        }

        cards.push({
          id: `ip-${num}-${question.substring(0, 20).replace(/[^a-zA-Z0-9]/g, '-')}`,
          type: 'interview',
          title: `Interview Point ${num}`,
          question,
          answer,
        })
      }

      // Advance outer loop index to end of blockquote
      i = j - 1
    }
  }

  // 2. Parse Exercises
  let inExercise = false
  let exerciseContent: string[] = []
  let exerciseTitle = ''

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i]
    if (line.startsWith('### Exercise')) {
      if (inExercise) {
        processExercise(exerciseTitle, exerciseContent.join('\n'), cards)
        exerciseContent = []
      }
      inExercise = true
      exerciseTitle = line.replace('###', '').trim()
    } else if (inExercise && line.startsWith('##')) {
      processExercise(exerciseTitle, exerciseContent.join('\n'), cards)
      inExercise = false
      exerciseContent = []
    } else if (inExercise) {
      exerciseContent.push(line)
    }
  }
  if (inExercise) {
    processExercise(exerciseTitle, exerciseContent.join('\n'), cards)
  }

  return cards
}

function processExercise(title: string, rawContent: string, cards: Flashcard[]) {
  let task = ''
  const taskMatch = rawContent.match(/\*\*Task:\*\*\s*([\s\S]*?)(?=\n\s*<details>|\n\n|$)/i)
  if (taskMatch) {
    task = taskMatch[1].trim()
  } else {
    const cleanContent = rawContent.replace(/<details>[\s\S]*?<\/details>/gi, '').trim()
    task = cleanContent
  }

  let hint: string | undefined = undefined
  const hintMatch = rawContent.match(/<details>\s*<summary>💡 Hint[^]*?<\/summary>([\s\S]*?)<\/details>/i)
  if (hintMatch) {
    hint = hintMatch[1].trim()
  }

  let answer = ''
  const solutionMatch = rawContent.match(/<details>\s*<summary>✅ Solution[^]*?<\/summary>([\s\S]*?)<\/details>/i)
  if (solutionMatch) {
    answer = solutionMatch[1].trim()
  }

  if (task || answer) {
    cards.push({
      id: `ex-${title.substring(0, 20).replace(/[^a-zA-Z0-9]/g, '-')}`,
      type: 'exercise',
      title,
      question: task,
      answer: answer || 'No solution provided.',
      hint,
    })
  }
}
