**Short answer: the most likely cause is the automatic cold crash on FV3 and FV4. Don't dump L22 yet, and it isn't Pia.**

**What the data shows**

Every buttery batch (2, 4, 7, 8, 11) was fermented in FV3 or FV4, and every one was crashed at 9 to 10 days. Every clean batch except one was either in FV1/FV2 or ran 13 days or more. Here are the batches grouped by tank and crash timing:

| Group | Batches | Result |
|---|---|---|
| FV3/FV4, controller crashed automatically (9-10 days) | 2, 4, 7, 8, 11 | 5 of 5 buttery |
| FV1/FV2, crashed by hand (13-15 days) | 1, 3, 5, 6, 10, 12 | 6 of 6 clean |
| FV3 with controller in manual mode (15 days) | 9 | clean |

The mechanism fits. Diacetyl is a normal by-product of fermentation, and yeast clean it up afterward, but only while the beer is still warm and the yeast are active. The new density meters on FV3 and FV4 start the cold crash as soon as gravity reaches target. That is probably before the yeast have finished reabsorbing the diacetyl. Your hand-crashed tanks get a few extra days warm because the crash waits for someone to take a hydrometer reading, and that gap is effectively a diacetyl rest.

Batch 9 is the best test you have. It ran in FV3, but the controller was in manual mode, so a person decided when to crash. It ran 15 days and came out clean. Same tank and same hardware, with only the automatic crash removed.

**Why the other suspects don't fit**

- **L22 yeast.** Batch 2 was buttery on the old lot, L19. Five clean batches (3, 5, 6, 9, 10, 12) were made with L22. A bad lot would not skip FV1 and FV2 every time.
- **Pia.** She brewed 2, 4 and 8 (buttery) and 6 and 10 (clean). Marta's batch 7 and Arlo's batch 11 were also buttery. Pia just ended up on FV3/FV4 more often. Her clean batches were the ones on FV1/FV2 with longer schedules. Nothing in the data points at technique, and I'd tell the team that plainly.
- **Mill gap.** It changed for every batch since July 20, including all the clean ones.
- **Peracetic CIP (Aug 10).** Clean and buttery batches both came after it, and it doesn't line up with the tank pattern. It's worth a glance but is unlikely.
- **Temperature or the chiller.** Logs stayed within 0.5°C of setpoint.
- **Bacterial contamination.** Plates from batches 7 and 8 showed no growth. Plating can miss some lager spoilers, but the clean pattern by tank and timing makes this the least likely cause.

**Caveats**

Tank and crash timing are tangled together, because FV3/FV4 always crash early. Batch 9 is the only case that separates them, and one batch is thin evidence. That's why I'd confirm before changing anything permanent.

**What to check before spending money (all cheap)**

1. Pull the FV3/FV4 controller logs and compare the time the crash began with the gravity curve. If the crash starts the moment gravity hits target, with no hold, that is the cause.
2. Run a forced diacetyl test on the next FV3 or FV4 batch. Take a sample before the auto crash and warm it to roughly 60°C for 15 to 30 minutes. If it's much buttery than the cold sample, the precursor is still present. Repeat it after a few more days warm.
3. Change the controller program. Add a diacetyl rest of 2 to 3 days at about 15 to 18°C after target gravity, then crash. Alternatively, put the controllers in a mode where a person approves the crash.
4. Brew one L22 batch in FV3 or FV4 with the rest added. If it comes out clean, you have your answer, and the fix cost nothing.
5. Ask the vendor how the firmware update changed the crash trigger. Also check whether the density meters read gravity accurately. A meter that reads low would trigger the crash too early.

Dumping L22 and switching labs would cost about $1,800 and, on this evidence, probably wouldn't fix anything. Try the rest first.
