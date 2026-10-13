Notes (J-B, skeptical fact-checker):

- Z0E: Catches the central trap: an in-place cast rounds half away from zero and loses decimals before the backfill can read them. Proposes expand/contract and gets the 1834/712 arithmetic and the Math.round negative case right. Misses that quotes have no currency, and that bigint comes back as a string. The wave timeline is unclear against a single Friday merge.
- F3J: Its pricing prompt still does an in-place numeric-to-bigint migration with "do not convert data here". That destroys the values the backfill needs. Its later "compare against old numeric values" check then has nothing to compare against. It has no Postgres rounding or lock point, and it invents a "Kestrel 5 migration generator" assumption.
- E3F: Very thorough and the arithmetic is correct (7.1350, 18.3250, 0.005 and negative cases). It covers expand/contract, the lock, Postgres round(), and bigint arriving as a string, hedged correctly. Error: the production order deploys code that reads amount_minor before migration 0042 has run. Long.
- L6Z: Covers all the key couplings, including historical quote currency and node-pg bigint strings, with correct tie cases. The production order is correct (migrations, then code, then backfill). Good list of things to confirm. Wave 0 overlaps a little with prompt 1.
- E4F: Contradicts itself. It warns about double conversion, then has the migration convert amount to minor units AND the backfill convert from amount_legacy. Its roundHalfEven takes a float. The negative-rounding sentence is garbled ("-2, not -2"). The production order breaks old code. Credit for honestly flagging that Kestrel's bigint behaviour is unknown.
- P7W: Strongest overall. It has expand/contract with dual-write in the deploy order, correct tie arithmetic, and the string-concatenation hazard. It reserves 0044 and adds a CI check for duplicate numbers. Assumptions are clear. The SUM check lacks a stated tolerance.
- A8R: Deepest analysis, and it frames the decision explicitly: expand/contract vs in-place, and what changes if you choose each. The 7.125-is-exact nuance is correct. It wrongly equates "exact tie" with "half-even differs from half-up", and the contract block is pseudo-TS. Too long for the task.
- L9S: Recommends expand/contract, but its pricing prompt still writes an in-place ALTER to bigint. Backfill verification is weak, and its "settle decisions Thursday" conflicts with "before any agent starts". It raises the re-issue question well and handles currency defaults well.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,Z0E,6,6,6,5,6,7,5,41
J-B,F3J,3,4,3,4,5,6,4,29
J-B,E3F,7,7,5,6,5,7,6,43
J-B,L6Z,7,6,6,6,6,7,6,44
J-B,E4F,4,5,2,4,6,7,4,32
J-B,P7W,7,7,6,6,6,7,6,45
J-B,A8R,7,7,6,7,4,7,6,44
J-B,L9S,5,5,3,5,6,7,5,36
```

```ranking
judge,brief,order
J-B,brief-2,P7W A8R L6Z E3F Z0E L9S E4F F3J
```
