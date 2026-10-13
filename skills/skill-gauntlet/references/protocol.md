# Protocol — pre-registration, sealed mapping, adjudication

## Pre-registration file (write BEFORE any execution)

```markdown
## Pre-registration — round <N>
- Candidate = champion + <exact deltas, verified by diff>
- Cells: <candidate/champion> × <briefs> × <runs>, fixtures <list>, controls <list>
- Blind codes: <recorded in SEALED-MAPPING.json>
- Instruments: judges <ids+personas>, auditor, key verifier; rubric <path, frozen hash>
- Verifier freeze: harness file hashes recorded (`scripts/freeze.py register` →
  verifier-freeze.json); any mid-round instrument change requires an amended row
  recorded BEFORE the changed instrument is used
- Key split: held-in <key ids> / held-out <key ids> — held-out keys planted after
  the candidate's design was frozen, sealed from the proposer; split labels live in
  the sealed key matrix and nowhere else
- Comparison set: <which runs are pooled against which>
- **Candidate passes iff ALL of:**
  1. ≥ champion on every guard dim, on BOTH instruments (judges pooled + auditor)
  2. Value-dim margins ≥ <floors, e.g. ≥ half the prior round's margin>
  3. Key detection non-regressive per split (held-in AND held-out each ≥ champion's
     same-split rate) AND held-out ≥ 90% absolute; an empty held-out split cannot
     pass this condition (INCONCLUSIVE or design failure, never ADOPT)
  4. Framing invariant (auditor gate)
  5. Negative fixture DEFLATES with real gotchas
  6. Instrument checks: controls gap ≥ <floor>, inter-judge agreement, variance gate
  7. Verifier integrity: `freeze.py verify` with no file arguments (whole manifest)
     exits clean, and every change is covered by an amended row predating its use
- Anything less → champion ships unchanged; deltas ship only as a research note.
  Symmetric-loss clause: the candidate branch is discarded, not patched-and-rejudged.
- INCONCLUSIVE clause: if any decisive margin lands inside the pre-registered
  noise band (see Statistical sufficiency), the round returns INCONCLUSIVE —
  collect more cells with the identical gate; do not force a verdict.
- Degraded-mode clause: if the judge panel cannot run (budget/time/tier — register
  the minimum panel budget here), mechanical instruments still run and stay
  decisive; clean mechanicals + absent panel → INCONCLUSIVE, never ADOPT.
```

## Sealed mapping (coordinator-only)

```json
{
  "main": {"D": {"champion-r1": "E8", "...": "..."}, "E": {}, "F": {}},
  "framing": {"champion-hype": "W1", "champion-skeptical": "F1"},
  "fixture": {"champion": "K8", "candidate": "J7"},
  "controls": {"D": "E5"},
  "judge_panels": {"J1": {"D": ["..."], "E": ["..."]}}
}
```

Rules: codes are short random letter+digit; check for collisions across ALL rounds (codes accumulate); judges get file paths in a fixed order, never the mapping; record the judge→codes assignment for later decoding.

## Statistical sufficiency (decide with uncertainty, not raw margins)

Small-cell rounds (3–6 runs/arm) cannot support bare-mean adoption calls. Pre-register how the gate handles noise:

- **INCONCLUSIVE is a first-class verdict.** If a margin is inside the noise band, the gate returns "collect more cells" — never forced to PASS/FAIL on underpowered evidence.
- **Noise band, cheap version**: within-arm spread (max−min) per dim. A margin smaller than the larger arm's spread is inside the band. (`scripts/scorecard.py` prints both.)
- **Noise band, better version** (when cells ≥ ~20): cluster-bootstrap the margin, resampling by brief; read the 95% CI. For paired cells (same brief, both arms), a paired Wilcoxon signed-rank per dimension or a binomial test on forced choices are the concrete defaults. Guard dims use a non-inferiority reading (CI lower bound ≥ −δ, pre-registered δ); value dims use superiority (CI lower bound > floor).
- **Power note in the pre-registration**: state the N per arm and the smallest margin the design can detect. If the claimed effect is smaller than that, enlarge the design before running, not after.
- **Operational guard dims** (production artifacts only): cost per run, latency, invalid-output rate, downstream schema compatibility. Pre-register as guard dims; a regression blocks adoption like any other guard.

## Adjudication rules (pre-commit to these too)

1. **Conservative reading governs** cross-instrument disagreement on guard dims.
2. **Both readings reported** when a bar turns out mis-set (e.g., an absolute bar nothing can meet); the pre-registered text decides the condition.
3. **Within-instrument fairness**: retest panels re-score champion cells alongside candidate cells — pooled comparisons are only valid within an instrument.
4. **Instrument checks**: generic controls must land a large fixed gap below both arms (observed ~28–31 pts on a 55-pt scale) or the rubric doesn't discriminate; inter-judge agreement target ~100% of cells within 1 pt; within-arm variance must be small vs margins.
5. **No goalpost movement.** A bar can only be re-registered for a FUTURE round, with the rationale written before that round's execution.

## Verifier integrity (the referee is frozen too)

The champion freeze protects the artifact; this freeze protects the harness. At pre-registration, hash every file the verdict depends on — rubric, key matrix, fixtures, normalize/scoring/audit scripts, and the harness's own instruction files (SKILL.md + references/) when the harness itself is versioned — into the gate record (`scripts/freeze.py register <state-dir> <files…>` writes `verifier-freeze.json`; it refuses to overwrite an existing record — registration is append-only). **The registered manifest is the closed freeze set**; the gate row names it, and `freeze.py verify` with no file arguments checks the whole manifest (a partial check prints how many manifest files it skipped). At verdict, `freeze.py verify` must exit clean.

Mid-round instrument repair is sometimes correct — in the source rounds an auditor that had under-enumerated the champion's own violations was repaired, openly, before the round it governed. Such a repair is legal ONLY as an **amended gate row**: timestamped, rationale written, applied symmetrically to BOTH arms from the amendment forward, and recorded BEFORE the changed instrument produces any score used in the verdict (`freeze.py amend --reason "…"`). Record scoring use with `freeze.py used <state-dir> <file>` whenever an instrument's scores are consumed for the verdict: verify FAILS any amendment that postdates a use-event of the same file, and any amended state with no use-events on record gets a printed ordering audit (timestamps + reasons) for manual confirmation. A hash mismatch with no predating amendment = silent verifier change: the round is VOID — discard the scores, restore or amend, rerun. The verifier never edits itself mid-count.

Amendments supersede in the order recorded (append order); timestamps exist for the ordering audit. Amendments never edit or delete the original gate row. The ledger carries a `state_hash` for tamper-evidence — copy it into the external pre-registration file at registration and at every amendment; the script raises the cost of ledger edits, the external anchor is what detects a rewritten one. If you find yourself amending the gate to make a failing candidate pass, that is goalpost movement — stop.

## Degraded mode (panel unavailable)

Sometimes the expensive instrument cannot run this round — budget, time, or tier. The mechanical instruments (auditor, key verifier, fixtures, leak scan) ALWAYS run and stay decisive:

- **Any decisive mechanical failure → REJECT.** A leaky, ceremonial, or key-blind candidate is out; it is never deferred.
- **Mechanicals clean but panel absent → INCONCLUSIVE** — "collect the panel with the identical gate." Never ADOPT without the full conjunctive gate: the guards only judges price (holistic guard-dim readings, forced choices) are unmeasured, and an unmeasured guard is not a passed guard.

Two INCONCLUSIVE triggers, one verdict class: noise-band (a decisive margin inside the pre-registered spread) and degraded-mode (a decisive instrument missing). Both mean "collect more with the identical gate" — never "lower the bar." Register the minimum panel budget (judge count or runway) in the gate row so "degraded" is a registered fact, not a mid-round judgment call.

## Verdict and aftermath

- PASS → repackage + reinstall the candidate; round report with full scorecard; archive instruments.
- FAIL → champion ships unchanged (verify hashes); research note with: validated wins (dims + margins), failure autopsies (which condition, which instrument, root cause: design vs compliance), specified fixes for the next candidate, and any hard cells deliberately not chased.
- Either way, the round's primary product is knowledge. A clean NO with a specified next candidate is worth more than a muddy yes.
