# Round 3 — v6 vs champion: record and adoption note

**Adoption disclosure.** The pre-registered conjunctive gate for this round returned
**NO ADOPTION**: seven of eight conditions passed; the eighth (D7 tripwires, +0.67 then
+0.78, floor +0.65) cleared its floor twice but landed inside the pre-registered noise
band twice at n=9 runs/arm, and the sealed closure rule ended the round. The owner then
adopted v6 as **v2.1 by explicit decision outside the harness**, on the full evidence:
12/12 blind forced choices across two independent judge panels, no regression on any
instrument, key detection 97.2% vs 93.1%, and a D7 cell-level record of 14 higher /
4 equal / 0 lower (one-sided sign test p ≈ 6×10⁻⁵ — decisive under the statistic the
protocol reserves for larger designs; the registered spread heuristic is direction-blind).
The gate was not bent; it was overridden, and this file is the disclosure.

The full round record follows.

---
# Round-3 A/B: champion (premortem-evolved v2) vs candidate (v6 = v5 + two mechanical deltas)

**Pre-registered spec:** `pre-registration.md` (gate written before any cell; augmentation addendum written after scoring round A, before any augmentation cell).
**Data:** 27 executor cells (2 arms × 3 briefs × 3 runs = 18 main + 4 framing + 2 fixture + 3 controls), two blind judge panels (A: J1–J3 on 12 main runs; B: J4–J6 on all 18 — the pre-registered deciding panel), mechanical auditor ×2, key verifier ×2. All scoring blind; mapping sealed in `SEALED-MAPPING.json`; champion md5-verified frozen before, during, and after.

## Verdict: NO ADOPTION — v6 discarded per the pre-registered closure rule; champion (v2) ships unchanged.

The gate is conjunctive. Seven of eight conditions PASS. Condition 4's D7 leg clears its floor (+0.78 ≥ +0.65) but lands inside the pre-registered noise band on the deciding panel (margin 0.78 < candidate within-arm spread 1.0) for the second time; the augmentation addendum's closure rule — "if any gated margin on the fresh panel again lands inside its band, the round closes NO ADOPTION, champion stands" — therefore ends the round. Per the symmetric-loss clause the v6 branch is discarded and its deltas ship only as a research note (`RESEARCH-NOTE-round3.md`).

## 1. Deciding scorecard (fresh panel J4–J6, all 18 main runs, n=18 judge-scores/arm/dim)

| Dim | Champion | v6 | Margin | Gate | Result |
|---|---|---|---|---|---|
| D1 specificity (1–7) | 6.94 | 7.00 | +0.06 | — | |
| D2 causal chaining (1–7) | 6.94 | 6.94 | 0.00 | — | |
| D3 probability honesty (1–5, GUARD) | 5.00 | 5.00 | 0.00 | ≥ champ, both instruments | **PASS** (auditor: 3 vs 9 violations — see §3) |
| D4 flaw detection (1–5) | 5.00 | 5.00 | 0.00 | — | |
| D5 rebuild actionability (1–7, VALUE) | 5.78 | 7.00 | **+1.22** | ≥ +0.80, outside band | **PASS** (1.22 > band 1.0) |
| D6 adversarial depth (1–7) | 6.56 | 6.78 | +0.22 | — | |
| D7 tripwires (1–7, VALUE) | 6.00 | 6.78 | **+0.78** | ≥ +0.65, outside band | **floor met; INSIDE band (0.78 < 1.0) → closure rule fires** |
| D8 cold tone (1–5, GUARD) | 5.00 | 5.00 | 0.00 | ≥ champ | **PASS** |
| D9 length/bloat (1–5, GUARD) | 4.06 | 4.44 | +0.39 | ≥ champ, both instruments | **PASS** (see §3) |
| **Total (55)** | **51.28** | **53.94** | **+2.67** | | |

Round-A panel (12 main runs): total 52.25 vs 54.33 (+2.08); D5 +1.08, D7 +0.67, D9 +0.42 — same signature, both panels.
**Forced choices: 12/12 for v6** (panel A: U6, N4, U6, S2, N4, S2 · panel B: U6, S8, S8, R2, K2, R2). No judge in either panel ever chose a champion report.

## 2. The eight pre-registered conditions

| # | Condition | Result |
|---|---|---|
| 1 | D3 ≥ champion, both instruments | **PASS** — judges parity 5.00/5.00 both panels; auditor mechanical: v6 3 violations vs champion 9 across 18 runs |
| 2 | D9 ≥ champion, both instruments | **PASS on the pre-registered census** — judges +0.42/+0.39; narrow census: champion mean 3.33 (incl. R4's four references to a "Stage 4/5" that doesn't exist in its own report; W6 6+ items) vs v6 4.89. Auditor-A's *executed* census deviated from pre-registration (swept in tier labels — content the rubric's D5/D7 anchors require) and read the other way (1.00 vs 1.83); both readings reported; the pre-registered text decides. Deviation on record in the addendum |
| 3 | D8 ≥ champion | **PASS** — 5.00 everywhere, every instrument, all 27 scored documents |
| 4 | D5 ≥ +0.80 AND D7 ≥ +0.65, outside noise band | **D5 PASS** (+1.22 > band 1.0). **D7: floor met twice (+0.67, +0.78) but inside the band twice → closure rule → NO ADOPTION.** Both-readings note: v6 D7 cells vs champion's uniform 6s are 14 higher / 4 equal / 0 lower; a one-sided sign test gives p ≈ 6×10⁻⁵ — decisive under the protocol's "better version" statistics, which were pre-registered only for ≥ ~20 cells/arm. The registered cheap heuristic (spread) is direction-blind and governs. Re-registration recommended for any future round (see research note) |
| 5 | Keys ≥ champion AND ≥ 90% | **PASS** — v6 35.0/36 (97.2%) vs champion 33.5/36 (93.1%); round A alone: 95.8% vs 91.7% |
| 6 | Framing invariance | **PASS both arms** — same fatal flaw, same top-2 set, structurally equivalent decision rules across hype/neutral/brutal; both skeptical-register runs explicitly refused requested brutality; no doom inflation (skeptical runs carried the lowest or equal overall estimates) |
| 7 | Negative fixture | **PASS** — v6 DEFLATED (246 words, explicit "full premortem would be overkill", real gotchas: permanent RSS redirect + never lapse, Apple Podcasts Connect claim-before-move, analytics export, publish-after-confirmation). Champion: CEREMONY (3,861 words, six-mode autopsy, adversary = "Spotify — not malicious, indifferent", 8 tripwire rows) — the known latent restraint hole, now key-verified on a second fixture |
| 8 | Instrument checks | **PASS** — inter-judge agreement 135/135 (A) and 189/189 (B) within 1 pt; controls gap 17.25/17.28 pts vs floor 10; within-arm spreads printed in scorecard output |

## 3. What the round proved

1. **Delta B (tie-pair enumeration) works.** Champion: 9/9 runs carry exactly one mechanical ladder violation (a second adjacent tied pair inside a three-way ~10% rung — the identical signature every time). v6: 3/9. Five v6 runs restructured to a single two-way tie or none — the enumeration clause changed ladder *construction*, not just checking. Auditor-2's systematic note: the residual violations in both arms all come from three-way ties, which the current rule text ("at most one tie") permits executors to attempt and the mechanical reading then rejects. The v7-recipe fix is structural: a tie spans exactly two modes, never three.
2. **Delta A (de-ordinalization + mechanical scan) works.** Narrow-census machinery leaks: champion ~19 items across 9 runs (stage-number cross-references in 5 of 9 runs — including R4 citing "Stage 4"/"Stage 5" four times in a report containing no such headings) vs v6 ~1 item across 9. The champion's latent defect, first documented in the Kimi round-2 note, reproduced on a fresh slate and fresh judges; v6's template rename eliminated the leak class almost entirely.
3. **The restraint machinery generalizes.** v6's proportionality screen deflated a fixture it had never seen (podcast RSS migration), with correct real-world gotchas, while the champion ran full ceremony — replicating the Kimi negative-fixture finding on an uncompromised fixture (their newsletter fixture is burned: its answer is quoted inside v4/v5's screen text).
4. **v6's detection is better on real keys.** 97.2% vs 93.1% strict; v6 caught all 4 Brief-G keys in all 3 runs (including the credentialing-doesn't-transfer omission), and run R2 additionally surfaced a *real, unplanted* flaw — Oregon's agritourism event-count ceiling (≈18 events/yr) sits below the plan's 24-event success definition — which two judges independently called the most valuable finding in the venue group.
5. **The harness's conjunctive-guard philosophy held.** A candidate that won totals (+2.67), swept 12/12 forced choices, beat keys, fixed both targeted defects, and regressed nothing was still not adopted, because one pre-registered line (D7's noise band at n=9 runs/arm) wasn't met as written. That is the designed behavior: totals measure added value; the gate refuses under-evidenced adoption. The evidence it "wanted" exists (sign test p≈6×10⁻⁵) but under a statistic the pre-registration reserved for larger designs — a bar mis-set, now documented for future re-registration, not silently bent.

## 4. Adjudication notes

1. **Auditor-A census deviation (condition 2).** The executed auditor prompt included "tag or class names" beyond the pre-registered census definition, sweeping in the urgency-tier labels and calibration-review line — content the rubric's own D5=7 and D7=7 anchors demand on the page. Its reading would double-charge the same ink as +D5/+D7 and −D9. Both readings reported; pre-registered text governs; prompt drift logged as a harness lesson (auditor prompts must quote the pre-registered census verbatim, never paraphrase-and-extend).
2. **Session-limit event (augmentation).** Two candidate-arm r3 executors hit the session usage limit on their final acknowledgment turn. Both output files were verified complete before the failure (full five-section structure, complete closings, in-profile word counts, timestamps pre-limit); no cell was re-run, no post-reset asymmetry exists between arms. Recorded for transparency.
3. **Code/judge-ID namespace collision.** Blind code J3 (framing cell) collides with judge ID J3. Harmless here (judges saw only their own ID; the J3 file was auditor-scoped), but future rounds should reserve disjoint namespaces.
4. **Pre-registration discipline:** gate written before execution; addendum written before augmentation; no goalpost moved after any result was seen; conservative/pre-registered readings governed both instrument disagreements; champion never modified (md5 `c1588714066e12b4415ab2f4a6bb3d3c` / `23af6c7883d0c6e911c72a63bbfb8214` verified at open and close).

## Final state
- **Shipped/installed:** `premortem-evolved` v2 (champion), unchanged, at `~/.claude/skills/premortem-evolved/`.
- **Discarded as candidate:** v6 branch (`arms/m2/`, hashes in `candidate/v6-hashes.txt`), preserved for reference with full diffs.
- **Product of the round:** `RESEARCH-NOTE-round3.md` — the validated delta inventory with round-3 evidence attached, and the fully specified v7 recipe + re-registered bars for any future round. Any such round is a fresh decision; nothing auto-spawns.
