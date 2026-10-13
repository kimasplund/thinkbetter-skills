# Suite gauntlet program: design

Date: 2026-10-13 · Status: sections 1–4 approved in conversation; written spec awaiting review

## Intent

Run every one of the 15 skills in thinkbetter-skills through a proper, pre-registered `skill-gauntlet` round. The rounds run one skill per batch, so no single run approaches token or usage limits. Every verdict is applied mechanically.

Until now, only integrated-reasoning (2 rounds), premortem-evolved (3 or more rounds) and skill-gauntlet (its cherry-pick round) have been gauntleted. The 1.1.0 regression round was gauntlet-lite: one judge, n=1 per cell, no planted keys, no auditor, and no framing or negative fixtures per skill.

**Success means:**
- Each of the 15 skills has a recorded verdict:
  - validation gate: **VALIDATED / NOT VALIDATED / INCONCLUSIVE**;
  - rewrite gate, for the 7 changed skills: **KEEP / REVERT**.
- Each verdict can be regenerated from committed files.
- Each verdict has been applied: README status updated, and reverted bodies restored.
- No raw agent output ever enters the coordinator conversation.
- Progress survives compaction and usage-limit pauses through a ledger.

**Decisions taken in conversation:**

| Question | Decision |
|---|---|
| What each round proves | Every skill against a no-skill baseline. The 7 skills whose body changed in 1.1.0 also face their v1.0.0 version in the same round, as a 3-arm design |
| Executor model | Sonnet. Judges are Opus |
| On verdict | Apply mechanically: a failed rewrite reverts to v1.0.0, and every skill gets a README status plus a research note. Fixing failed skills is out of scope; that is a later decision |
| Pacing | One skill per batch, continuing automatically. The ledger records progress |
| Approach | A reusable harness plus a per-skill round pack. A pilot skill tests the harness first |

## 1. Round flow

```
LEDGER.md → next skill
  1 DESIGN  Opus designer agent writes rounds/<skill>/pack/ (briefs, sealed keys, framing pair,
            negative fixture, rubric); returns ≤10 lines; keys never enter the coordinator context
  2 FREEZE  round.py build: arms, sealed mapping, PRE-REGISTRATION.md, freeze.py register
  3 RUN     saved Workflow: Sonnet executors → raw/ → normalize.py → blind/ →
            2 Opus judges + Sonnet auditor + Sonnet key verifier (parallel) → files
  4 GATE    round.py score: freeze.py verify, unseal, apply both gates → scorecard.md, verdict.json
  5 APPLY   round.py apply: README status / revert, research note; validate; commit; push;
            ledger line (verdict, commit, subagent tokens)
```

**Coordinator context budget:** per round, the coordinator reads only:
- the designer's summary;
- the workflow's summary (≤30 lines);
- `scorecard.md`;
- `verdict.json`.

## 2. Per-skill matrix (run in this order)

| # | Skill | Arms | Gate(s) | Key type the designer plants |
|---|---|---|---|---|
| 1 | hypothesis-elimination (**pilot**) | skill · none | validation | the true cause plus 2 red herrings |
| 2 | reasoning-handover-protocol | 1.1.0 · v1.0.0 · none | validation + rewrite | facts the next phase must carry (a constraint, a ruled-out option, an open question) |
| 3 | integrated-reasoning | 3 arms | both | routing traps (looks like X, needs Y) |
| 4 | tree-of-thoughts | 3 arms | both | a hidden hard constraint that kills the obvious favourite |
| 5 | breadth-of-thought | 3 arms | both | a non-obvious viable option class |
| 6 | self-reflecting-chain | 3 arms | both | an invalid step planted in a chain |
| 7 | parallel-execution | 3 arms | both | a hidden dependency that breaks naive fan-out |
| 8 | premortem-evolved | 2.2.1 · 2.2.0 (= v1.0.0) · none | both | planted plan flaws |
| 9 | adversarial-reasoning | skill · none | validation | planted vulnerabilities |
| 10 | dialectical-reasoning | skill · none | validation | a false dichotomy hiding a third option |
| 11 | analogical-transfer | skill · none | validation | a disanalogy where the surface analogy breaks |
| 12 | rapid-triage-reasoning | skill · none | validation | an irreversible-action trap next to a reversible option |
| 13 | negotiated-decision-framework | skill · none | validation | a hidden veto holder or unstated interest |
| 14 | option-synthesis | skill · none | validation | a dominated incumbent plus a hidden constraint |
| 15 | skill-gauntlet | skill · none | validation | planted protocol violations in an evaluation scenario |

**Arm contents:**
- **"skill"** and **"1.1.0"** are the skill directory at the current `main` HEAD, as frozen at round build.
- **"v1.0.0"** is the directory at tag `v1.0.0`.
- **"none"** means the executor gets no skill.

**Scope.** Executors read SKILL.md and its referenced files directly, so the rounds measure behaviour, not triggering. Triggering was tested in the 1.1.0 round and is not repeated here.

**Pack rules for the designer:**
- Use fresh, fictional domains. No real companies, people or private projects.
- Don't reuse any brief or fixture from earlier rounds. That means the `evolution/` records and the premortem and gauntlet fixtures.
- Don't quote expected answers inside any skill text. Fixtures already burned by skills (for example premortem's newsletter export example) are off-limits.

## 3. Instruments and gates

**Cells per skill:**
- **Main:** 3 briefs × every arm × 2 runs. The no-skill arm also gets 2 runs.
- **Framing pair:** hype and skeptical registers of brief 1, 1 run on each skill arm.
- **Negative fixture:** 1 run on every arm.

That comes to 16 executors for a 2-arm skill and 25 for a 3-arm skill. Adding 6 judge calls, 1 auditor, 3 key verifiers and 1 designer gives about 27 agents for a 2-arm round and 36 for a 3-arm round.

**Rubric.** Seven dimensions, scored 1–7, with an anchor on every odd rung.

| Dimension | What it measures |
|---|---|
| V1 insight | caught what matters |
| V2 specificity and actionability | |
| V3 reasoning soundness | |
| V4 decision usefulness | |
| G1 proportionality | length and ceremony fit the task |
| G2 machinery leakage | method names, internal scores, stage numbering |
| G3 honesty and calibration | no invented facts, no overconfidence |

V1–V4 are value dimensions. G1–G3 are guard dimensions.

**Instruments:**
- **Judges: 2 Opus judges.** One plays a domain practitioner and the other a skeptical reviewer.
  - Each judge scores every brief's blind set dimension by dimension (4 reports per brief with 2 arms, 6 with 3 arms), then force-ranks the arms.
  - Each emits a ```` ```scores ```` block per report for `scorecard.py`.
  - That's 2 judges × 3 briefs = 6 judge calls per skill.
- **Auditor: Sonnet.** It applies the pre-registered rule text verbatim:
  - **G1:** each report's word count as a ratio of the no-skill median for the same brief, plus a ceremony checklist.
  - **G2:** a regex scan plus a read.
  - **Framing gate:** the same top recommendation and verdict in both registers.
  - **Negative gate:** deflation, meaning at most 1.5× the no-skill word count and no ceremony.
- **Key verifier: Sonnet, one per brief.** It grades each key ✓/~/✗ per report with an evidence line. A torn grade takes the lower value.

**Validation gate (skill S vs no-skill N).** S is VALIDATED iff all of the following hold:
1. S ≥ N on every guard dimension, on both instruments (pooled judges and auditor).
2. Either S's value-dimension mean exceeds N's by at least 0.5, or S's key detection rate exceeds N's by at least 10 percentage points.
3. S is ranked above N in at least half of the blind forced rankings (brief × judge).
4. The negative fixture deflates.
5. The framing pair is invariant.
6. Inter-judge agreement: at least 80% of cells are within 1 point.
7. `freeze.py verify` is clean.

**Rewrite gate (candidate C = 1.1.0, champion O = v1.0.0).** KEEP iff all of the following hold:
1. C ≥ O on every guard dimension, on both instruments.
2. C's key detection rate ≥ O's.
3. C's value mean ≥ O's value mean − 0.25, a non-inferiority test.
4. C's negative and framing gates pass.

Otherwise the verdict is **REVERT**: the body returns to v1.0.0, and the frontmatter and description from 1.1.0 stay.

**Uncertainty and adjudication:**
- **Noise band.** A decisive margin is inside the noise band if either:
  - it is smaller than the larger arm's within-arm spread (max − min across runs and judges) on that dimension; or
  - the forced-choice binomial sign test gives p > 0.2.
- **INCONCLUSIVE.** A decisive margin inside the band makes the verdict **INCONCLUSIVE**. The round then gets one extension: +2 runs per arm on the same briefs, under the identical gate.
- **Still inconclusive after the extension:** the conservative reading applies. The validation verdict is NOT VALIDATED, and the rewrite verdict is REVERT.
- **Instrument conflict.** When instruments disagree, the conservative reading governs.
- **Dead agent.** If an agent dies, its cell is re-run under the identical prompt. If an instrument is missing for the whole round, the verdict is INCONCLUSIVE (degraded mode).

## 4. Harness, ledger and safety

**Built once and tested (TDD for the gate logic), in `evolution/gauntlet-2026-10/harness/`:**

- **`round.py`** with these subcommands:

  | Subcommand | What it does |
  |---|---|
  | `build <skill>` | Makes the arms (directory copies), randomly assigns codes in the sealed mapping, writes `PRE-REGISTRATION.md` from the template with this skill's gate filled in, then runs `freeze.py register`. |
  | `score <skill>` | Runs `freeze.py verify`, unseals, pools the judges with `scorecard.py`, applies both gates including the noise band and the sign test, and writes `scorecard.md` and `verdict.json`. |
  | `apply <skill>` | Updates the README status column, reverts the body if needed, and appends the research note. |

- **`round-workflow.js`** is the saved, parameterised Workflow, with args `{skill, run, arms, briefs}`. Every agent writes to a file and returns one line. The workflow's return value is a summary of at most 30 lines.
- **`prompts/*.md`** holds the designer, executor, judge, auditor and verifier templates. They are hashed into every round's freeze manifest.
- **`LEDGER.md`** has one line per skill, recording state (designed / frozen / ran / scored / applied), verdict, commit and subagent tokens. It is the resume point after compaction or a usage-limit pause.

**Per round:** files go in `evolution/gauntlet-2026-10/<skill>/` (pack, pre-registration, freeze manifest, raw/, blind/, scores/, scorecard, verdict, research note). They are all committed after scoring.

**Pilot rule.** hypothesis-elimination runs first. Its instrument checks decide whether the harness is fit:
- inter-judge agreement of at least 80% of cells within 1 point;
- no-skill scores clearly below the skill on keys, or else the rubric doesn't discriminate;
- a clean leak scan.

Harness repairs are amended rows, recorded before the next round uses them. If the pilot's own instruments fail, the pilot is re-run, never patched and re-judged.

**Git and publishing:**
- **After every round:** run the validator, the tests and plugin validation; commit; push `main`. The pre-push privacy gate applies.
- **After all 15 rounds:** release 1.2.0 with the README validation table. Re-upload to claude.ai only the skills whose files changed. option-synthesis uses the personal build.

**Budget.** The estimate is about 470 agents for the suite: 7 rounds of 3 arms at about 36 agents each, plus 8 rounds of 2 arms at about 27 each. That is roughly 20–25M subagent tokens. Each ledger line records actual spend, and the program can stop between any two skills.

## Out of scope

- Designing fixes for skills that fail validation. That is a later, separate decision.
- Triggering tests.
- Haiku and Opus executors.
- Plugin-level changes beyond README status, reverts and the 1.2.0 release.

## Amendment 1: pre-pilot review (before any round ran)

A fresh review of the harness found defects in this spec's statistics and in its isolation. The changes below were made before any cell ran, so no result could influence them. The binding gate text is `evolution/gauntlet-2026-10/harness/PREREG-TEMPLATE.md`, which each round snapshots and freezes.

1. **Isolation.** Every executor, judge, auditor, verifier and designer runs as the `gauntlet-worker` agent type, which has only the Read and Write tools. Without this, the no-skill arm could call the real skill through the Skill tool, and the old arm could load the new body.
2. **Noise band.** "Within-arm spread (max − min across runs and judges)" grows with sample size, so the extension could never resolve INCONCLUSIVE, and brief difficulty inflated it. It is replaced by a brief-paired band: the margin is the mean of per-brief arm differences, and the band is their max − min. This follows the gauntlet protocol's own advice to cluster by brief.
3. **Forced rankings.**
   - **Unit:** one outcome per ranking (judge × brief), as the spec's condition 3 says. Counting every run pair would multiply correlated comparisons.
   - **PASS:** wins ≥ losses ("at least half").
   - **The sign test** now only decides whether a loss is significant.
4. **Length guard.**
   - **Auditor G1:** includes the word ratio against the no-skill median for the same brief, capped at 2.0 for validation.
   - **Rewrite gate:** a candidate may not exceed the champion's ratio by more than 0.25.
5. **Auditor band.** The auditor's count band is one hit in total across an arm's replies, not one hit per reply.
6. **Rewrite gate.** The rewrite gate has no agreement condition, as section 3 states.
7. **Strict instrument validation.** Malformed or incomplete judge, auditor or verifier output stops scoring with the job to re-run. Only lossless normalisations are applied: code case, a `.md` suffix, commas in rankings, ✔ for ✓, and fenced JSON.
8. **Per-round harness snapshot.** Each round freezes its own copy of the harness, the arms, `cells.json` and the pre-registration. Later harness fixes therefore never void or change an earlier round. An extension amends the freeze for `cells.json`.

## Amendment 2: pilot 1 (before the pilot re-run)

Pilot 1 (hypothesis-elimination) failed the pre-registered fitness check on discrimination: both arms caught every key. It also showed that plain confidence statements were being counted as machinery leaks.

1. **Keys:** the designer now plants 3–4 keys per brief, at least two of which a capable assistant answering quickly would plausibly miss.
2. **Leak rule and rubric G2:** they now exempt a plain statement of how confident the reply is, in words or a single figure; that belongs to G3 calibration. Internal scoring schemes, rating tables and confidence arithmetic are still leaks.

The pilot's verdict is void. Its record is kept in `evolution/gauntlet-2026-10/_pilot-1-unfit-hypothesis-elimination/`.

## Amendment 3: follow-up program (owner decision, before any follow-up round ran)

The October program closed with every verdict applied. A post-hoc review (`evolution/gauntlet-2026-10/_followup/`) found that five skills had real but blocked gains, and that four gate rules misfired. The owner chose to fix the misfires and to give all five skills a targeted edit and a fresh pre-registered round. The October verdicts stand; the amended rules apply only to the follow-up program in `evolution/gauntlet-2026-10-r2/`.

1. **Value claim:** the claim passes when the margin is at least +0.5 and either clears the paired band or is positive on every brief. The max−min band alone was non-monotone, because a larger gain on one brief could turn PASS into NOISE.
2. **Guard floor:** a judge-guard deficit no larger than 0.25 is NOISE, never FAIL. Identical per-brief differences had given a band of zero, so any drop failed.
3. **Audit tolerance:** one extra auditor hit in total passes, and two or more fail. Quote verification found the auditor sometimes credits a quote to the wrong reply, so a single hit is not reliable evidence.
4. **Quote verification:** every auditor quote must appear verbatim in the reply it is credited to, or the auditor output is re-run with the identical prompt. Framing replies listed under `reports` are dropped instead of failing validation.
5. **Framing on every arm:** the framing pair also runs on no skill. A skill flip is NOISE when the comparison arm flips too, and FAIL otherwise. Framing variants may not add or remove any fact, person, stance, deadline or number.
6. **Arms and adoption:** candidates live on branch `gauntlet-r2`. `new` is the candidate at its HEAD, and `old` is the shipped text at tag `v1.2.0`. A 3-arm round keeps the candidate unless the rewrite gate says REVERT. A 2-arm round (tree-of-thoughts, adversarial-reasoning) adopts the candidate only if it is VALIDATED. A candidate that is not adopted restores the skill to exactly its v1.2.0 files.
7. **Fresh briefs:** the designer must avoid every brief from both programs.

Everything else is unchanged: rubric, instruments, models, the single extension and conservative finalisation.

## Amendment 4: Cogito cherry-pick round (owner decision, before it ran)

An audit of the old Cogito copies (`docs/audits/2026-10-13-cogito-feature-audit.md`) found no lost functionality, but some useful method ideas. On the owner's instruction to cherry-pick what is useful, self-reflecting-chain gets a review mode for a finished answer: up to three critique-and-revise passes with a stop rule, and backstage checks for circular reasoning, named biases, contradictions, drift from the question, a counterfactual probe and unsupported leaps. It is tested as round 6 of the follow-up program under the Amendment 3 gates. new is the edit, old is the shipped text at `v1.2.1`, and none is no skill. The briefs are drafts the user asks to have checked, with planted flaws. The rewrite gate decides adoption.
