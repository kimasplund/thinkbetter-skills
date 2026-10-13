# Regression round: thinkbetter-skills v1.0.0 vs the format and bug pass

This file was written on 2026-10-13, before any arm ran.

- **Champion (old):** skills at tag `v1.0.0`.
- **Challenger (new):** the merged format and bug branch.
- **Blinding:** the arms are randomly coded `m1` and `m2`. The mapping is sealed in `SEALED.json` and opened only after scoring.
- **Fixtures:** `fixtures/fixtures.json` (40 triggering queries, 14 behaviour tasks). Its sha256 is recorded in `fixtures.sha256` before the run.

## Instruments

1. **Triggering.**
   - For each (arm × model ∈ {haiku, sonnet}), one agent sees that arm's 15 (name, description) pairs and picks, for each of the 40 queries, the single skill it would invoke, or `none`.
   - A query counts as correct if the pick is in `expect`.
2. **Behaviour.**
   - For each (fixture × model ∈ {haiku, sonnet} × arm), one executor reads that arm's SKILL.md (and any referenced files) and answers the task as a chat reply. Each reply is written to `raw/`.
   - Executors don't spawn subagents and don't search the web.
3. **Blind judge.**
   - One Sonnet judge per (fixture × model) sees both replies as A and B, in an order that alternates by index.
   - It scores quality (1–10) and proportionality (1–10), counts method or score leaks for each reply, and states a preference: A, B or tie.
4. **Mechanical leak scan.**
   - A script counts these whole-word hits in every reply:
     - skill names and pattern acronyms (ToT, BoT, SRC, HE, AR, DR, AT, RTR, NDF, IR);
     - "confidence: NN%" lines;
     - "Stage/Phase/Step N" headings.

## Gate (conjunctive; the challenger is adopted only if ALL hold)

- **G1 Triggering.** For each model, challenger correct ≥ champion correct − 1, so a one-query noise allowance.
- **G2 Preference.** Across the 28 judged pairs, the champion is preferred in at most 9 pairs (≤ 1/3). No skill has the champion preferred on both models.
- **G3 Leakage.** Challenger mechanical leak total ≤ champion's, AND challenger judge-counted leak total ≤ champion's.
- **G4 Restraint.** On `b-ir-trivial`, the challenger's reply is no longer than 1.25 × the champion's word count on each model. On `b-ir-urgent`, the challenger's proportionality score ≥ the champion's − 1 on each model.
- **G5 Guard.** No single fixture × model drops by ≥ 3 quality points (challenger vs champion).

## Outcomes and how they are read

- **Adopt** if the gate passes.
- **Revert the skill** if it is responsible for a failed condition: the champion version ships for that skill, and the failure goes into the CHANGELOG.
- **INCONCLUSIVE** if an instrument didn't run, for example because an agent died. In that case, re-run that cell only.
- **No goalpost movement after results.**
