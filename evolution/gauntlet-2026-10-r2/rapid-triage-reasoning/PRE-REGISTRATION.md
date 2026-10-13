# Pre-registration: rapid-triage-reasoning

Written 2026-10-13, before any cell ran. The program spec is `docs/superpowers/specs/2026-10-13-suite-gauntlet-design.md`, with Amendment 3 for this follow-up program.

- **Arms:** new, old, none. Arm codes are sealed in `SEALED.json`. `new` is the candidate edit, `skills/rapid-triage-reasoning` at `HEAD` when the round was built; `old` is the shipped text, `skills/rapid-triage-reasoning` at `v1.2.0`; and `none` means no skill.
- **Cells:** 27 in total:
  - main: 3 briefs × every arm × 2 runs;
  - framing: hype and skeptical, 1 run per arm, no skill included;
  - negative: 1 run per arm.
- **Instruments:**
  - **Judges:** J-A (domain practitioner) and J-B (skeptical reviewer), both Opus. They score the main briefs dimension by dimension against `harness/rubric.md`, then rank the replies.
  - **Auditor:** Sonnet. It applies the rule text below.
  - **Key verifiers:** Sonnet, one per brief, grading against `pack/keys.json`. Every key is held-out.
  - **Executors:** Sonnet.
- **Verifier freeze:** `freeze.py register state …` was run over the pack, the harness prompts, the rubric, `gates.py`, `round.py`, `skills.json` and the skill-gauntlet scripts. Its state hash is recorded below.
- **Gates:** validation + rewrite

## Gate text (binding)

**Validation gate (S = new, N = none).** S is VALIDATED iff all of the following hold:
1. S ≥ N on G1, G2 and G3 (judges, brief-paired; a deficit no larger than 0.25 is NOISE), S carries at most one more ceremony hit and at most one more leak hit than N in total, and S's replies are at most 2.0× the no-skill median length for the same brief (mean over briefs).
2. The value margin (mean of V1–V4) is at least +0.5 and either larger than its noise band or positive on every brief; or the key-rate margin is at least +0.10 and larger than its noise band.
3. Forced rankings: count one outcome per ranking (judge × brief). S wins a ranking when its replies' mean position beats N's. PASS if wins ≥ losses. FAIL only if wins < losses with a two-sided sign test p ≤ 0.2. Otherwise NOISE.
4. The negative fixture deflates: words ≤ 1.5 × the no-skill negative reply's word count, and the auditor finds no ceremony.
5. Framing invariance: the same top recommendation and verdict in both the hype and skeptical replies. A flip is NOISE when N's pair flips too, and FAIL otherwise.
6. Inter-judge agreement: at least 0.80 of shared cells within 1 point.
7. `freeze.py verify` is clean.

**Rewrite gate (C = new, O = old).** KEEP iff all of the following hold:
1. C ≥ O on every guard dimension, on both instruments (with the same 0.25 floor and one-hit audit tolerance), and C's length ratio is at most O's + 0.25.
2. C's key rate ≥ O's.
3. C's value mean ≥ O's value mean − 0.25.
4. C passes the negative gate, and the framing gate (a flip is NOISE when O's pair flips too).

Otherwise the verdict is REVERT.

**Adoption.** A 3-arm round keeps the candidate unless the rewrite gate says REVERT. A 2-arm round adopts the candidate only if it is VALIDATED. A candidate that is not adopted returns `skills/rapid-triage-reasoning` to exactly its files at `v1.2.0`.

**Conditions and noise:**
- Each condition is PASS, FAIL or NOISE.
- **Brief-paired noise band.** Every judge and key comparison is brief-paired: for each brief, the arm difference of that brief's means; the margin is the mean of those differences and the band is their max − min.
- A condition is NOISE when its margin is on the failing or unconfirmed side but within the band.
- An auditor difference of at most one hit in total across the arm's replies passes; two or more fail.
- Auditor quotes are checked mechanically: each must appear verbatim in the reply it is credited to. An auditor output that fails the check is re-run with the identical prompt.
- Any FAIL gives NOT VALIDATED or REVERT. Otherwise any NOISE gives INCONCLUSIVE.
- If agreement is below 0.80, mechanical FAILs (auditor counts, length, negative, framing) stay decisive and the validation verdict otherwise reads INCONCLUSIVE. The rewrite gate has no agreement condition.
- A failed freeze verify makes the round VOID, and it is re-run.

**INCONCLUSIVE.** The round gets one extension: runs 3 and 4 of every arm on the same main briefs, under the identical gate. If it is still INCONCLUSIVE, the verdict is NOT VALIDATED (validation) or REVERT (rewrite).

**Auditor rule text (quoted verbatim to the auditor):**
- **Ceremony:** a ceremony hit is any of the following, in a reply's user-facing text:
  - a section that restates the question;
  - a heading or label that describes the method rather than the content;
  - a summary that repeats earlier sections without adding information;
  - a template field left in place with nothing new in it;
  - a decision-record or report scaffold on a task that needed a direct answer.
- **Leak:** a leak hit is any of the following:
  - the name of a reasoning method, framework or skill (for example "tree of thoughts", "breadth-of-thought", "dialectical", "premortem", "hypothesis elimination");
  - an acronym for one;
  - internal scoring schemes, rating tables or confidence arithmetic shown to the user (a plain statement of how confident the reply is, in words or a single figure, is calibration and is not a leak);
  - numbering of the method's own stages or phases.

  Headings about the user's content are not leaks.

No goalpost movement after results. A bar that turns out to be mis-set is reported under both readings, and this text decides.

## Freeze record

Recorded in FREEZE.md (written right after registration).
