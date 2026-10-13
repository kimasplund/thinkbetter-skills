# Report template and pre-delivery checklist

The checklist and every rule name stay backstage. The report shows the decision, the evidence and the numbers.

## Direct answer (small, cheap, reversible)

No headers and no other files. At most about 300 words: the pick; the one or two checks that actually matter, each concrete enough to act on; one sentence saying a full option analysis would be overkill here. Nothing else.

## Full report (desk synthesis or blind round)

```markdown
# Options: [decision]
**Decide by:** [date] · **Objective:** [number + date] · **Horizon:** [date]
**Assumptions I'm working from:** [only if gaps were filled]

## The recommendation
[The call in one sentence: adopt / keep the incumbent / inconclusive, and what to do this week.]
[Why, 3–5 lines. Chance it misses the objective by the horizon: ~X%, because …]
[One line on how it was compared: in one context, not blind | blind, N judges, decoy caught by …]
[If you generated or favour the recommendation, say so.]

## What the choice had to satisfy
[The pre-registered hard constraints, guards and value dimensions, verbatim or linked, with the
hash or commit that sealed them.]

## The field
| Option | In one line | Outcome |
[every option considered, the incumbent and the competent default included; outcome = finalist,
or cut and why]
**Considered and cut:** …

## How each finalist dies
### [Option]
**Strongest case:** …
**Killing modes:** … (~X%, because …) · … · …
**Chance it misses the objective:** ~X%, [reference class; one disanalogy line]
**Most dangerous:** … · **Hidden assumption:** … · **Cheapest falsifier:** [what, how, cost, days,
the result that kills it]
[repeat per finalist]
**What the whole field assumes:** [the shared root, or "no common root"]

## The comparison
| Dimension | [incumbent] | [A] | [B] | … |
[one row per dimension, guard rows marked; totals descriptive only]
[forced choice(s); margins against the noise; instrument notes]

## The combination
| Change | Taken from | Mode or gap it closes | What it costs | Interaction risk | How it would show |
**How the combination dies:** …
**Status:** recommended, not yet tested; adopt only if [arm-complete test] | tested in a fresh
blind comparison: [result]

## The decision rule
**IF** … **THEN** … **ELSE** …
**Cheapest decisive experiment:** [what, cost, days, and the readout that flips the call]
**Runner-up:** [option]; switch if [signal].
**If passing over the runner-up was the mistake:** [≤4 lines, past tense from the horizon, resolving
into the ELSE branch or "the call stands"]

## The tripwires
| Failure mode | Measurable signal | Threshold | Check on | If tripped |
**Kill condition:** [a combination, not one signal]
**What this analysis probably missed:** [one category, and why this frame under-weights it]
**Calibration review, [horizon date]:** score each predicted mode and the regret check; append,
never edit the original numbers.
```

If there is no combination worth making (every graft costs more than it closes, or the winner is strictly dominant), that part is one line saying so, with the reason.

## Pre-delivery checklist

Run it against the finished report. Fix what fails; do not ship a report that fails a line.

1. The pre-registration was written and sealed before any option existed, and the report cites the seal. No criterion was added or changed afterwards, or both readings are reported.
2. The level matches the stakes, or the user's choice was honoured with a one-line statement of what it cannot show. At most one sentence frames the stakes; nothing names the level.
3. The field has every slot or an N/A with a reason; the competent default is present; every pair of survivors differs in at least two diversity dimensions; every cut cites a hard constraint literally or states dominance dimension by dimension; nothing was cut for being unfamiliar.
4. Every finalist has a steelman, its own arithmetic, three past-tense killing modes that pass the stranger-paste test, shares on the ladder with justification clauses (`ladder_check` clean; the one tie, if any, with its written break), a chance of missing the objective with a reference class and a disanalogy line, the most dangerous mode, the hidden assumption and a falsifier with what, how, cost, days and the killing result.
5. The field's shared assumption is stated, or its absence is.
6. Scores are dimension-major with evidence; the incumbent is steelmanned; hard constraints and guards were checked literally; the adoption rule was applied exactly as written; INCONCLUSIVE was used where margins sit inside the noise; the blind or not-blind disclosure is present; in a blind round, the decoy result, position check and agreement are reported.
7. Every graft names the mode or gap it closes, its cost, its interaction risk and the observable; at most four; "how the synthesis dies" is present; the synthesis carries no scores from the round; its adoption test is arm-complete or a fresh blind comparison, and the noise band was applied to it as to any leader.
8. The call is in plain words; any irreversible step has an IF/THEN with the capability test first; the cheapest decisive experiment is present where required; the runner-up has a switching signal; the reverse autopsy is at most four lines and resolves into the ELSE branch or "the call stands".
9. Every tripwire has a metric, a threshold, a date on the user's timeline and a response; at most ten rows; the most dangerous mode has an early-chain row; the kill condition is a combination; the calibration review line carries its date.
10. The recommendation's final premortem ran in a fresh context (a sub-agent or a separate model call), or its refusal is disclosed with no retry; the interested-party disclosure is present if you generated or favoured the recommendation.
11. No reassurance paragraph; requested tone moved no number; every quoted statistic carries its source and year, or is marked weakly sourced.
12. Budgets and the length band are respected, and no block repeats another.
13. Mechanical leak scan: run `leak_scan()` over the final text. Rewrite each hit to name the content, or delete it (a numbered reference such as "tripwire 6" becomes the row's name); the project's own terms that happen to match (a "Gate 1", a "Stage 0", a founder "checklist") are content and stay. Ship at zero unrewritten hits.
