import type { Metadata } from 'next';
import { Nav } from '@/components/Layout/Nav';
import './globals.css';

export const metadata: Metadata = {
  title: 'Real Estate OS',
  description: 'Rental property management SaaS',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <Nav />
        {children}
      </body>
    </html>
  );
}
