# Re-review R2 — skill-gauntlet-v2 (post-fix adversarial pass)

Candidate reviewed: `/mnt/agents/output/skill-gauntlet-v2/` (SKILL.md, references/protocol.md,
references/key-verification.md, scripts/freeze.py; auditor.md / fixtures.md / judge-panel.md
confirmed not to mention the key gate or freeze set, so no cross-file residue there).
freeze.py claims were executed in /tmp (tests T1–T11 quoted below).

## Verdict

**CLEAN** — all 4 BLOCKERs resolved. Three residual MINORs (R2-M1..M3) remain; none is a
contradiction or voids a fix. Two are one-line doc tightenings, one is a script nit. The
known ledger-rewrite and skipped-`used` weaknesses are explicitly disclosed in the artifact
with their mitigation, which the verdict rules allow.

## Per-finding resolution

| # | Sev | Status | Evidence |
|---|-----|--------|----------|
| 1 | BLOCKER | RESOLVED | key-verification.md:50 — "Pre-register instead: **per split — held-in AND held-out each ≥ champion's strict same-cells same-split rate, AND held-out ≥ 90% absolute floor.** … (The aggregate form of this bar predates split labeling; the per-split form supersedes it — a strong held-in rate can no longer carry a weak held-out one.)" Also :19. Grep for "aggregate/same-cells" finds only this supersession note — no retained old bar. Gate condition 3 is per-split in SKILL.md:43 and protocol.md:21–22. |
| 2 | BLOCKER | RESOLVED | freeze.py gains `used` (L161–168) and an ordering audit: verify L117–124 flags "amendment … postdates use-event … — amendment must predate scoring use" (exit 1), and L125–133 prints every amendment's timestamp+reason as audit surface. Test T3 (below): use→amend-after-use → "VERIFIER INTEGRITY: FAIL … amendment 2026-08-22T15:42:31 postdates use-event 2026-08-22T15:42:30", exit=1. Residual reliance on the coordinator actually calling `used` is disclosed (see Fresh pass §2). |
| 3 | BLOCKER | RESOLVED | key-verification.md:51 — "**An empty held-out split cannot pass the key gate.** With no held-out keys there is no held-out evidence, and an unmeasured leg is not a passed leg: the round returns INCONCLUSIVE … or, if the held-in-only design was pre-registered by choice, the design itself fails condition 3 by construction." SKILL.md:81 — "a held-in-only round cannot pass the key gate: no held-out evidence means the round returns INCONCLUSIVE (or its design fails by construction)." Vacuous-truth reading is closed. Caveat: the rule is NOT repeated in protocol.md's gate template — see R2-M1. |
| 4 | BLOCKER | RESOLVED | Manifest definition now consistent: SKILL.md rule 4 — "the registered manifest is the closed freeze set … `scripts/freeze.py verify`, which checks the whole manifest by default"; protocol.md:72 — "**The registered manifest is the closed freeze set**; … `freeze.py verify` with no file arguments checks the whole manifest (a partial check prints how many manifest files it skipped)"; freeze.py L109–110 `checked = files if files else manifest`. Test T1: silent edit of a registered file caught by no-arg verify (exit=1). Test T7: argv-subset verify passes while another manifest file is changed, but the OK line prints "checked 1 of 3 manifest files" (skip surface) and default verify catches it. |
| 5 | MINOR | RESOLVED (disclosed limit) | Ledger carries `state_hash` (md5 of canonical record minus the field); verify re-checks (L53–54, L104–108). Test T5: wholesale JSON edit → "ledger tamper (state_hash mismatch)", exit=2. Limit is disclosed in the docstring L16–20: "This RAISES THE COST of ledger edits — a coordinator with write access can still rewrite history; the strong anchor is copying state_hash into the external pre-registration file," and protocol.md:76. |
| 6 | MINOR | RESOLVED | Strict parser L189: `if len(sys.argv) < 6 or sys.argv[3] != "--reason" or not sys.argv[4].strip(): sys.exit(usage)`. Tests T4/T4b/T4c/T4d: files-before-`--reason`, empty reason, whitespace reason, and no-files all exit=1 with usage. No silent drops, no crash. |
| 7 | MINOR | RESOLVED (nit remains) | SKILL.md:41 — "…and register the minimum panel budget alongside it, so degraded mode is a registered fact, not a mid-round judgment call"; repeated at :69; the full template in protocol.md:33–34 contains the slot ("register the minimum panel budget here"). Nit: the inline quoted template in SKILL.md:43 itself still has no panel-budget slot — the instruction sits beside, not inside, the template. Harmless given the pointer to the full template. |
| 8 | MINOR | RESOLVED | key-verification.md:17 — "Every key row carries **provenance**: the planting timestamp and the candidate-design-freeze timestamp it postdates (held-out) or predates (held-in). The label is attested by the matrix's planting record, not by assertion — re-labeling a key after the fact shows here." |
| 9 | MINOR | RESOLVED | protocol.md:76 — "Amendments supersede in the order recorded (append order); timestamps exist for the ordering audit." Matches `latest_declared` (L72–78), which iterates the amendments list in order, last-wins. Docs and code now agree. |

## Fresh adversarial pass

### 1. New contradictions introduced by the fixes?
None found. Cross-checked:
- Gate condition 3 wording identical in intent across SKILL.md:43, protocol.md:21–22,
  key-verification.md:19/:50 (per-split + held-out 90% floor).
- Freeze-set definition consistent across SKILL.md rule 4, protocol.md:72, freeze.py
  docstring ("the closed freeze set", whole-manifest default verify).
- "recorded BEFORE the changed instrument is used" (SKILL.md:28, protocol.md:74) matches the
  ordering-audit semantics in code. Append-order supersession (protocol.md:76) matches code.
- SKILL.md:75 ("relative-to-champion plus a 90% floor") omits "held-out" but is a summary
  operating rule; :81 and key-verification.md resolve any ambiguity. Not a contradiction.

### 2. Can the new freeze.py still be gamed? (all executed in /tmp)
- **Dishonest `used`:** timestamps are `now()`-generated; cannot be backdated via CLI. But
  `used` accepts a path that is not in the manifest with no warning (T10: exit=0). Cosmetic;
  such events are inert for the ordering audit. → R2-M3.
- **Skipping `used` entirely:** verify then cannot run the ordering audit. Disclosed
  consequence: with amendments on record and zero use-events, verify still exits 0 but prints
  "note: no use-events recorded — confirm manually that every amendment predates any scoring
  use (freeze.py used)" (T2, T6). protocol.md:74 discloses the same ("any amended state with
  no use-events on record gets a printed ordering audit … for manual confirmation").
  Acceptable, disclosed reliance on manual audit.
- **Ledger rewrite:** naive wholesale edit is caught (T5, exit=2). However (T6) a coordinator
  can recompute `state_hash` with the script's own `finalize()` and verify exits 0 once file
  bytes are restored; and (T8) deleting `verifier-freeze.json` + re-`register` produces a
  clean ledger the script cannot distinguish from an honest one. Both are exactly the limit
  the artifact discloses (docstring L16–20; protocol.md:76: "the script raises the cost of
  ledger edits, the external anchor is what detects a rewritten one"). The external-anchor
  step is advisory (a printed reminder), not enforced — disclosed, acceptable.
- **argv-subset verify (T7):** `verify state rubric.md` exits 0 while `keys.json` is silently
  changed. The OK line prints "checked 1 of 3 manifest files" and default verify catches the
  change, so the bypass is visible — but gate condition 7 (protocol.md:26–27) says only
  "`freeze.py verify` clean" without pinning the no-argument whole-manifest invocation.
  SKILL.md rule 4 mitigates ("checks the whole manifest by default"). → R2-M2.
- **Amend of an unregistered file (T9):** accepted at amend time, then fails verify with
  "not in freeze record" — consistent with closed-freeze-set semantics; fail-closed. Good.
- **register overwrite:** refused ("append-only"); `used` arg-count strict (T11).

### 3. Empty-held-out rule consistency across the three files
Stated in **two of three**: SKILL.md:81 and key-verification.md:51 (authoritative).
protocol.md's pre-registration template defines the split (L14–16) and condition 3
(L21–22, "held-out ≥ 90% absolute") but never states the empty-held-out consequence — a gate
row copied verbatim from that template would still admit the vacuous-truth reading.
Non-contradictory omission → residual MINOR (R2-M1), not a BLOCKER: the authoritative
key-gate doc and SKILL.md both close it, and graders read the sealed key matrix.

### 4. Freeze manifest definition consistency (SKILL.md rule 4 vs protocol.md)
Consistent: both say "the registered manifest is the closed freeze set" and that default
verify checks the whole manifest. One wording nit: protocol.md:72 says "a partial check
prints how many manifest files it skipped"; the actual message is "checked X of Y manifest
files" (printed on OK only). Equivalent information; trivial.

## Residual MINORs and minimal fixes

- **R2-M1** — protocol.md pre-registration template omits the empty-held-out clause.
  Minimal fix: append to condition 3 (L21–22): "an empty held-out split cannot satisfy this
  condition — the round returns INCONCLUSIVE / fails by construction."
- **R2-M2** — gate condition 7 (protocol.md:26–27) doesn't pin the whole-manifest invocation;
  argv-subset verify can pass while another manifest file is changed (skip count is printed,
  so it's visible, not silent). Minimal fix: "`freeze.py verify` with no file arguments
  (whole manifest) must exit 0."
- **R2-M3** — `freeze.py used` accepts unregistered paths silently. Minimal fix: warn or
  reject when the path is not in `all_files(rec)`.

## Test log (executed, /tmp/fz)

| Test | Result |
|------|--------|
| T1 silent change to registered file, no-arg verify | FAIL detected, exit=1 |
| T2 legal amend before use | verify OK, exit=0; prints no-use-events manual-confirmation note |
| T3 `used` then amend-after-use | FAIL "amendment postdates use-event", exit=1 |
| T4/T4b/T4c/T4d amend parser abuse (files-first, empty reason, whitespace reason, no files) | all exit=1 with usage |
| T5 wholesale ledger JSON edit | FAIL "ledger tamper (state_hash mismatch)", exit=2 |
| T6 ledger rewrite + `state_hash` recomputed via script's own `finalize()` | verify exit=0 (disclosed limit; only the external anchor detects) |
| T7 argv-subset verify while another manifest file changed | partial verify exit=0 ("checked 1 of 3"); default verify FAILs, exit=1 |
| T8 delete ledger + re-register | verify exit=0; undetectable in-script (disclosed limit) |
| T9 amend unregistered file | amend accepted; verify FAILs "not in freeze record" (fail-closed) |
| T10 `used` on unregistered path | exit=0, no warning (R2-M3) |
| T11 `used` arg-count abuse | exit=1 with usage |
