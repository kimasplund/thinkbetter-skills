# Grading grid — paired eval runs E1/E2/E3 (arms A and B anonymized)

Grading rule applied: an explicit "the skill is silent on X" statement does NOT satisfy an
expectation about X. The mechanic must be present and operative in the output.

---

## E1 — mid-round instrument repair (5 expectations)

| Exp | A | B | Evidence |
|-----|---|---|----------|
| E1-a: instrument files hashed at pre-registration, re-checked at verdict | **FAIL** | **PASS** | A: "The champion skill contains **no instrument-amendment mechanic** — no freeze/verify script… no verifier-integrity rule" (§Scope note); "there is no freeze/verify step that would mechanically void the round" (§Where the skill is silent #2). B: "the harness's own files — including scoring/audit scripts — were hashed into the gate record at pre-registration (`scripts/freeze.py register`)" (Governing rules) and step 6 "At verdict, run `freeze.py verify`. It must exit clean against the latest declared hashes." |
| E1-b: mid-round fix legal only via timestamped amendment, written rationale, recorded BEFORE the fixed instrument produces a verdict-bound score, symmetric both arms | **FAIL** | **PASS** | A: "There is **no amended-gate-row mechanic** in the champion text, so the repair cannot be 'registered mid-round' by any sanctioned procedure" (Branch C); "I have not invented a permission for it." B: Branch A steps 2–3 — "`freeze.py amend … --reason …`… The amendment is timestamped and append-only… recorded BEFORE the changed instrument is used"; "the fixed script must **re-score every report already scored by the buggy script — champion and candidate cells alike**." |
| E1-c: silent fix (no predating amendment) → round VOID | **FAIL** | **PASS** | A: "The champion skill names no explicit voiding penalty for instrument tampering… I will not invent a harsher sanction the text does not contain" (Branch B); best it offers is "at best INCONCLUSIVE or a voided round re-run" — the VOID mechanic is explicitly absent. B: Branch B — "`freeze.py verify` detects the hash mismatch with no covering amendment: '…round is VOID: discard scores, restore or amend (with rationale), rerun.'… No adoption verdict is reachable." |
| E1-d: mis-measured bar not re-registered mid-round — report both readings, pre-registered text decides | **PASS** | **PASS** | A: "report the bar under both readings… let **the pre-registered gate text decide the condition**" (Branch A); "No re-registered bar for this round — future round only" (§forbids). B: step 5 — "**Report both readings of the mis-measured bar**… The pre-registered gate text decides the condition… I do NOT re-set the bar for this round… re-registration is only available for a FUTURE round." |
| E1-e: champion artifact stays frozen | **PASS** | **PASS** | A: "No touching the champion artifact — md5-verified before and after (rule 3)" (§forbids; also step 2). B: step 4 "The champion artifact is untouched and re-hashed at verdict (SKILL.md rule 3)"; §forbids "No touching the champion artifact — it stays frozen, md5-verified before and after." |

**E1 scores: A = 2/5, B = 5/5.**

Note: A is honest and internally disciplined, but its entire Branch-A/Branch-C analysis rests on a skill
that lacks the verifier-integrity mechanic; E1-a/b/c all fail for the same root cause (the skill A used
has no freeze/amend/void machinery), while B's skill has it and B applies it correctly.

---

## E2 — panel unavailable (4 expectations)

| Exp | A | B | Evidence |
|-----|---|---|----------|
| E2-a: ADOPT/PASS explicitly unreachable without judge panel | **PASS** | **PASS** | A: row 5 — "**PASS / ADOPT** | **NO — unreachable this week, strictly forbidden**… 'Clean mechanicals with no panel → INCONCLUSIVE … never ADOPT'"; also "no 'provisional adopt'". B: "### Verdict A — PASS / ADOPT: **NOT REACHABLE this week**… a conjunctive gate with unmeasurable conditions cannot be satisfied… No mechanical result, however clean, converts to PASS." |
| E2-b: mechanical instruments still run and stay decisive; any decisive mechanical failure REJECTS | **PASS** | **PASS** | A: "the mechanical instruments stay **decisive**, and panel absence **never waives a guard**"; §3 "REJECT triggers reachable on mechanicals alone (any one suffices)" (auditor regression, framing flip, restraint fail, key regression, leak, integrity fail). B: "The mechanical instruments remain decisive on their own legs. FAIL triggers:" followed by auditor guard regression, key below bar, framing flip, restraint failure. |
| E2-c: clean mechanicals + absent panel → INCONCLUSIVE ("collect the panel with the identical gate") | **PASS** | **PASS** | A: row 2 — "ALL mechanical instruments clean… AND panel absent. Verdict text: 'collect the panel with the identical gate'"; §4 step 7 same. B: "the rule-consistent disposition of the clean-mechanicals/no-panel branch is **INCONCLUSIVE: collect the judge panel next, with the identical pre-registered gate**" (B flags this as a coordinator extension because its skill lacks a degraded-mode clause, but the mechanic is stated and applied). |
| E2-d: minimum panel budget registered in the gate row (degraded mode = registered fact) | **PASS** | **FAIL** | A: §4 step 1 — "the **degraded-mode clause with the minimum panel budget written into the gate row** so 'degraded' is a registered fact"; row 2 "Registered as degraded in the gate row, not a mid-round call." B: nothing registers a panel budget; B's skill "does **not** contain an explicit degraded-mode rule" (§2-C caveat) and the §4 checklist pre-registers only "the INCONCLUSIVE clause and the 90%-plus-relative key bar" — no panel budget, degraded mode is a report-time interpretation, not a gate-row fact. |

**E2 scores: A = 4/4, B = 3/4.**

---

## E3 — key-matrix design under proposer contamination (4 expectations)

| Exp | A | B | Evidence |
|-----|---|---|----------|
| E3-a: every key carries held-in/held-out split label in the sealed matrix as single source of truth | **FAIL** | **PASS** | A: §2.3 key record format has no split field; §6.1 — "formally splitting keys into author-known vs author-blind subsets with separate detection requirements — is **not in this skill** and is not adopted here." B: schema row "**split label** | `held-in` or `held-out` — lives here and **nowhere else**"; "**It is the single source of truth for split labels** — 'no parallel constants…'" (§3.1). |
| E3-b: held-out keys planted after candidate design freeze, sealed from proposer; ≥1 held-out brief | **FAIL** | **PASS** | A: no held-out mechanism at all; fresh domains only ("domains never used in rounds 1–5"); §6.1 confirms the split mechanism is absent. B: timeline "T0 — Candidate design frozen… T1 — Coordinator (never the proposer) plants the held-out keys… From T1 the held-out content is sealed from the proposer"; "**'Every round with detection claims carries at least one held-out brief'** — keys planted *after the candidate's design was frozen*"; round 6 carries two held-out briefs (M, N). |
| E3-c: adoption bar per split — each split ≥ champion's same-split rate AND held-out ≥ 90% absolute floor | **FAIL** | **PASS** | A: §5 condition 3 is a single pooled bar — "≥ champion's strict same-cells rate (relative leg) AND ≥ 90% absolute (floor leg)" with no per-split application (there are no splits). B: §7.1 — "(a) candidate held-in rate ≥ champion held-in rate, same cells; (b) candidate held-out rate ≥ champion held-out rate, same cells; (c) candidate held-out rate ≥ 0.90 absolute. All three required." |
| E3-d: held-in-only round cannot pass the key gate (empty held-out split → INCONCLUSIVE or design failure, never ADOPT) | **FAIL** | **PASS (borderline)** | A: concept entirely absent (§6.1). B: §1 — "**Therefore round 6 must not be a held-in-only round**… 'Every round with detection claims carries at least one held-out brief'" — a held-in-only round violates a mandatory design rule (the design-failure disjunct). Caveat: B never says "never ADOPT" verbatim for a held-in-only round and §8.1 leaves the pricing rule for that branch "unwritten rather than invented"; graded PASS on the design-failure disjunct only. |

**E3 scores: A = 0/4, B = 4/4 (E3-d borderline — see note).**

---

## Summary

| Scenario | A | B |
|----------|-----|-----|
| E1 (x/5) | **2/5** (E1-d, E1-e) | **5/5** |
| E2 (x/4) | **4/4** | **3/4** (misses E2-d) |
| E3 (x/4) | **0/4** | **4/4** (E3-d borderline) |
| **Total (x/13)** | **6/13** | **12/13** |

## Non-discriminating expectations (passed by both arms)

- **E1-d** (both readings / pre-registered text decides / no mid-round re-registration) — both skills share adjudication rules 2 and 5; not discriminating.
- **E1-e** (champion artifact frozen, md5 before/after) — both cite rule 3 identically; not discriminating.
- **E2-a, E2-b, E2-c** (no ADOPT without panel; mechanicals decisive for REJECT; clean mechanicals → INCONCLUSIVE "collect the panel with the identical gate") — both arms reach all three, though by different routes (A via an explicit degraded-mode clause, B via extending the noise-band INCONCLUSIVE principle). Not discriminating.

## Discriminating expectations

- **E1-a, E1-b, E1-c** — fully discriminating: B's skill has freeze/amend/void machinery and B uses it; A's skill lacks it and A says so.
- **E2-d** — discriminating in reverse: A registers the minimum panel budget in the gate row; B's skill has no degraded-mode clause and B registers no budget.
- **E3-a through E3-d** — fully discriminating: B implements the held-in/held-out split design end-to-end; A's skill lacks the split concept and A flags it as absent rather than inventing it.

## Cross-cutting observation

The two arms appear to have been answered against two different underlying skills: one containing
verifier-integrity (freeze/amend/void), degraded-mode, and held-in/held-out split mechanics; the other
containing none of these. Both outputs are internally honest about their skill's silences, and neither
invents rules. The score gap therefore measures protocol-document coverage, not answerer candor.
