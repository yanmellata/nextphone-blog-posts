# PHASE 3: WRITING PROMPT

**Goal:** Execute outline with consistent voice, quality, and all content elements

**Time:** ~4-5 hours
**Input:** Approved outline from Phase 2
**Output:** Publication-ready 3,000-3,500 word blog post

**Reference:** See `NEXTPHONE_FACTBASE.md` and `CONTENT_PRODUCTION_GUIDELINES.md`

---

## Overview

Writing phase is about execution. With research done and outline approved, writing becomes filling in the blueprint with:
- Conversational, non-AI voice
- Properly cited data
- Natural keyword integration
- Contextual links and CTAs
- Clean structure

**Follow the outline exactly.** Don't freelance or "improve" the structure mid-writing. If you find issues, note them for revision but finish according to plan.

---

## Core Voice & Tone Guidelines

### Voice: Conversational Consultant

You're a knowledgeable advisor helping a small business owner. You're:
- **Confident** but not arrogant
- **Helpful** but not salesy
- **Direct** but not cold
- **Friendly** but not unprofessional

### Key Principles

**1. Write Like You Talk**
- Use contractions (you're, it's, doesn't)
- Use first/second person (I, you, we)
- Vary sentence length
- Keep paragraphs short (2-4 sentences max)

**2. Active Voice, Not Passive**
✅ "AI answers calls you'd otherwise miss"
❌ "Calls that would otherwise be missed are answered by AI"

**3. Show, Don't Just Tell**
✅ "Your phone rings at 9 PM. A customer needs emergency AC repair—95-degree heat, no cooling. You're at dinner. The call goes to voicemail. They call the next contractor. $3,500 job lost."
❌ "Businesses lose revenue when they miss calls after hours."

**4. Natural Keyword Usage**
- Keywords should flow naturally
- If it feels forced, rewrite
- Use semantic variations
- Don't repeat the same phrase 10 times

---

## MDX Formatting Essentials

**CRITICAL:** Lists are the #1 formatting issue. Follow these rules exactly:

### Lists Must Have:
1. **Blank line before** the list starts
2. **Hyphen + space** at start of each item: `- Item text`
3. **Blank line after** the list ends

**WRONG (renders as jumbled paragraph):**
```markdown
Your text here:
**Item 1:** Description
**Item 2:** Description
**Item 3:** Description
```

**RIGHT (renders as clean bullets):**
```markdown
Your text here:

- **Item 1:** Description
- **Item 2:** Description
- **Item 3:** Description
```

### Other Formatting:
- **Headings:** Use `## H2` for main sections, `### H3` for subsections (never use `# H1` in body)
- **Bold:** `**text**` for emphasis
- **Inline code:** `` `code` `` for technical terms
- **Links:** `[anchor text](/blog/slug)` for internal, `[text](https://url.com)` for external
- **Tables:** Must have header row with `|---|---|` separator
- **CTAs:** `<BlogCTA variant="section" href="/path" text="CTA text" />` for section boxes

---

## Voice Examples: GOOD vs BAD

### Example 1: Opening Hook

**❌ BAD (AI-generated feel):**
> It is important to note that in today's digital landscape, AI customer service has emerged as a game-changing solution for businesses.

**✅ GOOD (Conversational):**
> Your phone rings. A potential customer needs help. But you're on a job site, hands covered in drywall mud. The call goes to voicemail. They call the next contractor. You just lost $4,500.

**Why better:** Specific scenario, short sentences, relatable, no jargon.

---

### Example 2: Using Data

**❌ BAD (Vague):**
> Studies show that many businesses experience significant challenges with managing their incoming call volume.

**✅ GOOD (Specific):**
> We analyzed 13,175 calls from 45 home services contractors over 7 months. The data is brutal: 74.1% of calls went completely unanswered. That's three out of every four potential customers calling someone else.

**Why better:** Exact numbers, sample size shown, vivid language, clear meaning.

---

### Example 3: Product Mentions

**❌ BAD (Too salesy):**
> NextPhone is the industry-leading, revolutionary AI-powered platform that outperforms all competitors with unparalleled features.

**✅ GOOD (Informative):**
> NextPhone takes the hybrid approach: AI answers every call in under 5 seconds, handles routine questions (hours, pricing, booking), and routes urgent calls to your phone immediately. You get 24/7 coverage without hiring staff.

**Why better:** Explains how it works, focuses on benefits, not hype.

---

## Forbidden Phrases (AI Tell-Tales)

These phrases scream "AI-generated." Never use them:

❌ "It is important to note that..."
❌ "In today's digital landscape..."
❌ "At the end of the day..."
❌ "Leveraging cutting-edge solutions..."
❌ "In conclusion..." (just conclude naturally)
❌ "Revolutionize your business..."
❌ "Game-changing solution..."
❌ "Unparalleled expertise..."
❌ "Cutting-edge technology..."
❌ "Seamlessly integrate..."
❌ "Robust solution..."
❌ "Empower your business..."
❌ "Drive meaningful results..."

**If you catch yourself using these, rewrite in plain English.**

---

## Data Citation Formats

### Citing NextPhone Factbase Data

**✅ GOOD Citation Formats:**
- "In our analysis of 13,175 customer service calls from 45 home services contractors over 7 months..."
- "We analyzed 2,487 emergency service calls and found that..."
- "Our study of 45 small businesses revealed that 74.1% of calls..."

**Include:**
- Sample size (13,175 calls)
- Business count (45 contractors)
- Time period (7 months)
- Exact percentages (74.1%, not "about three-quarters")

**❌ BAD Citation Formats:**
- "Studies show..." (too vague)
- "Research indicates..." (whose research?)
- "Many businesses lose..." (how many?)

### Citing External Sources

**✅ GOOD Citation Formats:**
- "According to Gartner's 2024 report on AI customer service..."
- "Harvard Business Review found that companies using AI..."
- "The Bureau of Labor Statistics reports the average customer service rep salary is $37,000..."

**Include:**
- Organization name (Gartner, HBR, BLS)
- Year (2024, 2023 - must be recent)
- Linked to source (with anchor text)

---

## Writing Process: Step-by-Step

### Step 3.1: Pre-Writing Setup (10 mins)

**Open These Documents:**
1. Approved outline from Phase 2
2. Research doc from Phase 1
3. This writing prompt (voice guidelines)
4. NEXTPHONE_FACTBASE.md (for stats and product info)

**Create Writing Document:**
- Use outline structure as skeleton
- Have sections/subsections already formatted
- Ready to fill in content

**Pre-Flight Check:**
- [ ] I understand the unique angle
- [ ] I have all data/stats ready
- [ ] I know where CTAs go (from outline)
- [ ] I have external sources ready to cite
- [ ] I have customer quotes ready

---

### Step 3.2: Write Key Takeaways Box (10 mins)

**Goal:** Create above-the-fold clarity

**Format:**
```markdown
**Key Takeaways:**
- [Bullet 1]
- [Bullet 2]
- [Bullet 3]
- [Bullet 4]
- [Bullet 5]
- [Bullet 6]
```

**Guidelines:**
- 3-6 bullets total
- Each bullet = 1 sentence (occasionally 2 if needed)
- Summarize entire post in scannable format
- Include 1 surprising stat or data point
- Answer "What will I learn?"

**Voice Check:**
- Read aloud
- Does it sound conversational?
- Any AI phrases? (remove them)
- Too technical? (simplify)

---

### Step 3.3: Write Intro (100-150 words) (15 mins)

**Structure:**
1. **Hook** (1-2 sentences): Shocking stat, relatable scenario, or bold claim
2. **Problem** (2-3 sentences): Describe the pain this topic addresses
3. **Promise** (1-2 sentences): Tell them what they'll learn
4. **Optional:** Soft CTA (if planned in outline)

**Hook Options:**
- **Scenario:** "Your phone rings at 9 PM. A customer needs..."
- **Shocking stat:** "74.1% of customer calls go completely unanswered."
- **Bold claim:** "You're losing $189,000 per year and don't even know it."
- **Question:** "What if you never missed another customer call?"

**Voice Check:**
- Conversational? (not "It is important to note...")
- Specific numbers? (not "many businesses")
- Active voice? (not passive constructions)
- Relatable? (would your target reader recognize this scenario?)

---

### Step 3.4: Write Section-by-Section (2-3 hours)

**Goal:** Follow outline exactly with consistent voice

**Process for EACH Section:**

1. **Write H2 + H3 structure first** (skeleton)
2. **Write subsections one at a time** (don't jump around)
3. **Insert data/stats** with proper citations as you write
4. **Add examples/quotes** where outlined
5. **Hit word count target** (±50 words is fine)
6. **Place internal/external links** as you write (don't save for later)
7. **Mark visual placement** with placeholder: `[IMAGE: description]`

**Writing Guidelines:**

**Paragraph Rules:**
- Max 2-4 sentences per paragraph
- One idea per paragraph
- Alternate short (1-2 sentences) and medium (3-4 sentences)

**Sentence Rules:**
- Vary length: Mix short punchy sentences with longer explanatory ones
- Active voice: "AI answers calls" not "calls are answered by AI"
- Conversational: Use contractions, first/second person

**List Rules:**
- Use bullet lists for scanability
- 3-7 items per list (not 2, not 15)
- Parallel structure (all start same way)
- Keep items to 1-2 sentences

**Data Citation:**
- Show sample size: "In our analysis of 13,175 calls..."
- Be specific: "74.1%" not "about three-quarters"
- Link to source: Inline link on organization name or stat
- Explain significance: Don't just drop a number, say what it means

**Section Transitions:**
- Natural bridges between sections
- Use questions: "So how does this work?"
- Reference previous section: "Now that you understand the problem..."
- Don't use "In conclusion" or "Next, we will discuss"

**Voice Check After Each Section:**
- Read aloud (does it flow?)
- Remove AI phrases
- Check keyword placement (natural?)
- Verify data citations (sample size shown?)

---

### Step 3.5: Write NextPhone Product Section (15 mins)

**Goal:** Natural product mention, educational tone

**Structure:**
1. **H2:** "How NextPhone Solves This" or "[Problem] Solved with NextPhone"
2. **Context** (1 paragraph): Connect to pain points just discussed
3. **Features** (2-3 paragraphs): Highlight 2-3 relevant capabilities
4. **Social proof** (1 paragraph): Customer quote or quick stat
5. **Soft CTA:** Link to demo/trial/how-it-works

**Tone:**
- Educational, NOT promotional
- Focus on HOW it solves problems (not just what it does)
- Use specific examples
- Conversational

**Voice Check:**
- Helpful (not salesy)?
- Features explained as benefits?
- CTA natural (not pushy)?

---

### Step 3.6: Write FAQ Section (20 mins)

**Goal:** Answer remaining questions concisely

**For Each FAQ:**
1. **Question as H3:** Natural phrasing (how people actually ask)
2. **Answer in 2-3 sentences:** Direct, conversational
3. **Optional link:** To related content for depth

**Example FAQ:**

```markdown
### How accurate is AI customer service?

Modern AI customer service platforms achieve 85-95% accuracy for routine inquiries like hours, pricing, and scheduling. The key is training the AI on your specific business—what services you offer, how you price, your availability. For complex or unusual questions, the best systems route calls to humans rather than attempting to answer and potentially getting it wrong.
```

**Voice Check:**
- Answers are direct (no fluff)?
- Tone is helpful (not defensive)?
- Complex topics simplified?

---

### Step 3.7: Write Conclusion (10 mins)

**Goal:** Recap and final CTA

**Structure:**
1. **Recap** (2-3 sentences): Main takeaways
2. **Final thought** (1-2 sentences): Recommendation or perspective
3. **Hard CTA** (1 sentence): Direct call to action

**Example:**
```markdown
## Start Capturing Every Customer Call

AI customer service isn't just for enterprises anymore. Small businesses are using it to answer calls they'd otherwise miss, capture leads 24/7, and compete with bigger competitors—all without hiring full-time staff.

The businesses winning in 2025 aren't the ones with the biggest marketing budgets. They're the ones answering every call.

Ready to stop missing calls? Start your free 14-day trial of NextPhone today →
```

**Voice Check:**
- Confident (not pushy)?
- Clear action step?
- Benefit-focused CTA?

---

### Step 3.8: Quality & Voice Pass (30 mins)

**Goal:** Polish to publication quality

**Read Entire Post Aloud**
- Seriously, read it out loud
- This catches awkward phrasing, repetition, AI phrases

**AI Phrase Hunt:**
Find and remove:
- [ ] "It is important to note that..."
- [ ] "In today's digital landscape..."
- [ ] "At the end of the day..."
- [ ] "Leveraging cutting-edge..."
- [ ] "In conclusion..."
- [ ] "Revolutionize your business..."
- [ ] "Game-changing solution..."
- [ ] "Seamlessly integrate..."
- [ ] Any phrase from Forbidden Phrases list

**Voice Improvements:**

**Vary sentence starts:**
❌ All sentences start with "AI customer service..."
✅ Mix it up: "AI answers...", "The technology...", "Small businesses...", "You can..."

**Break long paragraphs:**
- Max 4 sentences
- Split if longer

**Add transitions:**
- Between sections: "So how does this work?"
- Between paragraphs: "But there's more..."

**Data/Citation Check:**
- [ ] Every stat has a source
- [ ] Sample sizes mentioned for proprietary data (13,175 calls, 45 contractors)
- [ ] External sources are authoritative (Gartner, HBR, BLS)
- [ ] Calculations show math (42 calls × 74.1% × $3,500 = X)

**Link Check:**
- [ ] 3-7 internal links placed and contextual
- [ ] Anchor text is descriptive (not "click here")
- [ ] 2-4 external links to authority sources
- [ ] All links relevant to context

---

### Step 3.9: Technical SEO & Formatting Pass (20 mins)

**Goal:** Ensure technical elements are correct

**Metadata:**
- [ ] **Title:** 50-60 characters with primary keyword
- [ ] **Meta Description:** 140-160 characters with keyword and hook
- [ ] **URL Slug:** Clean, lowercase, hyphens, no dates

**Structure:**
- [ ] **Only ONE H1** (the title)
- [ ] **Proper hierarchy** (H1 → H2 → H3, no skipping)
- [ ] **Keyword appears in:** Title, first paragraph, at least one H2, URL slug

**Visual Placeholders:**
- [ ] Hero image specified with alt text
- [ ] 2-4 inline images/charts specified with descriptive alt text
- [ ] Placement noted (after which paragraph/section)
- [ ] All alt text includes keywords naturally

**Final Checks:**
- [ ] Word count is 3,000-3,500 words (or target for post type)
- [ ] Key Takeaways box complete (3-6 bullets)
- [ ] 3 CTAs placed (soft intro, mid-article, hard conclusion)
- [ ] FAQ section has 5-7 questions
- [ ] No placeholder text like [INSERT STAT] or [TK]

---

### Step 3.10: Pre-Publish Review (15 mins)

**Goal:** Final sanity check

**Big Picture Questions:**

1. **Would the target audience find this valuable?**
   - Does it solve their problem?
   - Is it actionable?

2. **Does it answer the search intent completely?**
   - Check Google again for the keyword
   - Does our post answer what users are looking for?

3. **Is it better than the #1 ranking post?**
   - How are we better? (more data, clearer structure, better examples)
   - If not clearly better, what can we improve?

4. **Does NextPhone feel naturally integrated?**
   - Not forced or overly promotional?
   - Product section feels helpful, not salesy?
   - CTAs are natural?

5. **Would I personally share this article?**
   - Quality bar test
   - If you wouldn't share it, why not?

**Pre-Publish Checklist:**

**CONTENT QUALITY:**
- [ ] Title is 50-60 characters with keyword
- [ ] Meta description is 140-160 characters
- [ ] Key Takeaways box (3-6 bullets)
- [ ] Intro hooks with data or scenario
- [ ] Industry data cited with source + sample size
- [ ] 3-7 internal links with descriptive anchors
- [ ] 2-4 external authoritative links
- [ ] 3 CTAs placed (soft, mid, hard)
- [ ] FAQ section (5-7 questions)

**TECHNICAL SEO:**
- [ ] URL is clean (`/blog/keyword-phrase`)
- [ ] Only ONE H1 (title)
- [ ] Proper H2 → H3 hierarchy
- [ ] 4-6 images with alt text + optimized filenames
- [ ] All images <200KB and WebP format

**VOICE/QUALITY:**
- [ ] Reads naturally (conversational)
- [ ] No AI tell-tale phrases
- [ ] Sentence variety (not all same length/structure)
- [ ] Paragraphs are 2-4 sentences max
- [ ] No keyword stuffing
- [ ] Proofread for typos/errors
- [ ] Read-aloud test passed

**If any checkbox fails → Fix before publishing**

---

## Writing Tips

**Do:**
✅ Follow outline exactly (don't freelance)
✅ Write sections in order (easier flow)
✅ Insert links/citations as you write (not later)
✅ Use placeholders for images (specify exactly what's needed)
✅ Take breaks between sections (prevents fatigue)
✅ Read aloud (catches 90% of issues)
✅ Check AI phrases (they sneak in)

**Don't:**
❌ Skip the outline and "just write"
❌ Write out of order (creates inconsistency)
❌ Save all links for the end (you'll forget context)
❌ Rush through quality passes (they're critical)
❌ Edit while drafting (finish draft first, then edit)
❌ Use generic stats ("many businesses lose...")
❌ Be overly promotional (education first, product mention second)

---

## Next Step

Once writing is complete and all checklists pass:

👉 **Convert to Next.js/MDX format**
👉 **Add images (create or source based on placeholders)**
👉 **Implement schema markup**
👉 **Publish and track**

Update the tracking table in [`BLOG_PRODUCTION_SYSTEM.md`](./BLOG_PRODUCTION_SYSTEM.md) with publish date.

---

## Writing Complete!

**Congratulations!** You've created a publication-ready SEO blog post following a proven 3-phase process.

**Remember:**
- Research informed your angles
- Outline guided your structure
- Writing executed the plan

This process is repeatable for all 155 blog posts in Wave 2.

Keep refining with each post—you'll get faster and better over time.

---

## Required Metadata (Add at End of Draft)

Before submitting your draft for QA, include this at the very end:

```markdown
---

**URL Slug:** `/blog/your-seo-friendly-slug-here`
```

### URL Slug Guidelines:
- Use lowercase with hyphens (e.g., `ai-receptionist-pricing`)
- Include primary keyword
- Keep it short but descriptive (3-5 words ideal)
- No special characters, spaces, or underscores

**Examples:**
- ✅ `/blog/ai-receptionist-cost`
- ✅ `/blog/hubspot-crm-integration-guide`
- ❌ `/blog/How_Much_Does_AI_Cost` (wrong format)
- ❌ `/blog/post-123` (not descriptive)

This slug becomes the URL and filename. The conversion script extracts it automatically.
