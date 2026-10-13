L1K: Correct diagnosis, with a clean ordered checklist that starts with the cheapest check. It flags that the pressure drop can't be dated from June vs Sept 15 data. It also suggests modelling Well 7 on and off, which is useful. It misses the 0.3 mg/L secondary-standard point and the fact that complaint manganese sits above plant effluent.
J5O: Solid and correct, but a little thinner. The health line ("low health-wise") is softer than the iron levels justify, though it is caveated. Good fallbacks (a collapsed section, a leak, the Calder tank). Weaker on cheap confirmation beyond the valve check.
F2Q: Most actionable. It covers the valves, SCADA step-change on Sept 4, a hydrant flow test across the repair section, and a morning turbidity/iron cycle. The mass-balance point on Well 7 manganese is sound. It notes that the pressure data is a single day, and it adds the capital-plan framing. Slightly long.
W6Z: Strong. Unlike the others, it explains why complaint manganese sits above plant effluent (scale co-release), flags iron above the 0.3 mg/L secondary guideline, and warns to open the valve slowly to avoid a surge. It also gives a falsifiable prediction (pressure back toward 60 psi). The table is a bit heavy.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,L1K,5,6,5,6,6,7,6,41
J-A,J5O,5,5,5,5,6,7,5,38
J-A,F2Q,6,6,6,6,5,7,6,42
J-A,W6Z,6,6,6,6,5,6,6,41
```

```ranking
judge,brief,order
J-A,brief-2,F2Q W6Z L1K J5O
```
