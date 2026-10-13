Notes:
- F0O: Finds the 50-vs-60 pallet mismatch, covers both invoicing scenarios, acknowledges side-gate theft as a counter-case, and flags the Q3 restatement. The "earlier months were normal (check)" line half-asserts data the brief never gave, and "thieves don't favour 40 kg bags" overclaims.
- F0Y: Gets the mechanism, notes the one northern store that kept its old contractor, flags that bag sizes may differ by line in a clear assumptions section, and sets a residual threshold. It asks for an ASN but does not test whether Greenfold bills for 50 or 60.
- O5G: Gets the mechanism, adds a dose-response check (lowest Greenfold volume should show the smallest gap), covers invoices and per-SKU pallet sizes, and names the single test that would kill the theory. It does not mention the one northern store that kept its old contractor.
- Q5P: Gets the mechanism and makes good use of the control store and invoice scenarios. Its contractor logic is inverted ("should be at normal shrink if the contractor were the cause"), and it calls the non-northern switched stores "southern", which the brief does not say.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,F0O,6,6,5,6,6,7,5,41
J-A,F0Y,6,6,6,6,6,7,6,43
J-A,O5G,6,6,6,6,6,7,6,43
J-A,Q5P,6,6,4,6,6,7,5,40
```

```ranking
judge,brief,order
J-A,brief-2,F0Y O5G F0O Q5P
```
