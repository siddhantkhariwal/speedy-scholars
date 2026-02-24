"use client";

import { motion } from "framer-motion";
import Image from "next/image";
import Link from "next/link";

const fadeInUp = {
  initial: { opacity: 0, y: 40 },
  whileInView: { opacity: 1, y: 0 },
  viewport: { once: true },
  transition: { duration: 0.6 },
};

const timeline = [
  { year: "2003", event: "Founded Speedy Scholars with a single classroom and a vision to make mental math accessible to every child." },
  { year: "2006", event: "Expanded curriculum to include all levels of abacus training. First batch of students wins district-level competitions." },
  { year: "2009", event: "Received the Regional Excellence in Education Award. Expanded to serve students across multiple states." },
  { year: "2012", event: "Surpassed 500 students trained. Students begin competing and winning at national abacus championships." },
  { year: "2015", event: "Launched online classes to serve students globally. Welcomed students from the USA, UK, and Australia." },
  { year: "2018", event: "Crossed 1,000 students trained worldwide. 50th competition winner milestone achieved." },
  { year: "2020", event: "Transitioned fully to live online classes during the pandemic. Zero disruption to student learning." },
  { year: "2023", event: "Reached 2,000+ students across 15+ countries. Awarded for contributions to global mathematics education." },
  { year: "2026", event: "Continuing to transform young minds worldwide through expert abacus instruction and personalized teaching." },
];

const methodology = [
  {
    step: "01",
    title: "Assessment",
    description:
      "Every student begins with a personalised assessment to understand their current level, learning style, and goals.",
  },
  {
    step: "02",
    title: "Foundation Building",
    description:
      "Mastery of the physical abacus — place value, bead manipulation, and basic operations — forms the solid base.",
  },
  {
    step: "03",
    title: "Speed Development",
    description:
      "Structured drills and timed practice build calculation speed while maintaining accuracy.",
  },
  {
    step: "04",
    title: "Mental Transition",
    description:
      "Students progressively visualise the abacus mentally, performing complex calculations without the physical tool.",
  },
  {
    step: "05",
    title: "Mastery & Beyond",
    description:
      "Advanced students tackle multi-row operations, competition prep, and develop true mathematical intuition.",
  },
];

const differentiators = [
  {
    icon: "🎓",
    title: "20+ Years of Expertise",
    description:
      "Mrs. Nidhi Khariwal brings over two decades of dedicated abacus teaching — a depth of experience that is exceptionally rare in online education.",
  },
  {
    icon: "👤",
    title: "Truly Personalised Instruction",
    description:
      "Every child learns differently. Our curriculum adapts to each student's pace, style, and goals — no one-size-fits-all approach.",
  },
  {
    icon: "🌍",
    title: "Global Reach, Local Care",
    description:
      "Students from 15+ countries attend our classes. Flexible scheduling accommodates every time zone while maintaining the personal touch of small-group instruction.",
  },
  {
    icon: "🏆",
    title: "Proven Competition Results",
    description:
      "50+ students have won state, national, and international abacus competitions under our coaching — a testament to the quality of instruction.",
  },
  {
    icon: "📊",
    title: "Transparent Progress Tracking",
    description:
      "Regular assessments, parent reports, and clear milestones keep families informed and students motivated throughout their journey.",
  },
  {
    icon: "💯",
    title: "Results-First Philosophy",
    description:
      "We measure our success by your child's progress — in calculation speed, concentration, academic confidence, and overall mathematical ability.",
  },
];

const achievements = [
  { number: "20+", label: "Years of Teaching Excellence" },
  { number: "2,000+", label: "Students Trained Worldwide" },
  { number: "50+", label: "Competition Champions" },
  { number: "15+", label: "Awards & Recognitions" },
  { number: "15+", label: "Countries Served" },
  { number: "4.9★", label: "Average Student Rating" },
];

export default function AboutPage() {
  return (
    <div className="min-h-screen" style={{ backgroundColor: "#FDF8F3" }}>
      {/* Navigation */}
      <nav
        style={{ backgroundColor: "#6B5335" }}
        className="sticky top-0 z-50 shadow-md"
        aria-label="Main navigation"
      >
        <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
          <Link href="/" className="flex items-center gap-3" aria-label="Speedy Scholars home">
            <Image
              src="/images/logo.png"
              alt="Speedy Scholars logo"
              width={44}
              height={44}
              className="rounded-full"
            />
            <span className="text-white font-bold text-lg hidden sm:block">Speedy Scholars</span>
          </Link>
          <div className="flex items-center gap-4">
            <Link href="/" className="text-amber-200 hover:text-white text-sm transition-colors">
              Home
            </Link>
            <Link
              href="/blog"
              className="text-amber-200 hover:text-white text-sm transition-colors"
            >
              Blog
            </Link>
            <Link
              href="/resources"
              className="text-amber-200 hover:text-white text-sm transition-colors"
            >
              Resources
            </Link>
            <Link
              href="/#pricing"
              className="bg-amber-500 hover:bg-amber-400 text-white text-sm px-4 py-2 rounded-full font-semibold transition-colors"
            >
              Book Free Demo
            </Link>
          </div>
        </div>
      </nav>

      {/* Breadcrumb Schema */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify({
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            itemListElement: [
              { "@type": "ListItem", position: 1, name: "Home", item: "https://www.speedyscholars.com" },
              { "@type": "ListItem", position: 2, name: "About", item: "https://www.speedyscholars.com/about" },
            ],
          }),
        }}
      />

      {/* Hero Section */}
      <header className="relative py-24 px-4 text-white text-center overflow-hidden">
        <div
          className="absolute inset-0"
          style={{
            background: "linear-gradient(135deg, #5A4830 0%, #8B6F47 50%, #6B5335 100%)",
          }}
        />
        <div className="absolute inset-0 opacity-10">
          <div
            className="w-full h-full"
            style={{
              backgroundImage:
                "radial-gradient(circle at 20% 50%, #C9A86C 0%, transparent 50%), radial-gradient(circle at 80% 20%, #D4B896 0%, transparent 40%)",
            }}
          />
        </div>
        <div className="relative z-10 max-w-4xl mx-auto">
          <nav aria-label="Breadcrumb" className="mb-6">
            <ol className="flex justify-center items-center gap-2 text-amber-300 text-sm">
              <li>
                <Link href="/" className="hover:text-white transition-colors">
                  Home
                </Link>
              </li>
              <li aria-hidden="true" className="text-amber-600">/</li>
              <li className="text-amber-100" aria-current="page">
                About
              </li>
            </ol>
          </nav>
          <motion.h1
            className="text-4xl md:text-6xl font-bold mb-6"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
          >
            Transforming Young Minds
            <br />
            <span style={{ color: "#C9A86C" }}>Since 2003</span>
          </motion.h1>
          <motion.p
            className="text-xl md:text-2xl text-amber-100 max-w-2xl mx-auto"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
          >
            Empowering children across 15+ countries with the ancient art and modern science of
            abacus training.
          </motion.p>
        </div>
      </header>

      {/* Achievements Bar */}
      <section
        className="py-12 px-4"
        style={{ backgroundColor: "#8B6F47" }}
        aria-label="Key achievements"
      >
        <div className="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-6 text-center">
          {achievements.map((item, i) => (
            <motion.div
              key={item.label}
              className="text-white"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1 }}
            >
              <p className="text-3xl font-bold" style={{ color: "#C9A86C" }}>
                {item.number}
              </p>
              <p className="text-sm text-amber-200 mt-1">{item.label}</p>
            </motion.div>
          ))}
        </div>
      </section>

      <main className="max-w-6xl mx-auto px-4">
        {/* Founder Story */}
        <section className="py-20" aria-label="Our founder story">
          <div className="grid lg:grid-cols-2 gap-16 items-center">
            <motion.div {...fadeInUp}>
              <h2 className="text-4xl font-bold mb-6" style={{ color: "#5A4830" }}>
                The Story Behind Speedy Scholars
              </h2>
              <p className="text-stone-700 text-lg leading-relaxed mb-6">
                In 2003, Nidhi Khariwal started teaching abacus to a small group of children in her
                local community. She had one clear conviction: that every child carries extraordinary
                mathematical potential, waiting to be unlocked through the right teaching.
              </p>
              <p className="text-stone-700 text-lg leading-relaxed mb-6">
                What began as a modest local initiative grew into something far greater. Students who
                once struggled with basic arithmetic became competition champions. Children who
                avoided maths began to love it. Parents watched in astonishment as their children
                performed complex mental calculations at speeds that defied belief.
              </p>
              <p className="text-stone-700 text-lg leading-relaxed">
                Today, Speedy Scholars serves over 2,000 students across 15+ countries through live
                online classes. The mission has never changed: to give every child the mathematical
                foundation and cognitive confidence they deserve.
              </p>
            </motion.div>
            <motion.div
              className="relative h-96 lg:h-[500px] rounded-3xl overflow-hidden shadow-2xl"
              initial={{ opacity: 0, scale: 0.95 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true }}
              transition={{ duration: 0.7 }}
            >
              <Image
                src="/images/founder.jpeg"
                alt="Nidhi Khariwal, founder and lead instructor of Speedy Scholars, teaching abacus"
                fill
                className="object-cover"
              />
              <div
                className="absolute bottom-0 left-0 right-0 p-6 text-white"
                style={{
                  background: "linear-gradient(to top, rgba(90,72,48,0.9) 0%, transparent 100%)",
                }}
              >
                <p className="font-bold text-xl">Nidhi Khariwal</p>
                <p style={{ color: "#C9A86C" }}>Founder &amp; Lead Instructor</p>
              </div>
            </motion.div>
          </div>
        </section>

        {/* Timeline */}
        <section className="py-20" aria-label="Our journey timeline">
          <motion.h2
            className="text-4xl font-bold text-center mb-16"
            style={{ color: "#5A4830" }}
            {...fadeInUp}
          >
            20+ Years of Growth
          </motion.h2>
          <div className="relative">
            {/* Timeline line */}
            <div
              className="absolute left-4 md:left-1/2 top-0 bottom-0 w-0.5 md:-translate-x-0.5"
              style={{ backgroundColor: "#D4B896" }}
              aria-hidden="true"
            />
            <div className="space-y-10">
              {timeline.map((item, i) => (
                <motion.div
                  key={item.year}
                  className={`relative flex gap-8 md:gap-0 ${i % 2 === 0 ? "md:flex-row" : "md:flex-row-reverse"}`}
                  initial={{ opacity: 0, x: i % 2 === 0 ? -30 : 30 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: 0.1 }}
                >
                  <div className="w-full md:w-1/2 px-0 md:px-10">
                    <div
                      className="p-6 rounded-2xl shadow-md"
                      style={{ backgroundColor: "#FFF8F0", border: "1px solid #D4B896" }}
                    >
                      <span
                        className="inline-block px-3 py-1 rounded-full text-sm font-bold text-white mb-3"
                        style={{ backgroundColor: "#8B6F47" }}
                      >
                        {item.year}
                      </span>
                      <p className="text-stone-700 leading-relaxed">{item.event}</p>
                    </div>
                  </div>
                  {/* Dot */}
                  <div
                    className="absolute left-4 md:left-1/2 w-4 h-4 rounded-full border-4 border-white shadow-md -translate-x-1.5 md:-translate-x-2 top-8"
                    style={{ backgroundColor: "#C9A86C" }}
                    aria-hidden="true"
                  />
                </motion.div>
              ))}
            </div>
          </div>
        </section>

        {/* Teaching Methodology */}
        <section className="py-20" aria-label="Teaching methodology">
          <motion.div className="text-center mb-16" {...fadeInUp}>
            <h2 className="text-4xl font-bold mb-4" style={{ color: "#5A4830" }}>
              Our Teaching Methodology
            </h2>
            <p className="text-stone-600 text-lg max-w-2xl mx-auto">
              A structured, research-backed pathway from beginner to mental math mastery — designed
              for each child&apos;s individual pace.
            </p>
          </motion.div>
          <div className="grid md:grid-cols-5 gap-4">
            {methodology.map((step, i) => (
              <motion.div
                key={step.step}
                className="text-center p-6 rounded-2xl"
                style={{ backgroundColor: "#FFF8F0", border: "1px solid #D4B896" }}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
              >
                <div
                  className="w-12 h-12 rounded-full flex items-center justify-center text-white font-bold text-lg mx-auto mb-4"
                  style={{ backgroundColor: "#8B6F47" }}
                  aria-hidden="true"
                >
                  {step.step}
                </div>
                <h3 className="font-bold text-lg mb-2" style={{ color: "#5A4830" }}>
                  {step.title}
                </h3>
                <p className="text-stone-600 text-sm leading-relaxed">{step.description}</p>
              </motion.div>
            ))}
          </div>
        </section>

        {/* Why Choose Us */}
        <section className="py-20" aria-label="Why choose Speedy Scholars">
          <motion.div className="text-center mb-16" {...fadeInUp}>
            <h2 className="text-4xl font-bold mb-4" style={{ color: "#5A4830" }}>
              Why Families Choose Speedy Scholars
            </h2>
            <p className="text-stone-600 text-lg max-w-2xl mx-auto">
              What sets our abacus education apart from the rest.
            </p>
          </motion.div>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {differentiators.map((item, i) => (
              <motion.div
                key={item.title}
                className="p-8 rounded-2xl shadow-sm hover:shadow-md transition-shadow"
                style={{ backgroundColor: "#FFF8F0", border: "1px solid #D4B896" }}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
              >
                <div className="text-4xl mb-4" aria-hidden="true">
                  {item.icon}
                </div>
                <h3 className="font-bold text-xl mb-3" style={{ color: "#5A4830" }}>
                  {item.title}
                </h3>
                <p className="text-stone-600 leading-relaxed">{item.description}</p>
              </motion.div>
            ))}
          </div>
        </section>

        {/* Founder Deep Dive */}
        <section className="py-20" aria-label="About our instructor">
          <motion.div
            className="rounded-3xl overflow-hidden shadow-xl"
            style={{
              background: "linear-gradient(135deg, #5A4830 0%, #8B6F47 100%)",
            }}
            {...fadeInUp}
          >
            <div className="grid lg:grid-cols-2">
              <div className="p-10 md:p-14 text-white">
                <p
                  className="text-sm font-semibold uppercase tracking-wider mb-4"
                  style={{ color: "#C9A86C" }}
                >
                  Meet Your Instructor
                </p>
                <h2 className="text-3xl md:text-4xl font-bold mb-2">Nidhi Khariwal</h2>
                <p className="text-xl mb-8" style={{ color: "#D4B896" }}>
                  Founder &amp; Lead Instructor
                </p>
                <p className="text-amber-100 leading-relaxed mb-6">
                  With over 20 years of dedicated experience in abacus education, Nidhi Khariwal
                  has transformed the mathematical lives of more than 2,000 students across the
                  globe. Her passion for making mathematics accessible and joyful drives everything
                  at Speedy Scholars.
                </p>
                <p className="text-amber-100 leading-relaxed mb-8">
                  Her innovative teaching approach combines the time-tested abacus technique with
                  modern understanding of child psychology and learning science. Students do not just
                  learn to calculate — they develop the cognitive confidence to excel in all areas of
                  their academic lives.
                </p>
                <ul className="space-y-3">
                  {[
                    "20+ Years of Teaching Excellence",
                    "2,000+ Students Trained Worldwide",
                    "Award-Winning Educator (15+ Awards)",
                    "50+ Competition Champions Coached",
                    "Serving 15+ Countries via Live Online Classes",
                  ].map((item) => (
                    <li key={item} className="flex items-center gap-3 text-amber-100">
                      <div
                        className="w-2 h-2 rounded-full flex-shrink-0"
                        style={{ backgroundColor: "#C9A86C" }}
                        aria-hidden="true"
                      />
                      {item}
                    </li>
                  ))}
                </ul>
              </div>
              <div className="relative h-80 lg:h-auto">
                <Image
                  src="/images/founder.jpeg"
                  alt="Nidhi Khariwal teaching abacus online — founder of Speedy Scholars with 20+ years experience"
                  fill
                  className="object-cover"
                />
              </div>
            </div>
          </motion.div>
        </section>
      </main>

      {/* CTA Section */}
      <section
        className="py-20 px-4 text-center"
        style={{ backgroundColor: "#F5EDE3" }}
        aria-label="Book your free demo class"
      >
        <motion.div className="max-w-3xl mx-auto" {...fadeInUp}>
          <h2 className="text-4xl font-bold mb-6" style={{ color: "#5A4830" }}>
            Begin Your Child&apos;s Journey Today
          </h2>
          <p className="text-stone-600 text-xl mb-10">
            Join over 2,000 students who have transformed their mathematical abilities with Speedy
            Scholars. Start with a completely free, no-commitment demo class.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              href="/#pricing"
              className="inline-block font-bold px-10 py-5 rounded-full text-xl transition-all text-white shadow-lg hover:shadow-xl hover:scale-105"
              style={{ backgroundColor: "#8B6F47" }}
              aria-label="Book your free 45-minute demo class"
            >
              Book Your FREE Demo Class
            </Link>
            <Link
              href="/contact"
              className="inline-block font-bold px-10 py-5 rounded-full text-xl transition-all shadow-md hover:shadow-lg"
              style={{
                backgroundColor: "transparent",
                border: "2px solid #8B6F47",
                color: "#8B6F47",
              }}
              aria-label="Contact Speedy Scholars"
            >
              Get in Touch
            </Link>
          </div>
        </motion.div>
      </section>

      {/* Footer */}
      <footer style={{ backgroundColor: "#5A4830" }} className="py-10 px-4" aria-label="Footer">
        <div className="max-w-6xl mx-auto">
          <div className="flex flex-col md:flex-row justify-between items-center gap-6">
            <Link href="/" className="flex items-center gap-3" aria-label="Speedy Scholars home">
              <Image
                src="/images/logo.png"
                alt="Speedy Scholars logo"
                width={40}
                height={40}
                className="rounded-full"
              />
              <span className="text-white font-bold">Speedy Scholars</span>
            </Link>
            <nav aria-label="Footer navigation" className="flex flex-wrap justify-center gap-6 text-sm">
              <Link href="/" className="text-amber-300 hover:text-white transition-colors">
                Home
              </Link>
              <Link href="/blog" className="text-amber-300 hover:text-white transition-colors">
                Blog
              </Link>
              <Link href="/resources" className="text-amber-300 hover:text-white transition-colors">
                Resources
              </Link>
              <Link href="/contact" className="text-amber-300 hover:text-white transition-colors">
                Contact
              </Link>
              <Link href="/privacy" className="text-amber-300 hover:text-white transition-colors">
                Privacy
              </Link>
              <Link href="/terms" className="text-amber-300 hover:text-white transition-colors">
                Terms
              </Link>
            </nav>
          </div>
          <div className="mt-6 pt-6 border-t border-amber-800 text-center text-amber-300 text-sm">
            &copy; 2026 Speedy Scholars. All rights reserved.
          </div>
        </div>
      </footer>
    </div>
  );
}
