Neither of them is right, and I don't think there is a code bug. The most likely cause is a stale setting, and it's a business input, so it belongs to neither IT nor Odile alone.

**What the numbers say**

- The engine sells 62 x 1.06 = 65.72, rounded down to 65 car-equivalents. So it deliberately sells 3 units more than the deck holds. That is exactly what you configured, so IT is right that the engine is doing what it's told.
- The 0.06 was chosen to cover a 7.5% no-show rate. At 7.5%, a full sailing of 65 units loses about 4.9 units to no-shows, which leaves the deck comfortably full without overflowing.
- The weekend no-show rate is now 1.8%. A full sailing of 65 units loses only about 1.2 units, so about 63.8 units turn up for 62 spaces. On average that is nearly 2 units too many, and a bad day is worse. Overflow on any full sailing is therefore expected, not a freak event.
- The break-even factor at 1.8% no-shows is about 62 / 0.982 = 63.1 units, or a factor of roughly 0.018. Your 0.06 is more than three times that.

Odile's "it has always worked" is true, but only because the rate it was tuned to was far higher than today's. The 7.5% figure was measured November to February, which is off-season. Winter no-shows say little about a summer weekend, when people have paid for a holiday and are far less likely to skip the boat. So the setting was fragile before this summer.

**Why it got worse in June**

Dropping a Friday and a Saturday sailing didn't change the no-show rate, but it pushed the same demand onto fewer sailings. The remaining weekend sailings now sell out to the full 65 far more often. Overbooking only causes harm on sailings that sell to the cap, so more sold-out sailings means more overflow. That fits all 11 incidents being Fridays or Saturdays, and 3 last summer against 11 now.

**The campervan issue is probably not separate**

Please don't leave it for later. If the form defaults to "car" and a campervan books as 1 unit but turns up as 2, the engine thinks there is room that isn't there. Each mislabelled campervan quietly adds a unit to the real load, on top of the 3-unit overbook. I can't tell from here how much of the 11 this explains. It may be a lot, because weekends are when campervans travel.

**What to check this week (an hour or two with the data)**

1. For each of the 11 sailings, pull the units sold, the units that actually arrived (counting vehicles by their real size at the deck), and the no-show rate. If sold was 65 and arrivals were about 63 to 66, overbooking alone explains it. If arrivals exceed what the sold units could produce at a 1.8% no-show rate, mislabelled vehicles are adding to it.
2. Ask IT to confirm one thing: the engine counts in car-equivalents rather than in vehicles. If it counts vehicles, that is a real bug. A van or campervan would be counted as 1, and the deck would overfill even without overbooking. Nothing you've described suggests this, but it is the one place a genuine fault could hide, so ask.
3. Compare the weekend no-show rate for each sailing, not just the average. Rates can differ a lot between a Friday evening and a Saturday morning.

**What to do before the August bank holiday**

- Set the overbooking factor to 0 for Friday and Saturday sailings, and for the bank-holiday weekend including the Monday if it's busy. The cost of a few empty units is small next to the cost of cars left on a pier for four hours, council complaints and reviews. At 1.8% no-shows, even 0.01 is only worth about one extra unit and still risks overflow.
- Make the factor a setting that depends on season and day. Winter and midweek can carry a higher factor, and peak weekends should carry little or none. Review it each month against the actual no-show rate for that sailing type.
- Make the vehicle type on the booking form a required choice with no default, and ask for the length or height for anything that isn't a plain car. That also settles the deckhands' grumbling. You can do it before August, but if you only have time for one, do the factor first.

**On Odile and IT**

Both are partly right and both are missing the point. The engine runs as configured, and the configuration was right for winter 2023 and is wrong for a summer weekend now. Reframe it in the next meeting as "the input is stale", not "someone is at fault". The fix is a parameter change plus a clean look at the 11 sailings' data to confirm.

I'm about 80% confident the stale factor and the fewer weekend sailings account for most of the problem. The remaining uncertainty is how much the campervans and the unit-counting add, which the data in step 1 will show.
