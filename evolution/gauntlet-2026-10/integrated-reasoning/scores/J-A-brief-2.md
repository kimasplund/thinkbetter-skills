Notes

- L8W: Correct arithmetic, including break-even 0.018. Ties the campervans and the timetable cut to the same cause. Flags the units-versus-vehicles check as the one place a real bug could hide, and suggests per-sailing no-show rates. Clear fix ordering and a calibrated confidence. The most usable reply.
- C8X: Sound arithmetic, with a 4.6% break-even no-show rate. Adds loading efficiency with mixed vehicle lengths, and flags whether the 1.8% is measured in units or vehicles. Says Odile is "wrong that it has always worked", which is slightly off. A few speculative claims, and a bit long.
- D3S: Direct verdict and clear tests. The "IT right, Odile wrong" framing is actionable. The reason given for winter cancellations is invented. Its only engine-fault test is "sold units exceed 65", which would miss a unit-counting bug. Includes a cost framing and a useful assumption about all-days versus weekend rates.
- J2J: Good point that last summer's incidents show the factor was already too high. Includes a units-versus-vehicles check. Its falsification logic is a little muddled: selling fewer than 65 does not by itself mean the engine is miscounting, because mis-declared campervans could explain that too. Well calibrated overall.
- Y5O: Concise and well framed for the meeting. It makes an arithmetic error: at 0.02 the engine sells 63, and about 61.9 turn up, so it would not overflow on average. Thinner on the subtle points.
- P6F: Good extra points: bank-holiday no-shows will run lower than average, and mis-declared vehicles corrupt the no-show data. The claim that "roughly half of fully sold sailings would overflow even before random variation" is wrong, because the mean of 63.8 is above 62. The compensation section goes beyond what was asked.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,L8W,6,6,6,6,6,7,6,43
J-A,C8X,6,6,5,5,5,7,5,39
J-A,D3S,6,6,5,6,6,7,5,41
J-A,J2J,6,6,5,6,5,7,6,41
J-A,Y5O,5,5,4,5,6,7,5,37
J-A,P6F,6,6,4,6,5,7,5,39
```

```ranking
judge,brief,order
J-A,brief-2,L8W D3S J2J C8X P6F Y5O
```
