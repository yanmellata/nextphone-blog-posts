# NextPhone Technical SEO Audit

**Date:** December 20, 2025
**Site:** getnextphone.com
**Content Inventory:** 120 blog posts + 100+ industry pages

---

## Executive Summary

NextPhone has **solid technical SEO fundamentals** in place, but is missing **critical schema markup opportunities** that could significantly boost search visibility and rich snippet eligibility. The site has proper Article, Organization, and SoftwareApplication schema, but is missing FAQ schema across all 120 blog posts.

**Key Finding:** Implementing FAQ schema on all blog posts could unlock rich snippet opportunities for 100+ pages.

---

## Audit Results by Category

### ✅ What's Working Well

1. **Schema Markup (Partial)**
   - ✅ Article schema implemented on all blog posts (author, date, word count)
   - ✅ SoftwareApplication schema on homepage (4.9 rating, pricing)
   - ✅ Organization schema (Pure Labs Inc contact info)
   - ✅ BreadcrumbList schema for navigation

2. **Metadata**
   - ✅ Title tags present and keyword-optimized
   - ✅ Meta descriptions present with CTAs
   - ✅ H1 tags align with title tags
   - ✅ Open Graph and Twitter Card tags implemented
   - ✅ Canonical tags properly set

3. **Site Architecture**
   - ✅ Clean URL structure (/blog/[slug], /industries/[industry])
   - ✅ Sitemap exists and well-structured (200+ URLs)
   - ✅ Robots.txt properly configured (blocks admin/private areas)
   - ✅ Internal linking in header/footer
   - ✅ Blog posts interlink to related content

4. **Crawlability**
   - ✅ All public pages crawlable
   - ✅ Sitemap referenced in robots.txt
   - ✅ Crawl delay set to 1 second

---

## ❌ Critical Issues (High Impact)

### 1. **Missing FAQ Schema on ALL Blog Posts** 🔴 CRITICAL

**Issue:** All 120 blog posts have FAQ sections but NO FAQ schema markup (schema.org/FAQPage).

**Impact:**
- Missing rich snippet opportunities in Google search results
- Missing GEO/AEO citation opportunities (LLMs love FAQ schema)
- Competitors with FAQ schema will outrank you in SERP features

**Example:**
- Blog post "AI Receptionist: Complete 2025 Guide" has 7 FAQ questions
- Blog post "What Is an AI Receptionist?" has 9 FAQ questions
- **NONE have FAQ schema**

**Fix:**
Add FAQPage schema to every blog post with an FAQ section. Example:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How much does an AI receptionist cost?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "AI receptionists typically cost $99-$299 per month..."
    }
  }]
}
```

**Estimated Impact:** 🔥🔥🔥 HIGH - Could unlock rich snippets for 100+ pages

**Effort:** Medium (can be automated with script)

---

### 2. **No llms.txt File** 🟡 MEDIUM PRIORITY

**Issue:** No llms.txt file exists at getnextphone.com/llms.txt (returns 404)

**Impact:**
- Missing opportunity to guide LLM crawlers on what content to prioritize
- GEO/AEO best practice recommended in ai_seo_bookface.md

**Fix:**
Create llms.txt file specifying what content LLMs should/shouldn't ingest.

**Estimated Impact:** 🔥 MEDIUM - Marginal but free and takes 5 minutes

**Effort:** Very Low

---

### 3. **Title Tag Length Issues** 🟡 MEDIUM PRIORITY

**Issue:** Some title tags exceed 60 characters and get truncated in SERPs

**Examples:**
- Homepage: "NextPhone - AI Phone Answering for Service Businesses | Book More Jobs 24/7" (too long)
- Blog: "AI Receptionist: The Complete 2025 Guide for Small Busine... | NextPhone" (truncated)

**Impact:**
- Truncated titles in search results look unprofessional
- May reduce click-through rates

**Fix:**
Optimize title tags to 50-60 characters max. Use template like:
- `[Primary Keyword]: [Value Prop] | NextPhone`
- Example: "AI Receptionist 2025 Guide | NextPhone"

**Estimated Impact:** 🔥 LOW-MEDIUM - Improves CTR marginally

**Effort:** Medium (need to update 120+ pages)

---

## ⚠️ Missing Data (Cannot Assess)

### 4. **Page Speed**

**Status:** Not tested (requires tools)

**Action Required:**
Run Google PageSpeed Insights on:
- Homepage: getnextphone.com
- Blog post: getnextphone.com/blog/ai-receptionist
- Industry page: getnextphone.com/ai-receptionist-for-plumbers

**Target:**
- Mobile: 90+ score
- Desktop: 95+ score
- Core Web Vitals: All green

**Tool:** https://pagespeed.web.dev/

---

### 5. **Google Search Console Indexing Status**

**Status:** Not checked

**Action Required:**
Check Google Search Console for:
- How many pages are indexed vs submitted (target: 95%+ indexed)
- Any crawl errors or indexing issues
- Mobile usability issues
- Core Web Vitals status

**Tool:** https://search.google.com/search-console

---

### 6. **Duplicate Meta Descriptions**

**Status:** Not fully audited

**Action Required:**
Use Screaming Frog or Ahrefs Site Audit to check for:
- Duplicate meta descriptions across 120 blog posts
- Missing meta descriptions
- Meta descriptions exceeding 155 characters

---

## 📊 Priority Action Plan

### **TIER 1: Critical (Do First)** 🔴

| Task | Impact | Effort | Est. Time | Priority |
|------|--------|--------|-----------|----------|
| Add FAQ schema to all 120 blog posts | 🔥🔥🔥 | Medium | 4-8 hours | #1 |
| Run PageSpeed Insights on 5 key pages | 🔥🔥 | Low | 30 mins | #2 |
| Check Google Search Console for indexing issues | 🔥🔥 | Low | 15 mins | #3 |

**Rationale:** FAQ schema is the biggest quick win. It's missing on ALL blog posts and could unlock rich snippets for 100+ pages.

---

### **TIER 2: Important (Do Second)** 🟡

| Task | Impact | Effort | Est. Time | Priority |
|------|--------|--------|-----------|----------|
| Create llms.txt file | 🔥 | Very Low | 5 mins | #4 |
| Optimize title tags (120+ pages) | 🔥 | Medium | 3-5 hours | #5 |
| Audit duplicate meta descriptions | 🔥 | Low | 1 hour | #6 |

---

### **TIER 3: Nice-to-Have (Do Later)** 🟢

| Task | Impact | Effort | Est. Time | Priority |
|------|--------|--------|-----------|----------|
| Add Review schema to homepage | 🔥 | Low | 30 mins | #7 |
| Add HowTo schema to tutorial blog posts | 🔥 | Medium | 2-3 hours | #8 |
| Optimize internal linking structure | 🔥 | High | 8-10 hours | #9 |

---

## 🎯 Recommended Immediate Actions (Next 2 Weeks)

### Week 1: Schema & Indexing
1. **Add FAQ schema to all blog posts** (Priority #1)
   - Automate with a script (use LLM to extract Q&A from each post)
   - Add FAQPage schema to each blog post's frontmatter/head
   - Redeploy site
   - Resubmit sitemap to Google Search Console

2. **Check page speed and indexing** (Priority #2-3)
   - Run PageSpeed Insights on 5 key pages
   - Check Google Search Console for indexing issues
   - Document any critical issues found

### Week 2: Optimization
3. **Create llms.txt** (Priority #4)
4. **Optimize title tags** (Priority #5)
   - Start with top 20 highest-traffic pages
   - Use template: `[Primary Keyword]: [Value Prop] | NextPhone`

---

## 📈 Expected Impact

If you implement TIER 1 (FAQ schema + page speed + indexing check):

**Best Case:**
- 10-20% of blog posts gain FAQ rich snippets in Google
- Improved GEO/AEO citations (LLMs love FAQ schema)
- Better crawlability and indexing

**Conservative Case:**
- 5-10% of blog posts gain rich snippets
- Marginal improvement in CTR from SERP features
- Better structured data for future algorithm updates

**Effort Required:** ~6-10 hours total

---

## 🛠️ Technical Implementation Notes

### FAQ Schema Implementation Options

**Option A: Manual (Not Recommended)**
- Manually add FAQ schema to each blog post
- Time: ~5 mins per post × 120 posts = 10 hours

**Option B: Automated Script (Recommended)**
- Write a script to:
  1. Read each blog post MDX file
  2. Extract FAQ section (look for "Frequently Asked Questions" H2)
  3. Parse Q&A pairs
  4. Generate FAQ schema JSON-LD
  5. Add to frontmatter or inject into page head
- Time: ~2-3 hours to build script + 1 hour to run and verify

**Option C: Next.js Component (Best Long-Term)**
- Create a reusable FAQ component that automatically generates schema
- Add to blog post template
- Ensures all future posts have FAQ schema
- Time: ~3-4 hours to build + implement

---

## 📝 Next Steps

1. **Review this audit** with your team
2. **Decide on FAQ schema implementation approach** (Option B or C recommended)
3. **Check Page Speed and Google Search Console** (15 mins)
4. **Execute TIER 1 priorities** this week

---

## 🔗 Resources

- **Schema.org FAQPage:** https://schema.org/FAQPage
- **Google Rich Results Test:** https://search.google.com/test/rich-results
- **PageSpeed Insights:** https://pagespeed.web.dev/
- **Google Search Console:** https://search.google.com/search-console
- **Reference Guide:** `/docs/SEO/ai_seo_bookface.md`

---

## Appendix: Sample Pages Audited

1. **Homepage:** getnextphone.com
2. **Blog Post 1:** getnextphone.com/blog/ai-receptionist
3. **Blog Post 2:** getnextphone.com/blog/what-is-ai-receptionist
4. **Blog Post 3:** getnextphone.com/blog/ai-customer-service
5. **Sitemap:** getnextphone.com/sitemap.xml
6. **Robots.txt:** getnextphone.com/robots.txt

**Assumption:** All 120 blog posts follow the same template structure as audited samples.
