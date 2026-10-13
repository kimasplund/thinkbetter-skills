Short answer: neither of them is right, and I don't think there is a software bug. The engine is doing what it was told. The setting it was told to use is out of date. The fix is a config change you can make this week.

**What the numbers say**

- The engine sells 62 x 1.06 = 65.72, rounded down to 65 car-equivalents per sailing.
- That only works if enough people don't show up. At the 7.5% no-show rate the 2023 setting was based on, 65 sold means about 60.1 turn up, which fits on a 62 deck with a little room.
- At this summer's weekend no-show rate of 1.8%, 65 sold means about 63.8 turn up. That is above 62 before any variance. So on an average Friday or Saturday sailing you are already about 2 units over, and any sailing that is a bit fuller than average leaves people on the pier.

The setting is wrong for the season you are in. It is not malfunctioning.

**Why it used to work**

- The 2023 rate was measured from November to February. Winter travellers, and the small number of weekend travellers in winter, cancel and no-show far more than summer holidaymakers who have booked a ferry to a island months ahead. Summer no-shows are always lower, so the factor was always too generous for July and August. It just hadn't bitten much. You had three incidents all of last summer, and that is consistent with a margin that was already thin.
- This year you cut one Friday and one Saturday sailing. The same demand now sits on fewer sailings, so the remaining ones are fuller and more likely to have everyone turn up. That is why all 11 incidents are Friday or Saturday sailings, and why it jumped from 3 to 11 after 1 June.

**Who is right**

- IT is right that the engine works as specified. I can't see the code, but the behaviour is fully explained by the formula and the inputs. A 5-minute check will confirm it: take one of the 11 sailings, add up the booked units, and see whether the total was 65 or less. If the engine sold 65 or fewer and more than 62 turned up, it is not a bug.
- Odile is right that the overbooking "has always worked", but that isn't evidence of an IT fault. It worked because the no-show rate was high enough to absorb it. The factor is a business parameter, and keeping it current is a revenue management job. Nobody has re-measured it since 2023, and I would say that is the real root cause.

It's worth saying this to both of them in those terms, because it lets each of them be partly right and ends the argument.

**What to change before the bank-holiday weekend**

1. Lower the factor now. To expect 62 turn-ups at a 1.8% no-show rate you would sell about 63 units, which is a factor of about 0.015. But that gives you zero room for variance, and the cost of leaving someone on the pier (four hours' wait, a review, a complaint to the council) is much higher than the cost of one empty unit. For the bank-holiday weekend I would set the factor to 0 for Friday, Saturday and the holiday Monday sailings, so you sell exactly 62. Keep a higher factor on quiet midweek sailings if you want.
2. Make the factor depend on the day and season. A single number for the whole year is what caused this. Measure no-shows separately for weekend and weekday sailings, and for summer and winter, and review it each quarter. Ownership: Odile.
3. Confirm the one thing I'm assuming. I am assuming the engine counts booked space in car-equivalents, not in vehicles. If it counts vehicles (62 x 1.06 = 65 vehicles), then mixed vans and campervans make it worse, and IT should show you which.

**The campervan problem is not separate**

You said you'll deal with it later, but I think it is feeding this one. If a campervan books as a "car" because that's the form default, the engine reserves 1 unit but it takes 2 on the deck. A few of those per sailing, on top of an overbooking margin that is already too high, is enough to turn 63.8 expected turn-ups into 66 or more. I can't tell from what you've written how much of the 11 is from this and how much from the factor. The sailing records will tell you: for each of the 11, compare the units booked with the units actually loaded. If the loaded total is well above the booked total, the vehicle type is part of the cause.

A cheap fix is to remove the default so the customer must pick the vehicle type, and to ask for length or height when they book. Then charge or re-class at the pier when the vehicle doesn't match. That's a form change, which is fast, and I would try to get it in before August too.

**How sure I am**

About 85% that the stale factor, plus the reduced number of weekend sailings, is the main cause. The arithmetic is clear and it matches the pattern you describe: weekends only, a sharp rise after the timetable change. The remaining doubt is about the campervan mix and the unit counting, which the sailing records can settle in an hour.
