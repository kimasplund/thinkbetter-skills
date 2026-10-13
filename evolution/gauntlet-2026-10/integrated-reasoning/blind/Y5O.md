Neither of them is right, and I don't think there's a bug in the booking engine. The problem is the overbooking setting, which no longer matches how the boat is being used.

**What the numbers say**
- The engine sells 62 x 1.06 = 65.72, rounded down to 65 car-equivalents. That is what it's configured to do, so IT is right that it works as designed.
- The 6% factor came from a 7.5% no-show rate measured from November to February. At 7.5%, 65 sold units give about 60 that turn up, which fits comfortably on 62.
- Your weekend no-show rate this summer is 1.8%. On a sold-out sailing, 65 sold units give about 63.8 that turn up. That is nearly 2 units more than the deck holds. A single campervan or trailer, which counts as 2, is enough to leave someone on the pier.
- So Odile is wrong that it must be an IT fault. The overbooking "has always worked" only because the winter no-show rate it was tuned to was much higher than the summer one.

**Why it got worse this June**
- Cutting a Friday and a Saturday sailing pushed the same demand into fewer sailings, so more of the remaining ones sell out. Overbooking only causes trouble on sold-out sailings.
- The remaining Friday and Saturday sailings are also fuller, which probably means fewer no-shows still.
- Last summer, with more sailings and a looser fit between demand and capacity, you had three incidents. This summer you have 11, all on Friday or Saturday. That fits.

**Campervans are probably part of this**
You called this a separate headache, but I think it feeds the same problem. If the form defaults to "car" and campervans are booked as cars, each one is counted as 1 when it takes 2. A sailing that looks like 65 units on paper can then hold more real deck space. The deckhands' complaint and your overflows may be the same issue seen from two sides.

**What to do before the bank holiday**
1. **Change the factor now.** Set it to 0 for Friday, Saturday and bank-holiday sailings, so you sell at most 62 units. With a 1.8% no-show rate, even a factor of 0.02 would still overflow on average. The cost is a few units of revenue on sold-out sailings, which is small next to the complaints and council attention. Keep a higher factor for the quiet weekday sailings if you like.
2. **Check the 11 incidents.** For each one, compare the units sold with the units that arrived, and the declared vehicle types with what actually drove on. If sold units were 65 or fewer and arrivals were over 62, that confirms the cause. If any sailing sold more than 65, then the engine has a real fault and IT needs to look at it.
3. **Fix the vehicle type field.** Remove the "car" default so the customer has to choose, and add a deck-staff check or a charge for mis-declared vehicles. This is a quick form change and doesn't need to wait.
4. **Reset the factor every season.** Set it from the actual no-show rate for each day type, not a winter average, and review it every few weeks in summer.

I'm assuming the 1.8% rate and the incident counts are accurate, and that "capacity" in the engine really is 62 car-equivalents rather than a vehicle count. If the engine counts vehicles instead of equivalents, that would be a separate bug, but step 2 will show it.

For the meetings, the useful framing is that IT delivered what was specified and the specification has gone stale. That should lower the temperature between them.
