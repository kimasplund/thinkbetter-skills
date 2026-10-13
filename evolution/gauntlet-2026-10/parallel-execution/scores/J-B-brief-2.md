# J-B scores, brief-2

Notes per reply:

- C0D: Catches every central coupling, including that a plain cast to bigint drops the x100 scale (18.3350 -> 18) and destroys the history before the backfill runs. Correct tie arithmetic, a shared rounding function, bigint return type treated as unknown. Tight prompts. Small tension: it says Math.round also gives 1834, then shows that the float path gives 1833.
- H6T: Thorough and correct on scale loss, ties, waves and per-branch CI. States as fact that bigint arrives as a string through node-pg, but nothing in the brief says which driver Kestrel uses. "Each branch fails in isolation" is overstated.
- V5L: Strong on every axis, with useful HANDOFF.md and conflict-resolution guidance. It also asserts pg bigint-as-string as fact. The sum check has no rounding tolerance, and the dual-write in the deploy plan never appears in the pricing prompt.
- N3R: Very complete, with good extra tie vectors and the point that CI's empty DB never exercises the backfill. Two errors: the production order deploys code that reads amount_minor before migration 0042 exists, and the parseDbAmount adapter returns number, which contradicts its own no-floats rule.
- C3H: Gets the cast wrong. It says the in-place cast converts the rows and that a backfill would multiply by 100 a second time, missing that a plain cast loses the scale. It recommends merging Kestrel last with weak justification and leaves the core migration choice open inside the prompt.
- L9A: Solid. It catches that Postgres round() is not half-to-even and that the migration and backfill overlap, but it doesn't spell out the loss of scale under a plain cast. The pricing prompt says to "use amount_minor" before the backfill has filled it.
- Q2L: Concise and correct, including 18.3350 -> 18 under a plain cast. The merge schedule is concrete. It doesn't mention how bigint is returned or that CI's empty DB can't exercise the backfill.
- E0S: Compact and mostly right. It says Postgres would do the rounding, but misses that the cast doesn't scale by 100. It does catch the empty-DB CI gap and the JSON/API boundary. Its assumptions are flagged.
- P2H: Catches the scale loss and the ACCESS EXCLUSIVE lock, and hedges on bigint. Putting Kestrel on Day 1 is optimistic and serializes the work. "Migration B" vs "Agent B" naming is confusing.
- E2X: Good extras: penny drift between line totals and the invoice total, other consumers of quotes.amount, a feature flag for DKK. But it calls 18.3350 "a tie at 3 decimals" and misses the scale loss. Its wave plan delays billing, which is time-critical. It states that historical rows have no currency, which the brief doesn't say.
- M9C: Sound and well hedged, and it asks for a bigint check before any parsing code is written. It only says the cast would "silently round" and doesn't mention the lost scale. The JPY/KWD aside is mild padding.
- P1Z: The most exhaustive, and it makes the subtle point that 7.125 is exact in binary. The pseudo-TypeScript contract isn't valid code, the paste placeholders add bulk, and holding the DKK launch behind the backfill is questionable. Heavy length.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,C0D,7,7,6,6,6,7,6,45
J-B,H6T,7,7,6,6,6,7,5,44
J-B,V5L,7,7,5,6,6,7,5,43
J-B,N3R,7,7,5,6,5,7,6,43
J-B,C3H,5,5,3,4,5,7,4,33
J-B,L9A,6,6,5,6,6,7,6,42
J-B,Q2L,6,6,6,6,6,7,6,43
J-B,E0S,5,6,5,5,6,7,6,40
J-B,P2H,6,6,5,6,6,7,6,42
J-B,E2X,6,7,4,6,5,7,5,40
J-B,M9C,6,6,6,6,6,7,6,43
J-B,P1Z,7,7,6,6,4,7,6,43
```

```ranking
judge,brief,order
J-B,brief-2,C0D H6T N3R V5L P1Z Q2L M9C P2H L9A E0S E2X C3H
```
