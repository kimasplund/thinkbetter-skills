# Pilot 1: harness unfit (verdict void)

The pre-registered fitness check failed on discrimination:
- **Keys:** both arms caught 100% of the keys.
- **Value:** no-skill trailed by only 0.35.

Judge agreement was 1.00, and there were no arm-naming leaks. The pilot's raw verdict (NOT VALIDATED) does not count.

**Defects found:**
1. The designer prompt did not force key difficulty, so the keys sat at the ceiling.
2. The leak rule and the rubric's G2 anchor counted plain confidence statements ("Confidence: about 80%") as machinery leaks, while G3 rewards calibration.

**Amendment 2**, made before the pilot re-run:
- The designer now plants 3–4 keys per brief, at least two of which a quick answer would plausibly miss.
- The leak rule and G2 now exempt a plain statement of confidence, and still count scoring schemes and confidence arithmetic.

This record is kept for transparency. Its pack is on the designer's avoid list, so the re-run uses fresh briefs.
