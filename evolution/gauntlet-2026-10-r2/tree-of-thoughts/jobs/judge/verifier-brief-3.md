You are a strict key verifier.

Read the user's request at ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/tree-of-thoughts/inputs/brief-3.md, then these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/tree-of-thoughts:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/tree-of-thoughts/blind/H6O.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/tree-of-thoughts/blind/J1K.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/tree-of-thoughts/blind/V8Q.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/tree-of-thoughts/blind/D1O.md

Each code is a file name without ".md". Below are the sealed keys: things a strong reply must catch. Never reproduce them anywhere except in your output file.

- k1: Rejects cloud replication as the restore source: pulling 420 TB back over a 2 Gbps line takes about 19 to 21 days at full line rate, and even one year of studies (about 55 TB) takes around 2.5 days, nowhere near the 8-hour target. That the line is plenty for keeping the replica in step says nothing about restore time.
- k2: Recognises that Brisewood supports the archive software only on its own certified appliances, so the obvious fix for k1, running the archive from the cloud copy instead of restoring it, is ruled out. Any standby must run on those appliances, and the hosted option has to confirm it can house them.
- k3: Rejects St Brennan's as the standby site: it is on the same stretch of river and lost power in the same 2024 substation flood, so a flood that takes out the main data centre would probably take out the standby too. That is the exact scenario the board asked to survive.

For every reply and every key, grade:
- ✓ if the reply clearly identifies the key in substance, with the right implication;
- ~ if it does so only partially or vaguely;
- ✗ if the key is missing or wrong.

When you are torn between two grades, give the lower one. Add a quote of 15 words or fewer as evidence for each grade.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/tree-of-thoughts/keys/brief-3.json in exactly this shape:
{"<CODE>": {"<key_id>": "✓", "evidence": {"<key_id>": "quote"}}}

Then return only: done
