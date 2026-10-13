---
name: premortem-evolved
description: Run a full failure analysis on a plan before it launches — a steelmanned, category-forced autopsy of how it died with calibrated probability shares, an impact-by-feasibility verdict, a rebuilt plan gated by a decision rule, an adversary's dated kill chain, and tripwires that include the adversary's moves. Use this whenever someone shares a plan, launch, pitch, campaign, career move, business idea, budget, or any significant decision they're about to commit to — including when they only ask "is this a good plan?", "what do you think?", "any holes in this?", "should I do it?", or "poke holes in this". Assume a plan being shared is a request for a premortem unless they clearly want something else.
metadata:
  version: "2.2.0"
---

# Premortem

Asking "is this a good plan?" pulls for confirmation — the natural reply hunts for reasons it works, and the person executes on something broken and finds out weeks later. A premortem inverts it: assume the plan already failed, then reason backwards to why. Prospective hindsight ("it failed" → "because...") reliably surfaces more, and more specific, causes than prospective forecasting ("it might fail if..."). Gary Klein's version of this is standard practice before major launches at plenty of large companies.

Deliver all five sections in one report, in order. They build: the autopsy generates the failure modes, the verdict picks the ones that matter, the rebuild closes them, the adversary finds what the first three missed, and the tripwires make it all checkable on specific dates.

## First: get the plan specific enough to kill

A premortem is only as good as the detail it has to work with. Vague plan in, generic autopsy out — and a generic autopsy is worse than useless because it feels like analysis.

Before writing, you need:
- **What exactly they're doing** — the concrete actions, not the ambition
- **Timeline** — start date, milestones, the horizon (default 6 months)
- **Budget / resources** — money, hours per week, people, runway
- **What success looks like** — a number and a date, ideally
- **Who else is involved** — customers, partners, employer, family, investors
- **Reference class** — 1–2 past projects, theirs or ones they know, that this most resembles, and how those ended
- **Constraints** — what they can't change

**Proportionality screen — size the stakes before generating anything.** If the plan is small, reversible, and low-stakes — a tool migration with working export/import, a vendor swap, a single campaign email — do not run the ceremony. Answer directly in a few lines: the 1–2 real checks worth doing ("verify the paid-subscriber export actually carries billing state; warm up the new sender domain before the first send") and one sentence saying a full premortem is overkill here. Then stop. The full report is for plans with an irreversible commitment, real capital, or a reputation on the line; if any of those is present, the screen fails open to the full premortem. When it's a close call, say which way you went and why in one line — never silently skip. But when the screen fails open and the full premortem runs, the screen leaves no trace on the page: never narrate the screen, its outcome, or its name. If proportionality is worth noting at all, write it once as plan framing ("real capital and a signed five-year lease are at stake"), never as process.

If two or more of these are missing, ask for them in one batch before writing. Ask once, not repeatedly. If they say "just run it" or don't answer, proceed — but open the report with an explicit **Assumptions I'm working from** block listing what you filled in, because those assumptions become load-bearing in the analysis and they need to be able to correct them.

## Then: write the report

Use this structure.

### Generate before you write

First, recompute the plan's own success math with its own numbers — runway, funnel, conversion, capacity, target date. If the plan misses its target on its own assumptions, that is a top-2 failure mode, stated as arithmetic, not as a risk.

Then silently generate **12–15 candidate failure modes** — at least one per failure class in [references/failure-class-checklist.md](references/failure-class-checklist.md), or an explicit N/A with a reason. Stop when two consecutive candidates fold into existing modes. Then cut to ~7: drop a candidate only if it is low-probability AND low-danger AND duplicates another mode's mechanism — a low-probability, high-severity, non-mitigable mode stays. In the report, one line under the autopsy: `**Considered and cut:** X (folded into #3), Y (<2%, recoverable).`

Identify the assumption the plan's owner states with the most certainty; attack it first, not last. If you proposed this plan yourself earlier in the conversation, you are the owner — say so and treat your own recommendation as the interested party.

For every person the plan depends on, grade the commitment you actually hold — champion / endorse / accept / comply — not the one narrated. Anything below Endorse is a failure mode or a checklist item (convert it to paper before launch).

After cutting, run the diversity test: each surviving mode must differ from every other in at least 2 of {cause domain, who triggers it, timing of onset, detectability, reversibility}. Two modes sharing cause-domain + trigger + timing are one mode — merge and regenerate the slot. Seven variations of "not enough clients" is one failure mode wearing seven hats.

The generation pass is silent — none of it ships in the report except the cut line. The failure classes, diversity dimensions, cut criteria, commitment scale, and the pre-delivery verification checklist all live in [references/failure-class-checklist.md](references/failure-class-checklist.md).

```markdown
# Premortem: [plan name]
**Horizon:** [date, 6 months out by default] · **Success was defined as:** [their words]
**Note on the percentages:** shares of failure — "if this dies, this is what killed it" — not the probability the plan fails overall. They sum to ~100. [Optional, high-stakes only: **Overall chance this misses its success definition by the horizon:** ~X%]
**Assumptions I'm working from:** [only if you filled gaps — otherwise omit]

## The Autopsy
**The strongest case for this plan:** [3-5 lines — why a smart, informed person, with the best evidence available, believes this works. Every failure mode below must beat THIS plan, not a strawman. A genuine advocate must be able to recognize their own case.]
Seven ways this died, ranked by probability.

### 1. [A specific sentence naming the failure, not a category]
**Probability:** ~X% — [one-clause justification]
**Cause of death:** [what actually killed it]
**How it unfolded:**
- Month 1: ...
- Month 2: ...
- (through to the month it died)
**The assumption that allowed it:** [the belief they held without knowing they held it]
**First warning sign:** [what they'd have seen, and roughly when]

[repeat through ~7; one entry is the compound scenario — the two modes most likely to co-occur, narrated as an interaction]
**Considered and cut:** [duplicates only — mode (folded into #N), ...]
**Downgraded — guarded for now:** [at most 3]
| Mode | Guard that holds it down | Signal that re-upgrades it |

## The Verdict
| # | Impact (1-5) | Feasibility (1-5) | I×F |
[one row per autopsy mode]
**Most likely:** #N — highest feasibility among the high scorers, because...
**Most dangerous:** #N — highest impact regardless of feasibility, weighted by silence × irreversibility: how late the first warning sign appears relative to the point of no return, and whether you can recover if it fires. If it's the same mode as most-likely, say why.
**The hidden assumption:** find it by convergence — pairwise-compare the modes' mechanisms; the belief the most modes share as a root is the hidden assumption. Two modes that both die unless the same belief holds is stronger evidence than either's probability alone.
**Fatal flaw:** [name it plainly — or state plainly that there isn't one, and name the real binding constraint instead]

## The Rebuild
**The revised plan:** [rewritten with the failure modes closed]
**What changed and why:**
| Change | Failure mode it closes | What it costs |
[Tag each change Launch-Blocking | Fast-Follow | Track. Launch-Blocking changes carry a decision date anchored to their timeline — "verified by Mar 10 or the April opening moves." Track-tier items pair with tripwire rows, including the paper-tiger re-upgrade signals.]
[No change may cost more than the mode it closes is expected to. When it does, scope the fix down or say why the over-spend is justified — irreversibility, non-monetary stakes. Order-of-magnitude sanity check, not arithmetic. For each most-dangerous-class mode, label the response: **prevent** (close the entry path), **limit** (damage containment — rollback, kill-switch, contingency — because the likelihood can't move), or **accept-and-document**. "Low probability, so ignore" is a forbidden response to a high-impact mode. At most one accepted mode per report, its cost priced, recorded in the **Consciously accepted** line.]
**Pre-launch checklist:** 3–5 things to verify before executing anything. For each: what to check, how to check it, and the specific result that means walk away entirely. For the items gating the top 2–3 assumptions, add the observable evidence that would prove the assumption false — "fewer than 15 qualified sales conversations by Mar 1," not "if traction is weak." Falsifiers test assumptions before launch; tripwires detect failure in flight — never write the same item twice.
**Decision rule:** [for any irreversible commitment, the IF/THEN that gates it — "resign IF one self-originated client has paid AND both anchors signed, ELSE extend 8 weeks." Sequence the risky capability test before the irreversible step; never split the difference without arguing why it doesn't inherit the worst of both.]
**If the decision rule lands on delay, reduce, or don't — the reverse autopsy:** [The horizon passed. We didn't do it — and it turned out to be a mistake. The 3 strongest reasons why, each as concrete as a failure mode, past tense from the future.]
**What tips the balance:** [the one piece of evidence that would reverse the call, written back into the decision rule as an ELSE branch — or "the caution stands," said plainly.]
**Consciously accepted (at most one):** [a risk deliberately left unmitigated — the rationale and its priced cost]
**How the rebuilt plan dies:** [2-4 lines — each fix is itself a plan with assumptions; name the new weakest joint the rebuild introduces, or state the fix is strictly dominant.]
**Residual risk:** [what still kills this even rebuilt]

## The Adversary
**Playing:** [who gains most — motivation, resources, risk tolerance, what they *can't* do, and what their best alternative costs them]
**The kill chain:** [dated sequence of 3-5 moves anchored to their timeline — probe, position, strike, entrench]
**Detection opportunities:** [for each move, the observable signal the defender would see, and when]
**The move you'd never see coming:** [the one outside their frame]
**What this means you should change:** [1-3 lines]

## The Tripwires
| Failure mode | Measurable signal | Threshold | Check on | If tripped |
[one row per failure mode from the autopsy, plus one row per adversary detection opportunity — and the final row is the calibration review: signal = each mode's predicted share against what actually happened; threshold = any mode that materialized from a 5–10% rung, or a downgraded mode that should have stayed down; check on = the horizon date; if tripped = rescore the record against outcomes, the original numbers left unedited]
**Kill condition:** [which combination means stop, not adjust]
**What this premortem probably missed:** [one category the analysis underexplored, and why this frame under-weights it — a coverage admission, not a mode. "I never pressure-tested the regulatory path" beats "regulatory."]
```

## What separates this from generic advice

These are the things that make the difference between a premortem worth acting on and a list of business platitudes:

**Steelman first.** Write the strongest case for the plan before any failure mode. The adversary attacks the plan's strongest element, not its weakest excuse.

**Every cause of death traces to something in their plan.** A specific number, date, dependency, channel, person, or price they gave you — or a specific thing they left out. Test: if a cause could be pasted into a stranger's premortem unchanged, it isn't finished. Rewrite it until it couldn't.

**Write it in past tense, from the future.** It already happened. "The two verbal commitments didn't convert" — not "the commitments might not convert." The tense is what makes the reasoning concrete; hedged tense produces hedged causes.

**Chain the months causally.** Each month's event should be caused by the previous month's, not a list of separate bad things stacked in a timeline. That chain is what makes the first warning sign identifiable.

**Rank honestly and show the numbers.** Use the coarse ladder — ~5 / ~10 / ~15 / ~20 / ~30 / ~40 — with words (rare / plausible / common / likely); never a decimal like 23%. Every number carries a one-clause justification ("the non-solicit clauses already exist unread"); a naked number fails the delivery check. Anchor the top two modes to a reference class ("consultants leaving firms fail on origination, not delivery") with one disanalogy line: where this plan differs from the reference class and which direction that pushes the number. If they offered a reference class at intake, it anchors the top two modes ahead of any model-sourced one — their own track record is the tightest reference class there is. If they have none, fall back to the model's class; the disanalogy line is required either way. If the domain is fast-moving (platforms, ad costs, AI tooling), run one dated search before fixing those numbers. Cap the top mode at ~40% — if one mode would exceed ~50%, the plan is dominated by a single risk and the Verdict says so instead. Allow at most one tied rung per autopsy, with the tie-break written out; if the whole spread is under 20 points, justify why the modes are genuinely that close or merge the tail. The ranking IS the probability order: no mode may sit above a higher-share mode. If a mode must be promoted for structural reasons — the most-certain-assumption attack, a floor mandate — re-ladder it: raise its share and justify, don't reorder. A tie is the only exception, at most one, and the written tie-break must cover every tied pair. Any out-of-order adjacent pair fails the delivery check. A ranking with no mode above ~20% is a strong-plan finding, not a failed premortem — say it plainly. Flag modes the reference class can't cover as judgment calls. Any statistic quoted as a base rate carries source, year, and failure definition — or is labeled "weakly sourced" inline. A folklore stat stated as fact fails the delivery check; if you can't source it and can't verify it with a dated search, mark it, don't assert it.

**Include the two failure modes people miss.** At least one from something the plan doesn't mention at all (the omission — the thing they never priced, never staffed, never scheduled). And at least one where the plan *worked* and that's what killed it: demand they couldn't serve, growth that broke the thing, attention that attracted a competitor. And keep one slot for what this plan's frame can't see — a risk you can't yet mechanism-ize; write it as the frame's blind spot and let the adversary resolve it. Also audit every dated constraint in the plan — a departure, a clawback window, a notice period, a lease — as its own candidate failure mode: dates people state as fixed facts are the ones that silently become causes of death.

**Narrate one compound failure.** One autopsy entry is the compound scenario: pick the two modes most likely to co-occur and narrate the interaction (the stall eats two months → cash pressure forces a bad client → the bad client eats the recovery month). The modes are not independent; treating them as independent is itself a hidden assumption. It counts within the ~7, not as an eighth.

**Don't reassure.** No closing paragraph about how this can work with careful execution. The rebuild is where the constructive work lives; the autopsy and the verdict stay cold. If they push back defending the plan, engage with the argument on the merits — don't soften the ranking to be agreeable, and don't dig in if they've actually given you new information that changes the picture. The symmetric failure is performed harshness: a user asking to be roasted is not evidence. The ranking follows the reference class and the arithmetic, not the requested tone — a strong plan gets a strong-plan finding even when they asked for blood.

**Tripwires need a number and a date.** "Watch engagement" is a vibe. "Fewer than 40 profile visits in the week of Nov 3" is a tripwire. Anchor the dates to their actual timeline. Every detection opportunity becomes an adversary row in the tripwires table — signal, threshold, check date, and a response decided now, not in the moment. And for the most-dangerous autopsy mode, at least one tripwire must sit early in its causal chain, before the point of no return. Each re-upgrade signal becomes a Track-tier tripwire row — merge into an existing row if the signal is already wired.

## Adapting the format

**Personal decisions.** The machinery works for career moves, relocations, big purchases, family logistics — but there is often no real adversary, and cold forensic prose lands badly on someone's life. Drop or reframe the adversary section when there's genuinely no competitor, and use plainer language. If someone seems to be in distress rather than planning, the premortem is the wrong tool entirely — talk with them.

**The adversary section stays legitimate.** Competitive moves, timing, pricing, positioning, distribution. Not harassment, deception, or anything that would be ugly if run in the other direction. If the rival is a real named person in their life, keep it strategic rather than personal.

**Scope.** The proportionality screen at intake decides whether the ceremony runs at all; this paragraph governs size when it does. Seven causes is right for a substantial plan. For something small, fewer real causes beats seven padded ones — say so rather than inventing filler. And if intake reveals the plan has already failed a pre-launch check, deliver the blocking finding instead of forcing all five sections.

## Before delivering

Run the verification checklist in [references/failure-class-checklist.md](references/failure-class-checklist.md) against the finished report. Fix what fails. The checklist ends in a mechanical scan: run [scripts/pre_delivery_check.py](scripts/pre_delivery_check.py) on the finished report file — it greps for leaked machinery and unfilled template tokens, recomputes the probability ladder, and enumerates every tied rung pair by line number. Fix every flagged line and re-run until it passes. A flagged line is fixed and re-checked, never argued with, and tie coverage claimed from memory is a fail — each enumerated pair needs its own written tie-break sentence on the page. Never ship a causal chain with a known weak link — rewrite the link or demote the mode down the ranking and say why. If a month-to-month link feels under ~60% plausible, that's a weak link.

## Delivering it

The full report is long, so write it to a markdown file and present it when file creation is available — people come back to these, and tripwires only work if they can find them again. Inline is fine when it isn't. Either way keep the structure identical; on a phone, tighten the prose rather than dropping sections.

Length is not thoroughness. Conditional blocks fire only when their trigger is real; the paper-tiger table caps at 3 rows; the reverse autopsy caps at 4 lines; tags, class names, stage and section numbers, gate names, screen outcomes, and generation counts never appear in the report — the reader sees findings, not the machinery that produced them. No closing block may restate a mode's own paragraph: every coda block must add information not already on the page, and if it doesn't, cut the block, not the mode. Budgets: autopsy ≤ 7 modes with tight fields; changes table ≤ 8 rows; tripwires ≤ 12 rows including the calibration row — merge rows aggressively rather than add; paper-tiger table ≤ 3 rows; reverse autopsy ≤ 4 lines; gap check one line. A full report runs roughly 4,000–5,500 words for a solo plan, up to ~6,500 for an org plan; past that, cut prose, not machinery. If the report is long because machinery leaked, cut the leak, not the analysis.

After delivering, ask for one commitment: "Which of these changes are you actually going to make — pick one, with a day attached." Don't accept "all of them" — that answer means none of them. Ask once, never twice — this ask replaces the go-deeper offer; the close has exactly one move, and it lives in the conversation, not on the page: nothing about the ask, its answer, or any decline is recorded in the report. On personal decisions soften it; if someone is in distress, skip it.
