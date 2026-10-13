# thinkbetter-skills: repo rules

- **Skills ship from `skills/<name>/`, and nothing else in the repo is installed.** Validation records go in `evolution/<skill>/` and example outputs in `examples/<skill>/`. Never put either inside a skill directory.
- **A skill's text changes only through a pre-registered `skill-gauntlet` round, or through an owner decision disclosed in the README and CHANGELOG.** Mechanical fixes such as YAML quoting, broken links or formatting are fine without a round, but prove the content is unchanged.
- **Every content change bumps that skill's `metadata.version`, the plugin `version` in `.claude-plugin/plugin.json`, and adds a `CHANGELOG.md` entry.** Never set `version` in `marketplace.json`.
- **Before committing:** enable the pre-push gate once per clone with `git config core.hooksPath .githooks`, then run `python3 -m unittest discover -s tests`, `python3 scripts/validate_skills.py`, and `claude plugin validate . --strict` (plus `.claude-plugin/plugin.json` and `./skills`).
- **Keep frontmatter to the six Agent Skills spec keys.** Claude Code-only keys (`model`, `context`, `agent`, `user-invocable`) are allowed, but `build_zips.py` strips them for claude.ai.
- **Never commit private material.** Project-specific overlays (for example a domain pack under `references/`) go in `.git/info/exclude`, not `.gitignore`, so even their filenames stay private. Put private terms in the local, git-ignored `.privacy-denylist` so the validator catches leaks.
- **This machine runs the skills through symlinks** made by `scripts/link_local.sh`, so edits here are live immediately. Don't also install the plugin locally, or every skill appears twice.
