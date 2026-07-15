import { useEffect, useRef, useState } from 'react';
import { Menu, X } from 'lucide-react';

export type SectorVideo = {
  url: string;
  label: string;
};

export type SectorHeroConfig = {
  logoText: string;
  navLinks: { label: string; href: string }[];
  ctaLabel: string;
  ctaHref: string;
  badgeText: string;
  headingLines: string[];
  subtext: string;
  emailPlaceholder: string;
  emailButtonLabel: string;
  videos: SectorVideo[];
  overlayPngUrl?: string;
  /** index into `videos` that should flip hero content to dark text */
  darkVideoIndex?: number;
  darkColor?: string;
  stats: string[];
};

const TRANSITION_MS = 1000;

function SectorHero({ config }: { config: SectorHeroConfig }) {
  const {
    logoText,
    navLinks,
    ctaLabel,
    ctaHref,
    badgeText,
    headingLines,
    subtext,
    emailPlaceholder,
    emailButtonLabel,
    videos,
    overlayPngUrl,
    darkVideoIndex,
    darkColor = '#182C41',
    stats,
  } = config;

  const [activeVideo, setActiveVideo] = useState(0);
  const [isTransitioning, setIsTransitioning] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);
  const cooldown = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    return () => {
      if (cooldown.current) clearTimeout(cooldown.current);
    };
  }, []);

  function selectVideo(index: number) {
    if (index === activeVideo || isTransitioning) return;
    setActiveVideo(index);
    setIsTransitioning(true);
    cooldown.current = setTimeout(() => setIsTransitioning(false), TRANSITION_MS);
  }

  const isDark = darkVideoIndex !== undefined && activeVideo === darkVideoIndex;
  const contentColor = isDark ? darkColor : '#ffffff';

  return (
    <section className="relative w-full h-screen overflow-hidden bg-black">
      {/* Background video layer */}
      {videos.map((video, index) => (
        <video
          key={video.url}
          className="absolute inset-0 h-full w-full object-cover transition-opacity ease-in-out"
          style={{
            opacity: index === activeVideo ? 1 : 0,
            transitionDuration: `${TRANSITION_MS}ms`,
          }}
          src={video.url}
          autoPlay
          muted
          loop
          playsInline
        />
      ))}

      {/* Transparent PNG overlay */}
      {overlayPngUrl && (
        <img
          src={overlayPngUrl}
          alt=""
          aria-hidden="true"
          className="pointer-events-none absolute inset-0 z-[1] h-full w-full object-cover train-bob"
        />
      )}

      {/* Content layer */}
      <div className="relative z-[2] flex h-full w-full flex-col">
        {/* Navigation */}
        <div className="px-6 pt-6 md:px-12 lg:px-16">
          <div className="flex items-center justify-between">
            <span
              className="text-xl italic sm:text-2xl"
              style={{ fontFamily: "'Instrument Serif', serif", color: contentColor }}
            >
              {logoText}
            </span>

            {/* Desktop nav */}
            <div
              className="liquid-glass hidden items-center gap-6 rounded-full px-6 py-2 md:flex"
              style={{ fontFamily: 'system-ui, sans-serif' }}
            >
              {navLinks.map((link) => (
                <a
                  key={link.href}
                  href={link.href}
                  className="text-sm text-white/90 transition-colors duration-200 hover:text-white"
                >
                  {link.label}
                </a>
              ))}
              <a
                href={ctaHref}
                className="whitespace-nowrap rounded-full bg-white px-4 py-1.5 text-sm font-medium text-black transition-colors duration-200 hover:bg-gray-100"
              >
                {ctaLabel}
              </a>
            </div>

            {/* Mobile hamburger */}
            <button
              type="button"
              onClick={() => setMenuOpen((v) => !v)}
              aria-label="Toggle menu"
              className="liquid-glass relative flex h-10 w-10 items-center justify-center rounded-full md:hidden"
            >
              <Menu
                className="absolute h-5 w-5 text-white transition-all duration-300"
                style={{
                  opacity: menuOpen ? 0 : 1,
                  transform: menuOpen ? 'rotate(90deg) scale(0.75)' : 'rotate(0deg) scale(1)',
                }}
              />
              <X
                className="absolute h-5 w-5 text-white transition-all duration-300"
                style={{
                  opacity: menuOpen ? 1 : 0,
                  transform: menuOpen ? 'rotate(0deg) scale(1)' : 'rotate(-90deg) scale(0.75)',
                }}
              />
            </button>
          </div>
        </div>

        {/* Mobile menu overlay */}
        <div
          className={`fixed inset-0 z-50 flex flex-col items-center justify-center bg-black/60 backdrop-blur-sm transition-opacity duration-500 md:hidden ${
            menuOpen ? 'pointer-events-auto opacity-100' : 'pointer-events-none opacity-0'
          }`}
          style={{ transitionTimingFunction: 'cubic-bezier(0.4,0,0.2,1)' }}
        >
          <nav className="flex flex-col items-center gap-8">
            {navLinks.map((link, index) => (
              <a
                key={link.href}
                href={link.href}
                onClick={() => setMenuOpen(false)}
                className="text-3xl text-white transition-all duration-500"
                style={{
                  transitionDelay: menuOpen ? `${100 + index * 50}ms` : '0ms',
                  transform: menuOpen ? 'translateY(0)' : 'translateY(1rem)',
                  opacity: menuOpen ? 1 : 0,
                  transitionTimingFunction: 'cubic-bezier(0.4,0,0.2,1)',
                }}
              >
                {link.label}
              </a>
            ))}
          </nav>
          <a
            href={ctaHref}
            onClick={() => setMenuOpen(false)}
            className="mt-10 rounded-full bg-white px-8 py-3 text-base font-medium text-black transition-transform duration-500"
            style={{
              transform: menuOpen ? 'scale(1)' : 'scale(0.9)',
              opacity: menuOpen ? 1 : 0,
              transitionDelay: menuOpen ? '300ms' : '0ms',
            }}
          >
            {ctaLabel}
          </a>
        </div>

        {/* Hero content */}
        <div className="flex flex-1 flex-col items-center justify-center px-6 text-center">
          <div
            className="liquid-glass mb-6 rounded-full px-5 py-2 text-xs sm:text-sm"
            style={{ fontFamily: 'system-ui, sans-serif', color: contentColor, transition: 'color 700ms' }}
          >
            {badgeText}
          </div>

          <h1
            className="mb-6 max-w-4xl text-4xl leading-[1.1] sm:text-5xl md:text-7xl lg:text-[5.5rem]"
            style={{ fontFamily: "'Instrument Serif', serif", color: contentColor, transition: 'color 700ms' }}
          >
            {headingLines.map((line, index) => (
              <span key={line}>
                {line}
                {index < headingLines.length - 1 && <br />}
              </span>
            ))}
          </h1>

          <p
            className="mb-8 max-w-xl leading-relaxed text-sm sm:text-base"
            style={{
              fontFamily: 'system-ui, sans-serif',
              color: isDark ? darkColor : 'rgba(255,255,255,0.85)',
              transition: 'color 700ms',
            }}
          >
            {subtext}
          </p>

          <form
            className="liquid-glass flex w-full max-w-[320px] items-center rounded-full p-1 sm:max-w-sm"
            style={{ transition: 'color 700ms' }}
            onSubmit={(e) => e.preventDefault()}
          >
            <input
              type="email"
              placeholder={emailPlaceholder}
              className="w-full bg-transparent px-4 py-2 text-sm placeholder:text-white/50 focus:outline-none"
              style={{ fontFamily: 'system-ui, sans-serif', color: contentColor }}
            />
            <button
              type="submit"
              className="whitespace-nowrap rounded-full bg-white px-4 py-2 text-sm font-medium text-black transition-colors duration-200 hover:bg-gray-100"
              style={{ fontFamily: 'system-ui, sans-serif' }}
            >
              {emailButtonLabel}
            </button>
          </form>

          {/* Video switcher */}
          <div className="mt-8 flex flex-wrap items-center justify-center gap-6">
            {videos.map((video, index) => {
              const active = index === activeVideo;
              return (
                <button
                  key={video.url}
                  type="button"
                  onClick={() => selectVideo(index)}
                  className="border-b-2 pb-1 text-xs uppercase tracking-[0.14em] transition-opacity duration-300 sm:text-sm"
                  style={{
                    fontFamily: 'system-ui, sans-serif',
                    color: contentColor,
                    opacity: active ? 1 : 0.5,
                    borderColor: active ? contentColor : 'transparent',
                    transition: 'color 700ms, opacity 300ms, border-color 300ms',
                  }}
                  onMouseEnter={(e) => {
                    if (!active) e.currentTarget.style.opacity = '0.8';
                  }}
                  onMouseLeave={(e) => {
                    if (!active) e.currentTarget.style.opacity = '0.5';
                  }}
                >
                  {video.label}
                </button>
              );
            })}
          </div>
        </div>

        {/* Bottom stats */}
        <div className="px-6 pb-6 md:px-12 lg:px-16">
          <div
            className="flex flex-wrap items-center justify-center gap-x-3 gap-y-2 text-center text-xs text-white/70 sm:text-sm"
            style={{ fontFamily: 'system-ui, sans-serif' }}
          >
            {stats.map((stat, index) => (
              <span key={stat} className="flex items-center gap-3">
                {index > 0 && <span className="hidden text-white/30 sm:inline">|</span>}
                {stat}
              </span>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}

export default SectorHero;
