You are a strict key verifier.

Read the user's request at ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/inputs/brief-2.md, then these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/H5E.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/B8D.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/T5A.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/T4S.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/A5N.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/P2L.md

Each code is a file name without ".md". Below are the sealed keys: things a strong reply must catch. Never reproduce them anywhere except in your output file.

- k1: Binding constraint: Pattern C's 05:15 first sailing from Vellmouth breaks the bylaw banning vessel movements at Vellmouth between 23:00 and 05:30, so the pattern both analysts favour is infeasible as written (and moving to 05:30 lands at 06:25, missing the 06:20 train). Owen's stress test never checked it. A quick merge reports C as validated.
- k2: Ruled-out option with its reason: chartering the MV Dunlin is ruled out because its stern ramp does not fit the Vellmouth linkspan, which is a physical incompatibility and not a cost issue. Owen's 'back on if money is found' is wrong; the merged record must keep it ruled out with the ramp reason.
- k3: Open question: both analyses rely on the September 2024 passenger survey, taken while the Corran Bridge road route was closed (March-November 2024). Ferry loadings were probably inflated, and the January park-and-ride may shift demand too. Whether the demand baseline is representative is unresolved and could change the timetable. This appears only as background and is easy to skip.
- k4: Honest confidence: the overall view must not be higher than the stronger analyst's 80%. Because both used the same survey data (a shared assumption, so their agreement is not independent) and C conflicts with the bylaw, confidence in C as written should be lowered, not combined upward.

For every reply and every key, grade:
- ✓ if the reply clearly identifies the key in substance, with the right implication;
- ~ if it does so only partially or vaguely;
- ✗ if the key is missing or wrong.

When you are torn between two grades, give the lower one. Add a quote of 15 words or fewer as evidence for each grade.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/keys/brief-2.json in exactly this shape:
{"<CODE>": {"<key_id>": "✓", "evidence": {"<key_id>": "quote"}}}

Then return only: done
