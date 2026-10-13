**Recommendation: commit to option 4 (read-only cache of the day's jobs, plus offline completion forms uploaded later). Treat it as phase 1 of a larger plan, and start the Harrowgate IT review conversation today.**

**Why the deadline is really about the review, not the build**

Your last Harrowgate IT review took eight weeks. If the next one does too, you have about 3 weeks of the 11 to build and submit. A build that isn't through the managed catalogue by storm season doesn't exist for their crews. That decides most of this:

- **CRDT rebuild (9 weeks):** Ruled out. Nine weeks of build plus an eight-week review is about 17 weeks.
- **Operation queue and replay (5 weeks):** Ruled out on timing, about 13 weeks. It is also the best phase 2, see below.
- **Progressive web app (6 weeks):** Ruled out regardless of timing. Their handsets have the browser disabled and only install from the managed catalogue, so a PWA can't run there.
- **Driftwell (3 weeks):** Ruled out for two reasons. Its build time leaves no slack for the review. It also adds a sub-processor that handles job data, and your contract limits that to the schedule (you and your hosting provider). Adding one needs a contract change and Harrowgate's agreement, which probably can't happen in time. The $2,000 a month is not the problem.
- **Option 4 (2 weeks):** The only option that fits. Even so, it is tight: 2 weeks of build plus 8 of review is 10 of your 11 weeks.

**What to do about the review risk (this matters more than the choice of design)**

1. Contact Harrowgate's IT and your champion there today. Ask for an expedited or parallel review, and say it is for their own storm-season readiness. Ask what the review actually checks, since a small, low-risk change may qualify for a lighter path.
2. Keep the change small and avoid new permissions, new network endpoints and new third-party SDKs. A small diff is the best lever for a faster review.
3. Submit as soon as it is feature-complete, not when it is polished. Get an early build to them before week 2 if you can.
4. Say plainly to Harrowgate and to Rasmus that the eight-week review is the schedule risk. If the review can't be shortened, nothing on this list ships in time, and Harrowgate needs to know that now. Interim measures could include paper or another fallback process for the first storms.

**Design points that will bite you even in the simple option**

- **Sign-in expiry (12 hours, fixed by their security team):** Crews can be out for two days, so tokens will expire while offline. The app must let a technician keep working and recording locally with an expired token. Uploads then need a fresh sign-in on reconnect. Don't ask for a way around the policy. Store pending forms in encrypted local storage, tied to the signed-in user, and have the server check the user's identity at upload time. Confirm this approach with Harrowgate's security team early.
- **Van stock counts (two handsets, one van):** Two technicians logging parts offline will both decrement from the same count. Send parts as "used N of part X on job Y" records, not as an absolute stock number. The server applies them as deltas on upload, so the order doesn't matter and nothing is overwritten. Be ready for a stock count to go negative after sync. Flag it for review rather than rejecting the upload, because Harrowgate bills cost centres from these counts. Decide the rule for this with them.
- **Duplicate and late uploads:** Give each form a client-generated unique ID so retries can't double-count parts.
- **Stale jobs:** A dispatcher may reassign or cancel a job while a crew is offline. Show clearly in the app that the data was cached at a given time, and define what happens when a completed form comes in for a job that has since changed.

**Phase 2, after storm season starts**

Build the operation queue and replay (option 3) on top of the same local storage and the same delta and unique-ID design. It lets technicians create and edit jobs offline, not just complete them. This also gives Rasmus a staged path. If the CRDT is still the long-term goal, revisit it then, once you know how often real conflicts happen. The two-person-per-van pattern may turn out to need only counters and last-writer-wins for the rest.

**What to tell the team on Monday**

- Scope: cached jobs, offline completion forms, parts logged as deltas, unique IDs, and offline behaviour with expired tokens.
- Target: build-complete and submitted to Harrowgate's IT within 2 weeks.
- Owner: someone (probably you) is responsible for the review conversation, separately from the build.
- Phase 2 (queue and replay) is planned but not promised for this season.

**Assumptions I made:** the 8-week review time is typical and applies to any new version, including a small one; Harrowgate's crews mostly need to view jobs and record completion and parts rather than create jobs offline; and a contract amendment for Driftwell isn't achievable in a few weeks. If Harrowgate's IT will do a fast review, say a week or two, the ranking is unchanged, but you would then have room to build the queue-and-replay option instead.
