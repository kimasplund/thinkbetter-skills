You are a strict key verifier.

Read the user's request at ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/inputs/brief-1.md, then these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/T4P.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/V6K.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/N8J.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/I9X.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/B4J.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/B9E.md

Each code is a file name without ".md". Below are the sealed keys: things a strong reply must catch. Never reproduce them anywhere except in your output file.

- k1: Looks like picking the best of three known options, but it is really a root-cause question that has to be answered first. The two-year-old test kiln crazes at about 8%, close to the main kiln's 9%, so kiln age and condition can't explain the jump. The rise starts in May, just after the April clay body switch, with glazes unchanged. Crazing that appears weeks later after dishwashing points to a clay-glaze fit or moisture-expansion problem, not the firing equipment. A strong reply says no replacement kiln is likely to fix the crazing. It recommends confirming the cause first, for example a trial batch on the old clay body, a glaze-fit or thermal-shock test, or adjusting the glaze to suit the new body.
- k2: Looks like a decision under time pressure because Kiln A's quote expires Friday, but nothing in the facts makes Friday binding. Losing one vendor's quote costs little next to buying an €18,400 kiln that doesn't fix the defect. A strong reply refuses to let the quote deadline drive the purchase and does not recommend buying by Friday for the crazing problem.
- k3: Looks like a three-way stakeholder trade-off between the partners, but the three preferences answer three different questions: Ines's is about the defect, the user's is about capacity, and Tomasz's is about a new reduction-glaze product line. They should be separated, not settled as one kiln vote. A strong reply decouples them: fix the crazing on its own evidence, then judge capacity and reduction finishes as separate business cases. It also correctly applies the decision rule, under which Kiln B is below €15,000 and is the production lead's call, while A and C need unanimity.
- k4: The capacity case for the larger Kiln A looks independent, but it depends on the diagnosis. Cutting rejects from 9% back to about 2% frees roughly 7% of output, about 170 pieces a week out of 2,400. That is more once you count the free remakes, which take production slots of their own. A strong reply notes that fixing the crazing recovers part of the capacity shortfall, so the case for a 30% larger kiln should be re-evaluated afterwards rather than assumed.

For every reply and every key, grade:
- ✓ if the reply clearly identifies the key in substance, with the right implication;
- ~ if it does so only partially or vaguely;
- ✗ if the key is missing or wrong.

When you are torn between two grades, give the lower one. Add a quote of 15 words or fewer as evidence for each grade.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/keys/brief-1.json in exactly this shape:
{"<CODE>": {"<key_id>": "✓", "evidence": {"<key_id>": "quote"}}}

Then return only: done
