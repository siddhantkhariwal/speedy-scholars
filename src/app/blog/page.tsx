import { Metadata } from "next";
import Link from "next/link";
import Image from "next/image";
import { blogPosts } from "@/lib/blog";

export const metadata: Metadata = {
  title: "Abacus & Mental Math Blog | Expert Tips for Parents | Speedy Scholars",
  description:
    "Explore expert articles on abacus training, mental math tips, brain development, and how to support your child's mathematical journey. Written by award-winning educator Nidhi Khariwal.",
  keywords: [
    "abacus blog",
    "mental math tips",
    "abacus benefits",
    "kids math blog",
    "abacus education",
  ],
  openGraph: {
    title: "Abacus & Mental Math Blog | Speedy Scholars",
    description:
      "Expert articles on abacus training and mental math for children. Practical tips for parents from 20+ years of teaching experience.",
    url: "https://www.speedyscholars.com/blog",
    siteName: "Speedy Scholars",
    images: [
      {
        url: "https://www.speedyscholars.com/images/og-image.jpg",
        width: 1200,
        height: 630,
        alt: "Speedy Scholars Abacus Blog",
      },
    ],
    type: "website",
  },
  alternates: {
    canonical: "https://www.speedyscholars.com/blog",
  },
};

function formatDate(dateStr: string): string {
  const date = new Date(dateStr);
  return date.toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}

export default function BlogPage() {
  const featuredPost = blogPosts[0];
  const remainingPosts = blogPosts.slice(1);

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
              {
                "@type": "ListItem",
                position: 1,
                name: "Home",
                item: "https://www.speedyscholars.com",
              },
              {
                "@type": "ListItem",
                position: 2,
                name: "Blog",
                item: "https://www.speedyscholars.com/blog",
              },
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
          <Link
            href="/"
            className="flex items-center gap-2"
            aria-label="Speedy Scholars home page"
          >
            <Image
              src="/images/logo3_transparent.png"
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
            <Link
              href="/about"
              className="text-amber-200 hover:text-white text-sm transition-colors"
            >
              About
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

      {/* Hero */}
      <header style={{ backgroundColor: "#5A4830" }} className="py-16 px-4">
        <div className="max-w-4xl mx-auto text-center">
          <nav aria-label="Breadcrumb" className="mb-6">
            <ol className="flex justify-center items-center gap-2 text-amber-300 text-sm">
              <li>
                <Link href="/" className="hover:text-white transition-colors">
                  Home
                </Link>
              </li>
              <li aria-hidden="true" className="text-amber-600">
                /
              </li>
              <li className="text-amber-100" aria-current="page">
                Blog
              </li>
            </ol>
          </nav>
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-4">
            Abacus &amp; Mental Math Blog
          </h1>
          <p className="text-xl text-amber-200 max-w-2xl mx-auto">
            Expert insights on abacus training, mental math, and raising confident young
            mathematicians. Written by award-winning educator Nidhi Khariwal.
          </p>
        </div>
      </header>

      {/* Featured Post */}
      <section className="max-w-6xl mx-auto px-4 py-12" aria-label="Featured article">
        <Link
          href={`/blog/${featuredPost.slug}`}
          className="group block bg-white rounded-2xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300 border border-stone-200"
          aria-label={`Read featured article: ${featuredPost.title}`}
        >
          <div className="md:flex">
            <div className="md:w-2/5 relative h-64 md:h-auto">
              <Image
                src={featuredPost.coverImage}
                alt={`Illustration for article: ${featuredPost.title}`}
                fill
                className="object-cover"
                priority
              />
              <div
                className="absolute top-4 left-4 px-3 py-1 rounded-full text-xs font-semibold text-white"
                style={{ backgroundColor: "#C9A86C" }}
              >
                Featured
              </div>
            </div>
            <div className="md:w-3/5 p-8 flex flex-col justify-center">
              <div className="flex flex-wrap gap-2 mb-3">
                {featuredPost.tags.slice(0, 2).map((tag) => (
                  <span
                    key={tag}
                    className="text-xs px-2 py-1 rounded-full"
                    style={{ backgroundColor: "#F5EDE3", color: "#8B6F47" }}
                  >
                    {tag}
                  </span>
                ))}
              </div>
              <h2
                className="text-2xl md:text-3xl font-bold mb-3 group-hover:underline"
                style={{ color: "#5A4830" }}
              >
                {featuredPost.title}
              </h2>
              <p className="text-stone-600 mb-4 leading-relaxed">{featuredPost.excerpt}</p>
              <div className="flex items-center gap-4 text-sm text-stone-500">
                <span>{featuredPost.author}</span>
                <span aria-hidden="true">·</span>
                <time dateTime={featuredPost.date}>{formatDate(featuredPost.date)}</time>
                <span aria-hidden="true">·</span>
                <span>{featuredPost.readTime}</span>
              </div>
            </div>
          </div>
        </Link>
      </section>

      {/* All Posts Grid */}
      <section className="max-w-6xl mx-auto px-4 pb-16" aria-label="All articles">
        <h2 className="text-2xl font-bold mb-8" style={{ color: "#5A4830" }}>
          All Articles
        </h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-2 gap-8">
          {remainingPosts.map((post) => (
            <article
              key={post.slug}
              className="bg-white rounded-2xl shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300 border border-stone-200 flex flex-col"
            >
              <Link
                href={`/blog/${post.slug}`}
                aria-label={`Read article: ${post.title}`}
                className="block"
              >
                <div className="relative h-48">
                  <Image
                    src={post.coverImage}
                    alt={`Illustration for article: ${post.title}`}
                    fill
                    className="object-cover"
                  />
                </div>
              </Link>
              <div className="p-6 flex flex-col flex-1">
                <div className="flex flex-wrap gap-2 mb-3">
                  {post.tags.slice(0, 2).map((tag) => (
                    <span
                      key={tag}
                      className="text-xs px-2 py-1 rounded-full"
                      style={{ backgroundColor: "#F5EDE3", color: "#8B6F47" }}
                    >
                      {tag}
                    </span>
                  ))}
                </div>
                <h3 className="font-bold text-xl mb-2" style={{ color: "#5A4830" }}>
                  <Link
                    href={`/blog/${post.slug}`}
                    className="hover:underline"
                    aria-label={`Read: ${post.title}`}
                  >
                    {post.title}
                  </Link>
                </h3>
                <p className="text-stone-600 text-sm leading-relaxed flex-1 mb-4">
                  {post.excerpt}
                </p>
                <div className="flex items-center gap-3 text-xs text-stone-500 mt-auto">
                  <span>{post.author}</span>
                  <span aria-hidden="true">·</span>
                  <time dateTime={post.date}>{formatDate(post.date)}</time>
                  <span aria-hidden="true">·</span>
                  <span>{post.readTime}</span>
                </div>
              </div>
            </article>
          ))}
        </div>
      </section>

      {/* CTA Section */}
      <section
        style={{ backgroundColor: "#8B6F47" }}
        className="py-16 px-4"
        aria-label="Call to action"
      >
        <div className="max-w-3xl mx-auto text-center">
          <h2 className="text-3xl font-bold text-white mb-4">
            Ready to Transform Your Child&apos;s Math Skills?
          </h2>
          <p className="text-amber-200 text-lg mb-8">
            Book a FREE 45-minute demo class and experience the Speedy Scholars difference. No
            commitment required.
          </p>
          <Link
            href="/#pricing"
            className="inline-block bg-amber-400 hover:bg-amber-300 text-stone-900 font-bold px-8 py-4 rounded-full text-lg transition-colors shadow-lg"
            aria-label="Book your free demo class"
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
          <nav aria-label="Footer navigation" className="flex gap-6 text-sm">
            <Link href="/" className="text-amber-300 hover:text-white transition-colors">
              Home
            </Link>
            <Link href="/about" className="text-amber-300 hover:text-white transition-colors">
              About
            </Link>
            <Link href="/resources" className="text-amber-300 hover:text-white transition-colors">
              Resources
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
