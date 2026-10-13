Short answer: neither side is fully right, and the most likely cause is a stale setting rather than a code fault. Odile is closer to the root cause, but "it has always worked" is the wrong test. I can't see the booking engine's code, so the points below are inferences from your numbers. Please check them against the engine's configuration and the booking records for the 11 sailings.

**What the numbers say**

- Deck capacity is 62. With a 0.06 factor, the engine sells up to floor(62 × 1.06) = 65 car-equivalents per sailing.
- The 0.06 factor was set from a 7.5% no-show rate. Summer weekend no-shows are 1.8%.
- On a sailing sold to 65 at 1.8% no-show, you expect about 63.8 units to turn up against 62 spaces. Overflow is the normal outcome on a full sailing, not an exception. Only a few no-shows are needed to clear the 3-unit margin, and at this rate you should expect roughly one no-show per full sailing.
- The factor was right for November to February, when no-shows were higher. It is wrong for summer. That explains why it "always worked" for Odile and why the problem started with the summer timetable.
- The 11 incidents all fall on Fridays and Saturdays, which matches a full-sailing overflow. Dropping one Friday and one Saturday sailing concentrated the demand on the sailings that remain.

**Rough break-even**

- At 1.8% no-show, a factor of about 0.02 sells about 63 units and expects about 61.9 to show. That is roughly break-even, with no margin for error.
- A factor of 0.00 to 0.01 (sell 62 or 63) is safer for weekend sailings. You lose a little revenue, but you stop leaving people on the pier.
- Any single fixed factor will be wrong in some season. The factor should be set per season and per sailing day, using measured no-show rates, and reviewed at least each quarter.

**Possible second fault: vehicle weights**

- Check whether the engine counts car-equivalents (car 1, van 1.5, campervan or car with trailer 2) or simply counts bookings.
- If it counts bookings, every campervan booked as a "car" is undercounted by 1 unit. Two or three of those on a full sailing use up the whole margin. This would fit the deckhands' complaints about campervans on weekends.
- If the engine does use weights, the default vehicle type of "car" still undercounts at the booking stage. Either way, the default should be fixed. It is a small change that can go in alongside the factor change.

**What I would do before the August bank holiday**

1. Confirm the units the engine sells in, using a few booking records from the 11 bad sailings.
2. Lower the factor for weekend sailings now, to 0.00 to 0.01. This is a configuration change, not a code fix, and it can be made today.
3. Change the default vehicle type from "car" to require an explicit choice, or infer campervans from the booking if you can.
4. Check whether the engine has a waitlist or overflow rule. If it doesn't, turning one on protects the pier even when the factor is wrong.
5. Consider adding back one Friday or Saturday sailing for August. Four-hour gaps are the real cost of the timetable cut, and no overbooking setting removes that.

**Assumptions I made**

- The no-show rate of 1.8% is a per-booking rate. If it is per vehicle, campervans and vans may behave differently.
- Bookings for vehicles of different sizes are sold against the same 62-unit limit.
- The engine is configured as you describe, with no hidden buffer.

If you can send the engine's sell-limit formula or a sample of the booking records, I can check the units question directly.
