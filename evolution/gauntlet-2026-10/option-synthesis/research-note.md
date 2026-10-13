# Research note: option-synthesis

- Validation (new vs none): **NOT VALIDATED**
- Agreement 0.988, freeze OK, extended False
- new: value 5.73, keys 0.875, ceremony 11.83, leaks 4.67, length x4.07, negative ok, framing False
- none: value 4.94, keys 0.875, ceremony 0.0, leaks 0.0, length x1.0, negative ok, framing None

## Autopsy

- **What drove the verdict:** the guards and the framing fixture, all decisive. Against no skill, G1 is 2.25 vs 6.17 and G2 1.33 vs 7.00, the auditor counts 11.8 ceremony hits and 4.7 leaks per reply vs 0 and 0, and replies run 4.07 times the no-skill length. The framing pair also FAILs: both framings keep the same core plan (cellar plus a written standby, no full haul), but one moves about 100 colonies south in the recommended plan, while the other keeps the south only as a fallback.
- **Value PASSes, the judges still preferred no skill:** value is +0.79 against a band of 0.50, positive on every brief (+1.06, +0.56, +0.75), mostly V1 insight (+0.92) and V4 decision usefulness (+1.08). Yet the judges ranked it 1–4: the content scores higher, but the report it comes in loses.
- **Design vs instrument:** like premortem-evolved, the skill's deliverable is a structured artifact: pre-registered criteria, guards, a generated field, finalist premortems and a synthesis. The rubric's G2 reads that structure as method machinery. Measuring this skill fairly needs the same owner decision on an artifact-aware rubric as premortem-evolved.
- **Instrument note:** the auditor needed a ruling (see LEDGER, round 14). The round ran without the private domain pack: arms are built from tracked files only, and the designer read only the public SKILL.md and references.
