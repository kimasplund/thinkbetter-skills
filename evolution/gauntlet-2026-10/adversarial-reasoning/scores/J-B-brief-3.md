Notes (J-B, brief-3)

B5F: Solid coverage with correct cap/threshold arithmetic and a useful red-team test as the cheapest check. A garbled volunteer sentence ("20 hours at 25 hours"), no payment-diversion point, and it misses the tiny-donation trigger trick.
G2T: Strong and accurate: $8,300 -> $25,000 ring math checks out, it flags the volunteer-cap ambiguity instead of assuming, and covers payment diversion, insider risk and the quarter-lag window. Long, and has some hyperbole ("easiest document in the world to fake").
L7F: Broad and catches the $5 trigger point, but states "$2,500 per charity per year" as fact when the brief is ambiguous and builds on it. Has unsupported claims ("small registered charities with no independent oversight are common") and is very long.
E5F: Good subtle points: the $50 trigger, client/regulator bribery optics, the cross-year date, an explicit residual-risk statement and assumptions. Minor error: on a refunded gift "the charity keeps both".
W1L: Catches the sharp "five $1 donors then one large gift" trick, the arithmetic is correct, and it honestly flags that likelihoods are judgment. Budget exhaustion is under-weighted, and the conflict-declaration wording is inverted.
F6O: Rich in subtle points (individual fundraiser pages, coercion, vendor-funded donations) and the internal-audit test is good. But it has a factual error ("A third of the money moving is the company's", which should be two-thirds), and 20 controls is heavy.
V4R: Accurate, ranks budget exposure first, flags the volunteer-cap ambiguity, includes bribery-by-proxy and residual risk with stated assumptions. The edge-case list is a little padded.
M3L: The table maps controls to attacks well, and the pre-launch questions are sharp. Errors: it says nothing checks the donation date, but the brief says OCR checks it. It also calls volunteer grants "uncapped", and the "3x their gifts each month" claim ignores the annual cap.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,B5F,6,6,5,6,5,7,5,40
J-B,G2T,6,7,6,6,4,7,6,42
J-B,L7F,6,6,5,6,3,7,4,37
J-B,E5F,7,6,5,6,5,7,5,41
J-B,W1L,6,6,5,6,5,7,6,41
J-B,F6O,6,6,4,6,3,7,5,37
J-B,V4R,6,6,6,6,5,7,6,42
J-B,M3L,5,6,4,6,5,7,5,38
```

```ranking
judge,brief,order
J-B,brief-3,G2T V4R E5F W1L B5F M3L F6O L7F
```
