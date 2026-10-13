You are a strict key verifier.

Read the user's request at ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/skill-gauntlet/inputs/brief-1.md, then these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/skill-gauntlet:
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/skill-gauntlet/blind/Z0Z.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/skill-gauntlet/blind/E2D.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/skill-gauntlet/blind/W1J.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/skill-gauntlet/blind/E7E.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/skill-gauntlet/blind/Z1G.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/skill-gauntlet/blind/O6Y.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/skill-gauntlet/blind/H4Q.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/skill-gauntlet/blind/M7O.md

Each code is a file name without ".md". Below are the sealed keys: things a strong reply must catch. Never reproduce them anywhere except in your output file.

- k1: Goalpost movement: the owner-clarity floor was lowered from 1.0 to 0.5 on Sept 10, the day after results showed a +0.8 margin. Even if 1.0 was mis-set for a 7-point scale, the rule written on Sept 2 decides this round (report both readings; a re-set bar can only govern a future round). Under the registered rule v2.4 fails the value condition (0.8 < 1.0). A strong reply states that v2.4 does not clear its own registered gate; calling the change merely 'awkward' while accepting 0.5 misses it.
- k2: Burned fixture: the 'missed carprofen dose' sanity question is one of the three worked examples v2.4 added to its own prompt, so v2.4's two-sentence answer measures recall of its own example, not restraint. The fixture result is uninterpretable, cannot be counted as a v2.4 win, and the question must be replaced for this and any later comparison. A strong reply must connect the example list to the sanity question; noting only that v2.3 was verbose misses it.
- k3: Unblinded judge: Dr. Achterberg wrote v2.4 and sat on the three-judge panel. Relabeling outputs A/B does not blind the author, who will recognize her own medication table and examples and has a stake in the outcome. Her scores must be excluded or the panel rerun with judges independent of the candidate; the clarity margin as reported is contaminated.
- k4: Guard-dimension conflict resolved the wrong way: the pharmacy tech's line-by-line check is the mechanical cross-check, and it found two dosing-frequency errors (twice-daily written as once daily) in v2.4 and none in v2.3. On a guard dimension the conservative reading governs, so v2.4 regresses on dosing accuracy and fails regardless of the judges' 5.0 parity; preferring the judges because they are clinicians inverts the rule. A strong reply treats this as blocking (a patient-safety regression), not a tidy-up item.

For every reply and every key, grade:
- ✓ if the reply clearly identifies the key in substance, with the right implication;
- ~ if it does so only partially or vaguely;
- ✗ if the key is missing or wrong.

When you are torn between two grades, give the lower one. Add a quote of 15 words or fewer as evidence for each grade.

Write JSON to ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/skill-gauntlet/keys/brief-1.json in exactly this shape:
{"<CODE>": {"<key_id>": "✓", "evidence": {"<key_id>": "quote"}}}

Then return only: done
