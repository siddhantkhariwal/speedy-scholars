import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Contact Speedy Scholars | Book a Free Demo Class Today",
  description:
    "Get in touch with Speedy Scholars to book your child's FREE 45-minute demo abacus class. Call, WhatsApp, or email us — flexible scheduling available worldwide.",
  keywords: [
    "contact speedy scholars",
    "book abacus class",
    "free demo class",
    "abacus class inquiry",
    "online abacus enrollment",
  ],
  openGraph: {
    title: "Contact Speedy Scholars | Book Your Free Demo Class",
    description:
      "Ready to start your child's abacus journey? Contact us to book a free 45-minute demo class. We respond within 24 hours.",
    url: "https://www.speedyscholars.com/contact",
    siteName: "Speedy Scholars",
    images: [
      {
        url: "https://www.speedyscholars.com/images/og-image.jpg",
        width: 1200,
        height: 630,
        alt: "Contact Speedy Scholars",
      },
    ],
    type: "website",
  },
  alternates: {
    canonical: "https://www.speedyscholars.com/contact",
  },
};

export default function ContactLayout({ children }: { children: React.ReactNode }) {
  return children;
}
