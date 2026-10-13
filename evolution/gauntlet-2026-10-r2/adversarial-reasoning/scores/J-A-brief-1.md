Notes:
- X6D: Broad and specific (reconnect caps, canary items, red-team acceptance test, oral/practical layer, ordered pre-signing sequence). Overlap maths correct. Ranks impersonation above release-before-review in the narrative. Some muddled or invented details (the "different question order position" pause rule, comparison with a "register photo" not in the brief), and padding in sections 6 and F.
- J0U: Covers the main holes, including resit scouting, sampling unflagged sessions and a useful list of questions for Tallyward. Leads with the bank even though its own fix list puts the hold on registration first. Some weaker fixes ("show the same question" on reconnect), and it generalises about AI false positives. Assumptions are stated clearly.
- Q6U: Ranks release-before-review first and explains the liability chain. Concrete fixes throughout (10% unflagged sample, 3x5-minute pause cap with a 15-minute total, a cooling-off period on resits, a physical-card tilt check, a revocation process). Catches the non-obvious point that the vendor holds a copy of the bank, plus edge cases (Monday cut-off, clock changes, outage). Assumptions separated precisely.
- T7W: Very decision-useful: says don't sign, orders fixes by cost type, proposes a 100-session pilot to size review, states the trade-off of keeping the weekend window, and says which assumptions would or would not change the top two items. Longest reply, with some repetition. It misreads the resit rule as "one more try".

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,X6D,6,6,5,6,4,7,5,39
J-A,J0U,5,5,5,6,5,7,6,39
J-A,Q6U,7,7,6,6,5,7,7,45
J-A,T7W,6,6,6,7,4,7,6,42
```

```ranking
judge,brief,order
J-A,brief-1,Q6U T7W X6D J0U
```
