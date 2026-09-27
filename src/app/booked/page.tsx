import type { Metadata } from "next";
import Link from "next/link";
import { CheckCircle } from "lucide-react";
import { BookingTracker } from "./BookingTracker";

// Cal.com redirects here after a demo is booked (Event type → Advanced →
// "Redirect on booking"). Kept out of search results and the sitemap.
export const metadata: Metadata = {
  title: "Demo Booked | Speedy Scholars",
  robots: { index: false, follow: false },
};

export default function BookedPage() {
  return (
    <main className="min-h-screen flex items-center justify-center bg-[#FDF8F0] px-4 py-16">
      <BookingTracker />
      <div className="max-w-lg text-center">
        <CheckCircle className="w-16 h-16 text-[#5A2A72] mx-auto mb-6" />
        <h1 className="text-3xl md:text-4xl font-bold text-[#32173F] mb-4">
          Your free demo is booked
        </h1>
        <p className="text-lg text-gray-700 mb-8">
          A confirmation with the meeting link is on its way to your email. If
          you need to reschedule, use the link in that email or message us on
          WhatsApp.
        </p>
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <Link
            href="/online-abacus-classes"
            className="inline-flex items-center justify-center px-8 py-4 rounded-full font-semibold bg-[#5A2A72] text-white hover:bg-[#3F1D50] transition-all"
          >
            See how classes work
          </Link>
          <a
            href="https://wa.me/919352646671"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center justify-center px-8 py-4 rounded-full font-semibold bg-[#F9AE27] text-[#32173F] hover:bg-[#CA8406] transition-all"
          >
            WhatsApp us
          </a>
        </div>
      </div>
    </main>
  );
}
