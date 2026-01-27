import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import { Providers } from "@/components/Providers";
import { HomePageStructuredData } from "@/components/StructuredData";
import { GoogleAnalytics } from "@/components/GoogleAnalytics";

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

// Base URL for the site - update when domain is connected
const siteUrl = process.env.NEXT_PUBLIC_SITE_URL || "https://speedyscholars.com";

export const metadata: Metadata = {
  // Basic Meta Tags
  title: {
    default: "Speedy Scholars | Online Abacus Classes for Kids | Free Demo",
    template: "%s | Speedy Scholars",
  },
  description:
    "Transform your child's math skills with expert online abacus classes. 20+ years experience, 2000+ students worldwide. Learn mental math from home. Book your FREE demo class today!",
  keywords: [
    "abacus classes",
    "online abacus classes",
    "abacus for kids",
    "mental math",
    "abacus tutor",
    "learn abacus online",
    "mental arithmetic",
    "math classes for kids",
    "abacus training",
    "online math tutor",
    "abacus classes USA",
    "abacus classes UK",
    "abacus classes Australia",
    "vedic math",
    "brain development for kids",
    "concentration improvement",
    "math anxiety help",
  ],
  authors: [{ name: "Nidhi Khariwal", url: siteUrl }],
  creator: "Speedy Scholars",
  publisher: "Speedy Scholars",

  // Robots
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },

  // Icons
  icons: {
    icon: "/images/logo.png",
    shortcut: "/images/logo.png",
    apple: "/images/logo.png",
  },

  // Manifest
  manifest: "/manifest.json",

  // Open Graph (Facebook, WhatsApp, LinkedIn)
  openGraph: {
    type: "website",
    locale: "en_US",
    url: siteUrl,
    siteName: "Speedy Scholars",
    title: "Speedy Scholars | Online Abacus Classes for Kids",
    description:
      "Transform your child's math skills with expert online abacus classes. 20+ years experience, 2000+ students worldwide. Book your FREE demo class!",
    images: [
      {
        url: `${siteUrl}/images/og-image.jpg`,
        width: 1200,
        height: 630,
        alt: "Speedy Scholars - Online Abacus Classes for Kids",
        type: "image/jpeg",
      },
    ],
  },

  // Twitter Card
  twitter: {
    card: "summary_large_image",
    title: "Speedy Scholars | Online Abacus Classes for Kids",
    description:
      "Transform your child's math skills with expert online abacus classes. 20+ years experience. Book your FREE demo!",
    images: [`${siteUrl}/images/og-image.jpg`],
    creator: "@speedyscholars",
  },

  // Verification
  verification: {
    google: "1ztnwGqkDWvfmm313OU7Tp_8GzfSLztFzczorr5pMeE",
  },

  // Alternate languages (if you add multi-language support later)
  alternates: {
    canonical: siteUrl,
    languages: {
      "en-US": siteUrl,
      "en-GB": siteUrl,
      "en-AU": siteUrl,
    },
  },

  // Category
  category: "education",

  // Other
  other: {
    "mobile-web-app-capable": "yes",
    "apple-mobile-web-app-capable": "yes",
    "apple-mobile-web-app-status-bar-style": "default",
    "apple-mobile-web-app-title": "Speedy Scholars",
    "format-detection": "telephone=yes",
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
        {/* Structured Data for SEO */}
        <HomePageStructuredData />

        {/* Preconnect to external domains for better performance */}
        <link rel="preconnect" href="https://calendly.com" />
        <link rel="preconnect" href="https://assets.calendly.com" />
        <link rel="dns-prefetch" href="https://calendly.com" />

        {/* Calendly Widget */}
        <script src="https://assets.calendly.com/assets/external/widget.js" async></script>
      </head>
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {/* Google Analytics - Add your Measurement ID after creating GA4 property */}
        <GoogleAnalytics measurementId={process.env.NEXT_PUBLIC_GA_MEASUREMENT_ID || ""} />
        <Providers>
          {children}
        </Providers>
      </body>
    </html>
  );
}