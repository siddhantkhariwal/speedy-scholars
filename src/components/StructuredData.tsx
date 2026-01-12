// JSON-LD Structured Data for SEO
// This helps Google understand your content and show rich results

export function LocalBusinessSchema() {
  const structuredData = {
    "@context": "https://schema.org",
    "@type": "EducationalOrganization",
    name: "Speedy Scholars",
    description:
      "Online abacus classes for kids. Transform your child's math skills with expert instruction. 20+ years experience, 2000+ students worldwide.",
    url: "https://speedyscholars.com",
    logo: "https://speedyscholars.com/images/logo.png",
    image: "https://speedyscholars.com/images/og-image.jpg",
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
    aggregateRating: {
      "@type": "AggregateRating",
      ratingValue: "4.9",
      reviewCount: "150",
      bestRating: "5",
      worstRating: "1",
    },
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
      "Learn mental arithmetic and abacus techniques. Improve concentration, memory, and calculation speed. Suitable for children ages 5-14.",
    provider: {
      "@type": "Organization",
      name: "Speedy Scholars",
      url: "https://speedyscholars.com",
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
        description: "45-minute introductory session",
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
          text: "Children can start learning abacus from age 5-6. The ideal age range is 5-14 years, when the brain is most receptive to developing mental calculation skills.",
        },
      },
      {
        "@type": "Question",
        name: "How long does it take to learn abacus?",
        acceptedAnswer: {
          "@type": "Answer",
          text: "Most children see significant improvement within 3-6 months of regular practice. Complete mastery typically takes 2-3 years, depending on the level of proficiency desired.",
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
          text: "Yes! We offer a free 45-minute demo class where you can experience our teaching style and see if it's a good fit for your child. Book your free demo on our website.",
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

export function ReviewSchema() {
  const structuredData = {
    "@context": "https://schema.org",
    "@type": "Product",
    name: "Speedy Scholars Abacus Classes",
    description: "Online abacus and mental math classes for children",
    brand: {
      "@type": "Brand",
      name: "Speedy Scholars",
    },
    aggregateRating: {
      "@type": "AggregateRating",
      ratingValue: "4.9",
      reviewCount: "150",
      bestRating: "5",
      worstRating: "1",
    },
    review: [
      {
        "@type": "Review",
        author: { "@type": "Person", name: "Hanna M." },
        reviewRating: { "@type": "Rating", ratingValue: "5" },
        reviewBody:
          "Mrs. Nidhi is an excellent abacus teacher! My child's confidence in math has grown tremendously.",
      },
      {
        "@type": "Review",
        author: { "@type": "Person", name: "Tara S." },
        reviewRating: { "@type": "Rating", ratingValue: "5" },
        reviewBody:
          "The abacus classes are fantastic. My daughter improved her math skills and concentration.",
      },
      {
        "@type": "Review",
        author: { "@type": "Person", name: "Jordan H." },
        reviewRating: { "@type": "Rating", ratingValue: "5" },
        reviewBody:
          "Speedy Scholars has been a game-changer for my son. His mental calculation skills improved so much!",
      },
      {
        "@type": "Review",
        author: { "@type": "Person", name: "Joel G." },
        reviewRating: { "@type": "Rating", ratingValue: "5" },
        reviewBody:
          "Mrs. Nidhi brings out the best in every student. My son looks forward to class every week.",
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

// Combined component for the homepage
export function HomePageStructuredData() {
  return (
    <>
      <LocalBusinessSchema />
      <CourseSchema />
      <FAQSchema />
      <ReviewSchema />
    </>
  );
}
