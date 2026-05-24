import { FileQuestion } from 'lucide-react'
import { ButtonLink } from '@/components/ui/Button'

export function NotFoundPage() {
  return (
    <div className="flex flex-col items-center justify-center py-24 text-center">
      <FileQuestion size={48} strokeWidth={1.5} className="text-shade-40 mb-6" />
      <h1 className="font-display text-display-lg text-ink mb-3">Page not found</h1>
      <p className="text-body-lg text-shade-50 mb-10 max-w-sm">
        The page you're looking for doesn't exist or may have been moved.
      </p>
      <ButtonLink to="/" variant="primary-pill">
        Back to home
      </ButtonLink>
    </div>
  )
}
