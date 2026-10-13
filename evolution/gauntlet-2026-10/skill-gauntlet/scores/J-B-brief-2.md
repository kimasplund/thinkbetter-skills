Notes:
- Q2E: Gets the 5/6 = 83% fresh-lease failure, the mid-test change to the baseline, and the unmet two-attorney rule. Adds false-alarm testing and a correct one-sided coin-flip figure (about 1 in 9.5). Contradicts the brief by implying Halima gave only a preference and no usefulness scores, when the brief says she scored all 32. It also asserts "labeled" without support.
- M7W: Tight and correct on the core numbers, with a useful "documented exception" fallback and an assumptions section. It states outright that Halima gave "not a usefulness score on each write-up", which the brief contradicts. No false-alarm point, and it suggests Priya look at the shared miss without warning about tuning v6 to the test set.
- L0W: The most complete reply. It covers false alarms, warns against tuning v6 to the shared miss, says to re-register the rule, and notes that six leases can't tell 83% from 90%. The two-sided "about 1 in 5" figure is correct. It makes the same usefulness-score misreading and the same "labelled" assertion as Q2E, and it is a little long.
- I7F: Correct on the core points. It is the only reply that doesn't misread Halima's scoring, and it flags its inferences and assumptions. The shadow-run fallback is practical. It misses the false-alarm gap, and "seeded problems are easier" is an unflagged claim.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,Q2E,6,6,6,6,5,7,4,40
J-B,M7W,5,5,5,6,6,7,4,38
J-B,L0W,6,6,6,6,5,7,4,40
J-B,I7F,5,5,5,6,5,7,6,39
```

```ranking
judge,brief,order
J-B,brief-2,L0W Q2E I7F M7W
```
