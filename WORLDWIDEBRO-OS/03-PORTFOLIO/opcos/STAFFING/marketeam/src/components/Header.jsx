const NAV_LINKS = [
  { label: 'Your Team', href: '/workers.html' },
  { label: 'Solutions', href: '/clients.html' },
  { label: 'Pricing', href: '/pricing.html' },
  { label: 'Open Jobs', href: '/jobs.html' },
]

export function Header() {
  return (
    <header className="site-header">
      <div className="header-left">
        <a href="/" className="brand-mark">
          <span className="brand-dot">◆</span> Worldwidebro Staffing
        </a>
        <nav className="nav-links">
          {NAV_LINKS.map(({ label, href }) => (
            <a key={label} href={href} className="nav-link">
              {label}
            </a>
          ))}
        </nav>
      </div>

      <div className="header-right">
        <a href="/login.html" className="login-link">
          Log In
        </a>
        <div className="btn-border-wrap">
          <a href="/workers.html" className="btn-pill btn-join">
            Join Now
          </a>
        </div>
      </div>
    </header>
  )
}
