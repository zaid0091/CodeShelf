import { Link } from 'react-router-dom'
import type { ButtonHTMLAttributes, ReactNode } from 'react'

type NavbarButtonTone = 'dark' | 'light'
type NavbarButtonEmphasis = 'default' | 'accent'

interface NavbarButtonLinkProps {
  to: string
  children: ReactNode
  tone?: NavbarButtonTone
  emphasis?: NavbarButtonEmphasis
  className?: string
}

interface NavbarIconButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  tone?: NavbarButtonTone
  children: ReactNode
  className?: string
  'aria-label': string
}

const toneClass: Record<NavbarButtonTone, string> = {
  dark: 'navbar-btn--dark',
  light: 'navbar-btn--light',
}

export function NavbarButtonLink({
  to,
  children,
  tone = 'dark',
  emphasis = 'default',
  className = '',
}: NavbarButtonLinkProps) {
  return (
    <Link
      to={to}
      className={[
        'navbar-btn',
        toneClass[tone],
        emphasis === 'accent' ? 'navbar-btn--accent' : '',
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    >
      <span className="navbar-btn__border" aria-hidden />
      <span className="navbar-btn__shine" aria-hidden />
      <span className="navbar-btn__label">{children}</span>
    </Link>
  )
}

export function NavbarIconButton({
  tone = 'light',
  children,
  className = '',
  style,
  ...props
}: NavbarIconButtonProps) {
  return (
    <button
      type="button"
      className={['navbar-btn navbar-btn--icon', toneClass[tone], className]
        .filter(Boolean)
        .join(' ')}
      style={{ position: 'relative', zIndex: 2, ...style }}
      {...props}
    >
      <span className="navbar-btn__border" aria-hidden />
      <span className="navbar-btn__shine" aria-hidden />
      <span className="navbar-btn__label">{children}</span>
    </button>
  )
}
