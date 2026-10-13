I'd commit to the **cache-read-only-and-queue-forms-offline** option (2 weeks), and treat the other options as ruled out by the constraints you listed, not by their feature sets.

The deciding constraint is timing, not sync quality. Harrowgate's IT review takes about 8 weeks, and every new app version goes through it. You have 11 weeks. So a version has to be finished and submitted to review by about week 3 to be approved before storm season, and that makes the build estimate the real limit:

- **CRDT data layer (9 weeks):** 9 + 8 = 17 weeks. Misses the deadline by a wide margin. It is also a poor fit for the van stock counts: CRDTs merge concurrent edits, but a decrement on a shared count that Harrowgate bills from needs bounded, server-authoritative reconciliation, not automatic merging.
- **Driftwell (3 weeks, about $2,000/month):** 3 + 8 = 11 weeks, with zero slack. It also almost certainly fails the contract: job data would pass through a new sub-processor that is not in the schedule (today it is only you and your hosting provider). Adding one needs Harrowgate's agreement and a schedule amendment, which you cannot count on before Monday or before winter.
- **Queue and replay (5 weeks):** 5 + 8 = 13 weeks. Misses. Its design also has two problems you would have to solve anyway: replayed stock decrements from two handsets on the same van will conflict and need a server-side rule, and sign-in tokens last 12 hours while crews may be offline for two days, so replays will hit expired auth.
- **PWA (6 weeks):** 6 + 8 = 14 weeks. Misses. Harrowgate's handsets have the browser disabled, so a PWA cannot run on them at all.

**Cache-and-queue-forms (2 weeks):** 2 + 8 = 10 weeks, which leaves about one week of buffer. It is the only option that clears the review in time with a margin. It fits Harrowgate's constraints: no new sub-processor, and it doesn't need the sign-in token to be valid while offline.

To make it work, design these parts in from the start:

1. **Stock counts.** Do not show or change live van counts offline. Record each part log as a local event with a unique ID. On upload, the server applies it to the van's count, and if the result goes negative or two crews' entries conflict, the server flags it for a dispatcher. This keeps billing based on server-side counts, and you should tell Harrowgate that counts settle on upload rather than in real time.
2. **Auth.** Keep the local queue when a session expires or the user signs out. On reconnect, prompt for sign-in, then upload the queue. Never wipe offline data on token expiry.
3. **Idempotent uploads.** Use the event IDs so a retry after a dropped connection does not double-count parts.
4. **Local storage.** Encrypt the cached jobs and queued forms on the device, since they hold job and customer data.

Before Monday, check these with Harrowgate and your team:

- Ask Harrowgate's IT whether the 8-week review is fixed for every version, or whether a small, scoped release can be fast-tracked. This single answer could change the whole ranking.
- Confirm with Harrowgate that the offline stock-count behaviour above is acceptable for billing. If it is not, the CRDT or queue options become a question of scope, not just time, and you would need to renegotiate the deadline.
- Ask your mobile team whether the 2-week estimate includes the server-side reconciliation and the conflict flag. If not, that work could push it past the buffer.

Assumptions: the 8-week review applies to each release, not just the first; the estimates are accurate; and the storm-season deadline is firm. If the review can be shortened or started on an early build, reconsider the 5-week queue-and-replay option, since it gives fuller offline behaviour than read-only caching.
