Notes

- Q2G: Correct diagnosis, tight and actionable. It uses the inpatient/ED-on-same-lot argument and mentions tourniquet and fist clenching. It misreads Harbour's 5% share of flags as Harbour's rate and never notes that Millbrook has no Tomas.
- O9T: Sound overall, with a good clinical safety step and stated assumptions. It also misreads Harbour's 5% as a rate. Its explanation for why August 1 had no effect ("partly masked") is weaker than the 90-minute-loop argument, and it misses the Millbrook-has-no-Tomas point.
- M6M: Strong and practical. It covers Millbrook versus Tomas, the timing, the clinician advisory before Friday, the look-back, the plasma-versus-serum comparison, and checking low-potassium results. Item 3 (rerunning flagged samples on Analyzer A) has muddled logic.
- S2R: Good containment, and it makes the lot decision explicitly conditional on the time-split data, which is useful. It omits the inpatient/ED-unchanged argument and Millbrook's lack of Tomas, and the clinician safety messaging is thin.
- W3T: Concise. It gives a calibrated 75%, flags the other clinics as unknown, and compares Tomas's draws. Its claim that under a 90-minute loop "almost no specimen waited 30 minutes" is wrong, and it omits the inpatient/ED point.
- W2J: Thorough evidence table, with good EDTA-carryover and fridge-temperature fallbacks and a clear "what would change it". It invents "roughly 35% of volume" for the other two clinics, and it runs long.
- D1K: Most complete and best calibrated. Its fits/doesn't-fit table covers all the discriminators, including the lot on the same inpatient analyzer, Millbrook, and the time-of-day pattern. It gives an ~80% confidence, names the loose ends, and has scripts for the director and for Ridgeway. Heavy on length and headers.
- E4I: Strong. It compares Tomas within the same draw-time bands (a good confound control), treats the ED visits as incidents, adds a courier-contract maximum transit time, and flags the other clinics. "Harbour is normal" goes beyond what the share data shows.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,Q2G,5,6,4,5,6,7,4,37
J-A,O9T,5,5,4,5,5,7,4,35
J-A,M6M,6,6,5,6,6,7,5,41
J-A,S2R,5,5,5,6,6,7,5,39
J-A,W3T,5,5,4,6,6,7,5,38
J-A,W2J,6,6,5,6,4,7,4,38
J-A,D1K,6,6,6,7,4,7,6,42
J-A,E4I,6,6,5,6,5,7,5,40
```

```ranking
judge,brief,order
J-A,brief-1,D1K M6M E4I W2J S2R W3T Q2G O9T
```
