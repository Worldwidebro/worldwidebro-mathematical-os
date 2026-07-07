const LOGOS = [
  'https://polo-pecan-73837341.figma.site/_assets/v11/1e7b0e6fcc016cd28aec5c68990118b8c54c35a5.svg',
  'https://polo-pecan-73837341.figma.site/_assets/v11/3eac03c183db2ae080d910159211c14843398b61.svg',
  'https://polo-pecan-73837341.figma.site/_assets/v11/17705a4c0023a0e5a99154dfb10582adbbf4260b.svg',
  'https://polo-pecan-73837341.figma.site/_assets/v11/0e5f442b09dc5c248e3e60d40a65505fb1887228.svg',
  'https://polo-pecan-73837341.figma.site/_assets/v11/63f99030ceb459e3c9ab9e429cfa2353491d3816.svg',
]

const REPEATED = Array(4).fill(LOGOS).flat()

export function LogoTicker() {
  return (
    <div className="logo-ticker">
      <div className="logo-ticker-track">
        {REPEATED.map((src, i) => (
          <img key={i} src={src} alt="" width={137} height={40} loading="lazy" />
        ))}
      </div>
    </div>
  )
}
