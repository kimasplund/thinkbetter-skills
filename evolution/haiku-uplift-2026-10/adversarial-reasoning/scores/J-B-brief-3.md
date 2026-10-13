Notes:
- L1M: Solid coverage (round-trip, related charities, self-attested hours, splitting, 3:1 ring, budget math correct). Misses benefit-in-return gifts and puts the reputational-eligibility risk last despite the user's headline concern. "Registration is cheap" is unflagged. Clear must-have trio.
- B3Y: Thorough and correct arithmetic ($8,300 by five donors pulls $25,000). Covers benefit-in-return, refunds, lookalikes, steering via 3:1. Long; "don't publish the trigger" is weak security-by-obscurity. Good use of the payment-lag window.
- E3S: Dense and accurate; catches DAFs, private-benefit gifts, refunds/chargebacks, bank-transfer reference trick, sanctions, privacy. One garbled sentence on hours. Cheap red-team test is a good uncertainty reducer.
- M4C: Most complete insight ($5 donations trigger 3:1, DAFs, benefit-in-return, someone else's gift, no cap on number of charities, leavers), and a sensible "deprioritize" counter-case. Too long; one unflagged generalisation.
- B1Y: Compact and sound, honest residual-risk note, but misses controversial-charity eligibility (the user's stated headline worry), refunds/chargebacks and benefit-in-return.
- B1A: Reasonable list, flags volunteer-cap ambiguity, but the refund attack says "the employee keeps the match", which is wrong (match goes to the charity). Reputational risk ranked last; top-three picks are oddly weighted.
- T9M: Strong: benefit-in-return, controversial causes organising 3:1, pay-to-play with clients/suppliers, privacy leak via trigger. Minor slip ("3x their gifts each month" ignores annual cap). Good unknowns and residual-risk statement; table adds bulk.
- Y3Y: Report scaffolding (Target, Critical findings, Confidence: 70%, refers to "the user"). Good $1-donor point, but "budget is not capped" overstates, volunteer-cap reading is inconsistent, and the headline risk is ranked medium against the brief's stated priority.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,L1M,5,6,5,6,5,7,5,39
J-B,B3Y,6,6,5,6,4,7,5,39
J-B,E3S,6,6,5,6,5,7,5,40
J-B,M4C,7,6,6,6,3,7,5,40
J-B,B1Y,4,5,5,5,6,7,5,37
J-B,B1A,4,5,3,5,5,7,5,34
J-B,T9M,6,6,5,6,4,7,6,40
J-B,Y3Y,4,5,4,5,3,3,5,29
```

```ranking
judge,brief,order
J-B,brief-3,E3S M4C T9M B3Y L1M B1Y B1A Y3Y
```
