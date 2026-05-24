import { Link } from 'react-router-dom'
import type { ButtonHTMLAttributes, ReactNode } from 'react'

type ButtonVariant =
  | 'primary-pill'
  | 'outline-on-dark'
  | 'outline-on-light'
  | 'aloe-pill'
  | 'ghost-on-dark'
  | 'ghost-on-light'

const variants: Record<ButtonVariant, string> = {
  'primary-pill':
    'bg-ink text-on-primary hover:bg-shade-70 active:bg-shade-70',
  'outline-on-dark':
    'bg-canvas-night text-on-primary border-2 border-on-primary hover:bg-canvas-night-elevated',
  'outline-on-light':
    'bg-canvas-light text-ink border border-ink hover:bg-canvas-cream',
  'aloe-pill': 'bg-aloe text-ink hover:brightness-95 active:brightness-90',
  'ghost-on-dark':
    'bg-transparent text-on-primary hover:bg-white/10',
  'ghost-on-light':
    'bg-transparent text-ink hover:bg-shade-30/60',
}

const base =
  'inline-flex items-center justify-center gap-2 rounded-pill px-6 py-3 text-body-md font-medium transition-all duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ink/20'

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant
  children: ReactNode
  className?: string
}

export function Button({
  variant = 'primary-pill',
  children,
  className = '',
  ...props
}: ButtonProps) {
  return (
    <button className={`${base} ${variants[variant]} ${className}`} {...props}>
      {children}
    </button>
  )
}

interface ButtonLinkProps {
  to: string
  variant?: ButtonVariant
  children: ReactNode
  className?: string
}

export function ButtonLink({
  to,
  variant = 'primary-pill',
  children,
  className = '',
}: ButtonLinkProps) {
  return (
    <Link to={to} className={`${base} ${variants[variant]} ${className}`}>
      {children}
    </Link>
  )
}
