/**
 * Split a text-bearing element into per-word and per-character spans
 * while preserving inline elements like <br> and <em>.
 *
 * Returns the created spans and a `cleanup` function that restores the
 * element's original markup. Text nodes are walked individually so multi-line
 * headings (e.g. with `<br />`) keep their line breaks.
 */
export interface SplitTextResult {
  chars: HTMLElement[]
  words: HTMLElement[]
  cleanup: () => void
}

export function splitTextNodes(el: HTMLElement): SplitTextResult {
  const originalHTML = el.innerHTML

  const chars: HTMLElement[] = []
  const words: HTMLElement[] = []

  const textNodes: Text[] = []
  const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT)
  let node = walker.nextNode()
  while (node) {
    if (node.nodeValue && node.nodeValue.replace(/\s/g, '').length > 0) {
      textNodes.push(node as Text)
    }
    node = walker.nextNode()
  }

  textNodes.forEach((textNode) => {
    const parent = textNode.parentNode
    if (!parent) return

    const value = textNode.nodeValue ?? ''
    const fragment = document.createDocumentFragment()

    value.split(/(\s+)/).forEach((part) => {
      if (!part) return

      if (/^\s+$/.test(part)) {
        fragment.appendChild(document.createTextNode(part))
        return
      }

      const word = document.createElement('span')
      word.className = 'split-word'
      word.setAttribute('aria-hidden', 'false')

      for (const ch of Array.from(part)) {
        const charSpan = document.createElement('span')
        charSpan.className = 'split-char'
        charSpan.textContent = ch
        word.appendChild(charSpan)
        chars.push(charSpan)
      }

      fragment.appendChild(word)
      words.push(word)
    })

    parent.replaceChild(fragment, textNode)
  })

  el.classList.add('is-split')

  return {
    chars,
    words,
    cleanup() {
      el.classList.remove('is-split')
      el.innerHTML = originalHTML
    },
  }
}
