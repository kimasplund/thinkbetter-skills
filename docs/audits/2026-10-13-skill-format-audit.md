# Skill format audit, 2026-10-13

All 15 skills were audited line by line against the official rules as fetched on 2026-10-13. The sources were the platform.claude.com Agent Skills overview and best-practices pages, the code.claude.com/docs/en/skills page, agentskills.io/specification, and the skill-creator validator in anthropics/skills.

**Fix classes**
- **FORMAT** fixes do not change what the skill makes Claude do: frontmatter, names, paths, TOCs, stale tool names, ordering and descriptions.
- **CONTENT** fixes do change behaviour, so they need owner sign-off.

**What passes everywhere:**
- Every skill has valid YAML and spec-valid names that match their directories.
- Every description is at most 1024 characters with no `<` or `>`.
- `metadata` is a string map in every skill.
- No tracked file depends on ChromaDB or QAVR, and none contains private data.

## Suite-wide findings (the 12 reasoning skills)

| Finding | Skills | Class |
|---|---|---|
| **`model: opus`** forces Opus on every Claude Code user. Several bodies say Sonnet is fine. Drop it. | 10 patterns + router (handover has `model: inherit`, a no-op) | FORMAT |
| **`agent: general-purpose` and `user-invocable: true`** are defaults and no-ops. Drop them. | 12 | FORMAT |
| **`context: fork`** runs the skill in a subagent with no conversation history. The bodies have no `$ARGUMENTS` or task statement, so an auto-invoked fork starts without the problem. A fork also cannot spawn the "parallel" subagents the bodies describe. Drop it, except in breadth-of-thought, where isolation is worth keeping if a `$ARGUMENTS` problem block is added. | ToT, BoT, SRC, HE, AR, DR, AT | CONTENT |
| **`ultrathink`** in the body only works in Claude Code. Say "use extended thinking". | 10 | FORMAT |
| **The effort/model preamble** sits above the H1 and is addressed to the invoker, not the executor. Fold it into one line. | 10 | FORMAT |
| **The backstage rule** ("never name the method in the answer") is the last section, but Claude Code keeps only the first ~5k tokens after compaction. Move it to the top. | 11 | FORMAT (reorder only) |
| **Output templates break the backstage rule.** They are titled "Tree of Thoughts Analysis", "RTR Decision Record", "NDF Decision Record" and so on, and show internal scores. Make the templates name-free or mark them as internal scratch. | ToT, BoT, SRC, AR, DR, AT, RTR, NDF | CONTENT |
| **Undefined acronyms** (ToT, BoT, HE, DR, AT, RTR, NDF, SRC) appear in descriptions and bodies. Anyone who installs a single skill can't resolve them. Use the skill names. | 12 | FORMAT |
| **Descriptions** start with a generic noun phrase. The "Example: … →" clause takes about 90 characters (adversarial's "10 angles" contradicts its body's 8 categories), and "don't use" lists sit in the body. Lead with the situation, swap the examples for trigger phrases, and fold the exclusions in. | 12 | FORMAT |

## Per-skill findings

### integrated-reasoning: MINOR FIXES
- **Length:** 663 lines, against a 500-line guideline. Move Parallel Config (399-431), Limitations (517-564), Quick Guide (568-617) and the worked example (627-662) into `references/` and link them. FORMAT
- **Stale names:** "IR-v2" and "V2/V2.1" prose at 12, 86, 97, 103, 206, 257, 273, 473; "Task tool" at 375 should be the Agent tool. FORMAT
- **Broken cross-reference:** line 435 sends the `.reasoning/` protocol to parallel-execution; it lives in reasoning-handover-protocol. FORMAT
- **Contradictory threshold:** Direct Analysis is below 2.5 at lines 136/140 but MAX below 4.0 at line 167. CONTENT
- **Example arithmetic:** the worked example says DR is 3.80 but computes to 4.30, and it scores only 10 of the 11 dimensions. CONTENT
- **Dated anecdote:** "7.5B local model … three times in five runs" (32-36). Keep the rule, drop the anecdote. CONTENT
- **Unrunnable instructions:** `timeout_per_branch_ms` and "15-minute checkpoints"; Claude can't measure time. Mark them illustrative. CONTENT

### reasoning-handover-protocol: OUTDATED
- **Length and audience:** 1217 lines. It is a design spec for an "IR-v2 orchestrator" that doesn't exist, including a Python `ReasoningOrchestrator` class and "for orchestrator developers" sections (570-652, 1128-1156).
- **Orphaned reference:** `references/handover-templates.md` (277 lines, no TOC) is linked from nowhere.
- **Stale names:** "IR-v2" about 12 times.
- **Wrong claim at line 30:** it says forks reduce the need for handover. They increase it.
- **Contradictions:**
  - The cycle rule versus its own "blocked" example (503-512).
  - Confidence caps disagree across files: 0.95, 0.40–0.90, and 10–95%.
- **Fantasy mechanics:** "cognitive fatigue -5% after 2 hours", 30-day archiving, sha256 jobs.
- **Fix choice:** rewrite it as a short, for-Claude handover guide under 500 lines, or drop it from the suite. Either way this is CONTENT.

### parallel-execution: MINOR FIXES
- **Orphaned reference:** `references/parallel-patterns-advanced.md` (711 lines, no TOC) is not linked from SKILL.md. FORMAT
- **Stale tool names:** "Multiple Task calls", "Task 1 (run_in_background)" and "TaskOutput" at 18 and 41-46. FORMAT
- **Version pin:** "Claude Code v2.1.76+" at 13. FORMAT
- **Experimental features:** Agent teams env var and Ctrl+B (19-55). Mark them Claude Code-only and experimental. FORMAT
- **Confusing worktree example:** frontmatter-style blocks at 70-84. Rewrite as an Agent call with `isolation: "worktree"`. FORMAT
- **Unsupported speedup claims:** "2-4x" and "70% faster" (126, 269; ref 592-601). CONTENT
- **Path the handover protocol never defines:** ref 555 uses a `.reasoning/session-{id}/parallel/` path. FORMAT
- **Description:** has no "Use when" and leads with acronyms (DPTS, BSM, MoA, GoT, RASC). FORMAT

### rapid-triage-reasoning: MINOR FIXES
- **Templates break the backstage rule:** "RTR Decision Record" and "Checkpoint" (191, 350-381) versus line 396. CONTENT
- **Stale boilerplate:** "V1.0 (Current)" version history (385-392). FORMAT
- **Frontmatter:** `model: sonnet` overrides the user's choice. Drop it; if the intent should stay, use `effort: low`. FORMAT

### negotiated-decision-framework: MINOR FIXES
- **Templates break the backstage rule:** "NDF Decision Record" and the "Confidence" section (360, 395) versus line 413. CONTENT
- **Stale boilerplate:** "V1.0 (Current)" (401-409). FORMAT
- **Inconsistent spelling:** "archaeology" versus "Archeology" (17, 86). FORMAT
- **RTR pairing contradicts itself:** line 352 versus line 37. CONTENT

### tree-of-thoughts: MINOR FIXES
- **Stale tool names:** "Task tool" and "TodoWrite" (97-100). The reference (109-140) uses `Task(subagent_type=…)` inside a sequential `for` loop. FORMAT
- **Reference without a TOC:** 236 lines. FORMAT
- **Confidence math is broken:**
  - The `LR = 0.25 + (score/20)*3.75` formula is above 1 for any score over 4/20, so every branch hits the 95% cap.
  - "= 1,782" at 282 should be about 656.
  - The reference claims ~92% and ~75% where the real values are 99.8% and 99.3%.

  CONTENT
- **Example contradicts its own rules:** it uses 3 levels and 3 branches, against the skill's minimums of 5+ branches and 4+ levels (338-364). CONTENT

### breadth-of-thought: MINOR FIXES
- **Stale tool names:** "Task tool" and "TodoWrite" (148-150, 326-329). FORMAT
- **Reference has no TOC and is mis-described:** 596 lines, and SKILL.md 387-392 lists contents it doesn't have. FORMAT
- **Confidence formula can't reach 100%:** its maximum is about 83% (ref 269-275), and its boost range is inconsistent (190 versus 279). CONTENT
- **Branch counts disagree:** 38 versus "under 50 is too few" versus 50-100 versus 10-20 solutions. CONTENT
- **Overlaps hypothesis-elimination:** it claims debugging cases (31, 42). CONTENT
- **Minutes it can't measure:** "50-70 minutes" (320-324). CONTENT

### self-reflecting-chain: MINOR FIXES
- **Confidence thresholds contradict:** 60-69% "proceeding" at 116 versus ≥70% required at 164. CONTENT
- **PoC-specific rule in a general method:** "MAXIMUM 50%" for unrun code (87-95). That cap can never pass the ≥70% gate. Scope it to "if you can run it, run it". CONTENT
- **Overlaps hypothesis-elimination:** "Ideal for debugging". CONTENT

### hypothesis-elimination: MINOR FIXES
- **HEDAM letters don't match the phase names:** 47 versus 275-280. CONTENT
- **Written for human responders:** the "war room" and "assign team members" advice (226-228). CONTENT

### adversarial-reasoning: MINOR FIXES
- **Overlaps premortem-evolved:** "pre-mortem" in the description and the Pre-Mortem Variant (237-255). Point to premortem-evolved instead. CONTENT
- **Exploitation step needs a guard:** "Attempt exploitation (in test environment)" (267) should add "only with explicit authorization". CONTENT

### dialectical-reasoning: MINOR FIXES
- **Overlaps negotiated-decision-framework:** "stakeholder conflicts" in the description. Narrow it or add a handoff. CONTENT

### analogical-transfer: MINOR FIXES
- **Counts disagree:** 3 versus 3-5 versus top 3 (15, 116, 134, 343). CONTENT
- **Bad example:** "API rate limiting ✅" has in-domain solutions, which the skill says to skip (40). CONTENT

### premortem-evolved: MINOR FIXES (gauntlet-validated, so be conservative with content)
- **Description:** the "when" starts after about 330 characters, and it is imperative ("Run …"). Trim the section inventory and switch to third person. FORMAT
- **`pre_delivery_check.py` errors:** `--help` and a missing path both crash with a traceback. FORMAT
- **`pre_delivery_check.py` patterns:**
  - Over-broad: `TOKEN_WORDS` substring matches give false FAILs, for example "day" inside "[Monday]".
  - Private: harness-private patterns such as "treasury" and "audit handoff".

  CONTENT
- **Inconsistent terms:** "paper-tiger table" and "gap check" versus the template's names. FORMAT
- **Burned fixture:** the small-plan example at 27 is skill-gauntlet's negative-fixture answer. CONTENT
- **Packages:** state "Python 3, no packages", and add a fallback for when Python can't run. FORMAT/CONTENT

### skill-gauntlet: MINOR FIXES (gauntlet-validated)
- **`normalize.py` silently ignores the documented mapping form:** the flat `{"raw.md": "CODE"}` mapping yields "NORMALIZED: (none)" and exit 0. `collect()` is unused. This is a bug. FORMAT
- **`normalize.py` `--help`:** it crashes with an IndexError. FORMAT
- **Broken nested code fence:** `references/judge-panel.md` 28-48. FORMAT
- **Degraded-mode rule appears three times:** SKILL.md 43, 71, 84. Delete 84. FORMAT
- **No fallback without subagents:** the skill doesn't cover claude.ai or other agents. CONTENT

### option-synthesis: MINOR FIXES
- **Stale footer:** "Version 0.1 (2026-09-29) … premortem-evolved v2.1 … see LICENSE" contradicts 1.0.0, and there is no LICENSE file. Delete it, and add `license: MIT` to the frontmatter. FORMAT
- **`kernel.py` isn't linked or explained:** it needs an import or run line and "Python 3, stdlib". FORMAT
- **Description:** the "when" starts after about 520 characters, and it is imperative. Lead with what and when. FORMAT
- **`references/blind-round.md`:** 120 lines with no TOC, and the same broken nested fence as skill-gauntlet. FORMAT
- **Terms borrowed from premortem-evolved:** "stranger-paste test" and the commitment-grade meanings are undefined when this skill is installed alone. Inline one-line definitions. CONTENT
- **Ladder sum ranges differ:** 90-110 in `kernel.py` versus 95-105 in premortem. CONTENT
- **No fallback without subagents:** add one that runs at desk level and discloses it. CONTENT
