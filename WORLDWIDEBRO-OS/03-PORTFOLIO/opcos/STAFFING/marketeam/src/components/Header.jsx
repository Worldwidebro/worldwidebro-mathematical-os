const NAV_LINKS = ['Your Team', 'Solutions', 'Blog', 'Pricing']

export function Header() {
  return (
    <header className="site-header">
      <div className="header-left">
        <img
          className="logo"
          src="https://polo-pecan-73837341.figma.site/_assets/v11/17ae538989a509947a8de3892c644664895e69b1.png"
          alt="Marketeam"
          height={32}
        />
        <nav className="nav-links">
          {NAV_LINKS.map((label) => (
            <a key={label} href="#" className="nav-link">
              {label}
            </a>
          ))}
        </nav>
      </div>

      <div className="header-right">
        <a href="#" className="login-link">
          Log In
        </a>
        <div className="btn-border-wrap">
          <button type="button" className="btn-pill btn-join">
            Join Now
          </button>
        </div>
      </div>
    </header>
  )
}
