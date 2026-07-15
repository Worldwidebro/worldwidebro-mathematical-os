import { useEffect, useMemo, useRef, useState } from 'react';

export interface ArchiveHeroConfig {
  wordmark: string;
  caption: string;
  aboutLabel?: string;
  cartLabel?: string;
  collectionLines: [string, string];
  price: string;
  videos: { left: string; right: string };
  galleryImages: string[];
  ctaWord?: string;
  footerBrand: string;
  footerRight?: string;
  accentHex?: string;
}

const SYMBOLS = ['8', '$', '^^', '%', '/'];

/** Scattered grid layout: primary image per row, extra image every 3rd row. */
function buildLayout(count: number, cols: number): number[][] {
  const rows: number[][] = [];
  let placed = 0;
  let r = 0;
  while (placed < count) {
    const row = new Array(cols).fill(-1);
    const a = (r * 2 + (r % 2)) % cols;
    row[a] = placed++;
    if (r % 3 === 0 && placed < count) {
      let b = (a + 2) % cols;
      if (b === a) b = (a + 1) % cols;
      if (row[b] === -1) row[b] = placed++;
    }
    rows.push(row);
    r++;
  }
  return rows;
}

function useCols() {
  const [cols, setCols] = useState(4);
  useEffect(() => {
    const update = () => {
      const w = window.innerWidth;
      setCols(w < 640 ? 2 : w < 1024 ? 3 : 4);
    };
    update();
    window.addEventListener('resize', update);
    return () => window.removeEventListener('resize', update);
  }, []);
  return cols;
}

export default function ArchiveHero({ config }: { config: ArchiveHeroConfig }) {
  const spacerRef = useRef<HTMLDivElement>(null);
  const panelRef = useRef<HTMLDivElement>(null);
  const wrapRef = useRef<HTMLDivElement>(null);
  const cursorRef = useRef<HTMLDivElement>(null);
  const leftVideoRef = useRef<HTMLVideoElement>(null);
  const rightVideoRef = useRef<HTMLVideoElement>(null);
  const canvasRef = useRef<HTMLDivElement>(null);
  const outroInfoRef = useRef<HTMLDivElement>(null);
  const outroBuyRef = useRef<HTMLDivElement>(null);
  const outroOverlayRef = useRef<HTMLDivElement>(null);
  const outroFooterRef = useRef<HTMLDivElement>(null);
  const circleSymbolRef = useRef<HTMLSpanElement>(null);
  const cardRefs = useRef<Array<HTMLDivElement | null>>([]);
  const overlayGroupRef = useRef<HTMLDivElement>(null);

  const cols = useCols();
  const layout = useMemo(
    () => buildLayout(config.galleryImages.length, cols),
    [config.galleryImages.length, cols],
  );

  const [isTouch] = useState(
    () => typeof window !== 'undefined' && window.matchMedia('(pointer: coarse)').matches,
  );

  useEffect(() => {
    if (isTouch) return;
    const el = cursorRef.current;
    if (!el) return;
    const move = (e: MouseEvent) => {
      el.style.left = `${e.clientX}px`;
      el.style.top = `${e.clientY}px`;
    };
    window.addEventListener('mousemove', move);
    return () => window.removeEventListener('mousemove', move);
  }, [isTouch]);

  useEffect(() => {
    const left = leftVideoRef.current;
    const right = rightVideoRef.current;
    if (!left || !right) return;

    let loaded = 0;
    const onLoaded = () => {
      loaded++;
      if (loaded >= 2 && canvasRef.current) canvasRef.current.style.opacity = '1';
    };
    left.addEventListener('loadeddata', onLoaded);
    right.addEventListener('loadeddata', onLoaded);

    if (isTouch) {
      const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      if (reduced) {
        left.style.display = 'block';
        right.style.display = 'none';
        return () => {
          left.removeEventListener('loadeddata', onLoaded);
          right.removeEventListener('loadeddata', onLoaded);
        };
      }
      const showLeft = () => {
        left.style.display = 'block';
        right.style.display = 'none';
        left.currentTime = 0;
        void left.play();
      };
      const showRight = () => {
        right.style.display = 'block';
        left.style.display = 'none';
        right.currentTime = 0;
        void right.play();
      };
      left.addEventListener('ended', showRight);
      right.addEventListener('ended', showLeft);
      showLeft();
      return () => {
        left.removeEventListener('loadeddata', onLoaded);
        right.removeEventListener('loadeddata', onLoaded);
        left.removeEventListener('ended', showRight);
        right.removeEventListener('ended', showLeft);
      };
    }

    right.style.display = 'block';
    left.style.display = 'none';
    let mouseX = window.innerWidth / 2;
    const onMove = (e: MouseEvent) => {
      mouseX = e.clientX;
    };
    window.addEventListener('mousemove', onMove);

    let activeSide: 'left' | 'right' = 'right';
    let raf = 0;
    const tick = () => {
      const width = window.innerWidth;
      const center = width / 2;
      const deadZone = Math.max(30, width * 0.05);

      if (mouseX < center - deadZone) activeSide = 'right';
      else if (mouseX > center + deadZone) activeSide = 'left';

      const showVideo = activeSide === 'right' ? right : left;
      const hideVideo = activeSide === 'right' ? left : right;
      if (showVideo.style.display !== 'block') {
        showVideo.style.display = 'block';
        hideVideo.style.display = 'none';
      }

      const inDeadZone = mouseX >= center - deadZone && mouseX <= center + deadZone;
      if (inDeadZone) {
        if (!showVideo.seeking) showVideo.currentTime = 0;
      } else if (activeSide === 'right') {
        const range = Math.max(1, center - deadZone);
        const progress = Math.min(1, Math.max(0, (range - mouseX) / range));
        if (showVideo.duration && !showVideo.seeking) showVideo.currentTime = progress * showVideo.duration;
      } else {
        const start = center + deadZone;
        const range = Math.max(1, width - start);
        const progress = Math.min(1, Math.max(0, (mouseX - start) / range));
        if (showVideo.duration && !showVideo.seeking) showVideo.currentTime = progress * showVideo.duration;
      }
      raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);

    return () => {
      left.removeEventListener('loadeddata', onLoaded);
      right.removeEventListener('loadeddata', onLoaded);
      window.removeEventListener('mousemove', onMove);
      cancelAnimationFrame(raf);
    };
  }, [isTouch]);

  useEffect(() => {
    let last = 0;
    const onScroll = () => {
      const now = performance.now();
      if (now - last < 80) return;
      last = now;
      if (circleSymbolRef.current) {
        circleSymbolRef.current.textContent = SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)];
      }
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  useEffect(() => {
    const spacer = spacerRef.current;
    const panel = panelRef.current;
    const wrap = wrapRef.current;
    if (!spacer || !panel || !wrap) return;

    const setSpacerHeight = () => {
      const vh = window.innerHeight;
      const maxScroll = Math.max(0, wrap.scrollHeight - vh);
      spacer.style.height = `${vh + maxScroll + 2 * vh}px`;
    };
    setSpacerHeight();
    window.addEventListener('resize', setSpacerHeight);

    const outroOffsetDesktop = 166;
    const outroOffsetMobile = 132;

    let raf = 0;
    const tick = () => {
      const vh = window.innerHeight;
      const scrollY = window.scrollY;
      const maxScroll = Math.max(0, wrap.scrollHeight - vh);

      let panelY: number;
      let innerY: number;
      if (scrollY <= vh) {
        panelY = vh - scrollY;
        innerY = 0;
      } else {
        panelY = 0;
        innerY = -Math.min(scrollY - vh, maxScroll);
      }
      panel.style.transform = `translateY(${panelY}px)`;
      wrap.style.transform = `translateY(${innerY}px)`;

      if (canvasRef.current) {
        canvasRef.current.style.visibility = scrollY > vh ? 'hidden' : 'visible';
      }

      cardRefs.current.forEach((card) => {
        if (!card) return;
        const rect = card.getBoundingClientRect();
        if (rect.bottom <= 0 || rect.top >= vh) {
          card.style.transform = 'scale(0)';
          return;
        }
        const enter = Math.min(1, (vh - rect.top) / (vh * 0.6));
        const exit = Math.min(1, rect.bottom / (vh * 0.4));
        const scale = Math.max(0, Math.min(enter, exit));
        card.style.transform = `scale(${scale})`;
      });

      const isMobile = window.innerWidth < 640;
      const outroOffset = isMobile ? outroOffsetMobile : outroOffsetDesktop;
      const outroStart = vh + maxScroll;
      const progress = Math.min(1, Math.max(0, (scrollY - outroStart) / (vh - 100)));

      if (outroOverlayRef.current) outroOverlayRef.current.style.opacity = String(progress);
      if (outroInfoRef.current)
        outroInfoRef.current.style.transform = `translateY(${-outroOffset * progress}px)`;
      if (outroBuyRef.current) outroBuyRef.current.style.transform = `scale(${progress})`;
      if (outroFooterRef.current) outroFooterRef.current.style.opacity = String(progress);

      // Release all fixed overlays once scroll clears this hero's spacer, so page
      // content rendered after <ArchiveHero /> isn't permanently covered.
      if (overlayGroupRef.current) {
        const totalSpacerScroll = vh + maxScroll + 2 * vh;
        overlayGroupRef.current.style.display = scrollY >= totalSpacerScroll ? 'none' : '';
      }

      raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);

    return () => {
      window.removeEventListener('resize', setSpacerHeight);
      cancelAnimationFrame(raf);
    };
  }, [layout]);

  const accent = config.accentHex ?? '#ffffff';
  const flatLayout = layout.flat();

  return (
    <div
      ref={spacerRef}
      id="scroll-spacer"
      className={`relative bg-white select-none ${isTouch ? '' : 'cursor-none'}`}
      style={{ height: '500vh' }}
    >
      <div ref={overlayGroupRef}>
      {!isTouch && (
        <div
          ref={cursorRef}
          className="pointer-events-none fixed z-50 hidden -translate-x-1/2 -translate-y-1/2 lg:block"
          style={{ mixBlendMode: 'exclusion', left: 0, top: 0 }}
        >
          <svg width="48" height="48" viewBox="0 0 48 48" fill="none">
            <circle cx="24" cy="24" r="22.75" stroke="white" strokeWidth="2.5" />
            <path d="M17 24 L21.5 28.5 L31 18" stroke="white" strokeWidth="2" fill="none" />
          </svg>
        </div>
      )}

      <div
        className="pointer-events-none fixed z-20 w-[124px] sm:w-[266px] lg:w-[355px]"
        style={{ mixBlendMode: 'exclusion', top: 16, left: 16 }}
      >
        <div className="text-[22px] font-medium uppercase tracking-tight text-white sm:text-[36px] lg:text-[48px]">
          {config.wordmark}
        </div>
      </div>

      <div
        className="pointer-events-none fixed z-20 hidden text-[12px] leading-[140%] tracking-[-0.04em] text-white md:block"
        style={{ mixBlendMode: 'exclusion', left: 32, top: 244, width: 692 }}
      >
        {config.caption}
      </div>

      <div
        className="pointer-events-none fixed z-20 flex w-auto items-center justify-between gap-5 lg:w-[330px]"
        style={{ mixBlendMode: 'exclusion', top: 16, right: 16 }}
      >
        <span className="hidden text-[15px] uppercase tracking-tight text-white lg:inline">
          {config.aboutLabel ?? 'About'}
        </span>
        <div className="flex items-center gap-5 lg:gap-[50px]">
          <svg width="24" height="24" viewBox="0 0 40 40" className="lg:h-[30px] lg:w-[30px]">
            <path d="M0 14H40" stroke="white" strokeWidth="2.5" />
            <path d="M0 26H40" stroke="white" strokeWidth="2.5" />
          </svg>
          <span className="text-[13px] uppercase tracking-tight text-white lg:text-[15px]">
            [ {config.cartLabel ?? 'CART'} ]
          </span>
        </div>
      </div>

      <div
        ref={outroInfoRef}
        id="outro-info"
        className="pointer-events-none fixed bottom-12 left-0 right-0 z-20 flex flex-col items-center lg:bottom-20 lg:left-auto lg:right-8 lg:w-[330px]"
        style={{ mixBlendMode: 'exclusion' }}
      >
        <div className="mb-3 flex w-[252px] flex-col items-start lg:mb-8 lg:w-full">
          <div className="relative mb-2 h-5 w-5 lg:h-[30px] lg:w-[30px]">
            <svg viewBox="0 0 40 40" className="h-full w-full">
              <circle cx="20" cy="20" r="18.75" stroke="white" strokeWidth="2" />
            </svg>
            <span
              ref={circleSymbolRef}
              className="absolute inset-0 flex items-center justify-center text-[10px] uppercase tracking-tight text-white lg:text-[15px]"
            >
              8
            </span>
          </div>
          <div className="text-center text-[20px] uppercase leading-none tracking-tight text-white lg:text-[30px]">
            {config.collectionLines[0]}
            <br />
            {config.collectionLines[1]}
          </div>
        </div>
        <div
          className="text-center text-[60px] leading-none tracking-tight lg:text-[80px]"
          style={{ color: accent }}
        >
          {config.price}
        </div>
      </div>

      <div
        ref={outroBuyRef}
        id="outro-buy"
        className="pointer-events-none fixed bottom-[60px] left-4 right-4 z-20 flex h-[100px] items-center justify-center rounded-full bg-white lg:bottom-8 lg:left-auto lg:right-8 lg:h-[174px] lg:w-[330px]"
        style={{ mixBlendMode: 'exclusion', transformOrigin: 'right bottom', transform: 'scale(0)' }}
      >
        <span className="text-[72px] tracking-tight text-white lg:text-[110px]" style={{ mixBlendMode: 'exclusion' }}>
          {config.ctaWord ?? 'view'}
        </span>
      </div>

      <div
        ref={canvasRef}
        id="main-canvas"
        className="pointer-events-none fixed inset-0 z-0 overflow-hidden opacity-0 transition-opacity duration-300"
        style={isTouch ? { left: 0, top: 220, width: '100vw', height: 'calc(100vh - 220px)' } : undefined}
      >
        <video
          ref={leftVideoRef}
          muted
          playsInline
          preload="auto"
          className="absolute inset-0 h-full w-full object-cover"
          style={{ display: 'none' }}
          src={config.videos.left}
        />
        <video
          ref={rightVideoRef}
          muted
          playsInline
          preload="auto"
          className="absolute inset-0 h-full w-full object-cover"
          style={{ display: 'block' }}
          src={config.videos.right}
        />
      </div>

      <div ref={outroOverlayRef} id="outro-overlay" className="pointer-events-none fixed inset-0 z-[12] bg-white opacity-0" />

      <div
        ref={outroFooterRef}
        id="outro-footer"
        className="pointer-events-none fixed bottom-6 left-4 z-20 flex gap-20 text-[11px] uppercase tracking-tight text-white opacity-0 lg:bottom-8 lg:text-[13px]"
        style={{ mixBlendMode: 'exclusion' }}
      >
        <span>{config.footerBrand}</span>
        <span>{config.footerRight ?? 'Privacy Policy'}</span>
      </div>

      <div ref={panelRef} className="fixed inset-0 z-10 bg-black" style={{ transform: 'translateY(100vh)' }}>
        <div ref={wrapRef} className="w-full" style={{ paddingTop: 'min(400px, 40vh)' }}>
          <div className="grid gap-3 px-4" style={{ gridTemplateColumns: `repeat(${cols}, 1fr)` }}>
            {flatLayout.map((imgIndex, i) => (
              <div key={i} className="relative" style={{ aspectRatio: '2/3' }}>
                {imgIndex >= 0 && (
                  <div
                    ref={(el) => {
                      cardRefs.current[imgIndex] = el;
                    }}
                    className="bp-card absolute inset-0 overflow-hidden bg-neutral-900"
                    style={{
                      transform: 'scale(0)',
                      transformOrigin: i % cols < cols / 2 ? 'right bottom' : 'left bottom',
                    }}
                  >
                    <img
                      src={config.galleryImages[imgIndex]}
                      alt=""
                      className="h-full w-full object-cover"
                      loading="lazy"
                    />
                  </div>
                )}
              </div>
            ))}
          </div>
          <div style={{ height: '20vh' }} />
        </div>
      </div>
      </div>
    </div>
  );
}
