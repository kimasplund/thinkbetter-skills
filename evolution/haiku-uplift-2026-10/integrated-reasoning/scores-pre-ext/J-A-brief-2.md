Notes:
- G5D: Correct arithmetic. Practical extras: waitlist and restoring a sailing. Muddled on who's right: it calls Odile "closer to the root cause" even though she blames IT. It doesn't use the comparison with last summer.
- I8J: Tightest reasoning. The overflow probability (~85-90%) is right and the stated assumptions are clear. Recommends a factor of 0 on Fri/Sat. Ends with a discriminating data test (factor versus vehicle weights). Very actionable.
- O2T: Thorough. Gives the 4.6% break-even and flags the loading-efficiency caveat, a good non-obvious point. Includes meeting guidance. A bit long, and it states some guesses about traveller behaviour as fact.
- A3P: Clean and correct. The 0.016 threshold is exact. Less depth on confirming the diagnosis, and it hedges the timetable effect more than it needs to.
- U2Q: Gets the overall mechanism. Two errors: it says the factor "only works if about 7.5%" don't show (break-even is 4.6%), and it says Odile holds that the bug is not in the code (she blames IT).
- B2I: Good points: bank-holiday no-shows are likely lower, misdeclaration corrupts the no-show data, and a code-check sentence for IT. But "roughly half overflow even before random variation" is wrong (it's ~88%), and it opens with "neither right" while saying IT is right.
- U2U: Explains why last summer was mild (the same factor, with weekend demand split across more sailings). Suggests a test booking to rule IT in or out, and a bumping policy. States that the engine counts in car-equivalents as if it were known.
- K4K: Strong on what would change its mind, plus a cheap test. Claims weekend no-shows "fell" against last summer without evidence. The "~15% I'm holding back" is a trace of confidence arithmetic.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,G5D,5,5,4,5,5,7,6,37
J-A,I8J,6,6,6,6,6,7,6,43
J-A,O2T,6,6,5,6,4,7,5,39
J-A,A3P,5,5,5,5,6,7,5,38
J-A,U2Q,5,5,3,5,6,7,4,35
J-A,B2I,6,6,3,5,5,7,4,36
J-A,U2U,6,6,5,6,6,7,5,41
J-A,K4K,6,6,5,7,5,5,6,40
```

```ranking
judge,brief,order
J-A,brief-2,I8J U2U K4K O2T A3P G5D B2I U2Q
```
