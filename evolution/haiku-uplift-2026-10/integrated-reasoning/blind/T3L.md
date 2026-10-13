Short answer: neither is quite right. The engine's arithmetic is doing what it was set up to do. The problem is the input it was given, and that input was calibrated for a different season. There is also a second, related fault that IT and Odile both need to look at.

**1. The overbooking factor is out of date for summer weekends**

The engine sells up to 62 × (1 + 0.06) = 65.72, rounded down to 65 car-equivalents on each sailing. That only works if about 7.5% of booked vehicles fail to show. That figure came from November to February, and it is why "it has always worked" was true until this summer.

This summer's weekend no-show rate is 1.8%. On a full Friday or Saturday sailing, the expected turn-up is roughly 65 × 0.982 ≈ 63.8 car-equivalents against 62 spaces. That is about 1.8 vehicles over on average, and more on a busy day. That is what you are seeing. The fact that all 11 incidents fell on Friday or Saturday fits this, because weekday sailings are not full enough to overflow.

Your timetable change adds to this. Dropping a Friday and a Saturday sailing pushed weekend demand onto fewer sailings, so more of them now sell out. That makes an overflow more likely on each one.

**2. The vehicle-type default is probably making it worse**

Your deck capacity is measured in car-equivalents: a van is 1.5 and a campervan or car with trailer is 2. If the booking form defaults to "car" and campervans are not changed, the engine counts them as 1 when they actually take 2. The sold total then understates the real deck load, and the 6% margin is eaten by the gap. This is the same overflow mechanism, but it can hit on any sailing, not only in the high-no-show season. The deckhands' complaint and the overbooking problem are linked, so I would not leave it "for later" if the fix is before the bank holiday.

I am assuming the engine sells in car-equivalents and not in raw vehicle counts. If it sells in raw vehicles, the vehicle-type default matters even more.

**Who is right?**

- IT is right that the engine's formula works as written.
- Odile is right that the overbooking was set correctly for the conditions it was built on, and that the bug is not in the code.
- The actual bug is a stale parameter, plus a vehicle-type default that undercounts the deck. Neither side has spotted both.

**Before the August bank holiday**

1. Stop using the 2023 factor for weekend sailings. Set the weekend factor to 0 or 0.01 for now. At 0.01 the cap is 62 (62 × 1.01 = 62.62, rounded down), so it sells to capacity and no more. This is the safest choice while the no-show rate is uncertain. Treat 1.8% as a figure from a few summer weekends, not a settled rate.
2. Make the vehicle type a required field, and set the default to blank or to "check", not "car". Count campervans and cars with trailers at 2 in the sold total. Ask IT to confirm the engine does this in car-equivalents.
3. Keep the weekday factor separate. Your no-show rate varies by season and probably by day, so the factor should be set per season and per day type, not as one number.
4. After the bank holiday, check the no-show rate per sailing and reset the factor from data rather than from a single season's average.

If you can tell me how the engine stores bookings (vehicle counts or car-equivalents) and whether the no-show rate was measured per sailing or per booking, I can narrow this down further.
