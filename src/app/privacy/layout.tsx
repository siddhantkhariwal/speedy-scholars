import { Metadata } from "next";

export const metadata: Metadata = {
  title: { absolute: "Privacy Policy | Speedy Scholars" },
  description:
    "How Speedy Scholars collects, uses and protects your personal information when you book a demo class or contact us.",
  alternates: {
    canonical: "https://www.speedyscholars.com/privacy",
  },
  robots: {
    index: true,
    follow: true,
  },
};

export default function PrivacyLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return children;
}
