import { Link } from 'react-router-dom';

const navLinks = [
  { label: 'Who I Am', to: '/who-i-am' },
  { label: 'Services', to: '/services' },
  { label: 'Proof', to: '/proof' },
  { label: 'Ventures', to: '/ventures' },
  { label: 'Sectors', to: '/sectors' },
  { label: 'Contact', to: '/contact' },
];

type NavProps = {
  dark?: boolean;
};

function Nav({ dark = true }: NavProps) {
  const textColor = dark ? 'text-white' : 'text-black';
  const hoverColor = dark ? 'hover:text-gray-300' : 'hover:text-gray-600';

  return (
    <div className="px-6 pt-6 md:px-12 lg:px-16">
      <nav className="liquid-glass flex items-center justify-between rounded-xl px-4 py-2">
        <Link to="/" className={`text-2xl font-semibold tracking-tight ${textColor}`}>
          VEX
        </Link>

        <div className="hidden items-center gap-8 md:flex">
          {navLinks.map((link) => (
            <Link
              className={`text-sm transition-colors duration-200 ${textColor} ${hoverColor}`}
              to={link.to}
              key={link.to}
            >
              {link.label}
            </Link>
          ))}
        </div>

        <Link
          to="/contact"
          className="rounded-lg bg-white px-6 py-2 text-sm font-medium text-black transition-colors duration-200 hover:bg-gray-100"
        >
          Start a Chat
        </Link>
      </nav>
    </div>
  );
}

export default Nav;
