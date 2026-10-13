---
name: option-synthesis
description: "Find and build the best option for a decision instead of grading the first idea. Pre-registers what the choice must satisfy, generates a wide field of genuinely different options (the status quo and the competent default included), kills weak ones with short premortems, compares finalists against the frozen incumbent (blind when the stakes warrant it), and synthesizes the winner with grafts that close its failure modes. Delivers the recommendation, the runner-up, the cheapest decisive experiment, a decision rule and tripwires. Use when choosing between approaches, routes, materials, formulations, designs, equipment, test plans or strategies, e.g. 'what are our options', 'which should we pick', 'best way to', 'compare these approaches', 'is there something better than the current plan', 'design the best X'. Composes premortem-evolved and skill-gauntlet. Not for stress-testing one finished plan (use premortem-evolved) or a candidate skill revision (use skill-gauntlet)."
metadata:
  version: "1.0.0"
---

# Option Synthesis

Asking "what should we do?" pulls for the first plausible answer, and whoever proposed it then defends it. Three failures follow. The first option on the list is rarely the best one available. The favourite gets judged by criteria written after it appeared, so they fit it. And a combination of two good options is assumed to beat both without anyone testing it. This skill keeps apart the three things that usually get fused (deciding what the choice must satisfy, generating options, judging them) and synthesizes only from options that survived a written attempt to kill them.

It adapts two skills from one object to a field of options. **premortem-evolved** supplies how an option dies: steelman first, failure classes, the coarse probability ladder, falsifiers, decision rules, tripwires, the calibration review. **skill-gauntlet** supplies how a challenger must beat an incumbent: pre-registration, blinding, a frozen champion, conjunctive guards, planted flaws, generic controls, INCONCLUSIVE, symmetric loss. Load each when its part runs; this file says what changes when the object is a set of options. Both stay as shipped: never edit them to fit this workflow.

## Four rules that never bend

1. **Pre-register before you generate.** From desk synthesis up, hard constraints, guard dimensions, value dimensions, the incumbent, the horizon and the adoption rule are written to a file before any option exists, and sealed: in a git repository commit it and cite the commit; where committing is not allowed, cite its SHA-256 or md5. Afterwards the text decides. If a bar turns out mis-set, report both readings; the pre-registered one governs this decision and a corrected bar applies only to a future one. Criteria written after the favourite appeared are fitted to it.
2. **Generation and judgment never share a context, or the page says they did.** In a blind round, generators see only the brief and the hard constraints; judges see anonymised, format-matched dossiers, each judge in its own random order; only the coordinator knows which dossier is the incumbent, a favourite or the decoy. In a desk synthesis one context does both, and the report says so: "compared in one context, not blind".
3. **The incumbent is frozen and may win.** What happens if nothing changes is written up once, at its strongest, and is not improved during the round. A challenger replaces it only by clearing every hard constraint and every guard. "Keep the current plan" and INCONCLUSIVE are first-class verdicts; "no change, and here is the experiment that would change it" is a deliverable, not a failure.
4. **A synthesis is a new candidate.** A hybrid built after the scores were seen inherits none of them; re-judging a patched candidate on the same run is goalpost movement. It is adopted only after its own test, and only if it beats each parent, not just the incumbent. A combination that beats the incumbent but not its better parent is that parent with extra cost.

## Proportionality: decide the level at intake

Size the stakes before generating anything.

- **Direct answer.** Small, cheap and reversible: a file layout, a meeting cadence, a returnable purchase, a like-for-like replacement part. Give the pick, the one or two checks that actually matter, and one sentence saying a full option analysis is overkill, in at most about 300 words. Then stop. A direct answer writes no pre-registration and no field; the answer is the only file. Short is not enough; the checks must be real gotchas, not filler.
- **Desk synthesis.** Real money or weeks of work, but reversible or stageable. The full workflow below in one context, with a written pre-registration and dimension-major scoring, disclosed as not blind.
- **Blind round.** An irreversible commitment, capital the project would feel, safety or regulatory exposure, or a favourite someone is invested in, including you. Independent generators, one dossier writer, 2–3 persona judges, an auditor and a decoy, per [references/blind-round.md](references/blind-round.md). Generators and the dossier writer need research tools and run as sub-agents; judges, the auditor and the key verifier only read, so each can be one separate model call. Say what the round will cost before starting.

A user may choose the level; honour it and state in one line what the lower level cannot show. On a close call, say which way you went and why, in one line. When the full treatment runs, the level leaves no trace on the page beyond at most one sentence framing the stakes.

## Intake: get the decision specific enough to choose

- **The objective** as a number and a date: what "best" is for.
- **The incumbent**: what happens if nothing changes. There always is one; "do nothing" counts.
- **Hard constraints** as checkable statements: budget, equipment envelope, safety, regulation, time, skills.
- **What is reversible**, what is not, and the pain threshold (the spend or delay the project would feel).
- **Who decides, and whose commitment the options lean on**, graded champion / endorse / accept / comply as in premortem-evolved.
- **The reference class**: what similar choices chose and how they ended.
- **What was already tried or ruled out, and why.** A ruled-out option re-enters only with its reason restated as a checkable claim.

If two or more are missing, ask once, in one batch. If told to just run it, proceed and open the report with **Assumptions I'm working from**.

**Domain packs.** If `references/<project>.md` exists for the project, load it now. It supplies standing hard constraints, guard dimensions, evidence rules, reference classes, judge personas and the domain form of each option slot. The project's own current files override the pack; flag any disagreement on the page.

## Pre-register the choice

Write `preregistration.md` before generating:

```markdown
## Pre-registration: [decision], [date]
- Objective: [number + date] · Horizon: [date] · Level: [direct / desk / blind round], because [one line]
- Incumbent (frozen): [one paragraph, at its strongest]
- Hard constraints (violation removes the option; checked literally): H1 …, H2 …
- Guard dimensions (a challenger must be ≥ the incumbent): G1 …, G2 …
- Value dimensions (anchored 1/3/5/7 rungs; weights only if set now): V1 …, V2 …
- Adoption rule: a challenger replaces the incumbent iff ALL of: every H passes; ≥ incumbent on
  every G (the conservative reading when instruments disagree); value margin ≥ [floor] with no V
  more than [δ] below the incumbent; its premortem leaves no unmitigated fatal flaw; [blind round]
  the decoy was caught by the instruments that count.
- Synthesis rule: a hybrid is adopted only after [a fresh blind comparison | an arm-complete test:
  hybrid vs each parent vs incumbent at matched cost or dose], and only if it beats each.
- INCONCLUSIVE: if the leader's margin over the runner-up or the incumbent sits inside [noise band],
  no pick is forced; the deliverable is the cheapest experiment that separates them.
- What would change the call: [evidence named in advance]
```

Use 5–8 dimensions. Guards are where a regression is fatal: safety and do-no-harm, a hard cost or time ceiling, reversibility. Value dimensions are where options compete: expected performance against the objective, time to first decisive evidence, cost, learning value (what the option teaches whatever the outcome), fit with the people and equipment. Anchor every odd rung with observable behaviour (skill-gauntlet `references/judge-panel.md`). Totals describe; the conjunctive rule decides.

## Generate the field

**Slots.** Every field carries these, or an explicit N/A with a reason:
- the **incumbent**;
- the **competent default**: what a capable practitioner would pick first without this process. It is the generic control; if the search cannot beat it, the search added nothing, and the report says so;
- the **cheapest fast option**: the least that tests the core belief;
- a **different mechanism**: the objective reached by another physical, chemical, commercial or organisational route, not a parameter change;
- **buy, partner or outsource**: someone already does this;
- **staged**: a sequence that buys information before the irreversible step;
- the **habit-excluded option**: ruled out by custom rather than by a stated constraint. It is the field's blind spot, as the premortem keeps a frame-blind slot.

A blind round adds a decoy written by the coordinator. It is an instrument and never enters the field the user sees.

**Generate 10–15 candidates** (in a blind round, 2–3 independent generators of 6–8 each, blind to each other and to any favourite). Stop when two consecutive candidates fold into existing ones. Before an option earns a place, record what the literature, patents and the project's own notes say about it. A claim that carries weight in the ranking and cannot be sourced is marked weakly sourced. If the domain moves fast (prices, lead times, regulation), run one dated search before fixing numbers.

**Diversity test.** Every surviving option differs from every other in at least two of: mechanism; cost structure (capex, opex, people); time to first decisive evidence; reversibility; who controls the critical dependency; failure profile (how it would die). Two options sharing mechanism, dependency and failure profile are one option at two settings: merge them, keep the better setting as a parameter, and refill the slot. Seven variants of one route is one option wearing seven hats.

**Cut to 3–6 finalists plus the incumbent**, for only two reasons: a hard-constraint violation, checked literally and cited, or dominance (another option is at least as good on every dimension and better on one, stated dimension by dimension). Never cut an option for being unfamiliar. A long shot that is cheap to test stays, or becomes the staged option's first experiment. One line in the report: `**Considered and cut:** X (H2: needs 12 MPa), Y (dominated by C on every dimension).`

## Kill the finalists

Give each finalist, the incumbent included, a short premortem under premortem-evolved's rules (past tense from the horizon, the stranger-paste test, causally chained, no reassurance) at reduced size:

- **Steelman**: 2–3 lines a real advocate would recognise.
- **Its own arithmetic first**: cost, throughput, timeline, dose, capacity. If it misses the objective on its own numbers, that is its top killing mode, stated as arithmetic.
- **Three killing modes**, ranked, each with a share on the coarse ladder (~5/~10/~15/~20/~30/~40) and a justification clause, the cause, and the first warning sign. The three need not sum to 100; the rest is everything else. At least one per option is a mundane base-rate killer (a slip, a lead time, a key person, shipped-but-invisible); at least one success-kills mode appears somewhere in the field. If one mode would take more than half, say the option is dominated by that single risk instead of forcing a number.
- **Chance it misses the objective by the horizon**, on the ladder extended upward (~5/~10/~20/~30/~50/~70/~90), anchored to a reference class with one disanalogy line. This number compares across options; the shares do not.
- **Most dangerous mode**: silence × irreversibility.
- **Hidden assumption and cheapest falsifier**: what to check, how, the cost, the days, and the result that kills the option.

Check each ladder with `ladder_check(ranked, complete=False)`: descending, on the ladder, at most one tie, a tie spans exactly two modes, and the tie carries a written break. The ranking follows the arithmetic and the reference class; requested enthusiasm or brutality is tone, not evidence. Model only what decides the call: when one number (a lead time, a dose, a yield) decides it, compute that number; otherwise the ladder is enough.

Then find **the field's hidden assumption**: compare the finalists' mechanisms pairwise. The belief most of them share as a root is the one that, if false, kills the whole field together. If it is untested, testing it comes before choosing among them.

The recommendation's final premortem never runs in the context that chose it. After the comparison, a fresh context receives only the brief and the recommended option's dossier (not the scores, the field or who favoured it) and runs the short premortem above: a sub-agent, or where you cannot start one, a separate model call with only those inputs. It runs the full premortem-evolved instead when the recommendation contains an irreversible step above the pain threshold or the level is a blind round. If you generated or favour the option, say so on the page: you are the interested party.

**If a fresh-context call is refused** by a content filter, do not retry, rephrase or reroute it. Say on the page what was requested and that it did not run, and leave the next step to the user.

## Compare against the incumbent

- **One template for every dossier** ([references/blind-round.md](references/blind-round.md)): the same headers and fields, length within ±20% of the median, because length and format are tells. The incumbent is written at its strongest, not as a straw man.
- **Score dimension-major**, one dimension across all dossiers and then the next, with a one-sentence evidence note per score; then one forced choice ("which one would you hand the decision-maker?") and a suspected-generic call.
- **Desk synthesis:** you score in one pass, and the page says not blind. **Blind round:** 2–3 persona judges, crossed so every dossier gets at least two, each in its own random order; an auditor applies the hard constraints and guards literally, quoting the pre-registered text verbatim; a key verifier grades whether each judge caught the decoy's sealed flaw. The conservative reading governs a guard when judges and auditor disagree.
- **Apply the adoption rule exactly.** With few judges the margins are small-N: `compare_to_incumbent()` gives margins, between-judge spread and a one-sided paired sign test per challenger across judge × dimension cells. A margin inside the band without one-directional dominance is INCONCLUSIVE, not a narrow win, and the same band applies to every leader, a synthesis included. If forced choices track presentation order, flag it.
- **Report instrument failures; never hide them.** A judge who ranks the decoy in the top half is recorded. If every instrument misses the decoy, the round did not discriminate, and the report says so.

## Synthesize

Start from the winner, or the incumbent if it held. For each of its top killing modes and its weakest value dimension, look across the other finalists for a component that closes it:

| Graft | Taken from | Mode or gap it closes | What it costs | Interaction risk | How the interaction would show |

- No graft costs more than the mode it closes is expected to cost: an order-of-magnitude check, not arithmetic.
- Each graft is a new assumption. Parts interact, and in physical systems often antagonistically (additives competing for the same surface, process steps competing for the same reagent). Name the mechanism and the observable.
- At most four grafts. A synthesis that needs more is a different option; send it back to the field.
- **How the synthesis dies:** 2–4 lines naming the new weakest joint the grafts introduced, or state that the synthesis is strictly dominant, and why.
- **Its adoption is gated separately** (rule 4). Either a fresh blind comparison (new judges; synthesis vs winner vs incumbent; the same pre-registered rule; at desk level, at least one separate model call scoring coded, format-matched descriptions, disclosed as written by the interested party), or it ships as *recommended, not yet tested*, gated by an arm-complete test: the synthesis against each parent and the incumbent at matched cost or dose, one-sided per comparison.
- **When the leaders share their first step** (the same purchase, the same experiment), the call can be to take that step now and decide the rest at its readout, with the decision rule naming what the readout must show.

## Decide and instrument

- **The call**, in plain words: adopt [option], keep the incumbent, or inconclusive (run [experiment]).
- **Decision rule** for any irreversible step, as IF/THEN, with the risky capability test sequenced before the commitment. Never split the difference between two options without arguing why the blend does not inherit the worst of both.
- **The cheapest decisive experiment**: what, cost, days, and the readout that flips the call. Required when the verdict is inconclusive or the field's hidden assumption is untested.
- **The runner-up and its reverse autopsy:** "We didn't choose [runner-up], and by [horizon] that was the mistake, because …", at most four lines, resolving into the decision rule's ELSE branch or "the call stands".
- **Tripwires**: metric, threshold, check date on the user's timeline, and the response decided now. One per killing mode of the chosen option, plus the signal that switches to the runner-up; at most ten rows; the most dangerous mode gets a row early in its causal chain; the kill condition is a combination.
- **Calibration review on the horizon date**: score each predicted mode (materialised / didn't / can't tell) and the regret check (with what is known then, would the runner-up have been better?). Append; never edit the original numbers.

## Delivering

Use the report template and run the pre-delivery checklist in [references/report-template.md](references/report-template.md). Write the report to a file; in a project repository, follow its note conventions. The checklist ends in a mechanical leak scan, `leak_scan()` over the finished text and never from memory: the report shows findings, not the machinery (no stage, step, section or phase numbers cross-referencing the report; no numbered references to rows or assumptions, which are named instead; no slot, level or rule names; no generation counts). A project's own terms that happen to match, such as a "Gate 1" or a "Stage 0", are content and stay.

Budgets: at most six finalists plus the incumbent; three killing modes each; four grafts; ten tripwire rows; four lines of reverse autopsy. A desk report runs about 2,500–4,500 words, a blind round about 3,500–5,500 plus its instrument annex. Length is not thoroughness: every block adds information not already on the page, or it goes.

Close with one ask, as premortem-evolved does: which decision or experiment will they commit to, and by which day? Record `**Committed:** … by …` or `**Declined:** … (reason)` in the file. Ask once.

## Operating rules carried over (each cost a round to learn)

- **The restraint case is the most informative one.** Every revision of a method drifts toward more ceremony; check that small decisions still get small answers.
- **A compliance failure is not a design failure.** A run that skipped a rule its siblings followed needs a checklist fix; a method that cannot produce the right content needs redesign. Log which one you saw.
- **Don't chase a single cell.** If every instrument misses the same decoy the same way, the decoy was badly built: document it. Tuning the method to it teaches to the test.
- **Absolute bars are usually unattainable.** Pre-register relative-to-incumbent bars plus floors.
- **Namespace hygiene.** Option codes, judge IDs and dimension names stay disjoint, and disjoint from the project's own identifiers.
- **Operational guards.** When the choice feeds a purchase or a protocol, cost and schedule are guard dimensions.
- **No instrument sees another's work.** Judges never see each other's scores, and no sub-agent serves two roles.

## Helpers

Loaded with this skill (`kernel.py`): `ladder_check(ranked, complete=True)`, `leak_scan(text, extra=None, blind=False)`, `blind_copies(src_paths, out_dir, judges, seed=None)`, `read_scores(paths)`, `compare_to_incumbent(rows, incumbent, challengers, dims)`, `sign_test_p(wins, losses)`.

*Adapted from premortem-evolved v2.1 and skill-gauntlet (MIT, © 2026 kimasplund; see LICENSE). Version 0.1 (2026-09-29): smoke-tested on one desk decision and one trivial fixture, with the fixes from that test applied but not re-run; not yet run through skill-gauntlet.*
