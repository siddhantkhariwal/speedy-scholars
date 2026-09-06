// JSON-LD Structured Data for SEO
// This helps Google understand your content and show rich results

export function LocalBusinessSchema() {
  const structuredData = {
    "@context": "https://schema.org",
    "@type": "EducationalOrganization",
    name: "Speedy Scholars",
    description:
      "Online abacus classes for kids. Transform your child's math skills with expert instruction. 20+ years experience, 2000+ students worldwide.",
    url: "https://www.speedyscholars.com",
    logo: "https://www.speedyscholars.com/images/logo-owl.png",
    image: "https://www.speedyscholars.com/images/og-image.jpg",
    telephone: "+919352646671",
    email: "nidhikhariwal2012@gmail.com",
    founder: {
      "@type": "Person",
      name: "Nidhi Khariwal",
      jobTitle: "Founder & Lead Instructor",
      description: "20+ years of experience teaching abacus and mental arithmetic",
    },
    address: {
      "@type": "PostalAddress",
      addressCountry: "IN",
      addressLocality: "Online Classes Worldwide",
    },
    areaServed: [
      { "@type": "Country", name: "United States" },
      { "@type": "Country", name: "United Kingdom" },
      { "@type": "Country", name: "Australia" },
      { "@type": "Country", name: "India" },
      { "@type": "Country", name: "Canada" },
      { "@type": "Country", name: "New Zealand" },
    ],
    priceRange: "$$",
    openingHours: "Mo-Sa 09:00-19:00",
    sameAs: [
      // Add social media URLs when created
      // "https://facebook.com/speedyscholars",
      // "https://instagram.com/speedyscholars",
      // "https://youtube.com/@speedyscholars",
    ],
  };

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(structuredData) }}
    />
  );
}

export function CourseSchema() {
  const structuredData = {
    "@context": "https://schema.org",
    "@type": "Course",
    name: "Abacus Mental Math Course",
    description:
      "Learn mental arithmetic and abacus techniques. Improve concentration, memory, and calculation speed. Suitable for children aged 4 to 14.",
    provider: {
      "@type": "Organization",
      name: "Speedy Scholars",
      url: "https://www.speedyscholars.com",
    },
    instructor: {
      "@type": "Person",
      name: "Nidhi Khariwal",
      description: "Award-winning educator with 20+ years of experience",
    },
    courseMode: "Online",
    educationalLevel: "Beginner to Advanced",
    inLanguage: ["en", "hi"],
    offers: [
      {
        "@type": "Offer",
        name: "Free Demo Class",
        price: "0",
        priceCurrency: "INR",
        availability: "https://schema.org/InStock",
        description: "30-minute introductory session",
      },
      {
        "@type": "Offer",
        name: "Pay-As-You-Go",
        price: "1600",
        priceCurrency: "INR",
        availability: "https://schema.org/InStock",
        description: "Per class payment option",
      },
      {
        "@type": "Offer",
        name: "10-Class Pack",
        price: "12500",
        priceCurrency: "INR",
        availability: "https://schema.org/InStock",
        description: "Most popular - includes worksheets and progress tracking",
      },
    ],
    hasCourseInstance: {
      "@type": "CourseInstance",
      courseMode: "Online",
      instructor: {
        "@type": "Person",
        name: "Nidhi Khariwal",
      },
    },
  };

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(structuredData) }}
    />
  );
}

export function FAQSchema() {
  const structuredData = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: [
      {
        "@type": "Question",
        name: "What age is best to start learning abacus?",
        acceptedAnswer: {
          "@type": "Answer",
          text: "Children can start from around age 4, and the strongest window is roughly 7 to 10 years old. Older children still benefit, they simply move through the early levels faster.",
        },
      },
      {
        "@type": "Question",
        name: "How long does it take to learn abacus?",
        acceptedAnswer: {
          "@type": "Answer",
          text: "Most parents notice better concentration and faster basic calculation within 8 to 12 weeks of consistent classes and short daily practice. Full mental calculation usually develops over one to two years.",
        },
      },
      {
        "@type": "Question",
        name: "Are online abacus classes as effective as in-person?",
        acceptedAnswer: {
          "@type": "Answer",
          text: "Yes! Online abacus classes can be equally effective with proper instruction. Our live, interactive sessions ensure personalized attention and real-time feedback, just like in-person classes.",
        },
      },
      {
        "@type": "Question",
        name: "What are the benefits of learning abacus?",
        acceptedAnswer: {
          "@type": "Answer",
          text: "Abacus training improves mental calculation speed, concentration, memory, visualization skills, and overall academic performance. It also builds confidence and reduces math anxiety.",
        },
      },
      {
        "@type": "Question",
        name: "Do you offer a free trial class?",
        acceptedAnswer: {
          "@type": "Answer",
          text: "Yes! We offer a free 30-minute demo class where you can experience our teaching style and see if it's a good fit for your child. Book your free demo on our website.",
        },
      },
    ],
  };

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(structuredData) }}
    />
  );
}

/**
 * Product/Review schema was removed deliberately (Sept 2026).
 *
 * Two reasons, do not re-add without addressing both:
 * 1. Policy: Google does not grant review rich results for "self-serving"
 *    reviews, meaning testimonials a business publishes about itself on its
 *    own site. It was reporting 4 invalid review items in Search Console.
 * 2. Typing: these are classes, not a Product. Course schema already covers
 *    the offering correctly.
 *
 * The testimonials still render on the homepage for human visitors. If real
 * third-party reviews are ever collected on an external platform, link to
 * that instead of marking up our own testimonials.
 */

export function HomePageStructuredData() {
  return (
    <>
      <CourseSchema />
      <FAQSchema />
    </>
  );
}

/** Safe on every page: who the organisation is. */
export function SiteWideStructuredData() {
  return <LocalBusinessSchema />;
}

/**
 * Author/instructor entity for Nidhi Khariwal. Rendered on /about, which is
 * the URL every BlogPosting's author field points at, so search and answer
 * engines can resolve the person behind the content (E-E-A-T).
 */
export function PersonSchema() {
  const structuredData = {
    "@context": "https://schema.org",
    "@type": "Person",
    "@id": "https://www.speedyscholars.com/about#nidhi-khariwal",
    name: "Nidhi Khariwal",
    url: "https://www.speedyscholars.com/about",
    jobTitle: "Founder and Lead Instructor",
    description:
      "Abacus and mental arithmetic educator with over 20 years of teaching experience. Has taught more than 2,000 students worldwide and coached 50+ competition winners.",
    knowsAbout: [
      "Abacus",
      "Mental arithmetic",
      "Mental math for children",
      "Soroban technique",
      "Early years numeracy",
    ],
    knowsLanguage: ["English", "Hindi"],
    worksFor: {
      "@type": "EducationalOrganization",
      name: "Speedy Scholars",
      url: "https://www.speedyscholars.com",
    },
  };

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(structuredData) }}
    />
  );
}

interface BlogPostingSchemaProps {
  title: string;
  description: string;
  imageUrl: string;
  datePublished: string;
  dateModified: string;
  authorName: string;
  authorTitle: string;
  slug: string;
}

export function BlogPostingSchema({
  title,
  description,
  imageUrl,
  datePublished,
  dateModified,
  authorName,
  authorTitle,
  slug,
}: BlogPostingSchemaProps) {
  const structuredData = {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    headline: title,
    description,
    image: imageUrl,
    datePublished,
    dateModified,
    author: {
      "@type": "Person",
      name: authorName,
      jobTitle: authorTitle,
      url: "https://www.speedyscholars.com/about",
    },
    publisher: {
      "@type": "Organization",
      name: "Speedy Scholars",
      logo: {
        "@type": "ImageObject",
        url: "https://www.speedyscholars.com/images/logo-owl.png",
      },
    },
    mainEntityOfPage: {
      "@type": "WebPage",
      "@id": `https://www.speedyscholars.com/blog/${slug}`,
    },
    isPartOf: {
      "@type": "Blog",
      name: "Speedy Scholars Blog",
      url: "https://www.speedyscholars.com/blog",
    },
  };

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(structuredData) }}
    />
  );
}
