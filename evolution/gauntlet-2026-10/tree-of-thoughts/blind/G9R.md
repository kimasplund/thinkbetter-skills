**Recommendation: go with option 4, the read-only job cache plus offline completion forms. Build it in about 2 weeks, with parts usage captured as decrement events. Submit it to Harrowgate's IT review by the end of week 3.**

The deciding factor is the review window. Your constraints rule out most of the options before cost or elegance comes into it.

**Why the others fail**

- **Review timing.** Harrowgate's managed catalogue requires a review of every new version, and the last one took eight weeks. You have 11 weeks. To be live before storm season, a build has to be submitted by about week 3. Any option where dev plus review exceeds 11 weeks misses the date.
  - Action queue: 5 + 8 = 13 weeks. Misses.
  - PWA: 6 weeks, and it is also unusable. Their handsets have the browser disabled and only install apps from the managed catalogue.
  - CRDT rebuild: 9 + 8 = 17 weeks. Misses by a wide margin. It is also the riskiest, because you would be rebuilding the data layer on a deadline for your biggest customer.
  - Driftwell: 3 + 8 = 11 weeks. That leaves zero slack, and it has a second problem (below).
- **Driftwell and the contract.** Harrowgate's contract limits processing of job data to the sub-processors in its schedule, which today is you and your hosting provider. Driftwell would be a new sub-processor handling their job data. You would need a contract amendment from Harrowgate before you could ship it. That is a legal and security negotiation on top of the 8-week app review, and it makes the 3-week estimate misleading. Sales likes the speed, but the speed isn't real here.
- **Cost.** $2,000 a month is minor compared with the risk. The real costs are the amendment and the missed date.

**What option 4 needs to get right**

Its apparent weakness is that it is "only forms". The context you gave means it still has to handle a few things properly, and these should be in the 2-week scope.

1. **Stock counts.** Two technicians in a pair draw from the same van, each on their own handset, and may both be offline for up to two days. Do not upload an absolute count like "stock = 7". Record each part as an event ("used 2 of part X, van V, at time T, by technician U"), each with a unique ID. The server applies them as decrements. Decrements add up correctly in any order, so two offline handsets cannot overwrite each other. The unique ID makes retries and duplicate uploads safe, which matters because Harrowgate bills its cost centres from these counts.
   - Edge case: two offline handsets could together take stock below zero. Accept this and flag it for the dispatcher to reconcile. Don't block the technician in the field.
   - A van that shows 3 of a part on one handset may really have 1. Offline, the displayed count is only a local estimate, and the UI should say so.
2. **Token expiry.** Tokens last 12 hours and Harrowgate won't change that, so assume the token will be expired when the crew reconnects after a two-day trip. Two requirements follow.
   - The app must let a technician keep working offline with an expired token. Use a local unlock, such as the device PIN or biometrics, against data cached while they were signed in.
   - On reconnect the app should prompt for a fresh sign-in, then upload. The server should accept events authored while offline, attributed to the technician and device and carrying the offline timestamp. Check this with Harrowgate's security team, because it is the part they are most likely to ask about.
3. **Data on the device.** The cache holds job data on a phone that may sit in a van. Encrypt it at rest and clear it after a successful upload or on sign-out. This will probably be a question in the IT review, so having an answer ready helps.
4. **Job changes while offline.** A dispatcher may reassign or cancel a job while a technician is out of signal. With a read-only cache you can't merge those edits. On upload, flag any form for a job that changed and let the dispatcher resolve it. This is acceptable for storm season. It is not a full offline product.

**Plan for Monday**

- Commit the team to option 4. Allow 2 weeks of build and use the rest of the time before week 3 for testing and the review package. Write the security answers (encryption, offline auth, data handling) up front so the review doesn't stall on them.
- This week, ask Harrowgate's IT contact about the review: whether it can be expedited for a pre-storm release, whether a small update is faster than a full review, and whether you can submit a build for early feedback. If it goes faster than eight weeks, you gain slack.
- Treat the queue-and-replay design as phase two, after storm season. The event model above is the first step toward it, so the work carries over. Don't start it now. A second version would also need its own review.
- Be upfront with Harrowgate and with Rasmus about what this delivers. Technicians get their day's jobs, can complete jobs and log parts for up to two days without signal, and everything uploads on reconnect. They can't edit or create arbitrary records offline. Rasmus's CRDT idea may be a good long-term direction, but it doesn't fit this deadline and can be revisited once the immediate need is met.

**Assumptions**

- Eight weeks is a typical review time, not a guaranteed one. If Harrowgate says it will be shorter, you could stretch scope a little. If it is longer, even option 4 is at risk, and you should escalate to Harrowgate now.
- "Working offline" for Harrowgate means completing jobs and logging parts. If they need technicians to create new jobs or edit customer records offline, tell me and I'll rework this.
- Your mobile team can ship the 2-week estimate with the event-based parts logging included. If that adds more than a week, it is still the only option that fits.
