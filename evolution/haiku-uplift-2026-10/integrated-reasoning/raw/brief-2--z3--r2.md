**Short answer:** the bug is the overbooking setting, not the code. The engine is doing what it was told, but the setting was calibrated for a no-show rate that no longer applies.

**What's happening**

- Capacity is 62 car-equivalents. With a factor of 0.06, the engine sells up to floor(62 × 1.06) = 65.
- The 0.06 factor came from a 7.5% no-show rate. At that rate, a sailing sold to 65 expects about 4.9 no-shows, so about 60 people turn up, which fits on the deck.
- This summer's weekend no-show rate is 1.8%. A sailing sold to 65 expects about 1.2 no-shows, so about 64 turn up. The deck overflows whenever fewer than three people fail to show.
- That matches the 11 incidents: all on Friday and Saturday sailings, where demand is highest and the cap gets reached.

**Who's right**

- Odile is right that overbooking is the cause. It did work, at a 7.5% no-show rate.
- IT is right that the engine works in the narrow sense that it multiplies the numbers correctly. The fault is an out-of-date input, not a code bug.
- I haven't seen the engine or its configuration, so this comes from the numbers you gave. Check the factor in the config first.

**A second problem that adds to it**

If the engine counts each booking as one unit, a campervan booked as "car" uses 1 unit in the sale but 2 on the deck. That's the form default you mentioned. It doesn't cause the overbooking, but it adds load the sale never counted, on exactly the weekends when loading is busiest. You said you'd deal with it later. I'd still fix it before August, because it affects the same number and the bank-holiday weekend is the worst time to find it.

**Before the August bank-holiday weekend**

1. Lower the factor now. At 1.8%, a factor of 0.016 or less sells 62, which means no overbooking. That's the safe setting until you have a fresh measurement. (62 × 1.016 = 62.99, which rounds down to 62.)
2. Base the factor on no-show rates measured for summer Fridays and Saturdays, not November to February. Re-check it monthly.
3. Count sold units in car-equivalents (van 1.5, campervan or car with trailer 2), so the sale and the deck use the same measure.
4. Look at the timetable change. Dropping a Friday and a Saturday sailing may have pushed demand onto the sailings that remain. I can't confirm that without the booking data, so treat it as a question to check, not a cause.

**Assumptions**

- The engine multiplies capacity by (1 + factor), rounds down, and counts a sold unit as 1 unless the vehicle type says otherwise.
- The 1.8% rate and the 11 incidents come from your message. I had no access to the booking data.
