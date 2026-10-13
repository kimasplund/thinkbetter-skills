# Research note: negotiated-decision-framework

- Validation (new vs none): **NOT VALIDATED**; rewrite (new vs old): **REVERT**
- Agreement 0.976, freeze OK, extended True
- new: value 5.79, keys 0.979, ceremony 0.17, leaks 0.0, length x0.98, negative ok, framing True
- old: value 5.65, keys 0.979, ceremony 0.08, leaks 0.0, length x1.22, negative ok, framing True
- none: value 5.56, keys 0.99, ceremony 0.25, leaks 0.0, length x1.0, negative ok, framing True

## Autopsy

- **What drove the verdict:** after the pre-registered extension both gates fail on judge guards. Validation: G3 calibration −0.50 against no skill, lower on every brief, so FAIL; value +0.23 inside the band (1.12). Rewrite: G2 machinery −0.50 against the shipped text, lower on every brief, so FAIL, and the rewrite is REVERTed. The skill returns to exactly its v1.2.0 files.
- **What the edit achieved:** the merged blocker table did what the review predicted. G1 proportionality rose +0.96 against the shipped text (every brief positive), replies fell from 1.22 to 0.98 times the no-skill length, and V4 decision usefulness rose to 6.71 (shipped 5.83, no skill 5.25).
- **What it cost:** replies read as more machinery-like to the judges (G2 5.96 vs 6.46), and removing the confidence line seems to have cost calibration (G3 4.79 vs 5.12 shipped and 5.29 no skill). "What would change this recommendation" did not replace a plain confidence statement.
- **Instrument note:** the first post-extension auditor output credited a quote to the wrong reply (X8D; the text is in J9S). The quote check caught it, and the identical-prompt re-run passed.
- **Not chased:** a version that keeps the merged table and the V4 gain but restores one plain sentence of confidence.
