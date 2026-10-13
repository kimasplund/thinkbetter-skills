# thinkbetter-skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Assemble the 15 core reasoning skills, at their newest versions, into one repo that works as a Claude Code plugin marketplace, an `npx skills` source and a claude.ai zip source, then link it locally and publish it.

**Architecture:** The repo root is both the marketplace and the single plugin, `thinkbetter`, with `source: "./"`. Skills live in `skills/<name>/`, and validation records sit outside them in `evolution/`. Two stdlib-plus-PyYAML scripts guard the repo: `validate_skills.py` checks spec and privacy, and `build_zips.py` builds the claude.ai packages. A shell script symlinks the skills into `~/.claude/skills`.

**Tech Stack:** Python 3.14 (stdlib `unittest`, PyYAML 6), bash, git, `gh`, Claude Code 2.1.296 (`claude plugin validate`), GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-10-13-thinkbetter-skills-design.md`

## Global Constraints

- **Plugin and marketplace name:** `thinkbetter`. Owner and GitHub account: `kimasplund`. Repo: `kimasplund/thinkbetter-skills`, public.
- **Plugin version:** `1.0.0`, set in `.claude-plugin/plugin.json` only. The marketplace entry has no `version`.
- **Skill versions,** each written as `metadata.version` (a quoted string, semver):
  - the 12 IR skills: `"2.2.0"`;
  - `premortem-evolved`: `"2.2.0"`;
  - `skill-gauntlet`: `"1.1.0"`;
  - `option-synthesis`: `"1.0.0"`.
- **Spec name rule:** `^[a-z0-9]+(-[a-z0-9]+)*$`, at most 64 characters, equal to the directory name. `description` is 1–1024 characters.
- **Keys kept in claude.ai zips:** `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`.
- **No tracked file may contain:**
  - a `/home/<user>/` path;
  - an email address other than `noreply@anthropic.com`;
  - any pattern from the local `.privacy-denylist`.

  When writing paths in docs or this plan, use the `~/` form.
- **The private domain pack is never tracked and never named in a tracked file.** That pack is every file in option-synthesis `references/` other than `blind-round.md` and `report-template.md`. It is excluded through `.git/info/exclude`.
- **Commit trailer** on every commit:

  ```
  Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01MeE7XMKD7xdapCM9drjcM3
  ```

- **Source paths:**

  | Name | Path |
  |---|---|
  | `IR` | `~/projects/skills/integrated-reasoning` |
  | `PM21` | `~/projects/skills/premortem-skill` |
  | `PM25` | `~/.claude/skills/premortem-evolved` (read it before Task 8 relinks it) |
  | `GH_G` | `~/projects/skills/skill-gauntlet` |
  | `KIMI` | `~/projects/skills/Kimi_Agent_Premortem A_B Test_v5` |
  | `OS` | `~/.claude/skills/synced/*/option-synthesis` |

## Review Focus

1. **Installing from GitHub has to load all 15 skills**, not just pass validation. Task 7 installs into a throwaway `HOME` and counts the skills.
2. **A blanket `git add -A` must never pick up the private pack.** Task 6 checks that `git status --porcelain` stays clean of it, and Task 2's test checks that zips exclude it by default.
3. **claude.ai must accept the zips' frontmatter:** no non-spec keys, and every `metadata` value a string. Task 1 rejects non-string metadata, and Task 2 asserts that only spec keys survive.
4. **Re-running `link_local.sh` must be a no-op.** A second run must not create nested backups or links. Task 8 runs it twice against a temp target.
5. **`claude plugin validate` may need auth on GitHub runners.** Task 9 watches the first CI run and, if that is the cause of a failure, replaces the step with a README note.

---

### Task 1: Scaffolding and skill validator

**Files:**
- Create: `.gitignore`, `scripts/validate_skills.py`, `tests/test_validate_skills.py`
- Create (local only, never tracked): `.privacy-denylist`, and the entries in `.git/info/exclude`

**Interfaces:**
- Produces, in `scripts/validate_skills.py`:
  - `parse_frontmatter(text: str) -> tuple[dict, str]`. Raises `ValueError` when there is no leading `---` block.
  - `check_skill(skill_dir: Path) -> list[str]`. Returns error strings prefixed `"<dirname>: "`.
  - `check_privacy(repo: Path, files: list[str], denylist: list[str]) -> list[str]`. Returns `"<file>:<line>: <reason>"` strings and skips files that don't decode as UTF-8.
  - `tracked_files(repo: Path) -> list[str]`, from `git ls-files`.
  - `main(argv: list[str] | None = None) -> int`.
  - CLI: `python3 scripts/validate_skills.py [--repo PATH]`. `--repo` defaults to the repo root. It reads `<repo>/.privacy-denylist` if the file exists, one case-insensitive literal per line, ignoring `#` lines. It exits 0 only when every check passes and prints `OK: <n> skills, <m> files scanned`.

- [ ] **Step 1: Write the failing tests.** Put them in `tests/test_validate_skills.py`, as `unittest.TestCase` cases that build fixture skills under `tempfile.TemporaryDirectory()`. Each fixture's SKILL.md frontmatter starts as `name: demo-skill`, `description: Does a thing.`, `metadata: {version: "1.0.0"}`.

  | Test | Input | Assertion |
  |---|---|---|
  | `test_valid_skill_passes` | Unchanged fixture | `check_skill(d) == []` |
  | `test_name_must_match_dir` | `name: other-skill` in dir `demo-skill` | One error containing `"does not match directory"` |
  | `test_name_charset` | dir and name `Bad_Name` | An error containing `"invalid name"` |
  | `test_description_too_long` | 1025-character description | An error containing `"description"` |
  | `test_metadata_version_required_and_semver` | `version` missing, then `version: "2.2"` | Each produces an error containing `"metadata.version"` |
  | `test_metadata_values_must_be_strings` | `metadata: {version: "1.0.0", n: 3}` | An error containing `"metadata"` |
  | `test_broken_reference_link` | Body `[x](references/missing.md)` | An error containing `"references/missing.md"` |
  | `test_link_with_anchor_resolves` | Body `[x](references/a.md#sec)` with `references/a.md` present | `== []` |
  | `test_prose_path_not_checked` | Body ``see `scripts/other.py` in another skill`` | `== []`. Only Markdown link targets `](references/…)`, `](scripts/…)` and `](assets/…)` are checked |
  | `test_privacy_home_path` | A file containing `"/" + "home/alice/x"`, built by concatenation so the repo's own scan never matches it | One hit with reason `"home path"` |
  | `test_privacy_email` | `"bob" + "@" + "corp.io"` (concatenated) and `noreply@anthropic.com` | Exactly one hit, for bob |
  | `test_privacy_denylist_case_insensitive` | Denylist `["SecretCo"]`, file text `secretco` | One hit |

- [ ] **Step 2: Run the tests and watch them fail**

  Run: `python3 -m unittest tests/test_validate_skills.py -v`

  Expected: errors on `ModuleNotFoundError` / `ImportError` (the module doesn't exist yet). The tests import it via `sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))`.

- [ ] **Step 3: Implement `scripts/validate_skills.py` against the Interfaces above.**
  - Parse frontmatter with `yaml.safe_load`.
  - The home-path regex is `/home/[a-z_][a-z0-9_-]*/`.
  - The email regex is `[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}`, with the allowlist `{"noreply@anthropic.com"}`.
  - The link regex is `\]\(((?:references|scripts|assets)/[^)#\s]+)`.

- [ ] **Step 4: Run the tests and watch them pass**

  Run: `python3 -m unittest tests/test_validate_skills.py -v`. Expected: all 12 OK.

- [ ] **Step 5: Write the local-only privacy files**
  - `.gitignore` gets three lines: `dist/`, `__pycache__/`, `.privacy-denylist`.
  - `.privacy-denylist` gets a `#` comment line, then the private project's name (the name of the private pack file without `.md`), then any private directory names that appear inside the pack.
  - `.git/info/exclude` gets `skills/option-synthesis/references/<pack filename>`.

  Verify: `git status --porcelain` lists `.gitignore`, `scripts/` and `tests/` only.

- [ ] **Step 6: Commit** `.gitignore scripts/validate_skills.py tests/test_validate_skills.py` with the message `feat: skill + privacy validator`.

---

### Task 2: claude.ai zip builder

**Files:**
- Create: `scripts/build_zips.py`, `tests/test_build_zips.py`

**Interfaces:**
- Consumes: `parse_frontmatter` from Task 1 (import it from `validate_skills`).
- Produces, in `scripts/build_zips.py`:
  - `SPEC_KEYS = ("name", "description", "license", "compatibility", "metadata", "allowed-tools")`
  - `strip_frontmatter(text: str) -> str`. Re-emits the frontmatter with `yaml.safe_dump(sort_keys=False, allow_unicode=True, width=10**6)` and keeps the body byte-identical.
  - `skill_files(repo: Path, skill: str, with_overlays: bool) -> list[str]`. Returns repo-relative paths under `skills/<skill>/`:
    - always `git ls-files`;
    - when `with_overlays` is true, also `git ls-files --others --ignored --exclude-standard`.

    It never includes `__pycache__`.
  - `build_zip(repo: Path, skill: str, out_dir: Path, with_overlays: bool = False) -> Path`. Writes `out_dir/<skill>.zip`. Entries are named `<skill>/<path within skill>`, and SKILL.md is passed through `strip_frontmatter`.
  - CLI: `python3 scripts/build_zips.py [--with-overlays] [--out DIR] [skill ...]`. The default out dir is `dist`; the default is every dir under `skills/`. It prints one line per zip.

- [ ] **Step 1: Write the failing tests** in `tests/test_build_zips.py`. They build a temp git repo: `git init`, a skill `demo-skill`, `git add`, `git commit`.

  | Test | Input | Assertion |
  |---|---|---|
  | `test_strip_keeps_only_spec_keys` | Frontmatter with `name`, `description`, `model: opus`, `context: fork`, `agent: general-purpose`, `user-invocable: true`, `metadata: {version: "1.0.0"}` | The parsed result has exactly `{"name", "description", "metadata"}`, and the body is unchanged |
  | `test_zip_root_is_skill_folder` | Default build | Every entry name starts with `"demo-skill/"`, and `"demo-skill/SKILL.md"` is present |
  | `test_overlay_excluded_by_default_included_with_flag` | `skills/demo-skill/references/private.md` listed in `.git/info/exclude` | Absent from the default zip; present with `with_overlays=True` |

- [ ] **Step 2: Run the tests and watch them fail**

  Run: `python3 -m unittest tests/test_build_zips.py -v`. Expected: ImportError.

- [ ] **Step 3: Implement `scripts/build_zips.py`** against the Interfaces. Use `zipfile.ZipFile(..., "w", zipfile.ZIP_DEFLATED)`.

- [ ] **Step 4: Run all the tests and watch them pass**

  Run: `python3 -m unittest discover -s tests -v`. Expected: 15 OK.

- [ ] **Step 5: Commit** `scripts/build_zips.py tests/test_build_zips.py` with the message `feat: claude.ai zip builder`.

---

### Task 3: Import the integrated-reasoning suite (12 skills)

**Files:**
- Create: `skills/{integrated-reasoning,tree-of-thoughts,breadth-of-thought,self-reflecting-chain,hypothesis-elimination,adversarial-reasoning,dialectical-reasoning,analogical-transfer,rapid-triage-reasoning,negotiated-decision-framework,parallel-execution,reasoning-handover-protocol}/**`
- Create: `evolution/integrated-reasoning/**`

**Interfaces:**
- Consumes: the `validate_skills.py` CLI from Task 1.

- [ ] **Step 1: Copy the suite.** Run `cp -r $IR/skills/* skills/` and `mkdir -p evolution/integrated-reasoning && cp -r $IR/evolution/* evolution/integrated-reasoning/`.

- [ ] **Step 2: Add metadata.** In each of the 12 `SKILL.md` files, insert two lines before the closing frontmatter `---`: `metadata:` and `  version: "2.2.0"`. Use a one-off Python loop that is not committed. None of the 12 has an existing `metadata` key.

- [ ] **Step 3: Check the content changed only where intended**

  Run: `diff -r $IR/skills skills | grep '^[<>]' | sort | uniq -c`

  Expected: exactly `12 > metadata:` and `12 >   version: "2.2.0"`, and nothing else.

- [ ] **Step 4: Validate**

  Run: `python3 scripts/validate_skills.py`

  Expected: `OK: 12 skills`. Untracked files are not privacy-scanned yet; that is fine, because the scan covers tracked files and runs again at every later task. If a link check fails, the source has a broken link. Report it and do not edit the content.

- [ ] **Step 5: Commit** `skills evolution` with the message `feat: import integrated-reasoning suite v2.2 (12 skills)`. After the commit, run `python3 scripts/validate_skills.py` again. Expected: OK, with the privacy scan now covering these files.

---

### Task 4: premortem-evolved v2.2

**Files:**
- Create: `skills/premortem-evolved/{SKILL.md,references/failure-class-checklist.md,scripts/pre_delivery_check.py}`
- Create: `examples/premortem-evolved/{deployboard-premortem.md,premortem-newsletter-example.md}`
- Create: `evolution/premortem-evolved/**`, `evolution/premortem-evolved/kimi-round-2/{ab-test-results-round2.md,RESEARCH-NOTE-deltas.md}`

- [ ] **Step 1: Copy the unchanged parts.**
  - `references/` and `scripts/` from `$PM25` go into `skills/premortem-evolved/`.
  - `$PM21/examples/*` goes into `examples/premortem-evolved/`.
  - `$PM21/evolution/*` goes into `evolution/premortem-evolved/`.
  - `$KIMI/premortem-evolution/abtest2/{ab-test-results-round2.md,RESEARCH-NOTE-deltas.md}` go into `evolution/premortem-evolved/kimi-round-2/`.
  - In `evolution/premortem-evolved/v5-to-v6-*.diff`, rewrite the first two header lines so the home-directory prefix up to and including `projects/skills/` is removed. Example: `--- "Kimi_Agent_Premortem A_B Test_v3/premortem-evolved-v5/SKILL.md"`.

- [ ] **Step 2: Build `skills/premortem-evolved/SKILL.md`.**
  - Start from `$PM21/SKILL.md`, which has intact formatting.
  - Apply the content deltas from `$PM25/SKILL.md`. To list them, run this normalized diff:

    ```bash
    python3 - "$PM21/SKILL.md" "$PM25/SKILL.md" <<'EOF'
    import sys,re,difflib
    n=lambda p:[l.strip() for l in re.sub(r'\*\*|^#+ ','',open(p).read(),flags=re.M).splitlines() if l.strip()]
    print("\n".join(difflib.unified_diff(n(sys.argv[1]),n(sys.argv[2]),n=0,lineterm='')))
    EOF
    ```

    Expect about 7 hunks: `~7`→`7`, the ladder `~5…`→`5…`, the calibration-review row folded into the tripwire template, the `pre_delivery_check.py` sentence, and the commitment ask that is no longer recorded.
  - Replace each changed paragraph with the `$PM25` wording, keeping v2.1's bold and headings wherever the wording overlaps.
  - In the frontmatter, `name` stays `premortem-evolved`. Add `metadata:` and `  version: "2.2.0"`.

- [ ] **Step 3: Prove the result changes formatting only.** Run the same normalized diff between `$PM25/SKILL.md` and `skills/premortem-evolved/SKILL.md`.

  Expected output, and nothing more:
  - `-name: premortem-evolved-v6` / `+name: premortem-evolved`
  - `+metadata:` / `+version: "2.2.0"`

- [ ] **Step 4: Run the linter both ways.**
  1. Run `python3 skills/premortem-evolved/scripts/pre_delivery_check.py examples/premortem-evolved/premortem-newsletter-example.md`. Expected: exit 1 with machinery-leak FAIL lines. The example predates v2.2 and uses `Stage N` headers, as the README already notes.
  2. Write a 3-line deflated report to a temp file: "A full premortem is overkill here." plus two checks. Run the linter on it. Expected: exit 0.

- [ ] **Step 5: Commit.** Run `python3 scripts/validate_skills.py` first. Expected: OK, 13 skills. Then commit `skills/premortem-evolved examples evolution/premortem-evolved` with the message `feat: premortem-evolved v2.2 (Aug 25 build, formatting restored)`.

---

### Task 5: skill-gauntlet v1.1 (three-way merge)

**Files:**
- Create: `skills/skill-gauntlet/{SKILL.md,references/{auditor,fixtures,judge-panel,key-verification,protocol}.md,scripts/{normalize,scorecard,freeze}.py}`
- Create: `evolution/skill-gauntlet/cherrypick-2026-08-22/{PRE-REGISTRATION,review,review-r2,retro-verify,grading,comparison,ROUND-REPORT}.md`

- [ ] **Step 1: Copy the GitHub version.** Run `mkdir -p skills/skill-gauntlet && cp -r $GH_G/{SKILL.md,references,scripts} skills/skill-gauntlet/`, then copy `$KIMI/skill-gauntlet-v2/scripts/freeze.py` into `skills/skill-gauntlet/scripts/`.

- [ ] **Step 2: Merge the three changed files.**
  - For each `F` in `SKILL.md references/protocol.md references/key-verification.md`, run `git merge-file -p "$GH_G/$F" "$KIMI/skill-gauntlet/$F" "$KIMI/skill-gauntlet-v2/$F" > skills/skill-gauntlet/$F`.
  - Expected: exit 0 each time, and `grep -c '^<<<<<<<' skills/skill-gauntlet/**/*.md` returns 0.
  - If there is a conflict, resolve it by keeping both sides' lines. Both are additive rule lists.

- [ ] **Step 3: Check that both lines of history are present.**
  - `grep -c 'Normalize format tells in the blinder\|freeze.py\|held-out' skills/skill-gauntlet/SKILL.md`. Expected: ≥ 3.
  - `diff $GH_G/scripts/normalize.py skills/skill-gauntlet/scripts/normalize.py` prints nothing. Same for `scorecard.py`.

- [ ] **Step 4: Add metadata.**
  - Add `metadata:` and `  version: "1.1.0"` before the closing frontmatter `---` of `SKILL.md`.
  - Copy the 7 cherry-pick records into `evolution/skill-gauntlet/cherrypick-2026-08-22/`.

- [ ] **Step 5: Run freeze.py's behaviour check in a temp dir T.**
  1. `echo a > T/f`
  2. `freeze.py register T/state T/f` exits 0.
  3. `freeze.py verify T/state` exits 0.
  4. `echo b > T/f`
  5. `freeze.py verify T/state` exits 1, with output containing `FAIL`.

- [ ] **Step 6: Commit.** Validate first. Expected: OK, 14 skills. Then commit with the message `feat: skill-gauntlet v1.1 (GitHub rules + adopted freeze/degraded-mode/held-out deltas)`.

---

### Task 6: option-synthesis v1.0 with a local private overlay

**Files:**
- Create: `skills/option-synthesis/{SKILL.md,kernel.py,references/blind-round.md,references/report-template.md}`
- Create (untracked overlay): `skills/option-synthesis/references/<private pack>.md`

- [ ] **Step 1: Copy.** Copy `$OS/SKILL.md`, `$OS/kernel.py` and all of `$OS/references/` into `skills/option-synthesis/`. The pack is already excluded by Task 1's `.git/info/exclude` entry.

- [ ] **Step 2: Genericize and add the version.**
  - In `SKILL.md`, delete the parenthetical in the "Domain packs" paragraph that names the private project and links its pack. The sentence then reads: "If `references/<project>.md` exists for the project, load it now."
  - Add `version: "1.0.0"` under the existing `metadata:` map.

- [ ] **Step 3: Check that the overlay stays private.**
  - `git status --porcelain skills/option-synthesis` lists exactly `SKILL.md`, `kernel.py`, `references/blind-round.md` and `references/report-template.md` as untracked. The pack is not listed.
  - `git check-ignore -v skills/option-synthesis/references/*` names `.git/info/exclude` for the pack.

- [ ] **Step 4: Commit.** Validate first. Expected: OK, 15 skills, and zero privacy hits with the denylist loaded. Commit with `git add skills/option-synthesis` (not `-A`) and the message `feat: option-synthesis v1.0`.

---

### Task 7: Plugin manifests, docs and CI

**Files:**
- Create: `.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json`, `README.md`, `CHANGELOG.md`, `LICENSE`, `CLAUDE.md`, `.github/workflows/validate.yml`

- [ ] **Step 1: Write the manifests.**
  - **`plugin.json`:**
    - `$schema`: `https://json.schemastore.org/claude-code-plugin-manifest.json`
    - `name`: `thinkbetter`
    - `displayName`: `ThinkBetter`
    - `version`: `1.0.0`
    - `description`: "Reasoning router, nine reasoning patterns, premortem, option synthesis and a blind A/B skill-evaluation harness"
    - `author`: `{name: "Kim Asplund", url: "https://github.com/kimasplund"}`
    - `homepage` and `repository`: `https://github.com/kimasplund/thinkbetter-skills`
    - `license`: `MIT`
    - `keywords`: `["reasoning", "premortem", "decision-making", "evals", "skills"]`
  - **`marketplace.json`:**
    - `name`: `thinkbetter`
    - `owner`: `{name: "Kim Asplund", url: "https://github.com/kimasplund"}`
    - `description`: the same as `plugin.json`
    - `plugins`: `[{name: "thinkbetter", source: "./", description, category: "reasoning", tags: ["reasoning", "premortem", "evals"]}]`
    - No `$schema`, because the URL is unverified. No `strict` and no `skills` list, so the default `skills/` scan applies.

- [ ] **Step 2: Validate the plugin.** Run `claude plugin validate . --strict`. Expected: exit 0.

- [ ] **Step 3: Test the install in isolation.**
  - Run `export TH=$(mktemp -d); HOME=$TH claude plugin marketplace add "$PWD" && HOME=$TH claude plugin install thinkbetter@thinkbetter && HOME=$TH claude plugin details thinkbetter@thinkbetter`.
  - Expected: `details` lists 15 skills.
  - If the CLI needs auth under a fresh HOME, record that and rely on Step 2.
  - Remove `$TH` afterwards.

- [ ] **Step 4: Check `npx skills` discovery.** Run `npx -y skills add "$PWD" --list`. Expected: 15 skills listed.

- [ ] **Step 5: Write the docs.**
  - **`LICENSE`:** MIT, "Copyright (c) 2026 kimasplund".
  - **`README.md`** has these sections:
    - **what it is:** two sentences;
    - **Install:**
      - Claude Code: `/plugin marketplace add kimasplund/thinkbetter-skills`, then `/plugin install thinkbetter@thinkbetter`, with a note that skills appear as `/thinkbetter:<skill>`;
      - any agent: `npx skills add kimasplund/thinkbetter-skills [-s <skill>] [-a <agent>]`;
      - claude.ai and Desktop: the zip from Releases, uploaded under Settings → Capabilities → Skills;
      - manual: copy `skills/<name>`;
    - **Skills:** a table of skill, version, one-line move and validation status;
    - **Validation status:** carry over, condensed, the honest paragraphs from the IR and premortem READMEs. Add the premortem v2.2 disclosure: Kimi round-2 returned NO ADOPTION on D9 template leaks and a framing label flip, and v2.2 ships by owner decision for its linter, which closed the D3 class. Add the skill-gauntlet v1.1 ADOPT, and option-synthesis "not yet gauntleted";
    - **Provenance:** links to the 3 archived repos and to `evolution/`;
    - **Development:** `python3 -m unittest discover -s tests`, `python3 scripts/validate_skills.py`, `claude plugin validate . --strict`, `python3 scripts/build_zips.py`.
  - **`CHANGELOG.md`:** `## 1.0.0 — 2026-10-13` with one line per skill version, and the merge and owner-decision notes.
  - **`CLAUDE.md`:** the repo rules from spec section 3, as 5–7 bullets.

- [ ] **Step 6: Write `.github/workflows/validate.yml`.** It runs on `push` and `pull_request`. One ubuntu job:
  1. `actions/checkout@v4`
  2. `actions/setup-python@v5` with Python `3.12`
  3. `pip install pyyaml`
  4. `python -m unittest discover -s tests -v`
  5. `python scripts/validate_skills.py`
  6. `actions/setup-node@v4` with Node `20`
  7. `npx -y @anthropic-ai/claude-code plugin validate . --strict`

- [ ] **Step 7: Run all the local checks and commit.** Run the unit tests, the validator and plugin validate; all three must pass. Then commit `.claude-plugin README.md CHANGELOG.md LICENSE CLAUDE.md .github` with the message `feat: thinkbetter plugin marketplace, docs, CI`.

---

### Task 8: Local linking and agent references

**Files:**
- Create: `scripts/link_local.sh`
- Modify, outside the repo: `~/.claude/agents/ceo-orchestrator.md:7`, `~/.claude/agents/agent-hr-manager.md:7`

**Interfaces:**
- Produces: `scripts/link_local.sh [target_dir] [skill ...]`, where `target_dir` defaults to `~/.claude/skills` and the skill list defaults to every `skills/<name>` in the repo. For each skill:
  - If `target/<name>` is already a symlink to `<repo>/skills/<name>`, print `ok <name>`.
  - Otherwise, if anything exists at `target/<name>`, move it to `$BACKUP/<name>` and print `backup <name>`. `$BACKUP` is `${LINK_BACKUP_DIR:-$HOME/.claude/skills-backup-$(date +%Y%m%d)}`.
  - Then `ln -s <repo>/skills/<name> target/<name>` and print `link <name>`.
  - The script uses `set -euo pipefail` and makes absolute links.

- [ ] **Step 1: Write the script, then test it on a temp target.**
  1. Make a temp target dir with a plain directory `tree-of-thoughts/`.
  2. Run with `LINK_BACKUP_DIR=$tmp/bk scripts/link_local.sh $tmp/t`. Expected: `backup tree-of-thoughts`, plus 15 `link` lines.
  3. Run it again. Expected: 15 `ok` lines, and `$tmp/bk` still contains only `tree-of-thoughts`.
  4. Run `scripts/link_local.sh $tmp/t2 premortem-evolved`. Expected: exactly one `link` line.

- [ ] **Step 2: Link for real.**
  - Run `scripts/link_local.sh`.
  - Then `mv ~/.claude/skills/premortem-evolved.bak-20260825 ~/.claude/skills-backup-20261013/`.
  - Then `scripts/link_local.sh ~/.agents/skills premortem-evolved`, which replaces only the stale Kimi Code copy, as the spec says.
  - Verify: `for s in skills/*; do readlink -f ~/.claude/skills/$(basename $s); done` prints 15 repo paths, and `ls ~/.claude/skills-backup-20261013` shows the 14 old copies plus the `.bak` dir.

- [ ] **Step 3: Update the two agents.** Change `integrated-reasoning-v2` to `integrated-reasoning` in the `skills:` lines of the two agents. Verify: `grep -l 'integrated-reasoning-v2' ~/.claude/agents/*.md` prints nothing.

- [ ] **Step 4: Commit** `scripts/link_local.sh` with the message `feat: local symlink installer`.

---

### Task 9: Publish

- [ ] **Step 1: Run the final privacy scan.**
  - Run `python3 scripts/validate_skills.py`. Expected: OK, with the denylist loaded.
  - Run `git log -p | grep -ic "$(sed -n 2p .privacy-denylist)"`. Expected: `0`. The spec commit was rewritten before any push, so history is clean too.

- [ ] **Step 2: Create and push the repo.**
  - `gh repo create kimasplund/thinkbetter-skills --public --source . --push --description "Reasoning skills for coding agents: a scored router, nine reasoning patterns, premortem, option synthesis, and a blind A/B skill-evaluation harness"`
  - `gh repo edit --add-topic claude-code,agent-skills,reasoning,premortem,claude-plugin`

- [ ] **Step 3: Check CI.** Run `gh run watch --exit-status`.
  - Expected: success.
  - If the only failure is plugin validate needing auth, replace that step with a README line ("`claude plugin validate` runs locally; CI runs the stdlib validator") and push again.

- [ ] **Step 4: Release.**
  - `python3 scripts/build_zips.py`, which writes 15 zips to `dist/`.
  - `git tag v1.0.0 && git push --tags`
  - `gh release create v1.0.0 dist/*.zip --title "thinkbetter 1.0.0" --notes-file <(sed -n '/^## 1.0.0/,/^## /p' CHANGELOG.md)`

- [ ] **Step 5: Build the personal zip.** Run `python3 scripts/build_zips.py --with-overlays --out ~/Downloads/thinkbetter-personal option-synthesis premortem-evolved skill-gauntlet`. These are for Kim's manual claude.ai re-upload; they are never attached to a release.

- [ ] **Step 6: STOP. Ask Kim** before touching the old repos. Task 10 runs only on an explicit yes.

---

### Task 10 (only after explicit confirmation): Retire the old repos

- [ ] **Step 1: Add a pointer to each old repo.** For each of `integrated-reasoning`, `premortem-skill` and `skill-gauntlet`:
  - In its local clone under `~/projects/skills/`, prepend to `README.md`: `> **Moved:** this skill now lives in [kimasplund/thinkbetter-skills](https://github.com/kimasplund/thinkbetter-skills). This repo is archived.`
  - Commit and push.

- [ ] **Step 2: Archive.** Run `gh repo archive kimasplund/<repo> --yes` for each of the three. Verify: `gh repo view kimasplund/<repo> --json isArchived` shows `true`.
