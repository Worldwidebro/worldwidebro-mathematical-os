import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

/** Lightweight session anchor for future server-side personalization and scoring. */
export function middleware(request: NextRequest) {
  const res = NextResponse.next();
  if (!request.cookies.get('cognitive_sid')) {
    const sid = crypto.randomUUID();
    res.cookies.set('cognitive_sid', sid, { path: '/', sameSite: 'lax' });
  }
  return res;
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)'],
};
