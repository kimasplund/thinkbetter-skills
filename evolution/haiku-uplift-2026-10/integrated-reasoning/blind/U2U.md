Neither of them is right, and I don't think there is a bug to find. The numbers say the engine is doing exactly what it was told, and what it was told is out of date. I'm about 85% confident of that. A 15-minute check, described below, would settle it.

**What the engine is doing**

62 x 1.06 = 65.72, rounded down to 65. So it sells 65 car-equivalents of space on a deck that holds 62.

That only works if enough people don't turn up. The 2023 factor was built on a 7.5% no-show rate:

- At 7.5% no-shows, 65 sold means about 60.1 turn up. That fits on the deck with a little room, and it's why the setting "has always worked".
- At this summer's 1.8% weekend no-show rate, 65 sold means about 63.8 turn up. That is already over 62 on average, so a full sailing overflows more often than not.

This matches your symptoms:

- **Only Friday and Saturday.** Those are the sailings that sell out to the 65 cap. Quieter sailings never reach it, so the factor never matters on them.
- **11 events versus 3 last summer.** Two things changed. Weekend no-shows fell, because the 7.5% came from a Nov-Feb winter sample and summer weekend travellers are committed and show up. You also removed one Friday and one Saturday sailing, which pushes the same demand onto fewer sailings and makes sell-outs more common. Each change makes overflow more likely, and together they would explain the jump.

**Who's right**

- **IT is right** that the engine works. It enforces the cap as configured.
- **Odile is wrong** that it's an IT fault. The setting is stale, and it's a business parameter, not code. The "always worked" claim was only true while the no-show rate was near 7.5%.
- The fix is a parameter change that Odile owns. I'd put that to both of them as "the input changed", not "you were wrong". That should take some heat out of the meetings.

**Fix before the bank-holiday weekend**

1. **Lower the factor for Friday and Saturday sailings now.** To break even at 1.8% no-shows you need about 62 / 0.982 = 63.1 units. A factor of 0.01 gives 62 (no overbooking), and 0.02 gives 63. I'd start at 0.01 for the bank-holiday weekend. Peak sailings carry the most risk, and a few empty spaces cost far less than leaving cars on the pier with a four-hour wait and a complaint to the council. Review it after the weekend.
2. **Set it per day type, not as one number.** Use your own recent weekend no-show data, not a Nov-Feb average, and re-measure each season. Keep a separate, higher factor for quiet sailings if you want one.
3. **Do a quick sanity check with IT.** Put a test sailing into the engine and book until it refuses. It should stop at 65 units. If it stops somewhere else, such as above 65, there is a real bug, and that is the ~15% I'm holding back. Also ask whether it counts in car-equivalents (van 1.5, campervan/trailer 2) or in raw vehicle counts. If it counts raw vehicles, that is a genuine defect and it would cause overflow on its own.

**The campervan issue is not separate**

You said you'd deal with it later, but it feeds the same problem. If the form defaults to "car" and people don't change it, a campervan booked as 1 unit takes 2 on the deck. That means 65 units sold can really be more than 65 units of space needed. It would also explain why the deckhands see the pressure at the weekend, when campervans are more common.

Before the bank holiday, pull the last 11 incidents and compare declared against actual vehicle types on the sailings that overflowed. That will show how much of the overflow comes from the factor and how much from misdeclared types. You can fix the form cheaply:

- Make vehicle type a required choice, with no default.
- Add a line such as "Campervan, motorhome, or anything towing a trailer? Select this type or you may be refused boarding."
- Consider a small surcharge or check at the pier for mismatches.

Lowering the factor handles the average problem. Fixing the form handles the variance and protects you if the no-show rate drifts again.

**Confidence and what would change my mind**

I'm fairly sure about the stale factor, because the arithmetic matches the pattern (weekend-only, sell-out sailings, a big rise on a small base). What would change my mind is the engine stopping at the wrong number in the test, or overflow on sailings that were not sold to the cap. If either shows up, the engine is at fault after all, and IT owns the next step.
