import { Menu, X } from 'lucide-react'

const NAV_LINKS = ['Home', 'Projects', 'Studio', 'Reach Us']

interface NavbarProps {
  mobileMenuOpen: boolean
  setMobileMenuOpen: (open: boolean) => void
}

export default function Navbar({ mobileMenuOpen, setMobileMenuOpen }: NavbarProps) {
  return (
    <nav className="relative z-30 flex items-center justify-between px-6 py-5 md:px-12 lg:px-16">
      <div className="flex items-center gap-x-10">
        <span className="text-lg font-semibold tracking-tight text-white sm:text-xl">
          Foldcraft
        </span>

        <div className="hidden md:flex md:items-center md:gap-x-8">
          {NAV_LINKS.map((link) => (
            <a
              key={link}
              href="#"
              className="text-sm text-white/80 transition-colors hover:text-white"
            >
              {link}
            </a>
          ))}
        </div>
      </div>

      <button
        type="button"
        className="hidden rounded-lg bg-white px-5 py-2 text-sm font-medium text-black transition-transform hover:scale-105 md:inline-block"
      >
        Let&apos;s Talk
      </button>

      <button
        type="button"
        aria-label="Toggle menu"
        onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
        className="relative z-50 flex h-10 w-10 items-center justify-center active:scale-90 md:hidden"
      >
        <Menu
          size={24}
          className={`absolute text-white transition-all duration-300 ${
            mobileMenuOpen ? 'rotate-90 scale-0 opacity-0' : 'rotate-0 scale-100 opacity-100'
          }`}
        />
        <X
          size={24}
          className={`absolute text-white transition-all duration-300 ${
            mobileMenuOpen ? 'rotate-0 scale-100 opacity-100' : '-rotate-90 scale-0 opacity-0'
          }`}
        />
      </button>
    </nav>
  )
}
