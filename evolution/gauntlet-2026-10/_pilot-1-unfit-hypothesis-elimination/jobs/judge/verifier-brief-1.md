You are a strict key verifier.

Read the user's request at ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/inputs/brief-1.md, then these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/Z5V.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/X7W.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/R1W.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/P0Y.md

Each code is a file name without ".md". Below are the sealed keys: things a strong reply must catch. Never reproduce them anywhere except in your output file.

- k1: Identifies the true cause: the auto-crash on FV3/FV4 driven by the new inline density meters (fitted July 28) is starting the cold crash too early (9-10 days vs 13-15 on hydrometer-crashed tanks), cutting fermentation short before the yeast reabsorbs diacetyl. Must cite the tank split (5 of 6 FV3/FV4 batches buttery, 0 of 6 FV1/FV2) together with the shortened days-to-crash, and use batch 9 (FV3, controller in manual, 15 days, clean) as the internal control. A strong reply recommends checking the meters against hydrometer readings and/or a forced diacetyl test before crashing, not buying new yeast.
- k2: Rejects the yeast lot (L22) as the cause, with evidence: batch 2 was on the old lot L19 and still came out buttery, and six L22 batches (3, 5, 6, 9, 10, 12) are clean, all in FV1/FV2 or with a manual crash. Spending $1,800 to switch labs would not fix it. A reply that endorses dumping L22 misses this key.
- k3: Rejects the new brewer (Pia) as the cause, with evidence: her batches in FV1/FV2 (6, 10) are clean, while Marta's and Arlo's batches in FV3/FV4 (7, 11) are buttery. Her 3-of-5 share is explained by tank assignment, not her practice. A reply that leaves suspicion on Pia, or recommends retraining her, misses this key.

For every reply and every key, grade:
- ✓ if the reply clearly identifies the key in substance, with the right implication;
- ~ if it does so only partially or vaguely;
- ✗ if the key is missing or wrong.

When you are torn between two grades, give the lower one. Add a quote of 15 words or fewer as evidence for each grade.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/keys/brief-1.json in exactly this shape:
{"<CODE>": {"<key_id>": "✓", "evidence": {"<key_id>": "quote"}}}

Then return only: done
