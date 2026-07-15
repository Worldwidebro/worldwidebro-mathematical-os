import { Link } from 'react-router-dom';
import type { ReactNode } from 'react';

type SectionProps = {
  id?: string;
  children: ReactNode;
  border?: 'none' | 'top' | 'y';
  className?: string;
};

export function Section({ id, children, border = 'none', className = '' }: SectionProps) {
  const borderClass =
    border === 'y' ? 'border-y border-white/10' : border === 'top' ? 'border-t border-white/10' : '';
  return (
    <section id={id} className={`px-6 py-20 md:px-12 lg:px-16 ${borderClass} ${className}`}>
      <div className="mx-auto max-w-7xl">{children}</div>
    </section>
  );
}

export function Eyebrow({ children }: { children: ReactNode }) {
  return <p className="mb-4 text-sm uppercase tracking-[0.18em] text-gray-400">{children}</p>;
}

export function PageHeading({ children, className = '' }: { children: ReactNode; className?: string }) {
  return (
    <h1 className={`mb-6 text-4xl font-normal leading-tight md:text-6xl ${className}`}>{children}</h1>
  );
}

export function Card({ children, className = '' }: { children: ReactNode; className?: string }) {
  return <div className={`border border-white/10 p-5 ${className}`}>{children}</div>;
}

export function Tag({ children }: { children: ReactNode }) {
  return <span className="border border-white/10 px-3 py-1 text-xs text-gray-300">{children}</span>;
}

export function Pill({ children }: { children: ReactNode }) {
  return (
    <span className="whitespace-nowrap rounded-full border border-white/10 px-3 py-1 text-xs text-gray-300">
      {children}
    </span>
  );
}

export function PrimaryLink({ to, children }: { to: string; children: ReactNode }) {
  return (
    <Link
      to={to}
      className="inline-block rounded-lg bg-white px-8 py-3 font-medium text-black transition-colors duration-200 hover:bg-gray-100"
    >
      {children}
    </Link>
  );
}

export function SecondaryLink({ to, children }: { to: string; children: ReactNode }) {
  return (
    <Link
      to={to}
      className="liquid-glass inline-block rounded-lg border border-white/20 px-8 py-3 font-medium text-white transition-colors duration-200 hover:bg-white hover:text-black"
    >
      {children}
    </Link>
  );
}

export function TextLink({ to, children }: { to: string; children: ReactNode }) {
  return (
    <Link to={to} className="text-sm text-gray-300 underline underline-offset-4 hover:text-white">
      {children}
    </Link>
  );
}
