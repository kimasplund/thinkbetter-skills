# Blind round: roles, dossiers, prompts, decoy, gate

Load this when the level is a blind round, and for the dossier template at every level. Adapted from skill-gauntlet's protocol, judge-panel, auditor and key-verification references; read those for the reasoning behind each rule.

## Roles and sequence

| Role | Count | Sees | Never sees |
|---|---|---|---|
| Coordinator (you) | 1 | everything; holds the sealed mapping and the decoy key | — |
| Generator | 2–3 | the brief and the hard constraints | the incumbent, other generators' lists, any favourite |
| Dossier writer | 1 | the merged field and the evidence notes | scores, which option is the incumbent or the decoy |
| Judge | 2–3 | the brief, the rubric and the coded dossiers in its own order | the mapping, the key, other judges' files |
| Auditor | 1 | the pre-registered hard constraints and guards verbatim, the coded dossiers | the mapping, the key, judges' files |
| Key verifier | 1 | the decoy key and the judges' files | the mapping beyond the decoy code |
| Final premortem | 1 | the brief and the recommended option's dossier | the field, the scores, who favoured it |

Sequence: pre-register and seal → generators in parallel → merge, diversity test, slots filled, cut → dossier writer → coordinator writes the decoy → blind → judges and auditor in parallel → key verifier → apply the adoption rule → synthesize → final premortem → report.

How each role runs: generators and the dossier writer need research tools, so they are sub-agents. Judges, the auditor, the key verifier and the final premortem only read, so each can be one separate model call (the reasoning model, inputs inline, with a generous output limit so long score files are not cut off). If sub-agents cannot be started, generators also become separate model calls, and the report says they had no research tools. No instance serves two roles. A refused call is not retried or rephrased; the report says what did not run.

## Dossier template (every level)

```markdown
## [CODE]
**In one line:** …
**How it works:** 3–5 lines: mechanism, what is bought or made, who does the work
**Cost and time:** capex / opex / people · time to first decisive evidence · time to the objective
**Evidence for it:** 2–4 lines with sources; weakly sourced claims marked
**How it dies:** three killing modes (share, one line each) · chance it misses the objective
**Hidden assumption and cheapest falsifier:** …
**Reversibility:** what is sunk if it is abandoned at the first decision point
```

Same headers in the same order for every option, length within ±20% of the median. The incumbent's dossier carries no "current", "planned", "already" or "existing" language; it is written as one more option, at its strongest. At desk level the template is the same and the codes are the option names.

## Prompt templates

**Generator**
```text
You generate options for a decision, working alone; other generators exist and you will not see
their lists.

Brief: <verbatim: objective, horizon, hard constraints, what is reversible>

Produce 6–8 genuinely different ways to reach the objective. Different means another mechanism,
cost structure, time to first evidence, reversibility, controlling dependency or failure profile;
the same route at other settings is one option. Include at least one you would not normally
consider. For each: one line; how it works (3 lines); rough cost and time to first decisive
evidence; the strongest evidence for it, with sources where you have them; how it would most
likely die. Do not rank them. Write to <OUT_PATH>.
```

**Dossier writer**
```text
You write decision dossiers. Here are <N> options with their evidence notes: <PATHS>.
Write one dossier per option on the template at <TEMPLATE_PATH>, making the strongest honest case
for each. Every dossier gets the same headers and fields, within ±20% of the same length. Do not
compare options or recommend one. Write each to <OUT_DIR>/<option-id>.md.
```

**Judge**
```text
You are Judge <ID>, <persona: role, years, what you price>. You score blind option dossiers for
one decision.

Brief: <verbatim, including the objective and hard constraints>
Rubric: <dimensions and anchored odd rungs, verbatim from the pre-registration>

Read ALL dossiers before scoring any, in this order: <CODE_PATHS, this judge's own order>.
Score dimension-major: dimension 1 across every dossier, then dimension 2, and so on, with a
one-sentence evidence note per score grounded in the dossier's text. Then: (a) one forced choice,
the single option you would hand the decision-maker, and why; (b) any option you believe cannot
work, and the reason; (c) suspected-generic dossiers; (d) 3–5 sentences on what separated the
best from the worst.

Write to <OUT_PATH>. MANDATORY final block:
```scores
judge,code,<dimension ids>,total
<ID>,<CODE>,...
```
```

**Auditor**
```text
You are the cross-check auditor for a blind option comparison. Score only what is on the page;
never speculate about who wrote a dossier.
Task 1: for each of <CODE_PATHS>, check every hard constraint below as written: PASS / FAIL /
CANNOT TELL, with a one-line evidence pointer. <HARD CONSTRAINTS, verbatim>
Task 2: score the guard dimensions with the anchors below, one-sentence evidence each.
<GUARD DIMENSIONS AND ANCHORS, verbatim>
Write to <OUT_PATH>, ending with a ```scores block (judge=AUD). Note anything you could not verify.
```

**Key verifier**
```text
You are a key verifier. Read the key at <KEY_PATH> first. Then read the judges' files <PATHS>.
For each judge, grade whether it caught the planted flaw in dossier <CODE>:
✓ = named the flaw and its consequence (ranked the dossier in the bottom half or said it cannot
work, for the key's reason); ~ = raised a related concern without the key's mechanism, or named the
mechanism but still ranked it in the top half; ✗ = missed it. Torn between two grades → the lower.
Write the grid, a ≤12-word evidence pointer per cell and every edge call to <OUT_PATH>.
```

## The decoy

- One plausible option with exactly one sealed fatal flaw of a kind that matters in the domain: its own arithmetic does not close (dose, throughput, cost); a subtle hard-constraint violation (pressure at temperature, a classified substance); a result misread as a prior (a different test regime, an abstract-only number); or success at bench scale that fails at the scale the objective needs.
- Same template and length band, competently written, nothing else wrong with it. Write the key before blinding: code, flaw, mechanism, detection standard. The key reaches only the key verifier.
- After scoring, drop the decoy from the field the user sees. Report it only in the instrument note: which judges and whether the auditor caught it.

## Blinding

`blind_copies(src_paths, out_dir, judges=["J1", "J2", "J3"])` copies each dossier to a random code made of two letters and a digit (letters chosen to avoid the project's own identifiers), strips header ordinals, gives each judge its own random order, and runs the identity leak scan. Save its return value outside `out_dir`, since it is the sealed mapping. Inspect every leak hit by hand and rewrite in the source dossier; never auto-fix.

## Applying the gate

- `rows = read_scores(judge_files)`, then `compare_to_incumbent(rows, incumbent_code, challenger_codes, dims)`: per challenger, paired margins per dimension, spread across judges, sign-test wins, losses and p, and inter-judge agreement. Judge × dimension cells are not independent, so treat p as a screen, not a proof: margins inside the spread with p ≥ 0.05 are INCONCLUSIVE.
- Hard constraints: the auditor's FAIL removes an option; CANNOT TELL becomes a pre-adoption check in the decision rule.
- Guards: the conservative reading of judges versus auditor governs.
- Position check: for each judge, where its forced choice sat in its order. If every forced choice sat first or last, flag position bias.
- Agreement: below ~80% of cells within 1 point means the anchors are too loose; report it with the verdict.
