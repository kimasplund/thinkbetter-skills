Short answer: neither IT nor Odile is entirely right, but the evidence points at the setting, not a fault in the engine's code. Odile is closer on the cause and IT is closer on the mechanism.

**What the numbers show**

- Deck capacity is 62 car-equivalents. The engine sells up to 62 × 1.06 = 65.72, rounded down, so 65 car-equivalents of bookings.
- The 0.06 factor was set in 2023 from a 7.5% no-show rate. This summer's weekend no-show rate is 1.8%.
- At 1.8% no-shows, a sailing sold to 65 will typically bring about 63.8 people on board. To fit the deck you need at least three of the 65 to not show. The chance of two or fewer no-shows is roughly 85–90% for a full sale, so most full Friday and Saturday sailings will overflow.
- In 2023 the same 65 bookings with 7.5% no-shows gave about 60 actual vehicles, which is why the overbooking "always worked".
- The change to the timetable matters too. Dropping a Friday and a Saturday sailing concentrated the same demand onto fewer sailings, so each remaining weekend sailing sells out and reaches the limit far more often. That fits why all 11 incidents fell on Friday or Saturday.

So the engine is doing what it was configured to do. The configuration is wrong for the current no-show rate. That is Odile's area, and the 2023 figure is the root cause.

**The second problem is the vehicle default**

The booking form defaults to "car", and the deckhands' account of campervans "disguised as cars" is consistent with that. If a campervan (2 car-equivalents) is booked as a car (1), the engine's count is short by one unit per campervan. A few campervans on a full sailing can push the actual load over the deck even when the factor is right. This is a data-entry problem in the booking form, which is IT's area. It is worth fixing before August, because it adds to the overflow regardless of the factor, and it is cheap to fix (default to car, but require the vehicle type to be confirmed).

**Assumptions I made (please check)**

- The engine counts bookings in car-equivalents. If it counts vehicles, the campervan problem is much larger, and the overflow happens earlier.
- The 65-unit limit is applied per sailing and is not already reduced for vehicle type.
- The 1.8% no-show rate applies to all weekend sailings, not just some.

**What to do before the August bank-holiday weekend**

1. Lower the overbooking factor now. At 1.8% no-shows, a factor of about 0.02 gives 63 bookings (62 × 1.02 = 63.24, rounded down), with about 61.9 expected to show, so it sits close to the deck limit and needs watching. A factor of 0 is the safe choice until you have data for August. Odile should set the value, since she owns the forecast.
2. Ask IT to confirm whether the engine counts vehicles or car-equivalents, and to make the vehicle type a required field, with no default to "car".
3. Check the existing bookings for the August weekends, since the lower factor only affects new sales. Bookings already sold above 62 car-equivalents will still overflow, so you may need to contact those customers now.
4. Track the no-show rate each weekend and reset the factor from that data, not from the 2023 figure.

If you want, send me the engine's booking export or the vehicle-type breakdown for the 11 incidents and I can check the counts against the 62-unit limit.
