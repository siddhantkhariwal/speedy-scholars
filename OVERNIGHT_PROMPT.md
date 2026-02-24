# Overnight Mega-Prompt for Claude

Copy everything below the line and paste it into the terminal after running `claude --dangerously-skip-permissions`:

---

You are working on the Speedy Scholars website at /Users/macbook/Desktop/speedy-scholars. This is a Next.js 14 website for an online abacus teaching business. The site is LIVE at https://www.speedyscholars.com.

## Brand Guidelines:
- Primary: #8B6F47 (Warm Brown), Dark: #6B5335, Darker: #5A4830
- Gold: #C9A86C, #D4B896, Cream: #F5EDE3
- Font: Arial/Geist Sans
- Style: Professional, warm, trustworthy, educational

## Your Tasks (Complete ALL of these in order):

### TASK 1: Create Blog Infrastructure
Create a complete blog system:
- Create `src/lib/blog.ts` with blog post data (title, slug, date, excerpt, content, author, readTime, tags, metaDescription)
- Create `src/app/blog/page.tsx` - Blog listing page with cards showing all posts, matching the brown/gold brand palette
- Create `src/app/blog/[slug]/page.tsx` - Individual blog post page with proper layout, author info, related posts, and CTA
- Add generateStaticParams and generateMetadata for SEO
- Match the premium design style of the home page (page.tsx)

### TASK 2: Write 5 SEO Blog Articles
In `src/lib/blog.ts`, create full content for these 5 articles (1000-1500 words each, real educational content):

1. **"10 Amazing Benefits of Abacus Training for Children"** - slug: benefits-of-abacus-training
   - Cover cognitive, academic, and life skill benefits
   - Include statistics and research references
   - Keywords: abacus benefits, abacus for kids, mental math benefits

2. **"What Age Should Kids Start Learning Abacus? A Complete Guide"** - slug: best-age-to-start-abacus
   - Age-by-age breakdown (4-14)
   - Signs of readiness
   - Keywords: abacus age, when to start abacus, abacus for beginners

3. **"Mental Math Tips: 7 Easy Tricks Every Parent Should Know"** - slug: mental-math-tips-for-kids
   - Practical math tricks with examples
   - How abacus helps with mental math
   - Keywords: mental math tricks, math tips for kids, mental arithmetic

4. **"How Abacus Improves Concentration and Focus in Children"** - slug: abacus-improves-concentration
   - Science behind abacus and brain development
   - Attention span improvement
   - Keywords: abacus concentration, focus improvement, brain development

5. **"Abacus vs Calculator: Why Traditional Methods Still Matter"** - slug: abacus-vs-calculator
   - Comparison of both approaches
   - Why abacus builds understanding
   - Keywords: abacus vs calculator, traditional math, mental calculation

Each article MUST include:
- SEO meta title and description
- Proper heading hierarchy (H1 > H2 > H3)
- Internal links to other blog posts and main pages
- CTA section at the end ("Book Your Free Demo Class")
- Author: Nidhi Khariwal
- Read time estimate

### TASK 3: Full SEO Audit & Fixes
- Add unique `generateMetadata` exports to `about/page.tsx`, `contact/page.tsx`
- Fix heading hierarchy on ALL pages (ensure single H1 per page)
- Add ArticleSchema structured data in blog post pages
- Add BreadcrumbSchema to inner pages
- Ensure all images have descriptive alt text
- Add internal links between pages (blog posts link to home pricing, about page, etc.)
- Update `src/components/StructuredData.tsx` to add BlogPosting schema

### TASK 4: Redesign About Page
Completely redesign `src/app/about/page.tsx` to:
- Use the brown/gold color palette (#8B6F47, #6B5335, #D4B896) instead of green (#556B2F)
- Add a proper founder story section with timeline (20+ years of milestones)
- Add teaching methodology section
- Add "Why Choose Us" section with 4-6 differentiators
- Add achievements/awards section
- Add CTA for booking demo class (opens Calendly or links to home)
- Add link back to home page
- Match the premium design quality of the home page
- Make it "use client" with smooth animations

### TASK 5: Create Resources Page
Create `src/app/resources/page.tsx`:
- "Free Resources" landing page
- Section 1: "10 Mental Math Tricks for Kids" - write actual content (tips parents can use)
- Section 2: "How to Choose the Right Abacus" - buying guide
- Section 3: "Practice Tips for Parents" - how to support abacus learning at home
- CTA: "Want personalized guidance? Book a FREE Demo Class"
- Match brand design

### TASK 6: Update Navigation & Footer
In `src/app/page.tsx`:
- Add "Blog" and "Resources" to the navigation menu
- Update footer to include links to Blog, Resources, Privacy, Terms
- Add structured breadcrumb-style navigation

### TASK 7: Update Sitemap
In `src/app/sitemap.ts`:
- Add /blog route (priority 0.9, weekly)
- Add /resources route (priority 0.7, monthly)
- Add all 5 blog post routes (priority 0.8, monthly)

### TASK 8: Performance & Accessibility
- Review all pages for proper aria-labels on interactive elements
- Ensure all buttons and links have descriptive text
- Add proper semantic HTML (nav, main, article, section, aside)
- Check for proper color contrast

### TASK 9: Generate Audit Report
Create `WEBSITE_AUDIT_REPORT.md` documenting:
- All changes made during this session
- Current SEO status (what's good, what needs improvement)
- Performance recommendations
- Content strategy recommendations
- List of all pages and their SEO status
- Remaining tasks from GROWTH_PLAN.md
- Recommendations for next steps

### TASK 10: Build, Commit & Push
1. Run `npm run build` - fix ALL errors before proceeding
2. If there are ESLint errors, fix them (escape quotes with &apos; and &quot;)
3. Run build again until it succeeds
4. Commit ALL changes with a detailed commit message
5. Push to GitHub (which auto-deploys to Vercel)

## IMPORTANT RULES:
- Use "use client" directive on pages with client-side interactivity
- Escape all quotes in JSX text: use &apos; for ' and &quot; for "
- DO NOT use emojis in the actual website pages (only in documentation)
- Match the EXACT color palette from the home page
- Every page must have proper metadata for SEO
- Run `npm run build` after each major task to catch errors early
- If a build fails, FIX the errors before moving on
- Commit after each major task so progress is saved
- Do NOT modify existing working functionality - only add/enhance

## START NOW. Begin with Task 1 and work through all 10 tasks sequentially. Build and test frequently. Commit after each major milestone.
