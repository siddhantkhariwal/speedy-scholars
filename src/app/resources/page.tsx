import { Metadata } from "next";
import Link from "next/link";
import Image from "next/image";

export const metadata: Metadata = {
  title: "Free Resources for Parents | Mental Math Tips & Abacus Guide | Speedy Scholars",
  description:
    "Free educational resources for parents: 10 mental math tricks for kids, how to choose the right abacus, and practice tips to support your child at home.",
  keywords: [
    "mental math tricks",
    "how to choose abacus",
    "abacus buying guide",
    "math practice tips for kids",
    "free math resources",
    "abacus practice at home",
  ],
  openGraph: {
    title: "Free Resources for Parents | Speedy Scholars",
    description:
      "Practical, expert-written resources to help parents support their child's abacus and mental math journey at home.",
    url: "https://www.speedyscholars.com/resources",
    siteName: "Speedy Scholars",
    images: [
      {
        url: "https://www.speedyscholars.com/images/og-image.jpg",
        width: 1200,
        height: 630,
        alt: "Speedy Scholars Free Resources",
      },
    ],
    type: "website",
  },
  alternates: {
    canonical: "https://www.speedyscholars.com/resources",
  },
};

const mentalMathTricks = [
  {
    number: "1",
    title: "Round to the Nearest Ten",
    description:
      "When adding numbers like 38 + 47, round 38 to 40 (add 2), compute 40 + 47 = 87, then subtract 2 to get 85. Rounding reduces mental load dramatically.",
    example: "38 + 47: round 38 to 40 → 40 + 47 = 87 → 87 - 2 = 85",
  },
  {
    number: "2",
    title: "Split Numbers Apart (Decomposition)",
    description:
      "Break large numbers into tens and units before adding. 56 + 37 becomes (50 + 30) + (6 + 7) = 80 + 13 = 93. This mirrors how the abacus works.",
    example: "56 + 37 = (50+30) + (6+7) = 80 + 13 = 93",
  },
  {
    number: "3",
    title: "Multiply by 5 Using Halving",
    description:
      "Multiplying by 5 is the same as multiplying by 10 and halving the result. Much easier than direct multiplication.",
    example: "5 × 18 = (10 × 18) ÷ 2 = 180 ÷ 2 = 90",
  },
  {
    number: "4",
    title: "Subtract by Adding Up",
    description:
      "Instead of subtracting 73 - 48, count up from 48 to 73: +2 to 50, +23 to 73 = 25. This counting-up method is more intuitive for most children.",
    example: "73 - 48: count 48→50 (+2), 50→73 (+23) = 25",
  },
  {
    number: "5",
    title: "The 9 Times Table Trick",
    description:
      "For 9 × any single digit: the tens digit is (digit - 1) and the two digits always add to 9. Never memorise the 9 table the hard way again.",
    example: "9 × 7: tens = 7-1 = 6, units = 9-6 = 3 → 63",
  },
  {
    number: "6",
    title: "Double and Halve for Multiplication",
    description:
      "You can double one factor and halve the other without changing the product. This turns awkward multiplications into easy ones.",
    example: "16 × 25: halve 16→8, double 25→50 → 8 × 50 = 400",
  },
  {
    number: "7",
    title: "Estimate First, Then Refine",
    description:
      "Before calculating, estimate the answer. 47 × 6 is roughly 50 × 6 = 300. The real answer (282) is close. Estimation builds number sense and checks for errors.",
    example: "47 × 6 ≈ 50 × 6 = 300 (actual: 282 — in the right range)",
  },
  {
    number: "8",
    title: "Squares of Numbers Ending in 5",
    description:
      "Take the tens digit, multiply by the next number up, and append 25. This gives instant squares for 15, 25, 35, 45, 55, 65, 75 and beyond.",
    example: "35² = 3×4 then append 25 = 1225",
  },
  {
    number: "9",
    title: "The 11 Times Table Pattern",
    description:
      "For 11 × single digits, repeat the digit. For teens (11-18), split the digits and insert their sum in the middle.",
    example: "11 × 7 = 77 | 11 × 14: 1_4, middle = 1+4 = 5 → 154",
  },
  {
    number: "10",
    title: "Percentage Made Simple",
    description:
      "10% of any number is just move the decimal one left. 1% is move it two left. Build percentages from these: 15% = 10% + 5% (half of 10%).",
    example: "15% of 80: 10%=8, 5%=4, total = 12",
  },
];

const abacusGuide = [
  {
    title: "Standard vs Soroban",
    description:
      "The Japanese Soroban (1 upper bead, 4 lower beads per rod) is the modern standard for mental math education. Avoid the older Chinese Suanpan style for educational purposes.",
    recommendation: "Choose a Soroban-style abacus",
  },
  {
    title: "Number of Rods",
    description:
      "A 17-rod abacus covers all numbers up to 99,999,999 — more than sufficient for children. For competitions, 23 rods are sometimes preferred.",
    recommendation: "17 rods is ideal for beginners",
  },
  {
    title: "Bead Material",
    description:
      "Plastic beads move smoothly and are durable. Wooden beads feel pleasant but can warp. Avoid metal beads — they are heavy and loud.",
    recommendation: "Smooth plastic beads are best",
  },
  {
    title: "Frame Colour Coding",
    description:
      "Many educational abacuses use coloured beads to help beginners identify place values. This is helpful for the first 3-4 months but becomes unnecessary over time.",
    recommendation: "Colour coding is great for young beginners",
  },
  {
    title: "Size",
    description:
      "A standard classroom abacus (approximately 23cm × 8cm) is comfortable for ages 5+. Mini abacuses are too small for young children to manipulate accurately.",
    recommendation: "Standard classroom size is appropriate",
  },
  {
    title: "Where to Buy",
    description:
      "Look for educational abacuses from reputable brands on Amazon or educational supply stores. Avoid toy-store versions — they often have imprecise bead movement.",
    recommendation: "Look for educational grade abacuses",
  },
];

const practiceTips = [
  {
    title: "Consistency Over Duration",
    description:
      "15 minutes of daily practice is worth more than 90 minutes once a week. The brain consolidates skills during sleep, so frequent short sessions are ideal.",
  },
  {
    title: "Create a Dedicated Practice Space",
    description:
      "Set up a consistent, distraction-free area for practice. Remove phones, tablets, and other devices. The ritual of going to the same space signals the brain that focus time has begun.",
  },
  {
    title: "Time the Drills",
    description:
      "Use a simple timer for calculation drills. The gentle time pressure maintains alertness and mirrors the focused conditions of class. Track personal bests and celebrate improvement.",
  },
  {
    title: "Praise Effort, Not Just Results",
    description:
      "When your child makes progress — even small progress — acknowledge the hard work that made it happen. \"I can see how much concentration you used\" is more powerful than \"Well done.\"",
  },
  {
    title: "Play Calculation Games",
    description:
      "Turn everyday activities into mental math opportunities. Ask your child to calculate the change at a shop, estimate the total grocery bill, or solve quick mental challenges during car journeys.",
  },
  {
    title: "Never Practice When Tired or Upset",
    description:
      "Abacus practice requires focused attention. A tired or frustrated child will form poor habits and negative associations. If emotions are running high, reschedule and return when calm.",
  },
  {
    title: "Review With Your Child",
    description:
      "Ask your child to explain what they learned in class. Teaching is the deepest form of learning. Listening to your child explain a technique also helps you understand their progress.",
  },
  {
    title: "Communicate With the Instructor",
    description:
      "Share observations about your child's practice at home with their instructor. Good feedback helps the teacher understand where additional support or challenge is needed.",
  },
];

export default function ResourcesPage() {
  return (
    <main>
      {/* Breadcrumb Schema */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify({
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            itemListElement: [
              { "@type": "ListItem", position: 1, name: "Home", item: "https://www.speedyscholars.com" },
              { "@type": "ListItem", position: 2, name: "Resources", item: "https://www.speedyscholars.com/resources" },
            ],
          }),
        }}
      />

      {/* Navigation */}
      <nav
        style={{ backgroundColor: "#6B5335" }}
        className="sticky top-0 z-50 shadow-md"
        aria-label="Main navigation"
      >
        <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
          <Link href="/" className="flex items-center gap-2" aria-label="Speedy Scholars home page">
            <Image
              src="/images/logo.png"
              alt="Speedy Scholars logo"
              width={40}
              height={40}
              className="rounded-full"
            />
            <span className="text-white font-bold text-lg hidden sm:block">Speedy Scholars</span>
          </Link>
          <div className="flex items-center gap-4">
            <Link href="/" className="text-amber-200 hover:text-white text-sm transition-colors">
              Home
            </Link>
            <Link href="/blog" className="text-amber-200 hover:text-white text-sm transition-colors">
              Blog
            </Link>
            <Link href="/about" className="text-amber-200 hover:text-white text-sm transition-colors">
              About
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

      {/* Hero */}
      <header
        style={{
          background: "linear-gradient(135deg, #5A4830 0%, #8B6F47 50%, #6B5335 100%)",
        }}
        className="py-20 px-4"
      >
        <div className="max-w-4xl mx-auto text-center">
          <nav aria-label="Breadcrumb" className="mb-6">
            <ol className="flex justify-center items-center gap-2 text-amber-300 text-sm">
              <li>
                <Link href="/" className="hover:text-white transition-colors">
                  Home
                </Link>
              </li>
              <li aria-hidden="true" className="text-amber-600">/</li>
              <li className="text-amber-100" aria-current="page">
                Resources
              </li>
            </ol>
          </nav>
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-6">
            Free Resources for Parents
          </h1>
          <p className="text-xl text-amber-200 max-w-2xl mx-auto">
            Practical, expert-written guides to help you support your child&apos;s abacus and mental
            math journey at home.
          </p>
        </div>
      </header>

      {/* Quick Navigation */}
      <nav
        className="py-6 px-4 border-b border-stone-200 bg-white sticky top-16 z-40"
        aria-label="Section navigation"
      >
        <div className="max-w-4xl mx-auto flex flex-wrap gap-4 justify-center">
          <a
            href="#mental-math-tricks"
            className="text-sm font-semibold px-4 py-2 rounded-full border border-[#8B6F47] text-[#8B6F47] hover:bg-[#8B6F47] hover:text-white transition-colors"
          >
            10 Mental Math Tricks
          </a>
          <a
            href="#abacus-guide"
            className="text-sm font-semibold px-4 py-2 rounded-full border border-[#8B6F47] text-[#8B6F47] hover:bg-[#8B6F47] hover:text-white transition-colors"
          >
            Abacus Buying Guide
          </a>
          <a
            href="#practice-tips"
            className="text-sm font-semibold px-4 py-2 rounded-full border border-[#8B6F47] text-[#8B6F47] hover:bg-[#8B6F47] hover:text-white transition-colors"
          >
            Practice Tips
          </a>
        </div>
      </nav>

      {/* Section 1: Mental Math Tricks */}
      <section id="mental-math-tricks" className="py-20 px-4" aria-label="10 mental math tricks">
        <div className="max-w-5xl mx-auto">
          <div className="text-center mb-14">
            <h2 className="text-4xl font-bold mb-4" style={{ color: "#5A4830" }}>
              10 Mental Math Tricks for Kids
            </h2>
            <p className="text-stone-600 text-lg max-w-2xl mx-auto">
              Practical techniques you can teach at home. These are the building blocks that abacus
              training makes automatic — start introducing them today.
            </p>
          </div>
          <div className="space-y-6">
            {mentalMathTricks.map((trick) => (
              <article
                key={trick.number}
                className="flex gap-6 p-6 rounded-2xl"
                style={{ backgroundColor: "#FFF8F0", border: "1px solid #D4B896" }}
              >
                <div
                  className="w-12 h-12 rounded-full flex items-center justify-center text-white font-bold text-xl flex-shrink-0"
                  style={{ backgroundColor: "#8B6F47" }}
                  aria-hidden="true"
                >
                  {trick.number}
                </div>
                <div>
                  <h3 className="text-xl font-bold mb-2" style={{ color: "#5A4830" }}>
                    {trick.title}
                  </h3>
                  <p className="text-stone-600 mb-3 leading-relaxed">{trick.description}</p>
                  <div
                    className="inline-block px-4 py-2 rounded-lg text-sm font-mono"
                    style={{ backgroundColor: "#F5EDE3", color: "#6B5335" }}
                  >
                    <strong>Example:</strong> {trick.example}
                  </div>
                </div>
              </article>
            ))}
          </div>
          <div className="mt-10 p-6 rounded-2xl text-center" style={{ backgroundColor: "#F5EDE3" }}>
            <p className="text-stone-700 mb-4">
              Want your child to master these techniques automatically through structured abacus
              training?
            </p>
            <Link
              href="/blog/mental-math-tips-for-kids"
              className="font-semibold underline"
              style={{ color: "#8B6F47" }}
            >
              Read our full guide: 7 Mental Math Tips Every Parent Should Know &rarr;
            </Link>
          </div>
        </div>
      </section>

      {/* Section 2: Abacus Buying Guide */}
      <section
        id="abacus-guide"
        className="py-20 px-4"
        style={{ backgroundColor: "#F5EDE3" }}
        aria-label="How to choose the right abacus"
      >
        <div className="max-w-5xl mx-auto">
          <div className="text-center mb-14">
            <h2 className="text-4xl font-bold mb-4" style={{ color: "#5A4830" }}>
              How to Choose the Right Abacus
            </h2>
            <p className="text-stone-600 text-lg max-w-2xl mx-auto">
              Not all abacuses are created equal. Here is everything you need to know before buying
              one for your child.
            </p>
          </div>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {abacusGuide.map((item) => (
              <article
                key={item.title}
                className="bg-white p-6 rounded-2xl shadow-sm border border-stone-200"
              >
                <h3 className="font-bold text-lg mb-3" style={{ color: "#5A4830" }}>
                  {item.title}
                </h3>
                <p className="text-stone-600 text-sm leading-relaxed mb-4">{item.description}</p>
                <div
                  className="px-3 py-2 rounded-lg text-sm font-semibold"
                  style={{ backgroundColor: "#F5EDE3", color: "#6B5335" }}
                >
                  ✓ {item.recommendation}
                </div>
              </article>
            ))}
          </div>
          <div className="mt-10 bg-white p-8 rounded-2xl shadow-sm border border-stone-200">
            <h3 className="text-xl font-bold mb-4" style={{ color: "#5A4830" }}>
              Do You Need to Buy an Abacus Before Starting?
            </h3>
            <p className="text-stone-700 leading-relaxed mb-4">
              <strong>No.</strong> During your free demo class, we will guide you on exactly what to
              purchase based on your child&apos;s age and level. We recommend waiting until after the
              first class so you buy exactly the right tool — nothing more, nothing less.
            </p>
            <Link
              href="/#pricing"
              className="inline-block font-bold px-6 py-3 rounded-full text-white transition-colors"
              style={{ backgroundColor: "#8B6F47" }}
              aria-label="Book your free demo class before buying an abacus"
            >
              Book Your Free Demo First
            </Link>
          </div>
        </div>
      </section>

      {/* Section 3: Practice Tips */}
      <section id="practice-tips" className="py-20 px-4" aria-label="Practice tips for parents">
        <div className="max-w-5xl mx-auto">
          <div className="text-center mb-14">
            <h2 className="text-4xl font-bold mb-4" style={{ color: "#5A4830" }}>
              Practice Tips for Parents
            </h2>
            <p className="text-stone-600 text-lg max-w-2xl mx-auto">
              How to support your child&apos;s abacus learning between classes — the small habits
              that make the biggest difference.
            </p>
          </div>
          <div className="grid md:grid-cols-2 gap-6">
            {practiceTips.map((tip) => (
              <article
                key={tip.title}
                className="p-6 rounded-2xl shadow-sm border"
                style={{ backgroundColor: "#FFF8F0", borderColor: "#D4B896" }}
              >
                <h3 className="font-bold text-lg mb-3" style={{ color: "#5A4830" }}>
                  {tip.title}
                </h3>
                <p className="text-stone-600 leading-relaxed">{tip.description}</p>
              </article>
            ))}
          </div>
        </div>
      </section>

      {/* More Resources */}
      <section
        className="py-16 px-4"
        style={{ backgroundColor: "#F5EDE3" }}
        aria-label="More learning resources"
      >
        <div className="max-w-5xl mx-auto">
          <h2 className="text-2xl font-bold mb-8 text-center" style={{ color: "#5A4830" }}>
            Continue Learning
          </h2>
          <div className="grid md:grid-cols-3 gap-6">
            {[
              {
                title: "10 Amazing Benefits of Abacus Training",
                href: "/blog/benefits-of-abacus-training",
                desc: "Discover the cognitive and academic benefits of abacus training backed by research.",
              },
              {
                title: "What Age Should Kids Start Abacus?",
                href: "/blog/best-age-to-start-abacus",
                desc: "An age-by-age guide to help you decide when your child is ready to begin.",
              },
              {
                title: "How Abacus Improves Concentration",
                href: "/blog/abacus-improves-concentration",
                desc: "Learn the neuroscience behind how abacus training builds focus and attention.",
              },
            ].map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="bg-white p-6 rounded-2xl shadow-sm border border-stone-200 hover:shadow-md transition-shadow block"
                aria-label={`Read article: ${item.title}`}
              >
                <h3 className="font-bold mb-2" style={{ color: "#5A4830" }}>
                  {item.title}
                </h3>
                <p className="text-stone-600 text-sm leading-relaxed">{item.desc}</p>
                <p className="text-sm font-semibold mt-3" style={{ color: "#8B6F47" }}>
                  Read article &rarr;
                </p>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section
        style={{ backgroundColor: "#8B6F47" }}
        className="py-20 px-4 text-center"
        aria-label="Book a free demo class"
      >
        <div className="max-w-3xl mx-auto">
          <h2 className="text-4xl font-bold text-white mb-6">
            Want Personalised Guidance?
          </h2>
          <p className="text-amber-200 text-xl mb-10">
            Every child is different. Book a FREE 45-minute demo class and let our expert instructor
            Nidhi Khariwal assess your child&apos;s individual needs and create a personalised
            learning plan.
          </p>
          <Link
            href="/#pricing"
            className="inline-block bg-amber-400 hover:bg-amber-300 text-stone-900 font-bold px-10 py-5 rounded-full text-xl transition-colors shadow-lg"
            aria-label="Book your free demo class at Speedy Scholars"
          >
            Book Your FREE Demo Class
          </Link>
        </div>
      </section>

      {/* Footer */}
      <footer style={{ backgroundColor: "#5A4830" }} className="py-8 px-4" aria-label="Footer">
        <div className="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-center gap-4">
          <div className="text-amber-200 text-sm">
            &copy; 2026 Speedy Scholars. All rights reserved.
          </div>
          <nav aria-label="Footer navigation" className="flex flex-wrap gap-6 text-sm">
            <Link href="/" className="text-amber-300 hover:text-white transition-colors">
              Home
            </Link>
            <Link href="/blog" className="text-amber-300 hover:text-white transition-colors">
              Blog
            </Link>
            <Link href="/about" className="text-amber-300 hover:text-white transition-colors">
              About
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
      </footer>
    </main>
  );
}
