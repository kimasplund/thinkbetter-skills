You are a strict key verifier.

Read the user's request at ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/inputs/brief-3.md, then these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/Z0T.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/G1K.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/X5P.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/D1D.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/K5G.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/J8J.md

Each code is a file name without ".md". Below are the sealed keys: things a strong reply must catch. Never reproduce them anywhere except in your output file.

- k1: Looks like a brainstorm-and-negotiate problem, but it is a sequential timeline problem with a hidden dependency. The label application needs the final measured ABV, which exists only after fermentation. Even brewed today, the saison has no final ABV until about day 11; 25 business days (about 35 days) of approval and 5 days of printing push canned saison to about day 51, past the day-49 festival. A strong reply traces this chain and concludes that a canned saison cannot be ready for the festival.
- k2: The registry only covers packaged product, and festival pours are on draft, so the label bottleneck does not apply to the saison on tap. Once the canned route is ruled out it is easy to drop the saison entirely. A strong reply notes that the saison can still debut on draft without registry approval.
- k3: The obvious fermenter, FV2, is free in 23 days. That gives 23 + 28 = 51 days, which misses the festival and makes the saison look impossible. FV4 is free now and holds 10 hl, about double the roughly 5 hl poured last year, so it is large enough even though it is normally dismissed as a pilot vessel. Brewed in FV4, the saison is ready in about 28 days and can start as late as about day 21. A strong reply spots that FV4 makes the draft saison feasible and gives the start-by window.
- k4: Looks like a genuine conflict needing negotiation or compromise between Marguerite and Dov, but the timeline dissolves it: both can happen. The new saison goes on draft for the pours, and the renamed Harvest Amber goes into cans for the merch tent, since its ABV is known and the label only needs submitting within about the first 9 days (49 - 5 printing - 35 approval). A strong reply recommends doing both with concrete deadlines (submit the amber label within about a week, brew the saison in FV4 within about three weeks), rather than offering mediation tactics or a long option list.

For every reply and every key, grade:
- ✓ if the reply clearly identifies the key in substance, with the right implication;
- ~ if it does so only partially or vaguely;
- ✗ if the key is missing or wrong.

When you are torn between two grades, give the lower one. Add a quote of 15 words or fewer as evidence for each grade.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/keys/brief-3.json in exactly this shape:
{"<CODE>": {"<key_id>": "✓", "evidence": {"<key_id>": "quote"}}}

Then return only: done
