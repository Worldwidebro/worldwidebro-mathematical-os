import { useEffect, useRef, useState } from 'react'

function easeOutCubic(t) {
  return 1 - Math.pow(1 - t, 3)
}

export function useCountUp(end, { duration = 2000, startDelay = 1200 } = {}) {
  const [value, setValue] = useState(0)
  const frameRef = useRef(null)

  useEffect(() => {
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    if (reduceMotion) {
      setValue(end)
      return
    }

    let startTime = null
    const startTimer = setTimeout(() => {
      const step = (timestamp) => {
        if (startTime === null) startTime = timestamp
        const elapsed = timestamp - startTime
        const progress = Math.min(elapsed / duration, 1)
        setValue(end * easeOutCubic(progress))
        if (progress < 1) {
          frameRef.current = requestAnimationFrame(step)
        }
      }
      frameRef.current = requestAnimationFrame(step)
    }, startDelay)

    return () => {
      clearTimeout(startTimer)
      if (frameRef.current) cancelAnimationFrame(frameRef.current)
    }
  }, [end, duration, startDelay])

  return value
}
