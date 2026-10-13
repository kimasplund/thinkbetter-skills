**Most likely cause: the automatic cold crash on FV3 and FV4. It is not the yeast, and it is not Pia.**

**The pattern in your table**
- All 5 buttery batches (2, 4, 7, 8, 11) were in FV3 or FV4, the two tanks with the inline density meters. They crashed after 9 to 10 days.
- Every batch on FV1 or FV2, where someone crashes by hand after a hydrometer reading, was clean. Those ran 13 to 15 days.
- The one FV3 batch that was clean is batch 9. Its controller was in manual mode for most of the run, and it ran 15 days. This is your natural experiment. With the auto-crash taken out, the same tank, same brewer and same yeast gave clean beer.

So the split is by crash trigger and timing, not by anything else. The mechanism fits. The controller sees gravity hit target and starts the cold crash straight away. That cuts off the diacetyl rest and the period when yeast reabsorbs diacetyl. A human with a hydrometer naturally crashes later, which gives the yeast extra days. Diacetyl is a classic result of crashing before the yeast has finished cleaning up.

**Why the other suspects don't fit**
- **Yeast lot L22:** Batch 2 was buttery on the old lot L19. L22 gave clean beer in batches 3, 5, 6, 9, 10 and 12. Dumping L22 would not have prevented any of this.
- **Pia:** She brewed batches 6 and 10, and both were clean. Arlo (batch 11) and Marta (batch 7) also had buttery batches. She was simply assigned FV3 and FV4 more often (batches 2, 4 and 8). Tank is the real driver, and brewer is a coincidental overlap.
- **New peracetic CIP (August 10):** Batch 2 was buttery, and by the table's order it was brewed before the switch, assuming batches are in date order. Clean batches after it also rule it out as the cause.
- **Mill gap:** It applies to every batch since July 20, clean and buttery alike, so it can't explain the difference.
- **Temperature and the hot August:** All tanks stayed within 0.5°C of setpoint.
- **Infection:** Plates from batches 7 and 8 grew nothing. Bacterial diacetyl production is also unlikely to line up this neatly with tank.

**Assumptions:** The table is in chronological order. The 9 to 10 day batches were crashed at the point gravity hit target, with no hold. Nothing else differs between the tank pairs.

**What to check before spending $1,800**
1. Pull the FV3 and FV4 controller logs. Check when the crash began relative to when gravity hit target. Also check whether there is any hold or diacetyl rest step in the program, since the firmware update may have reset it.
2. Run a forced diacetyl test. Warm a sample from a buttery batch, or from a current FV3/FV4 batch, to about 60°C for 15 to 30 minutes, then taste it against an unheated control. If the heated sample is much more buttery, the beer is still carrying diacetyl precursor and was crashed too early.
3. Fix the program on FV3 and FV4. Add a diacetyl rest of 2 to 3 days at fermentation temperature, or a slight rise, after the gravity target and before the crash. Alternatively, put those tanks on manual crash for now. Make the crash conditional on a sensory or forced-diacetyl check passing.
4. Run the next 2 or 3 batches in FV3 and FV4 with the rest in place. Keep FV1 and FV2 as controls. If the butter flavor goes away, the cause is confirmed.
5. Keep L22 for now. If you want to be thorough, run one L22 batch in a manually crashed tank. Batches 3, 5, 6, 9, 10 and 12 already show it can make clean beer.

Please tell Pia the data does not point at her. The tank assignment pattern does.
