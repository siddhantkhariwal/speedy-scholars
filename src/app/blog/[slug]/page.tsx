import { Metadata } from "next";
import { notFound } from "next/navigation";
import Link from "next/link";
import Image from "next/image";
import { blogPosts, getBlogPost, getRelatedPosts, getAllSlugs } from "@/lib/blog";

interface Props {
  params: { slug: string };
}

export async function generateStaticParams() {
  return getAllSlugs().map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const post = getBlogPost(params.slug);
  if (!post) return {};

  return {
    title: post.metaTitle,
    description: post.metaDescription,
    keywords: post.tags,
    authors: [{ name: post.author }],
    openGraph: {
      title: post.metaTitle,
      description: post.metaDescription,
      url: `https://www.speedyscholars.com/blog/${post.slug}`,
      siteName: "Speedy Scholars",
      images: [
        {
          url: `https://www.speedyscholars.com${post.coverImage}`,
          width: 1200,
          height: 630,
          alt: post.title,
        },
      ],
      type: "article",
      publishedTime: post.date,
      authors: [post.author],
    },
    twitter: {
      card: "summary_large_image",
      title: post.metaTitle,
      description: post.metaDescription,
    },
    alternates: {
      canonical: `https://www.speedyscholars.com/blog/${post.slug}`,
    },
  };
}

function formatDate(dateStr: string): string {
  const date = new Date(dateStr);
  return date.toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}

// Render simple markdown-like content to HTML
function renderContent(content: string): string {
  return content
    .trim()
    .split("\n")
    .map((line) => {
      // H1
      if (line.startsWith("# ")) {
        return `<h1 class="text-3xl font-bold mt-8 mb-4" style="color:#5A4830">${line.slice(2)}</h1>`;
      }
      // H2
      if (line.startsWith("## ")) {
        return `<h2 class="text-2xl font-bold mt-10 mb-4" style="color:#6B5335">${line.slice(3)}</h2>`;
      }
      // H3
      if (line.startsWith("### ")) {
        return `<h3 class="text-xl font-semibold mt-6 mb-3" style="color:#8B6F47">${line.slice(4)}</h3>`;
      }
      // HR
      if (line.trim() === "---") {
        return `<hr class="my-8 border-stone-200" />`;
      }
      // Bullet list item
      if (line.startsWith("- ")) {
        return `<li class="ml-6 mb-2 list-disc text-stone-700">${renderInline(line.slice(2))}</li>`;
      }
      // Numbered list item
      if (/^\d+\.\s/.test(line)) {
        return `<li class="ml-6 mb-2 list-decimal text-stone-700">${renderInline(line.replace(/^\d+\.\s/, ""))}</li>`;
      }
      // Empty line
      if (line.trim() === "") {
        return "";
      }
      // Regular paragraph
      return `<p class="mb-4 text-stone-700 leading-relaxed">${renderInline(line)}</p>`;
    })
    .join("\n");
}

function renderInline(text: string): string {
  return text
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/\*(.+?)\*/g, "<em>$1</em>")
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" class="underline font-medium" style="color:#8B6F47">$1</a>');
}

export default function BlogPostPage({ params }: Props) {
  const post = getBlogPost(params.slug);
  if (!post) notFound();

  const relatedPosts = getRelatedPosts(params.slug, 3);
  const allPostSlugs = getAllSlugs();
  const currentIndex = allPostSlugs.indexOf(params.slug);
  const prevPost = currentIndex > 0 ? blogPosts[currentIndex - 1] : null;
  const nextPost = currentIndex < blogPosts.length - 1 ? blogPosts[currentIndex + 1] : null;

  const articleSchema = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: post.title,
    description: post.metaDescription,
    image: `https://www.speedyscholars.com${post.coverImage}`,
    datePublished: post.date,
    dateModified: post.date,
    author: {
      "@type": "Person",
      name: post.author,
      jobTitle: post.authorTitle,
      url: "https://www.speedyscholars.com/about",
    },
    publisher: {
      "@type": "Organization",
      name: "Speedy Scholars",
      logo: {
        "@type": "ImageObject",
        url: "https://www.speedyscholars.com/images/logo.png",
      },
    },
    mainEntityOfPage: {
      "@type": "WebPage",
      "@id": `https://www.speedyscholars.com/blog/${post.slug}`,
    },
  };

  const breadcrumbSchema = {
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
      {
        "@type": "ListItem",
        position: 3,
        name: post.title,
        item: `https://www.speedyscholars.com/blog/${post.slug}`,
      },
    ],
  };

  return (
    <main>
      {/* Structured Data */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(articleSchema) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }}
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

      {/* Hero Image */}
      <div className="relative h-64 md:h-80" aria-hidden="true">
        <Image
          src={post.coverImage}
          alt={`Cover image for: ${post.title}`}
          fill
          className="object-cover"
          priority
        />
        <div className="absolute inset-0 bg-gradient-to-b from-transparent to-black/60" />
      </div>

      {/* Article Content */}
      <div className="max-w-4xl mx-auto px-4">
        {/* Breadcrumb */}
        <nav aria-label="Breadcrumb" className="py-4">
          <ol className="flex items-center gap-2 text-sm text-stone-500">
            <li>
              <Link href="/" className="hover:text-stone-700 transition-colors">
                Home
              </Link>
            </li>
            <li aria-hidden="true">/</li>
            <li>
              <Link href="/blog" className="hover:text-stone-700 transition-colors">
                Blog
              </Link>
            </li>
            <li aria-hidden="true">/</li>
            <li className="text-stone-700 truncate max-w-xs" aria-current="page">
              {post.title}
            </li>
          </ol>
        </nav>

        {/* Article Header */}
        <header className="py-8 border-b border-stone-200">
          <div className="flex flex-wrap gap-2 mb-4">
            {post.tags.map((tag) => (
              <span
                key={tag}
                className="text-xs px-3 py-1 rounded-full"
                style={{ backgroundColor: "#F5EDE3", color: "#8B6F47" }}
              >
                {tag}
              </span>
            ))}
          </div>
          <h1 className="text-3xl md:text-4xl font-bold mb-6" style={{ color: "#5A4830" }}>
            {post.title}
          </h1>
          <div className="flex items-center gap-4">
            <Image
              src="/images/founder.jpeg"
              alt={`Portrait of ${post.author}, author`}
              width={48}
              height={48}
              className="rounded-full object-cover"
            />
            <div>
              <p className="font-semibold text-stone-800">{post.author}</p>
              <p className="text-stone-500 text-sm">{post.authorTitle}</p>
            </div>
            <div className="ml-auto text-right text-sm text-stone-500">
              <time dateTime={post.date}>{formatDate(post.date)}</time>
              <p>{post.readTime}</p>
            </div>
          </div>
        </header>

        {/* Article Body */}
        <article
          className="prose max-w-none py-10"
          aria-label="Article content"
          dangerouslySetInnerHTML={{ __html: renderContent(post.content) }}
        />

        {/* CTA Box */}
        <aside
          className="my-10 p-8 rounded-2xl text-center"
          style={{ backgroundColor: "#F5EDE3", border: "2px solid #D4B896" }}
          aria-label="Book a free demo class"
        >
          <h2 className="text-2xl font-bold mb-3" style={{ color: "#5A4830" }}>
            Book Your FREE Demo Class
          </h2>
          <p className="text-stone-600 mb-6">
            See the difference expert abacus training makes. 45 minutes, completely free, no
            commitment required.
          </p>
          <Link
            href="/#pricing"
            className="inline-block font-bold px-8 py-4 rounded-full text-lg transition-colors text-white shadow-md"
            style={{ backgroundColor: "#8B6F47" }}
            aria-label="Book your free demo class at Speedy Scholars"
          >
            Book My Free Demo Class
          </Link>
        </aside>

        {/* Prev / Next Navigation */}
        <nav aria-label="Article navigation" className="border-t border-stone-200 py-8">
          <div className="flex justify-between gap-4">
            {prevPost ? (
              <Link
                href={`/blog/${prevPost.slug}`}
                className="group flex-1 p-4 rounded-xl hover:bg-stone-50 transition-colors text-left border border-stone-200"
                aria-label={`Previous article: ${prevPost.title}`}
              >
                <p className="text-xs text-stone-500 mb-1">Previous</p>
                <p
                  className="font-semibold group-hover:underline line-clamp-2"
                  style={{ color: "#5A4830" }}
                >
                  {prevPost.title}
                </p>
              </Link>
            ) : (
              <div className="flex-1" />
            )}
            {nextPost ? (
              <Link
                href={`/blog/${nextPost.slug}`}
                className="group flex-1 p-4 rounded-xl hover:bg-stone-50 transition-colors text-right border border-stone-200"
                aria-label={`Next article: ${nextPost.title}`}
              >
                <p className="text-xs text-stone-500 mb-1">Next</p>
                <p
                  className="font-semibold group-hover:underline line-clamp-2"
                  style={{ color: "#5A4830" }}
                >
                  {nextPost.title}
                </p>
              </Link>
            ) : (
              <div className="flex-1" />
            )}
          </div>
        </nav>
      </div>

      {/* Related Posts */}
      {relatedPosts.length > 0 && (
        <section
          style={{ backgroundColor: "#F5EDE3" }}
          className="py-16 px-4"
          aria-label="Related articles"
        >
          <div className="max-w-6xl mx-auto">
            <h2 className="text-2xl font-bold mb-8 text-center" style={{ color: "#5A4830" }}>
              You May Also Like
            </h2>
            <div className="grid md:grid-cols-3 gap-6">
              {relatedPosts.map((related) => (
                <article
                  key={related.slug}
                  className="bg-white rounded-xl shadow-sm overflow-hidden hover:shadow-md transition-shadow border border-stone-200"
                >
                  <Link
                    href={`/blog/${related.slug}`}
                    aria-label={`Read related article: ${related.title}`}
                  >
                    <div className="relative h-40">
                      <Image
                        src={related.coverImage}
                        alt={`Cover for: ${related.title}`}
                        fill
                        className="object-cover"
                      />
                    </div>
                    <div className="p-4">
                      <h3
                        className="font-semibold mb-2 hover:underline line-clamp-2"
                        style={{ color: "#5A4830" }}
                      >
                        {related.title}
                      </h3>
                      <p className="text-stone-500 text-xs">{related.readTime}</p>
                    </div>
                  </Link>
                </article>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* Footer */}
      <footer style={{ backgroundColor: "#5A4830" }} className="py-8 px-4" aria-label="Footer">
        <div className="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-center gap-4">
          <div className="text-amber-200 text-sm">
            &copy; 2026 Speedy Scholars. All rights reserved.
          </div>
          <nav aria-label="Footer links" className="flex gap-6 text-sm">
            <Link href="/" className="text-amber-300 hover:text-white transition-colors">
              Home
            </Link>
            <Link href="/blog" className="text-amber-300 hover:text-white transition-colors">
              Blog
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
