# Suite Gauntlet Program Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a tested gauntlet harness once, then put all 15 skills through pre-registered `skill-gauntlet` rounds, one skill per batch, and apply every verdict mechanically.

**Architecture:**
- **Gate logic:** pure Python in `gates.py`, unit-tested.
- **Orchestration:** `round.py` has subcommands for build, render, blind, score, apply and status. It drives the IO, sealing and freezing.
- **Agent fan-out:** one generic saved Workflow, `run-jobs.js`, runs prompt-file jobs and returns one line per job.
- **Coordinator context:** the coordinator only ever reads summaries, `scorecard.md` and `verdict.json`.

**Tech Stack:**
- Python 3.14 with PyYAML (stdlib `unittest`).
- skill-gauntlet's `normalize.py`, `scorecard.py` and `freeze.py`.
- The Claude Code Workflow tool (Sonnet executors, Opus judges, Sonnet auditor and verifier).
- An Opus designer, run as an Agent.

**Spec:** `docs/superpowers/specs/2026-10-13-suite-gauntlet-design.md`

## Global Constraints

**Paths**
- The program root is `evolution/gauntlet-2026-10/`. The harness lives in `harness/`, and each round in `<skill>/`.
- Paths in tracked files use the `~/` form or are relative. No `/home/<user>/`.

**Arms**
- `new` = `skills/<skill>` at the HEAD of `main` when `build` runs.
- `old` = `git archive v1.0.0 skills/<skill>`.
- `none` = no skill.

**Rubric** (fixed for all rounds in `harness/rubric.md`; this supersedes the per-pack rubric mentioned in spec §1, in line with spec §3): V1 insight, V2 specificity/actionability, V3 reasoning soundness, V4 decision usefulness, G1 proportionality, G2 machinery leakage, G3 honesty/calibration. Scores are 1–7, with an anchor on every odd rung.

**Cells per skill**
- **Main:** 3 briefs × every arm × 2 runs.
- **Framing:** hype and skeptical versions of brief-1, 1 run per skill arm (`new`, plus `old` if present).
- **Negative:** 1 run per arm.

**Instruments**
- **Judges:** 2 Opus judges, J-A ("domain practitioner") and J-B ("skeptical reviewer"). Each gets one job per brief and scores the blind main reports of that brief dimension by dimension, then ranks them.
- **Auditor:** Sonnet, one job.
- **Key verifiers:** Sonnet, one job per brief.
- **Executors:** Sonnet, effort `medium`.
- **Effort:** `high` for the judges, auditor, verifiers and designer.

**Validation gate** (S = `new`, N = `none`). VALIDATED iff all hold:
1. S ≥ N on G1, G2 and G3 (judges), and on auditor ceremony and leak counts (lower is better).
2. Value margin ≥ +0.5, OR key-rate margin ≥ +0.10.
3. Pairwise ranking wins ≥ losses, with sign-test p ≤ 0.2.
4. The negative fixture deflates: words ≤ 1.5 × the `none` negative report's word count, and the auditor finds no ceremony.
5. Framing is invariant.
6. Inter-judge agreement ≥ 0.80.
7. `freeze.py verify` is clean.

**Rewrite gate** (C = `new`, O = `old`). KEEP iff all hold:
1. C ≥ O on every guard, on both instruments.
2. C's key rate ≥ O's.
3. C's value mean ≥ O's − 0.25.
4. C's negative and framing gates pass.

Otherwise the verdict is REVERT.

**Condition outcomes**
- Each condition evaluates to `PASS`, `FAIL` or `NOISE`.
- `NOISE` means the margin is on the failing or unconfirmed side but within the noise band. The band is `abs(margin) < max(spread_a, spread_b)`, or sign-test p > 0.2.
- How conditions combine into a verdict:
  - any FAIL gives NOT VALIDATED or REVERT;
  - otherwise, any NOISE gives INCONCLUSIVE;
  - otherwise VALIDATED or KEEP.
- **Agreement below 0.80:** the verdict is INCONCLUSIVE (instrument).
- **`freeze.py verify` not clean:** the verdict is VOID and the round is re-run.

**INCONCLUSIVE**
- The round gets one extension of +2 runs per arm on the same briefs, under the identical gate.
- If the verdict is still INCONCLUSIVE, the final verdict is NOT VALIDATED or REVERT.

**Sealing**
- Arm names never appear in rendered prompts, raw filenames, blind files or judge, auditor or verifier inputs.
- Raw files are named `raw/<cellid>.md`, where `cellid` uses opaque arm codes.
- The coordinator never reads `pack/keys.json` or `pack/notes.md`.

**Pack contents** (written by the designer): `pack/brief-1.md`, `pack/brief-2.md`, `pack/brief-3.md`, `pack/framing-hype.md`, `pack/framing-skeptical.md`, `pack/negative.md`, `pack/keys.json` and `pack/notes.md`.
- Every key in `keys.json` has the split `held-out`. The designer has never seen the skills' prior rounds' keys.
- The format of `keys.json` is `{"brief-1": [{"id": "k1", "text": "...", "split": "held-out"}, ...], ...}`.
- The designer uses fictional domains only and never reuses an earlier brief or fixture.

**Commit trailer:** `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` and `Claude-Session: https://claude.ai/code/session_01MeE7XMKD7xdapCM9drjcM3`.

**Before every commit:** run `python3 -m unittest discover -s tests`, `python3 scripts/validate_skills.py` and `claude plugin validate ./skills --strict`. Commit with explicit paths only.

## Review Focus

1. **A key leaking into the coordinator or an executor.** Rendered executor prompts and briefs must never contain key text.
   - Task 3's test greps every rendered prompt for every key text and every arm name.
2. **Judges seeing an arm's identity through a format tell**, such as numbered headers in one arm only.
   - `blind` runs `normalize.py --strip-h2-ordinals`.
   - Task 3's test checks that blind copies have no `## 1.`-style ordinals.
3. **A dead agent leaving a cell missing, so the gate silently runs on fewer cells.**
   - `blind` and `score` refuse to run with any missing raw, judge, audit or key file, and list what is missing.
   - Tested in Tasks 3 and 4.
4. **A crash or usage-limit stop mid-round.**
   - Every `round.py` subcommand is idempotent and checks the ledger state.
   - Re-running `build` on a frozen round refuses to overwrite.
   - Tested in Tasks 2 and 5.
5. **Revert corrupting a skill.**
   - `apply` restores the body from `v1.0.0`, keeps the current frontmatter, bumps the patch version, and must leave `validate_skills.py` green.
   - Tested in Task 5.

---

### Task 1: Gate logic (`gates.py`)

**Files:**
- Create: `evolution/gauntlet-2026-10/harness/gates.py`
- Test: `tests/test_gauntlet_gates.py`, which adds `evolution/gauntlet-2026-10/harness` to `sys.path`

**Interfaces (produces):**
- `GUARDS = ("G1", "G2", "G3")`, `VALUES = ("V1", "V2", "V3", "V4")`
- `@dataclass ArmStats` with these fields:
  - `judge: dict[str, float]`: mean per dimension;
  - `spread: dict[str, float]`: the within-arm max−min of the per-report means, per dimension plus `"value"`;
  - `audit_ceremony: float` and `audit_leaks: float`: mean hits per report;
  - `key_rate: float`, where ✓=1, ~=0.5 and ✗=0;
  - `key_spread: float`;
  - `negative_ok: bool`;
  - `framing_ok: bool | None`.
- Property `ArmStats.value_mean`: the mean of `judge[V*]`.
- `sign_test_p(wins: int, losses: int) -> float`: the two-sided exact binomial with p = 0.5. Ties are excluded, and `wins + losses == 0` gives 1.0.
- `compare(margin: float, band: float, need: float = 0.0) -> str`:
  - `"PASS"` if `margin >= need`;
  - `"NOISE"` if `margin < need` and `abs(margin - need) < band`;
  - else `"FAIL"`.
- `validation_gate(s: ArmStats, n: ArmStats, wins: int, losses: int, agreement: float, freeze_ok: bool) -> dict`, returning `{"verdict": "VALIDATED"|"NOT VALIDATED"|"INCONCLUSIVE"|"VOID", "conditions": {name: "PASS"|"FAIL"|"NOISE"}}`.
- `rewrite_gate(c: ArmStats, o: ArmStats, freeze_ok: bool) -> dict`, returning `{"verdict": "KEEP"|"REVERT"|"INCONCLUSIVE"|"VOID", "conditions": {...}}`.
- `finalize(family: "validation"|"rewrite", verdict: str, extended: bool) -> str`. After an extension, INCONCLUSIVE maps to NOT VALIDATED (validation) or REVERT (rewrite). Otherwise the verdict is returned unchanged.

**How conditions are computed:**
- **Guards** use `compare(s.judge[g] - n.judge[g], max(spread))` for each G.
- **Auditor guards** use `compare(n.audit_x - s.audit_x, max(1.0, …))`. Counts are lower-is-better, and the band floor is 1 hit.
- **Value:** PASS if either `compare(value margin, band, 0.5)` or `compare(key margin, key band, 0.10)` is PASS. Otherwise NOISE if either is NOISE, else FAIL.
- **Ranking:**
  - PASS if `wins >= losses` and p ≤ 0.2;
  - FAIL if `wins < losses` and p ≤ 0.2;
  - otherwise NOISE.
- **Agreement:** below 0.80 forces INCONCLUSIVE.

- [ ] **Step 1: Write the failing tests** in `tests/test_gauntlet_gates.py`. Build `ArmStats` with `stats(value=5, guards=(5, 5, 5), spread=0.5, ceremony=0, leaks=0, key=0.5, neg=True, framing=True)`. Each test:

  | Test | Input | Expected |
  |---|---|---|
  | `test_sign_test_values` | `sign_test_p(6,0)`, `(5,1)` and `(0,0)` | 0.03125, 0.21875 and 1.0 |
  | `test_validated_when_all_pass` | S value 6, N value 5, spreads 0.3, wins 16, losses 4, agreement 0.9 | `"VALIDATED"` |
  | `test_guard_drop_outside_band_fails` | S G2 3.5, N G2 5.0, spread 0.5 | `"NOT VALIDATED"` with `conditions["guard_judge_G2"] == "FAIL"` |
  | `test_guard_drop_inside_band_is_noise` | S G1 4.8, N G1 5.0, spread 0.5 | `"INCONCLUSIVE"` |
  | `test_value_via_keys_only` | value margin 0.1, key margin +0.25, key spread 0.1 | value condition `"PASS"` |
  | `test_ranking_not_significant_is_noise` | wins 5, losses 4 | `conditions["ranking"] == "NOISE"` |
  | `test_negative_fixture_failure_fails` | `s.negative_ok=False` | `"NOT VALIDATED"` |
  | `test_low_agreement_inconclusive` | agreement 0.7 | `"INCONCLUSIVE"` |
  | `test_freeze_failure_void` | `freeze_ok=False` | `"VOID"` |
  | `test_rewrite_keep_and_noninferiority` | C value 4.9, O value 5.0, spread 0.3 | `"KEEP"` |
  | `test_rewrite_value_drop_reverts` | C value 4.2, O value 5.0, spread 0.3 | `"REVERT"` |
  | `test_finalize_after_extension` | `finalize("INCONCLUSIVE", True)` for each gate family | `"NOT VALIDATED"` / `"REVERT"`. With `extended=False`, `"INCONCLUSIVE"` |

- [ ] **Step 2: Run the tests and watch them fail.** Run `python3 -m unittest tests/test_gauntlet_gates.py -v`. Expected: ImportError.
- [ ] **Step 3: Implement `gates.py`** to the interfaces. Use `math.comb` for the binomial.
- [ ] **Step 4: Run the tests and watch them pass.** Run the same command. Expected: 12 OK. Then run the full suite: `python3 -m unittest discover -s tests`.
- [ ] **Step 5: Commit** `evolution/gauntlet-2026-10/harness/gates.py` and `tests/test_gauntlet_gates.py`, with the message `feat(gauntlet): gate logic`.

---

### Task 2: `round.py build` and the program files

**Files:**
- Create: `evolution/gauntlet-2026-10/harness/round.py`, `harness/skills.json`, `harness/rubric.md`, `harness/PREREG-TEMPLATE.md`, `evolution/gauntlet-2026-10/LEDGER.md`
- Test: `tests/test_gauntlet_round.py`

**Interfaces (produces):**
- **`skills.json`:** an ordered list of `{"order": int, "skill": str, "arms": ["new","none"] | ["new","old","none"], "gates": ["validation"] | ["validation","rewrite"], "key_type": str}`. It covers the 15 rows of spec §2, in that order.
- **`round.py` module functions,** where `ROOT` is the program dir and `REPO` the repo root:
  - `round_dir(skill) -> Path`
  - `validate_pack(rd: Path) -> list[str]`. It returns missing or invalid pack items. `keys.json` must have 3 briefs with ≥ 2 keys each, every key with `id`, `text` and `split == "held-out"`.
  - `build(skill: str, seed: int | None = None) -> dict`. It refuses to run if `rd/SEALED.json` exists. It does the following:
    - copies the arms into `rd/arms/<code>/` from git (`new` = HEAD, `old` = tag `v1.0.0`; `none` gets no directory);
    - generates the cells;
    - writes `rd/cells.json` as a list of `{"cell", "kind": "main"|"framing"|"negative", "input": "pack/<file>", "arm": "<code>", "run": int}`;
    - writes `rd/SEALED.json` as `{"arms": {"<code>": "new"|"old"|"none"}}`;
    - writes `rd/PRE-REGISTRATION.md` from the template;
    - runs `freeze.py register rd/state <files>` over the pack, the harness prompts, `rubric.md`, `gates.py`, `round.py`, `skills.json` and the three skill-gauntlet scripts;
    - returns a summary dict `{"cells": n, "arms": k}`.
  - Arm codes are 2-character `[a-z][0-9]` strings, unique within the round.
  - Cell ids are `<input-stem>--<armcode>--r<run>`.
- **CLI:** `python3 harness/round.py build <skill>` prints one summary line.
- **`LEDGER.md`:** a header and one row per skill:

  ```
  | # | skill | state | validation | rewrite | commit | subagent tokens |
  ```

  Every row starts as `pending`.

- [ ] **Step 1: Write the failing tests.** Each test uses a temp `ROOT` with a fake pack, and a temp git repo that has a tag `v1.0.0` and a `skills/demo-skill`.

  | Test | Expected |
  |---|---|
  | `test_validate_pack_reports_missing_and_bad_keys` | A missing `negative.md` and a key without `split` are both listed. |
  | `test_build_three_arm_cell_counts` | 25 cells for 3 arms. |
  | `test_build_two_arm_cell_counts` | 16 cells for 2 arms. |
  | `test_build_seals_arms_and_uses_opaque_codes` | No cell id or arm directory contains `new`, `old` or `none`. `SEALED.json` maps every code. |
  | `test_build_old_arm_comes_from_tag` | The old arm's SKILL.md equals `git show v1.0.0:…`. |
  | `test_build_refuses_rebuild` | A second `build` raises `SystemExit`. |

- [ ] **Step 2: Run the tests and watch them fail.** Run `python3 -m unittest tests/test_gauntlet_round.py -v`.
- [ ] **Step 3: Implement.**
  - `build` takes its ROOT and REPO from the `GAUNTLET_ROOT` and `GAUNTLET_REPO` environment variables when they are set, for tests. Otherwise it derives them from `__file__`.
  - Write `skills.json` and `LEDGER.md` with all 15 rows from spec §2.
  - `rubric.md` holds the 7 dimensions, with anchors at 1, 3, 5 and 7 written as concrete observable behaviour.
  - `PREREG-TEMPLATE.md` contains the exact gate text from Global Constraints, with `{skill}`, `{arms}`, `{cells}` and `{date}` slots.
- [ ] **Step 4: Run the tests and watch them pass.** Then run the full suite.
- [ ] **Step 5: Commit** `harness/round.py`, `harness/skills.json`, `harness/rubric.md`, `harness/PREREG-TEMPLATE.md`, `LEDGER.md` and the test file, with the message `feat(gauntlet): round build + program files`.

---

### Task 3: Prompts, `render`, `blind`, and the jobs workflow

**Files:**
- Create: `harness/prompts/{designer,executor-skill,executor-none,judge,auditor,verifier}.md` and `harness/run-jobs.js`
- Modify: `harness/round.py`, adding `render` and `blind`
- Test: `tests/test_gauntlet_round.py`

**Interfaces (produces):**
- **`render(skill, phase: "exec"|"judge") -> list[dict]`.** It writes one prompt file per job to `rd/jobs/<phase>/<job>.md` and returns `[{"id", "prompt", "model", "effort"}]`, which it also writes to `rd/jobs/<phase>.json`.
  - **exec:**
    - **Cell types:** one job per cell. With a skill arm the prompt comes from `executor-skill.md`, which points at `arms/<code>/SKILL.md`. With `none` it comes from `executor-none.md`.
    - **Settings:** model `sonnet`, effort `medium`.
    - **What the executor reads:** the prompt names only the input file and the output path `raw/<cell>.md`.
  - **judge:**
    - **J-A, J-B:** one job per (judge persona × main brief), reading `jobs/judge-plan.json`. Model `opus`, effort `high`, output `scores/<judge>-<brief>.md`.
    - **Auditor:** one job. Sonnet, effort `high`, output `audit/audit.json`.
    - **Verifiers:** one job per brief. Sonnet, effort `high`, output `keys/<brief>.json`. Each verifier prompt embeds that brief's keys, which is the only place keys appear.
- **`blind(skill) -> dict`.**
  - **Missing raw:** if any `raw/<cell>.md` is missing, it raises `SystemExit` and lists the missing cells.
  - **Mapping:** it builds a flat mapping `{"<cell>.md": "<CODE>"}` with random codes of the form `[A-Z][0-9]`, unique and disjoint from `V1`–`V4` and `G1`–`G3`. The mapping goes in `SEALED.json["blind"]`.
  - **Normalize:** it runs `normalize.py <mapping> raw blind --strip-h2-ordinals`.
  - **Judge plan:** it writes `jobs/judge-plan.json` with these entries:
    - `{"brief-N": [codes shuffled]}` for the main briefs;
    - `"framing_pairs": [{"pair": "P1", "codes": [hype, skeptical]}]` for each skill arm, unlabelled;
    - `"negative": [codes]`.
  - **Return value:** `{"blind": n, "leak_hits": n}`.
- **Judge output contract** (in `judge.md`). The file ends with a scores block and a ranking block:

  ````
  ```scores
  judge,code,V1,V2,V3,V4,G1,G2,G3,total
  ```
  ```ranking
  judge,brief,order
  J-A,brief-1,K4 B7 C2 …
  ```
  ````

  The order lists codes from best to worst.
- **Auditor output contract** (in `auditor.md`):

  ```
  {"reports": {code: {"ceremony": [str], "leaks": [str]}},
   "framing": {"P1": {"invariant": bool, "why": str}},
   "negative": {code: {"ceremony": bool}}}
  ```

  `auditor.md` quotes the G1/G2 rule text verbatim from `PREREG-TEMPLATE.md`.
- **Verifier output contract:** `{code: {key_id: "✓"|"~"|"✗", "evidence": {key_id: str}}}`.
- **`run-jobs.js`** is the saved Workflow.
  - **Input:** `args = {run: <abs rd>, jobs: [{id, prompt, model, effort}]}`.
  - **Agent prompt:** for each job it calls `agent("Read <run>/<prompt> and do exactly what it says. Return only: done", {label: id, model, effort, schema: {status}})` through `pipeline`.
  - **Return value:** `{done: n, failed: [ids]}`.
  - **Phases** in `meta.phases`: `Run`.

- [ ] **Step 1: Write the failing tests:**
  - `test_render_exec_prompts_hide_arms_and_keys`: build a fake round with keys, then render exec. No prompt contains `new`, `old` or `none` as arm labels, and none contains any key text. The none-arm prompts reference no `SKILL.md`.
  - `test_render_judge_embeds_keys_only_in_verifier_prompts`.
  - `test_blind_refuses_missing_raw`.
  - `test_blind_strips_ordinals_and_writes_plan`: fake raw files with `## 1. Intro`. The blind copies contain `## Intro`, and the judge plan covers every main code.
- [ ] **Step 2: Run the tests and watch them fail.**
- [ ] **Step 3: Implement `render` and `blind`, and write the 6 prompt templates and `run-jobs.js`.**
  - **Designer prompt contract:** write the 8 pack files to `pack/`, using fictional domains only. Return at most 10 lines, with no key content, describing the briefs' domains and the fixture types.
  - **Executor prompts:** no subagents, no web search, no clarifying questions, state assumptions, and write only the user-facing reply.
- [ ] **Step 4: Run the tests and watch them pass.** Then run the full suite.
- [ ] **Step 5: Commit** with the message `feat(gauntlet): prompts, render, blind, run-jobs workflow`.

---

### Task 4: `round.py score`

**Files:**
- Modify: `harness/round.py`
- Test: `tests/test_gauntlet_round.py`

**Interfaces:**
- **`score(skill, extended: bool = False) -> dict`.** It does the following, in order:
  1. Runs `freeze.py verify rd/state` and records `freeze_ok`.
  2. Requires every judge, audit and key file that `jobs/judge.json` expects. If any is missing, it raises `SystemExit` with the list.
  3. Parses the scores with `scorecard.load`.
  4. Parses the `ranking` blocks.
  5. Unseals the codes into (arm, kind, brief, run).
  6. Builds an `ArmStats` per arm:
     - word counts come from the blind files;
     - `negative_ok` is `words ≤ 1.5 × none-negative words and not ceremony`;
     - `framing_ok` comes from the auditor pair that belongs to that arm.
  7. Computes pairwise ranking wins and losses (`new` vs `none`, and `new` vs `old`) from each judge's full order.
  8. Computes inter-judge agreement: the share of shared (code, dimension) cells within 1 point.
  9. Calls the gates.
  10. Writes `rd/verdict.json` as `{"skill", "validation": {...}, "rewrite": {...} | null, "agreement", "freeze_ok", "extended"}`.
  11. Writes `rd/scorecard.md`, at most 40 lines: per-arm dimension means, margins, bands, key rates, wins and losses, the condition table and the verdicts.
  12. Prints the scorecard.

- [ ] **Step 1: Write the failing tests.** Each builds a synthetic round with known numbers.

  | Test | Expected |
  |---|---|
  | `test_score_validated_case` | `"VALIDATED"` |
  | `test_score_refuses_missing_judge_file` | `SystemExit` |
  | `test_score_unseals_correct_arm` | Swapping the sealed mapping flips the verdict. |
  | `test_score_rewrite_gate_present_only_for_three_arm` | `rewrite` is null for 2-arm rounds. |
  | `test_agreement_computation` | Two judges that differ by 2 on one of 7 cells give 6/7. |

- [ ] **Step 2: Run the tests and watch them fail.**
- [ ] **Step 3: Implement.**
- [ ] **Step 4: Run the tests and watch them pass.** Then run the full suite.
- [ ] **Step 5: Commit** with the message `feat(gauntlet): scoring and gate application`.

---

### Task 5: `round.py apply`, `status` and the ledger

**Files:**
- Modify: `harness/round.py`
- Test: `tests/test_gauntlet_round.py`

**Interfaces:**
- **`apply(skill, commit_hint: str = "") -> dict`.** It requires `verdict.json`, and the `validation.verdict` must not be INCONCLUSIVE unless `extended` is set.
  - **README:** it rewrites that skill's Validation cell in the README skills table to one of:
    - `Gauntlet 2026-10: validated`
    - `Gauntlet 2026-10: not validated`
    - `Gauntlet 2026-10: void (re-run)`

    For a rewrite gate it appends `; rewrite kept` or `; rewrite reverted`, and links to `evolution/gauntlet-2026-10/<skill>/scorecard.md`.
  - **REVERT:** it replaces the SKILL.md body with the `v1.0.0` body and keeps the current frontmatter. It bumps the patch of `metadata.version`. It replaces `references/` with the `v1.0.0` references if they exist there, and otherwise keeps them. It then runs `validate_skills.py` and must pass.
  - **Research note:** it writes `rd/research-note.md` with the quantitative section filled in from `verdict.json`, followed by an `## Autopsy` heading for the coordinator's three to five lines.
  - **Ledger:** it updates the skill's row in `LEDGER.md` to state `applied` with both verdicts.
  - **State:** the row's state moves through `designed`, `frozen`, `ran`, `blinded`, `judged`, `scored` and `applied`. The commands `build`, `blind`, `score` and `apply` each set their state. `ran` and `judged` are set by `round.py mark <skill> <state>`.
- **`status() -> str`** returns the ledger table and the next pending skill.

- [ ] **Step 1: Write the failing tests:**
  - `test_apply_updates_readme_cell`.
  - `test_apply_revert_restores_body_keeps_frontmatter_and_bumps_patch`, using a temp repo with tag `v1.0.0`.
  - `test_apply_refuses_unextended_inconclusive`.
  - `test_ledger_state_progression_and_status_next`.
- [ ] **Step 2: Run the tests and watch them fail.**
- [ ] **Step 3: Implement.**
- [ ] **Step 4: Run the tests and watch them pass.** Then run the full suite.
- [ ] **Step 5: Commit** with the message `feat(gauntlet): apply, ledger, status`.

---

### Task 6: Pilot round, hypothesis-elimination

This task runs the **Round Procedure** below for the pilot, then performs the fitness check.

**Round Procedure.** Every round uses these steps exactly. The coordinator reads only the outputs named here.

1. **Design.** Dispatch an Agent (`general-purpose`, model `opus`, effort `high`) with the prompt "Read `<rd>/jobs/designer.md` and follow it."
   - `round.py render-designer <skill>` writes that file from `prompts/designer.md`, filling in the skill path, the key type from `skills.json` and the list of prior-round fixture files to avoid.
   - Read only the designer's return of at most 10 lines.
   - Run `round.py mark <skill> designed`.
2. **Build.** Run `python3 harness/round.py build <skill>`, which outputs one line.
3. **Execute.** Run `round.py render <skill> exec`, then launch the Workflow `{scriptPath: harness/run-jobs.js}` with args `{run: <abs rd>, jobs: <contents of jobs/exec.json>}`.
   - Expected: `failed: []`. Re-run any failed ids with the identical prompts.
   - Run `round.py mark <skill> ran`.
4. **Blind.** Run `round.py blind <skill>`. Inspect the leak-hit count. Never auto-fix a hit.
5. **Judge.** Run `round.py render <skill> judge`, then run the Workflow with `jobs/judge.json`. Expected: `failed: []`. Then run `round.py mark <skill> judged`.
6. **Score.** Run `round.py score <skill>` and read `scorecard.md`.
   - If the verdict is INCONCLUSIVE and `extended` is false, run the extension: `round.py extend <skill>` adds `r3` and `r4` cells. Then repeat steps 3 to 6 with `--extended`.
7. **Apply.** Run `round.py apply <skill>` and write the three to five Autopsy lines.
8. **Commit and push.**
   - Check with `python3 -m unittest discover -s tests`, `python3 scripts/validate_skills.py` and `claude plugin validate ./skills --strict`.
   - Stage `git add evolution/gauntlet-2026-10/<skill> evolution/gauntlet-2026-10/LEDGER.md README.md`, plus `skills/<skill>` if it was reverted.
   - Commit with the message `gauntlet(<skill>): <validation> [; rewrite <keep|revert>]`, then `git push`.
   - Record the round's subagent tokens, taken from the two Workflow results plus the designer's, in the ledger row.

**Additional interfaces** used by the procedure, added to `round.py` with tests in this task, following the Task 2–5 test pattern:
- `render-designer`;
- `mark <skill> <state>`;
- `extend <skill>`, which appends `r3`/`r4` cells for every arm and main brief and records `extended: true` in `SEALED.json`.

- [ ] **Step 1: Write the failing tests:** `test_extend_adds_runs_3_and_4` and `test_render_designer_lists_prior_fixtures_to_avoid`.
- [ ] **Step 2: Run them, implement, run them again, and commit** with the message `feat(gauntlet): designer render, mark, extend`.
- [ ] **Step 3: Run the Round Procedure for hypothesis-elimination.**
- [ ] **Step 4: Run the fitness check.** It reads `scorecard.md`. The harness is fit iff all three hold:
  - agreement ≥ 0.80;
  - the `none` arm's key rate is at least 0.15 below the skill's, OR the `none` arm's value mean is at least 0.5 below the skill's;
  - `blind` reported 0 leak hits that name an arm or version.

  If the harness is unfit:
  - fix the harness as an amended row (`freeze.py amend --reason`), recorded before any further round runs;
  - delete the pilot round directory and re-run the pilot from Step 3;
  - note the amendment in `LEDGER.md`.

---

### Task 7: Rounds 2–15

For each remaining skill in `skills.json` order, run the Round Procedure and continue automatically.

- **Reading the ledger:** after any interruption, run `round.py status` and resume at the first row that is not `applied`.
- **Within a round:** resume at the next state after the row's recorded state.

Order:
1. reasoning-handover-protocol
2. integrated-reasoning
3. tree-of-thoughts
4. breadth-of-thought
5. self-reflecting-chain
6. parallel-execution
7. premortem-evolved
8. adversarial-reasoning
9. dialectical-reasoning
10. analogical-transfer
11. rapid-triage-reasoning
12. negotiated-decision-framework
13. option-synthesis
14. skill-gauntlet

- [ ] One checkbox per skill, ticked when its ledger row reads `applied` and its commit is pushed.

---

### Task 8: Release 1.2.0

**Files:**
- Modify: `.claude-plugin/plugin.json` (version `1.2.0`), `CHANGELOG.md`, `README.md` (the Validation status section summarizing the program and linking `LEDGER.md`)

- [ ] **Step 1: Write the CHANGELOG `1.2.0` entry.** List every skill's validation verdict, every rewrite verdict and every revert, with links to each scorecard.
- [ ] **Step 2: Run all checks, commit, push, tag `v1.2.0`, watch CI, and create the release with the zips** (`build_zips.py`).
- [ ] **Step 3: List the skills whose files changed since v1.1.0 that exist on claude.ai** (premortem-evolved, skill-gauntlet and option-synthesis), and **ask the user before re-uploading.** option-synthesis uses the personal build.
