# Competitor Excel Extraction Prompt

**Purpose:** Analyze competitor blog post Excel files to generate blog post ideas inspired by their coverage. Focus on what they HAVE, how to copy their approach, and how to go beyond.

**Approach:** Learn from each competitor individually (no cross-competitor analysis yet - that comes in Master Consolidation).

**Target:** Extract 20-30+ blog post ideas per competitor based on strength of hypothesis (no arbitrary limit).

---

## Input Files

Competitor Excel files in `/2. competitor/`:
- `ruby.xlsx` → `03_ruby_competitor_extraction.md`
- `smith.ai.xlsx` → `04_smith_ai_extraction.md`
- `abby.xlsx` → `05_abby_extraction.md`
- `goodcall.xlsx` → `06_goodcall_extraction.md`
- `myaifrontdesk.xlsx` → `07_myaifrontdesk_extraction.md` (need to add)
- `upfirst.ai.xlsx` → `08_upfirst_extraction.md`
- `emitrr.xlsx` → `09_emitrr_extraction.md`
- `heyrosie.xlsx` → `10_heyrosie_extraction.md` (renumber - was 09)

---

## Extraction Process

### Step 1: Load & Analyze Excel Data

1. Read competitor Excel file (title, URL, category columns)
2. Group posts by topic/category theme
3. Count posts per topic category
4. Classify investment level:
   - **Strong** (10+ posts) - they're trying to own this topic
   - **Medium** (3-9 posts) - decent coverage
   - **Weak** (1-2 posts) - exploratory/light coverage

### Step 2: Identify Content Strategy

Based on topic distribution:
- What topics do they invest in heavily?
- What's their positioning? (Industry-focused? Integration-focused? Compliance-focused?)
- What does their title/category structure tell us about their approach?

### Step 3: Generate Blog Post Ideas

For each topic they cover, recommend posts NextPhone should write:

**For Strong Topics (10+ posts):**
- They're investing heavily = high-value topic validated
- **We write:** Match their coverage + go beyond with deeper implementation
- **Example:** They have 15 HVAC posts on emergency workflows → We write comprehensive HVAC series adding automation, seasonal surge handling, dispatch integration

**For Medium Topics (3-9 posts):**
- Decent coverage validates demand
- **We write:** Go deeper with step-by-step guides, frameworks, implementation details
- **Example:** They have 5 integration comparison posts → We write detailed platform-specific setup guides with field mapping, workflows, troubleshooting

**For Weak Topics (1-2 posts):**
- They validated the topic is valuable (wrote about it)
- **We write:** Comprehensive coverage on the same topic
- **Example:** They have 1 setup overview → We write complete setup playbook series (pre-launch checklist, testing protocol, QA scenarios)

### Step 4: Apply Content Filters

Use `EXTRACTION_GUIDELINES.md` filters:
- ❌ **Exclude:** HIPAA/medical/healthcare, SOC 2, GDPR, ServiceTitan
- ✅ **Focus:** Service businesses (HVAC, plumbing, legal, real estate, accounting, contractors)
- ✅ **Prioritize:** IVR routing, business phone systems, calendars, integrations, setup/migration

### Step 5: Write Detailed Rationale

For each recommended post, include:
- **Their coverage:** What they have (number of posts, depth)
- **Our opportunity:** How we can copy their approach and go beyond
- **Specific angle:** What makes our post different/better
- **Strategic value:** Why this topic matters (based on their investment level)

---

## Output Format

```markdown
# [##]_[COMPETITOR]_extraction

**Source:** `/2. competitor/[competitor].xlsx`
**Extraction Date:** 2025-12-22
**Total Posts Analyzed:** [X]
**Total Posts Recommended:** [Y]

**Key Insight:** [1-2 sentences on their content strategy - what they invest in, what this tells us about valuable topics, what opportunities this reveals]

---

## Topic Coverage Inventory

| Topic Category | Posts | Investment Level | Their Approach |
|----------------|-------|------------------|----------------|
| HVAC Industry | 15 | Strong | Emergency workflows, seasonal tips, maintenance |
| Integration Guides | 12 | Strong | Multiple platforms, comparison-focused |
| Legal Industry | 5 | Medium | General practice tips, not niche-specific |
| Setup/Onboarding | 2 | Weak | Surface-level overview, no checklists |

**Content Strategy Summary:**
- Strong investment in: [List 2-3 topics with 10+ posts]
- Medium investment in: [List 2-3 topics with 3-9 posts]
- Weak coverage: [List 2-3 topics with 1-2 posts]
- What they teach us: [What their topic choices validate as valuable]

---

## Recommended Blog Posts

| # | Keyword/Topic | Blog Post Title | Rationale | Intent | Priority | Cluster |
|---|---------------|-----------------|-----------|--------|----------|------------|
| 1 | HVAC emergency routing | HVAC AI Receptionist Playbook: Emergency Triage, Seasonal Surge & Automated Dispatch | **Their coverage:** 15 HVAC posts focused on emergency scenarios and maintenance tips. **Our opportunity:** Go beyond with seasonal surge handling (summer AC vs winter heating), automated dispatch workflows, and escalation protocols they don't cover. They validate HVAC is high-value, we add operational depth + automation angle. | Problem-aware | High | Industry |
| 2 | HubSpot integration setup | HubSpot AI Receptionist Integration: Complete Field Mapping & Workflow Automation Guide | **Their coverage:** 12 integration posts but comparison-focused, not step-by-step implementation. **Our opportunity:** Platform-specific deep dive with field mapping examples, custom workflow setup, lead routing automation, sync troubleshooting. They prove integrations matter, we provide the implementation guide they lack. | Transactional | High | Integration |

[Continue for 20-30+ posts]

```

---

## Quality Guidelines

### Each blog post recommendation should:
- ✅ Be inspired by their actual coverage (reference their topic investment)
- ✅ Explain how we copy + go beyond (not just "write about X")
- ✅ Include strategic rationale (why this topic based on their investment level)
- ✅ Apply content filters (no HIPAA/medical/SOC 2/GDPR)
- ✅ Have clear differentiation angle (what makes ours better/different)

### Extract based on strength of hypothesis:
- **High Priority:** They invested heavily (10+ posts) = validated high-value topic, we need presence
- **High Priority:** They invested lightly (1-2 posts) + topic aligns with our focus areas (integrations, setup, IVR) = domination opportunity
- **Medium Priority:** They have medium coverage (3-9 posts) = go deeper to win
- **Low Priority:** Off-brand topics even if they cover them heavily (e.g., if they have 20 healthcare posts but we exclude HIPAA)

---

## Target Output

- **Minimum:** 20 posts per competitor (ensure we extract enough value)
- **Typical:** 20-30 posts per competitor
- **Large competitors:** 30-40 posts if extensive coverage warrants it
- **No arbitrary cap:** Extract ALL ideas that meet quality bar

---

## Workflow

1. **Load Excel** → Read competitor blog post data
2. **Analyze coverage** → Group by topic, count posts, classify investment level
3. **Identify strategy** → What are they trying to own?
4. **Generate ideas** → Match strong topics, deepen medium topics, dominate weak topics
5. **Apply filters** → Remove HIPAA/medical/SOC 2/GDPR
6. **Write rationale** → Explain their coverage + our opportunity for each post
7. **Output markdown** → Numbered extraction file matching tracker

---

## Notes

- **This pass:** Focus on learning from each competitor individually - what they HAVE, what they invest in
- **Later pass (Master Consolidation):** Cross-reference all 7 competitors + search intent + SEMrush to prioritize final blog list
- **Key principle:** We're learning what topics competitors validate as valuable (by publishing about them) and how to beat them at their own game by going deeper
