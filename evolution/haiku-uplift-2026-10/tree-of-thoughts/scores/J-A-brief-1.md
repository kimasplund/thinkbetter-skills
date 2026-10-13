Notes (J-A, brief-1)

All 16 replies pick option 4. They differ on how well they handle the van-stock problem, how they deal with token expiry, whether they make uploads idempotent, whether the cache covers a two-day outage, and whether their reasoning about the review timeline holds up.

- J2K: Complete and well ordered. Catches the subtle point that the cache must cover two days, not "the day's", and that the upload queue has to survive token expiry. Also says to get legal sign-off on device caching and to make the team re-estimate with the hidden scope included.
- O2I: Clear table and four design points, including duplicate completions from a crew pair. Open questions ranked by risk, with an escalation path. Does not catch the two-day cache scope.
- N4I: Solid. Server decides stock and the billing-timing question is a good catch. Idempotency is not explicit, and "start the IT review this week" before any build exists is loose.
- R0S: Contains a logic error: it says the 5-week queue "leaves about 6 weeks of review" and is "possibly survivable", which contradicts the 8-week review. It also says not to commit Monday, then gives a plan to commit Monday.
- P5L: Strong event-based stock design, local unlock, encryption and dispatcher conflicts. Good assumption that a longer review puts even option 4 at risk.
- D5E: Makes parts logging online-only for this release. That is a weak call, because parts drive the billing and crews are offline for up to two days. Its CRDT objection is also muddled: both draws really happened. At least it flags the assumption honestly.
- L1W: Hybrid framing with commuting deltas, an idempotent batch endpoint, and keeping logic on the server because server changes skip the review. Insightful, but light on dispatcher conflicts and cache scope.
- G5S: Concise and sound. Says the Driftwell amendment "will not happen in 11 weeks" with more confidence than the evidence supports, and its "submitted in week one or two" timing doesn't fit a two-week build.
- J9V: Very actionable: two-handset airplane-mode test and a Monday message. Extending to 3 weeks leaves zero slack, but it says so.
- Y2L: Thinner. Stock handling is left as "decide how", with no idempotency. Its claim that the Driftwell amendment "will take longer than three weeks" is overconfident.
- J2P: Good review-risk levers: small diff, no new SDKs or permissions, paper fallback. Its "ranking unchanged" claim slightly contradicts the line that follows it.
- M4N: The most thorough. Covers billing from the event log, two-day cache scope, sync-status UI, a re-estimate, and the point that nothing fits if crews need offline editing. Longer than it needs to be.
- W7R: Covers everything that matters, including two-day cache scope and idempotent events. Sets an ordered Monday plan with the queue submitted around week 7, and states its confidence and what would change it.
- U3E: Compact and sound. Notes that replays would hit expired tokens. Missing the local unlock detail, the two-day cache scope and dispatcher conflicts.
- O5F: The "one release, not several" insight is valuable. The delta counter is framed as what a CRDT would give here. Says to ask security first and gives clear "what could change this" conditions.
- D3X: Concise and actionable. Says the server must accept records created under an expired token. Missing dispatcher conflicts.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,J2K,7,6,6,6,6,7,6,44
J-A,O2I,6,7,6,7,5,7,6,44
J-A,N4I,6,5,5,5,6,7,5,39
J-A,R0S,5,5,3,4,5,7,4,33
J-A,P5L,6,6,6,6,5,7,6,42
J-A,D5E,5,5,4,5,5,7,5,36
J-A,L1W,6,6,6,5,5,7,6,41
J-A,G5S,6,5,5,6,6,7,5,40
J-A,J9V,6,7,5,6,6,7,5,42
J-A,Y2L,5,4,5,5,6,7,5,37
J-A,J2P,6,6,5,6,5,7,5,40
J-A,M4N,7,7,6,6,4,7,6,43
J-A,W7R,7,7,6,7,5,7,6,45
J-A,U3E,5,5,6,6,6,7,6,41
J-A,O5F,7,6,6,7,5,7,6,44
J-A,D3X,6,6,6,6,6,7,5,42
```

```ranking
judge,brief,order
J-A,brief-1,W7R J2K O5F O2I M4N P5L J9V D3X L1W U3E J2P G5S N4I Y2L D5E R0S
```
