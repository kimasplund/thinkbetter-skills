# Research Note — Cherry-Picked Premortem Deltas: Two Regression-Guarded Adoption Attempts

**Status:** Research note only. No adoption. The installed skill `premortem-evolved` (v2, champion) is unchanged — md5-verified frozen throughout both rounds.
**Context:** 21 deltas cherry-picked from a deep recon of external premortem/risk skills (GitHub topics + adjacent sources) were candidate-merged and A/B tested "extreme" against the champion: blind scoring, sealed mapping, persona-diverse judges, planted-flaw key verification, framing-invariance pairs, negative fixtures, generic controls. Two candidate builds (v3, v4) both failed their pre-registered conjunctive gates. This note preserves everything the rounds proved so the next re-mine starts from evidence, not memory.

---

## 1. Validated wins (real, replicated, adoption-ready in a future build)

These survived two independent blind evaluations with effect sizes far above inter-judge noise:

| Delta | Evidence |
|---|---|
| **Urgency-tiered rebuild with dates** (Launch-Blocking / Fast-Follow / Track) | D5 +1.67 (v3), +1.00 (v4-retained); cited in all 12 forced choices |
| **Prevent / limit / accept labels with argued proportionality and priced acceptance** | Same D5 margin; judges: "what makes them fundable rather than merely persuasive" |
| **Pre-launch falsifiers with walk-away thresholds** | D5; every top report named "evidence that kills the plan cheaply" |
| **Re-upgrade rows + early-chain wires in tripwires** | D7 +1.33 (v3), **+1.50** (v4 — exceeded the original margin) |
| **Dated calibration review** (score the premortem itself) | D7; judges singled it out as a differentiator |
| **Reverse autopsy (conditional) + tips-the-balance branch** — price the rebuild's own over-correction | D5/D6; "each top report names exactly how the *rebuilt* plan dies" |
| **Downgraded-guarded table** (demote weak links with re-upgrade signals) | D2 +1.00 in the v4 retest pool |
| **Proportionality screen** (small/reversible/low-stakes → deflate to 1–2 real checks + "overkill" sentence) | Fixed the restraint hole — round-2's strongest single finding. Fixture DEFLATED (D9 5, D8 5) with genuinely non-obvious catches (Substack↔beehiiv paid-tier Stripe porting is support-gated; SPF/DKIM; suppression carryover; sender warming) |
| **Ranking-IS-probability-order rule** (re-ladder, don't reorder; tie-breaks must cover every tied pair) | D3 restored to 5.00 on both instruments, zero inversions — vs 4-of-9 v3 reports docked |
| **Most-certain-first attack, existing-guard check, boring-failure floor, incentive/sustainment classes, citation standard, tone pair, commitment ask** | No regressions anywhere; D6/D8 at or near ceiling throughout |

**Both candidates beat the champion on total score (54.06 and 53.49 vs ~50) and swept all forced choices (6/6 and 6/6)** — and both were correctly rejected anyway. That is the regression guard working as designed: totals measure added value; conjunctive guard dims protect existing value.

## 2. Failed or unresolved items (do not re-attempt without a redesign)

1. **On-page process narration.** Both v3 and v4 lost D9 to visible machinery, not length: stage/section references, and — the ironic one — the proportionality screen narrating itself ("fails the low-stakes screen, so it gets the full treatment", docked by both judge personas; the auditor read the same line favorably — split instrument = still a leak). Raw length was never the problem in v4 (32–36KB, inside the champion's 32–38KB band). **Fix for v5: the screen must be silent or expressed once as plan framing, never as process.**
2. **Coda-stack restatement.** Row caps displaced volume but not duplication: closing blocks restated mode paragraphs. **Fix for v5: explicit no-restatement clause — each closing block must add information not already on the page.**
3. **Seasonality prompt (directionless).** v4 surfaced seasonality prominently but inverted its direction on Brief D (winter trough causalized; the key's summer hot-coffee slowdown contradicted). v3 got the summer mechanism 2-of-3 times *without* the prompt. A prompt that names the topic but not the direction anchors a competing mechanism. **Fix: name the demand trough in the launch window explicitly.**
4. **The absolute 100% key bar is unattainable on the round-2 matrix** — champion 90.3%, v3 95.8%, v4 95.8%. The D4 double-mechanism flaw (seasonality direction + key-person) has never been fully solved by any arm reliably. **Fix: pre-register key gates as relative-to-champion with a 90% absolute floor.**
5. **Length alone is not a bloat metric.** Champion runs at 38KB scored D9 5; a 43.5KB sibling scored 4. Judges price *visible scaffolding and duplication*, not bytes. Future length discipline should target leaks and restatement, not word counts.

## 3. Harness lessons (for the next round)

- The **negative fixture** was the highest-information single cell in round 2 (caught a restraint hole shared by both arms). Keep one in every round.
- **Dimension-major scoring + crossed judge design** produced 100% inter-judge agreement (21/21 cells within 1 pt) — the instrument is reliable enough to detect −0.11 regressions.
- **Auditor cross-check is the validated D3/D9 instrument**; when judges and auditor disagreed, the conservative reading governed and was right both times.
- **Generic controls** (27.8–31.1 pt gap) confirmed the instrument discriminates skill from base-model competence.
- Retest panels must re-score champion cells alongside challenger cells (RB's harsher D9 eye docked 7 of 18 champion cells — pooled comparisons only stay fair within an instrument).

## 4. The v5 recipe (built and tested — failed; do not re-run unchanged)

v5 (v4 + screen-silence + no-restatement clause + direction-grounded seasonality) was built and run through the identical 6-cell scoped retest with the re-registered key bar. Results: D5 +1.44 / D7 +1.50, keys 11.5/12 (95.8%, passed the re-registered bar), fixture DEFLATED again, framing invariant — but **D3 failed on the auditor instrument (4.33 vs 5.00: second 5%-rung ties without written ordering justification — a compliance failure, not a design failure; v4's runs complied) and D9 failed on both instruments (4.33 vs 4.44 judges; 3.33 vs 5.00 auditor)**. Verdict: NO ADOPTION; loop closed per pre-registration.

**What v5's failure adds to the inventory:**

1. **Prose bans do not stop template-driven leaks.** The explicit "stage and section numbers never appear" rule did not prevent "Stage 4" cross-references in 3 of 5 full runs — because the report template is itself organized as named stages, so cross-references naturally cite them. **The champion shares this latent defect** (5 of 9 champion runs docked for stage leaks under judge RD). A future fix must be mechanical, not rhetorical: a pre-delivery grep gate in the verification checklist ("search for 'Stage N', 'Section N', screen/gate names; each hit must be rewritten as content"), or de-ordinalized template section names ("The autopsy", "The adversary") so cross-references read as content.
2. **Ladder compliance needs enumeration, not intention.** The tie-break rule ("at most one tie, covering every tied pair") failed where executors wrote one tie-break and missed a second tie at the floor rung. A future fix should make the pre-delivery check enumerate: "list every tied pair; each has a written ordering or is merged."
3. **The D4 seasonality-direction cell resisted its third fix** (direction-grounded prompt; N9 still inverted — iced season framed as helping). Cell record across builds: champion 0✓/3~, v3 2✓/1~, v4 0✓/1~, v5 0✓/1~. Hypothesis: the brief's surface cues (April open, patio season) actively bias toward the inversion. Documented as a hard cell; deliberately not chased further — chasing a specific key risks teaching to the test and corrupting the harness.
4. **Judge/auditor divergence pattern is stable:** judges grade ranking honesty holistically (all 5s for v5), the auditor applies the written rule mechanically. Both readings are real; the conservative one governs adoption. Future candidates should self-audit against the *mechanical* reading — that is the binding constraint.

---

*Files: champion `/mnt/agents/output/premortem-evolved/` (frozen, shipped) · v3 branch `/mnt/agents/output/premortem-evolved-v3/` (discarded) · v4 branch `/mnt/agents/output/premortem-evolved-v4/` (discarded as candidate; reference implementation of the validated machinery) · v5 branch `/mnt/agents/output/premortem-evolved-v5/` (discarded as candidate) · full verdicts `ab-test-results-round2.md` · all instruments in `scores/`.*

---

## 5. The evo-88905a round (external candidate, tested 2026-08-22 — failed; do not re-run unchanged)

Candidate = v5 + five own deltas (de-ordinalization, de-tilded numbers, mechanical leak-scan sentence, Audit Handoff coda, treasury-audit description trigger). Full protocol and verdict: ab-test-results-round2.md §11–12. Result: NO ADOPTION — D3 failed on the auditor instrument (4.67 vs 5.00), D9 failed on both instruments (judges 4.00 vs 4.89; auditor 3.00 vs 5.00); value gates passed (D5 +1.50, D7 +1.50), keys 11.5/12 = 95.8%, fixture deflated, framing invariant, forced choices 6/6, totals +2.89.

**Validated (works — safe to reuse):**
- **De-ordinalized template section names** (role names: intake / the verdict / the rebuild / the adversary / the autopsy; First/Next/Then for steps). Eliminated the "Stage N"/"Section N" leak class completely — zero ordinal hits in 6/6 cells, grep-verified by the auditor, where prose bans had failed in 3/5 v5 runs. This is the durable fix for that class.

**Failed (do not ship):**
- **Audit Handoff coda** ("one-paragraph handoff summarizing the top failure mode and the kill condition"): restates verdict/top-mode content in every full report — near-definitional violation of the no-restatement clause; docked by all three instruments. Machinery growth priced by D9 exactly as designed.
- **Commitment-recording apparatus as template syntax:** leaked an unfilled placeholder token ("Committed: [change] by [day]") into V7 — new leak class: *raw template tokens on the page*. Any future template block must instruct "fill or delete the placeholders" or render as prose.

**Open (untested mechanical fixes):**
- **Ladder linter:** tie coverage improved (4/5 full runs vs v5's 3/5) but the remaining misses are arithmetic, not textual — a leak-scan sentence cannot catch them. Untested fix: a pre-delivery linter that recomputes descending order and enumerates ALL tied pairs at every rung, requiring a written tie-break per pair.
- D4 seasonality-direction cell: stable hard cell across five builds (champion 0✓/3~, v3 2✓/1~, v4 0✓/1~, v5 0✓/1~, evo 0✓/1~). Not chased — teaching-to-the-test risk.

**Harness note:** judge RE's written totals ran uniformly 5–6 under its own dimension sums; dimension-major pooling (recomputed totals) is the correct design — always recompute totals from dimension scores.

---

## 6. The v6 round (assembled from the validated inventory, tested 2026-08-22 — failed; do not re-run unchanged)

v6 = evo-88905a + five surgical reversals/additions (§13): audit handoff deleted, calibration review rewoven as the final dated tripwire row, commitment ask de-instrumented, references de-ordinalized, NEW `scripts/pre_delivery_check.py` linter as a required pre-delivery gate. Result: gates 1/3/4/5 PASS; gates 2 (D9 judges leg) and 6 (framing) FAIL → NO ADOPTION. Closest any candidate has come.

**Newly validated (replicated under the conjunctive gauntlet):**
- **Linter as pre-delivery gate — the D3 fix.** First build ever to pass probability honesty on BOTH instruments (judges 5.00 vs 4.78; auditor 5.00 vs 4.11 under full tie enumeration). Every tied rung single and covered; zero ordinal/stage/section/audit-handoff/bracket-token leaks across all six cells. The mechanical gate closes the class that sank v3/v5 (tie coverage) and v4/evo (ordinal leaks). Any future build keeps the linter, non-negotiably.
- **Calibration review as the final tripwire row.** Dated (Oct 1 2027 / Jan 2028 / Sep 2 2027), thresholded, credited on D7 (+1.00) with zero auditor D9 cost — the v4/evo coda-restatement class eliminated while keeping the additive rung.
- **De-instrumented commitment ask.** No `[change] by [day]` tokens, nothing about the ask recorded on the page. Ladder vocabulary ("graded as Comply") now appears only as substance (grading the PLAN's stakeholder support); judge readings differ on whether that vocabulary is content or machinery (RG docks it in both arms symmetrically; RH accepts it) — keep it, but it is a style risk.
- **Guarded-demotion table** credited on D2 (+0.56 vs champion).

**Newly failed (the two defects that blocked adoption — precise, reproducible, greppable):**
- **Template-instruction leakage (D9 judges leg).** v6's own template embeds instruction text in output-facing headers: `**Consciously accepted (at most one):**` (SKILL.md L92) was copied verbatim into all three neutral reports, and "paper-tiger re-upgrade signals" (L86) surfaced as a visible row label `| Paper-tiger re-upgrades (Track) |` (F7). The linter catches bracketed tokens but NOT the template's own phrasing → both passed the mechanical gate. **Fix for any v7:** (a) strip instruction parentheticals from every output-facing header (move the rule into the instruction sentence: "Consciously accepted risk:" with "(at most one)" stated in prose the executor does not copy); rename backstage labels to reader-facing language ("re-upgrade watch"); (b) extend the linter with a self-similarity check — grep the OUTPUT for the template's own instruction strings, not just generic tokens.
- **Framing: verdict label + trigger numbers are register-sensitive (gate 6).** Substance held (no doom inflation under "be brutal"; ~70% = ~70%), but the fatal-flaw LABEL flipped (hype: "the cash architecture is fatal" vs neutral/skeptical: "there isn't one") and decision-rule trigger numbers drifted ($198k/$207k/$215k caps; 140/150/160 per day; cushion $10–20k vs $35–45k). Evo precedent: drift tolerable only when the fatal flaw and top-2 hold strictly; a label flip unique to the challenger blocks adoption. **Fix for any v7:** pin the verdict label and trigger numbers to a single computation — "the Verdict's fatal-flaw call and the decision rule's numbers are computed once, from the brief's arithmetic, and appear verbatim-identical in every register; register may change tone, never the call or its numbers."

**Open items:**
- D6 adversary: v6's adversaries attacked the weakest joints; the champion's best (C7) attacks the steelmanned strongest joint. Consider strengthening the adversary instruction toward the steelman target (−0.11 margin this round).
- D4 seasonality-direction cell: stable hard cell across SIX builds (champion 0✓/3~, v3 2✓/1~, v4/v5/evo/v6 0✓/1~ each). Not chased — teaching-to-the-test risk.
- Rubric-v2 tension: D9's "no machinery" anchor vs. machinery other dimensions mandate (tie-coverage sentences, demotion labels, tier tags). One judge reads mandated machinery as D9 violations; the gate outcome did not depend on that reading this round (the template-leak evidence alone flipped the leg), but a future rubric revision should define "machinery the reader needs" vs. "machinery the process needed."

**Harness notes:** the judge-prompt fix ("compute TOTAL as the sum of your dimension scores") eliminated the §12.4.5 arithmetic slips — both panels' totals verified exact. Linter gaps logged: TIE_LINE regex missed "the tie with #3 breaks in #3's favor" (add "the tie with...breaks"); "Section N" hits need a heading-resolution check before docking (U2's resolved to real visible headings). Neither affected v6's scores.
