# thinkbetter-skills — design

Date: 2026-10-13 · Status: approved in conversation (sections 1–2), section 3 pending review

## Intent

One maintained home for Kim's AI-reasoning and result-quality skills, installable the current recommended ways (Claude Code plugin marketplace, `npx skills add`, claude.ai upload) and carrying the newest version of every skill. It supersedes three public repos: `kimasplund/integrated-reasoning`, `kimasplund/premortem-skill`, `kimasplund/skill-gauntlet`.

**Success means:**
- `claude plugin validate . --strict` passes, and `/plugin marketplace add kimasplund/thinkbetter-skills` + `/plugin install thinkbetter@thinkbetter` installs all 15 skills.
- Every skill is the newest version that exists anywhere on this machine, GitHub or claude.ai, with every content change proven mechanically.
- Nothing private (option-synthesis's private domain pack, local paths) is in a tracked file.
- Kim's machine runs the skills from the repo through symlinks, so the 12 agents that preload skills by plain name keep working.

**Decisions taken in conversation:**

| Question | Decision |
|---|---|
| Scope | The core set only: 15 skills |
| Old repos | This monorepo supersedes them. The old repos get a pointer README and are archived, after explicit confirmation |
| Plugin cut | One plugin, `thinkbetter`, so skills are named `/thinkbetter:<skill>` |
| Local use | Symlink `~/.claude/skills/<name>` to `repo/skills/<name>`. No local plugin install, which would duplicate every skill |
| Premortem | Ship the Aug 25 build with its formatting restored, as v2.2. Kimi's NO-ADOPTION verdict is disclosed |
| Repo shape | The root is both the marketplace and the single plugin (`source: "./"`) |

## Section 1: layout

```
thinkbetter-skills/
├── .claude-plugin/marketplace.json   # name "thinkbetter", owner kimasplund, plugins[0] = {name "thinkbetter", source "./"}
├── .claude-plugin/plugin.json        # name "thinkbetter", version "1.0.0" (pinned), license MIT, repository/homepage
├── skills/<15 skill dirs>            # installed payload only
├── evolution/<skill>/                # validation records: provenance, not payload
├── examples/premortem-evolved/       # the two example reports
├── scripts/                          # validate_skills.py, build_zips.py, link_local.sh
├── tests/                            # unittest for the scripts
├── .github/workflows/validate.yml
├── README.md  CHANGELOG.md  LICENSE  CLAUDE.md  .gitignore
└── docs/superpowers/{specs,plans}/
```

- **Plugin version.** `version` is set only in `plugin.json`; the marketplace entry carries none. A pinned version means users get updates only when it is bumped, and every bump gets a CHANGELOG entry.
- **Skill versions.** Each skill carries `metadata.version` in its frontmatter. `metadata` is a portable spec field, and a version there makes "which version is this?" answerable from the file.
- **Frontmatter.** Claude Code-only keys (`model`, `context`, `agent`, `user-invocable`) stay in the source. The claude.ai zips strip them (section 3).
- **History.** Git history starts fresh. The README's provenance section links to the archived repos.

## Section 2: content assembly

| Skill(s) | Source | Change | Proof |
|---|---|---|---|
| 12 IR skills: `integrated-reasoning`, the 9 patterns, `parallel-execution`, `reasoning-handover-protocol` | `~/projects/skills/integrated-reasoning/skills/*` (identical to GitHub HEAD `5e0e44d` and to the installed copies) | Add `metadata.version: "2.2.0"` (the suite version) to all 12, and change nothing else | Diff against the source shows only the added frontmatter lines |
| `premortem-evolved` 2.2.0 | `~/.claude/skills/premortem-evolved` (Aug 25; identical to Kimi `premortem-evolved-v6`, plus `scripts/pre_delivery_check.py`) | Restore the Markdown headings and bold that were lost in the Kimi round-trip, using v2.1's markup. Rename `premortem-evolved-v6` to `premortem-evolved`. Remove the blank lines inside the frontmatter. Copy `references/` and `scripts/` unchanged | `strip_md(new) == strip_md(aug25)` apart from the `name` line. `pre_delivery_check.py` runs on a fixture report |
| `skill-gauntlet` 1.1.0 | Three-way merge. Base: Kimi `skill-gauntlet` (Aug 17). Ours: GitHub `b19af15` (Aug 18; adds 5 operating rules, `--strip-h2-ordinals`, scorecard fixes). Theirs: Kimi `skill-gauntlet-v2` (Aug 22; `freeze.py`, degraded-mode gating, held-in/held-out key splits; its gate said ADOPT) | `git merge-file` on `SKILL.md`, `references/protocol.md` and `references/key-verification.md`. Add `scripts/freeze.py`. `normalize.py` and `scorecard.py` come from GitHub, since Kimi left them unchanged | No conflict markers. Each side's hunks are present. `freeze.py` register → verify passes, a silent edit then makes verify exit 1 |
| `option-synthesis` 1.0.0 | claude.ai sync, Sep 29: `SKILL.md`, `kernel.py`, `references/{blind-round,report-template}.md` plus one private domain pack | The private domain pack becomes a **local overlay**, excluded through `.git/info/exclude` (which is never published, so even its filename stays private): present on disk and used locally, never tracked. The SKILL.md parenthetical that names the private project becomes generic | The privacy grep with the local denylist finds no hits in tracked files |

**What goes into `evolution/`** (summaries and verdicts only; raw judge outputs stay in `~/projects/skills`):

- **`integrated-reasoning/`:** the GitHub repo's `evolution/`, i.e. v1, validation round 1 and validation round 2.
- **`premortem-evolved/`:** the GitHub repo's `evolution/` (round 3, v7 recipe, diffs), plus Kimi's `ab-test-results-round2.md` (its §13–14 cover the v6 NO ADOPTION) and `RESEARCH-NOTE-deltas.md`.
- **`skill-gauntlet/cherrypick-2026-08-22/`:** `PRE-REGISTRATION.md`, `review.md`, `review-r2.md`, `retro-verify.md`, `grading.md`, `comparison.md` and `ROUND-REPORT.md`.
- **`option-synthesis`:** no record exists, so the README states that it has not been gauntleted.

The Kimi sandbox paths (`/mnt/agents/...`) in these records are history and stay as they are.

## Section 3: tooling and operations

### `scripts/validate_skills.py` (Python 3, PyYAML)

**Checks on every `skills/<dir>/SKILL.md`:**
- The frontmatter parses as YAML.
- `name` matches `^[a-z0-9]+(-[a-z0-9]+)*$`, is at most 64 characters, and equals `<dir>`.
- `description` is 1–1024 characters.
- `metadata`, if present, maps strings to strings, and `metadata.version` is semver.
- Every relative link or path to `references/`, `scripts/` or `assets/` in the body resolves.

**Privacy checks on every tracked file (`git ls-files`):**
- No `/home/<user>/` paths.
- No email addresses other than `noreply@anthropic.com`.
- Nothing matching the patterns in an optional local `.privacy-denylist` file. That file is gitignored and holds private project and repo names, so the denylist itself never publishes them.

The script exits non-zero on any failure. CI runs it without the local denylist.

### `scripts/build_zips.py`

- Writes `dist/<skill>.zip` with the skill folder at the zip root, for claude.ai and Desktop upload.
- Reduces the frontmatter to the six spec keys: `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`.
- Selects files with `git ls-files`, so gitignored overlays never leak into a zip.
- `--with-overlays` also includes untracked, git-ignored files inside the skill (the local overlays), for Kim's personal claude.ai upload of `option-synthesis`.

### `scripts/link_local.sh [target_dir]` (default `~/.claude/skills`)

For each `skills/<name>`:
- If it is already linked correctly, skip it.
- Otherwise, move whatever exists at `target/<name>` to `~/.claude/skills-backup-<YYYYMMDD>/<name>`. The backup must live outside the skills directory, or the backups would be loaded as skills.
- Then create `ln -s repo/skills/<name> target/<name>`.

The script is idempotent. In addition, `~/.claude/skills/premortem-evolved.bak-20260825` moves to the same backup directory, because it currently loads as a duplicate skill. The stale Kimi Code copy at `~/.agents/skills/premortem-evolved` (Aug 17, v2) becomes a symlink as well.

### Tests

`tests/` holds stdlib `unittest` tests for the validator (good and bad fixture skills) and for the zip builder's frontmatter stripping and overlay exclusion.

### CI (`.github/workflows/validate.yml`)

On push and PR, it runs:
- the unit tests;
- `validate_skills.py`;
- `npx -y @anthropic-ai/claude-code plugin validate . --strict`. If that step needs auth in CI, it is replaced with an explicit note in the README rather than silently skipped.

### Repo documents

- **README:** what the repo is; install instructions per surface (Claude Code plugin, `npx skills add kimasplund/thinkbetter-skills [-s <skill>]`, claude.ai zip from Releases, Kimi/Codex via `npx skills`); a skill table with version and validation status; honest validation notes carried over from the old READMEs; provenance.
- **CHANGELOG:** 1.0.0 lists the per-skill versions and the premortem v2.2 owner decision.
- **LICENSE:** MIT, copyright 2026 kimasplund.
- **CLAUDE.md:** the repo rules. A skill changes only through a pre-registered gauntlet round or a disclosed owner decision; bump `metadata.version` and the plugin version; run the validator and tests; never track private overlays.
- **.gitignore:** `dist/`, `__pycache__/`, `.privacy-denylist`. Private overlays are excluded in `.git/info/exclude` instead, so their filenames are never published.

### Publishing (outward-facing, in order)

1. `gh repo create kimasplund/thinkbetter-skills --public` and push `main`.
2. Tag `v1.0.0` and run `gh release create` with the `dist/*.zip` files attached.
3. **Only after Kim confirms:** a pointer commit on each old repo ("Moved to kimasplund/thinkbetter-skills"), then `gh repo archive`.

### Local follow-through

- Run `link_local.sh`.
- Update `skills:` in `ceo-orchestrator.md` and `agent-hr-manager.md` from `integrated-reasoning-v2` to `integrated-reasoning`. The tombstone skill stays locally.
- Kim re-uploads `premortem-evolved`, `skill-gauntlet` and `option-synthesis` (`--with-overlays`) to claude.ai by hand. Claude cannot upload there.

## Out of scope

- New skills, non-core skills, any content change beyond those listed in section 2, `claude plugin eval` suites, and per-harness manifests (`.codex-plugin`, `gemini-extension.json`).
- Each of these is a follow-up with its own decision.
