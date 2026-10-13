# Adversarial review — skill-gauntlet-v2 (acceptance-gate condition 2)

Reviewer: independent adversarial subagent. Scope: contradictions, loopholes, ambiguity,
freeze.py code review, survival of the (now four) inviolable rules.
Method: full read of candidate SKILL.md / references/protocol.md / references/key-verification.md /
scripts/freeze.py; `diff -r` vs champion; functional tests of freeze.py (register/verify/amend/show)
in /tmp/fz (transcripts below).

**VERDICT: ISSUES — 4 BLOCKERs, 5 MINORs. Do not adopt as written.**

The three original inviolable rules survive verbatim (SKILL.md ll. 25–27 identical to champion);
rule 4 is added cleanly; `diff -r` shows only the declared edit surface; the degraded-mode vs
noise-band INCONCLUSIVE distinction is explicit and consistent (protocol.md "Two INCONCLUSIVE
triggers, one verdict class"; SKILL.md Phase 5). Those parts are good. The blockers below are
in the new mechanics themselves.

---

## BLOCKER 1 — key-verification.md contradicts itself on the detection bar

**Location:** candidate `references/key-verification.md` line 18 (new per-split bar:
"non-regressive vs champion on held-in AND on held-out, AND held-out ≥ 90% absolute floor")
vs line 49 (retained champion text: "Pre-register instead: **≥ champion's strict same-cells
rate AND ≥ 90% absolute floor**"). The diff updated SKILL.md and protocol.md to the per-split
bar but left the old aggregate bar standing in the same reference file.

**Failure scenario:** round with 8 held-in keys at 100% and 2 held-out keys at 60%. Aggregate
rate = 92% ≥ 90% floor and ≥ champion's aggregate → PASSES under line 49's bar; FAILS the
per-split gate (held-out < 90%) that SKILL.md condition (3) and protocol.md item 3 now require.
The file that defines the key-verification instrument gives two different verdicts for the same
numbers. The "conservative reading governs" adjudication rule covers cross-instrument
disagreement, not a self-contradictory instrument definition; gate condition 2 demands zero
unresolved contradictions.

**Minimal fix:** rewrite line 49 to the per-split formulation (or delete it and point at the
new section); keep the "100% is unattainable" data but re-express the recommended bar as
"per-split non-regression + held-out ≥ 90% floor".

## BLOCKER 2 — freeze.py's amend path launders goalpost movement: amend AFTER use verifies clean

**Location:** `scripts/freeze.py` `cmd_amend` (ll. 87–97) + `cmd_verify` (ll. 69–84);
protocol.md "Verifier integrity" section.

**Demonstrated** (test T3): registered 3 files; silently edited `harness/auditor.py`
(verify correctly FAILED, exit 1 — good); then, *after* the changed instrument had "produced
scores", ran `freeze.py amend state --reason "repair…" harness/auditor.py`; `verify` then
printed **VERIFIER INTEGRITY: OK, exit 0**. The ledger contains no instrument-use events, no
score-file manifest, nothing against which the amendment timestamp can be checked. Ordering
("recorded BEFORE the changed instrument is used") is a prose rule with zero mechanical
support, and `verify` does not even print the amendment timestamps/reasons a human would need
to audit ordering out-of-band — it reports only a count. Nothing in SKILL.md or protocol.md
discloses this limitation or prescribes the audit step (e.g., "compare amendment timestamps
against score-file mtimes / round log"). The pre-registration's condition 2 explicitly requires
"freeze.py itself cannot be used to move goalposts" — as shipped, amending after use is
indistinguishable from amending before use.

**Minimal fix (any one, in order of strength):** (a) add `freeze.py mark-used <state_dir> <file>`
(or a `scores-sealed` event) appending use-events to the ledger, and make `verify` FAIL when an
amendment to a file postdates that file's first use-event; (b) have `verify` print every
amendment's timestamp + reason and exit 2 ("clean but amended — manual ordering audit
required") whenever amendments exist, with protocol.md prescribing the audit; (c) at absolute
minimum, disclose in both files that pre-use ordering is procedural, not enforced.

## BLOCKER 3 — held-in-only rounds: gate condition 3's consequence is undefined (vacuous-truth hole)

**Location:** SKILL.md operating rule ("A round whose proposer has seen prior keys is a
held-in-only round — say so, and price the gate accordingly") + gate condition (3) ("held-in
AND held-out each ≥ champion's same-split rate — AND held-out ≥ 90% absolute floor");
key-verification.md ("Every round with detection claims carries at least one held-out brief").

**Failure scenario:** a round whose entire matrix is reused/held-in (exactly the premortem v6
case that acceptance test 3(c) says this mechanic must adjudicate unambiguously). With an empty
held-out split, is condition (3) vacuously satisfied (candidate adoptable with zero held-out
evidence — precisely the failure mode this delta exists to prevent), or unsatisfiable
(→ not-ADOPT)? The texts never say. "Price the gate accordingly" prices nothing. Three
plausible readings (vacuous pass / auto-INCONCLUSIVE / auto-FAIL) are all defensible from the
text as written, so the functional test's "definite outcome" requirement fails for case (c).

**Minimal fix:** one sentence, e.g. in key-verification.md and protocol.md item 3: "If the
held-out split is empty, condition 3 cannot be satisfied — the round is at best INCONCLUSIVE
for detection claims; a held-in-only round can REJECT but never ADOPT." (Match the
degraded-mode pattern, which already states its verdict explicitly.)

## BLOCKER 4 — freeze coverage is undefined and verify only checks the files you remember to pass

**Location:** three divergent enumerations of what gets frozen — PRE-REGISTRATION.md delta 1:
"skill files + round rubric/keys/scripts"; SKILL.md rule 4: "rubric, key matrix, fixtures,
scoring/audit scripts" (no skill files, no normalize); protocol.md "Verifier integrity":
"rubric, key matrix, fixtures, scoring/audit/normalize scripts" (no skill files). freeze.py
takes an ad-hoc CLI file list; there is no manifest. `cmd_verify` checks only its argv files.

**Failure scenarios:** (a) a mid-round edit to `references/auditor.md` or
`references/judge-panel.md` — files that *define* the auditor and panel instruments — is a
silent instrument change that no enumeration unambiguously covers; (b) **demonstrated** (T4):
after silently changing `harness/keys.md`, `freeze.py verify state harness/rubric.md` printed
OK, exit 0 — a verdict-time caller that lists a subset (by accident or intent) never detects
the change. The mechanic's whole value is that verification is total; the tool makes it
opt-in per file.

**Minimal fix:** define a closed manifest (skill files + round rubric/key matrix/fixture
files/normalize+scorecard+freeze scripts + gate row) recorded in the pre-registration and
registered wholesale; change `verify` so that with no file arguments (or `--all`) it checks
EVERY registered file and every amendment-covered file, and warns if any registered file was
not verified.

---

## MINOR 1 — "append-only" ledger is not tamper-evident

`save()` rewrites the whole `verifier-freeze.json`; there is no hash chain and no external
anchor. Demonstrated (T6): editing a registered hash directly in the JSON laundered a silent
file change (tampered `keys.md` passed verify). The trust model is coordinator-held (same as
the sealed mapping), so this is not a new privilege — but the docs' "append-only, never edits"
language oversells a plain JSON file. Fix: chain row hashes, or record the ledger hash in the
pre-registration file held outside `state_dir`.

## MINOR 2 — amend argument parsing silently drops files

`freeze.py amend state harness/keys.md --reason "fix"` (file before `--reason`) recorded an
amendment with `"files": {}` and exit 0 (demonstrated T5) — the intended file is NOT covered,
and the next verify will spuriously VOID the round. Also `--reason` as the last argument raises
an IndexError traceback. Fix: error out on an empty file list; parse args properly (argparse).

## MINOR 3 — "decisive mechanical failure" is exemplified, not defined

Degraded mode hinges on "any decisive mechanical failure → REJECT" but the decisive legs are
only illustrated ("a leaky, ceremonial, or key-blind candidate"). Edge cases (negative fixture
neither deflates nor inflates; key margin inside the noise band on a mechanical leg) have no
stated reading. Fix: enumerate the decisive legs (leak scan, framing gate, negative-fixture
deflation, per-split key floor/non-regression) and state that a non-decisive/ambiguous
mechanical reading degrades to INCONCLUSIVE. Related nit: SKILL.md says "register the panel
budget in the gate row" but SKILL.md's own inline gate template has no panel-budget slot (only
protocol.md's does).

## MINOR 4 — split labels are self-attested; provenance is documentary only

Nothing mechanically ties a key's split label to its planting date — a coordinator (or a
proposer-coordinator) can label reused keys "held-out" at pre-registration, and re-labeling
post-hoc is caught only if the key matrix was actually frozen (see BLOCKER 4) and only via the
amend path (see BLOCKER 2). Fix: record planting date + provenance ("round N matrix, published
in results file X") per key inside the sealed matrix so the label is checkable against a frozen
artifact; require the key matrix in the freeze manifest.

## MINOR 5 — "amendments supersede by timestamp" but code supersedes by list order

`latest_declared` iterates the amendments list in order; last-in-list wins. Equivalent to
timestamp order only while the ledger is written solely by this script on a monotonic clock.
Fix: sort by `timestamp` in `latest_declared` (or assert monotonicity on load).

## Notes (no action required)

- md5 is not collision-resistant, but champion rule 3 already mandates md5; freeze.py is
  consistent with retained doctrine. Not a regression.
- The pre-registration/gate file itself is not freeze-covered (hashing it would mismatch once
  results append). Rule 1 protects it procedurally; consider hashing the gate section
  separately in a future revision.
- Degraded mode cannot be gamed into an ADOPT: both files state INCONCLUSIVE-never-ADOPT and
  "ADOPT always requires the full conjunctive gate", and the panel budget must be pre-registered
  so "degraded" cannot be declared as a mid-round judgment call. Checked; holds.
- SKILL.md condition (7) wording matches protocol.md gate item 7. The two INCONCLUSIVE triggers
  are explicitly distinguished. Original inviolable rules 1–3 verbatim-intact.

## Functional test transcript (freeze.py, /tmp/fz)

- T1 register 3 files → verify OK, exit 0. ✔
- T2 silent edit → verify FAIL "silent change detected … round is VOID", exit 1. ✔ (the
  mechanic's core path works)
- T3 amend AFTER simulated use → verify OK, exit 0. ✘ (BLOCKER 2)
- T4 verify with subset of files while another registered file was changed → OK, exit 0. ✘
  (BLOCKER 4)
- T5 amend with file before `--reason` → empty amendment recorded, exit 0. ✘ (MINOR 2)
- T6 direct ledger edit of a registered hash → changed file verifies OK. ✘ (MINOR 1)
