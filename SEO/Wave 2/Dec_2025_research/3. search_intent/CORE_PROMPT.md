# Core Keyword Research Prompt Template

**How to use:**
1. Copy this entire prompt
2. Replace the placeholders with content from `PROMPT_VARIATIONS.md`
3. Run in Perplexity
4. Save output as `[ANGLE_NAME]_results.md`

---

## THE PROMPT:

```
You are an SEO keyword researcher specializing in B2B SaaS for service businesses.

CONTEXT:
I run NextPhone, an AI receptionist service for small service businesses (HVAC, plumbing, dental, legal, accounting, real estate, contractors).

RESEARCH ANGLE:
[ANGLE_DESCRIPTION]

YOUR TASK:
Generate 50 high-potential keyword ideas based on REAL search behavior patterns for this specific angle.

For each keyword, estimate:
1. Search volume (monthly searches):
   - High (>500/mo)
   - Medium (100-500/mo)
   - Low (10-100/mo)

2. Keyword difficulty:
   - Easy (<30)
   - Medium (30-50)
   - Hard (>50)

3. Search intent:
   - Transactional (ready to buy/implement)
   - Problem-aware (looking for solutions)
   - Solution-aware (comparing options)
   - Informational (learning)

4. User type:
   - Business owner
   - Office manager
   - IT admin
   - Operations manager
   - Other

FOCUS AREAS FOR THIS ANGLE:
[FOCUS_AREAS]

ADDITIONAL CONTEXT:
[ADDITIONAL_CONTEXT]

OUTPUT FORMAT:
Provide results as a markdown table:

| # | Keyword | Volume | Difficulty | Intent | User Type | Why This Matters |
|---|---------|--------|------------|--------|-----------|------------------|
| 1 | [keyword phrase] | Medium | Easy | Transactional | Business owner | [1 sentence explanation] |

REQUIREMENTS:
- Include long-tail keywords (3-6 words preferred)
- Focus on transactional and problem-aware intent (not just informational)
- Include industry-specific variations where applicable
- Note seasonal patterns if relevant
- Base estimates on realistic B2B SaaS search patterns
- Prioritize keywords where existing content is weak or missing
- Include specific tool names, industries, or use cases in keywords

Generate all 50 keywords now.
```

---

## After Running:

Save the output as: `[ANGLE_NAME]_results.md` in the `results/` folder.

Example filenames:
- `integration_specific_results.md`
- `hvac_industry_results.md`
- `competitor_switching_results.md`
