Neither side is quite right. From what you've described, the engine is probably doing exactly what it was told, and the fault is the overbooking factor. That is a business setting, not an IT fault. I'd put this at roughly 80% likely, and you can confirm it quickly (see below).

**What the engine does now**
- 62 x 1.06 = 65.72, rounded down to 65 deck units sold per sailing.
- That only works if about 4.6% or more of bookings fail to show: 1 - 62/65 = 4.6%, and a little more in practice because of the variation described below.
- The 2023 factor was set from a 7.5% no-show rate, measured from November to February. Winter foot-traffic and off-season bookings are the most likely to cancel or not turn up. Summer weekend travellers are far more committed.
- This summer's weekend no-show rate is 1.8%. At that rate, 65 sold units give an expected 63.8 units arriving for 62 units of space, so most full weekend sailings will overflow.
- The timing also fits. Dropping a Friday and a Saturday sailing pushed demand onto the remaining weekend sailings, which are now the ones that sell out. All 11 incidents are Friday or Saturday, which is the pattern you'd expect.

**Odile and IT**
- IT is right that the engine works. It sells what the formula says.
- Odile is right that the setting used to work. It was last summer's low-demand weekends that hid the problem, and the three incidents all season fit that. She is wrong that it must be an IT fault. The setting has gone stale, and since she owns the setting, this is a revenue-management decision.
- That should take the heat out of the meetings. Nobody has to have been wrong. The inputs changed.

**A second, smaller contributor**
You called the campervan issue separate, but I wouldn't treat it that way. The engine counts space in car-equivalents, so a campervan booked as a "car" takes 2 units of deck but is sold as 1. Every misdeclared campervan quietly oversells the sailing by one unit, on top of the overbooking. The deckhands' complaint and the left-behind cars may be the same problem. It matters most on busy weekend sailings, which is where you're failing.

**How to confirm in an afternoon**
1. Pull the 11 failed sailings. For each, add up the units booked and the units that actually arrived, using real vehicle types from the deck.
2. If booked units were at or below 65 and arrivals were above 62, the factor is the cause. If arrivals were far higher than the booked units, misdeclared vehicle types are the cause. Expect some of each.
3. Check that the engine really sells 65. A test booking run on an empty sailing will show it. This is the only check that could put the fault back on IT.

**What to do before the bank-holiday weekend**
- **Lower the weekend factor now.** At a 1.8% no-show rate the break-even is about 1.8% (62 / 0.982 = 63.1). A factor of 0.02 sells 63 units and 0.00 sells 62. Given the cost of leaving cars on the pier, I'd use 0.00 to 0.02 for Friday, Saturday and the bank-holiday sailings. Overbooking costs you far more than a few empty spaces do.
- **Set the factor per day and season.** Use a separate factor for weekends and summer, and recalculate it from recent data. Do this every season, not once every few years.
- **Stop trusting the vehicle-type default.** Ask for vehicle length or height at booking, or make the type field mandatory with no preselected value. Alternatively, require campervan owners to confirm the type. This is cheap, and it also fixes the loading delays you mentioned.

Last, a business choice: if you want overbooking to stay on, set a policy for who gets bumped, such as the last bookings made, and what compensation they get. Without a rule like that, the island council complaints will keep coming even when the numbers are right.
