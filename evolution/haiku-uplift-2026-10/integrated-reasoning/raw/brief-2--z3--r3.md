Short answer: neither side is wrong about everything, but the cause is the overbooking setting, not a code fault. The engine is doing what it was told. The number it was told is out of date.

**Why it happens**

- The engine sells up to 62 × 1.06 = 65.72, rounded down to 65 car-equivalents.
- The 6% was set in 2023 from a 7.5% winter no-show rate. At that rate, 65 sold gives about 60 people turning up, which fits 62 spaces. The setting was correct for the conditions it was built for.
- This summer's weekend no-show rate is 1.8%. On a full 65-unit sale, about 1.2 people no-show, so about 63.8 units turn up for 62 spaces. A full weekend sailing overflows by a couple of spaces almost every time. That matches the 11 sailings, all on Fridays or Saturdays.
- Odile is right that the overbooking "worked": it was right for winter. It stopped being right when no-show behaviour changed, and the number was never re-set. IT is right that the arithmetic is correct. Each of you is right about a different part.

**Two other things to check (both quick)**

1. **Vehicle weighting.** If the engine counts bookings rather than car-equivalents when it applies the 65 cap, a campervan booked as "car" (the form default) takes 2 spaces but counts as 1. That would make overflow worse on exactly the weekends where the deckhands report campervans holding up loading. Pull the manifests for the 11 sailings and compare the booked vehicle type with what was actually loaded. If they differ, that is a second cause, and it is an engine problem.
2. **Fewer sailings on weekends.** The dropped Friday and Saturday sailings push the same demand onto fewer sailings, so full sailings are more common. That is not a bug, but it means the overbooking figure should be set from weekend data.

**What I would do before the August bank-holiday weekend**

- Set the factor for Friday and Saturday sailings to 0.01 as an interim change. That sells 62 spaces, roughly matching the deck, and expected no-shows leave a small margin. It costs a few seats of revenue, which is far cheaper than people left on the pier.
- Recalibrate using June to August weekend no-show data, not the winter figure. Keep weekday sailings on their own setting only if weekday data supports it.
- Ask the IT contractor to confirm in writing that the cap is computed from car-equivalents, and to show the sales log for one of the 11 sailings. That settles the IT question with evidence instead of argument.
- Fix the vehicle-type default on the booking form. You said you'd leave it for later, but if the weighting check above shows a mismatch, it affects the cap and should go in before August.

**Caveats**

I have not seen the engine's code or the sailing records. The 1.8% is a summer average, so some sailings will have more no-shows and some fewer. Treat the figures above as estimates. Three weeks is enough time to change a setting and to revert it if the first weekends look wrong.
