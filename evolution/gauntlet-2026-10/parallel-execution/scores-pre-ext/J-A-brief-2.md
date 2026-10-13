Notes:
- P1Z: Most complete. It explains why "alter, then backfill" loses data, gets the tie arithmetic right, notes that Postgres ROUND rounds half away from zero, points out that 7.125 is exact in binary and that Math.round behaves differently on negatives, and covers CI blindness and locking. It ranks the expand/contract decision as the top item. The shared contract contains pseudo-TypeScript that won't compile, and gating the DKK launch on the backfill is arguable.
- H6T: Tight and correct. It raises the 4-to-2 decimal precision loss for finance and notes that pg returns bigint as a string. It ends with a short list of questions to confirm. The backfill verification is weak: "within 0.005" doesn't check half-to-even.
- M9C: Sound structure with an integration branch, dual-writes and empirical type checks for Kestrel 5. The rounding section has a muddled sentence, and the backfill only verifies a sample. Thinner on detail than the others.
- V5L: Good conflict-resolution step in the merge plan and a good point that tie rows will differ from what customers were actually charged. The backfill's SUM(amount) vs SUM(amount_minor)/100 check expects equality, which rounding prevents, and it divides with floats.
- E2X: Strong extra risks: other consumers of quotes.amount, reports mixing units, line vs total rounding drift, a DKK feature flag. It wrongly calls 18.3350 "a tie at 3 decimals". It also requires the "SQL migration" to agree on rounding even though its own expand migration does no conversion.
- N3R: Sharp on the bare cast (18.3350 becomes 18) and on adding a reusable half-even SQL function. But the production order deploys code that reads amount_minor before migration 0042 adds the column. The "under half a minor unit" check contradicts exact ties, and "1 hour" for Day 0 is optimistic.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,P1Z,7,6,6,6,5,7,6,43
J-A,H6T,6,5,5,6,6,7,6,41
J-A,M9C,5,5,5,5,5,7,5,37
J-A,V5L,6,6,5,5,5,7,6,40
J-A,E2X,6,6,5,6,5,7,5,40
J-A,N3R,6,6,4,5,5,7,5,38
```

```ranking
judge,brief,order
J-A,brief-2,P1Z H6T E2X V5L N3R M9C
```
