Notes per reply

- N4I: Correctly makes the 8-week review the binding constraint. It covers PWA, Driftwell and the stock count, with server-applied decrements, and handles tokens and billing timing. It catches the one-release point. It misses idempotent retries and the staleness of cached jobs. Tight and actionable.
- D3X: Strong and compact. It gets delta events for stock, offline unlock for expired tokens, and encryption, and it is honest about what technicians lose. It has no idempotency or duplicate-upload safety. The suggestion that queue-and-replay "might still make storm season" is reasonable because it is conditioned on a shorter review.
- P5L: Very thorough. It uses ID-keyed decrement events with idempotent retries, and it flags that the offline count is only a local estimate. It covers token handling, encryption and dispatcher changes while offline. Its assumptions include the possibility that the review takes longer than 8 weeks. Slightly long.
- O5F: The best overall. It states the subtle "one release, not several" point explicitly, along with idempotent deltas, the token plan, stale jobs and a week-by-week schedule. It closes with a clear "what could still change this" section. The table earns its place. It runs a little long.
- J2K: It catches that a "day's jobs" cache is too short for a two-day outage, which is a subtle, practical point. It also covers idempotent upserts, billing timing, and asking the team whether the 2-week estimate includes this scope. Its explicit assumption that server changes skip app review is useful. A week-2 submission is ambitious.
- O2I: Strong. It covers the Driftwell runner-up case and duplicate completions by the pair, tests a 48-hour dead token, and orders its open questions by risk. "Security team won't bend, so won't add a vendor" is an inference, but it is presented as judgement. Slightly long.
- D5E: Recommends keeping parts logging online-only. For crews out of signal for two days, that removes the core billing workflow. It also overstates the difficulty ("can't be designed responsibly in two weeks") when a simple delta rule exists. Its claim that replay "validates each draw" ignores that the parts are already physically used. It does flag this as the assumption most likely to change.
- R0S: Its timeline reasoning is wrong. It treats queue-and-replay as "6 weeks of review... possibly survivable" when the review takes 8 weeks. It also contradicts itself: "don't commit Monday without resolving blockers", then "commit Monday". The token concern and the device-bound credential idea are good. It misses the one-release constraint.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,N4I,6,6,6,6,6,7,5,42
J-A,D3X,6,6,6,6,6,7,5,42
J-A,P5L,7,7,6,7,5,7,6,45
J-A,O5F,7,7,7,7,5,7,6,46
J-A,J2K,7,7,6,6,6,7,6,45
J-A,O2I,7,7,6,7,5,7,6,45
J-A,D5E,4,5,4,5,6,7,5,36
J-A,R0S,5,5,3,4,6,7,4,34
```

```ranking
judge,brief,order
J-A,brief-1,O5F P5L O2I J2K N4I D3X D5E R0S
```
