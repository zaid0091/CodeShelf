const TOPIC_ICON_SRC: Record<string, string> = {
  typescript: '/icons/topics/typescript.svg',
  javascript: '/icons/topics/javascript.svg',
  react: '/icons/topics/react.svg',
  python: '/icons/topics/python.svg',
  django: '/icons/topics/django.svg',
  drf: '/icons/topics/drf.svg',
}

interface TopicIconProps {
  topicId: string
  size?: number
  className?: string
}

export function TopicIcon({ topicId, size = 20, className = '' }: TopicIconProps) {
  const src = TOPIC_ICON_SRC[topicId]

  if (!src) {
    return (
      <span
        className={`inline-flex shrink-0 items-center justify-center rounded-md bg-white/10 text-[0.65rem] font-medium text-on-primary ${className}`}
        style={{ width: size, height: size }}
        aria-hidden
      >
        ?
      </span>
    )
  }

  return (
    <img
      src={src}
      alt=""
      width={size}
      height={size}
      className={`topic-icon shrink-0 object-contain ${className}`}
      loading="lazy"
      decoding="async"
      aria-hidden
    />
  )
}
