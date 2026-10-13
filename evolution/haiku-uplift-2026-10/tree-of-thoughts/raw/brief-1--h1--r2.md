Go with the read-only cache plus offline completion forms (the 2-week option). Widen it slightly to include parts logging, and start the review clock as early as you can.

**Why the 8-week review decides this**
- You have 11 weeks. Harrowgate's IT review took 8 weeks last time, so a build has to be submitted by about week 3 to be installed before storm season.
- Only the 2-week option fits that window with any margin. The 5-week queue and the 9-week CRDT rebuild would reach review at week 5 or later and land after the deadline (week 13 or later). That holds unless Harrowgate agrees to a faster review, which you should ask for (see below).

**Why the others fail**
- **Progressive web app:** Harrowgate's handsets have the browser disabled and only install from the managed catalogue. This option can't run on their devices at all, and it would also need a review.
- **Driftwell:** It would be a new sub-processor handling job data. Your contract limits that to you and your hosting provider, so you'd need Harrowgate's agreement to amend the schedule. That is likely slow, and it is a legal and security question you can't settle by Monday. Three weeks of build plus the review also leaves almost no slack.
- **CRDT rebuild:** At 9 weeks it can't make the window. Rasmus's instinct is sound as a long-term direction, but the data layer is better rebuilt after this deadline than under it.

**Three problems to design for in the 2-week scope**
1. **Van stock with two handsets.** Two technicians drawing from the same van while offline will both decrement from a stale count. Don't sync absolute counts. Log each part use as an event (van, part, quantity, timestamp, device) and have the server apply them as deltas. The count can then go negative after a merge. Show that to dispatch as a flag to reconcile, not as an error, because Harrowgate bills cost centres from these numbers. This is a small queue for one action type, not a general queue.
2. **12-hour tokens against a 2-day outage.** The token will expire while the crew is offline, and Harrowgate won't change that. Let the app open and work from the local cache using a device unlock (PIN or biometric). Hold the pending uploads, and require a normal sign-in on reconnect before uploading. Make sure the server accepts records created under an expired token once the user re-authenticates, with the original timestamps. Confirm this approach with Harrowgate's security team early.
3. **Local data on the phone.** Encrypt the cached jobs and pending forms on the device, and clear them once they've uploaded.

**What to do this week**
- **Monday:** commit the team to this scope. Target a review submission by the end of week 3 at the latest, and aim for week 2.
- **Immediately:** ask your Harrowgate contact to start the IT review early, or to fast-track it given storm season. Offer them a preview build. This is your biggest schedule risk, and a faster review is the only way the larger options become possible.
- **Next:** plan the queue-and-replay approach (5 weeks) as a second release. It can cover edits to jobs and other actions beyond forms and parts. If the review can be shortened, it might still make storm season. Plan the CRDT work for after that.
- **Tell Sales:** Driftwell is off the table for Harrowgate unless the contract changes.

**What this doesn't give technicians**
They can't edit job details or see jobs dispatched after they lose signal. Check with Harrowgate that "view the day's jobs and complete them" is enough for a two-day outage. If crews need more, say so before Monday, because that changes the answer.

**Assumptions I made**
- The 8-week review applies to every new app version.
- Your estimates include testing.
- Jobs are assigned before crews leave signal.
