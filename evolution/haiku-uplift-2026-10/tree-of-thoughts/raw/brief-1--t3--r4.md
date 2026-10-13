My recommendation is the two-week option: cache the day's jobs read-only and let technicians fill in completion forms offline, uploaded when they reconnect. It is the only option that fits the constraints you've described, and the reason is the IT review, not the build time.

**The review sets the real deadline.** Each new app version takes about eight weeks through Harrowgate's IT review. Eleven weeks minus eight leaves roughly three weeks to get a build into review. Only the two-week option can be built and submitted inside that window. The five-week queue-and-replay option would reach review around week five and finish around week thirteen, two weeks after the storm season starts. Please confirm with Harrowgate's IT team whether they have an expedited or pre-approved path for a release of this kind. If they don't, the timeline above is the plan.

**The other options fail on specific constraints:**

- **Driftwell** would send job data to a third-party sub-processor that is not in the contract schedule. Adding it means a contract amendment, which will take longer than three weeks, and it still hits the review.
- **Progressive web app** is out. Harrowgate's handsets have the browser disabled and only install from their managed catalogue.
- **CRDT rebuild** is nine weeks, which is too long for the review window. It also does not fit the stock counts well. Van stock and internal billing need one authoritative number, and automatic merging of two handsets drawing from the same van can produce a count the server cannot defend on an invoice. Stock needs server-side rules whatever the sync method.
- **Queue-and-replay** is the right long-term design for the stock problem, because the server can validate each logged part against the current count and flag conflicts. It is too late for this storm season, though. Plan it as the next release, with its own review.

**What the two-week release has to handle:**

1. **Sign-in expiry.** Tokens last 12 hours and crews can be offline for two days. A technician's session will expire in the field. The app must keep the locally stored forms when the session has expired, and must not wipe them on sign-out or failed sign-in. Uploads should run once the technician signs in again after reconnecting. Test this with a two-day offline run.
2. **Stock is stale while offline.** Parts logged on offline forms will not reduce the van count until the form uploads. Two handsets working from the same van can both draw down the same parts. Decide how the server handles a form that uploads after the van has run short, and what the technician sees. Billing should be based on what the server accepts, not what the handset recorded.
3. **Scope.** Make sure the offline forms cover everything a technician must record in the field, including parts and job status. Anything left out will force a signal-dependent step.

**Assumptions I've made:** that IT review applies to every new build, including minor ones; that the two-week estimate covers the offline forms and the upload logic; and that Harrowgate will accept a read-only cache for jobs without other changes. If any of these is wrong, tell me and I will revise the recommendation.

**Before Monday:** ask Harrowgate's IT team about an expedited review, confirm the sub-processor position with their legal team, and agree the stock-conflict rule with their billing contact. Those three answers matter more than the choice between the remaining options.
