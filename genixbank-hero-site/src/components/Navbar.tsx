import { Link } from 'react-router-dom';
import LogoIcon from './LogoIcon';

const NAV_LINKS = [
  { label: 'Network', to: '/' },
  { label: 'Ecosystem', to: '/' },
  { label: 'Banking', to: '/verticals/banking' },
  { label: 'Help', to: '/' },
  { label: 'News', to: '/' },
];

export default function Navbar() {
  return (
    <nav className="absolute top-0 left-0 right-0 z-20 px-6 py-5">
      <div className="max-w-[88rem] mx-auto flex items-center justify-between">
        <Link to="/" className="flex items-center gap-2">
          <LogoIcon className="w-7 h-7 text-black" />
          <span className="text-2xl font-medium tracking-tight text-black">GenixBank</span>
        </Link>

        <div className="hidden md:flex items-center gap-8">
          {NAV_LINKS.map((link) => (
            <Link
              key={link.label}
              to={link.to}
              className="text-base text-gray-700 hover:text-black font-medium transition-colors duration-200"
            >
              {link.label}
            </Link>
          ))}
        </div>

        <a
          href="#"
          className="bg-black text-white text-base font-medium px-7 py-2.5 rounded-full hover:bg-gray-800 transition-colors duration-200"
        >
          Open Account
        </a>
      </div>
    </nav>
  );
}
