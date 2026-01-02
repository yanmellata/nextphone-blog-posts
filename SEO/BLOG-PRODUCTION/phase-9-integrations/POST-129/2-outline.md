# OUTLINE: "Contactually + NextPhone: Real Estate CRM Integration Guide"

## 2.1 STRUCTURE PLANNING

**User Intent:** Informational/Commercial (Understanding integration options + evaluating alternatives)

**User Journey:**
1. Problem awareness (missing calls = lost SOI relationships)
2. Understanding what Contactually was and why it mattered
3. Learning current alternatives exist
4. How phone + CRM integration works
5. Evaluating NextPhone as solution

**Questions to Answer (in order):**
1. What was Contactually and why did agents love it?
2. What happened to Contactually?
3. Why does sphere of influence matter for real estate agents?
4. How do missed calls damage SOI relationships?
5. How does phone + CRM integration work?
6. What CRMs work with NextPhone?
7. How does NextPhone preserve SOI relationships?
8. How complex is the setup?

**High-Level Section Flow:**
- Key Takeaways � Quick value overview
- Intro � Hook with missed call scenario from SOI contact
- Section 1 � Contactually legacy (what it was, why it mattered)
- Section 2 � The SOI problem for real estate agents
- Section 3 � How phone + CRM integration solves this
- Section 4 � NextPhone integration approach
- FAQ � Address technical concerns
- Conclusion � Recap & CTA

---

## 2.2 TOPIC COVERAGE CHECKLIST

### Table Stakes Topics (MUST Cover)
- [x] What Contactually was � Will cover in: **Section 1**
- [x] Sphere of influence concept � Will cover in: **Section 2**
- [x] CRM integration benefits � Will cover in: **Section 3**
- [x] Real estate workflow challenges � Will cover in: **Section 2**
- [x] How integration works � Will cover in: **Section 4**

### Differentiating Topics (SHOULD Cover to Beat Competitors)
- [x] Contactually shutdown context � **Section 1**
- [x] SOI degradation from missed callbacks � **Section 2**
- [x] Real estate-specific missed call stats � **Section 2**
- [x] HTTP webhook implementation � **Section 4**
- [x] Current CRM alternatives � **Section 4**

### Topics to Skip (And Why)
- Technical API documentation - Reason: Too technical for target audience (agents, not developers)
- Detailed Contactually feature list - Reason: Product is discontinued, not relevant

---

## DETAILED SECTION-BY-SECTION OUTLINE

## KEY TAKEAWAYS BOX

**Purpose:** Above-fold clarity for scanners
**Word Count Target:** 50-75 words (5 bullets)

**Bullets:**
1. Contactually shut down in 2022, but the need for relationship-focused real estate CRM remains critical
2. Real estate agents miss 46% of calls, and 87% of callers won't call back - devastating for sphere of influence relationships
3. Every missed callback request (25.4% of calls) weakens SOI relationships that generate 80% of deals
4. NextPhone + CRM integration captures every call and logs it automatically via HTTP webhooks
5. Works with Follow Up Boss, LionDesk, and other modern real estate CRMs using the same approach Contactually would have used

---

## INTRO

**Purpose:** Hook readers with relatable SOI scenario
**Word Count Target:** 100-120 words

**Structure:**
- Scenario: Past client calls about referral while agent is at showing
- Call goes to voicemail
- They call another agent
- Lost referral = lost relationship touchpoint

**Key Points to Cover:**
- Specific scenario (showing house, can't answer)
- Past client calling (SOI context)
- Immediate consequence (they move on)
- Broader impact (weakened relationship)

**Data/Stats to Include:**
- 78% of buyers choose the first agent who responds (CRITICAL HOOK STAT)

**Transition:** This is the problem Contactually was built to solve. Here's what happenedand what works now.

---

## SECTION 1: What Contactually Was (And Why Agents Loved It)

**Purpose:** Establish context for former users and educate new readers
**Word Count Target:** 200-250 words

**H3 Subsections:**
1. Contactually's Relationship-First Approach
2. Why It Mattered for Real Estate
3. What Happened to Contactually

**Key Points to Cover:**
- Contactually = relationship CRM (not just lead capture)
- Focused on sphere of influence tracking
- Automated follow-up reminders based on relationship strength
- Acquired by Compass in 2019
- Shut down March 31, 2022
- Agents needed alternative that preserved SOI focus

**Data/Stats to Include:**
- Acquired by Compass in 2019 for mid-eight figures
- Shut down March 31, 2022 (official)
- 80% of real estate deals come from SOI (establish why Contactually's focus mattered)

**Examples/Quotes:**
- Mention Contactually's "buckets" feature for segmenting contacts
- Reference that it integrated with 60+ tools

**Links to Add:**
- **External:** Link to [Contactually shutdown announcement](https://www.contactually.com/shutdown) with anchor text "Contactually permanently closed"

---

## SECTION 2: The Real Problem - Sphere of Influence Degradation

**Purpose:** Establish the core problem that phone + CRM integration solves
**Word Count Target:** 300-350 words

**H3 Subsections:**
1. What Is Sphere of Influence in Real Estate?
2. The Missed Call Problem for Agents
3. How Missed Callbacks Damage SOI Relationships

**Key Points to Cover:**
- SOI = network of family, friends, past clients, professional contacts
- Generates 33% of $100K+ agents' business (referrals) + 34% (repeat business)
- Agents can't answer during showings, open houses, closings
- 46% of real estate calls go unanswered
- 87% of callers won't call back
- 25.4% of calls include explicit callback requests
- Every missed callback = weakened relationship, lost referral opportunity

**Data/Stats to Include:**
- **External:** "Over 78% of property buyers choose the first agent who responds" - Moneypenny (LEAD WITH THIS)
- **External:** "Nearly 70% of buyers and sellers engage with the first real estate agent they speak to" - Callyzer
- **External:** "46% of calls to real estate agents go unanswered" - Zurple study
- **External:** "69% of callers who reach voicemail won't leave a message" - Callin.io
- **External:** "80% of real estate teams say most deals come from their SOI" - Follow Up Boss
- **External:** "33% of business from referrals, 34% from repeat business" - RealOffice360
- **Internal:** "25.4% of calls explicitly request callbacks" - NextPhone data
- **External:** "Missing 5 calls/month = $45,000 in annual lost commissions" - Callin.io

**Examples/Quotes:**
- Scenario: Past client calls for contractor referral, agent misses call, client asks different agent, relationship weakens
- Scenario: Buyer lead from Zillow calls, agent at showing, lead moves to next agent

**Visual Needed:**
- Type: Bar chart showing real estate missed call statistics
- Placement: After subsection 2
- Alt text: "Chart showing 46% of real estate agent calls go unanswered"

**Links to Add:**
- **External:** Cite [Zurple study](https://blog.zurple.com/-zurple-research-reveals-average-real-estate-lead-response-time) on missed calls
- **External:** Cite [Follow Up Boss SOI guide](https://www.followupboss.com/blog/spheres-influence) on SOI importance

---

## SECTION 3: Why Phone + CRM Integration Matters for SOI

**Purpose:** Bridge from problem to solution
**Word Count Target:** 200-250 words

**H3 Subsections:**
1. What Real Estate Agents Actually Need
2. The Two-Part Solution: Capture + Log

**Key Points to Cover:**
- Need #1: Answer or route every call (especially from SOI)
- Need #2: Automatically log call details in CRM
- Need #3: Preserve relationship continuity (know who called, when, why)
- Traditional solutions: Hire receptionist ($35K/year), use answering service ($500-800/mo), or use voicemail (ineffective)
- Modern solution: AI answers + CRM integration

**Data/Stats to Include:**
- **Internal:** "In our analysis of customer service calls, 74.1% went unanswered"
- Traditional receptionist: $35,000/year
- Traditional answering service: $500-800/month
- NextPhone: $199/month

**Examples/Quotes:**
- Example: Agent at showing � AI answers � captures callback request � logs to CRM � agent follows up later with full context

**Links to Add:**
- **Internal:** Link to AI Receptionist page with anchor text "AI receptionist"

---

## SECTION 4: How NextPhone + Real Estate CRM Integration Works

**Purpose:** Show practical implementation (differentiator)
**Word Count Target:** 300-350 words

**H3 Subsections:**
1. HTTP Webhook Integration (Universal Approach)
2. What Gets Captured and Logged
3. CRMs That Work with NextPhone

**Key Points to Cover:**
- NextPhone uses HTTP webhooks (same approach Contactually would have used)
- Works with any CRM that accepts webhooks: Follow Up Boss, LionDesk, HubSpot, custom systems
- No complex setup - configure once, works automatically
- Captures: Caller name, phone, reason for call, callback request, urgency level
- Logs to CRM in real-time (during or after call)
- Agent sees full context before returning call

**Data/Stats to Include:**
- List 3-5 compatible CRMs (Follow Up Boss, LionDesk, HubSpot, Salesforce, custom)
- Response time comparison: <5 seconds (AI) vs. 30+ seconds (traditional answering service)

**Examples/Quotes:**
- Example workflow: Call comes in � AI answers � collects info � sends to CRM via webhook � agent notified
- Template snippet (simplified):
  ```
  When call ends � POST to CRM:
  - contact_name: {{caller_name}}
  - phone: {{caller_number}}
  - message: {{call_summary}}
  - urgency: {{urgency_level}}
  ```

**Visual Needed:**
- Type: Flowchart diagram
- Placement: After subsection 1
- Alt text: "Flowchart showing NextPhone call capture to CRM via HTTP webhook"

**Links to Add:**
- **Internal:** Link to HTTP Webhooks feature page with anchor text "HTTP webhooks"
- **Internal:** Link to pricing page when mentioning cost

---

## SECTION 5: NextPhone for Real Estate SOI Management

**Purpose:** Product pitch (natural, educational)
**Word Count Target:** 150-200 words

**H3 Subsections:**
1. How NextPhone Preserves SOI Relationships

**Key Points to Cover:**
- Answers every call in <5 seconds (even during showings)
- Routes urgent calls to your phone immediately
- Captures callback requests (25.4% of calls)
- Logs everything to your CRM automatically
- 24/7 coverage (after-hours, weekends)
- No missed SOI touchpoints

**Data/Stats to Include:**
- $199/month unlimited calls
- Answers in <5 seconds
- 24/7 availability

**Examples/Quotes:**
- "Whether you're at a showing, closing, or dinner, every call from your sphere gets handled professionally and logged automatically."

**Links to Add:**
- **Internal:** CTA link to demo or trial page

---

## FAQ SECTION

**Purpose:** Address remaining objections/questions
**Word Count Target:** 250-300 words (5 questions)

### FAQ #1: Is NextPhone compatible with my current CRM?

**Answer Outline:**
- Works with any CRM that accepts HTTP webhooks
- Examples: Follow Up Boss, LionDesk, HubSpot, Salesforce
- Also works with Zapier for 1000+ apps

**Link:** No link needed

---

### FAQ #2: Will AI sound robotic to my sphere of influence contacts?

**Answer Outline:**
- Modern AI sounds natural (conversational, not robotic)
- Can be trained on your business specifics
- For complex situations, routes to you immediately
- Most callers prefer fast AI answer vs. voicemail

**Link:** No link

---

### FAQ #3: What information gets captured and sent to my CRM?

**Answer Outline:**
- Caller name and phone number
- Reason for call (inquiry, callback request, referral)
- Urgency level
- Any details they share (property address, buyer needs, etc.)
- Fully customizable based on your workflow

**Link:** Internal link to features page

---

### FAQ #4: How hard is it to set up the CRM integration?

**Answer Outline:**
- One-time setup (usually <30 minutes)
- Provide your CRM webhook URL
- Configure what fields to send
- Test with a call, then it runs automatically
- Support team helps with setup

**Link:** No link

---

### FAQ #5: What if someone from my sphere wants to talk to me directly?

**Answer Outline:**
- AI can transfer calls mid-conversation
- You can set rules (e.g., always transfer past clients)
- Urgent calls route immediately
- You stay in control of who you talk to directly

**Link:** No link

---

## CONCLUSION

**Purpose:** Recap and final CTA
**Word Count Target:** 80-100 words

**Structure:**
1. Recap main point (SOI relationships need consistent touchpoints)
2. Missed calls break that consistency
3. Modern solution: AI + CRM integration
4. Hard CTA

**Key Message:**
- Contactually understood that real estate is a relationship business
- That hasn't changed - your sphere generates most of your deals
- The tool has changed, but the goal remains: never miss a touchpoint

**CTA:**
"Stop missing calls from your sphere. Try NextPhone free for 14 days �"

---

## 2.4 CONTENT ELEMENT MAPPING

### Visual Content Plan

| Placement | Type | Purpose | Description | Alt Text |
|-----------|------|---------|-------------|----------|
| Hero | Stock photo | Relatability | Real estate agent on phone during property showing | "Real estate agent answering call during home showing" |
| Section 2 | Bar chart | Show problem data | Chart: 46% of RE calls unanswered, 87% won't call back | "Chart showing real estate agents miss 46% of calls" |
| Section 4 | Flowchart | Explain process | Call � AI � Webhook � CRM flow | "Flowchart: NextPhone call to CRM integration via HTTP webhook" |

**Total visuals needed:** 3
**Notes:** All images <200KB WebP, alt text includes keywords

---

### Internal Linking Plan

| Section | Link To | Anchor Text | Context |
|---------|---------|-------------|---------|
| Section 3 | AI Receptionist page | "AI receptionist" | When explaining solution |
| Section 4 | HTTP Webhooks feature | "HTTP webhooks" | When explaining integration tech |
| Section 4 | Pricing page | "$199/month" | When discussing cost |
| FAQ #3 | Features page | "learn more about customization" | Custom data capture |

**Total internal links:** 4
**Notes:** Descriptive anchor text, contextual placement

---

### External Citation Plan

| Section | Source | What We're Citing | URL | Anchor Text |
|---------|--------|-------------------|-----|-------------|
| Section 1 | Contactually | Shutdown announcement | https://www.contactually.com/shutdown | "Contactually permanently closed" |
| Section 2 | Zurple | 46% unanswered stat | https://blog.zurple.com/-zurple-research-reveals-average-real-estate-lead-response-time | "Zurple's research" |
| Section 2 | Callin.io | 87% won't call back | https://callin.io/best-answering-service-for-real-estate-never-miss-a-lead-again/ | "industry data" |
| Section 2 | Follow Up Boss | SOI importance | https://www.followupboss.com/blog/spheres-influence | "Follow Up Boss" |

**Total external links:** 4
**Notes:** Authoritative sources, open in new tab

---

### CTA Plan

| Placement | Type | Copy | Link |
|-----------|------|------|------|
| After Key Takeaways | Soft | "See how NextPhone preserves SOI relationships �" | How It Works page |
| After Section 4 | Mid | "Stop missing calls from your sphere �" | Demo page |
| Conclusion | Hard | "Try NextPhone free for 14 days �" | Trial signup page |

**Total CTAs:** 3 (soft, mid, hard)

---

## 2.5 FAQ SECTION PLAN

*(Already detailed above in main outline)*

**Total FAQ Questions:** 5
**Schema Markup:** Yes, add FAQ schema

---

## 2.6 OUTLINE REVIEW

### Checklist Results

**Content Structure:**
- [x] Intro hooks with scenario (SOI call missed during showing)
- [x] Sections in logical order (follows user journey)
- [x] Each section answers clear question
- [x] Transitions between sections natural
- [x] Total word count realistic (1,200-1,400 words for low-priority integration)

**Topic Coverage:**
- [x] ALL table stakes topics covered
- [x] ALL differentiating topics/gaps covered
- [x] NextPhone mentioned naturally (Section 4-5, not forced)
- [x] Unique angle clear (SOI preservation via call capture + CRM logging)

**Content Elements:**
- [x] 3 CTAs planned (soft, mid, hard)
- [x] 4 internal links planned with anchor text
- [x] 4 external citations planned with sources
- [x] 3 visuals planned with placement
- [x] FAQ section has 5 questions

**Data & Examples:**
- [x] NextPhone factbase data used (74.1% missed, 25.4% callbacks)
- [x] External sources credible and recent (2024-2025)
- [x] Customer scenarios included
- [x] Cost comparisons shown

**Technical:**
- [x] Only ONE H1 (title)
- [x] H2 � H3 hierarchy proper
- [x] Primary keyword in: Title, intro, H2s
- [x] Semantic keywords distributed

---

### Refinements Made

1. **Shortened overall length** - Target 1,200-1,400 words (appropriate for low-priority integration post)
2. **Emphasized SOI angle** - Made sphere of influence degradation the central theme throughout
3. **Added Contactually context** - Section 1 clearly addresses what happened and why it mattered
4. **Practical webhook details** - Section 4 shows actual implementation approach (differentiator)
5. **Real estate specific stats** - Used RE industry data (46% missed, 87% won't call back, SOI importance)

---

### Final Approval

- [x] Outline reviewed
- [x] All feedback incorporated
- [x] Ready for Phase 3 (Writing)

---

**TOTAL TARGET WORD COUNT:** 1,200-1,400 words
**UNIQUE ANGLE:** SOI relationship preservation through call capture + automated CRM logging
**KEY DIFFERENTIATOR:** Real estate-specific stats + practical webhook implementation + current alternatives focus

**Status: Approved for Phase 3 Writing**
