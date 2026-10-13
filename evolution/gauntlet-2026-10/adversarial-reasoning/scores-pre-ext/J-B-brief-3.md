L7F: Broad and mostly accurate. The arithmetic is right ($316 per head, 240 people at the cap), and it makes the sharp point that a $5 gift counts toward the five-donor trigger. It also covers payment diversion, departing employees and possibly uncapped volunteer charities. Weaknesses: it is long (15 controls plus extra sections), it refers to an "attack 1" that is never numbered, it claims "anyone can register a tiny charity" without support, and it offers no cheap test.
B5F: Tight, and it gives a good cheap test (a red-team hour). The point about bank transfers to an account carrying the charity's name as a reference is specific. Weaknesses: one sentence is garbled ("20 hours at 25 hours"). The $9.5M volunteer exposure treats the ambiguous $2,500 cap as per employee without flagging that. It misses payment diversion and segregation of duties.
M3L: The strongest calibration. It flags that the brief doesn't say whether volunteer grants count against the cap or the budget, gives a residual-risk section with plainly stated confidence, and asks what finance means by "abuse". Its non-obvious points are good: the 3:1 trigger leaks who gave to what, and gifts can look like pay-to-play with clients. The control table maps each control to an attack. Minor flaws: "Nothing checks the date" partly contradicts the OCR date check in the brief, and $1,999 is called a $1,000 gift.
G2T: Thorough, with correct arithmetic ($1,667 x 3, $8,300 -> $25,000), and it flags that the volunteer cap is ambiguous. Ranking budget exhaustion first is defensible. Weaknesses: "a handful of employees could steer six figures" overstates what the $5k cap allows, it is long, and its prioritisation repeats itself.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,L7F,6,6,5,5,4,6,5,37
J-B,B5F,5,5,4,6,6,7,4,37
J-B,M3L,6,6,6,6,5,7,6,42
J-B,G2T,6,6,5,5,4,7,5,38
```

```ranking
judge,brief,order
J-B,brief-3,M3L G2T L7F B5F
```
