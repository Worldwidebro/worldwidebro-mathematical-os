import { ArrowRight } from 'lucide-react'

export default function Hero() {
  return (
    <div className="relative z-10 flex h-[calc(100vh-80px)] flex-col justify-between px-6 pb-10 pt-12 sm:pb-12 sm:pt-16 md:px-12 md:pb-16 md:pt-20 lg:px-16">
      <div className="max-w-3xl">
        <p
          className="mb-4 text-xs text-white/90 sm:mb-6 sm:text-sm"
          style={{ animation: 'fadeSlideUp 0.8s ease 0.2s both' }}
        >
          Brand &amp; Visual Storytelling
        </p>

        <h1
          className="text-3xl font-medium leading-[1.1] tracking-tight text-white sm:text-5xl md:text-6xl lg:text-7xl"
          style={{ animation: 'fadeSlideUp 0.8s ease 0.4s both' }}
        >
          Shaping visual
          <br />
          narratives,
          <br />
          one pixel at a time.
        </h1>
      </div>

      <div>
        <p
          className="mb-5 max-w-sm text-sm leading-relaxed text-white/60 sm:mb-6 sm:max-w-lg sm:text-base md:text-lg"
          style={{ animation: 'fadeSlideUp 0.8s ease 0.7s both' }}
        >
          Turning vision into reality through craft, motion, and an endless pursuit of beauty.
        </p>

        <button
          type="button"
          className="inline-flex items-center gap-2 rounded-lg bg-white px-5 py-2.5 text-sm font-medium text-black transition-transform hover:scale-105 sm:px-6 sm:py-3"
          style={{ animation: 'fadeSlideUp 0.8s ease 0.9s both' }}
        >
          Explore Work
          <ArrowRight size={16} />
        </button>
      </div>
    </div>
  )
}
