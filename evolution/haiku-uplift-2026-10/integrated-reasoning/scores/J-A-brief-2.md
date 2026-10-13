# J-A scores, brief-2

Notes:
- O2T: Gets the stale factor, the timetable concentration and the misdeclared campervans as one mechanism. Factor 0 for Fri/Sat, a data check, and a reset of the IT/Odile dispute. A little long.
- P0L: Says Odile is "right that the factor is the lever", but she blamed IT. Ties campervans only to a booking-count bug. Its claim that overflow "would be more frequent than 11" is unsupported. Holds off the fix until data is pulled.
- G0S: Core diagnosis and interim factor are correct. Wrongly calls a vehicle-type mismatch "an engine problem", and links misdeclaration only to bookings-versus-units counting.
- J0G: Thorough and correct on all three causes, with ownership-gap framing and good assumptions. Overlong. Wrongly credits winter calibration for last summer's three overflows.
- U2Q: Strong diagnosis that ties in the campervans, with sensible bank-holiday caution. "Roughly half of full sailings overflow" understates the risk. The compensation section is extra.
- L5L: The only reply to flag that August bookings already sold above 62 will not be fixed by changing the factor. Very actionable. Says Odile is "closer on the cause", which misreads her position.
- I8J: Careful probability estimates, clearly flagged. A clean test to settle the IT/Odile question. Misattributes "factor is the cause" to Odile.
- D9R: Clean and well ordered: factor 0 this week, an engine check, incident data, a form fix and ownership. Sound throughout.
- G5D: Good core diagnosis. Says "0.01 sells 63" (it sells 62). Misreads Odile. Useful extras: a waitlist and adding a sailing back.
- M3V: Correct, with a 5-minute falsification check, factor 0 including the holiday Monday, and the campervans tied in. States one seasonal generalisation as fact.
- X9C: Includes a "what would show I'm wrong" test and separates the factor fix from the vehicle-mix fix. Garbles Odile's position slightly.
- K4K: Diagnosis is right, but it says Odile thinks the bug is "not in the code", which is the opposite of her view. No step to verify against the 11 incidents.
- B2I: Correct and compact. The afternoon confirmation plan names which check could put the fault back on IT. Adds a bump/compensation policy. Strong.
- U2U: Best overall. Clear verdict, a booking test to settle IT's side, an explicit "what would change my mind", campervans tied in, a concrete form fix, and how the factor fix and the form fix divide the work.
- A3P: Thin. Under-weights the timetable change and misreads Odile. Treats campervans only as a unit-counting question.
- M6C: The rounding point is useful, but it gives no concrete factor for August and says "confirm before you change anything". Calls the vehicle gap both separate and tied. Misreads Odile.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,O2T,7,6,6,6,5,7,6,43
J-A,P0L,4,5,4,4,6,7,5,35
J-A,G0S,5,6,4,6,6,7,5,39
J-A,J0G,7,6,5,6,4,7,6,41
J-A,U2Q,7,6,5,6,5,7,5,41
J-A,L5L,6,6,5,6,6,7,5,41
J-A,I8J,6,6,5,6,6,7,6,42
J-A,D9R,6,6,6,6,6,7,6,43
J-A,G5D,6,6,5,5,6,7,5,40
J-A,M3V,7,6,6,7,5,7,6,44
J-A,X9C,7,6,5,7,5,7,6,43
J-A,K4K,6,5,4,5,6,7,5,38
J-A,B2I,7,6,6,6,6,7,6,44
J-A,U2U,7,7,6,7,5,7,6,45
J-A,A3P,4,5,4,5,6,7,5,36
J-A,M6C,5,4,4,4,5,7,5,34
```

```ranking
judge,brief,order
J-A,brief-2,U2U M3V B2I O2T X9C D9R I8J J0G L5L U2Q G5D G0S K4K A3P P0L M6C
```
