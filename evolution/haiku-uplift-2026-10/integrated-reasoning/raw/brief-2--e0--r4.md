Short answer: neither IT nor Odile is fully right, and the most likely cause is the overbooking setting, not a code fault. I can't see the booking engine, so treat this as a strong hypothesis to confirm, not a verified bug.

**The arithmetic**

- Deck: 62 car-equivalents. Factor 0.06 means the engine sells up to floor(62 × 1.06) = 65 units.
- The factor was set from a 7.5% no-show rate. To fill 62 expected arrivals at 7.5% no-show, you would sell about 62 / 0.925 = 67, which is a factor of about 0.08. So 0.06 was conservative in winter, which is why it "always worked" then.
- This summer's weekend no-show rate is 1.8%. Selling 65 at 1.8% gives about 63.8 expected arrivals, which is above 62. Break-even for 1.8% is a factor of about 0.018.

So the same formula that was safe in winter oversells every peak sailing in summer. The overflow is worst on Friday and Saturday because the dropped sailings concentrated demand on those days.

**Caveats**

- A simple per-booking model suggests overflow would be more frequent than 11 times this season. The real pattern is less severe, so the no-show rate probably isn't uniform across bookings, or the engine's counting differs from my model. This is one reason to check the engine itself.
- Campervans and car-with-trailer bookings take 2 units, and vans take 1.5. If the engine counts bookings rather than units against the 62 cap, the sold total is understated and the overbooking is effectively larger than 0.06. Campervans booked as "car" by default would make this worse. That's a real possibility, and it would be a bug in the sense that the cap logic doesn't match the units you sell.

**Who is right**

- Odile is right that the factor is the lever, and it was set for the wrong season.
- The IT contractor may be right that the engine computes what it was configured to do. Ask them to confirm whether the cap is applied in car-equivalent units or in bookings.
- Both are partly right, and the fix is probably a config change plus a units check.

**Before the August bank-holiday weekend**

1. Pull the 11 incident sailings. For each, compare sold units, vehicles by type, and actual boarded units. This tells you whether the problem is the factor, the counting, or both.
2. Ask IT to confirm the cap unit (units or bookings) and whether vehicle type can be set to campervan or trailer at booking. Changing the default to force a choice would be a quick fix for the form.
3. Set the factor for summer from current no-show data. At 1.8%, a factor around 0.01 or lower gives a margin. Decide the number, not the engine. This is a business call for you and Odile.
4. Keep a manual check for the three bank-holiday sailings: count units against 62 before boarding, and have a plan for anyone left behind.

I'd avoid a blanket fix until step 1 is done, because it tells you whether the 0.06 setting or the counting is the main cause.
