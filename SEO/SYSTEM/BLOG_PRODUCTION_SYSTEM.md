# NextPhone Blog Production System

**The Complete 4-Phase Process for Creating High-Quality SEO Blog Posts**

---

## Overview

This system is designed to produce consistent, high-quality SEO blog posts that rank well and convert readers. It breaks blog creation into 4 distinct phases, each with clear deliverables and quality gates.

**Total Time Per Post:** ~7-8 hours
**Output:** Publication-ready 3,000-3,500 word blog post

---

## The 4-Phase Process

### **Phase 1: Research** (~2 hours)
**Purpose:** Understand the competitive landscape, gather data, and identify unique angles

**Input:** Keyword from SEO Master Plan (e.g., "AI customer service")

**Process:** Execute all steps in [`PHASE_1_RESEARCH_PROMPT.md`](./PHASE_1_RESEARCH_PROMPT.md)

**Output:** Complete research document with:
- Keyword intel (search intent, related questions, semantic keywords)
- Top 10 competitor analysis (structure, topics, gaps)
- User questions from forums/Reddit/Quora
- 5-10 authoritative sources to cite
- NextPhone factbase stats relevant to topic
- Unique angle and content gaps we'll fill

**Quality Gate:** Research is complete when you can answer:
- What is the search intent?
- What are competitors covering (and missing)?
- What unique angle will we take?
- What data/stats will we use?
- How will we differentiate from #1 ranking post?

---

### **Phase 2: Outline** (~1.5 hours)
**Purpose:** Create detailed blueprint for writing phase

**Input:** Approved research document from Phase 1

**Process:** Execute all steps in [`PHASE_2_OUTLINE_PROMPT.md`](./PHASE_2_OUTLINE_PROMPT.md)

**Output:** Detailed section-by-section outline with:
- 8-12 main sections (H2s) with subsections (H3s)
- Word count targets per section
- Key points, data, examples, quotes for each section
- Visual content plan (4-6 images/charts with placement)
- Internal linking plan (3-7 links with anchor text)
- External citation plan (2-4 authoritative sources)
- CTA plan (3 CTAs: soft, mid, hard)
- FAQ section (5-7 questions with answers)

**Quality Gate:** Outline is complete when:
- Every section has clear purpose and word count
- All table stakes topics are covered
- Unique differentiators are included
- Data placement is specified
- CTAs, links, and visuals are planned
- User/stakeholder approves direction

---

### **Phase 3: Writing** (~4-5 hours)
**Purpose:** Execute outline with consistent voice and quality

**Input:** Approved outline from Phase 2

**Process:** Execute all steps in [`PHASE_3_WRITING_PROMPT.md`](./PHASE_3_WRITING_PROMPT.md)

**Output:** Publication-ready blog post with:
- 3,000-3,500 words (or type-specific target)
- Conversational, non-AI voice
- Key takeaways box + strong intro
- All sections written per outline
- Data cited properly with sources
- 3-7 internal links + 2-4 external links
- 3 CTAs placed naturally
- FAQ section with schema markup
- Author bio + related articles
- Technical SEO optimized

**Quality Gate:** Post is ready when:
- All pre-publish checklist items pass
- Voice sounds natural (read-aloud test)
- No AI tell-tale phrases
- All data is cited credibly
- Links are contextual and working
- Metadata is complete
- Would you personally share this article?

---

### **Phase 4: QA Review** (~30-45 mins)
**Purpose:** Validate formatting, compliance, and publish readiness using the QA checklist

**Input:** Final draft from Phase 3 (or published MDX if already live)

**Process:** Review against the QA checklist and log status in [`PHASE_4_QA_REVIEW_TRACKER.md`](./PHASE_4_QA_REVIEW_TRACKER.md)

**Output:** Review status + notes for any fixes needed

**Quality Gate:** QA review is complete when:
- All formatting issues are resolved (tables, lists, headings)
- CTAs and links render correctly
- Any required fixes are documented in the tracker

---

## How to Use This System

### For Each New Blog Post:

**1. Select Post from SEO Master Plan**
- Choose from one of 13 keyword clusters
- Priority: Start with Cluster #2 (AI-Specific) - highest volume
- Track which posts are complete in table below

**2. Execute Phase 1 (Research)**
- Open [`PHASE_1_RESEARCH_PROMPT.md`](./PHASE_1_RESEARCH_PROMPT.md)
- Follow all 7 steps
- Create research doc using template
- Check quality gate before proceeding

**3. Review & Approve Research**
- Review unique angle
- Confirm topics to cover
- Verify data sources
- Approve or request revisions

**4. Execute Phase 2 (Outline)**
- Open [`PHASE_2_OUTLINE_PROMPT.md`](./PHASE_2_OUTLINE_PROMPT.md)
- Follow all 6 steps
- Create detailed outline
- Check quality gate before proceeding

**5. Review & Approve Outline**
- Check section structure
- Verify all topics covered
- Confirm data placement
- Approve or request revisions

**6. Execute Phase 3 (Writing)**
- Open [`PHASE_3_WRITING_PROMPT.md`](./PHASE_3_WRITING_PROMPT.md)
- Follow all 11 steps
- Write complete post
- Run through pre-publish checklist

**7. QA Review (Phase 4)**
- Run QA checklist on the final post
- Log results in [`PHASE_4_QA_REVIEW_TRACKER.md`](./PHASE_4_QA_REVIEW_TRACKER.md)

**8. Publish**
- Quality pass (read aloud)
- Technical SEO check
- Convert to Next.js/MDX format
- Publish and track in table below

---

## Blog Post Tracking

Use this table to track progress on all blog posts:

| Post # | Keyword | Cluster | Phase | Status | Notes | Date Started | Date Published |
|--------|---------|---------|-------|--------|-------|--------------|----------------|
| POST-014 | AI customer service | #2 AI-Specific | Phase 1 | In Progress | Research started | 2025-11-19 | - |
| POST-015 | AI receptionist | #2 AI-Specific | Not Started | Pending | - | - | - |
| POST-016 | AI answering service | #2 AI-Specific | Not Started | Pending | - | - | - |

*Add rows as you work through the 120+ posts from the SEO Master Plan*

---

## Success Metrics

### Per Post:
- **Quality:** Passes all pre-publish checklist items
- **SEO:** Targets primary keyword + 3-5 semantic variants naturally
- **Length:** Hits target word count (3K-3.5K for pillar, 1.8K-2.5K for feature)
- **Data:** Uses NextPhone factbase stats + 2-4 external authoritative sources
- **Voice:** Sounds conversational, not AI-generated
- **Structure:** Follows MEGA AI framework (Key Takeaways, proper H2/H3 hierarchy, FAQ, CTAs)

### Aggregate:
- **Consistency:** All posts follow same process and quality bar
- **Speed:** Average 7-8 hours per post (gets faster with practice)
- **Rankings:** Track keyword positions monthly (target top 10 within 3-6 months)
- **Conversions:** Track leads generated from organic blog traffic

---

## Key Documents Reference

### Writing Guidelines:
- **Content Writing Guidelines:** `/docs/SEO/1b. content_writing_guidelines.md` (voice, tone, style)
- **Technical SEO Guidelines:** `/docs/SEO/1c. technical_seo_guidelines.md` (schema, structure, technical requirements)
- **SEO Factbase:** `/docs/SEO/1a. seo_factbase.md` (proprietary data to cite)
- **SEO Master Plan:** `/docs/SEO/1. SEO_CONTENT_MASTER_PLAN.md` (243 keywords, 13 clusters, strategy)

### Phase-Specific Prompts:
- **Phase 1:** [`PHASE_1_RESEARCH_PROMPT.md`](./PHASE_1_RESEARCH_PROMPT.md)
- **Phase 2:** [`PHASE_2_OUTLINE_PROMPT.md`](./PHASE_2_OUTLINE_PROMPT.md)
- **Phase 3:** [`PHASE_3_WRITING_PROMPT.md`](./PHASE_3_WRITING_PROMPT.md)
- **Phase 4:** [`PHASE_4_QA_REVIEW_TRACKER.md`](./PHASE_4_QA_REVIEW_TRACKER.md)

---

## Tips for Success

### Do:
✅ Follow the process step-by-step (don't skip steps)
✅ Complete quality gates before moving to next phase
✅ Use the factbase data extensively (it's your competitive advantage)
✅ Get approval on research and outline before writing
✅ Read every post aloud before publishing (catches issues)
✅ Track progress in the table above

### Don't:
❌ Skip research phase (it informs everything else)
❌ Write before outline is approved (wastes time on revisions)
❌ Use AI phrases ("It is important to note that...")
❌ Stuff keywords unnaturally
❌ Rush the quality passes (they catch critical issues)
❌ Forget to cite data sources credibly

---

## FAQ

**Q: Can I modify the process for different post types?**
A: Yes! Adjust word counts and structure based on post type:
- Pillar posts: 3,000-4,000 words, more comprehensive
- Feature posts: 1,800-2,500 words, focused on one capability
- Comparison posts: 2,000-2,800 words, structured around comparison
- Cost/ROI posts: 2,200-3,000 words, include calculators

**Q: What if the research reveals the keyword isn't worth targeting?**
A: That's valuable information! Document why and move to next keyword. Better to learn in Phase 1 than after writing 3,500 words.

**Q: How do I handle posts that need technical diagrams or custom images?**
A: Note in Phase 2 outline what's needed. Create placeholder text like `[IMAGE: Call routing flowchart showing AI decision tree]` and create/source images before final publish.

**Q: Can I batch certain phases?**
A: Research phase can be batched (research 5 posts at once), but outline and writing should be done one at a time for quality.

**Q: What if I find better data during writing phase?**
A: Add it! The phases are guidelines, not rigid rules. If you discover a perfect stat or example while writing, include it.

---

## Version History

- **v1.1** (2025-12-19): Added Phase 4 QA Review tracker and clarified publish flow
