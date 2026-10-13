Notes:
- Z5V: Best-designed checks. The forced test is taken at the moment of crash, with an FV1/FV2 comparison, and it proposes a discriminating test (an early hand crash in FV1/FV2). It also says what would change its mind and admits the sanitizer dates are unknown. The CIP row is muddled, and the explicit "about 80%" is a small trace of machinery.
- X7W: Raises a useful non-obvious point: a density meter that reads low would trigger the crash early, so ask the vendor. But it says "five clean batches" and lists six, its "every clean batch except one" phrasing is wrong, and it assumes the CIP dates without saying so. It has no "what would change my mind".
- R1W: Tight and actionable. It lists its assumptions, including chronological order, and keeps FV1/FV2 as controls over 2-3 trial batches. It overreaches with "same brewer" about batch 9 and states some claims with too much certainty.
- P0Y: Sound, with a clear caveat on confounding and a sensible fallback to testing the yeast. Its first check runs the forced test on already-buttery finished beer, which is the weaker choice. It suggests a risky deliberate auto-crash control, and one step about the dates is filler.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,Z5V,6,6,6,7,5,5,6,41
J-A,X7W,6,6,4,5,5,7,4,37
J-A,R1W,5,6,5,5,6,7,6,40
J-A,P0Y,5,5,6,6,5,7,6,40
```

```ranking
judge,brief,order
J-A,brief-1,Z5V R1W P0Y X7W
```
