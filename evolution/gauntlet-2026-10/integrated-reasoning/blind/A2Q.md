**Short answer: neither is quite right. The engine is doing what it was told, so IT is correct that there's no software bug. But Odile is wrong that "it has always worked". The overbooking setting is stale, and it's a business-parameter problem, not an IT fault.**

**The arithmetic**

- Capacity 62 x 1.06 = 65.72, rounded down to **65 car-equivalents sold** per sailing. That's 3 units more than the deck holds.
- The break-even no-show rate for that is 1 - 62/65 = **4.6%**. If fewer than 4.6% of booked space doesn't turn up, someone is left on the pier.
- The 2023 factor was set from a 7.5% no-show rate. At 7.5%, 65 sold gives about 60 units showing up, which fits on the deck with room to spare. The factor worked then.
- This summer's weekend no-show rate is 1.8%. 65 x 0.982 = about **63.8 units turning up for 62 spaces**. On an average weekend sailing you're already over capacity, so small variation (a few campervans, a full boat) produces left-behind vehicles regularly.

So the engine sells exactly what the configured factor says. The factor assumes a no-show rate that no longer applies.

**Why it got worse this year (three causes, in order of likely weight)**

1. **The factor was calibrated on the wrong data.** It was measured November to February. Winter travellers (islanders, commuters, work trips) behave differently from summer weekend visitors, who have prepaid, planned holidays and rarely skip. A winter no-show rate says little about a summer weekend.
2. **You cut one Friday and one Saturday sailing.** Demand from the removed sailings moves onto the remaining ones, so those fill up with people who have fewer alternatives and are less likely to no-show. This explains why every incident is a Friday or Saturday, and why this year is 11 against 3 last summer. It also deserves a check in your data: confirm the incidents began on 1 June and compare the no-show rate before and after the change.
3. **Vehicle types are probably under-declared.** The form defaults to "car" (1.0), and the deckhands think campervans are booked as cars. A campervan booked as a car takes 2 units of deck but only 1 of booked space. This is not a separate headache. It feeds the same problem, because the engine thinks the deck has more room than it does, and it makes the overbooking worse on top of the factor. Even a few per sailing is enough to account for the 1 to 3 units of overflow.

**What to do before the bank-holiday weekend (three weeks)**

1. **Set the overbooking factor to 0 for Friday and Saturday sailings now** (or at most 0.02, which sells 63 units). At 0, you sell 62 and at a 1.8% no-show rate about 61 turn up, so the deck almost never overflows. A few empty spaces cost far less than a vehicle stranded for four hours, plus the reviews and council complaints. Ask IT to make the factor configurable by day of week if it isn't already. This is a settings change, not a code fix, and it can be done this week.
2. **Keep a modest factor on quieter days** (Sunday to Thursday) only if the no-show data supports it. Recompute from this summer's actual data per day type, with the break-even rule above (factor should be no higher than the observed no-show rate, with a safety margin).
3. **Fix the vehicle-type problem enough to help the bank holiday.** Make the form require a choice (no default), or add a prompt for height/length. Check against the registration or a "is this a campervan, motorhome or has a trailer?" question. A quick win is to look at last weekend's actual loading against bookings to see how many were mis-declared. Consider a surcharge or a reload fee if a vehicle turns up bigger than booked.
4. **Check the data to confirm the diagnosis.** For each of the 11 incidents, pull booked units, units turned up, and the type mix. If booked units were 65 and turned up were over 62, it confirms the above. If the booked units were within 62 and still didn't fit, the misdeclared vehicles are the main cause (or loading efficiency, since a real deck can't always be filled to 100% with mixed lengths).
5. **Use a standing rule going forward.** Review the factor each season and by day type, using the latest 8 to 12 weeks of data, so it can't go stale again.

**For the meetings**

- To IT: you're right that the engine has no bug. It would still help to make the factor adjustable by day and to log booked versus arrived units per sailing.
- To Odile: the logic of overbooking was sound, but the number was set from winter data and has not been revisited since 2023. That's a revenue-management decision, so this one is yours to fix, and the fix is a configuration change.

Neither side did anything wrong in a way that requires blame. The inputs changed and nobody re-checked the setting.

**Assumptions:** I've assumed the engine uses the car-equivalent units you describe, that the 1.8% figure is a booked-unit no-show rate rather than a count of vehicles, and that the 11 incidents are spread across the weekend sailings that remain.
