Notes

- R6S: Finds the 50-vs-60 pallet mismatch. Strong 60-vs-50 reconciliation, invoice-claim branch, abrupt-vs-gradual test, explicit confidence and what would change it. Misses the one northern store that kept its contractor and the two stores where tools are off book.
- J5W: Correct core and a good list of checks; flags the northern store that kept its contractor and other lines that moved to direct delivery. One muddled sentence on self-checkout logic, no invoice-recovery angle, softer landing.
- O5G: Correct core with the size put in numbers (landscape slice about 1.2 points), a store-by-store volume gradient test, per-SKU pallet check, recommendation with a residual threshold and 80% confidence. Most usable on the day.
- F0O: Correct core with the gap sized in points, and it fairly concedes that bags could be stolen at the side gate. But it cites "earlier months normal" as evidence while admitting it is unknown, and "thieves don't favour gravel" is overstated.
- Q5P: Sharpest coverage of the secondary points: the northern store that kept its old contractor as a control, the two stores where tools are off book, the invoice claim, other direct-delivery lines possibly explaining paint and other, and why Store 14 would not flag the change. No explicit confidence figure.
- U9D: Solid and well calibrated on effect size, with per-SKU and mixed-pallet checks and a process fix for supplier changes. "Heavy, low-value, hard to steal" is asserted rather than shown.
- G2R: Correct core, but there are errors. It says "17% of received quantity" when that should be "of booked". It calls the residual "~1.5% above normal", which contradicts its own arithmetic. "Nobody walks out with those" is overconfident, and the size check is vague and a bit padded.
- F0Y: Correct core with a good per-store reconciliation, a DC-vs-Greenfold split and an ASN fix. It states "DC pallets really were 60" as fact, and the "20% of that pallet" framing is loose.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,R6S,6,6,6,7,6,7,6,44
J-A,J5W,6,6,5,5,6,7,5,40
J-A,O5G,6,7,6,7,6,7,6,45
J-A,F0O,5,6,5,6,6,7,5,40
J-A,Q5P,7,6,6,6,6,7,6,44
J-A,U9D,6,6,5,6,6,7,6,42
J-A,G2R,5,5,4,5,5,7,4,35
J-A,F0Y,6,6,5,6,6,7,5,41
```

```ranking
judge,brief,order
J-A,brief-2,O5G Q5P R6S U9D F0Y J5W F0O G2R
```
