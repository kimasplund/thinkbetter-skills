Notes:
- D1M: Gets the grid timing and capacity right, and the noise rule as the binding constraint. Battery sizing is correct: 4 packs, and 2 is not enough. But it picks 4 hybrids (£20.4k) for the campsite over relocating 2 diesels plus cable, with no cost comparison. It also calls six hybrids "far more capacity than the peak needs" and misses that the engines alone give 480 kW against a 520 kW peak. The Gantry checklist is actionable.
- V5G: The content is strong: the 480 kW engine shortfall, the 32% breakeven, re-sited diesels with a medical battery and changeover, the council measurement question, and heads of terms with the landowner. The voltage-drop arithmetic checks out. But it is buried under adoption rules, scoring tables, "not blind" disclaimers and invented percentage odds with made-up reference classes. Far too long to act on quickly.
- X6F: Same heavy scaffolding. The recommendation depends on an untested cut of the overnight load to about 20 kW and an assumed arena load of 460 kW. It misses that the hybrid engines fall short of peak, and it scores six hybrids high on noise even though its own night arithmetic shows they fail. The probabilities and reference classes are invented.
- X2V: Concise and correct on the grid, the hybrid cost, and the hybrid engine capacity shortfall against peak. It lays out the overnight options clearly with costs and picks the cheapest compliant one (relocate plus a medical UPS), with a hybrid trial and council confirmation. Slightly vague on cable cost and run length.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,D1M,5,5,4,5,6,7,5,37
J-A,V5G,6,6,5,7,2,1,4,31
J-A,X6F,5,6,4,6,2,1,3,27
J-A,X2V,6,5,5,5,6,7,5,39
```

```ranking
judge,brief,order
J-A,brief-2,X2V D1M V5G X6F
```
