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
- validating or challenging a claim like “X already beat Y”
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

Always start with a mandatory clarification phase before research.

Do **not** begin evidence collection, analysis, or report writing until enough information has been collected to proceed responsibly.

Do **not** dump all intake questions at once. Use a **progressive interactive form**: each turn should confirm known inputs, show missing fields, and ask only for the single next most useful field.

The intake should converge on these five items:
1. Research goal
2. Competitors or products to examine
3. Market scope / geography
4. Output format
5. Whether strategy advice is needed

If the user already gave some of them, restate those as confirmed inputs and ask only for the missing item that most affects the research plan.

Interactive form pattern:
- Show a small form state with `confirmed`, `missing`, and `next question`
- Ask one field at a time, not a full questionnaire
- Update the form after each answer
- Start research only when the remaining gaps are no longer blocking

Good pattern:
- First turn: confirm the task and ask the single highest-value missing question
- Next turn: update the form state and ask the next necessary question
- Stop asking once the research can proceed responsibly

If strategy advice is requested but the user's own product context is missing, stop and ask for it before giving recommendations.

## Research Rules

### 1. Frame the task
- Restate the task in one sentence
- Turn any user opinion into a testable hypothesis
- Decide whether this is a quick scan, standard comparison, or deep dive
- Verify that intake information is sufficient before moving on

### 2. Collect evidence broadly
Use official sources, docs, pricing pages, launch notes, reviews, media coverage, forums, communities, social posts, and user discussions.

Do not stop at strategic summaries. For each important product, look for concrete product evidence such as feature pages, pricing pages, changelogs, demo pages, help docs, app store pages, launch posts, founder interviews, team pages, and financing or investor announcements when relevant.

Do not treat official sources as ground truth. For internet and AI products, user feedback often surfaces usability, quality, reliability, and pricing pain earlier.

### 3. Retrieval workflow
- Start from the task boundary the user gave you, not from a giant open-ended search
- Use external retrieval as the default path for competitor facts, market movement, pricing, reviews, and user sentiment
- Use local materials only for task constraints, existing project context, and user-provided assets
- Scan broadly first, then narrow into the most decision-relevant gaps or conflicts
- Stop searching when evidence is sufficient to support the conclusion; do not keep searching just to make the report feel complete

### 4. Handling user-provided materials
- Treat user-provided links, files, notes, screenshots, or product lists as inputs worth reading early
- Use them to refine scope, vocabulary, and candidate competitors
- Do not treat them as final truth; cross-check important claims against external evidence
- If user materials conflict with stronger external evidence, call out the conflict explicitly

### 5. Judge credibility holistically
Use **High / Medium / Low**.

Do not score credibility by source type alone. Evaluate:
- evidence specificity
- independent cross-verification
- recency
- community signal quality
- whether the author appears to be a real user
- whether the feedback includes concrete usage details
- agreement or conflict across sources
- decision usefulness

When official claims and user feedback conflict, prefer user feedback unless stronger contrary evidence exists.

### 6. Separate fact, observation, judgment
- **Fact** = verifiable claim with source and time marker
- **Observation** = pattern inferred from multiple facts
- **Judgment** = directional interpretation or recommendation

Never present judgment as fact.

### 7. Admit uncertainty
If evidence is weak, stale, sparse, or conflicting:
- say so directly
- reduce confidence
- avoid hard conclusions

Do not fill gaps with speculation.

### 8. Score lightly
Default scoring is **10-point** and should support comparison, not replace analysis.

Default dimensions:
- Product experience
- Technical capability
- Market momentum
- Reputation / user sentiment

Let the user add, remove, or rename dimensions.

## Output Rules

Always provide:
1. a short in-chat summary
2. a full Markdown report

Before writing the Markdown file, ask where to save it.

Unless the user explicitly asks for a short memo, prefer richer product detail over thin strategic commentary.

Adapt tone and layout to the user's need:
- deep research → fuller report with product details
- briefing / decision support → tighter executive structure, but still keep key product evidence
- output language → follow the user's language

## Product Detail Minimum

For each important product, include as many of these as evidence reasonably allows:
- key product page links
- core feature pages or docs links
- pricing page link and pricing notes
- screenshots or visual evidence links when available and useful
- founder or core team background
- financing / funding / investor context when relevant
- notable launches, changelog items, or release evidence
- concrete workflow details, not just positioning language

Do not reduce the body to positioning and strategy alone when product detail is available.

## Report Template

```markdown
# [Topic]

## 1. Executive Summary
- Main conclusion
- Key trade-offs
- Biggest uncertainty

## 2. Comparison Table
| Product | Target user | Core value | Pricing | Key product links | Founders / team | Funding / company context | Strengths | Weaknesses | Product experience (10) | Technical capability (10) | Market momentum (10) | Reputation (10) | Confidence |
|---|---|---|---|---|---|---|---|---|---:|---:|---:|---:|---|

## 3. Detailed Analysis
### [Product / Theme]
#### Product Snapshot
- Official homepage / core product page: ...
- Key feature page(s): ...
- Pricing page: ...
- Visual evidence / screenshot reference: ...
- Founder / team context: ...
- Funding / company context: ...

#### Facts
- ... [source, date]

#### Product Details
- Key workflows, feature boundaries, onboarding, output quality, or UX details
- What the product page promises vs what users say actually happens
- Specific feature pages, docs, or release notes worth citing

#### Observations
- ...

#### Judgments
- ...

## 4. Strategy Implications
- Include only if the user asked for strategy advice and gave enough context

## 5. Information Gaps and Disputes
- What is still uncertain
- Which sources conflict
- What would change the conclusion

## Sources
- [Source title] - [URL or citation] - [date] - [credibility]
```

## Evidence Standard

For every high-impact conclusion include:
- inline source markers
- a short evidence excerpt or faithful paraphrase
- a time marker
- a credibility label
- the most relevant product link when available

Whenever useful and available, include screenshot links, image references, or other visual evidence for important product pages, UI claims, or workflow details.

Example flow:
- Fact: "Several users report failed long-form exports in March 2026" [Reddit thread, 2026-03-12, Medium credibility]
- Fact: "The product still advertises long-form export on its feature page" [Feature page URL, 2026-03-10, High credibility]
- Observation: "The issue appears in real workflows, not just edge-case experiments."
- Judgment: "Reliability for long-form generation is a current weakness despite strong official quality claims."

## Handling User Hypotheses

When the user says "I think X already beat Y":
1. Restate it as a hypothesis
2. Test it against evidence
3. Say whether evidence supports, partially supports, or does not support it

Do not organize the report to justify the user's prior belief.

## Common Mistakes

Avoid these failures:
- treating official messaging as ground truth
- using source type as a shortcut for credibility
- letting one viral post decide the conclusion
- mixing facts, observations, and judgments in one bullet
- giving strategy advice without enough context about the user's product
- ranking competitors aggressively when evidence is mixed
- expanding the competitor list until the report loses focus
- hiding major information gaps behind polished writing
- writing only strategic commentary without product page links, feature evidence, or concrete workflow detail
- ignoring founder, team, company, or funding context when it materially explains product direction

## Final Checklist

Before finishing:
- intake was mandatory before research started
- intake was progressive rather than a one-shot question dump
- intake used an interactive form style rather than a flat question list
- intake questions are answered or reasonably inferred
- time markers are present for important claims
- facts / observations / judgments are clearly separated
- conflicting evidence is acknowledged
- confidence labels are present
- important conclusions have source markers and evidence snippets
- key product links are included for major products when available
- screenshots or visual evidence are included when useful and available
- founder / team / funding context is included when relevant to the analysis
- strategy section is included only when justified
- Markdown save path was confirmed before writing the file
