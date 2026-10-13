Notes (J-A, brief-2)

- P1Z: Catches nearly everything: migration collision, the alter-then-backfill data loss, Postgres half-away rounding, bigint as string, unknown currency, CI's empty DB and locking. It names the single most important decision. The prompts are the most usable as written. It is long, and the contract pseudo-signature is not valid TS.
- M9C: Tight and correct. It reserves migration numbers, uses expand/contract and a Step 0 integration branch, and raises line versus total rounding. It doesn't say outright that a plain cast drops the x100 scale. Well sized.
- E2X: Strong and very specific: aggregates and counts come back as strings, other consumers of quotes.amount, reports mixing minor and major units, and the same fixtures run end to end in TS, SQL and the backfill. It misses the explicit scale loss and the precision-loss decision. Long.
- P2H: States outright that 18.3350 would become 18. It covers bigint, wants finance sign-off in writing, and puts tie rows in a CSV. Compact, with a clear Kestrel-first order.
- E0S: Sound and concise, and it flags the precision-loss decision and the JSON/API boundary. It misses bigint-as-string, and its prompts are thinner.
- Q2L: Explicitly says the cast leaves major units. Good deploy and rollback plan. It misses bigint-as-string.
- L9A: Good. It says billing/DKK is the time-critical piece, and has a bigint check. But the pricing prompt switches reads to amount_minor before the backfill has filled it.
- C3H: It misdiagnoses the migration/backfill clash as a double x100 conversion instead of data loss. It leaves the core decision as a bracketed option inside the prompt. Its Kestrel-last order is weakly justified.
- N3R: Very thorough: shared SQL half-even function, extra tie vectors, bigint, rollback order, review checklist. The prod order puts fallback code before migrations, and the reply is long.
- V5L: Solid. It notes that pg returns int8 as a string, logs rounding differences against Math.round, and has a clear deploy order and 0045 for Kestrel. Moderate length.
- H6T: The most complete list of issues: explicit scaling, bigint, precision loss, CI per-branch schema and currency. Practical prompts and merge order.
- C0D: Correct and compact. It ships a contract-first commit today, shows the float value 1833.4999999999998 and has sensible gates. It doesn't mention CI's empty DB for the backfill.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,P1Z,6,7,6,7,4,7,6,43
J-A,M9C,6,6,6,6,6,7,6,43
J-A,E2X,6,7,6,6,4,7,6,42
J-A,P2H,6,6,6,6,6,7,6,43
J-A,E0S,5,5,6,5,6,7,6,40
J-A,Q2L,6,6,6,6,5,7,6,42
J-A,L9A,6,6,5,6,5,7,6,41
J-A,C3H,4,5,4,4,4,7,4,32
J-A,N3R,6,7,6,6,4,7,6,42
J-A,V5L,6,6,6,6,5,7,6,42
J-A,H6T,7,6,6,6,5,7,6,43
J-A,C0D,6,6,6,6,6,7,6,43
```

```ranking
judge,brief,order
J-A,brief-2,P1Z H6T P2H M9C C0D N3R E2X V5L Q2L L9A E0S C3H
```
