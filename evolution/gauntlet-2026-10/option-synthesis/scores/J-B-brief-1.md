Notes:
- V1H: The most realistic substance. It treats survival and grading separately (outdoors at 55%, not 65%), notices that the neighbours' 15% losses cannot fit with 90% of hauled colonies grading, and says honestly that even the combination may not reach 420. The broker arithmetic is right and its correlation risk is flagged. The arithmetic checks out ($57.3k, $63.5k, $63.7k). It is buried under heavy method scaffolding: anchored value scales, adoption rules, "not blind" and "could not hash" disclaimers, and a points table. It uses many invented percentage guesses, though they are mostly flagged.
- M4V: Clean and direct. It correctly reverses the broker decision (+$80 against being short) and correctly notes he needs no cash now. However, it treats 104/150 as if it were the share of all wintered colonies, so outdoor grading becomes about 65%. The plan then lands at "about 420, right at your target", which is optimistic. It takes Dunmere's 90% at face value and leaves out mite health and whether the co-op accepts broker colonies.
- N4O: Readable, with correct broker logic and good checks on the contract terms. But it has a muddled cost-per-graded claim ("about $100 at Dunmere ... about $100 for the cellar too") that contradicts its own conclusion. It also suggests using the reserve to move colonies to Dunmere "if winter is worse than average" by late October, before the winter can be known. It labels four years of data as "one cellar season" and has the same optimistic 65% outdoor assumption.
- E3Y: Good insight on how Rafe's supply depends on the same hard winter, on co-op acceptance, and on the value of surviving colonies. But it has the heaviest machinery leakage (guards, adoption rule, a breakdown of the miss probability, "could not hash"). It warns against splitting the herd three ways, and then its own ELSE IF branch does exactly that. It uses the same optimistic 66% outdoor rate, and its net figures can't be reproduced from the stated assumptions.

Ranking note: V1H ranks first despite a lower total, because for this user its realistic numbers on whether 420 is reachable outweigh the scaffolding.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,V1H,6,6,6,6,2,1,5,32
J-B,M4V,4,5,4,5,6,7,4,35
J-B,N4O,4,5,3,5,6,7,4,34
J-B,E3Y,5,6,4,6,2,1,4,28
```

```ranking
judge,brief,order
J-B,brief-1,V1H M4V E3Y N4O
```
