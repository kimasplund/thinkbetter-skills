My recommendation: don't pick any single option as written. Commit on Monday to a narrower offline release built on the 2-week option, with stock changes sent to the server as deltas, and start the Harrowgate IT review conversation this week. Here is the reasoning.

**The binding constraint is the 8-week IT review, not the build.**
Eleven weeks minus an eight-week review leaves about three weeks. Any new app version has to be in Harrowgate's catalogue before the storms, so the app build has to be submitted by roughly week 3. That rules out the 5-week queue-and-replay, the 6-week PWA and the 9-week CRDT rebuild as app releases. Server-side changes don't go through that review, so put as much logic as possible on the server.

**Option by option:**

- **PWA (6 weeks): drop it.** Harrowgate's handsets have the browser disabled and only run apps from their managed catalogue. A PWA runs in the browser, so it's probably not deployable on those handsets at all. It's also too long.
- **CRDT rebuild (9 weeks): drop it for this deadline.** It doesn't fit the review window. It also solves the wrong problem: stock is a shared counter, and a CRDT-style merge of an absolute count would still need a business rule for oversold vans.
- **Driftwell (3 weeks, about $2,000/month): not as a default.** The timing is good, but the contract limits processing of job data to the sub-processors in its schedule, which lists only you and your hosting provider. Adding Driftwell means a contract change with Harrowgate, and a legal and security review, before any build starts. Ask Harrowgate's procurement team now whether they'd agree; if they wouldn't, this option is off the table.
- **Cache plus offline forms (2 weeks): the right base, but it's missing the parts log.** Technicians need to log parts offline too, and this option doesn't cover it as described.
- **Queue and replay (5 weeks): the right mechanism, but too slow as a full build.** A reduced version fits.

**Proposed plan:**

1. **Offline job cache and completion forms (about 2 weeks).** Read-only cache of the day's jobs, plus completion forms saved on the device.
2. **Offline parts logging as an append-only queue (in the same release).** Each part log is an event, for example "job X, part Y, quantity −2, by technician Z, at time T". Don't sync an absolute stock figure from the handset. The server applies each event as a delta to the van's stock.
   - Two pair members logging from the same van then merge cleanly, in any order, with no conflict. Deltas commute, so you don't need a CRDT library for this.
   - Harrowgate's cost-centre billing reads from the server ledger, which keeps the record of who used what, when, and offline or not.
   - Let the stock go negative when it has to, and flag it for dispatch to reconcile. Don't reject a logged part at the handset.
3. **Replay on reconnect, with an authentication rule.** Sign-in tokens last 12 hours and the app may be offline for up to two days. On reconnect, the queued uploads will often fail with an expired token. The app should keep the queue on disk (encrypted), prompt the technician to sign in again, and then retry in order without losing anything. Don't require sign-in while offline, and don't try to extend or bypass the token lifetime.
4. **Server-side change.** Add an endpoint that accepts batched, idempotent events (each with a client-generated ID so retries don't double-count), and returns per-event results.

**Timeline check:** roughly 3 weeks for the app build and test, then submission to IT review by week 3, then review finishes around week 11. That leaves almost no slack, so the build must be scoped tightly. Also ask Harrowgate whether they can start the review on a beta build or run it in parallel with you.

**What to do before Monday:**

- Ask Harrowgate's IT team whether a review can be started early, or whether they'll review a version with the offline features behind a flag.
- Ask Harrowgate's procurement team whether a sub-processor change for Driftwell is possible, so you know whether it's an option at all.
- Confirm the parts-logging API can take deltas. If it currently sets absolute counts, that's the server change to scope first.
- Get Rasmus's view on the CRDT idea in the context of the stock rules above. The concern is that the stock problem is a business rule about oversold vans, and a library won't settle it.

**Assumptions:** I've assumed the 8-week review applies to every new app version, that the three developers can build the 2-week scope in about 3 weeks including testing, and that the stock ledger can be changed on the server. If any of these are wrong, the plan changes, and I'd be glad to go through it again.
