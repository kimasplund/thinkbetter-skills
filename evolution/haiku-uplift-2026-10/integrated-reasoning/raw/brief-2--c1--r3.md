Short answer: it probably isn't a software bug, and neither side is quite right. IT is right that the engine does what it was told. Odile is right that nothing changed in the engine, but wrong that this means it must be an IT fault. The setting is out of date. I'd put roughly 85% on that being the main cause.

**The arithmetic**

- Capacity is 62. At a factor of 0.06 the engine sells up to floor(62 x 1.06) = floor(65.72) = 65 car-equivalents. That is 3 more than the deck holds.
- The 0.06 only works if enough people fail to turn up to absorb those 3. The 2023 figure was a 7.5% no-show rate. At 7.5%, a full sale of 65 gives about 65 x 0.925 = 60.1 arriving, which fits.
- At this summer's weekend no-show rate of 1.8%, a full sale of 65 gives about 65 x 0.982 = 63.8 arriving. That is already about 2 over the deck on average, before any random variation. A sailing that is sold out will overflow more often than not.
- To break even at 1.8% you would sell only about 62 / 0.982 = 63.1. That means a factor of about 0.02. A cushion for random variation would push it lower still.

So the engine is working as configured, but the 0.06 was calibrated on winter data and is wrong for summer weekends. A winter no-show rate says little about a summer weekend. Winter travellers are more often casual or commuter trips, and summer weekend holidaymakers with pre-paid bookings rarely skip.

**Why it shows up now, and only on Fridays and Saturdays**

- Dropping one Friday and one Saturday sailing pushed the same demand onto fewer sailings. Those sailings now sell out much more often, and overbooking only bites on a sold-out sailing. That fits 11 incidents since 1 June, all on Fridays or Saturdays, against 3 all of last summer.
- The timetable change didn't break anything. It made the stale setting matter.

**What would show I'm wrong**

Pull the booking records for the 11 sailings and check these:

1. What was the total sold on each? If the engine never went above 65, it is behaving correctly. If any went above 65, then there is an engine or rounding fault, and IT needs to look at it.
2. What was the actual no-show rate on those sailings, compared with 1.8%?
3. Did the vehicles that arrived, measured in car-equivalents, exceed 62 by more than the overbooking explains? If so, something else is adding to the overflow (see the campervan point below).

If the totals sold are 65 or below and arrivals are about 63 to 65, my diagnosis holds.

**The campervan issue is not separate**

You've set it aside, but it feeds directly into this problem. The deck is counted in car-equivalents. A campervan booked as "car" is counted as 1 but uses 2. If a handful per weekend are booked as cars, the engine thinks there is room that doesn't exist. Every mis-typed campervan quietly uses up one unit of the overbooking cushion. So some of your 11 overflows may be caused by the mix of vehicles, not only by the factor. Step 3 above will show how much. This matters because lowering the factor fixes the overbooking part but not the mix part.

**What to do before the August bank-holiday weekend**

1. Today, lower the overbooking factor for Friday and Saturday sailings. Setting it to 0 (sell exactly 62) is the safe choice for the bank-holiday weekend. About 0.02 (sell 63) is a reasonable option if you want to keep a small cushion. Give weekdays and winter sailings their own values, because their no-show rates really are higher.
2. Make the factor depend on the season and the day of the week, and review it against measured no-shows, say monthly. A fixed number set once in 2023 is what got you here.
3. Cheap fix for the vehicle type: remove the default of "car" so people must choose, and show the car-equivalent sizes on the form. This could reasonably be done before the bank holiday, since it is a form change and not a pricing change.
4. For the meetings between IT and Odile: the dispute dissolves once both accept that the question is "what should the number be?", not "who broke it?". Odile owns the number. IT owns making the engine apply it correctly, which the data should confirm in step 1 above.

The cost to weigh is revenue. Selling 62 and not 65 on a full sailing gives up up to 3 car-equivalents, though that is small next to furious reviews, island council complaints and cars left four hours on the pier.
