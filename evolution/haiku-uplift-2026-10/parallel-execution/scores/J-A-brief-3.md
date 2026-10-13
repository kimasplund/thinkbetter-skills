Notes:
- Z9J: Catches transect 7, the tit-wren lump, and that the B/C ratio mixes observers. But it puts an observer term in each per-site model, where observer is identical to period, so it can't be estimated. It keeps the flawed design.
- X4N: Sees correctly that the pooled model separates observer from trend because the sites are crossed. Misses the transect 7 overlap and uses 7/6/5/5 as fact. Doesn't catch the observer bias in the B/C ratio.
- H8P: Covers everything: the crossed design, transect 7, the tit-wren lump (D-only split too short), the observer-biased B fill. Parallelizes the cleaning by site and the fitting by species. Good questions, including asking for observer-overlap data.
- W3O: Thorough, with a usable timeline and hand-back schema. The design is muddled: site analysts still fit per-site models with a "diagnostic" observer effect that can't be identified. Long.
- X2H: Covers everything. Splits by species with a joint model and notes the observer bias in the B/C ratio. Adds the strongest caveat: the observer estimate rests on the A/B vs C/D contrast. Clear hand-back and combination steps.
- I7T: Recommends the joint model correctly, but misses transect 7 and the observer bias in the B fill. Also suggests per-site observer terms, which can't be estimated.
- O6U: Covers everything, plus the short-series point. Splits by species and adds a sanity check on the observer-effect sign. The "3 vs 4 years asymmetry" argument is a little loose.
- C5C: Catches transect 7 and the tit-wren issue. Treats observer as a per-site covariate, which can't be estimated, and calls it an A-vs-C problem. Asks to confirm the observer change year, which the brief already gives. Vague "site offset".

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,Z9J,5,5,3,4,6,7,5,35
J-A,X4N,4,5,5,5,6,7,5,37
J-A,H8P,7,7,6,7,5,7,6,45
J-A,W3O,6,7,5,6,4,7,6,41
J-A,X2H,7,7,7,7,5,7,7,47
J-A,I7T,5,5,4,5,6,7,5,37
J-A,O6U,7,7,6,7,5,7,6,45
J-A,C5C,4,5,3,4,6,7,4,33
```

```ranking
judge,brief,order
J-A,brief-3,X2H H8P O6U W3O X4N I7T Z9J C5C
```
