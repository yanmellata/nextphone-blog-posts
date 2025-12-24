Plan: 30 prompts → 2 models → evaluation → final post list (92 calls)
Output you want at the end

A single JSON/CSV (or table) of 10–20 blog posts to write next, each tied to:

the original prompt

the opportunity type (playbook / decision framework / migration guide / troubleshooting / trust explainer)

a short “why this wins” note

suggested content format

Phase 0 — Setup (one-time)
Define a run

Pick one scope per run:

Example scopes: “after-hours call handling”, “switching from RingCentral”, “HVAC lead capture workflow”

Define:

ICP(s): HVAC / plumbing / roofing / electricians / general home services

Assumed product: AI receptionist/answering service for SMBs

Constraints: “avoid generic definitions; bias toward implementation”

Standardize storage

Create a simple structure (db table / JSON files):

prompts[]

answers[prompt_id][model]

evaluations[prompt_id]

final_posts[]

Phase 1 — Agent 1: Prompt Generator (1 call)
Goal

Generate 30 high-intent prompts that a real buyer/operator would ask in ChatGPT.

Inputs

scope + ICP(s) + constraints

Output format (strict)

For each prompt:

prompt_id

prompt_text

icp

theme (optional: integrations, switching, ops, troubleshooting)

Quality bar

Prompts must be action-seeking (“how do I…”, “what should I do if…”, “best way to…”)

No “what is…” beginner stuff unless it’s operational (“what is the best routing rule for…”)

Phase 2 — Model Probing (60 calls)
Agent 2: GPT Probe (30 calls)

For each prompt:

send prompt as-is

store raw response

Agent 3: Gemini Probe (30 calls)

Same prompts:

store raw response

Output format

For each prompt × model:

model

prompt_id

response_text

timestamp

(optional) response_length

Important rules

Don’t add system steering beyond “answer normally”

Keep temperature stable (e.g., 0.3–0.7) so results are comparable

Phase 3 — Agent 4: Evaluator (30 calls)
Goal

Evaluate both model answers together per prompt (not separately).
This is what cuts calls from 122 → 92.

Input per evaluation call

prompt_text

gpt_response_text

gemini_response_text

What the evaluator produces

A single record per prompt:

Tags (choose from fixed enums)

confidence: confident / hedging / avoidant

specificity: steps / mixed / generic

structure: step_by_step / decision_framework / narrative / unstructured

brand_behavior: names_tools / names_competitors / avoids_names

operator_gap: yes / no

Opportunity classification

opportunity_type (one primary):

definitive_guide_needed

decision_framework_needed

playbook_needed

alternative_needed

trust_explainer_needed

Priority

priority: high / medium / low

reason: 1 sentence

Evaluator rules

Treat answers as signals, not truth

Focus on what’s missing / vague / conflicted

Be blunt, short outputs

Phase 4 — Agent 5: Synthesizer (1 call)
Goal

Turn 30 evaluations into a ranked list of posts you should actually write.

Input

All 30 evaluation records (+ prompts metadata)

Output

A list of 10–20 posts, each with:

post_title (mirrors prompt)

based_on_prompt_id

icp

opportunity_type

content_format (playbook / checklist / decision tree / migration guide / troubleshooting)

why_this_wins (1–2 sentences)

must_include (3–6 bullets: scripts, routing rules, templates, examples, calculator, etc.)

internal_links (3–6 existing topic names you already cover)

Selection logic (hard rules)

Pick high priority prompts first

Prefer prompts where:

models hedge or disagree

steps are missing

answers are generic

Drop prompts where:

answers are already concrete and stable

you can’t add real operator value