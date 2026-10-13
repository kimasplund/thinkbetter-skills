**Recommendation: commit on Monday to the two-week option (cache the day's jobs read-only, let technicians complete forms offline and upload them later), and submit the first build to Harrowgate's IT review in week 2.** Here is why, and what has to be true for it to work.

**Why the others don't fit**

- **Timing is the binding constraint, not build time.** Every new app version goes through Harrowgate's eight-week IT review, and you have eleven weeks. Anything that needs a new app version live before storm season has to be in review by about week 3, with no slack. Counting from Monday, the CRDT rebuild (9 weeks) reaches the handsets around week 17 and the queue-and-replay approach (5 weeks) around week 13, before any allowance for testing. Neither makes it. Only the two-week version can be in review by week 2 and still leave a margin.
- **Progressive web app: not viable.** The handsets have the browser disabled and only install apps from Harrowgate's managed catalogue, so a PWA cannot run on them at all.
- **Driftwell: blocked by the contract, not by engineering.** The contract limits processing of job data to the sub-processors in its schedule, which lists only you and your hosting provider. Driftwell would be a new sub-processor, so it needs a contract amendment and Harrowgate's sign-off before go-live, plus IT review as a new integration. The three-week estimate is not the real timeline, and it adds about $2,000 a month.
- **CRDT rebuild: right direction eventually, wrong for this deadline.** The hard problem here is van stock counts and billing, which must be exact and shared by two handsets. CRDT merging makes concurrent edits converge, but it cannot enforce a rule such as "stock cannot go below zero" or give you a clean audit trail for billing. That logic belongs on the server regardless, and the rebuild would still have to pass the review.
- **Queue-and-replay: the natural next step, not this release.** Once the two-week version is live, replaying individual queued actions against the API is a sensible follow-on. It is a later release with its own review, so it should not go into the storm-season build.

**What has to be true for the two-week version**

1. **The offline cache covers the whole outage, not just today.** Crews can be out for up to two days. Cache the next two days of assigned jobs, plus the forms, parts lists and van stock those jobs need.
2. **Offline work must not depend on a valid sign-in.** Tokens expire after 12 hours, and Harrowgate will not change that. Technicians must be able to open the cache and fill in forms with no token. The upload queue must survive token expiry on the device. On reconnect, the app asks for sign-in and then uploads. Test this directly: a outage longer than 12 hours, then reconnect, must lose no data.
3. **Uploads must be safe to retry.** If a connection drops mid-upload, a retry must not double-count parts. Give each form a device-generated ID and have the API upsert on it.
4. **Stock counts will be late, and they can go negative.** Both crew handsets draw from the same van, and the counts do not update until upload. Two technicians could log the same part while offline. The API should accept every logged use with its real timestamp and flag any stock that drops below zero, rather than reject work already done in the field. Agree with Harrowgate now how late-synced usage is billed to their cost centres, because that is the number they care about.
5. **Be explicit about the read-only limit.** Dispatch changes made during an outage will not reach the technician until reconnect. Tell Harrowgate this before they see the build.
6. **Get the data-handling position in writing.** Caching job data on the handset is processing on the device rather than a new hosted sub-processor, but legal should confirm that against the schedule before the review submission. The cache must be cleared on sign-out.

**Actions this week**

- Ask your mobile team to confirm that the two-week estimate includes the upload queue, the token handling, retry safety and the stock-flag logic. If any of those are missing, the real figure is higher and the week-2 submission date moves.
- Ask Harrowgate whether their IT review can start on a pre-release build, or be fast-tracked given the storm date. Do not plan on a yes, but ask.
- Get legal's answer on the sub-processor question in writing, so the Driftwell question is closed for this release.

**Assumptions**

- Parts usage is logged on the completion form. If it is entered separately, the two-week version needs that flow too.
- Server-side API changes do not go through the app review, as only app versions are described as doing so.

**For Rasmus:** the CRDT rebuild is a sound long-term direction for multi-device editing, but the problems on this contract are exact stock counts, billing and a slow app release cycle. The server handles those better, and the CRDT path cannot ship before winter. Position it as phase two, after the storm-season release.
