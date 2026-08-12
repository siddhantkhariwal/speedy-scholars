import { Metadata } from "next";
import Link from "next/link";
import { CheckCircle } from "lucide-react";
import { BookDemoLink } from "@/components/BookDemoLink";

export const metadata: Metadata = {
  title: {
    absolute:
      "How Much Do Online Abacus Classes Cost? 2026 Pricing Guide | Speedy Scholars",
  },
  description:
    "Online abacus classes cost roughly $15 to $30 per class. See full Speedy Scholars pricing in USD, GBP, AUD and INR, what is included, and how packs compare to paying per class.",
  keywords: [
    "online abacus classes cost",
    "abacus class fees",
    "how much do abacus classes cost",
    "abacus classes price",
    "online abacus class fees USA",
    "abacus tuition cost UK",
  ],
  openGraph: {
    title: "How Much Do Online Abacus Classes Cost? 2026 Pricing Guide",
    description:
      "Transparent pricing for live online abacus classes in USD, GBP, AUD and INR. Free 30-minute demo, pay per class or buy a 10-class pack.",
    url: "https://www.speedyscholars.com/online-abacus-classes-cost",
    siteName: "Speedy Scholars",
    images: [
      {
        url: "https://www.speedyscholars.com/images/og-image.jpg",
        width: 1200,
        height: 630,
        alt: "Online abacus class pricing",
      },
    ],
    type: "website",
  },
  alternates: {
    canonical: "https://www.speedyscholars.com/online-abacus-classes-cost",
  },
};

const pricing = [
  {
    tier: "Free demo",
    detail: "30 minutes, one time",
    usd: "Free",
    gbp: "Free",
    aud: "Free",
    inr: "Free",
  },
  {
    tier: "Pay as you go",
    detail: "Per 45-minute class",
    usd: "$20",
    gbp: "£15",
    aud: "A$30",
    inr: "₹1,600",
  },
  {
    tier: "10-class pack",
    detail: "10 x 45-minute classes",
    usd: "$150",
    gbp: "£120",
    aud: "A$230",
    inr: "₹12,500",
  },
];

const included = [
  "Live class with the instructor, not a recording",
  "Workbooks and practice worksheets",
  "Progress tracking and parent updates",
  "Flexible rescheduling",
  "No joining fee, no exam fee, no annual contract",
];

const faqs = [
  {
    q: "How much do online abacus classes cost?",
    a: "Online abacus classes typically cost between $15 and $30 per class worldwide. At Speedy Scholars a single class is $20 (£15, A$30, ₹1,600), and a 10-class pack is $150 (£120, A$230, ₹12,500), which works out to $15 per class. The first 30-minute demo class is free.",
  },
  {
    q: "Is there a discount for buying classes in bulk?",
    a: "Yes. The 10-class pack costs $150 instead of $200 for ten individual classes, so you save 25 percent. The pack also includes books, worksheets and priority scheduling.",
  },
  {
    q: "Do you charge a registration or exam fee?",
    a: "No. There is no joining fee, no registration fee and no annual membership. You pay only for the classes you book.",
  },
  {
    q: "How long is each class?",
    a: "The free demo class is 30 minutes. Regular paid classes are 45 minutes.",
  },
  {
    q: "Can I pay in my own currency?",
    a: "Yes. Pricing is shown in US dollars, British pounds, Australian dollars and Indian rupees, and the website detects your country automatically.",
  },
  {
    q: "What happens if we need to stop?",
    a: "You can stop at any time. There is no contract or notice period. Unused classes in a pack stay available for you to book.",
  },
];

export default function OnlineAbacusClassesCostPage() {
  const faqSchema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: faqs.map((f) => ({
      "@type": "Question",
      name: f.q,
      acceptedAnswer: { "@type": "Answer", text: f.a },
    })),
  };

  return (
    <div className="min-h-screen bg-white">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }}
      />

      {/* Hero */}
      <section className="bg-gradient-to-br from-[#5A2A72] to-[#3F1D50] text-white">
        <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
          <h1 className="text-4xl md:text-5xl font-bold leading-tight mb-6">
            How much do online abacus classes cost?
          </h1>
          <p className="text-xl text-white/90 max-w-3xl">
            Short answer: most online abacus classes cost between $15 and $30
            per class. At Speedy Scholars a single class is $20, a 10-class pack
            brings it down to $15 per class, and the first 30-minute demo is
            free.
          </p>
        </div>
      </section>

      <main className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        {/* Pricing table */}
        <section className="mb-16">
          <h2 className="text-3xl font-bold text-[#32173F] mb-6">
            Speedy Scholars pricing
          </h2>
          <div className="overflow-x-auto rounded-2xl border border-[#EFE7F3]">
            <table className="w-full text-left">
              <thead className="bg-[#F8F5F9]">
                <tr>
                  <th className="px-5 py-4 font-bold text-[#32173F]">Option</th>
                  <th className="px-5 py-4 font-bold text-[#32173F]">USD</th>
                  <th className="px-5 py-4 font-bold text-[#32173F]">GBP</th>
                  <th className="px-5 py-4 font-bold text-[#32173F]">AUD</th>
                  <th className="px-5 py-4 font-bold text-[#32173F]">INR</th>
                </tr>
              </thead>
              <tbody>
                {pricing.map((row) => (
                  <tr key={row.tier} className="border-t border-[#EFE7F3]">
                    <td className="px-5 py-4">
                      <div className="font-semibold text-[#32173F]">
                        {row.tier}
                      </div>
                      <div className="text-sm text-[#3A313F]">{row.detail}</div>
                    </td>
                    <td className="px-5 py-4 text-[#3A313F]">{row.usd}</td>
                    <td className="px-5 py-4 text-[#3A313F]">{row.gbp}</td>
                    <td className="px-5 py-4 text-[#3A313F]">{row.aud}</td>
                    <td className="px-5 py-4 text-[#3A313F]">{row.inr}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <p className="text-sm text-[#3A313F] mt-4">
            The 10-class pack works out to $15 per class, a saving of 25 percent
            against paying per class.
          </p>
        </section>

        {/* Included */}
        <section className="mb-16">
          <h2 className="text-3xl font-bold text-[#32173F] mb-6">
            What is included in the price
          </h2>
          <ul className="space-y-3">
            {included.map((item) => (
              <li key={item} className="flex items-start gap-3">
                <CheckCircle className="w-5 h-5 text-[#5A2A72] flex-shrink-0 mt-1" />
                <span className="text-[#3A313F] leading-relaxed">{item}</span>
              </li>
            ))}
          </ul>
        </section>

        {/* Context */}
        <section className="mb-16">
          <h2 className="text-3xl font-bold text-[#32173F] mb-4">
            How this compares to in-person classes
          </h2>
          <p className="text-[#3A313F] leading-relaxed mb-4">
            In-person abacus centres often charge a monthly fee plus a
            registration fee, books, and level examination fees, which are easy
            to miss when comparing prices. Online classes remove travel time and
            usually remove the extra fees.
          </p>
          <p className="text-[#3A313F] leading-relaxed">
            The other difference is attention. A centre class may have 10 to 20
            children to one teacher. Our classes are one-to-one or very small
            groups, so a lower headline price per hour is not really comparing
            the same thing.
          </p>
        </section>

        {/* FAQ */}
        <section className="mb-16">
          <h2 className="text-3xl font-bold text-[#32173F] mb-6">
            Pricing questions
          </h2>
          <div className="space-y-6">
            {faqs.map((f) => (
              <div
                key={f.q}
                className="border border-[#EFE7F3] rounded-2xl p-6 bg-[#F8F5F9]"
              >
                <h3 className="text-lg font-bold text-[#32173F] mb-2">{f.q}</h3>
                <p className="text-[#3A313F] leading-relaxed">{f.a}</p>
              </div>
            ))}
          </div>
        </section>

        {/* CTA */}
        <section className="text-center bg-gradient-to-br from-[#5A2A72] to-[#3F1D50] rounded-3xl p-10 text-white">
          <h2 className="text-3xl font-bold mb-4">
            Start with the free demo class
          </h2>
          <p className="text-white/90 mb-8 max-w-2xl mx-auto">
            Before you pay anything, book a free 30-minute demo so you can see
            the teaching for yourself.
          </p>
          <BookDemoLink location="cost_footer_cta" variant="gold">
            Book the free demo
          </BookDemoLink>
          <div className="mt-6">
            <Link
              href="/online-abacus-classes"
              className="text-white/90 underline hover:text-white"
            >
              Read more about how the classes work
            </Link>
          </div>
        </section>
      </main>
    </div>
  );
}
