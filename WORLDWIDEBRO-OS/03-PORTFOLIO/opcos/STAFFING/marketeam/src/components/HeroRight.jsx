import { useCountUp } from '../hooks/useCountUp'

const AVATARS = [
  {
    src: 'https://polo-pecan-73837341.figma.site/_assets/v11/aa51718fb3af3637e6d666b6543fc27a175fada6.png',
    orbit: 1,
    angle: 270,
    radius: 177,
    size: 58,
    shape: 'square',
    glow: 'purple',
    delay: 0.6,
  },
  {
    src: 'https://polo-pecan-73837341.figma.site/_assets/v11/ca755f7f93c1126fb8bdbf99ab364a33aa9ab272.png',
    orbit: 2,
    angle: 60,
    radius: 251,
    size: 58,
    shape: 'round',
    glow: 'yellow',
    delay: 0.9,
  },
  {
    src: 'https://polo-pecan-73837341.figma.site/_assets/v11/dc01064c7093dcc32674876ee3cf5e41c4a485c6.png',
    orbit: 2,
    angle: 180,
    radius: 251,
    size: 78,
    shape: 'round',
    glow: 'pink',
    delay: 1.2,
  },
  {
    src: 'https://polo-pecan-73837341.figma.site/_assets/v11/d5470a58b02388336141575048720f19a50de832.png',
    orbit: 2,
    angle: 300,
    radius: 251,
    size: 58,
    shape: 'square',
    glow: 'blue',
    delay: 1.4,
  },
  {
    src: 'https://polo-pecan-73837341.figma.site/_assets/v11/018736aa5d0275c4ce56cfebaf2ae3007d81ca1e.png',
    orbit: 3,
    angle: 130,
    radius: 325,
    size: 88,
    shape: 'round',
    glow: 'pink',
    delay: 1.6,
  },
  {
    src: 'https://polo-pecan-73837341.figma.site/_assets/v11/c76d8a0b99676de31c014344bfaf75bad090758d.png',
    orbit: 4,
    angle: 30,
    radius: 399,
    size: 58,
    shape: 'round',
    glow: 'purple',
    delay: 1.8,
  },
  {
    src: 'https://polo-pecan-73837341.figma.site/_assets/v11/7b1b5f039de7b54cc9913e96c1923c3b15a157fa.png',
    orbit: 4,
    angle: 95,
    radius: 399,
    size: 88,
    shape: 'square',
    borderRadius: 24,
    glow: 'orange',
    delay: 2,
  },
  {
    src: 'https://polo-pecan-73837341.figma.site/_assets/v11/9ae171d8895199349755c43fbff00e122221a027.png',
    orbit: 4,
    angle: 220,
    radius: 399,
    size: 88,
    shape: 'square',
    borderRadius: 24,
    glow: 'pink',
    delay: 2.15,
  },
  {
    src: 'https://polo-pecan-73837341.figma.site/_assets/v11/926c9eb7b4bc1df846fa0e39f0b0dc3fefd80671.png',
    orbit: 4,
    angle: 320,
    radius: 399,
    size: 58,
    shape: 'round',
    glow: 'purple',
    delay: 2.3,
  },
]

function Avatar({ src, angle, radius, size, shape, glow, borderRadius, delay }) {
  return (
    <div
      className={`orbit-avatar glow-${glow} shape-${shape}`}
      style={{
        width: size,
        height: size,
        borderRadius: shape === 'round' ? '50%' : borderRadius || 20,
        transform: `translate(-50%, -50%) rotate(${angle}deg) translate(${radius}px) rotate(${-angle}deg)`,
        animationDelay: `${delay}s`,
      }}
    >
      <img src={src} alt="" width={size} height={size} loading="lazy" />
    </div>
  )
}

export function HeroRight() {
  const count = useCountUp(20, { duration: 2000, startDelay: 1200 })

  return (
    <div className="hero-right">
      <div className="circles-stage">
        <div className="orbit orbit-4">
          <div className="orbit-border" />
        </div>
        <div className="orbit orbit-3">
          <div className="orbit-border" />
        </div>
        <div className="orbit orbit-2">
          <div className="orbit-border" />
        </div>
        <div className="orbit orbit-1">
          <div className="orbit-border" />
          <div className="orbit-center">
            <span className="center-count">{count.toFixed(0)}k+</span>
            <span className="center-label">Specialists</span>
          </div>
        </div>

        {AVATARS.map((a, i) => (
          <Avatar key={i} {...a} />
        ))}
      </div>
    </div>
  )
}
