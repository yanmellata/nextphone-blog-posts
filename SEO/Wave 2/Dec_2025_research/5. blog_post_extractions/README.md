# Blog Post Extractions - Methodology & Output Format

**Created:** 2025-12-21
**Purpose:** Extract blog post recommendations from each research source individually, maintaining unique insights before master consolidation.

---

## Output Format (Simplified)

Each extraction file contains:

### 1. Header Metadata
```markdown
# Blog Post Extraction: [SOURCE NAME]

**Source:** [file path]
**Extraction Date:** 2025-12-21
**Total Posts Recommended:** X

**Key Insight:** [1-2 sentences summarizing what this source reveals, main gaps/opportunities, user feedback applied]
```

### 2. Blog Posts Table
Single comprehensive table with detailed rationale column:

| # | Keyword/Topic | Blog Post Title | Rationale | Intent | Priority | Cluster |
|---|---------------|-----------------|-----------|--------|----------|---------|

**Rationale Column Should Include:**
- Why this topic matters (evidence from source)
- Search volume estimates if available
- Competition level / competitor gaps
- User feedback if applicable ("user-approved", removed content, etc.)
- Strategic value / differentiation
- Specific pain points addressed
- Any seasonal/timing considerations

**No Extra Sections:** Cluster Analysis, Quick Wins, Content Format Recommendations, etc. have been removed. All insights go into the rationale column.

---

## Extraction Principles

### 1. No Arbitrary Limits
- Extract ALL valuable topics that meet quality bar
- Focus on strength of hypothesis, not hitting a target number
- Could be 5 posts or 50 posts depending on source richness

### 2. Maintain Source Uniqueness
- Each source provides different insights:
  - **Gap Analysis** → Internal content gaps, volume estimates
  - **Competitor Analysis** → Blue ocean opportunities, what competitors miss
  - **Search Intent Research** → Validated keyword demand, intent classification
  - **SEMrush** → Volume + difficulty data, keyword clustering
- Don't consolidate prematurely
- Preserve rationale tied to specific source

### 3. Quality Bar (Strength of Hypothesis)
- **High Priority:** Clear demand + low competition + high conversion intent
- **Medium Priority:** Validated demand + medium competition OR high strategic value
- **Low Priority:** Long-tail opportunity + builds authority OR seasonal relevance

### 4. Apply Content Filters (See EXTRACTION_GUIDELINES.md)
- ❌ **Exclude:** HIPAA/medical/healthcare, SOC 2, GDPR, ServiceTitan, sync errors troubleshooting
- ✅ **Focus:** Service businesses (HVAC, plumbing, legal, real estate, accounting, contractors)
- ✅ **Prioritize:** IVR routing, business phone systems, calendars, integrations, setup/migration

---

## File Organization (Numbered 1-to-1 Matching)

### Global Research (2 files)
| # | Source File | Extraction File | Status |
|---|-------------|-----------------|--------|
| 01 | `/1.global/GAP_ANALYSIS.md` | `01_GAP_ANALYSIS_extraction.md` | ✅ Complete (42 posts) |
| 02 | `/1.global/NextPhone-100-Posts.md` | `02_NextPhone_100_Posts_extraction.md` | Pending |

### Competitor Analyses (7 files - re-running with new prompt)
| # | Source File | Extraction File | Status |
|---|-------------|-----------------|--------|
| 03 | `/2. competitor/Ruby_Analysis.md` | `03_ruby_competitor_extraction.md` | ⏳ Re-running research |
| 04 | `/2. competitor/SmithAI_Analysis.md` | `04_smith_ai_extraction.md` | ⏳ Re-running research |
| 05 | `/2. competitor/Abby_Analysis.md` | `05_abby_extraction.md` | ⏳ Re-running research |
| 06 | `/2. competitor/Goodcall_Analysis.md` | `06_goodcall_extraction.md` | ⏳ Re-running research |
| 07 | `/2. competitor/MyAIFrontDesk_Analysis.md` | `07_myaifrontdesk_extraction.md` | ⏳ Re-running research |
| 08 | `/2. competitor/Upfirst_Analysis.md` | `08_upfirst_extraction.md` | ⏳ Re-running research |
| 09 | `/2. competitor/Emitrr_Analysis.md` | `09_emitrr_extraction.md` | ⏳ Re-running research |

### Search Intent Research (13 files)
| # | Source File | Extraction File | Status |
|---|-------------|-----------------|--------|
| 10 | `/3. search_intent/results/1. nextphone-keywords.md` | `10_integration_keywords_extraction.md` | ✅ Complete (16 posts) |
| 11 | `/3. search_intent/results/2. NextPhone_HVAC_Keywords_50.md` | `11_hvac_keywords_extraction.md` | Pending |
| 12 | `/3. search_intent/results/3.comeptitor switching.md` | `12_competitor_switching_extraction.md` | Pending |
| 13 | `/3. search_intent/results/4. nextphone-50-keywords.md` | `13_problem_solution_extraction.md` | Pending |
| 14 | `/3. search_intent/results/7. prompt.md` | `14_legal_keywords_extraction.md` | Pending |
| 15 | `/3. search_intent/results/8. nextphone-keywords.md` | `15_setup_implementation_extraction.md` | Pending |
| 16 | `/3. search_intent/results/9.prompt.md` | `16_jtbd_keywords_extraction.md` | Pending |
| 17 | `/3. search_intent/results/10. NextPhone_PAA_Keywords.md` | `17_paa_keywords_extraction.md` | Pending |
| 18 | `/3. search_intent/results/11. prompt.md` | `18_seasonal_keywords_extraction.md` | Pending |
| 19 | `/3. search_intent/results/12. prompt.md` | `19_budget_pricing_extraction.md` | Pending |
| 20 | `/3. search_intent/results/13. NextPhone-50-keywords.md` | `20_micro_niches_extraction.md` | Pending |
| 21 | `/3. search_intent/results/14. nextphone_keywords.md` | `21_feature_capability_extraction.md` | Pending |
| 22 | `/3. search_intent/results/15. NextPhone_Keywords.md` | `22_objection_concern_extraction.md` | Pending |

### SEMrush Data (1 file - special clustering approach)
| # | Source File | Extraction File | Status |
|---|-------------|-----------------|--------|
| 23 | `/4. keyword search (semrush)/consolidated_semrush_keyword_answering-service_broad-match_us_2025-12-21.xlsx` | `23_semrush_consolidated_extraction.md` | Pending |

### Master Consolidation
- `MASTER_CONSOLIDATION.md` - Final step combining all 23 extractions

**Progress: 2/23 complete (9%)**
- ✅ GAP_ANALYSIS (42 posts)
- ✅ Integration keywords (16 posts)
- ⏳ 7 competitor analyses (re-running research with revised prompt)
- ⏸️ 12 search intent files pending
- ⏸️ 1 SEMrush file pending

---

## SEMrush Special Handling (500 Keywords)

**Challenge:** 500 keywords total, all meet quality bar (KD <40, volume >10), can't just extract "top 50"

**Solution: Keyword Clustering + Multi-Keyword Posts**
1. Group keywords into thematic clusters (e.g., all "bilingual answering" keywords together)
2. Create blog posts that target 3-5 related keywords each
3. Result: ~100-150 strategic posts covering ALL 500 keywords comprehensively

**Extraction Output for SEMrush:**
- Same table format as other sources
- Rationale column lists the 3-5 keyword cluster each post addresses
- Ensures comprehensive coverage without arbitrary top-N filtering

---

## Extraction Workflow

### For Each Source File:

1. **Read source thoroughly**
2. **Apply EXTRACTION_GUIDELINES.md filters**
   - Remove HIPAA/medical/healthcare topics
   - Remove enterprise compliance (SOC 2, GDPR)
   - Focus on service businesses only
   - Prioritize user-identified opportunities (IVR, phone systems, calendars)

3. **Extract blog post recommendations**
   - No arbitrary limits (extract ALL that meet quality bar)
   - Write detailed rationale for each post
   - Include source evidence (volume, competition, gaps, user feedback)

4. **Ask user validation questions**
   - Any posts to remove? (wrong positioning, product doesn't support it)
   - Topics/angles missed?
   - Priority alignment check
   - Competitive context updates

5. **Iterate based on feedback**

---

## Sample Extractions (3 Completed)

### 1. GAP_ANALYSIS_extraction.md (42 posts)
- **Source:** Internal gap analysis of 119 existing blog posts
- **Key Insight:** Integration & IVR routing have near-zero competitor coverage
- **User Feedback Applied:** Removed 11 HIPAA/medical posts, added 18 new posts (IVR x4, phone systems x5, website platforms x3, calendars x3)

### 2. ruby_competitor_extraction.md (15 posts)
- **Source:** Ruby Receptionists competitor analysis
- **Key Insight:** Ruby has zero platform-specific integrations, zero setup guides
- **User Feedback Applied:** Removed 5 HIPAA/SOC 2/GDPR posts, kept user-approved "sick" integrations

### 3. integration_keywords_extraction.md (16 posts)
- **Source:** Search intent research (50 integration keywords)
- **Key Insight:** 64% transactional intent, two-way sync is differentiated keyword
- **User Feedback Applied:** Removed sync errors troubleshooting ("weird"), highlighted user-approved integrations

---

## Remaining Extractions (21 Files)

**Next to Process:**
- 1 global research file (NextPhone-100-Posts.md)
- 7 competitor analyses (Smith.ai, Abby, Emitrr, Goodcall, HeyRosie, MyAIFrontDesk, Upfirst)
- 12 search intent files (HVAC, competitor switching, legal, setup, JTBD, PAA, seasonal, budget, micro-niches, features, objections, etc.)
- 1 SEMrush file (500 keywords - clustering approach)

**Timeline Estimate:**
- Processing: ~3-4 hours (with user validation after each)
- SEMrush clustering: ~1 hour
- Master consolidation: ~1 hour
- Wave prioritization: ~30 minutes
- **Total:** ~6-7 hours for all 24 sources

---

## Master Consolidation (Final Step)

Once all 24 extractions are complete:

### 1. Combine All Recommendations
- Merge all ~300-500 blog post recommendations
- Organize by cluster (Integration, IVR, Setup, Industry, etc.)
- De-duplicate overlapping topics (keep strongest rationale from source with best evidence)

### 2. Wave-Based Prioritization
Organize final list into production waves:
- **Wave 1 (Critical):** High volume + low competition + high intent + purchase blocker removal
- **Wave 2 (High Priority):** Medium volume + strategic value + differentiation
- **Wave 3 (Authority Building):** Long-tail + seasonal + educational

### 3. Production Tracker Format
Final output ready for batch production:
- Topic/Keyword
- Blog Post Title
- Cluster
- Priority Wave
- Rationale (from strongest source)
- Source(s)
- Production Status

---

## Quality Checklist

Each extraction should:
- ✅ Apply EXTRACTION_GUIDELINES.md filters (no HIPAA/medical/SOC 2/GDPR)
- ✅ Include detailed rationale with source evidence
- ✅ Classify intent (Transactional/Problem-aware/Solution-aware/Informational)
- ✅ Assign priority based on strength of hypothesis
- ✅ Organize by cluster for thematic grouping
- ✅ Note user feedback where applicable ("user-approved", "sick", removed content)
- ✅ Include competitive positioning (what competitors miss)
- ✅ Have concise 1-2 sentence key insight at top

Each extraction should avoid:
- ❌ Arbitrary top-N limits (extract ALL that meet quality bar)
- ❌ Generic rationale ("good keyword" → explain WHY from source)
- ❌ Premature consolidation (maintain unique insights per source)
- ❌ Missing context (always reference source data)
- ❌ Extra sections (Cluster Analysis, Quick Wins, etc. - all insights go in rationale column)
