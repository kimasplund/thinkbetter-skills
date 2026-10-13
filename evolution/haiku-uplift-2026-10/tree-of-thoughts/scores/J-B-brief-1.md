# J-B scores, brief-1

Notes per reply:

- D3X: Tight and correct. It names the review gate, the PWA and Driftwell blockers, stock as deltas, an expired-token flow with local unlock, and encryption. It skips idempotency and stale-job conflicts. Very well proportioned.
- O5F: The most complete. It adds the point that each iteration costs eight weeks of review, so the first submission is the only one before the storms. It also covers ID-keyed deltas, stale jobs and a security pre-check. A little long, and "end of week 3 = one spare week" is loose.
- U3E: Sound throughout, with a good check on whether the 2-week estimate includes reconciliation. The kebab-case option label reads like an internal tag.
- W7R: Strong. It covers parts events, two days of cached data, idempotency and an owner for the review conversation. It gives a stated confidence and says what would flip the answer. "Every version goes through an eight-week review" overgeneralises from one data point. Long.
- M4N: Very thorough. It suggests billing from the event log, a local caution on parts that may already be gone, and keeping the release narrow, and asks for a re-estimate. Too long for the task, and "photos" is not in the brief.
- J2P: Good, and it includes a paper fallback if the review can't be shortened. The closing sentence contradicts itself: the ranking is "unchanged", yet the reader should build the queue instead.
- Y2L: Correct choice, but it leaves the stock rule for the reader to decide and doesn't propose deltas. It says the contract amendment "will take longer than three weeks" as a certainty.
- J9V: Grows option 4 to about 3 weeks, which uses up all the slack, then claims a buffer. It also calls Driftwell's timing "works" when Driftwell lands at week 11 with no slack, the same date as J9V's own plan.
- G5S: Reasonable design points, and it correctly makes offline token behaviour a decision for Harrowgate's security team. It says the amendment "will not happen in 11 weeks" as if certain. Re-authenticating "without asking the technician to re-enter anything" sits badly with the 12-hour token policy.
- L1W: Raises a useful point: server changes avoid the app review. It states this as fact, without flagging it as an assumption. It calls Driftwell's timing "good" and plans a 3-week build with no slack. The framing "don't pick any single option" doesn't match the plan that follows.
- D5E: Makes parts logging online-only, which fails crews who are offline for two days. It says a reconciliation rule can't be designed in two weeks, without support. It also misses the token issue for the queue option.
- P5L: Strong and well grounded. It covers events, IDs, offline auth that the server accepts after re-auth, preparing the review package, and an honest scope limit. Slightly long.
- R0S: Contains a logic error: it calls queue-and-replay with 6 weeks left for an 8-week review "possibly survivable". It also says not to commit Monday, then commits Monday. Its stock rule flags any change made in the meantime, which would flag nearly every upload.
- N4I: Concise and mostly right, and it asks a good question about billing timing. It invents "must not go negative", then accepts negative counts anyway. No idempotency, and no cache scope for a two-day outage.
- O2I: Excellent. It covers duplicate completions by the pair, a 48-hour dead-token test, open questions ranked by risk, and an argument from the security team's past rigidity. "Two likely shapes" lists only one, and it overgeneralises the review length.
- J2K: Caches two days of jobs. It asks legal to confirm device caching against the schedule, and flags the server-side review exemption as an assumption. It does not mention encryption or a local unlock.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,D3X,6,6,6,6,7,7,6,44
J-B,O5F,7,7,6,7,5,7,6,45
J-B,U3E,6,6,6,6,6,5,6,41
J-B,W7R,7,7,6,7,5,7,6,45
J-B,M4N,7,7,6,7,4,7,5,43
J-B,J2P,6,6,5,6,6,7,6,42
J-B,Y2L,5,4,5,5,6,7,4,36
J-B,J9V,6,6,4,6,6,7,5,40
J-B,G5S,6,6,5,6,6,7,4,40
J-B,L1W,6,6,4,5,6,7,5,39
J-B,D5E,4,5,3,5,6,7,5,35
J-B,P5L,7,7,6,6,5,7,6,44
J-B,R0S,4,4,2,4,6,7,4,31
J-B,N4I,5,5,5,5,6,7,4,37
J-B,O2I,7,7,6,7,5,7,5,44
J-B,J2K,6,6,6,6,6,7,6,43
```

```ranking
judge,brief,order
J-B,brief-1,O5F W7R O2I P5L D3X M4N J2K J2P U3E G5S J9V L1W N4I Y2L D5E R0S
```
