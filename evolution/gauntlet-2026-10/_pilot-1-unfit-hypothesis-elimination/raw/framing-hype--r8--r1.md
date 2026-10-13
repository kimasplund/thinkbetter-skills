Don't dump L22 yet. The data points to the new inline density meters on FV3 and FV4. They start the cold crash too early, before the yeast has finished cleaning up diacetyl.

**What the table shows**

| Group | Batches | Result |
|---|---|---|
| FV3/FV4 under auto-crash (meters) | 2, 4, 7, 8, 11 | All 5 buttery, 9-10 days pitch to crash |
| FV1/FV2 (crash after a hydrometer reading) | 1, 3, 5, 6, 10, 12 | All 6 clean, 13-15 days |
| FV3 in manual mode (batch 9) | 9 | Clean, 15 days |

The meters went in on July 28. The first buttery batch (2) came after that, and no FV3/FV4 batch run under auto-crash has been clean.

**Why this fits**

- **Mechanism.** Diacetyl is a normal by-product of fermentation, and the yeast reabsorbs it at the end. The controller crashes the tank the moment gravity hits target. That is usually before the yeast has finished its cleanup, and cold stops the cleanup. Hydrometer-timed crashes on FV1 and FV2 happen days later, so the yeast has time to finish.
- **Batch 9 is your natural experiment.** FV3 was in manual mode, so the auto-crash didn't fire, and the batch came out clean after 15 days.

**What the data rules out**

- **L22 yeast.** Batch 2 was buttery on the old lot, L19. Six of the L22 batches (3, 5, 6, 9, 10, 12) were clean. A bad lot wouldn't split by tank.
- **Pia.** Her batches split by tank: buttery on FV3/FV4 (2, 4, 8), clean on FV1/FV2 (6, 10). Marta (batch 7) and Arlo (batch 11) also got buttery batches when they used FV3/FV4, and both made clean ones on FV1/FV2. She was assigned those tanks more often, which is why it looks like her. You can tell her it isn't her.
- **Mill gap, new CIP sanitizer, hot weather.** All of these applied to clean batches too. Tank temperatures stayed within 0.5°C of setpoint.
- **Infection.** Your plates from batches 7 and 8 showed nothing, which fits. Buttery character from bacteria would usually come with other signs as well. I wouldn't call it ruled out entirely, because you only plated two batches.

**Caveat.** Tank and crash timing are almost perfectly tied together in this data. Only batch 9 separates them. So I can't yet tell "early crash" apart from "something else about FV3/FV4", such as the meter hardware itself. That's why the checks below matter.

**Checks before spending anything**

1. **Run a forced diacetyl test.** Take a sample from the next FV3/FV4 batch at the moment of auto-crash, warm it for about 10 minutes, and taste or measure it. If it's high, the yeast hadn't finished.
2. **Change the next FV3/FV4 batch.** Hold it warm for 2-3 extra days after target gravity, then crash. If you can't change the controller setpoint, put it in manual mode and crash by hand. If it comes out clean, that's your answer.
3. **Run the reverse test.** Let one FV1 or FV2 batch crash early, at 9-10 days. If it turns buttery, tank hardware is ruled out.
4. **Fix it permanently.** Add a hold or diacetyl rest to the controller logic, for example a timer or a minimum number of days after target gravity before the crash starts.
5. **Optional, to be safe.** Plate the other buttery batches too (2, 4, 11).

Checks 1 and 2 cost almost nothing and take about one batch cycle. If the extra warm hold fixes it, you've saved the $1,800 and kept the L22 yeast. If it doesn't, you've ruled out the leading cause and the yeast question is worth reopening with better evidence.
