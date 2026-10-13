**Recommendation: ship the cached read-only jobs with offline completion forms (the 2-week option) for this release. Don't commit the team to the others on Monday.**

The deciding constraint is the calendar, not engineering effort. Every new app version goes through Harrowgate's IT review, which took eight weeks last time. With 11 weeks left, a build has to be submitted for review by about week 2 or 3 to reach crews' handsets before storm season. That leaves roughly a three-week build window, and only one option fits it.

| Option | Build | Build plus 8-week review | Fits in 11 weeks? | Other blockers |
|---|---|---|---|---|
| CRDT rebuild | 9 wks | about 17 wks | No | Auto-merge doesn't solve stock counts (see below) |
| Driftwell hosted sync | 3 wks | about 11 wks | Only with zero slack | Sends job data to a new sub-processor not in Harrowgate's contract schedule |
| Queue and replay | 5 wks | about 13 wks | No | None beyond the calendar |
| Cached jobs plus offline forms | 2 wks | about 10 wks | Yes, about one week spare | Parts-stock handling needs a decision (below) |
| Progressive web app | 6 wks | about 14 wks | No | Handsets have the browser disabled, so a PWA can't run on them at all |

**Why not the others now**

- **Driftwell** would need Harrowgate's contract schedule amended before any job data goes to it, and that is not something to plan around in 11 weeks. Even on the timeline it leaves no slack.
- **CRDT** is the wrong tool for the stock counts. Two crews on the same van can each draw the last unit while offline, and a CRDT merges both draws successfully, leaving the count negative and the billing wrong. That is a business-rule problem that merging can't fix. It also misses the window.
- **Queue and replay** is a sound long-term design, because the server validates each draw on replay. It is 13 weeks with review, though, so it belongs in the next release after storm season.

**What the two-week option needs before it's safe**

1. **Parts logging.** Offline draws against a shared van can overdraw stock and corrupt Harrowgate's cost-centre billing. For this release, I'd keep parts logging online-only and make everything else (job details, completion notes, photos, signatures) work offline. Confirm with Harrowgate that holding parts entries until signal returns is workable for their crews. If they need offline parts logging now, that requires an agreed reconciliation rule, which can't be designed responsibly in two weeks.
2. **Sign-in expiry.** Tokens expire after 12 hours and Harrowgate won't change that. The offline app should let technicians view cached jobs and fill in forms without a valid token. Queued uploads wait and sync after the technician signs in again on reconnect. Tell Harrowgate that a crew returning from a two-day outage will need to sign in before their work uploads.
3. **Offline queue storage.** Store unsent forms encrypted on the device, and delete them only after the server confirms receipt.
4. **Sub-processors.** This option keeps job data with the two parties already in the schedule, so no contract change is needed.

**What to do this week**

- Start the IT review conversation with Harrowgate now. Ask whether a pre-review or an expedited slot is possible, and agree a submission date. The margin is about one week, so the review is the main risk to the storm-season date.
- If the review slips past about week 10, there is no further fix inside this window. Be explicit about that with Sales and with Harrowgate now, so nobody is surprised.
- Put the queue-and-replay design on the roadmap for the release after storm season, with the review cycle built in. Rasmus's interest in a CRDT-style approach can be tested in that design, once the stock-count rules are settled.

**Assumptions**

- The 2-week and 9-week estimates are accurate and cover the work listed, including testing.
- Each new app version, including this one, needs the full 8-week review.
- Harrowgate's contract schedule lists only Quillmark and the current hosting provider.
- Crews will accept parts logging being online-only for this release. This is the assumption most likely to change the plan, so confirm it first.
