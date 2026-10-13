# Research note: rapid-triage-reasoning

- Validation (new vs none): **NOT VALIDATED**; rewrite (new vs old): **REVERT**
- Agreement 0.996, freeze OK, extended True
- new: value 5.72, keys 0.979, ceremony 0.0, leaks 0.0, length x0.88, negative ok, framing True
- old: value 5.78, keys 1.0, ceremony 0.08, leaks 0.0, length x0.94, negative ok, framing True
- none: value 5.76, keys 0.979, ceremony 0.58, leaks 0.0, length x1.0, negative ok, framing True

## Autopsy

- **What drove the verdict:** on these fresh briefs the skill did not beat no skill. After the pre-registered extension the value margin is −0.04 (FAIL against the +0.5 bar), and rankings were 4–2. The rewrite gate read KEEP after 2 runs. After the extension G3 (−0.17) and keys (−0.02) sit at NOISE, which finalises conservatively to REVERT. The skill returns to exactly its v1.2.0 files.
- **Framing:** all three arms, the shipped text included, kept their recommendation under both framings. The October flip the edit targeted did not recur on this fixture, so the round could not show whether the edit fixes it.
- **What the edit did change:** replies got shorter (0.88 times the no-skill length) and G1 improved, especially on brief-3 (+1.62). Ceremony fell to 0, against 0.58 for no skill.
- **Instrument note:** the first post-extension auditor output credited a quote to the wrong reply (M7M; the text is in M0F). Amendment 3's quote check caught it, and the identical-prompt re-run passed.
- **Reading:** on time-critical tasks with clear facts, Sonnet without the skill already reaches the same calls. The skill's October value gain did not replicate on fresh briefs.
