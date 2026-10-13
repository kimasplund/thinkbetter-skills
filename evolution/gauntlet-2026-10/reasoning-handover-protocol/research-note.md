# Research note: reasoning-handover-protocol

- Validation (new vs none): **NOT VALIDATED**; rewrite (new vs old): **REVERT**
- Agreement 0.992, freeze OK, extended False
- new: value 5.62, keys 0.938, ceremony 0.17, leaks 0.0, length x0.85, negative ok, framing True
- old: value 5.77, keys 0.958, ceremony 0.0, leaks 0.33, length x0.96, negative ok, framing True
- none: value 5.62, keys 0.958, ceremony 0.0, leaks 0.0, length x1.0, negative ok, framing None

## Autopsy

- **What drove the verdict:** all three arms were level on value (new 5.62, old 5.77, none 5.62), and on keys (0.94 to 0.96). One auditor ceremony hit in the new arm decided both gates under the pre-registered text, which treats a difference of less than one hit as noise, so exactly one hit FAILS. That hit was a section headed "Contacts (names only, nothing new)".
- **The other reading, reported per protocol:** with a one-hit tolerance, both gates would read INCONCLUSIVE and go to an extension. The pre-registered text decides.
- **Design vs compliance:** the 116-line rewrite produced no measurable value gain over either v1.0.0 or no skill on realistic hand-off briefs. It did produce shorter replies (×0.85) and no rating-table leaks; v1.0.0 had 2. The earlier gauntlet-lite win (quality 10 to 15) came from one artefact-style fixture and did not replicate.
- **Consequence:** the body reverts to v1.0.0, mechanically and as the owner pre-authorized. The modernised frontmatter stays.
