import { TypewriterHeading } from './TypewriterHeading'

const HEADLINE =
  "Unlock Top Marketing Talent You Thought Was Out of Reach - Now Just One Click Away!"

export function HeroLeft() {
  return (
    <div className="hero-left">
      <TypewriterHeading text={HEADLINE} splitAt={67} />

      <div className="cta-row">
        <div className="btn-border-wrap">
          <button type="button" className="btn-pill btn-start">
            Start Project
            <svg width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden="true">
              <path
                d="M6.5 3.5L11.5 9L6.5 14.5"
                stroke="currentColor"
                strokeWidth="1.8"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
          </button>
        </div>
      </div>

      <div className="cursor-tag">
        <svg width="28" height="32" viewBox="0 0 28 32" fill="none" aria-hidden="true">
          <path
            d="M2 2L2 26L9 20L13.5 29L18 27L13.5 18L22 18L2 2Z"
            fill="#A068FF"
          />
        </svg>
        <span className="cursor-badge">David</span>
      </div>
    </div>
  )
}
