import { NextRequest, NextResponse } from "next/server";

const PUBLIC_ROUTES = ["/", "/login", "/register"];

export function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;
  const token = request.cookies.get("360human-auth")?.value;

  // Parse token từ Zustand persist cookie
  let isAuthenticated = false;
  if (token) {
    try {
      const parsed = JSON.parse(token);
      isAuthenticated = !!parsed?.state?.token;
    } catch {
      isAuthenticated = false;
    }
  }

  const isPublic = PUBLIC_ROUTES.some((r) => pathname === r || pathname.startsWith(r + "/"));

  // Chưa login → redirect về /login
  if (!isAuthenticated && !isPublic) {
    return NextResponse.redirect(new URL("/login", request.url));
  }

  // Đã login → không cho vào /login, /register nữa
  if (isAuthenticated && (pathname === "/login" || pathname === "/register")) {
    return NextResponse.redirect(new URL("/dashboard", request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon.ico|api).*)"],
};
