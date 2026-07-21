const NAV_LINKS = ['Home', 'Projects', 'Studio', 'Reach Us']

interface MobileMenuProps {
  mobileMenuOpen: boolean
  setMobileMenuOpen: (open: boolean) => void
}

export default function MobileMenu({ mobileMenuOpen, setMobileMenuOpen }: MobileMenuProps) {
  const close = () => setMobileMenuOpen(false)

  return (
    <div
      className={`absolute inset-x-0 top-0 z-20 overflow-hidden bg-black/98 backdrop-blur-xl transition-all duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] ${
        mobileMenuOpen ? 'h-screen opacity-100' : 'pointer-events-none h-0 opacity-0'
      }`}
    >
      <div
        className={`flex h-full flex-col justify-center px-8 transition-all delay-100 duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] ${
          mobileMenuOpen ? 'translate-y-0 opacity-100' : 'translate-y-8 opacity-0'
        }`}
      >
        {NAV_LINKS.map((link) => (
          <a
            key={link}
            href="#"
            onClick={close}
            className="py-3 text-3xl font-medium text-white/90 hover:text-white"
          >
            {link}
          </a>
        ))}

        <button
          type="button"
          onClick={close}
          className="mt-6 w-fit rounded-full bg-white px-8 py-3.5 text-base font-medium text-black transition-transform hover:scale-105"
        >
          Let&apos;s Talk
        </button>
      </div>
    </div>
  )
}
