T7W: Catches all four core holes and ranks release-before-review first. Also covers revocation and notifying people who relied on the reports, insider risk, and Monday cut-off testing. Assumptions are separated cleanly and it names what to check first. Weaknesses: long, with a "smaller points" section plus an "other ways" section; "pause the timer only while the connection is down" restates the current design; it misreads the resit rule as "one more try".
Q6U: Tight and highly specific: caps of 3/5/15, a 10% sample of unflagged passes, a 300-item bank, a resit cool-off, the ID tilt check, and the Monday 07:40 start interacting with pause time. It notes that the vendor holds the exam content. It flags its assumed flag rate. Weakness: "membership numbers are often printed on certificates" and "proctoring itself is reasonable" are asserted without support.
J0U: Covers the main holes, and the viva/hybrid point and the vendor question list are useful. Fewer concrete numbers. It invents a "one hour average" session length. Ranks bank harvesting most serious but fixes release-first without reconciling the two. The scheduling item duplicates the bank item. The "offline-tolerant mode" idea is unexplained.
X6D: Correct overlap arithmetic (min 30, mean 40), plus collusion statistics, a contractual acceptance test and an oral component. However, it states guesses as facts: membership numbers are not secret, flags "need tuning", an assumed 30-50% flag rate, and CPD events. The reconnection "different order position" fix does not stop lookup of a question already seen, and the overlap-forbidding rule is muddled.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,T7W,6,6,6,7,4,7,6,42
J-B,Q6U,6,7,6,6,5,6,5,41
J-B,J0U,5,5,5,6,5,7,5,38
J-B,X6D,6,6,4,5,4,7,3,35
```

```ranking
judge,brief,order
J-B,brief-1,T7W Q6U J0U X6D
```
