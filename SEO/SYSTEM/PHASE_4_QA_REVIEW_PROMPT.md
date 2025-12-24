# Prompt for LLM: Blog Post Quality Review & Fixes

You are reviewing a blog post MDX file to ensure it renders correctly on the live website. You must check for specific rendering issues that have been verified to break on the actual site.

---

## Your Task

1. Read the entire MDX file
2. Identify ALL issues listed below
3. Output a report listing every issue found with line numbers
4. For each issue, provide the exact fix needed

---

## CRITICAL ISSUES TO CHECK (Must Fix)

### Issue #1: Numbered Lists with Bold Text

**Problem:** When a numbered list starts with bold text like `1. **Text**`, it renders with the number on a separate line from the text.

**What to look for:**
- Any line matching pattern: `1. **`, `2. **`, `3. **`, etc.
- Numbered lists where the first word after the number is bold

**How to fix:**
```markdown
# WRONG (breaks rendering):
1. **Set specific call-return windows.** Block 15 minutes at noon...
2. **Use text templates.** When you can't call back...

# CORRECT (renders properly):
**1. Set specific call-return windows.** Block 15 minutes at noon...

**2. Use text templates.** When you can't call back...
```

**Search pattern:** `^\d+\.\s+\*\*`

---

### Issue #2: Extra Table Separator Rows

**Problem:** Tables have an extra row of dashes after the header separator, causing visual glitches.

**What to look for:**
- Lines that contain only `|`, dashes, and spaces
- Specifically: `| -------- | --------------- | -------------- |`
- These appear AFTER the proper header separator `| --- | --- | --- |`

**How to fix:**
```markdown
# WRONG (has extra separator row):
| Factor | Full-Time Hire | Live Service |
| --- | --- | --- |
| -------- | --------------- | -------------- |
| Monthly Cost | $4,000 | $400 |

# CORRECT (no extra row):
| Factor | Full-Time Hire | Live Service |
| --- | --- | --- |
| Monthly Cost | $4,000 | $400 |
```

**Search pattern:** Look for any line matching `^\|\s*-{4,}` that appears after a proper `| --- |` separator

---

### Issue #3: Pros/Cons as Paragraphs Instead of Bullets

**Problem:** Pros and Cons sections running together as paragraph text instead of bulleted lists.

**What to look for:**
- Sections with **Pros:** or **Cons:** headers
- Multiple bold terms with colons in a row without bullets
- Text like: `**Item:** Description **Item:** Description **Item:** Description`

**How to fix:**
```markdown
# WRONG (paragraph format):
**Pros:**
**Fast response:** Answers in under 5 seconds **Scales infinitely:** Handles 1 call or 100 simultaneous calls **Never unavailable:** No sick days, vacations, lunch breaks

# CORRECT (bulleted format):
**Pros:**
- **Fast response:** Answers in under 5 seconds
- **Scales infinitely:** Handles 1 call or 100 simultaneous calls
- **Never unavailable:** No sick days, vacations, lunch breaks
```

**Search pattern:** Find `**Pros:**` or `**Cons:**` and check if the following lines have bullets (`-` or `*`)

---

### Issue #4: Cost Breakdown Formatting

**Problem:** "Total" cost lines are formatted as bullets when they should be standalone for emphasis.

**What to look for:**
- Lines containing "Total:" in cost comparison sections
- "Total" appearing as a bullet item: `- **Total: $X**` or `* Total: $X`

**How to fix:**
```markdown
# WRONG (Total as bullet):
- Salary: $33,960/year
- Benefits: $8,490
- **Total: $42,450/year**
- Availability: 40 hours/week

# CORRECT (Total standalone):
- Salary: $33,960/year
- Benefits: $8,490

**Total: $42,450/year**

- Availability: 40 hours/week
```

**Rule:** Total lines should have blank lines before and after, and NOT be bulleted.

---

### Issue #5: Nested List Hierarchy (Timeline Sections)

**Problem:** Parent items (like "Hour 1", "Hour 2") at the same indentation level as their children.

**What to look for:**
- Sections describing timelines or multi-step processes
- Bold items like `* Hour 1:` or `* Step 1:` followed by sub-items at the same level
- Missing indentation for child items

**How to fix:**
```markdown
# WRONG (flat structure):
* Hour 1: Initial setup
* Connect your business phone number
* Enter business basics
* Hour 2: Train the AI
* Add your service list

# CORRECT (nested structure):
- **Hour 1: Initial setup**
  - Connect your business phone number
  - Enter business basics
- **Hour 2: Train the AI**
  - Add your service list
  - Input common FAQs
```

**Rule:** Parent items should be bold and at the left margin. Child items should be indented 2-4 spaces.

---

### Issue #6: FAQ Section Structure for Schema Generation

**Problem:** FAQ sections must follow a specific structure for automatic FAQ schema generation.

**What to look for:**
- FAQ section must start with `## Frequently Asked Questions` or `## FAQ` (H2 heading)
- Each question must be an H3 heading (`### Question text?`)
- Answer must be plain paragraph text immediately following the question
- No other formatting between question and answer

**How to fix:**
```markdown
# WRONG (inconsistent structure):
## FAQs

**Q: How much does it cost?**
A: It costs $199/month...

# CORRECT (schema-compatible structure):
## Frequently Asked Questions

### How much does it cost?

It costs $199/month...

### What are the main features?

The main features include...
```

**Why this matters:**
- Our Next.js blog automatically extracts FAQs and generates FAQ schema (JSON-LD)
- This schema enables rich snippets in Google search results
- LLMs also use FAQ schema for citations and answers
- Consistent structure = automatic SEO optimization for all 113+ blog posts

**Search pattern:** Find `## Frequently Asked Questions` or `## FAQ` and verify all questions are H3 headings with plain text answers

---

## SECONDARY ISSUES TO CHECK

### Issue #7: Broken CTAs

**What to look for:**
- Text in square brackets appearing alone on a line: `[Start your free trial]`
- These should be BlogCTA components, not plain markdown links

**How to fix:**
```markdown
# WRONG:
[Start your free trial today]

# CORRECT:
<BlogCTA text="Start your free trial today" variant="section" />
```

---

### Issue #8: Placeholder Links

**What to look for:**
- Links to `/blog/link`
- Generic company homepage links: `https://anthropic.com`, `https://techcrunch.com`, `https://hbr.org`, `https://mckinsey.com`
- Links that just say `(link)` in Related Articles sections

**How to fix:**
- If you can infer the correct blog post slug, replace `/blog/link` with the actual slug
- For generic company links, please go look at the relevant draft for the blog post which should hav the ORIGINAL LINK (or the research) 

  ```markdown
  # WRONG:
  According to [Anthropic research](https://anthropic.com), AI is improving.

  # CORRECT:
  According to [Anthropic research](https://anthropic.com/blog/relevant-research-study), AI is improving. 
  ```


---

### Issue #9: Checkmark Lists

**What to look for:**
- Checkmarks (✓) appearing without bullet formatting
- Text like: `✓ Item one ✓ Item two ✓ Item three` running together

**How to fix:**
```markdown
# WRONG:
✓ Unlimited incoming calls ✓ 24/7/365 availability ✓ Natural conversation AI

# CORRECT:
- ✓ Unlimited incoming calls
- ✓ 24/7/365 availability
- ✓ Natural conversation AI
```

---

### Issue #10: Dialogue Formatting

**What to look for:**
- Conversation examples running together in paragraph form
- Text like: `Customer: "Question" AI: "Answer" Customer: "Follow-up"`

**How to fix:**
```markdown
# WRONG:
Customer: "I need someone to look at my roof." AI: "I can help you schedule a roof inspection." Customer: "There's a leak."

# CORRECT:
- **Customer:** "I need someone to look at my roof."
- **AI:** "I can help you schedule a roof inspection."
- **Customer:** "There's a leak in the bedroom."
```

---

## OUTPUT FORMAT

Structure your response like this:

```
FILE: blog-post-slug.mdx

CRITICAL ISSUES FOUND:

1. [Line XX] Numbered list with bold text
   Current: 1. **Set specific call-return windows.** Block 15 minutes...
   Fix: **1. Set specific call-return windows.** Block 15 minutes...

2. [Line YY] Extra table separator row
   Current: | -------- | --------------- | -------------- |
   Fix: DELETE this line

SECONDARY ISSUES FOUND:

3. [Line ZZ] Broken CTA
   Current: [Start your free trial]
   Fix: <BlogCTA text="Start your free trial" variant="section" />

SUMMARY:
- Critical issues: 2
- Secondary issues: 1
- Total fixes needed: 3

PRIORITY: [HIGH/MEDIUM/LOW]
```

---

## TESTING INSTRUCTIONS

After making fixes, verify:

1. **Numbered lists:** Numbers appear on the SAME line as text (not separate lines)
2. **Tables:** Clean borders, no extra separator rows
3. **Pros/Cons:** Properly bulleted with clear structure
4. **Cost breakdowns:** Total lines are standalone with blank lines around them
5. **Nested lists:** Clear parent/child hierarchy with proper indentation

---

## IMPORTANT NOTES

- Be thorough - check EVERY numbered list, EVERY table, EVERY pros/cons section
- Line numbers are critical - always include them
- Show the exact current text and exact replacement text
- If multiple instances of the same issue exist, list ALL of them
- Prioritize critical issues (they break rendering) over secondary issues (just unprofessional looking)

---

## DO NOT

- Skip any section of the file
- Assume something is fine without checking
- Provide vague fixes like "fix the list" - give exact before/after
- Miss issues because they "look okay" in the markdown - they may render broken on the live site

---

Your goal: Ensure this blog post renders perfectly on getnextphone.com with no visual glitches, proper formatting, and working links.

---

## PHASE 4 ADDITION: SEO META FIELDS (REQUIRED BEFORE CONVERSION)

### Issue #11: Missing or Poor Quality Meta Title & Meta Description

**CRITICAL:** Before converting the draft to MDX, you MUST create optimized SEO meta fields. These should be added to the draft file as:

```markdown
**Meta Title:** [Your optimized title here]
**Meta Description:** [Your optimized description here]
```

---

### Meta Title Guidelines (60-70 characters)

**Purpose:** This is what appears in Google search results and browser tabs. It should be MORE compelling than the article title.

**Formula:**
- Include primary keyword
- Add specific numbers/pricing when relevant
- Add year (2025) for freshness
- Show clear value proposition
- Use comparison format when applicable

**Examples of GOOD meta titles:**

```markdown
# Article Title:
"How to Integrate NextPhone with HubSpot CRM: Complete Setup Guide"

# Meta Title (GOOD):
"NextPhone HubSpot Integration: 15-Min Setup Guide (No Coding Required)"
Why: Emphasizes speed, removes technical barrier

# Article Title:
"AI Receptionist Cost: Complete Pricing Guide for 2025"

# Meta Title (GOOD):
"AI Receptionist Cost 2025: Pricing Guide ($99-$500/Month vs $35K/Year Hiring)"
Why: Shows specific pricing range + comparison to alternative

# Article Title:
"Answering Service vs Voicemail: Which One Costs You More Customers?"

# Meta Title (GOOD):
"Answering Service vs Voicemail: 74% Miss Rate Costs $260K/Year"
Why: Quantifies the problem with specific data
```

**Examples of BAD meta titles:**

```markdown
❌ "Integration Guide: Connect AI Receptionist to Your Tech S..."
   (Truncated mid-word - looks broken in search results)

❌ "How to Integrate NextPhone with HubSpot CRM: Complete Setup Guide"
   (Just the title - no optimization, no compelling hook)

❌ "Best AI Receptionist"
   (Too short, no value prop, no differentiation)
```

---

### Meta Description Guidelines (150-160 characters)

**Purpose:** The snippet that appears under your title in Google search results. This is your sales pitch to get the click.

**Formula:**
- Start with a problem or statistic
- Include primary keyword naturally
- Show the solution/benefit
- End with a complete sentence (never truncate mid-word!)
- Use specific numbers when possible

**Examples of GOOD meta descriptions:**

```markdown
"74% of contractor calls go unanswered, costing $260K/year in lost revenue. NextPhone's AI receptionist integration with HubSpot captures every lead automatically at $199/month."
(159 chars - complete sentence, problem + solution + pricing)

"AI receptionist pricing 2025: $99-299/mo with unlimited calls and 24/7 coverage. Compare plans, features, and ROI calculations for your business."
(147 chars - clear value, specific pricing, complete thought)

"CRM phone integration auto-logs calls, cuts data entry by 17%, returns 42% more callbacks. Works with HubSpot, Salesforce, Zoho. Setup guide + AI integration."
(159 chars - specific benefits with numbers, platform names, complete)
```

**Examples of BAD meta descriptions:**

```markdown
❌ "The average home services contractor receives 42 calls per month. With a 74.1% miss rate, that's 31 missed opportunities every month. Without CRM integrati"
   (Truncated mid-word "integrati" - looks broken and unprofessional)

❌ "- HubSpot AI Receptionist Integration: Complete Setup Guide - Salesforce AI Receptionist Integration: Connect Your CRM - Google Calendar Integration for AI"
   (Just a list of keywords, no value prop, no complete thought)

❌ "Learn about AI receptionists for small businesses."
   (Generic, no specifics, no compelling reason to click)
```

---

### Where to Add Meta Fields in Draft

Add these fields at the TOP of the draft, right after the title and before Key Takeaways:

```markdown
# How to Integrate NextPhone with HubSpot CRM: Complete Setup Guide

**Meta Title:** NextPhone HubSpot Integration: 15-Min Setup Guide (No Coding Required)

**Meta Description:** 74% of contractor calls go unanswered, costing $260K/year. NextPhone's HubSpot integration captures every lead automatically. Complete setup guide with field mapping examples.

**Key Takeaways:**
- NextPhone integrates with HubSpot via HTTP webhooks...
```

---

### QA Checklist for Meta Fields

Before approving a draft for conversion, verify:

- [ ] Meta Title exists and is 60-70 characters
- [ ] Meta Title includes primary keyword
- [ ] Meta Title has specific numbers/pricing/year when relevant
- [ ] Meta Title is MORE compelling than the article title
- [ ] Meta Description exists and is 150-160 characters
- [ ] Meta Description ends with a complete sentence (no truncation!)
- [ ] Meta Description includes problem + solution or clear value prop
- [ ] Meta Description uses specific numbers/data when possible
- [ ] Both fields are added to the draft file in the correct location

---

### Why This Matters

**The conversion script will extract these fields from the draft.** If they're missing or poorly written:
- ❌ Script will auto-generate garbage (truncated first paragraph)
- ❌ All your manual edits will be lost if post is reconverted
- ❌ Search results will look broken and unprofessional
- ❌ Click-through rates will be significantly lower

**With proper meta fields in the draft:**
- ✅ One-time conversion preserves your SEO work
- ✅ Professional appearance in search results
- ✅ Higher click-through rates (better CTR = better rankings)
- ✅ No need to manually edit MDX files after conversion

---

## UPDATED OUTPUT FORMAT

When reviewing a draft, your response should now include:

```
FILE: POST-XXX/3-draft.md

META FIELDS REVIEW:

Meta Title: [MISSING / NEEDS OPTIMIZATION / GOOD]
- Current: [show current if exists]
- Suggested: [your optimized version]
- Length: XX chars
- Issues: [list any problems]

Meta Description: [MISSING / NEEDS OPTIMIZATION / GOOD]
- Current: [show current if exists]  
- Suggested: [your optimized version]
- Length: XXX chars
- Issues: [list any problems]

CRITICAL ISSUES FOUND:
[... rest of QA as before ...]
```

