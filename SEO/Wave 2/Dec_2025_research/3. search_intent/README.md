# Search Intent Keyword Research

**Purpose:** Find high-volume, high-intent keywords using multi-angle Perplexity research.

---

## 📁 Folder Structure

```
3. search_intent/
├── README.md                    ← You are here
├── CORE_PROMPT.md              ← Master prompt template (with placeholders)
├── PROMPT_VARIATIONS.md        ← 15 different angles to research
└── results/                    ← Save Perplexity outputs here
    ├── integration_specific_results.md
    ├── hvac_industry_results.md
    ├── competitor_switching_results.md
    └── ...
```

---

## 🚀 Quick Start Guide

### Step 1: Pick a Variation

Open `PROMPT_VARIATIONS.md` and choose a variation to run.

**Recommended order:**
1. Integration-Specific (Tier 1)
2. HVAC Industry (Tier 1)
3. Competitor Switching (Tier 1)
4. Problem → Solution (Tier 1)
5. Compliance & Security (Tier 1)

### Step 2: Build the Prompt

1. Open `CORE_PROMPT.md`
2. Copy the entire prompt
3. Replace these placeholders with content from your chosen variation:
   - `[ANGLE_DESCRIPTION]`
   - `[FOCUS_AREAS]`
   - `[ADDITIONAL_CONTEXT]`

### Step 3: Run in Perplexity

1. Go to perplexity.ai
2. Paste your customized prompt
3. Wait for results (~2-3 minutes)
4. Copy the entire response

### Step 4: Save Results

1. Create a new file in `results/` folder
2. Name it: `[variation_name]_results.md`
   - Example: `integration_specific_results.md`
3. Paste the Perplexity output
4. Save

### Step 5: Repeat

Do Steps 1-4 for each variation you want to research.

**Recommended: Run 5-10 variations** (not all 15 unless you want comprehensive coverage)

---

## 📊 Expected Output Per Variation

Each Perplexity run should give you a table with ~50 keywords:

```markdown
| # | Keyword | Volume | Difficulty | Intent | User Type | Why This Matters |
|---|---------|--------|------------|--------|-----------|------------------|
| 1 | how to integrate hubspot with ai receptionist | Medium | Easy | Transactional | Business owner | High intent, zero competition |
| 2 | salesforce phone answering integration | Medium | Easy | Transactional | IT admin | Implementation search |
...
```

---

## 🎯 Prioritization Guide

### **Run First (Tier 1)** - 5 variations
- Integration-Specific
- HVAC Industry-Specific
- Competitor Switching
- Problem → Solution
- Compliance & Security

**Why:** Highest ROI, lowest competition, best commercial intent

**Output:** 250 keywords (50 × 5)

**Time:** 2-3 hours

---

### **Run Second (Tier 2)** - 5 variations
- Dental Practice-Specific
- Legal Practice-Specific
- Setup & Implementation
- Job-to-be-Done
- Question-Based (PAA Mining)

**Why:** Additional coverage, different angles

**Output:** +250 keywords = 500 total

**Time:** 2-3 hours

---

### **Optional (Tier 3)** - 5 variations
- Seasonal & Event-Based
- Budget & Pricing-Focused
- Long-Tail Micro-Niches
- Feature & Capability-Based
- Objection & Concern-Based

**Why:** Deep coverage, niche opportunities

**Output:** +250 keywords = 750 total

**Time:** 2-3 hours

---

## 🔄 After You're Done

**When you've run 5-10 variations:**

1. **Send all result files to Claude** (me)
2. **I will consolidate** all keywords into one master list
3. **Remove duplicates**
4. **Score by:** Volume + Intent + Difficulty + Strategic fit
5. **Output:** Top 100-150 keywords ranked by value

---

## 💡 Pro Tips

### Tip 1: Customize the Variations
Feel free to modify the variations in `PROMPT_VARIATIONS.md`:
- Change industries (add "roofing" or "electrician" specific)
- Add competitors you want to target
- Adjust focus areas based on your priorities

### Tip 2: Run in Batches
Don't try to run all 15 variations at once:
- **Week 1:** Run Tier 1 (5 variations)
- **Week 2:** Run Tier 2 (5 variations)
- **Week 3:** Consolidate and analyze

### Tip 3: Note Patterns
As you run variations, note:
- Keywords that appear in multiple variations (high priority)
- Emerging themes (new content categories)
- Gaps in your current content

### Tip 4: Use Different Models
Try running the same variation in:
- Perplexity (best for research)
- ChatGPT (different angle)
- Claude (me - can run one for you as example)

Different models = different keyword suggestions

---

## 📈 What You'll Get

**After running 5 Tier 1 variations:**
- 250 keywords with volume/difficulty/intent estimates
- Multiple angles on same topic (cross-validation)
- Identification of blue ocean opportunities (zero competition)
- Industry-specific terminology and long-tail phrases
- Question-based keywords for featured snippets

**After consolidation:**
- Top 100-150 keywords ranked by value
- Grouped by theme (integrations, compliance, industries, etc.)
- Scored by: Search volume + Competition + Intent + Strategic fit
- Ready for content production

---

## 🎬 Example Workflow

**Monday:**
- Run "Integration-Specific" variation → Save `integration_specific_results.md`
- Run "HVAC Industry" variation → Save `hvac_industry_results.md`

**Tuesday:**
- Run "Competitor Switching" variation → Save `competitor_switching_results.md`
- Run "Problem → Solution" variation → Save `problem_solution_results.md`

**Wednesday:**
- Run "Compliance & Security" variation → Save `compliance_security_results.md`

**Thursday:**
- Send all 5 result files to Claude
- Claude consolidates into ranked list
- Pick top 100 keywords for content production

**Total time:** 3-4 hours over 4 days
**Total cost:** $0

---

## ❓ FAQ

**Q: Do I need to run all 15 variations?**
A: No. Start with Tier 1 (5 variations). That's enough for 100-150 blog posts.

**Q: Can I modify the variations?**
A: Yes! Customize for your specific needs (different industries, competitors, etc.)

**Q: What if Perplexity doesn't give 50 keywords?**
A: That's fine. Ask it to "continue" or "give me 20 more". Or accept fewer keywords (quality > quantity).

**Q: Should I validate these with keyword tools?**
A: Yes, ideally validate top 20-30 keywords with Google Keyword Planner (free) to confirm volume estimates.

**Q: How do I know which variation to prioritize?**
A: Start with Tier 1. If you're unsure, run "Integration-Specific" first - it has lowest competition and highest intent.

---

## 🔗 Related Files

- `/1.global/GAP_ANALYSIS.md` - Internal content gaps
- `/2. competitor/COMPETITOR_RESEARCH_PROMPT.md` - Competitor analysis
- `/TOPIC_EXPANSION_METHODOLOGY.md` - How to combine all research

---

## Next Actions

1. ✅ Read this README
2. 🔄 Open `PROMPT_VARIATIONS.md` and pick 5 variations (Tier 1 recommended)
3. 🔄 For each variation, build prompt using `CORE_PROMPT.md`
4. 🔄 Run in Perplexity
5. 🔄 Save results in `results/` folder
6. 🔄 Send all result files to Claude for consolidation
