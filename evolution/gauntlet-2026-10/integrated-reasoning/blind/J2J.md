Short answer: neither of them is right, and I don't think there is a code bug. The most likely cause is the overbooking setting, which is out of date. I'm about 85% confident of that. The campervan issue is probably part of the same problem, not a separate one.

**What the numbers say**

- The engine sells up to 62 × 1.06 = 65.72, rounded down to 65 units. That is what it is configured to do, so IT is right that it "works".
- Overbooking only works if the expected no-shows cover the extra units sold. At the 2023 winter no-show rate of 7.5%, selling 65 would leave about 60 units turning up, which fits. At this summer's weekend rate of 1.8%, selling 65 leaves about 63.8 turning up on a full sailing. That is more than 62, so someone gets left behind.
- Three units of oversell against roughly 1.2 units of no-shows means a fully sold weekend sailing has a shortfall built in. It won't happen every time, because bookings arrive in lumpy sizes and some sailings don't sell out. But it will happen regularly on full sailings, and you have had 11.
- The break-even factor at 1.8% no-shows is about 0.018, which means selling about 63 units. Even 63 leaves almost no margin, and a safe setting for weekends is probably 62 or 63.

**Why it got worse this summer**

1. Last summer's three incidents show the 6% factor was already too high. The same settings are now hitting much fuller weekend sailings.
2. Dropping one Friday and one Saturday sailing squeezed the same demand into fewer departures. More weekend sailings now sell out, and only sold-out sailings can overflow. That also explains why every case is a Friday or Saturday.
3. The no-show rate was measured from November to February, when ferry travel is mostly locals and commuters, who skip bookings more often. Summer weekend travellers who have paid for a holiday crossing turn up much more reliably.

**Who's right**

- IT is right that the engine does what it was told. The fault is the input to it, not the code.
- Odile is right that overbooking worked before. It "has always worked" because the setting was fitted to a different season, and it stopped fitting once the season and timetable changed. The 0.06 comes from her predecessor in 2023, and nobody has re-checked it since. Keeping that figure up to date is a revenue management job, so this lands more on her side than IT's.

**The campervans are likely part of this**

The engine sells deck space in units, so a campervan booked as a "car" is counted as 1 but takes 2 on the deck. Every one of those hides a unit of load that the engine can't see. If a few of them are on each weekend sailing, they add to the overflow on top of the overbooking. They would also explain why the deckhands see the problem only at weekends, when campervans and trailers are most common. This is a plausible second cause, not a proven one, so I'd treat it as part of the same fix.

**What to do before the bank-holiday weekend**

1. Pull the 11 incident sailings. For each, note the units sold, the units that actually turned up (by real vehicle type, from the deck), and the number of no-shows. This will tell you in an hour how much is overbooking and how much is misdeclared vehicles. If the units that turned up exceed 62 even after allowing for disguised campervans, overbooking alone explains it.
2. Set the Friday and Saturday factor to 0 to 0.01 straight away, and keep the higher figure for quiet midweek sailings if you want. This is a configuration change, not a code change, so it can go live now, and for the bank-holiday weekend I'd take it down to zero. The cost is a few units of lost revenue per sailing, against furious reviews and council complaints.
3. Make the vehicle type on the booking form a required choice with no default. Better still, ask for length or height. If you can't change the form in time, add a rule that charges or holds extra space for anyone who picks "car" but enters a long vehicle's registration or length.
4. Set the factor from the live no-show rate per day of week and season, reviewed every month, instead of one fixed figure from one winter.
5. Ask IT for one thing only, which is to confirm the engine rounds down and is counting units, not vehicles. That is a five-minute check, and it also settles whether there is a real bug. If the sold total on the incident sailings never exceeded 65 units, the engine is clean.

**What I couldn't check**

I haven't seen the sailing-level data. If the 11 incidents turn out to have sold fewer than 65 units, the engine would be counting something wrongly, and that would change my answer, so step 1 is the test that could prove me wrong.
