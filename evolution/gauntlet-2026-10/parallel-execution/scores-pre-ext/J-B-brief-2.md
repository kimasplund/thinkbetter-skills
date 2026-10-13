Notes:

- N3R: Catches the most of any reply. It names the in-place cast loss explicitly (18.3350 becomes 18, not 1834) and says Postgres round() rounds half away from zero. It requires parsing that works under both Kestrel versions and points out that CI's empty database never exercises the 3.1M-row backfill. Every tie example checks out (7.1350, 18.3250, 0.005, negatives), and the prompts can be pasted as they are. Two errors: the production deploy order ships code that reads amount_minor before migration 0042 has added the column, and it says the max rounding difference "must be under half a minor unit" when exact ties come out at exactly half a unit.
- E2X: Has good risk items (a DKK feature flag, other consumers of quotes.amount, reports that sum amounts). But it never warns that Postgres round() is half away from zero, yet it lets the backfill "do it in SQL". It calls 18.3350 "a tie at 3 decimals", which is wrong. Its merge check expects 0044 to be present even though 0044 is deferred. And it runs "rounding fixtures through the SQL migration" when under expand/contract that migration doesn't convert anything.
- V5L: Compact and accurate. It gets the cast truncation, Postgres half-away rounding, and pg returning bigint as a string. It gives concrete conflict-resolution guidance for the merge and the correct deploy order (migrations before code). It also flags well that tie rows will differ from what customers were charged. Weaknesses: the SUM(amount) vs SUM(amount_minor)/100 check has no tolerance, so rounding makes it fail by design. It also says less than others about CI being unable to exercise the backfill.
- M9C: Sound and well sized. It offers the cheapest uncertainty reducer of any reply: have the Kestrel agent test what types numeric and bigint actually come back as before anyone writes parsing code. Tie analysis and the Postgres round() warning are correct, and its dual-write rollout is right. It is weaker on the cast truncation detail, the production order leaves out 0043, and backfill verification only samples the known ties.
- H6T: Thorough and correct on the 7.1250 vs 18.3350 tie behaviour, the 2^53 bound, and the "within 0.005" verification. It handles calibration well, with an explicit list of things to confirm. Minor problems: the agent letters (A = pricing, C = Kestrel) don't line up with the prompt numbering, and the backfill branch is told to test "through 0042" when it doesn't have that migration.
- P1Z: Deepest reasoning. It weighs the in-place ALTER counter-case, gives an exact tie test in numeric, and notes that 7.125 is exact in binary while other values are not. But it is the longest reply and repeats itself. The shared contract is not valid TypeScript ("Decimal-or-string-or-bigint-safe input"), the prompts contain "[paste here]" placeholders, and 0044 is promised to both the ORM agent and the contract step.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,N3R,7,7,5,6,5,7,6,43
J-B,E2X,5,6,4,5,4,7,5,36
J-B,V5L,6,6,5,5,6,7,6,41
J-B,M9C,6,6,5,6,6,7,6,42
J-B,H6T,6,6,5,6,5,7,6,41
J-B,P1Z,7,5,6,6,3,7,6,40
```

```ranking
judge,brief,order
J-B,brief-2,N3R M9C H6T V5L P1Z E2X
```
