# Retroactive verification — candidate skill-gauntlet-v2 mechanics applied to the historical v6 round

Historical record: `/mnt/agents/output/premortem-evolution/abtest2/ab-test-results-round2.md`, §13 (v6 pre-registration, 2026-08-22) and §14 (v6 results/verdict).
Candidate mechanics: `/mnt/agents/output/skill-gauntlet-v2/SKILL.md`, `references/protocol.md`, `references/key-verification.md`, `scripts/freeze.py`.

Shared historical facts (§13–§14):
- v6 ran 6 cells (fixture B4; Brief D hype G7; Brief D skeptical K2; neutral E2/H4/F7), judged blind against the champion's 9 re-scored main runs by 2 judge panels (RG, RH), a linter-assisted auditor (symmetric D3 tie enumeration + D9 leak scan on both arms, framing gate on E2/G7/K2, fixture gate on B4), and a key verifier on the SAME 12-key matrix reused across all five prior builds, whose proposer had read every prior verdict.
- §13 declared, BEFORE any v6 run, an "Instrument-symmetry correction": the historical auditor D3 champion bar (5.00) had been produced without full tie enumeration; the repaired (linter-assisted) enumeration would be applied "to BOTH arms symmetrically," with the gates unchanged ("≥ champion on both instruments").
- Actual verdict (§14.3): NO ADOPTION. Gate 1 (D3) passed on both instruments (judges 5.00 vs 4.78; auditor 5.00 vs 4.11). Gate 2 (D9) failed on the judges instrument (3.50 vs 4.11; auditor dissented 5.00 vs 3.56; conservative reading governed). Gate 3 value margins passed (D5 +1.00 ≥ +0.80; D7 +1.00 ≥ +0.65). Gate 4 keys passed (11.5/12 = 95.8% ≥ 90% floor and ≥ champion's 90.3%). Gate 5 fixture passed (B4 deflates). Gate 6 framing failed (fatal-flaw label flip unique to the challenger; trigger-number drift; auditor PARTIAL PASS, conjunctive rule → FAIL).

---

## (a) Verifier-integrity — the instrument-symmetry correction

### Mechanic text (quoted)

SKILL.md, inviolable rule 4:
> "The verifier is frozen too. … A mid-round instrument change is legal only as an amended gate row — timestamped, justified, applied symmetrically to both arms, recorded BEFORE the changed instrument is used. A silent change voids the round."

protocol.md, "Verifier integrity":
> "Mid-round instrument repair is sometimes correct — in the source rounds an auditor that had under-enumerated the champion's own violations was repaired, openly, before the round it governed. Such a repair is legal ONLY as an **amended gate row**: timestamped, rationale written, applied symmetrically to BOTH arms from the amendment forward, and recorded BEFORE the changed instrument produces any score used in the verdict (`freeze.py amend --reason "…"`). A hash mismatch with no predating amendment = silent verifier change: the round is VOID — discard the scores, restore or amend, rerun. The verifier never edits itself mid-count."

freeze.py behavior: `verify` compares each file against its latest declared hash (registration superseded by amendments by timestamp) and on mismatch prints "round is VOID: discard scores, restore or amend (with rationale), rerun" and exits 1. `register` refuses to overwrite (append-only); `amend` appends a timestamped, reason-mandatory row and never edits prior rows.

### Historical facts

§13 ("written BEFORE any v6 run", dated 2026-08-22) contains the correction in full: rationale (linter validation exposed that the 5.00 champion D3 bar was produced without full tie enumeration; 6/9 champion neutral reports carry tie violations and 5/9 carry ordinal leaks under exhaustive enumeration), scope ("the auditor applies the linter's enumeration to BOTH arms symmetrically"), and an explicit statement that the comparison standard is unchanged ("the gates remain '≥ champion on both instruments' … This is instrument repair, not goalpost movement"). The changed instrument produced scores only in §14, after the declaration.

### Adjudicated outcome

Checked against the four amended-gate-row criteria:
1. **Timestamped** — yes; the §13 header dates the pre-registration 2026-08-22 and states it was written before any v6 run.
2. **Rationale written** — yes; the under-enumeration finding and its evidence (6/9, 5/9 counts) are in the row itself.
3. **Applied symmetrically to both arms** — yes; explicit "BOTH arms symmetrically," and the champion's 9 runs were re-scored by the same repaired auditor (also satisfying protocol adjudication rule 3, within-instrument fairness).
4. **Recorded BEFORE the changed instrument was used** — yes; the declaration is in the pre-registration, before any execution, stronger than the minimum "before use."

→ The correction is a **legal amended gate row; the round stays VALID.** The protocol text even anticipates this exact event ("an auditor that had under-enumerated the champion's own violations was repaired, openly, before the round it governed"), so classification is a direct textual match, not an inference.

Adversarial notes (do not change the outcome):
- The repair lowered the champion's effective D3 bar from 5.00 to 4.11, which eased the candidate's gate 1. The rule's only guard against self-serving amendments is "If you find yourself amending the gate to make a failing candidate pass, that is goalpost movement — stop." Because the amendment predates all scores and applies symmetrically, that stop rule is not triggered; the rule as written admits this amendment. A stricter harness might require amendments that move a champion bar to be ratified by a non-proposer, but the candidate text does not.
- `freeze.py` cannot itself verify the "predates use" condition (an amendment's timestamp proves only when it was recorded); legality of timing remains a procedural check against the gate record, as the script's own warning acknowledges. For this round the documentary record (§13 before §14) settles it.

### Hypothetical: SILENT auditor edit discovered at verdict (hash mismatch, no predating amendment)

The rule adjudicates mechanically: `freeze.py verify` reports "VERIFIER INTEGRITY: FAIL — silent change detected … round is VOID," exit 1; protocol.md: "the round is VOID — discard the scores, restore or amend, rerun." Because an amendment recorded at verdict time cannot satisfy "recorded BEFORE the changed instrument is used," no retroactive cure exists for the current scores; only restore-or-amend **plus rerun** is available. The verdict for the discovered-silent-edit case is unambiguous: VOID, no score salvage.

### Verdict (a): PASS

Both cases are adjudicated by crisp, complementary branches — documented pre-use symmetric amendment → valid; undocumented mismatch → void-and-rerun — and the historical correction satisfies every enumerated criterion on the documented facts. (Caveats noted above are hardening suggestions, not ambiguity in this adjudication.)

---

## (b) Degraded mode — v6 re-run with judge panels RG/RH removed

### Mechanic text (quoted)

SKILL.md:
> "**Degraded mode (panel unavailable).** If judge panels cannot run this round … the mechanical instruments — auditor, key verifier, fixtures, leak scan — still run and stay decisive: any decisive mechanical failure REJECTS. Clean mechanicals with no panel → INCONCLUSIVE ("collect the panel with the identical gate"), never ADOPT. Panel absence never waives a guard…"

protocol.md:
> "- **Any decisive mechanical failure → REJECT.** A leaky, ceremonial, or key-blind candidate is out; it is never deferred.
> - **Mechanicals clean but panel absent → INCONCLUSIVE** — "collect the panel with the identical gate." Never ADOPT without the full conjunctive gate: the guards only judges price (holistic guard-dim readings, forced choices) are unmeasured, and an unmeasured guard is not a passed guard."

### Historical facts, re-scored per gate without judges

| Gate (§13 numbering) | Mechanical leg present? | Mechanical result | Judge-dependent leg |
|---|---|---|---|
| 1. D3 ≥ champion, both instruments | Auditor leg: linter-assisted symmetric enumeration | **PASS** (5.00 vs 4.11) | Judges leg (5.00 vs 4.78 ✓) now unmeasured |
| 2. D9 ≥ champion, both instruments | Auditor leg: D9 leak scan | **PASS** (5.00 vs 3.56) | Judges leg was the ACTUAL FAILURE (3.50 vs 4.11 ✗, driven by RH's docks of the two template-authored leaks) — now unmeasured |
| 3. D5 ≥ +0.80, D7 ≥ +0.65 | None — gate text is "judges pooled" | unmeasurable | Entirely judge-dependent (actual: both passed) |
| 4. Key detection ≥ 11/12 and ≥ 90.3% | Key verifier | **PASS** (11.5/12 = 95.8%) | — |
| 5. Fixture DEFLATES | Auditor fixture gate | **PASS** (B4 deflates, real gotchas, linter confirms no ladder) | — |
| 6. Framing invariant | Auditor framing gate on G7/K2/E2 | **FAIL** — fatal-flaw label flips across registers ("the cash architecture is [fatal]" vs "There isn't one"), top-2 holds only at category level, trigger numbers drift; flip unique to the challenger; the §fixtures criterion states a unique flip "blocks adoption regardless of means" | — |

Mechanical tally: gates 1, 4, 5 pass mechanically; **gate 6 is a decisive mechanical failure** (framing is an auditor-run gate in both the historical pre-registration and the candidate's template: "Framing invariant (auditor gate)"). The historical auditor's "PARTIAL PASS" is converted to FAIL by the conjunctive no-partial-credit rule, which the candidate's protocol shares ("Candidates passes iff ALL of …").

### Adjudicated outcome

The facts land in the first degraded-mode branch: **any decisive mechanical failure → REJECT.** The framing gate's fatal-flaw label flip is a documented, mechanically gated failure unique to the challenger.

→ Degraded-mode verdict: **REJECT (NO ADOPTION)** — identical terminal outcome to the actual judged round, reached on gate 6 alone.

Judge-dependent conditions (gate 2's judges leg, gate 3's value margins, the 6/6 forced choices) become unmeasured; under "an unmeasured guard is not a passed guard" that would have capped the outcome at INCONCLUSIVE had the mechanicals been clean — but they are not, so REJECT governs and the moot judge legs never need resolving. Both branches of the rule and the boundary between them are fully specified, and the framing failure unambiguously selects the REJECT branch.

Adversarial notes (do not change the outcome):
- Degraded mode would have **missed the actual gate-2 defect**: the two template-authored leaks (`**Consciously accepted (at most one):**` header, `Paper-tiger re-upgrades (Track)` label) were caught only by judge RH; §14.4.2 records that "the linter's token wordlist catches bracketed tokens but not the template's own phrasing — so both leaked through the mechanical gate undetected." In this round the miss is harmless to the verdict (framing already rejects), but it demonstrates that "mechanical instruments stay decisive" does not mean "mechanical instruments are sufficient": a candidate whose only defect is judge-visible would get INCONCLUSIVE rather than the REJECT the full gate would deliver. The protocol's insistence on "never ADOPT" in degraded mode is exactly the compensating control, and it is correctly specified.
- Champion-bar comparisons for mechanical legs remain valid in degraded mode only because the champion's cells were re-scored by the same auditor; the candidate protocol's within-instrument fairness rule covers this.

### Verdict (b): PASS

The mechanic produces a definite verdict — REJECT via the decisive mechanical framing failure — with no branch ambiguity, and the verdict coincides with the actual round's NO ADOPTION.

---

## (c) Held-in / held-out — classifying the v6 key matrix

### Mechanic text (quoted)

key-verification.md:
> "**Held-in**: keys the candidate's author may have seen or tuned to — any key reused from prior rounds, any key in a published results file, any brief the proposer helped design.
> **Held-out**: keys planted after the candidate's design was frozen, sealed from the proposer like every other key. Every round with detection claims carries at least one held-out brief."
> "The bar applies **per split**: detection non-regressive vs champion on held-in AND on held-out, AND held-out ≥ 90% absolute floor."
> "Why this exists: in the source rounds one 12-key matrix was reused across five builds whose proposer had read every prior verdict — every key was held-in."

SKILL.md:
> "A round whose proposer has seen prior keys is a held-in-only round — say so, and price the gate accordingly."

Gate template (SKILL.md / protocol.md):
> "(3) key detection non-regressive per split — held-in AND held-out each ≥ champion's same-split rate — AND held-out ≥ 90% absolute floor"

### Historical facts

§13: "key verifier (12 cells on E2/H4/F7, same KEY-MATRIX, hard-grader rule)." The matrix is the same 12-key matrix used across v3, v4, v5, evo-88905a, and v6; the keys and their grading history are published in the results file (e.g., §14.4.6 documents the D4 seasonality cell's six-build record); the v6 proposer authored the candidate "from the validated delta inventory" after four rounds of published verdicts, i.e., had read every prior verdict.

### Adjudicated outcome

Classification is mechanical under the definition's first clause: every one of the 12 keys is "a key reused from prior rounds" and "a key in a published results file," and the proposer had seen all of them → **all 12 keys are held-in; the held-out split is empty. The v6 round is a held-in-only round.** The rule's rationale paragraph names this exact scenario as its motivating case, so there is no classificatory judgment call at all.

What the per-split adoption bar would have required that the round did not contain:
1. **At least one held-out brief** — keys planted AFTER the v6 design freeze and sealed from the proposer ("Every round with detection claims carries at least one held-out brief"). v6 had none; all three key-graded cells (E2/H4/F7) used the pre-existing matrix.
2. **A held-out detection rate ≥ 90% absolute floor AND ≥ the champion's same-split held-out rate.** With an empty held-out split, both conjuncts are unmeasurable — and since the gate is conjunctive, condition 3 as written **cannot be satisfied** by this round. The v6 key result (11.5/12 = 95.8%) satisfies only the held-in leg and the historical (pre-split) bar.
3. Consequently, under the candidate's rules as written, v6's key gate — despite passing numerically — would **not clear** condition 3: the held-out leg is absent, and "Every round with detection claims carries at least one held-out brief" makes that a design non-compliance, not a waivable omission. (Terminal effect on this round is nil — gates 2 and 6 already fail — but had v6 otherwise passed, the held-in-only matrix would independently block ADOPT or force a re-run with a sealed held-out brief.)

### Verdict (c): PASS

The classification rule is unambiguous (an enumerated clause plus an explicit reference to this exact source-round scenario) and yields a definite outcome: held-in-only matrix, per-split bar unmet/unmeetable for want of any held-out keys. One residual softness, flagged but not verdict-changing for this case: SKILL.md's "say so, and price the gate accordingly" acknowledges held-in-only rounds but never defines what "pricing" is permissible when the gate text mandates a held-out floor and a ≥1-held-out-brief requirement — the escape hatch's contents are unspecified. For the v6 facts, both readings agree on the classification and on the absence of the held-out leg.
