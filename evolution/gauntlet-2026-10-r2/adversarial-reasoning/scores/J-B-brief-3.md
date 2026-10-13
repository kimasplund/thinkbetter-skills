Z3O: The broadest coverage. It covers rollout phishing, closing the old email route, cutover duplicates, unverified migrated bank data and callback fatigue, and it ends with a sharp first check (shared-drive write access and a payee-level bank view). There is an internal slip: the closing line calls "items 4 and 5" duplicate-invoice checks and defers them, but item 5 is the payment file, which its own list ranks second. Long, though nearly all of it is substance.
I0C: Tight and correct on the four core routes and the scope of the certification. The "if you can only do three things" line is useful. It misses rollout phishing and bank-change requests that bypass the portal, and its assumptions are thin. Suggesting the supplier's website as a callback source is weak.
F1M: Clear verdict ("don't ship as designed"). Strong on route 1, aggregating limits, hashing account numbers, detection and recall, the out-of-portal email route and rollout phishing. Its residual risk and assumptions say which ranking would change and what to check first. Minor: route 2 says "combine with routes 3 and 4" when route 4 is not needed for that path. Long.
S8W: Concise and mostly sound on the core routes, and it does cover out-of-portal requests. It calls the CSV handoff "the weakest link" while ranking it fourth, under a "highest risk" item 1, and its priority list keeps it fourth. It misses rollout phishing, and its assumptions amount to a single line.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,Z3O,7,6,5,7,4,7,6,42
J-B,I0C,5,6,5,6,6,7,5,40
J-B,F1M,7,6,6,7,4,7,6,43
J-B,S8W,5,5,4,5,6,7,4,36
```

```ranking
judge,brief,order
J-B,brief-3,F1M Z3O I0C S8W
```
