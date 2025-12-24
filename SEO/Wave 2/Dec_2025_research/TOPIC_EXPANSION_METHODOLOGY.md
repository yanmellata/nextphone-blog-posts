# Topic Expansion Methodology (Step 3)
**How to Generate 100-150 Topics in ~3 Hours**

---

## TL;DR

1. Consolidate gap analysis + competitor research → master opportunity list
2. Use one AI prompt to expand each category into specific titles
3. Score topics: 0-25 points (search volume + competition + intent + gap value)
4. Pick top 100-150, cluster into batches, write with AI

**Time:** 3-4 hours from research to production-ready topic list

---

## Step 1: Consolidate Everything (30 min)

**You have:**
- ✅ Gap Analysis (`GAP_ANALYSIS.md`) - 7 categories we're missing
- ✅ Competitor Research (6 files) - 90-120 post ideas (15-20 per competitor)

**Create:** `CONSOLIDATED_OPPORTUNITIES.md`

**How:**
1. Copy all 🔥 topics from competitor analyses (zero coverage topics)
2. Add gap categories from gap analysis
3. Group by priority

**Template:**
```markdown
# Consolidated Opportunities

## 🔥🔥🔥 Tier 1: Zero Coverage (Us + All Competitors)
- Integration guides: HubSpot, Salesforce, Calendly, Zoho, etc.
- HIPAA compliance guides
- Call recording laws by state
- Migration/switching guides
- Setup/onboarding checklists

**Count:** ~30-40 topics

## 🔥🔥 Tier 2: Zero Coverage (Us) + Weak Coverage (Competitors)
- Industry-specific workflows (HVAC emergency, dental scheduling, etc.)
- Advanced features (API, webhooks, multi-location)
- Seasonal content (holiday coverage, seasonal surge)

**Count:** ~40-50 topics

## 🔥 Tier 3: Beat Their Weak Content
- Outdated guides (refresh 2020-2022 content for 2025)
- Thin posts (expand <1000 word posts to 2500+)
- Generic posts (make specific with examples/frameworks)

**Count:** ~20-30 topics
```

---

## Step 2: Expand Categories into Specific Titles (1 hour)

**Goal:** Turn broad categories into 100-150 specific blog post titles

**One AI Prompt to Rule Them All:**

```
I'm creating 100-150 blog posts for NextPhone, an AI receptionist for service businesses.

Based on my research, I need specific blog post titles for these categories:

CATEGORY 1: Integration Guides (15 titles)
Tools: HubSpot, Salesforce, Zoho, Calendly, Google Calendar, ServiceTitan, Housecall Pro, Jobber, Zapier
Format: "How to Connect [Tool] with AI Receptionist: [Benefit]"

CATEGORY 2: Compliance & Security (10 titles)
Topics: HIPAA compliance, call recording laws (by state), data security, GDPR, SOC 2
Format: "[Compliance Type] for AI Receptionist: Complete Setup Guide"

CATEGORY 3: Industry Workflows (15 titles)
Industries: HVAC, plumbing, electrical, roofing, dental, medical, legal, real estate, accounting
Format: "AI Receptionist for [Industry]: [Specific Workflow/Emergency] Playbook"

CATEGORY 4: Setup & Onboarding (10 titles)
Topics: Initial setup, configuration, custom greetings, testing, optimization
Format: "How to [Action]: Step-by-Step Guide for AI Receptionist"

CATEGORY 5: Migration/Switching (8 titles)
From: Ruby, Smith.ai, traditional receptionist, voicemail, old systems
Format: "Switching from [Old System] to AI Receptionist: Complete Migration Guide"

CATEGORY 6: Advanced Features (8 titles)
Topics: API, webhooks, Zapier, custom workflows, multi-location, team management
Format: "[Feature] Setup for AI Receptionist: Technical Guide"

CATEGORY 7: Seasonal Content (8 titles)
Topics: Holiday coverage, HVAC summer surge, roofing storm season, tax season overflow
Format: "[Season/Event] Coverage: AI Receptionist Guide for [Industry]"

CATEGORY 8: Beat Competitor Weak Content (15 titles)
Take their generic/outdated topics and make them better:
- Add "2025" for freshness
- Add "Complete Guide" for depth
- Add specific frameworks/checklists
Format: "[Topic]: Complete 2025 Guide with [Framework/Tool]"

Requirements:
- Be SPECIFIC (not "CRM integration" but "HubSpot Integration: Step-by-Step")
- Implementation-focused (playbooks, checklists, step-by-step)
- Include the tool/industry/system name in the title
- Target GEO (what would make an LLM cite this?)

Generate all titles organized by category.
```

**Save output as:** `GENERATED_TITLES.md`

**Expected result:** 90-120 specific, actionable blog post titles

---

## Step 3: Score Topics (1 hour)

**Goal:** Rank all titles by value (0-25 points)

**Scoring System:**
- **Search Volume** (0-10 pts): High >500/mo, Medium 200-500, Low 50-200, Very Low <50
- **Competition** (0-5 pts): Zero = 5pts, Low = 4pts, Medium = 3pts, High = 2pts
- **Intent** (0-5 pts): Transactional/Setup = 5pts, Problem-aware = 4pts, Informational = 2pts
- **Gap Value** (0-5 pts): Zero coverage = 5pts, Weak coverage = 4pts, Some coverage = 2pts

**Quick Scoring Prompt:**
```
Score these blog post titles for SEO value (0-25 points):

[Paste your 100-150 titles]

Scoring criteria:
- Search volume (0-10): Estimate monthly searches
- Competition (0-5): Based on market saturation
- Intent (0-5): How close to conversion?
- Gap (0-5): How unique is this content?

Return as a table:
| Title | Vol | Comp | Intent | Gap | Total |
```

**Create:** `SCORED_TOPICS.md` with results

**Priority tiers:**
- 🔥🔥🔥 **20-25 pts:** Write first (30-40 posts)
- 🔥🔥 **15-19 pts:** Write second (40-50 posts)
- 🔥 **10-14 pts:** Write third (20-30 posts)

---

## Step 4: Pick Topics & Start Writing (30 min + ongoing)

**Select your top 100-150:**
- 30-40 from Tier 1 (🔥🔥🔥 20-25 pts)
- 40-50 from Tier 2 (🔥🔥 15-19 pts)
- 20-30 from Tier 3 (🔥 10-14 pts)

**Batch them for efficiency:**
- **Batch A:** All integration guides (write together)
- **Batch B:** All compliance posts (write together)
- **Batch C:** All industry workflows (write together)
- **Batch D:** All setup/migration guides (write together)

**AI Writing Prompt:**
```
Write a 2500-3500 word blog post for NextPhone (AI receptionist for service businesses).

TOPIC: [Title]
PRIMARY KEYWORD: [keyword from title]

REQUIREMENTS:
✅ Key Takeaways box at top (3-5 bullets)
✅ H2/H3 structure
✅ FAQ section at bottom (5+ Q&As as H3s for schema)
✅ Use NextPhone stats: 45K calls/day, 4.9/5 stars, 74.1% missed calls
✅ Implementation-focused (step-by-step, checklists, playbooks)
✅ Examples and screenshots where applicable
✅ Professional but conversational tone
✅ Target GEO: depth, specificity, unique frameworks

STRUCTURE:
1. Intro + problem
2. Solution overview
3. Step-by-step implementation
4. Benefits/outcomes
5. FAQ section
6. Conclusion + CTA

Write now:
```

**Production flow:**
1. Pick 5-10 topics from same batch
2. Generate with AI ($15-30 for 10 posts)
3. Human review (2-3 hours for 10 posts)
4. Publish batch

**Timeline:**
- Week 1-2: Tier 1 posts (30-40 posts)
- Week 3-4: Tier 2 posts (40-50 posts)
- Week 5-6: Tier 3 posts (20-30 posts)

**Cost:** $200-450 for 100-150 posts

---

## Complete Workflow Summary

| Step | What | Time | Output |
|------|------|------|--------|
| 1 | Consolidate research | 30 min | `CONSOLIDATED_OPPORTUNITIES.md` |
| 2 | Generate titles | 1 hour | `GENERATED_TITLES.md` (100-150 titles) |
| 3 | Score titles | 1 hour | `SCORED_TOPICS.md` (ranked list) |
| 4 | Write with AI | 6 weeks | 100-150 published posts |

**Total prep time:** ~3 hours from research to production-ready list

**Total cost:** $200-450 for all content

---

## Why This Works

**GEO-optimized:**
- Depth: 2500-3500 words > thin competitor content
- Specificity: "HubSpot integration guide" > "CRM integration"
- Implementation: Step-by-step > high-level overview
- Freshness: 2025 content > 2020-2022 competitor posts
- Frameworks: Checklists, playbooks > generic tips

**We become the source LLMs cite.**

---

## Next Actions

1. ✅ Gap analysis (done)
2. ✅ Competitor research prompt (done)
3. 🔄 Run competitor research (6 competitors)
4. 🔄 Consolidate findings
5. 🔄 Generate & score topics
6. 🔄 Start writing Tier 1 posts
