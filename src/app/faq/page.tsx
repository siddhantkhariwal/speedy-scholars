import { Metadata } from "next";
import Link from "next/link";
import { BookDemoLink } from "@/components/BookDemoLink";

export const metadata: Metadata = {
  title: {
    absolute:
      "Online Abacus Classes: Frequently Asked Questions | Speedy Scholars",
  },
  description:
    "Straight answers about online abacus classes: what age to start, how long results take, whether online works as well as in person, what equipment you need, and what it costs.",
  keywords: [
    "abacus classes FAQ",
    "online abacus questions",
    "does abacus work",
    "abacus for kids questions",
    "how long does abacus take to learn",
    "abacus class requirements",
  ],
  openGraph: {
    title: "Online Abacus Classes: Frequently Asked Questions",
    description:
      "Answers to the questions parents ask most about online abacus classes for children.",
    url: "https://www.speedyscholars.com/faq",
    siteName: "Speedy Scholars",
    images: [
      {
        url: "https://www.speedyscholars.com/images/og-image.jpg",
        width: 1200,
        height: 630,
        alt: "Online abacus classes FAQ",
      },
    ],
    type: "website",
  },
  alternates: {
    canonical: "https://www.speedyscholars.com/faq",
  },
};

const sections: { heading: string; items: { q: string; a: string }[] }[] = [
  {
    heading: "Getting started",
    items: [
      {
        q: "What is the best age to start abacus classes?",
        a: "Children can start from around age 4, and the strongest window is roughly 7 to 10 years old. At that age children pick up the bead mechanics quickly and can begin visualising the abacus mentally. Older children still benefit, they simply move through the early levels faster.",
      },
      {
        q: "Does my child need any maths ability to start?",
        a: "No. A child only needs to recognise numbers and be able to sit and focus for a short session. The abacus method starts from the very beginning and builds up, so it works for children who currently dislike maths as well as children who are already ahead.",
      },
      {
        q: "What equipment do we need?",
        a: "A physical abacus, a device with a camera such as a laptop or tablet, and a stable internet connection. We tell you exactly which abacus to buy before the first class, and we can start the demo without one.",
      },
      {
        q: "Is the first class really free?",
        a: "Yes. The first class is a free 30-minute demo with the instructor. There is no payment, no card details and no obligation to continue.",
      },
    ],
  },
  {
    heading: "How the classes work",
    items: [
      {
        q: "Are online abacus classes as effective as in-person classes?",
        a: "Yes, when they are live and taught in small groups. The abacus method depends on the instructor watching the child's hands and correcting technique, which works over video as long as the camera shows the abacus. What online removes is travel time and large class sizes, which is why many children get more individual attention online than at a centre.",
      },
      {
        q: "Are classes live or pre-recorded?",
        a: "Every class is live with the instructor. There are no pre-recorded videos, because a child learning abacus needs their mistakes corrected in the moment.",
      },
      {
        q: "How long is each class and how often are they?",
        a: "The free demo is 30 minutes. Regular classes are 45 minutes, and most students take one or two classes a week alongside short daily practice at home.",
      },
      {
        q: "Who teaches the classes?",
        a: "Classes are taught by Nidhi Khariwal, founder of Speedy Scholars, who has taught abacus for over 20 years to more than 2,000 students and has coached 50 or more competition winners. She teaches in English and Hindi.",
      },
      {
        q: "Which countries do you teach students in?",
        a: "We teach families in the United States, United Kingdom, Australia, New Zealand, Canada and India. Class times are scheduled around your timezone.",
      },
    ],
  },
  {
    heading: "Results and progress",
    items: [
      {
        q: "How long does it take to see results?",
        a: "Most parents notice better concentration and faster basic calculation within 8 to 12 weeks of consistent classes and short daily practice. Full mental calculation, where the child pictures the abacus instead of using it, usually develops over one to two years of steady progress through the levels.",
      },
      {
        q: "How much practice does my child need at home?",
        a: "About 10 to 15 minutes a day. Abacus rewards short frequent practice far more than long occasional sessions.",
      },
      {
        q: "Does abacus training actually help with school maths?",
        a: "Yes, mostly indirectly. Children gain calculation speed and accuracy, which reduces the time they spend on arithmetic, and they build concentration and working memory, which helps across subjects. Many parents report that maths anxiety drops because the child stops feeling slow.",
      },
      {
        q: "What if my child is not enjoying it?",
        a: "You can stop at any time. There is no contract and no notice period. We would rather you pause than push a child through lessons they resent, because abacus depends on consistent willing practice.",
      },
    ],
  },
  {
    heading: "Pricing and scheduling",
    items: [
      {
        q: "How much do the classes cost?",
        a: "A single class is $20 (£15, A$30, ₹1,600) and a 10-class pack is $150 (£120, A$230, ₹12,500), which works out to $15 per class. The first 30-minute demo is free. There is no joining fee, registration fee or exam fee.",
      },
      {
        q: "Can we reschedule a class?",
        a: "Yes. Classes can be rescheduled with reasonable notice, and unused classes in a pack stay available for you to book later.",
      },
      {
        q: "How do we book?",
        a: "Book the free demo through the booking page, pick a time that suits your timezone, and you will get a confirmation email with the meeting link plus reminders before the class.",
      },
    ],
  },
];

export default function FaqPage() {
  const allItems = sections.flatMap((s) => s.items);

  const faqSchema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: allItems.map((f) => ({
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

      <section className="bg-gradient-to-br from-[#5A2A72] to-[#3F1D50] text-white">
        <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
          <h1 className="text-4xl md:text-5xl font-bold leading-tight mb-6">
            Online abacus classes: your questions answered
          </h1>
          <p className="text-xl text-white/90 max-w-3xl">
            Straight answers to what parents ask us most, written by an
            instructor with 20 years of teaching behind them.
          </p>
        </div>
      </section>

      <main className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        {sections.map((section) => (
          <section key={section.heading} className="mb-14">
            <h2 className="text-3xl font-bold text-[#32173F] mb-6">
              {section.heading}
            </h2>
            <div className="space-y-5">
              {section.items.map((f) => (
                <div
                  key={f.q}
                  className="border border-[#EFE7F3] rounded-2xl p-6 bg-[#F8F5F9]"
                >
                  <h3 className="text-lg font-bold text-[#32173F] mb-2">
                    {f.q}
                  </h3>
                  <p className="text-[#3A313F] leading-relaxed">{f.a}</p>
                </div>
              ))}
            </div>
          </section>
        ))}

        <section className="mb-14">
          <h2 className="text-2xl font-bold text-[#32173F] mb-4">
            Still deciding?
          </h2>
          <p className="text-[#3A313F] leading-relaxed">
            You may find these useful:{" "}
            <Link
              href="/online-abacus-classes"
              className="text-[#5A2A72] font-semibold hover:underline"
            >
              how our online abacus classes work
            </Link>
            ,{" "}
            <Link
              href="/online-abacus-classes-cost"
              className="text-[#5A2A72] font-semibold hover:underline"
            >
              full pricing
            </Link>
            , or{" "}
            <Link
              href="/blog/best-age-to-start-abacus"
              className="text-[#5A2A72] font-semibold hover:underline"
            >
              the best age to start
            </Link>
            .
          </p>
        </section>

        <section className="text-center bg-gradient-to-br from-[#5A2A72] to-[#3F1D50] rounded-3xl p-10 text-white">
          <h2 className="text-3xl font-bold mb-4">
            The fastest way to get your answer
          </h2>
          <p className="text-white/90 mb-8 max-w-2xl mx-auto">
            Book a free 30-minute demo and ask Nidhi directly. Most parents
            decide within that one class.
          </p>
          <BookDemoLink location="faq_footer_cta" variant="gold">
            Book the free demo
          </BookDemoLink>
        </section>
      </main>
    </div>
  );
}
