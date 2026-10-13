Notes (J-A, brief-2)

- L9S: Catches coupling, migration numbering, Postgres round() and the correct tie arithmetic. But the pricing prompt still does an in-place ALTER to bigint with "no backfill here", which contradicts its own expand/contract advice and never says plainly that alter-then-backfill destroys the decimals. Concise and usable otherwise.
- A8R: Flags explicitly that alter-then-backfill loses data, plus Postgres half-away rounding, float traps, unknown quote currency and that CI cannot exercise the backfill. Gives an expand/contract plan and a midweek Kestrel merge. The contract block contains non-TypeScript pseudo-types. Long.
- P7W: Covers every key coupling, including the destructive cast, float ties, pg bigint as string and a CI check for duplicate migration numbers. Adds a production deploy order with dual-write, a rounding-difference log for finance and additive rollback. Very actionable.
- E4F: Spots the double-scaling risk and the audit-column idea, but the pricing prompt still converts in place while the backfill also converts. The "rounding rule for negatives" point is garbled (-2.5 is -2 under both rules). It does not address lock time.
- L6Z: Strong and complete. CI per-branch schema divergence, the destructive cast, float ties, bigint parsing, fallback reads, a migration-gap check and an additive production sequence. Assumptions are listed as questions.
- E3F: Thorough. It shows concretely that a plain cast turns 18.3350 into 18, its tie test cases are correct, and it includes a Thursday trial merge and a rollback order. Its production order deploys code that reads amount_minor before the migration that creates it, which is a slip. Long.
- F3J: Its pricing prompt converts the column to bigint before the backfill without converting data, which is the data-loss trap, and it never mentions Postgres rounding or lock time. Merging pricing before Kestrel is weakly justified, and its Kestrel migration-generator assumption has no basis in the brief.
- Z0E: Compact and correct on the destructive cast, Postgres rounding, expand/contract, floats and the audit column. It has no quotes.currency yet asks for per-currency totals, and it says less about how per-branch CI hides problems.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,L9S,5,5,4,5,6,7,5,37
J-A,A8R,7,6,6,6,4,7,6,42
J-A,P7W,7,7,6,6,5,7,6,44
J-A,E4F,5,4,3,4,5,7,4,32
J-A,L6Z,7,6,6,6,5,7,6,43
J-A,E3F,7,7,5,6,4,7,6,42
J-A,F3J,3,4,3,4,5,6,4,29
J-A,Z0E,6,6,5,5,6,7,5,40
```

```ranking
judge,brief,order
J-A,brief-2,P7W L6Z A8R E3F Z0E L9S E4F F3J
```
