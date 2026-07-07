import { useEffect, useState } from 'react'

export function TypewriterHeading({ text, splitAt, speed = 35, startDelay = 400 }) {
  const [visibleCount, setVisibleCount] = useState(0)
  const [done, setDone] = useState(false)

  useEffect(() => {
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    if (reduceMotion) {
      setVisibleCount(text.length)
      setDone(true)
      return
    }

    let i = 0
    let intervalId = null
    const startTimer = setTimeout(() => {
      intervalId = setInterval(() => {
        i += 1
        setVisibleCount(i)
        if (i >= text.length) {
          clearInterval(intervalId)
          setDone(true)
        }
      }, speed)
    }, startDelay)

    return () => {
      clearTimeout(startTimer)
      if (intervalId) clearInterval(intervalId)
    }
  }, [text, speed, startDelay])

  const visibleText = text.slice(0, visibleCount)
  const darkPart = visibleText.slice(0, splitAt)
  const lightPart = visibleText.slice(splitAt)

  return (
    <h1 className="hero-heading">
      <span className="heading-dark">{darkPart}</span>
      <span className="heading-light">{lightPart}</span>
      {!done && <span className="type-cursor" aria-hidden="true" />}
    </h1>
  )
}
