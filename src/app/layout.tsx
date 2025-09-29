import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: "Speedy Scholars - Abacus Classes for Kids",
  description: "Transform your child's mathematical abilities with engaging abacus classes. Expert instruction by Mrs. Nidhi. Book your free demo class today!",
  keywords: "abacus classes, mental math, kids education, online learning, arithmetic skills",
  authors: [{ name: "Speedy Scholars" }],
  openGraph: {
    title: "Speedy Scholars - Abacus Classes for Kids",
    description: "Transform your child's mathematical abilities with engaging abacus classes.",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        {/* Add Calendly script here when you have your URL */}
        {/* <script src="https://assets.calendly.com/assets/external/widget.js" async></script> */}
      </head>
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}