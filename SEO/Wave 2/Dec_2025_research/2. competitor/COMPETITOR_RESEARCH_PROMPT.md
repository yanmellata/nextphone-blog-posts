# Competitor Content Research Prompt (Objective Documentation)

**Purpose:** Document what educational content a competitor has published. NO recommendations, NO speculation - purely objective inventory.

**Output:** Numbered analysis file matching extraction tracker.

---

## THE PROMPT

Copy this for each competitor:

```
Analyze the content strategy of this competitor:

Company: [COMPETITOR NAME]
Website: [URL]

MY CONTEXT:
I run NextPhone, an AI receptionist/answering service for small service businesses.
I need to understand what educational content this competitor has published.

SCOPE:
- Focus on: Blog posts, resources, guides, tutorials, educational content
- Ignore: Sales pages, product pages, pricing pages, about us
- Where to look: [URL]/blog, [URL]/resources, [URL]/guides, [URL]/learn

YOUR TASK (OBJECTIVE DOCUMENTATION ONLY):

1) CONTENT INVENTORY - Topic Categories (30% of effort)
   - Visit their blog/resources/guides
   - List EVERY topic category they cover
   - For each topic, document:
     * Topic name
     * Number of posts (approximate)
     * Depth: Shallow (<1000 words), Medium (1000-2000), Deep (2000+)
     * Specificity: Generic overview vs specific implementation
     * Has examples/screenshots/code? (yes/no)
     * Recency: Old (2020-2022) vs Recent (2023-2025)

   Example output:
   | Topic | Posts | Depth | Specificity | Examples | Recency |
   |-------|-------|-------|-------------|----------|---------|
   | HubSpot integration | 1 | Shallow (800w) | Generic overview | No | Old (2021) |
   | HVAC industry | 3 | Deep (2500w avg) | Specific workflows | Yes (screenshots) | Recent (2024) |

2) COMPLETE BLOG POST INVENTORY (50% of effort - CRITICAL)
   - List ALL blog posts you can find (this is the fact base for extraction)
   - For each post include:
     * Title
     * URL or slug
     * Category (from section 1)
     * Depth (Shallow/Medium/Deep)
     * Date published (if visible)

   Format as table:
   | Title | URL | Category | Depth | Date |
   |-------|-----|----------|-------|------|
   | 5 Things Every Dental Receptionist Should Know | /blog/things-a-dental... | Dental | Medium | 2024 |
   | The History of the Telephone | /blog/history-of-telephone/ | Filler | Shallow | 2020 |
   | How to Vet Answering Services | /blog/vetting-services/ | Guides | Deep | 2025 |

   NOTE: List as many as you can find (aim for complete inventory, not just highlights)

3) STRONG CONTENT - Citation-Worthy (10% of effort)
   - What would an LLM cite them for today?
   - List 5-10 specific posts that are citation-worthy
   - What makes them strong? (depth, data, frameworks, examples, recency)
   - Cite full URLs

   Example:
   - "5 Things Every Dental Receptionist Should Know" (https://...)
     * Why citation-worthy: Highly specific to dental niche, includes insurance workflows, terminology depth

4) WEAK/OUTDATED CONTENT (10% of effort)
   - What topics do they cover but poorly?
   - Objectively identify:
     * Thin content (<1000 words, no examples)
     * Outdated content (2020-2022, references old trends like "social distancing")
     * Generic content (platitudes, no frameworks/scripts/data)

   Example:
   - "The Art of Personal Connection" (https://...)
     * Why weak: Generic platitudes ("be nice"), no scripts, no data, <800 words

OUTPUT FORMAT:
- Use markdown with clear section headers
- Be specific and concrete
- Cite URLs when referencing posts
- Base this ONLY on what exists on their site (don't speculate or recommend)
- This is DOCUMENTATION not ANALYSIS - just the facts
```

---

## Output File Naming (Numbered for Tracking)

Save analysis as numbered markdown files matching the extraction tracker:

| # | Competitor | Output File |
|---|------------|-------------|
| 03 | Ruby Receptionists | `03_Ruby_Analysis.md` |
| 04 | Smith.ai | `04_SmithAI_Analysis.md` |
| 05 | Abby Connect | `05_Abby_Analysis.md` |
| 06 | Goodcall | `06_Goodcall_Analysis.md` |
| 07 | MyAIFrontDesk | `07_MyAIFrontDesk_Analysis.md` |
| 08 | Upfirst | `08_Upfirst_Analysis.md` |
| 09 | Emitrr | `09_Emitrr_Analysis.md` |

---

## Output Template

```markdown
# [##]_[COMPETITOR]_Analysis

**Competitor:** [Name]
**Website:** [URL]
**Analysis Date:** [Date]
**Analyst:** [Perplexity/Claude/etc]

---

## 1. CONTENT INVENTORY - Topic Categories

| Topic | Posts | Depth | Specificity | Examples | Recency |
|-------|-------|-------|-------------|----------|---------|
| ... | ... | ... | ... | ... | ... |

**Publishing frequency:** [Weekly/Monthly/Rarely]
**Total estimated posts:** [Number]

---

## 2. COMPLETE BLOG POST INVENTORY

| Title | URL | Category | Depth | Date |
|-------|-----|----------|-------|------|
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |

[Continue for all posts found]

---

## 3. STRONG CONTENT (Citation-Worthy)

1. **[Post Title]** ([URL])
   - Why citation-worthy: [Objective criteria - depth, data, frameworks, specificity]

2. **[Post Title]** ([URL])
   - Why citation-worthy: [Objective criteria]

[Continue for 5-10 posts]

---

## 4. WEAK/OUTDATED CONTENT

1. **[Post Title]** ([URL])
   - Why weak: [Objective criteria - word count, outdated references, generic content]

2. **[Post Title]** ([URL])
   - Why weak: [Objective criteria]

[Continue for notable examples]

---

## Summary Stats

- **Total posts documented:** [Number]
- **Strongest categories:** [List 2-3 based on depth + recency]
- **Weakest categories:** [List 2-3 based on thin/outdated content]
- **Content age:** [% recent 2023-2025 vs % old 2020-2022]
```

---

## Key Principles

1. **OBJECTIVE ONLY** - Document what exists, don't recommend what to write
2. **COMPLETE INVENTORY** - Section 2 is the critical fact base for extraction
3. **CITE EVERYTHING** - URLs for all posts mentioned
4. **NO SPECULATION** - If you can't verify it on their site, don't include it
5. **NUMBERED FILES** - Use numbered filenames (03-09) for tracking

---

## Workflow

For each of the 7 competitors:

1. Run this prompt (Perplexity/Claude/ChatGPT)
2. Save output as `##_[Competitor]_Analysis.md` in `/2. competitor/`
3. Verify section 2 has comprehensive blog post inventory
4. Use this objective documentation as input for extraction phase

The extraction phase will use this fact base to identify gaps and recommend blog posts for NextPhone.
