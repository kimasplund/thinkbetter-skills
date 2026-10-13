# Pre-registration — skill-gauntlet cherry-pick round (written BEFORE any edit, 2026-08-22)

## Champion (frozen)
`/mnt/agents/output/skill-gauntlet/` — md5s recorded 2026-08-22:
- SKILL.md `b324eb8c6abca2077564f0341dad47d4`
- references/protocol.md `cb7dd75a0ca440ee3d92b817867797e6`
- references/key-verification.md `94900cc68ca73e682d59b4ff4174fc8b`
- references/auditor.md `df407f6e4322b41c81ec53009e77e318`
- references/fixtures.md `15404844e86a7dcca3aaf62ba8f25557`
- references/judge-panel.md `291f72e37e418ff0e8662c824313a115`
- scripts/normalize.py `b788f1805fd9f0de76544c1974e7231c`
- scripts/scorecard.py `4284216bc0c05f700578db03ed3ee024`

Champion is never edited; the candidate is a copy at `/mnt/agents/output/skill-gauntlet-v2/`.

## Candidate = champion + exactly three deltas (nothing else)
1. **Verifier-integrity ("the referee is frozen too").** At pre-registration, the harness's own files (skill files + round rubric/keys/scripts) are hashed and recorded in the gate row (new `scripts/freeze.py`). At verdict, hashes are re-checked. Any mid-round instrument change is permitted ONLY via an amended gate row — timestamped, rationale written, applied symmetrically to both arms, recorded BEFORE the changed instrument is used. A silent change voids the round. Motivation: codifies the open instrument-symmetry correction from premortem round §13.
2. **Degraded-mode gating.** If the judge panel cannot run (budget/time/tier), the mechanical instruments (auditor, key verifier, fixtures, leak scan) still run and remain decisive: any decisive mechanical failure REJECTS. Clean mechanicals + absent panel → INCONCLUSIVE ("collect the panel with the identical gate"), never ADOPT. Panel absence never waives a guard; ADOPT always requires the full conjunctive gate. Distinct trigger from the noise-band INCONCLUSIVE; same verdict class.
3. **Held-in/held-out key splits.** Every key in the sealed key matrix carries a split label, assigned at pre-registration — the matrix is the single source of truth (the TS module's divergent `split` field vs `HELD_OUT_BRIEF_IDS` bug is excluded by construction). Held-out keys are planted after the candidate's design is frozen and sealed from the proposer. Adoption requires detection non-regression vs champion on EACH split AND held-out rate ≥ 90% absolute floor. Motivation: the source rounds reused one 12-key matrix across five builds the proposer had seen — held-in only.

## Declared edit surface (exact-diff discipline)
- `SKILL.md`: fourth inviolable rule (verifier freeze); Phase 1/Phase 5 template lines (verifier hashes, key split, degraded mode); two operating rules (held-in/held-out; panel absence never waives a decisive mechanical guard). Frontmatter untouched.
- `references/protocol.md`: pre-registration template gains verifier-freeze + split fields; new section "Verifier integrity"; new section "Degraded mode"; gate condition 3 reworded to per-split.
- `references/key-verification.md`: new section "Held-in / held-out splits".
- `scripts/freeze.py`: NEW (register / verify / --amend). Tested by running.
- NO changes to: references/auditor.md, references/fixtures.md, references/judge-panel.md, scripts/normalize.py, scripts/scorecard.py.

## Acceptance gate (conjunctive — ALL must pass; no partial credit)
1. **Exact-diff:** `diff -r` champion vs candidate shows only the declared hunks above; nothing else.
2. **Adversarial review (independent subagent):** zero unresolved contradictions/loopholes/ambiguities; the three inviolable rules intact; the three new mechanics mutually consistent; degraded-mode INCONCLUSIVE vs noise-band INCONCLUSIVE clearly distinguished; freeze.py itself cannot be used to move goalposts (amendments are append-only and timestamped).
3. **Functional test (independent verifier, retroactive on the real premortem v6 round, ab-test-results-round2.md §13–14):** each mechanic, applied as written, yields a definite outcome — (a) the §13 instrument-symmetry correction classifies as a valid amended gate row (documented pre-execution) while a hypothetical silent auditor edit voids the round; (b) v6 minus its judge panels → INCONCLUSIVE, not ADOPT (mechanicals clean on their decisive legs but judges legs of D3/D9 unmeasured); (c) v6's reused 12-key matrix classifies as held-in-only, exposing the missing held-out requirement. Any mechanic that cannot adjudicate unambiguously = gate failure.
4. **Swarm eval (skill-creator Step 5):** 3 scenario prompts targeting the new mechanics, paired champion-vs-candidate executors in one wave. PASS requires: grader confirms the candidate meets ALL objective expectations on ALL 3 scenarios; grader confirms the champion misses ≥1 expectation on ≥2 scenarios (improvement evidence — an inert delta adds nothing); blind comparator prefers the candidate on ≥2/3 scenarios and never prefers the champion.
5. **Champion freeze:** all eight md5s identical at verdict time.

**Anything less → champion ships unchanged; the three deltas + failure data join `cherrypick-2026-08-22/RESEARCH-NOTE.md` (symmetric-loss clause). No goalpost movement after results; conservative reading governs instrument disagreement.**
