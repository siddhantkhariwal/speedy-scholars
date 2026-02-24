import { Metadata } from "next";

export const metadata: Metadata = {
  title: "About Speedy Scholars | Nidhi Khariwal - Expert Abacus Educator",
  description:
    "Meet Nidhi Khariwal, founder of Speedy Scholars — 20+ years of abacus teaching experience, 2,000+ students worldwide, and 15+ awards. Discover our story, mission, and teaching philosophy.",
  keywords: [
    "about speedy scholars",
    "Nidhi Khariwal abacus teacher",
    "abacus instructor",
    "online abacus school",
    "abacus educator",
  ],
  openGraph: {
    title: "About Speedy Scholars | Expert Abacus Educator Nidhi Khariwal",
    description:
      "20+ years of abacus teaching excellence. Meet the award-winning educator behind Speedy Scholars and discover our mission to transform children's math abilities.",
    url: "https://www.speedyscholars.com/about",
    siteName: "Speedy Scholars",
    images: [
      {
        url: "https://www.speedyscholars.com/images/og-image.jpg",
        width: 1200,
        height: 630,
        alt: "Nidhi Khariwal - Founder of Speedy Scholars",
      },
    ],
    type: "website",
  },
  alternates: {
    canonical: "https://www.speedyscholars.com/about",
  },
};

export default function AboutLayout({ children }: { children: React.ReactNode }) {
  return children;
}
