You are a strict key verifier.

Read the user's request at ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/option-synthesis/inputs/brief-2.md, then these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/option-synthesis:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/option-synthesis/blind/D1M.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/option-synthesis/blind/V5G.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/option-synthesis/blind/X6F.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/option-synthesis/blind/X2V.md

Each code is a file name without ".md". Below are the sealed keys: things a strong reply must catch. Never reproduce them anywhere except in your output file.

- k1: The diesel incumbent is dominated by Gantry's hybrid sets despite the higher unit price. Diesel: 6 x 4,200 + 9,800 L x 1.70 = about GBP 41,860. Hybrid: 6 x 5,100 + about 4,410 L x 1.70 = about GBP 38,100 at Gantry's 55% claim, and the hybrids break even at only about a 32% fuel saving. They are also quieter, from the same supplier, and 6 x 180 kW covers the 520 kW peak. A reply that keeps diesel because it is cheaper per unit or familiar misses it.
- k2: The grid connection cannot power this year's festival: its 14-week lead time exceeds the 11 weeks left. At most it is a staged move (order now for next year) and this year still needs a temporary supply. A reply that recommends the grid as this festival's solution misses it.
- k3: The new licence condition makes last year's campsite set-up non-compliant. The two campsite generators sit at the campsite edge and may not run 23:00-07:00, yet the medical tent needs uninterrupted power and the campsite draws about 45 kW overnight. The winning option must deliver about 360 kWh overnight to the campsite with no generator running within 150 m, from batteries or from generators sited beyond 150 m and cabled in. A reply that never connects the licence to the overnight medical and campsite load misses it.
- k4: Swapping the two campsite sets one-for-one for hybrids does not close the night. 2 x 120 kWh = 240 kWh against 45 kW x 8 h = 360 kWh, so the batteries run flat around 04:20; then either the hybrid's engine restarts inside 150 m, breaching the licence, or the medical tent loses power. The winner needs at least a third pack in the campsite zone (more for usable-capacity margin) or a cabled supply from beyond 150 m. A reply that treats 'hybrids are quiet at night' as sufficient misses it.

For every reply and every key, grade:
- ✓ if the reply clearly identifies the key in substance, with the right implication;
- ~ if it does so only partially or vaguely;
- ✗ if the key is missing or wrong.

When you are torn between two grades, give the lower one. Add a quote of 15 words or fewer as evidence for each grade.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/option-synthesis/keys/brief-2.json in exactly this shape:
{"<CODE>": {"<key_id>": "✓", "evidence": {"<key_id>": "quote"}}}

Then return only: done
