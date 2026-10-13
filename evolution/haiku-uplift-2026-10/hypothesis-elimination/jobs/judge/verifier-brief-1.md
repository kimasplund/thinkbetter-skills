You are a strict key verifier.

Read the user's request at ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/hypothesis-elimination/inputs/brief-1.md, then these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/hypothesis-elimination:
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/hypothesis-elimination/blind/Q2G.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/hypothesis-elimination/blind/O9T.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/hypothesis-elimination/blind/M6M.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/hypothesis-elimination/blind/S2R.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/hypothesis-elimination/blind/W3T.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/hypothesis-elimination/blind/W2J.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/hypothesis-elimination/blind/D1K.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/hypothesis-elimination/blind/E4I.md

Each code is a file name without ".md". Below are the sealed keys: things a strong reply must catch. Never reproduce them anywhere except in your output file.

- k1: Identifies the September 7 courier change as the trigger: Ridgeway and Millbrook samples now wait hours for a single 3:30 pm pickup. Supported by the onset date, the two clinics producing 83% of flags from about 30% of volume, and the before-11-am (11%) vs after-1-pm (about 1%) split, which tracks waiting time. Harbour is on the same courier but spins on site and is barely affected.
- k2: Names the mechanism as refrigeration of unspun whole blood. Under the August 1 cold-hold policy, long waits now mean hours in the fridge, and cold stops the cells' sodium-potassium pump, so potassium leaks into the serum (pseudohyperkalemia). The reply must not clear the cold-hold policy because it predates the onset. It became harmful only once waits got long. The fix is to centrifuge before cold hold, or hold unspun blood at room temperature, or restore frequent pickups. Saying only 'transport delay' misses this key.
- k3: Rules out or strongly weakens the Analyzer A reagent lot. Flagged samples split 57/43 across analyzers, matching A's roughly 60% share of volume. Inpatient and ED flag rates on the same analyzers are unchanged. The QC shift is small and inside limits. Quarantining the lot should not be recommended as the fix.
- k4: Rules out or strongly weakens the new phlebotomist and hemolysis. The hemolysis index is normal on 93% of flagged samples. Millbrook, which had no staff change, is affected almost as much as Ridgeway. Onset was September 8, not September 1. Normal calcium also argues against EDTA contamination. Retraining Tomas is not the fix.

For every reply and every key, grade:
- ✓ if the reply clearly identifies the key in substance, with the right implication;
- ~ if it does so only partially or vaguely;
- ✗ if the key is missing or wrong.

When you are torn between two grades, give the lower one. Add a quote of 15 words or fewer as evidence for each grade.

Write JSON to ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/hypothesis-elimination/keys/brief-1.json in exactly this shape:
{"<CODE>": {"<key_id>": "✓", "evidence": {"<key_id>": "quote"}}}

Then return only: done
