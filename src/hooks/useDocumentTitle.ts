import { useEffect } from 'react'

export function useDocumentTitle(title: string) {
  useEffect(() => {
    document.title = title
    return () => {
      document.title = 'CodeShelf — Personal Coding Notes'
    }
  }, [title])
}
