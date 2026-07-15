// App.tsx — 3D Creator Portfolio Landing Page for "Divine"
// Dependencies: react, react-dom, framer-motion, lucide-react, tailwindcss
// Font: Kanit (Google Fonts, 300–900)

import React, { useRef, useState, useEffect, useMemo } from "react";
import { motion, useScroll, useTransform, type MotionValue } from "framer-motion";
import { ArrowUpRight } from "lucide-react";

/* ============================================================
   GLOBAL STYLES (inject once)
   ============================================================ */
const GLOBAL_CSS = `
html, body, #root {
  background: #0C0C0C;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Kanit', sans-serif;
}
*, *::before, *::after { box-sizing: border-box; }
.hero-heading {
  background: linear-gradient(180deg, #646973 0%, #BBCCD7 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
`;

function useInjectGlobal() {
  useEffect(() => {
    const id = "ace-global-styles";
    if (!document.getElementById(id)) {
      const style = document.createElement("style");
      style.id = id;
      style.innerHTML = GLOBAL_CSS;
      document.head.appendChild(style);
    }
    const linkId = "kanit-font";
    if (!document.getElementById(linkId)) {
      const link = document.createElement("link");
      link.id = linkId;
      link.rel = "stylesheet";
      link.href =
        "https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500;600;700;800;900&display=swap";
      document.head.appendChild(link);
    }
    document.title = "Divine -- 3D Creator";
  }, []);
}

/* ============================================================
   REUSABLE COMPONENTS
   ============================================================ */

// FadeIn — scroll-triggered entrance
function FadeIn({
  children,
  delay = 0,
  duration = 0.7,
  x = 0,
  y = 30,
  as: Component = "div",
}: {
  children: React.ReactNode;
  delay?: number;
  duration?: number;
  x?: number;
  y?: number;
  as?: keyof React.JSX.IntrinsicElements;
}) {
  const MotionEl = motion[Component as keyof typeof motion] as any;
  return (
    <MotionEl
      initial={{ opacity: 0, x, y }}
      whileInView={{ opacity: 1, x: 0, y: 0 }}
      viewport={{ once: true, margin: "50px", amount: 0 }}
      transition={{
        delay,
        duration,
        ease: [0.25, 0.1, 0.25, 1] as const,
      }}
    >
      {children}
    </MotionEl>
  );
}

// ContactButton — gradient pill
function ContactButton() {
  return (
    <button
      className="relative inline-flex items-center justify-center rounded-full px-8 py-3 sm:px-10 sm:py-3.5 md:px-12 md:py-4 text-xs sm:text-sm md:text-base text-white font-medium uppercase tracking-widest transition-transform hover:scale-[1.03] active:scale-[0.98]"
      style={{
        background:
          "linear-gradient(123deg, #18011F 7%, #B600A8 37%, #7621B0 72%, #BE4C00 100%)",
        boxShadow:
          "0px 4px 4px rgba(181, 1, 167, 0.25), 4px 4px 12px #7721B1 inset",
        outline: "2px solid white",
        outlineOffset: "-3px",
      }}
    >
      Contact Me
    </button>
  );
}

// LiveProjectButton — ghost outline pill
function LiveProjectButton() {
  return (
    <button className="inline-flex items-center justify-center gap-2 rounded-full border-2 border-[#D7E2EA] px-8 py-3 sm:px-10 sm:py-3.5 text-sm sm:text-base font-medium uppercase tracking-widest text-[#D7E2EA] transition-colors hover:bg-[#D7E2EA]/10">
      Live Project <ArrowUpRight size={18} />
    </button>
  );
}

// Magnet — mouse-following magnetic hover
function Magnet({
  children,
  padding = 150,
  strength = 3,
  activeTransition = "transform 0.3s ease-out",
  inactiveTransition = "transform 0.6s ease-in-out",
}: {
  children: React.ReactNode;
  padding?: number;
  strength?: number;
  activeTransition?: string;
  inactiveTransition?: string;
}) {
  const ref = useRef<HTMLDivElement>(null);
  const [transition, setTransition] = useState(inactiveTransition);

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    const el = ref.current;
    if (!el) return;
    const rect = el.getBoundingClientRect();
    const cx = rect.left + rect.width / 2;
    const cy = rect.top + rect.height / 2;
    const dx = e.clientX - cx;
    const dy = e.clientY - cy;
    const dist = Math.sqrt(dx * dx + dy * dy);
    if (dist < padding) {
      setTransition(activeTransition);
      el.style.transform = `translate3d(${dx / strength}px, ${dy / strength}px, 0)`;
    }
  };

  const handleMouseLeave = () => {
    const el = ref.current;
    if (!el) return;
    setTransition(inactiveTransition);
    el.style.transform = `translate3d(0,0,0)`;
  };

  return (
    <div
      ref={ref}
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
      style={{ willChange: "transform", transition, display: "inline-block" }}
    >
      {children}
    </div>
  );
}

// AnimatedText — character-by-character scroll reveal
function AnimatedText({
  text,
  className = "",
}: {
  text: string;
  className?: string;
}) {
  const containerRef = useRef<HTMLParagraphElement>(null);
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ["start 0.8", "end 0.2"],
  });

  const chars = useMemo(() => text.split(""), [text]);
  const total = chars.length;

  return (
    <p ref={containerRef} className={className} style={{ fontSize: "clamp(1rem, 2vw, 1.35rem)" }}>
      {chars.map((ch, i) => {
        const start = i / total;
        const end = Math.min(1, (i + 1) / total + 0.02);
        return (
          <Character
            key={i}
            ch={ch}
            progress={scrollYProgress}
            start={start}
            end={end}
          />
        );
      })}
    </p>
  );
}

function Character({
  ch,
  progress,
  start,
  end,
}: {
  ch: string;
  progress: MotionValue<number>;
  start: number;
  end: number;
}) {
  const opacity = useTransform(
    progress,
    [start, end],
    ch === " " ? [1, 1] : [0.2, 1]
  );
  return (
    <span style={{ position: "relative", display: "inline-block" }}>
      <span style={{ visibility: "hidden" }}>{ch}</span>
      <motion.span
        style={{
          position: "absolute",
          inset: 0,
          opacity,
        }}
      >
        {ch}
      </motion.span>
    </span>
  );
}

/* ============================================================
   HERO SECTION
   ============================================================ */
function HeroSection() {
  const navLinks = ["About", "Price", "Projects", "Contact"];
  const portraitUrl =
    "https://shrug-person-78902957.figma.site/_components/v2/d24c01ad3a56fc65e942a1f501eb73db42d7cf9a/Rectangle_40443.81459862.png";

  return (
    <section
      className="relative h-screen flex flex-col overflow-x-clip"
      style={{ background: "#0C0C0C" }}
    >
      {/* Navbar */}
      <FadeIn delay={0} y={-20}>
        <nav className="flex justify-between items-center px-6 md:px-10 pt-6 md:pt-8">
          {navLinks.map((l) => (
            <a
              key={l}
              href={`#${l.toLowerCase()}`}
              className="text-[#D7E2EA] font-medium uppercase tracking-wider text-sm md:text-lg lg:text-[1.4rem] transition-opacity duration-200 hover:opacity-70"
            >
              {l}
            </a>
          ))}
        </nav>
      </FadeIn>

      {/* Portrait (absolutely centered, behind text) */}
      <FadeIn delay={0.6} y={30}>
        <div className="absolute left-1/2 -translate-x-1/2 top-1/2 -translate-y-1/2 sm:top-auto sm:translate-y-0 sm:bottom-0 z-10 pointer-events-none">
          <Magnet padding={150} strength={3}>
            <img
              src={portraitUrl}
              alt="Divine portrait"
              className="w-[280px] sm:w-[360px] md:w-[440px] lg:w-[520px] object-cover pointer-events-auto"
              draggable={false}
            />
          </Magnet>
        </div>
      </FadeIn>

      {/* Hero Heading */}
      <div className="relative z-20 overflow-hidden">
        <FadeIn delay={0.15} y={40}>
          <h1
            className="hero-heading font-black uppercase tracking-tight leading-none whitespace-nowrap w-full text-center text-[14vw] sm:text-[15vw] md:text-[16vw] lg:text-[17.5vw] mt-6 sm:mt-4 md:-mt-5"
          >
            Hi, i&apos;m divine
          </h1>
        </FadeIn>
      </div>

      {/* Bottom bar */}
      <div className="mt-auto relative z-20 flex justify-between items-end pb-7 sm:pb-8 md:pb-10 px-6 md:px-10">
        <FadeIn delay={0.35} y={20}>
          <p
            className="text-[#D7E2EA] font-light uppercase tracking-wide leading-snug max-w-[160px] sm:max-w-[220px] md:max-w-[260px]"
            style={{ fontSize: "clamp(0.75rem, 1.4vw, 1.5rem)" }}
          >
            a 3d creator driven by crafting striking and unforgettable projects
          </p>
        </FadeIn>
        <FadeIn delay={0.5} y={20}>
          <ContactButton />
        </FadeIn>
      </div>
    </section>
  );
}

/* ============================================================
   MARQUEE SECTION
   ============================================================ */
const MARQUEE_IMAGES = [
  "https://motionsites.ai/assets/hero-space-voyage-preview-eECLH3Yc.gif",
  "https://motionsites.ai/assets/hero-codenest-preview-Cgppc2qV.gif",
  "https://motionsites.ai/assets/hero-vex-ventures-preview-BczMFIiw.gif",
  "https://motionsites.ai/assets/hero-stellar-ai-v2-preview-DjvxjG3C.gif",
  "https://motionsites.ai/assets/hero-asme-preview-B_nGDnTP.gif",
  "https://motionsites.ai/assets/hero-transform-data-preview-Cx5OU29N.gif",
  "https://motionsites.ai/assets/hero-vitara-preview-Cjz2QYyU.gif",
  "https://motionsites.ai/assets/hero-terra-preview-BFjrCr7T.gif",
  "https://motionsites.ai/assets/hero-skyelite-preview-DHaZIgUv.gif",
  "https://motionsites.ai/assets/hero-aethera-preview-DknSlcTa.gif",
  "https://motionsites.ai/assets/hero-designpro-preview-D8c5_een.gif",
  "https://motionsites.ai/assets/hero-stellar-ai-preview-D3HL6bw1.gif",
  "https://motionsites.ai/assets/hero-xportfolio-preview-D4A8maiC.gif",
  "https://motionsites.ai/assets/hero-orbit-web3-preview-BXt4OttD.gif",
  "https://motionsites.ai/assets/hero-nexora-preview-cx5HmUgo.gif",
  "https://motionsites.ai/assets/hero-evr-ventures-preview-DZxeVFEX.gif",
  "https://motionsites.ai/assets/hero-planet-orbit-preview-DWAP8Z1P.gif",
  "https://motionsites.ai/assets/hero-new-era-preview-CocuDUm9.gif",
  "https://motionsites.ai/assets/hero-wealth-preview-B70idl_u.gif",
  "https://motionsites.ai/assets/hero-luminex-preview-CxOP7ce6.gif",
  "https://motionsites.ai/assets/hero-celestia-preview-0yO3jXO8.gif",
];

function MarqueeSection() {
  const row1 = MARQUEE_IMAGES.slice(0, 11);
  const row2 = MARQUEE_IMAGES.slice(11);
  const sectionRef = useRef<HTMLDivElement>(null);
  const [offset, setOffset] = useState(0);

  useEffect(() => {
    const onScroll = () => {
      const el = sectionRef.current;
      if (!el) return;
      const rect = el.getBoundingClientRect();
      const sectionTop = rect.top + window.scrollY;
      const o = (window.scrollY - sectionTop + window.innerHeight) * 0.3;
      setOffset(o);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  const row1X = offset - 200;
  const row2X = -(offset - 200);

  return (
    <section
      ref={sectionRef}
      className="pt-24 sm:pt-32 md:pt-40 pb-10 overflow-hidden"
      style={{ background: "#0C0C0C" }}
    >
      <div className="flex flex-col gap-3">
        <div
          className="flex gap-3"
          style={{
            transform: `translateX(${row1X}px)`,
            willChange: "transform",
          }}
        >
          {[...row1, ...row1, ...row1].map((src, i) => (
            <img
              key={`r1-${i}`}
              src={src}
              alt=""
              loading="lazy"
              className="shrink-0 w-[420px] h-[270px] rounded-2xl object-cover"
            />
          ))}
        </div>
        <div
          className="flex gap-3"
          style={{
            transform: `translateX(${row2X}px)`,
            willChange: "transform",
          }}
        >
          {[...row2, ...row2, ...row2].map((src, i) => (
            <img
              key={`r2-${i}`}
              src={src}
              alt=""
              loading="lazy"
              className="shrink-0 w-[420px] h-[270px] rounded-2xl object-cover"
            />
          ))}
        </div>
      </div>
    </section>
  );
}

/* ============================================================
   ABOUT SECTION
   ============================================================ */
function AboutSection() {
  const ABOUT_TEXT =
    "With more than five years of experience in design, i focus on branding, web design, and user experience, i truly enjoy working with businesses that aim to stand out and present their best image. Let's build something incredible together!";

  const decor = [
    {
      src: "https://shrug-person-78902957.figma.site/_components/v2/ebb2b8f25d8e24d5f0a5ca8af4c950de81aa2fd7/moon_icon.11395d36.png",
      pos: "top-[4%] left-[1%] sm:left-[2%] md:left-[4%]",
      w: "w-[120px] sm:w-[160px] md:w-[210px]",
      delay: 0.1,
      x: -80,
    },
    {
      src: "https://shrug-person-78902957.figma.site/_components/v2/ebb2b8f25d8e24d5f0a5ca8af4c950de81aa2fd7/p59_1.4659672e.png",
      pos: "bottom-[8%] left-[3%] sm:left-[6%] md:left-[10%]",
      w: "w-[100px] sm:w-[140px] md:w-[180px]",
      delay: 0.25,
      x: -80,
    },
    {
      src: "https://shrug-person-78902957.figma.site/_components/v2/ebb2b8f25d8e24d5f0a5ca8af4c950de81aa2fd7/lego_icon-1.703bb594.png",
      pos: "top-[4%] right-[1%] sm:right-[2%] md:right-[4%]",
      w: "w-[120px] sm:w-[160px] md:w-[210px]",
      delay: 0.15,
      x: 80,
    },
    {
      src: "https://shrug-person-78902957.figma.site/_components/v2/ebb2b8f25d8e24d5f0a5ca8af4c950de81aa2fd7/Group_134-1.2e04f3ce.png",
      pos: "bottom-[8%] right-[3%] sm:right-[6%] md:right-[10%]",
      w: "w-[130px] sm:w-[170px] md:w-[220px]",
      delay: 0.3,
      x: 80,
    },
  ];

  return (
    <section
      id="about"
      className="relative min-h-screen flex items-center justify-center px-5 sm:px-8 md:px-10 py-20"
      style={{ background: "#0C0C0C" }}
    >
      {/* Decorative images */}
      {decor.map((d, i) => (
        <FadeIn key={i} delay={d.delay} duration={0.9} x={d.x} y={0} as="div">
          <img
            src={d.src}
            alt=""
            className={`absolute ${d.pos} ${d.w} object-contain pointer-events-none`}
          />
        </FadeIn>
      ))}

      <div className="relative z-10 flex flex-col items-center gap-10 sm:gap-14 md:gap-16">
        <FadeIn delay={0} y={40}>
          <h2
            className="hero-heading font-black uppercase leading-none tracking-tight text-center"
            style={{ fontSize: "clamp(3rem, 12vw, 160px)" }}
          >
            About me
          </h2>
        </FadeIn>

        <AnimatedText
          text={ABOUT_TEXT}
          className="text-[#D7E2EA] font-medium text-center leading-relaxed max-w-[560px]"
        />

        <div className="mt-16 sm:mt-20 md:mt-24">
          <ContactButton />
        </div>
      </div>
    </section>
  );
}

/* ============================================================
   SERVICES SECTION
   ============================================================ */
const SERVICES = [
  {
    num: "01",
    name: "3D Modeling",
    desc: "Creation of detailed objects, characters, or environments tailored to specific client needs, ideal for games, products, and visualizations.",
  },
  {
    num: "02",
    name: "Rendering",
    desc: "High-quality, photorealistic renders that showcase designs with custom lighting, textures, and materials to bring concepts to life.",
  },
  {
    num: "03",
    name: "Motion Design",
    desc: "Dynamic animations and motion graphics that add energy and storytelling to brands, products, and digital experiences.",
  },
  {
    num: "04",
    name: "Branding",
    desc: "Crafting cohesive visual identities -- from logos to full brand systems -- that communicate a clear and memorable presence.",
  },
  {
    num: "05",
    name: "Web Design",
    desc: "Designing clean, modern, and conversion-focused websites with attention to layout, typography, and user experience.",
  },
];

function ServicesSection() {
  return (
    <section
      id="price"
      className="relative bg-white px-5 sm:px-8 md:px-10 py-20 sm:py-24 md:py-32 rounded-t-[40px] sm:rounded-t-[50px] md:rounded-t-[60px]"
    >
      <FadeIn delay={0} y={40}>
        <h2
          className="font-black uppercase text-center mb-16 sm:mb-20 md:mb-28"
          style={{
            color: "#0C0C0C",
            fontSize: "clamp(3rem, 12vw, 160px)",
            lineHeight: 1,
            letterSpacing: "-0.02em",
          }}
        >
          Services
        </h2>
      </FadeIn>

      <div className="max-w-5xl mx-auto">
        {SERVICES.map((s, i) => (
          <FadeIn key={s.num} delay={i * 0.1} y={30}>
            <div
              className="flex flex-col sm:flex-row sm:items-start gap-4 sm:gap-8 md:gap-12 py-8 sm:py-10 md:py-12 border-t"
              style={{ borderColor: "rgba(12, 12, 12, 0.15)" }}
            >
              <div
                className="font-black"
                style={{
                  color: "#0C0C0C",
                  fontSize: "clamp(3rem, 10vw, 140px)",
                  lineHeight: 1,
                }}
              >
                {s.num}
              </div>
              <div className="flex flex-col gap-2 sm:gap-3">
                <h3
                  className="font-medium uppercase"
                  style={{ fontSize: "clamp(1rem, 2.2vw, 2.1rem)" }}
                >
                  {s.name}
                </h3>
                <p
                  className="font-light leading-relaxed max-w-2xl"
                  style={{
                    fontSize: "clamp(0.85rem, 1.6vw, 1.25rem)",
                    opacity: 0.6,
                    color: "#0C0C0C",
                  }}
                >
                  {s.desc}
                </p>
              </div>
            </div>
          </FadeIn>
        ))}
      </div>
    </section>
  );
}

/* ============================================================
   PROJECTS SECTION
   ============================================================ */
const PROJECTS = [
  {
    num: "01",
    category: "Client",
    name: "Nextlevel Studio",
    col1: [
      "https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260412_055344_5eff02e0-87a5-41ce-b64f-eb08da8f33db.png&w=1280&q=85",
      "https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260412_055431_11d841fd-8b41-46a5-82e4-b04f2407a7d8.png&w=1280&q=85",
    ],
    col2:
      "https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260412_055451_e317bf2d-28d4-48cc-86b0-6f72f25b6327.png&w=1280&q=85",
  },
  {
    num: "02",
    category: "Personal",
    name: "Aura Brand Identity",
    col1: [
      "https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260412_055654_911201c5-36d9-4bc6-bac7-331adfce159f.png&w=1280&q=85",
      "https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260412_055723_5ceda0b8-d9c2-4665-b2e3-83ba19ba76d1.png&w=1280&q=85",
    ],
    col2:
      "https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260412_055753_adc5dcbd-a8e6-49c0-b43a-9b030d835cea.png&w=1280&q=85",
  },
  {
    num: "03",
    category: "Client",
    name: "Solaris Digital",
    col1: [
      "https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260412_055759_963cfb0b-4bd1-4b0f-9d0a-09bd6cf95b2f.png&w=1280&q=85",
      "https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260412_060108_438f781a-9846-4dcc-89ab-c4e6cb830f5b.png&w=1280&q=85",
    ],
    col2:
      "https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260412_055818_9d062121-ad7e-46b9-999a-1a6a692ef1ee.png&w=1280&q=85",
  },
];

function ProjectCard({
  project,
  index,
  total,
}: {
  project: (typeof PROJECTS)[number];
  index: number;
  total: number;
}) {
  const ref = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start start", "end start"],
  });
  const scale = useTransform(
    scrollYProgress,
    [0, 1],
    [1, 1 - (total - 1 - index) * 0.03]
  );

  return (
    <div
      ref={ref}
      className="sticky top-24 md:top-32 h-[85vh] flex items-start justify-center"
      style={{ zIndex: total - index }}
    >
      <motion.div
        style={{
          scale,
          top: `${index * 28}px`,
        }}
        className="relative w-full max-w-6xl rounded-[40px] sm:rounded-[50px] md:rounded-[60px] border-2 border-[#D7E2EA] p-4 sm:p-6 md:p-8"
      >
        <div
          className="w-full h-full rounded-[36px] sm:rounded-[46px] md:rounded-[56px] p-4 sm:p-6 md:p-8 flex flex-col"
          style={{ background: "#0C0C0C" }}
        >
          {/* Top row */}
          <div className="flex flex-wrap items-end justify-between gap-4 mb-6">
            <div className="flex items-end gap-4 sm:gap-6">
              <div
                className="hero-heading font-black leading-none"
                style={{ fontSize: "clamp(3rem, 10vw, 140px)" }}
              >
                {project.num}
              </div>
              <div className="flex flex-col">
                <span className="text-[#D7E2EA]/60 uppercase tracking-widest text-xs sm:text-sm font-medium">
                  {project.category}
                </span>
                <h3
                  className="text-[#D7E2EA] font-medium uppercase leading-tight"
                  style={{ fontSize: "clamp(1.2rem, 3vw, 2.5rem)" }}
                >
                  {project.name}
                </h3>
              </div>
            </div>
            <LiveProjectButton />
          </div>

          {/* Bottom row — image grid */}
          <div className="flex gap-3 flex-1 min-h-0">
            {/* Left column 40% */}
            <div className="w-[40%] flex flex-col gap-3">
              <img
                src={project.col1[0]}
                alt=""
                className="w-full object-cover rounded-[40px] sm:rounded-[50px] md:rounded-[60px]"
                style={{ height: "clamp(130px, 16vw, 230px)" }}
              />
              <img
                src={project.col1[1]}
                alt=""
                className="w-full object-cover rounded-[40px] sm:rounded-[50px] md:rounded-[60px] flex-1"
                style={{ height: "clamp(160px, 22vw, 340px)" }}
              />
            </div>
            {/* Right column 60% */}
            <div className="w-[60%]">
              <img
                src={project.col2}
                alt=""
                className="w-full h-full object-cover rounded-[40px] sm:rounded-[50px] md:rounded-[60px]"
              />
            </div>
          </div>
        </div>
      </motion.div>
    </div>
  );
}

function ProjectsSection() {
  return (
    <section
      id="projects"
      className="relative rounded-t-[40px] sm:rounded-t-[50px] md:rounded-t-[60px] -mt-10 sm:-mt-12 md:-mt-14 z-10"
      style={{ background: "#0C0C0C" }}
    >
      <div className="px-5 sm:px-8 md:px-10 pt-20 sm:pt-24 md:pt-32">
        <FadeIn delay={0} y={40}>
          <h2
            className="hero-heading font-black uppercase leading-none tracking-tight text-center mb-16 sm:mb-20 md:mb-24"
            style={{ fontSize: "clamp(3rem, 12vw, 160px)" }}
          >
            Project
          </h2>
        </FadeIn>
      </div>

      <div className="px-5 sm:px-8 md:px-10 pb-32">
        {PROJECTS.map((p, i) => (
          <ProjectCard key={p.num} project={p} index={i} total={PROJECTS.length} />
        ))}
      </div>
    </section>
  );
}

/* ============================================================
   MAIN APP
   ============================================================ */
export default function App() {
  useInjectGlobal();
  return (
    <div style={{ overflowX: "clip", background: "#0C0C0C" }}>
      <HeroSection />
      <MarqueeSection />
      <AboutSection />
      <ServicesSection />
      <ProjectsSection />
    </div>
  );
}
