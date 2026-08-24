import { MetadataRoute } from "next";
import { blogPosts } from "@/lib/blog";

/**
 * Real lastModified dates matter. Using new Date() on every entry told Google
 * that all pages changed on every deploy, which makes the signal worthless and
 * hurts recrawl prioritisation. Bump a page's date here when its content
 * actually changes.
 */
const LAST_MODIFIED: Record<string, string> = {
  "": "2026-08-12",
  "/online-abacus-classes": "2026-08-12",
  "/online-abacus-classes-cost": "2026-08-12",
  "/faq": "2026-08-12",
  "/about": "2026-08-12",
  "/contact": "2026-08-12",
  "/blog": "2026-08-12",
  "/resources": "2026-08-12",
  "/privacy": "2026-08-12",
  "/terms": "2026-08-12",
};

export default function sitemap(): MetadataRoute.Sitemap {
  const baseUrl =
    process.env.NEXT_PUBLIC_SITE_URL || "https://www.speedyscholars.com";

  const at = (path: string) => new Date(LAST_MODIFIED[path] ?? "2026-08-12");

  const blogPostRoutes: MetadataRoute.Sitemap = blogPosts.map((post) => ({
    url: `${baseUrl}/blog/${post.slug}`,
    lastModified: new Date(post.date),
    changeFrequency: "monthly",
    priority: 0.8,
  }));

  return [
    {
      url: baseUrl,
      lastModified: at(""),
      changeFrequency: "weekly",
      priority: 1,
    },
    {
      url: `${baseUrl}/online-abacus-classes`,
      lastModified: at("/online-abacus-classes"),
      changeFrequency: "monthly",
      priority: 0.95,
    },
    {
      url: `${baseUrl}/online-abacus-classes-cost`,
      lastModified: at("/online-abacus-classes-cost"),
      changeFrequency: "monthly",
      priority: 0.9,
    },
    {
      url: `${baseUrl}/faq`,
      lastModified: at("/faq"),
      changeFrequency: "monthly",
      priority: 0.85,
    },
    {
      url: `${baseUrl}/about`,
      lastModified: at("/about"),
      changeFrequency: "monthly",
      priority: 0.8,
    },
    {
      url: `${baseUrl}/contact`,
      lastModified: at("/contact"),
      changeFrequency: "monthly",
      priority: 0.8,
    },
    {
      url: `${baseUrl}/blog`,
      lastModified: at("/blog"),
      changeFrequency: "weekly",
      priority: 0.9,
    },
    {
      url: `${baseUrl}/resources`,
      lastModified: at("/resources"),
      changeFrequency: "monthly",
      priority: 0.7,
    },
    ...blogPostRoutes,
    {
      url: `${baseUrl}/privacy`,
      lastModified: at("/privacy"),
      changeFrequency: "yearly",
      priority: 0.5,
    },
    {
      url: `${baseUrl}/terms`,
      lastModified: at("/terms"),
      changeFrequency: "yearly",
      priority: 0.5,
    },
  ];
}
