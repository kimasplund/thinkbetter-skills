Notes

- Z0V: Covers the revocation lag, the audit log, maintenance codes and the photos well. It then says airplane mode "doesn't matter", which contradicts its own point that the revoked person can stay out of sync. It also gets "about 900 guesses ... roughly 10 hours" wrong (at one guess a minute that is about 15 hours) and misses the lockout as a denial-of-service.
- A8B: Sharp throughout. The person being logged writes the history, the attacker holds the sync channel, the gate lockout works as a DoS switch and gives wrong attribution, and the manager is alone with the contents at the photos. Ranking the gate first is argued from time-to-exploit. Good insurer wording and a clear first question for the vendor.
- D0T: The most complete. It notes that the revoked person can block their own revocation, that the photos may be taken against a stale lock state, that a full cache can crowd out other credentials, and the threats to phones as couriers. It ends with a residual-risk section and plain unknowns. Slightly long, and "on launch day every ex-tenant" overstates.
- C0F: Has the core revocation and gate arithmetic. It states "the lock has no notion of time" as fact, then relies on lock-enforced expiry. It misreads the maintenance codes as having "no per-unit scoping" and misses the attacker-controls-sync and lone-manager insider points. The 7 to 14 day window is loose.
- U7S: Strong. It notes that a phone can suppress an update, that you should confirm the denied state before relying on the photos, the lone-manager insider risk, the DoS, and incident response for a key leak. Well-ordered.
- G2M: Tight. It best captures the subtle point that one manager controls entry, the inventory record and the sale, plus the attacker modifying the app to drop the revocation. "Count failures per PIN" makes no sense, because a wrong guess can't be attributed to a PIN. It misses the DoS. The gateway as the top fix is costly but defensible.
- J3G: Good content, including the point that helpers added during the overlock window outlive it, stale-phone rollback, and concrete tests for the insurer. But it exposes an impact-times-feasibility scoring table, and it asserts unknowns as facts, such as "the lock keeps no log of its own".
- T5J: Thinner. It invents an eviction-by-count behaviour, overgeneralizes "the locks are in basements", repeats the per-PIN lockout error, and misses the attacker-controls-sync and insider-at-photos points.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,Z0V,5,6,4,5,5,7,5,37
J-A,A8B,6,7,6,6,5,7,6,43
J-A,D0T,7,6,6,7,4,6,6,42
J-A,C0F,4,5,4,5,5,7,4,34
J-A,U7S,6,6,6,6,5,7,5,41
J-A,G2M,6,6,5,6,6,7,6,42
J-A,J3G,5,6,5,6,4,2,4,32
J-A,T5J,4,5,4,5,5,7,3,33
```

```ranking
judge,brief,order
J-A,brief-2,D0T A8B U7S G2M Z0V J3G C0F T5J
```
