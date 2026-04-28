import { NextResponse } from "next/server";

// Block the analytics dashboard and its APIs on any deployed environment.
// They only work on local dev (npm run dev). VERCEL is set on every Vercel deploy.
const isDeployed = process.env.VERCEL === "1";

export function middleware() {
  if (isDeployed) {
    return new NextResponse("Not Found", { status: 404 });
  }
  return NextResponse.next();
}

export const config = {
  matcher: [
    "/analytics",
    "/analytics/:path*",
    "/api/analytics-brief/:path*",
    "/api/analytics-chat/:path*",
    "/api/action-items/:path*",
  ],
};
