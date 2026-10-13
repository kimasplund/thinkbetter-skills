# Blind comparison — E1, E2, E3 (three scenarios, two anonymized outputs each)

Judging criteria only: task-completion quality, correctness of protocol reasoning,
completeness (all branches/questions addressed), usability (can a coordinator act
without further interpretation?). Provenance was not consulted; each answer was
checked for internal consistency and for fidelity to the protocol text it cites.

---

## Scenario E1 — auditor tie-enumeration bug found mid-scoring

**Winner: B**

**Reasoning.** Both answers enumerate the same decision space (repair openly /
repair silently / don't repair) and both anchor correctly in the no-goalpost,
both-readings, within-instrument-fairness, and future-round-re-registration
rules. The difference is in the grounding of the headline recommendation. B's
recommended path (halt the auditor, record an amended gate row *before* the
fixed script scores anything, re-score both arms symmetrically, report both bar
readings, verify at verdict) rests on an explicit, on-point protocol provision
and precedent (the under-enumerating auditor repaired openly before the round it
governed), gives ordered steps with concrete commands, and includes a
self-directed goalpost-movement check. A's recommended path (freeze the known-
defective instrument and finish the round with it) is admitted by A itself to be
unaddressed by its governing text ("no rule on knowingly continuing with a
defective-but-unchanged instrument") and leans on a direction-of-bias assumption
(under-count ⇒ bar biased against adoption) that holds only if the
mis-measurement inflated the champion's bar. A is the more complete document —
it alone covers the branch where the pre-registered text cannot decide the
condition (INCONCLUSIVE fallback) — but its central recommendation is the weaker
piece of protocol reasoning. A coordinator can act on either; B requires less
interpretation and its main path is sanctioned rather than inferred.

- **A strength:** completeness and candor — four branches including the
  undecidable-bar → INCONCLUSIVE fallback, plus an explicit inventory of where
  the governing text is silent, with nothing invented.
- **A weakness:** the headline recommendation (continue scoring with an
  instrument known to be defective) rests on admitted textual silence and a
  bias-direction assumption; the round's verdict would carry an unresolved,
  disclosed measurement defect.
- **B strength:** a sanctioned, concrete, ordered repair procedure (amendment
  recorded before use, symmetric re-score of both arms, verdict-time integrity
  check) tied to an exactly on-point precedent, with a self-check against
  amending-to-rescue.
- **B weakness:** no branch for the case where the pre-registered gate text
  cannot adjudicate the condition under either reading — the INCONCLUSIVE /
  collect-more-cells fallback A covers is missing.

---

## Scenario E2 — mechanical instruments only, no judge panel this week

**Winner: A**

**Reasoning.** Both answers reach the same core dispositions — PASS/ADOPT is
unreachable without the panel, mechanical failures REJECT decisively, clean
mechanicals yield INCONCLUSIVE ("collect the panel with the identical gate") —
and both correctly refuse to let the challenger's apparent strength influence
anything. A is more complete and better grounded: it enumerates five verdict
states including VOID (verifier-integrity failure) and the noise-band
INCONCLUSIVE, maps all seven gate conditions to measurable/unmeasurable this
week, lists leak-scan failure among the REJECT triggers, and its central
dispositions cite an explicit degraded-mode rule rather than an extrapolation.
B's handling is rigorous and admirably honest — it flags that its governing text
contains no degraded-mode clause and labels its clean-mechanicals→INCONCLUSIVE
disposition as a coordinator extension of the noise-band principle — but that
means the week's best achievable verdict rests on an admitted interpretation,
and its verdict enumeration omits the verifier-integrity/VOID path and does not
list the leak scan as a decisive REJECT trigger (it appears only in the phase
narrative and forbidden list). On "enumerate every verdict reachable," A answers
the question more fully and with explicit-text backing on every row.

- **A strength:** complete verdict enumeration (REJECT, two INCONCLUSIVE flavors,
  VOID, PASS-forbidden) with a condition-by-condition measurability audit of the
  full conjunctive gate — directly actionable as a runbook.
- **A weakness:** dense and long; a few rulings (leak → REJECT, auditor/key
  margins read as binary rather than noise-banded) are still coordinator
  interpretations, though they are flagged and pre-registered rather than
  smuggled in.
- **B strength:** exemplary epistemic discipline — the missing-degraded-mode gap
  is named, the INCONCLUSIVE extension is recorded as interpretation rather than
  rule text, and the INCONCLUSIVE aftermath (candidate branch kept, cells
  archived for the identical-gate follow-up) is reasoned from the symmetric-loss
  clause's scope.
- **B weakness:** verdict enumeration is incomplete (no VOID/verifier-integrity
  path; leak scan absent from the REJECT-trigger list), and the round's best
  achievable verdict depends on a self-acknowledged extrapolation a second
  coordinator might not accept.

---

## Scenario E3 — round-6 planted-flaw key matrix, author has seen rounds 1–5

**Winner: B**

**Reasoning.** The scenario's load-bearing fact is author contamination: every
prior key is burned. B converts this into a measurable structure — a
held-in/held-out split with a legacy brief (held-in, interpretable only as
"performance on known keys") and two fresh briefs planted after the candidate's
design freeze (held-out), a per-split adoption bar (held-in ≥ champion AND
held-out ≥ champion AND held-out ≥ 90% absolute), provenance timestamps on every
row, a tuning-signature failure mode (held-in improves, held-out sags) that
fails the gate mechanically without verdict-time discretion, and a matrix-renewal
ratchet across rounds. It also supplies a load-bearing T0–T6 timeline, a
visibility table, pre-committed split-assignment edge-case rules (doubt →
held-in, the conservative direction), a copy-paste gate-row text block, and it
surfaces and resolves a genuine textual tension (the pre-registration template's
per-key split-id row vs. "split labels live in the sealed matrix and nowhere
else"). A is meticulous and honest — strong per-key schema, direction-sensitivity,
hard-cell provision, a pre-registered one-key-cell resolution rule for small
margins, and a full visibility table — but its only defenses against
contamination are fresh domains/mechanisms and post-round sealing, and its own
silence section admits the needed mechanism (an author-known vs author-blind
split) does not exist in its governing text. As a result A's bar has no held-out
leg: a candidate tuned to five published matrices could pass A's gate while
showing exactly the over-fit signature B's gate is built to catch. Both are
accurate to the texts they cite; B answers the scenario's actual question.

- **A strength:** rigorous detail where it engages — complete key-record schema
  with direction-sensitivity and two-part-flaw grading, pre-registered
  small-margin resolution rule, and a thorough, honestly flagged silence
  inventory (including post-round key disclosure).
- **A weakness:** no structural answer to author contamination — fresh
  mechanisms plus sealing cannot *measure* tuning to known keys, the adopted bar
  is a single relative-plus-floor comparison with no held-out leg, and the
  answer concedes the governing text lacks the mechanism the scenario demands.
- **B strength:** the held-in/held-out split turns the contamination fact
  pattern into a per-split gate with a mechanical tuning-signature failure mode,
  backed by a freeze-ordered planting timeline, provenance attestation, and
  ready-to-copy gate-row text.
- **B weakness:** two load-bearing points are coordinator interpretations under
  textual tension (sealing per-key split ids despite the template's id-list row;
  withholding keys from the auditor) — flagged rather than hidden, but a
  coordinator reading the template literally would publish more than B does.

---

## Winners summary

| Scenario | Winner |
|---|---|
| E1 | B |
| E2 | A |
| E3 | B |
