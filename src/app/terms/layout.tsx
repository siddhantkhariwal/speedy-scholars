import { Metadata } from "next";

export const metadata: Metadata = {
  title: { absolute: "Terms of Service | Speedy Scholars" },
  description:
    "The terms that apply to booking and attending Speedy Scholars online abacus classes, including payment, rescheduling and cancellation.",
  alternates: {
    canonical: "https://www.speedyscholars.com/terms",
  },
  robots: {
    index: true,
    follow: true,
  },
};

export default function TermsLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return children;
}
