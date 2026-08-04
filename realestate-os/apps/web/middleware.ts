import { type NextRequest, NextResponse } from 'next/server';

export function middleware(request: NextRequest) {
  const token = request.cookies.get('sb-access-token')?.value;
  const role = request.cookies.get('user-role')?.value;
  const { pathname } = request.nextUrl;

  // Public routes that don't require auth
  const publicRoutes = ['/', '/login', '/register'];
  const isPublicRoute = publicRoutes.includes(pathname);

  // Protected routes
  if (!isPublicRoute) {
    if (!token) {
      return NextResponse.redirect(new URL('/login', request.url));
    }

    // Role-based redirects
    if (pathname.startsWith('/landlord') && role !== 'landlord') {
      return NextResponse.redirect(new URL('/tenant', request.url));
    }

    if (pathname.startsWith('/tenant') && role !== 'tenant') {
      return NextResponse.redirect(new URL('/landlord', request.url));
    }

    if (pathname.startsWith('/admin') && role !== 'admin') {
      return NextResponse.redirect(new URL('/', request.url));
    }
  }

  // Redirect authenticated users away from auth pages
  if (isPublicRoute && token && pathname !== '/') {
    const dashboardMap: Record<string, string> = {
      landlord: '/landlord/dashboard',
      tenant: '/tenant/portal',
      admin: '/admin',
    };
    const redirectPath = dashboardMap[role || 'landlord'] || '/';
    return NextResponse.redirect(new URL(redirectPath, request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: [
    '/((?!_next/static|_next/image|favicon.ico|public).*)',
  ],
};
