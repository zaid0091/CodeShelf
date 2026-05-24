import { Moon, Sun } from 'lucide-react'
import { useTheme } from '@/hooks/useTheme'
import { NavbarIconButton } from '@/components/ui/NavbarButton'

export function DocsThemeToggle() {
  const { theme, toggleTheme } = useTheme()
  const isDark = theme === 'dark'

  return (
    <NavbarIconButton
      type="button"
      tone={isDark ? 'dark' : 'light'}
      className="docs-theme-toggle shrink-0"
      aria-label={isDark ? 'Switch to light mode' : 'Switch to dark mode'}
      onClick={(e) => {
        e.preventDefault()
        e.stopPropagation()
        toggleTheme()
      }}
    >
      {isDark ? <Sun size={18} strokeWidth={1.5} /> : <Moon size={18} strokeWidth={1.5} />}
    </NavbarIconButton>
  )
}
