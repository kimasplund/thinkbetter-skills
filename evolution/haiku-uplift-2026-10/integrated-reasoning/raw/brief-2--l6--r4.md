Neither of them is quite right, and I don't think the engine has a bug. The most likely cause is a stale overbooking setting, made worse by the vehicle-type default you called a separate headache. I haven't seen the engine, so the numbers below are my own working. Part of this can be checked in an afternoon.

**1. The overbooking factor no longer matches reality**
- The engine sells floor(62 x 1.06) = floor(65.72) = **65** car-equivalents against a 62-unit deck. That is 3 units of oversell.
- The 6% factor was set from a 7.5% no-show rate measured November to February. That is winter traffic, and it isn't representative of summer weekends.
- Weekend no-shows are now 1.8%. At 1.8%, about 64 of the 65 sold units turn up. That is 2 more than the deck holds, so a full sailing is oversold.
- Last summer you had 3 incidents, which suggests the factor was already marginal at that point.
- The break-even factor at 1.8% no-shows is about 1.8%, which sells 63 units. That leaves no safety margin, so I'd choose something lower.
- A factor of 0 to 1% (sell 62) is the safe setting for peak weekends.

**2. The timetable change concentrates demand**
- Dropping one Friday and one Saturday sailing pushed the same demand into fewer sailings. Those sailings now sell out more often, so they hit the oversell limit more often.
- This explains why all 11 incidents fall on Fridays and Saturdays. Sailings that don't fill never reach the overbooking cap, so they never show the problem.

**3. The vehicle-type default is probably part of this problem**
- The engine counts space in car-equivalents. A campervan booked as a "car" is counted as 1 unit but takes 2. A van booked as a car is counted as 1 but takes 1.5.
- A handful of misclassified vehicles per sailing is enough to push an exactly-full deck over. So the deckhands' complaint and your left-behind customers may be the same underlying cause.

**Who is right**
- **IT** is probably right that the engine does what it was configured to do. The arithmetic gives 65, which matches the formula.
- **Odile** is wrong that it must be an IT fault. The overbooking "has always worked" only because last summer's conditions made it work. Nobody has revalidated the factor since 2023.
- The real fault is ownership. The parameter was set once from the wrong season and never reviewed.

**What to do before the August bank holiday**
1. **This week:** Set the overbooking factor to 0, or to about 0.01, for Friday and Saturday sailings. This is a config change, so it is very low risk. It costs a little revenue and removes most of the stranded-customer risk. Bank-holiday weekends should get zero overbooking.
2. **Check the engine (about an hour):** Ask IT to show the computed sellable capacity for one Friday sailing. If it reads 65, the engine is behaving as designed. Also ask whether the units counted are car-equivalents or vehicle counts. If they are vehicle counts, that is a real bug.
3. **Pull the data for the 11 incidents:** For each one, compare booked vehicle types against what actually arrived. If campervans or vans were mostly booked as "car", that confirms point 3.
4. **Fix the form:** Remove the default so the customer must choose a vehicle type. Add a note about campervan size. If you want a safeguard, ask for the registration or the vehicle length.
5. **Fix the process:** Have Odile own the factor. Recompute it each season from the same season's no-show data, by day of week, and review it before each peak period.

**Assumptions:** I assumed the 1.8% figure is measured the same way as the 7.5% one (no-shows as a share of booked units). I also assumed the 11 incidents are not explained by a deck-loading problem such as poor stowage, which would waste capacity. If the data in step 3 doesn't fit, tell me what you see and we can narrow it down.
