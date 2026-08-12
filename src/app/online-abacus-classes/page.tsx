import { Metadata } from "next";
import Link from "next/link";
import { CheckCircle, Globe, Users, Award, Clock, Video, GraduationCap } from "lucide-react";
import { BookDemoLink } from "@/components/BookDemoLink";

export const metadata: Metadata = {
  title: {
    absolute:
      "Online Abacus Classes for Kids | Live 1-on-1 Lessons | Speedy Scholars",
  },
  description:
    "Live online abacus classes for children aged 4 to 14. Taught by Nidhi Khariwal, 20+ years experience and 2,000+ students worldwide. Free 30-minute demo, no commitment.",
  keywords: [
    "online abacus classes",
    "online abacus classes for kids",
    "abacus classes for children",
    "live abacus lessons online",
    "abacus tutor online",
    "mental math classes online",
    "abacus classes USA",
    "abacus classes UK",
    "abacus classes Australia",
  ],
  openGraph: {
    title: "Online Abacus Classes for Kids | Live 1-on-1 Lessons",
    description:
      "Live online abacus classes for children aged 4 to 14, taught by an instructor with 20+ years of experience and 2,000+ students worldwide.",
    url: "https://www.speedyscholars.com/online-abacus-classes",
    siteName: "Speedy Scholars",
    images: [
      {
        url: "https://www.speedyscholars.com/images/og-image.jpg",
        width: 1200,
        height: 630,
        alt: "Online Abacus Classes for Kids",
      },
    ],
    type: "website",
  },
  alternates: {
    canonical: "https://www.speedyscholars.com/online-abacus-classes",
  },
};

const howItWorks = [
  {
    icon: Video,
    title: "Live, not recorded",
    text: "Every class is a live video lesson with a real instructor. Your child asks questions and gets answers in the moment, the same as an in-person class.",
  },
  {
    icon: Users,
    title: "Small group or one-to-one",
    text: "Lessons are taught one-to-one or in very small groups, so the pace matches your child instead of the class average.",
  },
  {
    icon: Clock,
    title: "Scheduled around your timezone",
    text: "We teach families across the USA, UK, Australia, New Zealand and Canada. You pick a slot that fits your evenings or weekends.",
  },
  {
    icon: GraduationCap,
    title: "A structured level system",
    text: "Students move through clear levels, each with its own workbook and goals, so progress is visible rather than vague.",
  },
];

const whatTheyLearn = [
  "Reading and setting numbers on a physical abacus",
  "Addition and subtraction on the abacus, then at speed",
  "Multiplication and division as levels progress",
  "Visualising the abacus mentally, which is where mental math begins",
  "Calculating without any tool, faster than with a calculator",
  "Concentration, memory and listening skills that carry into school",
];

const ageGroups = [
  {
    range: "Ages 4 to 6",
    title: "Foundation",
    text: "Number recognition, bead movement and simple addition. Short sessions built around play and repetition.",
  },
  {
    range: "Ages 7 to 10",
    title: "Core skill building",
    text: "The strongest starting window. Children pick up abacus mechanics quickly and begin visualising the beads mentally.",
  },
  {
    range: "Ages 11 to 14",
    title: "Speed and application",
    text: "Faster calculation, larger numbers, and applying mental math to school work and competitive exams.",
  },
];

export default function OnlineAbacusClassesPage() {
  const courseSchema = {
    "@context": "https://schema.org",
    "@type": "Course",
    name: "Online Abacus Classes for Kids",
    description:
      "Live online abacus and mental arithmetic classes for children aged 4 to 14, taught by Nidhi Khariwal, an instructor with over 20 years of experience.",
    url: "https://www.speedyscholars.com/online-abacus-classes",
    provider: {
      "@type": "EducationalOrganization",
      name: "Speedy Scholars",
      url: "https://www.speedyscholars.com",
    },
    educationalLevel: "Beginner to Advanced",
    teaches:
      "Abacus technique, mental arithmetic, calculation speed, concentration",
    inLanguage: ["en", "hi"],
    hasCourseInstance: {
      "@type": "CourseInstance",
      courseMode: "Online",
      courseWorkload: "PT30M",
      instructor: {
        "@type": "Person",
        name: "Nidhi Khariwal",
        jobTitle: "Founder and Lead Instructor",
      },
    },
  };

  return (
    <div className="min-h-screen bg-white">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(courseSchema) }}
      />

      {/* Hero */}
      <section className="bg-gradient-to-br from-[#5A2A72] to-[#3F1D50] text-white">
        <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
          <h1 className="text-4xl md:text-5xl font-bold leading-tight mb-6">
            Online Abacus Classes for Kids
          </h1>
          <p className="text-xl text-white/90 max-w-3xl mb-8">
            Live, one-to-one abacus and mental math lessons for children aged 4
            to 14. Taught by Nidhi Khariwal, who has spent over 20 years
            teaching more than 2,000 students across the world.
          </p>
          <div className="flex flex-wrap gap-4 items-center">
            <BookDemoLink location="oac_hero" variant="gold">
              Book a free 30-minute demo
            </BookDemoLink>
            <span className="text-white/80">No payment, no commitment.</span>
          </div>
        </div>
      </section>

      {/* Trust strip */}
      <section className="bg-[#F8F5F9] border-b border-[#EFE7F3]">
        <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
          {[
            { icon: Award, stat: "20+", label: "Years teaching" },
            { icon: Users, stat: "2,000+", label: "Students taught" },
            { icon: GraduationCap, stat: "50+", label: "Competition winners" },
            { icon: Globe, stat: "6", label: "Countries served" },
          ].map((item) => (
            <div key={item.label}>
              <item.icon className="w-6 h-6 text-[#5A2A72] mx-auto mb-2" />
              <div className="text-2xl font-bold text-[#32173F]">
                {item.stat}
              </div>
              <div className="text-sm text-[#3A313F]">{item.label}</div>
            </div>
          ))}
        </div>
      </section>

      <main className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        {/* What is it */}
        <section className="mb-16">
          <h2 className="text-3xl font-bold text-[#32173F] mb-4">
            What are online abacus classes?
          </h2>
          <p className="text-[#3A313F] leading-relaxed mb-4">
            An online abacus class teaches a child to calculate using a physical
            abacus, and then to picture that abacus in their head. Once the
            image is strong enough, they can add, subtract, multiply and divide
            mentally, often faster than an adult with a calculator.
          </p>
          <p className="text-[#3A313F] leading-relaxed">
            The classes are taught live over video. Your child keeps a real
            abacus in front of them, the instructor watches their hands and
            corrects technique as they work. Nothing about the method changes
            because it is online. What changes is that you are not driving to a
            centre twice a week.
          </p>
        </section>

        {/* How it works */}
        <section className="mb-16">
          <h2 className="text-3xl font-bold text-[#32173F] mb-8">
            How our classes work
          </h2>
          <div className="grid md:grid-cols-2 gap-6">
            {howItWorks.map((item) => (
              <div
                key={item.title}
                className="bg-[#F8F5F9] rounded-2xl p-6 border border-[#EFE7F3]"
              >
                <item.icon className="w-8 h-8 text-[#5A2A72] mb-3" />
                <h3 className="text-xl font-bold text-[#32173F] mb-2">
                  {item.title}
                </h3>
                <p className="text-[#3A313F] leading-relaxed">{item.text}</p>
              </div>
            ))}
          </div>
        </section>

        {/* What they learn */}
        <section className="mb-16">
          <h2 className="text-3xl font-bold text-[#32173F] mb-6">
            What your child will learn
          </h2>
          <ul className="space-y-3">
            {whatTheyLearn.map((item) => (
              <li key={item} className="flex items-start gap-3">
                <CheckCircle className="w-5 h-5 text-[#5A2A72] flex-shrink-0 mt-1" />
                <span className="text-[#3A313F] leading-relaxed">{item}</span>
              </li>
            ))}
          </ul>
        </section>

        {/* Ages */}
        <section className="mb-16">
          <h2 className="text-3xl font-bold text-[#32173F] mb-3">
            What age should a child start?
          </h2>
          <p className="text-[#3A313F] leading-relaxed mb-8">
            Children can start from around age 4, and the strongest window is
            roughly 7 to 10. Older children still benefit, they simply move
            through the early levels faster.
          </p>
          <div className="grid md:grid-cols-3 gap-6">
            {ageGroups.map((g) => (
              <div
                key={g.range}
                className="border border-[#EFE7F3] rounded-2xl p-6"
              >
                <div className="text-sm font-semibold text-[#CA8406] mb-1">
                  {g.range}
                </div>
                <h3 className="text-lg font-bold text-[#32173F] mb-2">
                  {g.title}
                </h3>
                <p className="text-[#3A313F] text-sm leading-relaxed">
                  {g.text}
                </p>
              </div>
            ))}
          </div>
          <p className="text-[#3A313F] leading-relaxed mt-6">
            For a fuller answer, read{" "}
            <Link
              href="/blog/best-age-to-start-abacus"
              className="text-[#5A2A72] font-semibold hover:underline"
            >
              the best age to start abacus
            </Link>
            .
          </p>
        </section>

        {/* Instructor */}
        <section className="mb-16 bg-[#F8F5F9] rounded-3xl p-8 border border-[#EFE7F3]">
          <h2 className="text-3xl font-bold text-[#32173F] mb-4">
            Who teaches the classes
          </h2>
          <p className="text-[#3A313F] leading-relaxed mb-4">
            Every class is taught by Nidhi Khariwal, the founder of Speedy
            Scholars. She has taught abacus for more than 20 years to over
            2,000 students, has coached 50+ competition winners, and teaches in
            both English and Hindi.
          </p>
          <p className="text-[#3A313F] leading-relaxed">
            You are not assigned a rotating pool of tutors. The person who
            teaches your free demo is the person who teaches your child.{" "}
            <Link
              href="/about"
              className="text-[#5A2A72] font-semibold hover:underline"
            >
              Read more about Nidhi
            </Link>
            .
          </p>
        </section>

        {/* Pricing pointer */}
        <section className="mb-16">
          <h2 className="text-3xl font-bold text-[#32173F] mb-4">
            What do classes cost?
          </h2>
          <p className="text-[#3A313F] leading-relaxed mb-6">
            The first class is a free 30-minute demo. After that you can pay per
            class or buy a 10-class pack, priced in your local currency. There
            is no joining fee and no long contract.
          </p>
          <Link
            href="/online-abacus-classes-cost"
            className="inline-flex items-center gap-2 text-[#5A2A72] font-semibold hover:underline text-lg"
          >
            See full pricing for online abacus classes
          </Link>
        </section>

        {/* CTA */}
        <section className="text-center bg-gradient-to-br from-[#5A2A72] to-[#3F1D50] rounded-3xl p-10 text-white">
          <h2 className="text-3xl font-bold mb-4">
            Try a free class before you decide
          </h2>
          <p className="text-white/90 mb-8 max-w-2xl mx-auto">
            Book a free 30-minute demo. Your child meets Nidhi, works through a
            real lesson, and you get an honest assessment of where they are.
            Nothing to pay and nothing to cancel.
          </p>
          <BookDemoLink location="oac_footer_cta" variant="gold">
            Book the free demo
          </BookDemoLink>
        </section>
      </main>
    </div>
  );
}
