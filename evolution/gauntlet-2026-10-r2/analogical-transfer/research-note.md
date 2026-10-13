# Research note: analogical-transfer

- Validation (new vs none): **NOT VALIDATED**; rewrite (new vs old): **REVERT**
- Agreement 1.0, freeze OK, extended False
- new: value 6.1, keys 0.917, ceremony 1.83, leaks 0.0, length x1.24, negative ok, framing True
- old: value 5.79, keys 0.958, ceremony 0.17, leaks 0.0, length x1.24, negative ok, framing True
- none: value 5.21, keys 0.938, ceremony 0.5, leaks 0.0, length x1.0, negative ok, framing True

## Autopsy

- **What drove the verdict:** the candidate edit made visible method worse, not better. The auditor found 1.83 ceremony hits per reply, against 0.17 for the shipped text and 0.50 for no skill. Almost all of them are the template's remaining section headings ("Analogies Investigated", "Transferable Principles", "Proposed Solutions", "Disanalogies and Risks"). G2 fell to 4.83, against 6.83 for the shipped text. Ceremony FAILs in both gates, so the rewrite is REVERTed and validation is NOT VALIDATED, with no extension needed.
- **Why the edit backfired:** it removed the title and the abstraction section, but its new "Short answer" opening seems to have anchored replies to the fenced template, whose method headings it kept. The review's diagnosis (the template drives the ceremony) holds; the fix had to remove the template headings themselves.
- **Value still rose:** the candidate scored +0.90 against no skill (value PASS, positive on every brief) and +0.31 against the shipped text.
- **Shipped text vs no skill (post-hoc, not binding):** the shipped v1.2.0 text beat no skill on fresh briefs in all 6 rankings, with value +0.58 positive on every brief and fewer ceremony hits than no skill. Only G1 NOISE remains, so under Amendment 3 it would read INCONCLUSIVE and earn an extension. It is a good candidate for a plain 2-arm validation round of the shipped text.
- **Consequence:** `skills/analogical-transfer` returns to exactly its v1.2.0 files.
