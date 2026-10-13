**Short answer: neither of them is right, because this probably isn't a software bug. The engine is doing what it was told. The setting it was told to use is out of date.**

**The arithmetic**

- The engine sells 62 × 1.06 = 65.72, rounded down to **65 car-equivalents**.
- The 6% factor came from a 7.5% no-show rate measured in November to February. At 7.5%, 65 sold gives about 60.1 arriving, which fits on a 62 deck with room to spare. That is why it "always worked".
- This summer's weekend no-show rate is 1.8%. At 1.8%, 65 sold gives about 63.8 arriving, which is **about 2 car-equivalents more than the deck holds**, on average. Roughly half of fully sold sailings would overflow even before random variation.
- The break-even factor at 1.8% no-shows is about 62 / 0.982 = 63.1, so a factor of roughly 1.8%. Your 6% is more than three times too high for current behaviour.

**Who is right**

- **IT** is right that the engine works as configured. It sells exactly what the formula says.
- **Odile** is right that overbooking worked before. It worked because winter no-shows were high. She is wrong that this makes it an IT fault. The parameter is a business decision, and it has gone stale. A 2023 winter measurement was applied to a summer weekend peak, and that was never going to hold.

**Why it hit only Fridays and Saturdays, and why it got worse this year**

- Dropping a Friday and a Saturday sailing pushed the same demand onto fewer sailings. Those sailings fill completely, which is the only situation where overbooking can hurt you. Weekend passengers are also the ones most likely to show up (low no-show).
- Last summer you had three overflows all season. Now you have 11 in a few weeks. That fits the timetable change plus the stale factor.

**A second contributor to check: vehicle type**

The deckhands' complaint about campervans booked as cars may be part of the same problem. If a campervan (2) is booked as a car (1), the engine counts 1 and the deck needs 2. Every misclassified vehicle adds an unbooked extra unit on arrival. On a sailing sold to 65, a handful of these is enough to turn "just fits" into "left on the pier". This isn't a separate headache. It makes the overflow worse and it makes your no-show data unreliable. It is also a real software and form-design weakness, since a default of "car" is the cheapest way to get it wrong. I can't tell from here how much of the 11 it explains. Your data can.

**What to do before the bank-holiday weekend**

1. **Lower the factor now.** This is a config change and needs no code. Setting it to 0 (sell 62) removes the overflow risk. A factor of about 0.02 (sell 63) is the most you can justify at 1.8% no-shows. Given the vehicle-type problem, I'd start at 0 to 0.02 for Fridays and Saturdays for the bank-holiday weekend and revisit it with data. A bank-holiday weekend will probably have lower no-shows than a normal one, so don't use the average.
2. **Make the factor depend on day and season.** Use a separate no-show rate for Friday and Saturday summer sailings, measured from recent data. Review it every month or so.
3. **Fix the vehicle type cheaply.** Remove the default so the customer has to choose. Add length or height fields, or a line like "campervans and anything with a trailer count as 2 spaces". Consider a deck-side check or a surcharge if the type turns out to be wrong.
4. **Verify with data, not argument.** For the 11 overflow sailings, pull the number of bookings sold, the number that showed up, and the car-equivalents actually loaded. If sold was 65 and arrivals were above 62 in every case, the stale factor explains it. If arrivals in car-equivalents were higher than the booked car-equivalents, misclassification explains the gap.
5. **Get a code check for peace.** Ask IT for one sentence confirming the engine computes `floor(62 × (1 + 0.06))` = 65, and that it counts a campervan as 2 when it is booked as one. That should end the argument.

**Assumptions:** I'm assuming the 1.8% figure is for weekend sailings in vehicle-equivalent terms, that the engine treats the 62 as a hard capacity, and that the 11 sailings were sold at or near the cap. If sailings that overflowed were sold well below 65, something else is going on and the engine should be checked.

**Compensation:** For the people left on the pier and the council complaints, I'd put a clear message out saying that overbooking is being reduced for weekends, with a goodwill gesture such as a fare refund or priority on the next sailing for those affected.
