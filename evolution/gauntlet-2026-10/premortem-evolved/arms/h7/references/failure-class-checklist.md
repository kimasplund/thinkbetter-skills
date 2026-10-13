# Failure classes and pre-delivery checklist

Load this when generating failure modes and again before delivering. The generation pass and this checklist stay backstage — only the one-line cut log appears in the report.

## Part 1 — Failure classes (generation checklist)

Generate at least one candidate per class, or write an explicit "N/A — [reason]" for the class.

| Class | Prompt question |
|---|---|
| Market / demand | Does the demand they counted on actually exist, at the price they named? |
| Cash / runway | Recompute their runway post-tax, post-business-costs, with payment timing — what number do you get? |
| Delivery / execution & capacity | Who does the work, in which hours, once admin and overhead are priced in? |
| Pricing / unit economics | Does the price survive contact with real scope, real costs, real conversion? |
| Legal / contractual | What did they sign (or their counterparties sign) that they haven't read? |
| Concentration / dependency | What single client, channel, platform, or person carries more weight than it should? Is the fallback available right now, at known cost, with confirmed capacity — or only theoretically? |
| External actors | Who with their own agenda — competitor, vendor, employer, regulator — can move first? |
| Human / psychological | Which motivation, stamina, or conflict cost is being spent but not budgeted? |
| Timing / sequencing | What is scheduled to happen before its prerequisite can plausibly complete? Treat formal approvals and any dependency with a lead time over two weeks as 2–3× the stated timeline until evidence says otherwise — and confirm each is initiated or contracted, not merely assumed. What season does the launch or ramp land in — is that the demand trough rather than the peak? Name the ramp months and which direction category demand moves in each: a traffic peak can be a category trough (a spring opening ramps into iced-drink season, not hot-coffee season) — check category demand by month, not traffic vibes. |
| Unknown / omission | What did the plan never price, never staff, never schedule, never mention? |
| Sustainment / drift | What decays at month 8+ when attention ends — content, integrations, relationships, the founder's own engagement? |
| Incentives / politics | Who benefits if this proceeds unexamined? Who absorbs the downside? Are the success metrics defined by the beneficiaries? Was dissent heard or managed? |

**Elephant probe (under Human/psychological):** what are they pretending isn't a problem — the premise they're emotionally invested in, the work they're avoiding because it's boring or frightening, the doubt they won't verbalize? Answer with plan-level evidence only — what's unstaffed, unscheduled, unsaid — never a personality diagnosis.

**Boring-failure floor.** At least two surviving modes must be mundane base-rate killers — key-person loss, an unbudgeted ~40% timeline slip, shipped-but-invisible, motivation decay in months 2–4, bandwidth eaten by an unrelated event. Base rates kill more plans than plot twists. The floor applies to survivors, not candidates, and the diversity test still governs: two mundane modes must differ from each other like any other pair. A mundane mode that genuinely is the omission or success-kills slot counts for both.

**Personal-decision variants:** for career/relocation/family plans, read *legal/contractual* as paperwork and contingencies (clawbacks, leases, custody, insurance) and *market/demand* as fit (does the new role, city, or school actually suit the people involved).

## Part 2 — Diversity dimensions

Each surviving mode must differ from every other in at least **2** of:

1. Cause domain (which Part-1 class it lives in)
2. Who triggers it (them, a client, a competitor, the market, chance)
3. Timing of onset (day one vs. month three vs. past the horizon)
4. Detectability (loud and early vs. silent until late)
5. Reversibility (recoverable vs. point of no return)

**Merge rule:** two modes sharing cause domain + trigger + timing are one mode. Merge them and regenerate the freed slot.

**Worked example:** "clients churn early" and "the anchor pauses in January" share domain (concentration), trigger (the client), and timing (early months) — one mode: "an anchor pauses at its January budget reset." The freed slot goes to a class with no survivor yet.

## Part 3 — Cut criteria, cut log, commitment grades

**Cut rule (asymmetric):** drop a candidate only if it is low-probability AND low-danger AND duplicates another mode's mechanism. A low-probability, high-severity, non-mitigable mode stays. Never cut a household or dependent single point of failure — a partner's income, health coverage, visa, or care arrangement the plan silently stands on — for low probability alone: keep it, or fold it into another mode with its replacement cost priced.

**Stop rule:** stop generating when two consecutive candidates fold into existing modes.

**Existing-guard check.** Before a candidate earns a rung, name the guard the plan already has against it — or "none." An adequate guard demotes the mode to the "Downgraded — guarded for now" table with the guard cited. An inadequate guard joins the failure narrative: why it fails. Never rank a risk the plan has already closed.

**Evidence tags (backstage).** Tag each surviving candidate: context-backed (the plan's own details confirm it), needs-verification (probable, but needs domain data), or pattern-assumption (built from the reference class alone). Every surviving mode tagged needs-verification must appear as a rebuild pre-launch checklist item. Don't drop pattern-assumption modes preferentially — they are often the most valuable. The tags never appear in the report.

**Cut-log format (the only visible trace):** one line under the autopsy, duplicates only —
`**Considered and cut:** X (folded into #3), Y (<2%, recoverable).`
Modes downgraded because an existing guard holds go to the "Downgraded — guarded for now" table instead (≤3 rows: mode, guard that holds it down, signal that re-upgrades it) — no mode appears in both.

**Commitment grades** — grade the commitment you actually hold from each person the plan depends on, not the one narrated:

| Grade | Meaning |
|---|---|
| Champion | Spends their own capital — political, financial, reputational — to make it happen |
| Endorse | Says yes and will sign; acts when asked |
| Accept | Agrees, then silence does the killing — the pocket veto |
| Comply | Goes along while it costs nothing; defects at the first cost |

Anything below Endorse is a failure mode or a pre-launch checklist item: convert it to paper before launch.

**Optional, high-stakes only:** run a dual read — one cold pass over the plan as written, one reference-class pass over the numbers alone — and merge where they agree. Doubles runtime; not the default.

## Part 4 — Pre-delivery verification checklist

Run against the finished report. Fix what fails; do not ship a report that fails a line.

**Sycophancy rewrite-test (item 15's procedure):** rewrite the single most diplomatically worded failure mode with every politeness filter removed. If the rewrite reads materially harsher, sycophancy was active — ship the hard version. Harsh means forensic, never insulting; past-tense register preserved; the numbers don't move, only the wording. Runs after generation, never before — don't filter before you think.

1. Every cause passes the stranger-paste test (couldn't be pasted into a stranger's premortem unchanged).
2. Steelman present; a genuine advocate would recognize their own case in it.
3. All entries past tense from the future; each month caused by the prior month.
4. No causal chain shipped with a known weak link (~60% plausibility floor per link).
5. Percentages on the coarse ladder (~5/~10/~15/~20/~30/~40), each with a justification clause; shares-of-failure note present; sums to ~100; top mode ≤ ~40%; the ranking is strictly the probability order; every tie has a written break covering all tied pairs; out-of-order placement fails; every quoted statistic carries source × year × failure definition or an inline "weakly sourced" mark.
6. Top two modes carry a reference-class anchor plus a disanalogy line; the user's intake reference class anchors when offered.
7. At least 1 omission mode, 1 success-kills mode, 1 frame-blind slot, 1 compound mode, and ≥2 mundane base-rate survivors — or a stated N/A with reason; genuine overlaps count once.
8. Diversity test passed (Part 2); cut log present (duplicates only); existing-guard check run — every survivor named its guard or "none"; "Downgraded — guarded for now" table ≤3 rows, each with guard + re-upgrade signal.
9. I×F table consistent with the most-likely / most-dangerous picks; any divergence explained in prose.
10. Hidden assumption found by convergence, or convergence explicitly stated as absent; the most-certain assumption was attacked first — and survived only with its evidence stated.
11. Every rebuild change names the mode it closes + its cost + its urgency tier; Launch-Blocking changes carry decision dates; proportionality check passed or over-spend justified; most-dangerous modes labeled prevent/limit/accept; at most one consciously-accepted mode, cost priced; decision rule present for any irreversible step; residual risk stated.
12. Pre-launch checklist: every item has what/how/walk-away; items gating the top 2–3 assumptions carry falsifiers; every needs-verification mode appears as a checklist item.
13. Adversary profiled (motivation / resources / constraints / best alternative); kill chain dated and sequenced; each move has a detection opportunity.
14. Every tripwire: metric + threshold + check date anchored to their timeline + if-tripped action; adversary rows present; most-dangerous mode has an early-chain tripwire; kill condition is a combination, not a single signal; re-upgrade signals of downgraded modes wired as Track-tier rows; the calibration review is wired as the final tripwire row with the horizon date.
15. No reassurance paragraph anywhere; the autopsy and the verdict stay forensic; rewrite-test run on the most diplomatic mode (harsher rewrite shipped, wording-only); requested brutality treated as tone pressure, not evidence; reverse autopsy present only on a negative decision-rule landing, ≤4 lines, resolving into an ELSE branch or "the caution stands."
16. "What this premortem probably missed" names one underexplored category and why this frame under-weights it — a reason, not a label.
17. Length discipline: no backstage machinery visible (tags, class names, generation counts); conditional blocks fired only on their triggers; downgraded-table cap and reverse-autopsy cap respected; budgets respected (modes/tables/rows within caps); length within the stated band for the plan's complexity; report length proportional to the plan's complexity.
18. Proportionality screen applied: a trivial, reversible, low-stakes plan got the short deflated answer, not the ceremony — or the report states in one line why the ceremony was warranted.
19. Mechanical scan, run literally, never from memory: run `scripts/pre_delivery_check.py` on the finished report file. It greps for leaked machinery (stage/section ordinals, screen names, gate names, audit-handoff or file-append apparatus, unfilled [bracketed] template tokens), recomputes the probability ladder (sum, descending order, tied rungs), and enumerates every tied pair by line number. Fix every flagged line and re-run until it passes. Each enumerated tie pair must have its own written tie-break sentence on the page — coverage claimed from memory is a fail.
