import { Link } from 'react-router-dom';

function Footer() {
  return (
    <footer className="border-t border-white/10 px-6 py-10 md:px-12 lg:px-16">
      <div className="mx-auto flex max-w-7xl flex-col justify-between gap-4 text-xs text-gray-500 md:flex-row md:items-center">
        <p>© {new Date().getFullYear()} VEX. Worldwidebro Holdings.</p>
        <div className="flex gap-6">
          <Link className="hover:text-gray-300" to="/privacy">
            Privacy
          </Link>
          <Link className="hover:text-gray-300" to="/terms">
            Terms
          </Link>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
