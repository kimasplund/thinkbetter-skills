# J-B scores, brief-2

T5J: Correct gate arithmetic and sensible expiry fix, but states as fact that the cache "is evicted by count, not by time" and that the log "is not signed", neither of which is in the brief. Misses that the revoked person's own phone controls whether the revocation arrives, and does not tie the manager's entry to the photo record as an insider risk.

J3G: Strong, specific content: lock-side log with sequence numbers, a stale-state rollback, helpers added during the delinquency window, the 8-digit arithmetic (correct), and a test list for the insurer. But it exposes an impact x feasibility scoring table out of 25, and it asserts "the lock keeps no log of its own" as fact.

G2M: Ranks the points best of the set. It catches that the revoked tenant's own phone carries the revocation, and that one manager controls entry, the inventory photos and the sale. Also covers cache displacement and the gateway fix. Its closing section separates what it is sure of from four specific unknowns. Long, but the length is earned.

U7S: Revocation first, with good points on sync integrity (signed messages, rollback, suppression), physical reset at turnover, and checking the lock state before relying on the photos. Hedges where it should. Somewhat padded in its later sections.

C0F: Revocation first, with good gate maths and a useful list of assumptions. However, it states "the lock has no notion of time", then recommends that the lock enforce expiry itself, which contradicts it. The overlock fix ("tell the tenant the lock may still work") is weak, and it misses the manager-plus-photos insider combination.

D0T: Very thorough and accurate. The revoked person can block their own revocation, a guessed gate PIN frames a real tenant, the log is uploaded by the manager's own phone ("accountability is weakest where power is greatest"), and per-lock keys. Its pilot step measures the real revocation gap. The 75% confidence statement is plain and fine. It is long, and "1234" is not a 6-digit PIN.

A8B: Sharp framing ("the design gives them no reason to help it sync"; the log covers "cooperative users"). It proposes staff sync rounds, stale-lock alerts, a physical overlock fallback, and honest numeric bounds for the insurer. The keypad-bypass and scripting asides are speculative, but the reasoning is otherwise sound.

Z0V: Covers the main issues and has a good point about firmware updates riding the same sync path. But the gate maths is wrong ("about 900 guesses, roughly 10 hours" at 1 guess a minute is about 15 hours). The airplane-mode sentence and the PIN-uniqueness point are muddled.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,T5J,4,5,4,5,6,7,4,35
J-B,J3G,6,7,5,7,4,2,5,36
J-B,G2M,7,6,6,7,5,7,6,44
J-B,U7S,6,6,6,6,4,7,5,40
J-B,C0F,5,5,4,5,5,7,4,35
J-B,D0T,7,7,6,7,4,6,6,43
J-B,A8B,7,7,6,7,5,7,5,44
J-B,Z0V,6,6,4,5,5,7,4,37
```

```ranking
judge,brief,order
J-B,brief-2,G2M A8B D0T U7S Z0V J3G T5J C0F
```
