Short answer: neither of you is entirely right, and I don't think there's a code bug in the engine. The overbooking setting is wrong for this summer. Odile is closer to the cause, but the real problem is a stale input, and there is a second, separate gap that makes it worse.

**1. The arithmetic is doing what it was set up to do**

- Capacity 62 × (1 + 0.06) = 65.72, rounded down = **65 car-equivalents sold** per sailing.
- Your break-even no-show rate for that setting is 1 − 62/65 ≈ **4.6%**. Above that, the boat has room. Below it, you overflow.
- The 2023 factor was calibrated to a 7.5% winter no-show rate, so it was sensible then. This summer's weekend rate is 1.8%.
- At 1.8%, expected arrivals ≈ 65 × 0.982 ≈ **63.8**, which is about 1.8 over the deck on average. Friday and Saturday variance then pushes some sailings well past 62. Your 11 overflows on Fri/Sat fit this.

So IT is right that the engine isn't mis-computing, and Odile is right that the overbooking is the cause. "It has always worked" was true only in the season it was calibrated for.

**2. Fix for August (the setting, not the code)**

- Work out the factor from current data, not the 2023 number. Keep a margin below break-even so variance doesn't overflow the deck.
- Note the rounding: 62 × 1.01 = 62.62 rounds down to 62, so any factor under about 1.6% sells no extra space at all. A "small" factor like 0.01 is effectively zero overbooking. Test the real output of your engine at the values you're considering.
- Consider separate factors for weekends and weekdays, and for summer and winter, since no-show behaviour clearly differs.
- Re-check the factor monthly with the actual no-show rate, and cap it at a figure you can defend to the council.

**3. The vehicle-type gap (this is a real defect, and it's tied to the bug)**

If the engine sells against car-equivalents but a campervan is booked as "car", it counts as 1 when it actually takes 2. The engine then believes it has space it doesn't have, regardless of no-shows. Your deckhands' "campervans disguised as cars" observation is exactly this. It's a bigger driver of overflow than the factor if many weekend bookings are misclassified. I'd not leave it until "later" if you're fixing the factor before August: a simple guard (a required vehicle-type confirmation with a length or height question, or a weighted count at check-in) would close it.

**4. How to confirm before you change anything**

- Pull the manifests for the 11 overflow sailings. For each, compare the weighted total of boarded vehicles (car 1, van 1.5, campervan/trailer 2) with the number the engine sold. If the gap is mostly no-shows, it's the factor. If boarded weight exceeds what was sold for vehicles booked as "car", it's the vehicle-type gap.
- Check whether the engine's cap is applied in car-equivalents or in vehicle count. If it's vehicle count, vans and campervans will overflow even with zero no-shows, and that would be a genuine code bug, so IT should confirm this.
- Check how the dropped Friday and Saturday sailings changed demand per remaining sailing. Concentrated demand can push the sold-to-capacity ratio up and is a plausible second contributor.

**Assumptions I made:** the engine counts sales per sailing; the 1.8% is representative of the Fri/Sat sailings specifically; and the booking form's "car" default is the only source of misclassified vehicles. If any of these are wrong, the arithmetic above still holds but the split between causes will change.

**Bottom line:** the overbooking factor is stale for summer, which is Odile's point. The vehicle-type default is a separate, real defect that IT and the deckhands are both pointing at. Before August, reset the factor (and check the rounding), fix or guard the vehicle type, and verify against the manifests.
