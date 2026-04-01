---
name: competitive-research
description: Use when the user needs competitor research, product comparison, market scan, pricing comparison, substitute analysis, positioning analysis, or validation of a competitive hypothesis for internet or AI products, including 竞品调研/竞品分析. Trigger when the user is comparing tools, substitutes, market moves, differentiation, or competitive positioning, even without saying "competitor research".
---

# Competitive Research

## Overview

Run evidence-led competitor research for internet and AI products. Start with intake, then separate facts, observations, and judgments.

## When to Use

Use this skill for:
- comparing products, tools, SaaS, AI products, or workflows
- mapping direct competitors and substitutes
- scanning pricing, positioning, strengths, weaknesses, or momentum
- validating or challenging a claim like "X already beat Y"
- preparing a competitor memo, table, or briefing for product or strategy work

Do not use this skill for:
- opinion-only asks with no evidence requirement
- coding, UI review, implementation, or architecture work
- stock analysis, valuation, or investment research

## Quick Reference

| Item | Default |
|---|---|
| Focus | Internet + AI products |
| Geography | Global |
| Time window | Prioritize last 3 months |
| Competitor set | Direct competitors + substitutes |
| Auto-supplement | Up to 5 additional products |
| Credibility | High / Medium / Low |
| Conflict rule | Prefer user feedback over official claims unless stronger contrary evidence exists |
| Retrieval priority | External retrieval first; local materials only for task constraints, existing context, and user-provided assets |
| Intake mode | Mandatory progressive interactive form before research |
| Output | In-chat summary + Markdown report |
| File writing | Ask save path first |
| Scoring | 10-point, lightweight, configurable |

## Intake First

Always start with a mandatory clarification phase before research. Do **not** begin evidence collection, analysis, or report writing until enough information has been collected.

Do **not** dump all intake questions at once. Use a **progressive interactive form**: each turn confirms known inputs, shows missing fields, and asks only the single next most useful field.

Converge on five items:
1. Research goal
2. Competitors or products to examine
3. Market scope / geography
4. Output format
5. Whether strategy advice is needed

If the user already gave some, restate as confirmed and ask only the missing item that most affects the research plan.

Interactive form pattern:
- Show form state with `confirmed`, `missing`, and `next question`
- Ask one field at a time; update form after each answer
- Start research only when remaining gaps are no longer blocking

If strategy advice is requested but the user's own product context is missing, stop and ask for it.

## Research Rules

### 1. Frame the task
- Restate the task in one sentence; turn any user opinion into a testable hypothesis
- Classify as quick scan, standard comparison, or deep dive

### 2. Collect evidence broadly
Use official sources, docs, pricing pages, launch notes, reviews, media, forums, and user discussions. Go beyond strategic summaries—look for concrete product evidence: feature pages, pricing, changelogs, demos, app store pages, founder interviews, funding announcements.

Do not treat official sources as ground truth. User feedback often surfaces usability, quality, and pricing pain earlier.

### 3. Retrieval workflow
- Start from the task boundary the user gave, not an open-ended search
- External retrieval is the default; local materials only for task constraints and user-provided assets
- Scan broadly first, then narrow into decision-relevant gaps or conflicts
- Stop when evidence is sufficient; do not keep searching to pad the report

### 4. Handling user-provided materials
- Read user-provided links, files, notes, or screenshots early to refine scope and vocabulary
- Cross-check important claims against external evidence
- If user materials conflict with stronger external evidence, call out the conflict explicitly

### 5. Judge credibility holistically
Use **High / Medium / Low**. Evaluate by evidence specificity, independent cross-verification, recency, community signal quality, whether the author is a real user with concrete details, and agreement or conflict across sources.

When official claims and user feedback conflict, prefer user feedback unless stronger contrary evidence exists.

### 6. Separate fact, observation, judgment
- **Fact** = verifiable claim with source and time marker
- **Observation** = pattern inferred from multiple facts
- **Judgment** = directional interpretation or recommendation

Never present judgment as fact.

### 7. Admit uncertainty
If evidence is weak, stale, sparse, or conflicting: say so, reduce confidence, avoid hard conclusions. Do not fill gaps with speculation.

### 8. Score lightly
Default: **10-point**, four dimensions (Product experience, Technical capability, Market momentum, Reputation / user sentiment). Let the user customize. Scoring supports comparison, not replaces analysis.

## Output Rules

Always provide: (1) a short in-chat summary, (2) a full Markdown report.

Before writing the Markdown file, ask where to save it. Unless the user asks for a short memo, prefer richer product detail over thin strategic commentary.

Adapt tone to the user's need:
- deep research → fuller report with product details
- briefing / decision support → tighter executive structure, but still keep key evidence
- output language → follow the user's language

## Product Detail

For each important product, capture as many items as possible from the checklist in `docs/methodology.md`. Key items: product page links, feature pages, pricing, screenshots, founder/team, funding, workflow details, launch evidence.

Never reduce the body to positioning and strategy alone when product detail is available.

## Report Template

Use `templates/research-report.md` as the base structure. Key sections:
1. Executive Summary
2. Comparison Table
3. Detailed Analysis per product (Product Snapshot → Facts → Product Details → Observations → Judgments)
4. Strategy Implications (only if user asked and gave enough context)
5. Information Gaps and Disputes
6. Sources

For single-product deep dives, use `templates/competitor-profile.md`.

## Evidence Standard

For every high-impact conclusion include: inline source marker, short evidence excerpt or faithful paraphrase, time marker, credibility label, and the most relevant product link. Include screenshot links or visual evidence when useful.

Example: "Several users report failed long-form exports in March 2026" [Reddit thread, 2026-03-12, Medium credibility]

## Handling User Hypotheses

When the user says "I think X already beat Y":
1. Restate it as a hypothesis
2. Test it against evidence
3. Say whether evidence supports, partially supports, or does not support it

Do not organize the report to justify the user's prior belief.

## Common Mistakes

- treating official messaging as ground truth
- letting one viral post decide the conclusion
- mixing facts, observations, and judgments in one bullet
- giving strategy advice without enough context about the user's product
- ranking competitors aggressively when evidence is mixed
- expanding the competitor list until the report loses focus
- hiding major information gaps behind polished writing
- writing only strategic commentary without product links or concrete evidence

## Final Checklist

- [ ] intake was progressive, not a one-shot question dump
- [ ] time markers present for important claims
- [ ] facts / observations / judgments clearly separated
- [ ] conflicting evidence acknowledged
- [ ] key product links included for major products
- [ ] founder / team / funding context when relevant
- [ ] strategy section only when justified
- [ ] Markdown save path confirmed before writing
