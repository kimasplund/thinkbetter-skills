**Recommendation: commit Monday to the 2-week option (cached jobs, offline completion forms), built so the offline data is a durable log of events, not a snapshot. Submit it to Harrowgate's IT review as soon as it's built. Treat the full action queue as phase 2.**

The deciding constraint is the review, not the build time.

## Why the calendar decides this

Harrowgate's managed catalogue is the only way onto their handsets, and the last review took eight weeks. You have 11 weeks. Working backwards, the build must be finished and submitted about 3 weeks from now, and that assumes the review takes no longer than last time.

| Option | Build | + 8-week review | Verdict |
|---|---|---|---|
| Cached jobs + offline forms | 2 wks | 10 wks | Fits, with about a week of slack |
| Driftwell | 3 wks | 11 wks | Zero slack, and a contract problem (below) |
| Action queue | 5 wks | 13 wks | Misses the season |
| PWA | 6 wks | n/a | Impossible: their handsets have the browser disabled |
| CRDT rebuild | 9 wks | 17 wks | Misses the season by about 6 weeks |

Things that rule options out regardless of timing:

- **PWA:** it needs a browser, and the browser is disabled on their handsets. It's dead on arrival, not just slow.
- **Driftwell:** it would be a new processor of Harrowgate's job data. Their contract limits that to the listed sub-processors, which today are you and your hosting provider. You'd need a contract amendment and Harrowgate's sign-off, and that clock would run in parallel with the review. The $2,000 a month is minor next to that. You'd also still need an app update to integrate it, so it still goes through the review.
- **CRDT rebuild:** it's the most elegant option and the worst fit for the deadline. It also doesn't solve your two hardest business problems (stock counts and token expiry, below). Rasmus's instinct is sound as a long-term direction, but it can't be what ships this winter.

## What "2 weeks" has to include for this to work

Harrowgate's real issues are the shared van stock and the 12-hour tokens. Design for those from day one.

**1. Parts usage as append-only events, not a stock count.**
Two technicians drawing from the same van while both are offline will each have a stale count. If handsets write "stock = 14", one write silently overwrites the other. Instead, each handset records "used 2 × part X, job J, technician T, time, unique ID". On upload the server applies these as deltas, and the unique ID makes retries safe (no double-decrement). Two handsets' deltas add up correctly in any order.

- Make the event log the source of truth for Harrowgate's cost-centre billing, and derive the count from it.
- Don't reject an event that would take stock below zero, because the part has already physically left the van. Accept it and flag it for a stock reconcile.

**2. Work offline past the 12-hour token.**
Crews can be out for two days, so the token will expire mid-trip. The app must keep working on cached data and record events under the identity that was signed in at the time, with a local unlock such as PIN or biometric. When signal returns, the user signs in again and the app then uploads. Don't make upload depend on the old token still being valid.

This needs a yes from Harrowgate's security team, because it touches the policy they set. Ask this week. If they say no, no option delivers two-day offline work, so you want to know now.

**3. Dispatcher changes during an outage.**
Decide the rule now: the server's assignment wins. A completion that arrives for a job that was reassigned or cancelled is accepted and flagged for the dispatcher, not dropped. Technicians' field data shouldn't be silently lost.

**4. Encrypted storage on the device.**
Job data cached on the phone stays within your existing processing arrangements, so no new sub-processor is involved. It still needs to be encrypted at rest.

## What this option does not give them

- Technicians can't create new jobs offline. They also can't see their partner's updates or dispatcher changes until they reconnect.
- It covers what a crew does on a job (view, log parts, complete, add notes). If Harrowgate's definition of "works offline" is broader than that, find out in your next call.

That is the trade-off: this is the least capable option, and the only one that can realistically be live before the storms.

## What to do on Monday

1. **Start the build.** Aim to finish and submit at the end of week 2.
2. **Contact Harrowgate's IT contact now.** Tell them a submission is coming in about two weeks, ask what the review needs (test build, documentation, security questionnaire), and ask whether a small, scoped update can be expedited. Their answer on timing is the single biggest risk to the plan. If you can't get a commitment of 8 weeks or less, tell Harrowgate's sponsor early, because no option on your list fixes that.
3. **Ask their security team about the token point above.**
4. **Plan phase 2.** Once the first release is submitted, build the full action queue (create and edit actions offline, replay on reconnect) on the same event log and ID scheme. It's about 5 weeks, and it reuses the work from this release. It can go into a later review slot after the storm window. If you later want a CRDT-style data layer, the event log is a sensible foundation for it.

## Remaining uncertainties

- **The review time.** I'm assuming eight weeks again. A faster review gives you room to add scope. A slower one means any option misses the date.
- **How broad Harrowgate's offline requirement is.** I'm assuming viewing jobs, logging parts, completing, and adding notes is enough for the winter season.
- **The security team's answer** on offline use past token expiry.
- **Whether your three developers can really deliver in 2 weeks.** I'd hold the scope tight and resist adding queue features to this release, since every extra week eats the slack.

I'm fairly confident in this recommendation. The calendar and the disabled browser rule out most of the list, and the remaining choice is about how much to put in the first release. The open risks are all outside your code: the review time and the security sign-off.
