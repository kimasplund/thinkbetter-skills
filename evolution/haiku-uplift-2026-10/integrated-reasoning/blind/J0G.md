**Short answer: IT is right that the engine works, and Odile is right that the overbooking "always worked". Neither is the cause. The bug is a stale setting, and probably a data problem too.**

**1. The engine is doing what it was told**

- 62 x 1.06 = 65.72, rounded down to 65 car-equivalents sold per sailing. That is the engine working as specified.
- The 6% factor came from a 7.5% no-show rate measured in November to February. Winter no-shows are not a good guide to summer weekends.
- This summer's weekend no-show rate is 1.8%.
- At 1.8%, a full sailing of 65 units gives about 65 x 0.982 = 63.8 units showing up, against 62 of space. You are over capacity on average on any sailing that sells out.
- A sailing is over capacity whenever fewer than about 3 units of bookings fail to show up. With a 1.8% rate that is the normal outcome, not bad luck.
- In 2023 the same 6% was roughly right for a 7.5% no-show rate, since 65 x 0.925 = 60.1. That is why it "always worked", and why last summer had only three overflows.

So the problem is not in the code. It is in an input that stopped matching reality. Nobody owns re-checking that input, which is why the two of them are arguing past each other.

**2. Why it got bad on 1 June**

Dropping a Friday and a Saturday sailing pushed the same weekend demand onto fewer sailings. Those sailings now sell out more often, and a sold-out sailing is where overbooking bites. This fits all 11 incidents being Fridays or Saturdays.

**3. The campervan issue is probably part of the same problem**

- You called it a separate headache, but I would not treat it that way.
- The form defaults to "car" (1.0). A campervan or a car with a trailer takes 2.0.
- Every misdeclared vehicle means the engine thinks it has sold less deck space than it has. Deck space is overcommitted on top of the overbooking.
- Check this first, because it is cheap to measure. For the 11 incidents, compare booked vehicle types with what actually boarded or was turned away. Do the same for a few sold-out weekend sailings that did not overflow.

**4. What I would do before the bank holiday (three weeks)**

1. **Pull the actual data.** For each weekend sailing since 1 June, get units sold, units that showed up and units left behind. This gives you a real no-show rate by day, and shows how much of the overflow is misdeclared vehicles.
2. **Lower the overbooking factor now.** At 1.8% no-shows, the break-even factor is about 1.8%, which is 62 x 1.018 = 63.1, so 63 units sold. Because left-behind passengers cost you far more than an empty space does, I would go lower, to 0 to 1% on Fridays and Saturdays (62 to 62.6, so 62 units). Keep a higher factor on quiet sailings if the data supports it. This is a configuration change, not a code fix, so it can go in this week.
3. **Make the vehicle type something people must choose.** Remove the "car" default and add a required choice with a short note ("campervan, motorhome or anything with a trailer counts as 2"). Consider asking for vehicle length or height too. Even a quick change to a required dropdown will help.
4. **Handle the bank-holiday weekend specifically.** Bank-holiday demand is high and no-shows are typically low, so use the most conservative setting there. Consider a standby or priority rule for the sailing after, and send an advance message to people holding bookings.
5. **Fix the ownership gap.** Review the factor every season, using the last full season's no-show data, split by day type. Give one person that job.
6. **Recheck the timetable.** Weigh the crew hours saved by dropping those two sailings against the cost of the complaints, refunds and council attention. I can't see your figures, but it may not have been a good trade.

**5. Settling the dispute**

- Tell IT their engine passed because it matches the spec, and ask them for a change that lets the factor be set per day or sailing type, with a report that logs booked vs. boarded units.
- Tell Odile the factor is a business parameter, not a code setting, so the revenue side owns it, and it needs updating.
- The disagreement is about whose job it is to keep the number current, not about a bug.

**Assumptions:**

- I've assumed the engine counts units correctly (a van as 1.5 and so on) and only applies the factor to total capacity. If it applies the factor per vehicle type, or counts vehicles instead of units, that could be a real bug, so have IT confirm with one test booking.
- I've also assumed your 1.8% is measured in units, not bookings. If it's by booking count, the real unit figure could differ.
- I have no data on how many of the 11 overflows involved misdeclared campervans. The numbers above show overbooking alone is enough to cause overflows, but the campervan share is something to measure rather than guess.
