Short answer: one option is defensible, the read-only cache with offline completion forms (2 weeks). Your doubts about the rest are justified, but the reason isn't the one you gave. The constraint that decides this is Harrowgate's app review, not engineering effort.

**The deadline is really about 3 weeks of build time, not 11**

Every new version of the app goes through Harrowgate's IT review, and the last one took eight weeks. Their handsets can't run a browser or install from anywhere else. So the real arithmetic is build time plus about 8 weeks of review, against 11 weeks:

| Option | Build | + 8 weeks review | Verdict against 11 weeks |
|---|---|---|---|
| Read-only cache + offline forms | 2 wks | 10 wks | Fits, with about a week of slack |
| Hosted sync (Driftwell) | 3 wks | 11 wks | Zero slack, and has a contract problem (below) |
| Action queue and replay | 5 wks | 13 wks | Misses winter |
| PWA | 6 wks | n/a | Dead: the browser is disabled on their handsets |
| CRDT data layer | 9 wks | 17 wks | Misses winter by a wide margin |

Rasmus's CRDT idea fails on schedule alone, however interesting it is. The PWA fails outright, because it needs the one thing their handsets don't allow.

**Why Driftwell is out even though it looks fast**

Your contract limits job-data processing to the sub-processors in its schedule, which today is you and your hosting provider. Driftwell would be a third one. That means a contract amendment with Harrowgate, and likely a security review of Driftwell, before any job data touches it. Their security team has already shown it doesn't move quickly. Even if everything went well, 3 weeks plus 8 weeks of review leaves no margin, and the amendment can't be done in parallel with certainty. Sales is right that it's fast, but the speed doesn't survive contact with the contract.

**Why the action queue is more dangerous than it looks (even if time weren't a problem)**

- Two techs in a pair log parts against the same van's stock count. If each queues "decrement stock" actions for up to two days and replays them later, the count can go negative or end up wrong. Harrowgate bills its cost centres from those counts, so errors become invoice disputes.
- Tokens expire after 12 hours and won't be extended. A two-day offline stretch means every queued action replays with an expired token, so replay has to wait for a fresh sign-in and handle partial failures.
- Those are solvable, but they're the reason 5 weeks is probably optimistic.

**What I'd commit to on Monday**

Option 4, with these guardrails, because they are what make it safe rather than merely quick:

1. **Cache the day's jobs read-only** at the start of shift. Accept that a dispatcher's mid-day changes won't reach a tech who is out of signal.
2. **Completion forms are saved as records, not live edits.** Give each record a client-generated ID so uploads are idempotent if a retry happens.
3. **Log parts as deltas ("used 2 of part X"), never as an absolute stock count.** Two handsets in one van then add up correctly when they sync, because the changes commute. Have the server flag a van that goes negative for human review rather than rejecting the upload.
4. **Leave the 12-hour token alone.** Offline use after expiry should be gated by the device lock plus a local session, and uploads should wait for a fresh sign-in on reconnect. Check that design with Harrowgate's security team now, since they own that rule.
5. **Cut scope hard.** Anything that needs a network round trip, such as live reassignment or messaging, stays online-only for this release.

**Start the review clock early**

Your slack is about one week, and the review is out of your hands. So this week, before Monday if possible, ask Harrowgate's IT how to get on their review schedule, whether a small scoped release can be fast-tracked, and what they need in the submission. Submit the 2-week build the day it is done. If their review takes longer than last time, nothing on this list rescues the date, so that conversation matters more than any estimate your team can give.

**What it won't do**

This is not true sync. Crews get a read-only picture of the day and a reliable way to record what they did, which covers the two-day outage scenario. It will not handle jobs changing underneath them while they are offline. I'd tell Harrowgate that plainly now rather than at delivery.

Design the data model so a later release can grow into queued actions: client IDs and delta-style records cost almost nothing now. Each later release goes back through their review, so plan that increment for after winter, not before.

**What I assumed**

- The 8-week review is roughly typical and applies to any new version, not just major ones.
- Your estimates are accurate and the three developers can start Monday.
- Completion forms and part logging are the offline-critical actions. If crews also need to create new jobs offline, tell me, because that changes the picture.
