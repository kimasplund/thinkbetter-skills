# J-B scores, brief-2

Notes:

- B7R: The arithmetic is correct, and it models switcher churn as a sensitivity rather than the base case. It leads its list of problems with the 6% churn point while admitting that point barely matters for the one-year question, so the ranking is off. Assumptions are flagged well. The £1,000 annual price option is concrete and correct in direction.
- D4F: It uses 6% in-year churn on prepaid switchers as its base case. That is a dubious step for a 12-month ARR snapshot and leads to "even Anya's own assumptions only get you to roughly break-even" (96%). The control-group question and the acquisition risk are good catches. The renewal-timing point is confused, because monthly clinics renew within a month. The reply is long.
- I0A: Correct break-even at 90%, with the £1,080 per leaver framing. It notes that prepaid switchers cannot churn within the year. Its next step is the cheapest real one before Tuesday: sample 30 to 50 existing clinics or have account managers rate them, and pull the acceptance rate when both plans are offered. The length is tight.
- O4F: The most thorough on insight. It points out that Anya expects 5% loss when 25% leave in a normal year, that the upfront £900 is a cash-flow shock, and that the longer horizon makes an honest counter-case. One row is off by about £800 (-229,600 vs -228,800). It is otherwise sound.
- Q2U: Clean break-even derivation and good pilot ideas, including tracking first-renewal churn of switchers. "These keep the churn benefit" slightly overclaims a benefit that it shows earlier is unproven.
- G4Z: It correctly ranks the missing price cut first and correctly calls the "never committed" argument circular. It states "the test had no control group" and "forced clinics are the more price-sensitive ones" as facts, though the brief supports neither.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,B7R,6,6,6,6,5,7,6,42
J-B,D4F,6,6,4,6,4,7,6,39
J-B,I0A,6,6,6,7,6,7,6,44
J-B,O4F,7,6,6,6,5,7,6,43
J-B,Q2U,6,6,6,6,6,7,6,43
J-B,G4Z,6,6,5,6,6,7,5,41
```

```ranking
judge,brief,order
J-B,brief-2,I0A O4F Q2U B7R G4Z D4F
```
