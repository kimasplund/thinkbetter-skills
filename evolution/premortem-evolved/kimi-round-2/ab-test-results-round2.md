# Round-2 A/B: champion (premortem-evolved v2) vs challenger (v3, 21 cherry-picked deltas)

**Pre-registered spec:** `research2/design-spec-v3.md` §8 (harness v2) and §8.5 (8-condition adoption rule).
**Data:** 27 runs (2 skills × 3 briefs × 3 runs + 3 controls + 4 framing + 2 fixtures), 3 persona judges (crossed design, every brief double-judged), 1 cross-check auditor, 3 key-verification verifiers. All scoring blind; mapping sealed in `SEALED-MAPPING.json`.

## Verdict: NO ADOPTION — v3 branch discarded per the pre-registered symmetric-loss clause; champion stands. Re-mined candidate (v4) + scoped retest follows below.

## 1. The scorecard (pooled judges, n=18 per skill)

| Dim | Champion | Challenger | Margin | Note |
|---|---|---|---|---|
| D1 specificity (1–7) | 6.67 | 6.94 | +0.28 | |
| D2 causal chaining (1–7) | 6.67 | 7.00 | +0.33 | |
| D3 probability honesty (1–5) | 5.00 | 4.89 | **−0.11** | auditor cross-check: 5.00 vs **4.56** |
| D4 flaw detection (1–5) | 5.00 | 5.00 | 0.00 | key-verified: 32.5/36 vs **34.5/36** |
| D5 rebuild actionability (1–7) | 5.33 | 7.00 | **+1.67** | tiers, dates, proportionality, falsifiers, prevent/limit/accept |
| D6 adversarial depth (1–7) | 6.89 | 6.89 | 0.00 | both at ceiling |
| D7 tripwires (1–7) | 5.67 | 7.00 | **+1.33** | re-upgrade rows, early-chain, calibration review |
| D8 cold tone (1–5) | 5.00 | 5.00 | 0.00 | both cold; tone guardrails held |
| D9 length/bloat (1–5) | 4.61 | 4.33 | **−0.28** | challenger ~10% longer; judges docked length |
| **Total (55)** | 50.83 | 54.06 | +3.22 | |

## 2. The 8 pre-registered conditions

| # | Condition | Result |
|---|---|---|
| 1 | ≥ champion on all nine dims | **FAIL** (D3 −0.11, D9 −0.28) |
| 2 | Strictly better on ≥3 of {D3,D4,D5,D7} | **FAIL** — only D5, D7 (2 of 4); D3/D4 pinned at ceiling |
| 3 | No D3/D8 regression | **FAIL** — D3 regressed on both instruments (judges −0.11; auditor −0.44: unexplained rung inversions, e.g. a 5% mode ranked above a 10% mode) |
| 4 | D4 key-verified ≥ champion's strict rate; 100% bar on new keys | **FAIL on the bar** — challenger 34.5/36 (95.8%); champion 32.5/36 (90.3%). Challenger beats champion on the same keys but neither holds 100% |
| 5 | D9 ≥ champion | **FAIL** (4.33 vs 4.61) |
| 6 | Framing-invariance gate (Brief D hype vs skeptical) | **PASS, both arms** — fatal flaw / top-2 set / decision rule invariant; "be brutal" moved no ranking (identical ~65–70% overall estimates across framings) |
| 7 | Negative-fixture gate (trivial newsletter migration must deflate) | **FAIL, both arms** — both ran the full 5-stage ceremony (auditor: CEREMONY, D9=1 each). Challenger admitted "padding would be filler" and ran it anyway, including *all* optional apparatus |
| 8 | Instrument checks | **PASS** — controls gap 27.8/31.1 pts (floor 8); inter-judge agreement 100% (21/21 cells within 1 pt on every dim); variance gate clean (within-skill sd ≤0.76 ≪ margins); judges' forced choices 6/6 challenger |

## 3. What the round proved

1. **The cherry-picked deltas work where aimed.** D5 +1.67 and D7 +1.33 are the largest dimension margins in either round; key-verified detection rose 32.5→34.5; the challenger's rebuilds (tiered dated changes, falsifiers, prevent/limit/accept honesty, priced acceptance) are what judges cited in all six forced choices.
2. **The 21-delta stack regressed two guard dimensions.** D3: v3 runs produced probability-order inversions the champion never did (4 of 9 reports docked by the auditor) — the new mandates pressure the ladder. D9: report-visible additions stacked ~10% more length without displacement discipline; both judge panels noticed.
3. **Both skills share a restraint hole.** Neither can say "this plan is too small for a premortem." The negative fixture caught a real gap that predates v3 — the strongest single finding of the round.
4. **Framing robustness is excellent in both.** Hype and "be brutal" framings produce identical verdicts. The F20 counter-sycophancy sentence shipped in v3 was not strictly needed for this — the champion was already invariant — but it did no harm (D8 flat).

## 4. Adjudication notes

- Condition 4's absolute 100% bar was written expecting round-1 champion performance to persist; on the harder round-2 keys neither arm holds 100%. The relative reading (challenger ≥ champion's same-keys rate) passes 95.8% ≥ 90.3%. Both readings are reported; the condition fails on the pre-registered absolute text.
- Condition 3's D3 regression: judges saw −0.11 (within noise); the auditor — the round-1-validated instrument for exactly this dimension — saw −0.44 with named evidence (rung inversions whose tie notes don't cover them). Conservative reading governs: regression.

## 5. v4 re-mine directive (branch discarded; re-derived from the same recon inventory + failure data)

v3 is discarded as a candidate; the deltas remain the inventory, now with failure data attached. v4 must:
1. **Add an intake proportionality screen (new mechanism, fixture-driven):** if the plan is small, reversible, and low-stakes, deliver the 1–2 real checks plus "a full premortem is overkill" — and stop. The ceremony is for plans with irreversible commitments or real capital at stake.
2. **Repair the ladder interaction (D3):** the ranking IS the probability order. A mode promoted for structural reasons (most-certain attack, floor mandates) must be re-laddered, not re-ordered; every out-of-order placement fails gate 5. Tie-breaks must cover every non-ascending adjacent pair.
3. **Length displacement, not stacking (D9):** the report-visible additions (paper-tiger table, calibration line, gap check, tiers) must displace prose, not add to it — cap the autopsy at ~7 modes × tight fields, changes table ≤8 rows, tripwires ≤12 rows with mandatory merging, and state a per-report length ceiling.
4. **Keep the validated wins intact:** tiers+dates, falsifiers, proportionality, prevent/limit/accept, paper-tiger register, calibration review, commitment ask, most-certain-first attack, existing-guard check, boring floor, incentive/sustainment classes, citation standard, reverse autopsy (conditional), tone pair.
5. **Seasonality prompt** in the Timing class (both arms under-causalized the April-into-summer ramp; the class prompt should name launch-season troughs).

## 6. Scoped retest protocol (fixed BEFORE running v4)

- Cells: v4 × {fixture ×1, Brief D hype + skeptical ×1 each, Briefs D/E/F ×1 neutral} = 6 runs.
- Comparison set: champion's existing 9 main runs + 2 fixture/framing runs (same briefs, already scored).
- Judges: 2 persona judges score the 3 neutral v4 runs blind against 3 champion runs per brief (same rubric); auditor re-runs D3/D9 cross-check + both fixture gates.
- Key verification: v4's 3 neutral runs must go 12/12 on the planted flaws.
- **v4 passes iff:** D3 ≥ champion (both instruments), D9 ≥ champion, D5/D7 retain ≥ half the v3 margin (≥ +0.8 / ≥ +0.65), key-detection 12/12, fixture DEFLATES, framing invariant. Anything less → champion ships unchanged and the deltas ship only as a research note.

---

## 7. v4 scoped retest — results and final verdict

**Data:** 6 v4 runs (fixture J1; Brief D hype T2 + skeptical D9; neutral B8/Y8/K7), judged blind against the champion's 9 main runs by 2 fresh persona judges (RA operator/CFO, RB founder), plus the retest auditor (D3/D9 cross-check, framing gate, fixture gate) and the key verifier (12 planted-flaw cells). Full instruments: `scores/judge-RA.md`, `scores/judge-RB.md`, `scores/auditor-retest.md`, `scores/keyverify-v4.md`. Mapping remained sealed throughout.

### 7.1 Pooled retest scorecard (judges RA+RB; champion n=18, v4 n=6)

| Dim | Champion | v4 | Margin | Gate requirement | Result |
|---|---|---|---|---|---|
| D1 specificity (1–7) | 6.67 | 6.83 | +0.17 | — | |
| D2 causal chaining (1–7) | 6.00 | 7.00 | +1.00 | — | |
| D3 probability honesty (1–5) | 4.94 | 5.00 | +0.06 | ≥ champion, both instruments | **PASS** (auditor: 5.00 = 5.00) |
| D4 flaw detection (1–5) | 5.00 | 5.00 | 0.00 | — | |
| D5 rebuild actionability (1–7) | 6.00 | 7.00 | +1.00 | ≥ +0.80 | **PASS** |
| D6 adversarial depth (1–7) | 6.22 | 6.33 | +0.11 | — | |
| D7 tripwires (1–7) | 5.50 | 7.00 | +1.50 | ≥ +0.65 | **PASS** (exceeds v3's +1.33) |
| D8 cold tone (1–5) | 5.00 | 5.00 | 0.00 | — | |
| D9 length/bloat (1–5) | 4.61 | 4.33 | **−0.28** | ≥ champion | **FAIL** (auditor: 4.00 vs 5.00 — both instruments agree) |
| **Total (55)** | 49.94 | 53.49 | +3.55 | | |

Forced choices: **6/6 for v4** (RA: B8, Y8, K7; RB: B8, Y8, K7).

### 7.2 Non-judge gates

| Gate | Requirement | Result |
|---|---|---|
| Key detection | 12/12 strict | **FAIL on the absolute text** — 11.5/12 (B8 3.5: D4 ~; Y8 4.0; K7 4.0). Relative reading: 95.8% ≥ champion's 90.3% (passes) |
| Negative fixture | DEFLATE | **PASS** — 11 lines / ~1.8KB, restraint call on the page, D9 5 / D8 5, and it caught the real non-obvious trap (Substack paid subscriptions live in Substack-tied Stripe; porting is support-gated and not weekend-self-serve) plus SPF/DKIM, suppression carryover, sender warming |
| Framing invariance | invariant | **PASS** — hype/neutral/skeptical are the same finding in three registers; decision rules structurally identical three-leg AND gates; "be brutal" moved nothing (~60–65% overall miss across framings; the *hype* run declined a fatal flaw while the *neutral* run named one — framing effect runs against register prediction, i.e., noise) |

### 7.3 Verdict: **NO ADOPTION of v4. Champion (premortem-evolved v2) stands and ships unchanged.**

The pre-registered gate is conjunctive and fails on two conditions: D9 (−0.28 judges, −1.00 auditor) and the absolute 12/12 key bar (11.5). Per §6: "Anything less → champion ships unchanged and the deltas ship only as a research note." The research note is `RESEARCH-NOTE-deltas.md`.

### 7.4 Adjudication notes

1. **What the repairs fixed.** R2 (ladder repair) fully restored D3: zero dockable inversions across all three v4 runs, every tie-break written and covering every tied pair — versus v3's 4-of-9 docked reports. R1 (proportionality screen) fixed the restraint hole that was round-2's strongest finding: the fixture deflated for the first time in any round, with genuine migration gotchas rather than filler. R3 (length budgets) fixed raw bloat: v4 full runs are 32–36KB, inside the champion's own 32–38KB band.
2. **Why D9 still failed.** Every v4 D9 dock across all three instruments was for **process leakage, not length**: the screen narrating itself on the page ("fails the low-stakes screen, so it gets the full treatment" — docked by both judges), stage scaffolding ("Stage 4", "Section 4 resolves…"), and the coda-block stack restating mode prose (auditor). The budgets capped rows but did not forbid restatement or self-narration. The repair machinery works; its footprint on the page is what judges priced.
3. **The key bar.** 12/12 has never been met by any arm on this matrix (champion 32.5/36, v3 34.5/36, v4 11.5/12). The sole v4 miss is D4's seasonality half — causalized but direction-inverted (winter trough, not the summer hot-coffee slowdown), the identical failure mode as all three champion runs (0✓/3~). v3 remains the best D4 performer (2✓/1~) *without* the seasonality prompt. Consistent with round-2 condition-4 adjudication: the absolute bar fails as written; the relative reading (95.8% ≥ 90.3%) passes. Both reported.
4. **Consistency note on Q6:** under RB's harsher D9/D3 eye, the champion's Q6 run was itself docked (D3 4, undefended tie) — within-instrument fairness held; no arm was graded against a standard the other escaped.
5. Pre-registration discipline was maintained exactly as in round 2: no goalpost movement after results were seen; conservative reading governs cross-instrument disagreements; the champion directory was never modified (md5-verified pre/post).

## 8. Forward path (documented, not executed)

A v5 candidate is fully specified by the failure data and would differ from v4 by exactly two craft deltas:
1. **Silence the screen:** the proportionality call must never be narrated as process. Either invisible in output, or expressed once as plan framing ("real capital and a signed five-year lease are at stake") — never as "the screen says."
2. **No-restatement clause:** extend R3's budgets with "no coda block may restate a mode's own paragraph; each closing block must add information not on the page already."
(Optionally re-ground the seasonality prompt with direction: name the demand *trough* in the launch window, not just "consider seasonality.")

v5 would require the identical scoped retest (6 cells, same gates, same conjunctive rule — with the key bar re-registered as *relative-to-champion with a 90% absolute floor*, since the absolute 100% bar is now known to be unattainable on this matrix by any arm). Whether to run that cycle is the owner's call.

---

## 9. v5 pre-registration (written BEFORE any v5 run; candidate authored from v4 + the §8 recipe)

**v5 = v4 + exactly three deltas** (verified by diff, nothing else changed):
1. Screen silence: when the proportionality screen fails open, it leaves no trace on the page (no name, outcome, or narration; proportionality expressible once as plan framing only).
2. No-restatement clause + machinery-leak enumeration extended to stage/section numbers, gate names, screen outcomes.
3. Seasonality prompt direction-grounded (category demand by ramp month; traffic peaks can be category troughs).

**Cells (identical to the v4 retest):** v5 × {fixture ×1, Brief D hype ×1, Brief D skeptical ×1, Briefs D/E/F neutral ×1 each} = 6 runs.
**Blind codes:** fixture=L6, D-hype=G4, D-skeptical=S7, D-neutral=N9, E-neutral=W5, F-neutral=T9 (recorded in SEALED-MAPPING.json).
**Comparison:** champion's 9 main runs re-scored alongside by the same panels (crossed: RC judges D=[V2,U2,N9,E8], E=[X3,D5,C7,W5], F=[Q6,T9,F5,P3]; RD judges D=[N9,E8,V2,U2], E=[X3,D5,W5,C7], F=[Q6,P3,F5,T9]).
**Instruments:** 2 fresh persona judges (RC, RD) on rubric v2; retest auditor (D3/D9 cross-check, framing gate on the N9/G4/S7 trio, fixture gate on L6); key verifier (12 cells on N9/W5/T9).

**v5 passes iff ALL of (conjunctive, no partial credit):**
1. D3 ≥ champion on both instruments (judges pooled + auditor)
2. D9 ≥ champion on both instruments
3. D5 ≥ +0.80 and D7 ≥ +0.65 vs champion (judges pooled)
4. Key detection ≥ 11/12 (90% absolute floor) AND ≥ champion's pooled strict same-cells rate (32.5/36 = 90.3%)
5. Fixture DEFLATES per the §fixtures gate
6. Framing invariant per the §fixtures gate

**Anything less → champion ships unchanged, v5's deltas join RESEARCH-NOTE-deltas.md, and this session's evolution loop closes.** No v6 will be auto-spawned; any further cycle is a fresh decision.

---

## 10. v5 retest — results and final verdict

**Data:** 6 v5 runs (fixture L6; Brief D hype G4 + skeptical S7; neutral N9/W5/T9), judged blind against the champion's 9 main runs by 2 fresh persona judges (RC enterprise-risk-officer, RD early-stage investor), plus the retest auditor and key verifier. Instruments: `scores/judge-RC.md`, `scores/judge-RD.md`, `scores/auditor-retest-v5.md`, `scores/keyverify-v5.md`. Mapping sealed throughout; champion untouched (md5-verified).

### 10.1 Pooled retest scorecard (judges RC+RD; champion n=18, v5 n=6)

| Dim | Champion | v5 | Margin | Gate requirement | Result |
|---|---|---|---|---|---|
| D1 specificity | 6.44 | 6.83 | +0.39 | — | |
| D2 causal chaining | 6.22 | 7.00 | +0.78 | — | |
| D3 probability honesty | 5.00 | 5.00 | 0.00 | ≥ champion, **both instruments** | judges: parity ✓ · auditor: **4.33 vs 5.00 ✗ → FAIL** |
| D4 flaw detection | 5.00 | 5.00 | 0.00 | — | |
| D5 rebuild actionability | 5.56 | 7.00 | +1.44 | ≥ +0.80 | **PASS** |
| D6 adversarial depth | 6.39 | 6.17 | −0.22 | — | |
| D7 tripwires | 5.50 | 7.00 | +1.50 | ≥ +0.65 | **PASS** |
| D8 cold tone | 5.00 | 5.00 | 0.00 | — | |
| D9 length/bloat | 4.44 | 4.33 | **−0.11** | ≥ champion, **both instruments** | judges: ✗ · auditor: **3.33 vs 5.00 ✗ → FAIL** |
| **Total (55)** | 49.56 | 53.33 | **+3.78** | | |

Forced choices: **6/6 for v5** (RC: N9, W5, T9; RD: N9, W5, T9).

### 10.2 Non-judge gates

| Gate | Requirement | Result |
|---|---|---|
| Key detection | ≥ 11/12 (90% floor) AND ≥ champion's 90.3% | **PASS** — 11.5/12 = 95.8% (N9 3.5: D4 ~; W5 4.0; T9 4.0) |
| Negative fixture | DEFLATE | **PASS** — 9 lines, "a full premortem is overkill here" on the page, D9 5 / D8 5, real gotchas (Stripe paid-sub state carryover; sender-reputation warm-up; keep-Substack-live safeguard) |
| Framing invariance | invariant | **PASS** — same fatal finding, identical top-2 set, structurally equivalent pre-spend gate rules across registers; overalls 65/65/70%; no doom inflation under "be brutal" |

### 10.3 Verdict: **NO ADOPTION of v5. Champion (premortem-evolved v2) stands. The evolution loop closes per the §9 pre-registration — no further candidate will be auto-spawned.**

### 10.4 Adjudication notes

1. **The D3 split decision.** Both judges scored every v5 run 5/5 on D3 (parity). The auditor — the round-1-validated instrument for exactly this dimension, applying the ladder rule mechanically — docked W5 and T9 one rung each: both carry a **second tie at the 5% rung with no written ordering justification**, violating the "at most one tie, and the tie-break must cover every tied pair" clause. The rule is in the skill; executor self-verification did not enumerate all tied pairs. Conservative reading governs cross-instrument disagreement (established precedent): regression. Note the regression is in *compliance*, not design — v4's runs complied fully (5/5/5).
2. **D9 moved in the right direction and still failed.** Judges: −0.28 (v4) → −0.11 (v5). But the specific leak class persisted: "Stage 4" cross-references in 3 of 5 full runs (W5, T9, G4) despite an explicit written ban — both judges and the auditor caught them independently (RD grepped for the pattern). The auditor additionally docked T9 for ceremony-on-a-simpler-plan. **Key structural finding: the champion has the same latent defect** — RD docked 5 of 9 champion runs for stage-reference leaks — so the judges' relative bar already prices a shared base rate. A prose ban inside the skill is insufficient when the report template itself is organized as named stages; the durable fix is mechanical (a pre-delivery grep gate for "Stage N"/section ordinals/screen names in the verification checklist) or de-ordinalized template section names.
3. **D4's seasonality direction resisted its third consecutive fix.** With the direction-grounded prompt in the references, N9 still substituted the inverted mechanism (iced-drink season framed as *helping*). Score across all builds on this cell: champion 0✓/3~, v3 2✓/1~, v4 0✓/1~, v5 0✓/1~. This key cell measures something prompting has not fixed; plausible cause is that the brief's surface cues (April open, patio season) actively bias executors toward the inversion. Left as a documented hard cell rather than chased further — chasing it risks teaching to the test.
4. **The value story is intact and unrebutted:** +3.78 total, 6/6 forced choices, D5 +1.44 / D7 +1.50, key detection 95.8% > champion's 90.3%, fixture deflation replicated, framing robust. Every candidate beat the champion on totals and forced choices across three rounds; none was adopted, because the guard dimensions are conjunctive. That is the harness behaving exactly as specified: totals measure added value, conjunctive guards protect existing value.
5. Pre-registration discipline held: the §9 gate was written before any v5 run; the key bar was re-registered with its rationale *before* execution; no goalpost moved after results arrived.

---

## 11. evo-88905a pre-registration (written BEFORE any evo run; candidate supplied externally by the owner)

**Candidate provenance.** `premortem-evolved-evo-88905a` arrived as an external evolution of the v5 branch (SKILL.md only, md5 `e6ba579f1da097bacd89f679e1587f18`; its own `references/failure-class-checklist.md` was not supplied). Diff-verified: candidate = v5 + exactly five own deltas:
1. **Full de-ordinalization** — "five stages"→"five sections"; Step 1/2/3 → First/Next/Then; every "Stage N" cross-reference → role names (intake / the verdict / the rebuild / the adversary / the autopsy). Grep-verified: zero "Stage N"/"Section N" strings remain. This is the §10.4.2 structural ("durable") fix for the D9 ordinal-leak class.
2. **De-tilded approximations** throughout (~5→5, ~60%→60%, ~6,500→6,500, cut to ~7→7).
3. **Mechanical leak-scan sentence**: "The checklist ends in a mechanical leak scan — run it as a literal text search over the report, never from memory." Targets the v5 D3/D9 *compliance* failures (§10.4.1–2).
4. **NEW closing machinery — "Audit Handoff":** a one-paragraph closing block summarizing the top failure mode and the kill condition "for the daily audit trail." Unvetted; in constructional tension with the no-restatement clause (a summary of the top mode is near-definitional restatement). D9/D8 are the pricing instruments.
5. **Description trigger added**: "Use when a premortem needs an audit-trail handoff for the daily treasury audit." Trigger-surface only; no effect on execution cells.

**Test-condition caveat (declared before execution):** the candidate's own references file was not supplied; cells run with the v5 references file (md5 `9911d88a5361b8625f1df50e45c9e685`), which does NOT literally end in a mechanical leak scan. Delta 3's sentence is self-contained ("literal text search over the report"), so executors can comply; if compliance ambiguity decides a guard dimension, that is recorded as a finding about the candidate's packaging, not excused.

**Cells (identical to the v4/v5 retests):** evo × {fixture ×1, Brief D hype ×1, Brief D skeptical ×1, Briefs D/E/F neutral ×1 each} = 6 runs.
**Blind codes:** fixture=A5, D-hype=R5, D-skeptical=C2, D-neutral=M7, E-neutral=A2, F-neutral=V7 (SEALED-MAPPING.json).
**Comparison:** champion's 9 main runs re-scored alongside by the same panels (crossed: RE judges D=[V2,U2,M7,E8], E=[X3,D5,C7,A2], F=[Q6,V7,F5,P3]; RF judges D=[M7,E8,V2,U2], E=[X3,D5,A2,C7], F=[Q6,P3,F5,V7]).
**Instruments:** 2 fresh persona judges (RE operations-turnaround executive, RF unit-economics CFO) on rubric v2; retest auditor (D3/D9 mechanical cross-check — ordinal grep extended to BOTH "Stage N" and "Section N", plus machinery/audit-trail leakage; framing gate on the M7/R5/C2 trio; fixture gate on A5); key verifier (12 cells on M7/A2/V7, same KEY-MATRIX).

**evo-88905a passes iff ALL of (conjunctive, no partial credit — identical to §9):**
1. D3 ≥ champion on both instruments (judges pooled + auditor)
2. D9 ≥ champion on both instruments
3. D5 ≥ +0.80 and D7 ≥ +0.65 vs champion (judges pooled)
4. Key detection ≥ 11/12 (90% absolute floor) AND ≥ champion's pooled strict same-cells rate (32.5/36 = 90.3%)
5. Fixture DEFLATES per the §fixtures gate
6. Framing invariant per the §fixtures gate

**Anything less → champion ships unchanged, evo-88905a's deltas join RESEARCH-NOTE-deltas.md (symmetric-loss clause), and the candidate is discarded like v3/v4/v5.** Pre-registered answer to the owner's question: "measurable improvement" = passing all six gates; totals and forced choices are reported but cannot substitute for a failed guard. No goalpost movement after results; conservative reading governs cross-instrument disagreement.

## 12. evo-88905a retest — results and verdict

**Data:** 6 evo runs (fixture A5; Brief D hype R5 + skeptical C2; neutral M7/A2/V7), judged blind against the champion's 9 main runs by 2 fresh persona judges (RE operations-turnaround executive, RF unit-economics CFO), plus the retest auditor and key verifier. Instruments: `scores/judge-RE.md`, `scores/judge-RF.md`, `scores/auditor-retest-evo.md`, `scores/keyverify-evo.md`. Mapping sealed throughout; champion untouched (md5-verified pre/post). Candidate tested with the v5 references file per the §11 declared caveat.

### 12.1 Pooled retest scorecard (judges RE+RF; champion n=18, evo n=6; totals recomputed from dimension scores — see §12.4.5)

| Dim | Champion | evo | Margin | Gate requirement | Result |
|---|---|---|---|---|---|
| D1 specificity | 6.61 | 6.67 | +0.06 | — | |
| D2 causal chaining | 6.50 | 7.00 | +0.50 | — | |
| D3 probability honesty | 4.78 | 5.00 | +0.22 | ≥ champion, **both instruments** | judges: ✓ · auditor: **4.67 vs 5.00 ✗ → FAIL** |
| D4 flaw detection | 4.94 | 5.00 | +0.06 | — | |
| D5 rebuild actionability | 5.50 | 7.00 | +1.50 | ≥ +0.80 | **PASS** |
| D6 adversarial depth | 5.89 | 5.83 | −0.06 | — | |
| D7 tripwires | 5.50 | 7.00 | +1.50 | ≥ +0.65 | **PASS** |
| D8 cold tone | 5.00 | 5.00 | 0.00 | — | |
| D9 length/bloat | 4.89 | 4.00 | **−0.89** | ≥ champion, **both instruments** | judges: **✗** · auditor: **3.00 vs 5.00 ✗ → FAIL** |
| **Total (55)** | 49.61 | 52.50 | **+2.89** | | |

Forced choices: **6/6 for evo** (RE: M7, A2, V7; RF: M7, A2, V7). Suspected-generic: none flagged by either judge.

### 12.2 Non-judge gates

| Gate | Requirement | Result |
|---|---|---|
| Key detection | ≥ 11/12 (90% floor) AND ≥ champion's 90.3% | **PASS** — 11.5/12 = 95.8% (M7 3.5: D4 ~; A2 4.0; V7 4.0) |
| Negative fixture | DEFLATE | **PASS** — 9 lines, "a full premortem is overkill here" on the page, D9 5 / D8 5, real gotchas (Stripe billing-state carryover test import; SPF/DKIM/DMARC sender warm-up; keep-Substack-live hedge) |
| Framing invariance | invariant | **PASS** — fatal flaw, top-2 modes (same order), and decision-rule structure invariant across registers; no doom inflation under "be brutal" (skeptical 65% = hype 65%). Robustness note: thresholds drift across registers (reserve floor $45k+$25k line / $60k / $120k; gate date Jan 2027 / Sep 2026); the "most dangerous" pick flips. Structural invariance holds; drift reported. |

### 12.3 Verdict: **NO ADOPTION of evo-88905a. Champion (premortem-evolved v2) stands, unchanged.** Gates 1 and 2 fail (D3 on the auditor instrument; D9 on both instruments); the conjunctive rule gives no partial credit. Per the §11 symmetric-loss clause, evo's deltas and failure data join RESEARCH-NOTE-deltas.md.

### 12.4 Adjudication notes

1. **The structural fix worked against its target class.** De-ordinalization eliminated the ordinal-leak class entirely: zero "Stage N"/"Section N" hits across all six cells (auditor grep-verified), and zero screen self-narration — the two classes that sank v4 and v5. This validates the §10.4.2 hypothesis: template-level de-naming beats prose bans.
2. **The new machinery became the new leak.** Every full report carries the Audit Handoff coda, which both judges and the auditor independently found restates verdict/top-mode content without adding information — the exact constructional tension pre-registered in §11 (a top-mode summary is near-definitional restatement under the no-restatement clause). V7 additionally leaked raw template-placeholder syntax ("Committed: [change] by [day]") — a newly observed leak class: unfilled template tokens. Net D9: judges −0.89 (v5 was −0.11), auditor 3.00 vs 5.00 (v5 was 3.33). Machinery growth was priced exactly as the guard dims are designed to price it.
3. **D3 compliance improved but didn't close.** 4 of 5 full runs now enumerate every tied pair with written tie-breaks (v5: 3 of 5); M7's 5%-rung pair (#6/#7) went uncovered → one dock, auditor 4.67 vs the champion's stable 5.00 bar. The mechanical leak-scan sentence targets text leaks, not ladder arithmetic; tie-coverage self-checks remain from-memory. The untested mechanical fix is a literal ladder linter (recompute descending order + enumerate all tied pairs before delivery) — recorded for any future round, not auto-spawned.
4. **D4's seasonality cell resisted its fifth consecutive build.** M7 inverted the mechanism again (credits the April→patio/iced-drink ramp as a strength, places the dip in winter) while genuinely causalizing the key-person half → ~. Cell record across builds: champion 0✓/3~, v3 2✓/1~, v4 0✓/1~, v5 0✓/1~, evo 0✓/1~. Stable hard cell; documented, not chased (teaching-to-the-test risk).
5. **Judge arithmetic integrity.** RE's written TOTAL rows run 5–6 points below the arithmetic sum of its own dimension scores on all 12 reports (uniform slip); RF's totals are exact except E8 (47 written vs 48 computed). Pooling is dimension-major by design, so totals were recomputed from dimension scores (champion 49.61, evo 52.50); no dimension score is affected and every margin's direction is unchanged under either totaling.
6. **The pattern is now four-deep.** v3, v4, v5, and evo-88905a all beat the champion on totals (+2.89 here) and swept forced choices (6/6); none was adopted. The evo round demonstrates both halves of the guard design at once: the guards correctly refused a genuine value improvement because it arrived with a guard regression, and the pre-registered definition of "measurable improvement" (pass all six gates) kept the owner's question settled by the harness rather than by the totals.
7. **Pre-registration discipline held:** §11 gate written before any run; the references-file caveat declared before execution; no goalpost movement after results; conservative reading applied (the auditor leg governs D3 disagreement; both legs failed D9 outright). Champion md5 identical pre/post.

## 13. v6 pre-registration (written BEFORE any v6 run; candidate authored from the validated delta inventory, 2026-08-22)

**Design basis.** v6 assembles only what four rounds of failure data validated, and surgically removes what they falsified. v6 = evo-88905a with exactly five reversals/additions (diff-verifiable):
1. **Audit Handoff section deleted** (validated failure, §12.4.2) and the "daily treasury audit" description trigger removed.
2. **Calibration review rewoven as the final tripwire-table row** (dated, thresholded) instead of a placeholder-laden coda block — preserving the D7 additive rung judges credit while removing the machinery the auditor docks.
3. **Commitment ask kept; recording apparatus cut** — the ask stays conversational ("one move"), and nothing about it is recorded on the page (removes the `[change] by [day]` template-token leak class).
4. **NEW: `scripts/pre_delivery_check.py`** — the mechanical pre-delivery gate the research note prescribed: greps leaked machinery (stage/section ordinals, screen narration, gate names, audit-handoff/file-append apparatus, unfilled template tokens), recomputes the ladder (sum, descending order), and enumerates every tied pair with mode numbers; SKILL.md and checklist item 19 require running it and fixing every flag before delivery. **Instrument validation:** the linter reproduces every documented human tie/leak judgment in the corpus (auditor's M7 call; RF's V2/X3/C7/Q6 docks; R5/C2/A2/U2/P3 acceptances) and is stricter than lenient readings on second tied rungs (E8/D5/F5) per the rule's plain text — which v4 proved satisfiable.
5. **References de-ordinalized** (the v5 references still carried "Step 2"/"Stage 3" backstage ordinals) and checklist item 14 updated for the calibration row.

**Instrument-symmetry correction (declared before execution).** Linter validation exposed that the historical auditor D3 champion bar (5.00) was produced WITHOUT full tie enumeration: under exhaustive enumeration, 6 of 9 champion neutral reports carry a tie-rule violation (uncovered pairs on V2/X3/C7/Q6; second tied rungs on E8/D5/F5). Likewise 5 of 9 champion reports carry stage/section-ordinal leaks (matching RD's judge-side docks, §10.4.2). For this round, **the auditor applies the linter's enumeration to BOTH arms symmetrically** (script-assisted, then rubric judgment). The gates remain "≥ champion on both instruments" — champion's instrument scores are whatever the symmetric instrument yields this round. This is instrument repair, not goalpost movement: the comparison standard (≥ champion, both instruments, conjunctive) is unchanged.

**Cells (identical to prior retests):** v6 × {fixture ×1, Brief D hype ×1, Brief D skeptical ×1, Briefs D/E/F neutral ×1 each} = 6 runs.
**Blind codes:** fixture=B4, D-hype=G7, D-skeptical=K2, D-neutral=E2, E-neutral=H4, F-neutral=F7 (SEALED-MAPPING.json).
**Comparison:** champion's 9 main runs re-scored alongside by the same panels (crossed: RG judges D=[V2,U2,E2,E8], E=[X3,D5,C7,H4], F=[Q6,F7,F5,P3]; RH judges D=[E2,E8,V2,U2], E=[X3,D5,H4,C7], F=[Q6,P3,F5,F7]).
**Instruments:** 2 fresh persona judges (RG insolvency practitioner, RH platform-engineering lead) on rubric v2; retest auditor (linter-assisted D3 enumeration and D9 leak scan on BOTH arms, framing gate on the E2/G7/K2 trio, fixture gate on B4); key verifier (12 cells on E2/H4/F7, same KEY-MATRIX, hard-grader rule).

**v6 passes iff ALL of (conjunctive, no partial credit — identical structure to §9/§11):**
1. D3 ≥ champion on both instruments (judges pooled + auditor)
2. D9 ≥ champion on both instruments
3. D5 ≥ +0.80 and D7 ≥ +0.65 vs champion (judges pooled)
4. Key detection ≥ 11/12 (90% absolute floor) AND ≥ champion's pooled strict same-cells rate (32.5/36 = 90.3%)
5. Fixture DEFLATES per the §fixtures gate
6. Framing invariant per the §fixtures gate

**Anything less → champion ships unchanged and v6's deltas join the research note.** If v6 passes all six gates, it is adopted as the new champion and installed in place of v2 (with the installed copy's name normalized to `premortem-evolved`). No goalpost movement after results; conservative reading governs cross-instrument disagreement.

## 14. v6 retest — results and verdict

**Data:** 6 v6 runs (fixture B4; Brief D hype G7 + skeptical K2; neutral E2/H4/F7) — every cell passed `pre_delivery_check.py` before delivery — judged blind against the champion's 9 main runs by 2 fresh persona judges (RG insolvency practitioner, RH platform-engineering lead), plus the symmetric linter-assisted auditor and the key verifier. Instruments: `scores/judge-RG.md`, `scores/judge-RH.md`, `scores/auditor-retest-v6.md`, `scores/keyverify-v6.md`. Mapping sealed throughout; champion untouched (md5-verified pre/post). Both judges' TOTAL rows arithmetic-verified against their own dimension sums (the §12.4.5 prompt fix worked).

### 14.1 Pooled retest scorecard (judges RG+RH, dimension-major; champion n=18, v6 n=6)

| Dim | Champion | v6 | Margin | Gate requirement | Result |
|---|---|---|---|---|---|
| D1 specificity | 7.00 | 7.00 | 0.00 | — | |
| D2 causal chaining | 6.44 | 7.00 | +0.56 | — | |
| D3 probability honesty | 4.78 | 5.00 | +0.22 | ≥ champion, **both instruments** | judges ✓ · auditor **5.00 vs 4.11 ✓ → PASS** |
| D4 flaw detection | 5.00 | 5.00 | 0.00 | — | |
| D5 rebuild actionability | 6.00 | 7.00 | +1.00 | ≥ +0.80 | **PASS** |
| D6 adversarial depth | 6.28 | 6.17 | −0.11 | — | |
| D7 tripwires | 6.00 | 7.00 | +1.00 | ≥ +0.65 | **PASS** |
| D8 cold tone | 5.00 | 5.00 | 0.00 | — | |
| D9 length/bloat | 4.11 | 3.50 | **−0.61** | ≥ champion, **both instruments** | judges: **3.50 vs 4.11 ✗** · auditor: 5.00 vs 3.56 ✓ **→ FAIL** |
| **Total (55)** | 50.61 | 52.67 | **+2.06** | | |

Forced choices: **6/6 for v6** (RG: E2, H4, F7; RH: E2, H4, F7). Suspected-generic: none flagged by either judge.

### 14.2 Non-judge gates

| Gate | Requirement | Result |
|---|---|---|
| Key detection | ≥ 11/12 floor AND ≥ champion's 90.3% | **PASS** — 11.5/12 = 95.8% (E2 3.5: D4 ~; H4 4.0; F7 4.0) |
| Negative fixture | DEFLATE | **PASS** — B4: 9 lines, "A full premortem is overkill here" on the page, two real checks (Stripe billing-state transfer; SPF/DKIM/DMARC sender warm-up), zero ceremony artifacts; linter confirms no ladder |
| Framing invariance | fatal flaw, top-2 modes, decision rule invariant (G7 vs K2, E2 as neutral context); a flip unique to the challenger blocks adoption | **FAIL** — fatal-flaw LABEL flips (G7 hype: "the cash architecture is [fatal]"; K2 skeptical and E2 neutral: "There isn't one — binding constraint"); top-2 hold only at category level (mode decomposition differs across registers); decision-rule structure holds but trigger numbers are register-dependent ($198k/$207k/$215k caps; 140/150/160 per day; cushion $10–20k vs $35–45k). No doom inflation (~70% = ~70%). Auditor verdict: PARTIAL PASS; the conjunctive rule gives no partial credit, and the label flip is unique to the challenger → gate FAILS |

### 14.3 Verdict: **NO ADOPTION of v6. Champion (premortem-evolved v2) stands, unchanged.** Gates 2 and 6 fail (D9 on the judges instrument; framing on the fatal-flaw label flip plus trigger-number drift); the conjunctive rule gives no partial credit. Per the §13 symmetric-loss clause, v6's validated deltas and failure data join RESEARCH-NOTE-deltas.md. Champion md5 identical pre/post (`c1588714066e12b4415ab2f4a6bb3d3c` / `23af6c7883d0c6e911c72a63bbfb8214`).

### 14.4 Adjudication notes

1. **The linter closed the D3 class completely — the first build ever to pass gate 1.** All six v6 cells passed the pre-delivery linter; the auditor's symmetric enumeration found every v6 tied rung single and fully covered (E2/H4/F7 = 5/5/5) with zero ordinal, stage/section, audit-handoff, or template-token leaks. v6 cleared the champion's *honest* bar (auditor D3 4.11 under full enumeration — the bar the historical 5.00 never faced) with room on both instruments (judges 5.00 vs 4.78). The mechanical pre-delivery gate is the validated fix for the tie-coverage failures that sank v3/v5 and the ordinal-leak classes that sank v4/evo.
2. **The D9 failure is a template-authored leak, and it survives the most charitable reading.** All three v6 neutral reports carry `**Consciously accepted (at most one):**` verbatim as a visible header (E2 L154, H4 L145, F7 L157); F7 adds a `| Paper-tiger re-upgrades (Track) |` row label (L197). Both strings trace to v6's SKILL.md itself (L92, L86): the instruction parenthetical is embedded in the output-facing header, and "paper-tiger re-upgrade signals" is backstage vocabulary inside the tier-tag instruction. Executors copy template headers verbatim, and the linter's token wordlist catches bracketed tokens but not the template's own phrasing — so both leaked through the mechanical gate undetected. The champion's template contains neither string and no champion report carries them. RH — who scored champion D9 5.00 across the board and docked v6 *only* for these leaks — alone flips the judges leg (4.00 vs 5.00; pooled 3.50 vs 4.11). Gate 2's failure therefore does not rest on RG's harsher reading.
3. **Rubric tension logged, not adjudicated into the gate (no goalpost movement).** RG docked v6 additionally for machinery the rubric's other dimensions REQUIRE — written tie-coverage sentences (D3's own rule), "Downgraded — guarded for now" demotion labels (D2/D7 anchors), tier tags (D5 anchor-7) — calling the set "worksheets with the scaffolding still bolted on." This is a genuine rubric-v2 tension (D9's "no machinery" anchor vs. mandated machinery), recorded for the harness. The gate stands as pre-registered; note 2 shows the verdict is unchanged without RG's reading.
4. **Framing: substance invariant; labels and numbers not.** The verdict's substance held across registers — no doom inflation under "be brutal" (~70% = ~70%; D8 anchor-5 in both framing cells, a genuine strength). But gate 6's letter requires the fatal flaw, top-2, and decision rule invariant: v6's fatal-flaw label flips between registers (hype names the cash architecture fatal; neutral and skeptical explicitly deny any fatal flaw) and the trigger numbers drift. The evo precedent (§12.2) tolerated threshold drift only because the fatal flaw and top-2 held strictly; v6 exhibits a label flip no prior arm showed — a flip unique to the challenger, which the §fixtures criterion says blocks adoption regardless of means. Root-cause hypothesis: nothing in the skill pins the verdict label or the trigger numbers to a single computation, so register pressure re-derives them.
5. **What v6 proved on the value side.** Totals +2.06, forced choices 6/6 (fifth consecutive challenger sweep), D5 +1.00 / D7 +1.00 — the urgency-tier / prevent-limit-accept rebuild machinery and the calibration-as-tripwire-row (dated in all three neutral reports: Oct 1 2027, Jan 2028, Sep 2 2027) are validated additive rungs with zero auditor D9 cost; the guarded-demotion table was credited on D2 (+0.56). D6 slipped −0.11: both judges noted v6's adversaries attacking the weakest joints rather than the steelmanned strongest one (champion C7's steelman-attacking adversary remains the round's best); recorded as an open design item.
6. **D4's seasonality cell resisted its sixth consecutive build** (E2 ~). Cell record: champion 0✓/3~, v3 2✓/1~, v4/v5/evo/v6 0✓/1~ each. Stable hard cell; documented, not chased (teaching-to-the-test risk).
7. **Instrument health.** Judge totals verified exact for both panels. Auditor logged two linter limitations, neither affecting v6 scores: the TIE_LINE regex missed F5's "the tie with #3 breaks in #3's favor" phrasing (evidence corrected, score unchanged — the 5% rung was genuinely uncovered), and U2's "Section 4/3" references resolve to real visible headings (auditor override: reader-resolvable cross-references, not machinery). Conservative reading governed the one cross-instrument disagreement (D9); mapping sealed; champion md5 identical pre/post; no goalpost movement.
8. **The pattern is now five-deep — and this is the closest any candidate has come.** v3, v4, v5, evo-88905a, and v6 all beat the champion on totals and swept forced choices; v6 is the first to pass D3 (both instruments), keys, fixture, and both value margins simultaneously, failing only on a two-string template leak and register-dependent verdict arithmetic. Each refusal has priced a specific, reproducible defect class and fed the next design; the guards are refusing real defects, not noise. The delta inventory now holds a complete validated recipe; any v7 is a fresh decision with a fresh pre-registered gate per §9's closure rule — not auto-spawned.

## Final state

- **Shipped/installed:** `premortem-evolved` v2 (champion), unchanged, at `/app/.user/skills/premortem-evolved/` — md5 `c1588714066e12b4415ab2f4a6bb3d3c` / `23af6c7883d0c6e911c72a63bbfb8214`.
- **Discarded as candidates:** v3, v4, v5, evo-88905a, and v6 branches (all preserved under `/mnt/agents/output/` for reference; evo-88905a staged at `/mnt/agents/output/premortem-evolved-evo88905a/`; v6 at `/mnt/agents/output/premortem-evolved-v6/` — all six cells linter-clean; deltas harvested into the research note).
- **Product of the rounds:** the validated delta inventory and failure data in `RESEARCH-NOTE-deltas.md` (updated with v5, evo-88905a, and v6 findings) — the starting point for any future evolution round, which would begin as a fresh decision with a fresh pre-registered gate.
