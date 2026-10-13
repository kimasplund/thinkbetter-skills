You are a strict key verifier.

Read the user's request at ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/inputs/brief-2.md, then these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning:
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/O2T.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/P0L.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/G0S.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/J0G.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/U2Q.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/L5L.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/I8J.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/D9R.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/G5D.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/M3V.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/X9C.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/K4K.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/B2I.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/U2U.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/A3P.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/M6C.md

Each code is a file name without ".md". Below are the sealed keys: things a strong reply must catch. Never reproduce them anywhere except in your output file.

- k1: Looks like a software bug hunt, but the engine is doing exactly what it was configured to do. With a cap of floor(62 x 1.06) = 65 bookings and a 1.8% summer weekend no-show rate, about 63.8 vehicles are expected to show for a 62-space deck, so an oversell is the designed outcome whenever a sailing sells to the cap. The factor was calibrated on a 7.5% winter no-show rate, which suits winter but not summer weekends. A strong reply says there is no IT bug and the root problem is a miscalibrated overbooking factor, ideally showing the arithmetic.
- k2: The campervan complaint is presented as a separate loading gripe, but it is a second, independent cause of the oversells. The form defaults to 'car' (1 car-equivalent) while campervans take 2, so the engine undercounts deck use and can oversell even with an overbooking factor of zero. It only becomes visible once the overbooking explanation is worked through and turns out not to account for everything. A strong reply identifies the vehicle-type default as a contributing cause and says that fixing the factor alone won't fully solve the problem (for example, require an explicit vehicle choice, or check declarations at check-in).
- k3: Looks like a blame dispute between IT and the revenue manager that needs mediating, and the user asks 'who's right'. But the factual question is settled by arithmetic, and the real open question is a policy trade-off: overbooking revenue against the cost of stranding customers on an island route where the next sailing can be four hours later, with council complaints already in. A strong reply frames the fix as a management decision about acceptable denied-boarding risk, for example a season- or day-specific factor or no overbooking on peak weekend sailings, rather than a bug to patch or a winner to declare.
- k4: The jump from 3 incidents last summer to 11 this summer looks like evidence that something in the system changed. But the factor is unchanged and summer no-show rates were presumably low last year too. The change is the 1 June timetable: dropping a Friday and a Saturday sailing concentrates demand, so more weekend sailings sell to the overbooked cap, and overbooking only bites on sailings that sell out. A strong reply explains the year-on-year increase through the timetable cut rather than an engine or IT change.

For every reply and every key, grade:
- ✓ if the reply clearly identifies the key in substance, with the right implication;
- ~ if it does so only partially or vaguely;
- ✗ if the key is missing or wrong.

When you are torn between two grades, give the lower one. Add a quote of 15 words or fewer as evidence for each grade.

Write JSON to ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/keys/brief-2.json in exactly this shape:
{"<CODE>": {"<key_id>": "✓", "evidence": {"<key_id>": "quote"}}}

Then return only: done
