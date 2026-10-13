Notes:
- I7F: Correctly finds the 83% fresh-set failure, the missing second attorney, the mid-test change to v5, the non-blind review and the holdover miss. Flags its inferences clearly and offers running both versions in parallel as a fallback. Misses that a preference is not a usefulness score, and misses the untested false-alarm rate.
- L0W: The most complete. Adds the false-alarm gap from seeding every lease, the difference between a preference and a usefulness score, a correct coin-flip check on 11-5, and a warning not to tune v6 to the test clause. Slightly overstates the bias ("biased in a way you can't measure") and gives a timeline guess.
- M7W: Clean and actionable. Catches the preference-versus-usefulness gap and gives an honest path to a documented exception, with assumptions stated. Doesn't consider false alarms, and does less with the small-sample uncertainty.
- Q2E: Covers everything that matters, including false alarms, preference versus score, chance on both the 15-13 gap and the 11-5 split, and naming a replacement attorney before the retest starts rather than after. The retest plan is the most precise and is tied to the facts. A little long.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,I7F,5,6,5,6,6,7,6,41
J-A,L0W,7,6,6,6,5,7,5,42
J-A,M7W,5,6,5,6,6,7,6,41
J-A,Q2E,7,7,6,6,5,7,6,44
```

```ranking
judge,brief,order
J-A,brief-2,Q2E L0W M7W I7F
```
