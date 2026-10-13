**Recommendation: go with the read-only job cache plus offline completion forms (2 weeks). Commit the team to it on Monday.**

**The deciding constraint is Harrowgate's app review, not build time.** Every option except the PWA ships as a new app version, and each new version goes through Harrowgate's IT review. The last review took eight weeks. You have 11 weeks. So the build has to be finished and submitted with about eight weeks left, which means the real build budget is roughly 3 weeks, with no slack at that figure.

| Option | Build | Submitted by | Cleared by (8-week review) | Verdict |
|---|---|---|---|---|
| Read-only cache + offline forms | 2 wks | wk 2 | wk 10 | Fits, with about 1 week of slack |
| Driftwell | 3 wks | wk 3 | wk 11 | Zero slack, and blocked by the contract (below) |
| Action queue + replay | 5 wks | wk 5 | wk 13 | Misses the season |
| PWA | 6 wks | n/a | n/a | Cannot run: the browser is disabled on their handsets |
| CRDT data layer | 9 wks | wk 9 | wk 17 | Misses by about 6 weeks |

**Why not the others**
- **Driftwell:** The contract limits job-data processing to the sub-processors in its schedule, which today is you and your hosting provider. Driftwell would be a new one. It needs Harrowgate's agreement and a contract amendment, which is a legal and procurement process you don't control, running alongside a review that already leaves no slack. Sales likes the speed, but the speed disappears once those steps are counted.
- **PWA:** The browser is disabled on the handsets, so it can't run there at all, whatever the estimate.
- **Queue and replay, and CRDT:** Both are better engineering for the long run and both land after storm season starts. The CRDT rebuild is also much more than this problem needs. Your merge problem is mostly stock counts, and those can be handled with simple additive adjustments. Rasmus's instinct isn't wrong as a direction. It is just a 2027 project.

**Design points that will bite if you skip them**
1. **Stock counts and the shared van.** Two technicians draw from one van on separate handsets. Don't upload "stock is now 14". Upload "used 2 of part X", each with a unique ID, and have the server apply those as decrements and ignore duplicates. Then two offline handsets can't overwrite each other, and Harrowgate's cost-centre billing stays accurate. Expect the count to dip below zero occasionally. Flag that for review instead of rejecting the upload.
2. **The 12-hour token against a 2-day outage.** A technician's token will expire while they're out of signal. The app must let them keep working and recording locally on an expired token. On reconnect they sign in again, and the app then uploads everything queued. The server has to accept uploads whose work happened before the new token was issued. Take this design to Harrowgate's security team now, since they own the token policy. You aren't asking them to change it, only to confirm that a deferred upload under a fresh sign-in is acceptable.
3. **Stale job data.** A read-only cache means a dispatcher may reassign or cancel a job while the technician is offline. On upload, detect that and send it to a dispatcher for resolution. Don't silently overwrite. Also show the technician when their data was last refreshed.
4. **Local data on the device.** Job data cached on the handset is still Harrowgate job data. Use encrypted storage and clear it on sign-out or after a set retention period. This is also something their IT review will probably ask about.

**What to do Monday**
- Scope the 2-week build tightly: cache the day's jobs, completion forms with parts used, an upload queue with idempotent IDs, and the expired-token flow. Nothing else.
- Aim to submit by the end of week 2, and have the same day-one conversation with Harrowgate's IT about the review. Ask whether a small, well-described update can go through an expedited path, and whether they'll take a pre-submission briefing. Shortening that review is the largest lever you have, and a single week lost anywhere uses up your slack.
- Tell Harrowgate plainly what winter-ready means: technicians can see their day's jobs and record completion and parts offline, with no live changes from dispatch while out of signal. If they expect two-way editing offline, that is the queue-and-replay option, and it can't make this season.
- Once this ships, start queue-and-replay as the next release, scoped for the next review cycle. Build the upload path from this release so it can carry over.

**Assumptions and risks**
- The eight-week review is the main risk. If this version takes the same eight weeks and you lose even a week to rework after review feedback, you miss the season. That is why the early IT conversation matters more than anything in the build.
- I'm assuming the 2-week estimate includes the token and stock handling above. If your team's number covers only the forms, ask them to re-estimate with those included before you commit. If it lands at 3 weeks, it still fits, but with no slack.
- I'm assuming that a review-free way to ship (for example a server-side change to the existing app) isn't available. If you have one, tell me, because it would change the answer.
- I'm assuming Harrowgate would accept a Driftwell amendment only slowly. If their procurement can turn one around in days, Driftwell is still a risk, because it also needs a full app update and has zero slack.
