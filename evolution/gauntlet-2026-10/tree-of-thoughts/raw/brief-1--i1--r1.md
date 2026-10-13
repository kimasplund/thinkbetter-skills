**Recommendation: commit the team on Monday to option 4, the read-only cache of the day's jobs plus offline completion forms uploaded later.** Build it so the forms are stored as a queue of discrete, idempotent actions. That way it can grow into option 3 after storm season without a rewrite.

## Why the calendar decides this

Your build estimates are not the real constraint. Harrowgate's IT review is. Every new app version goes through it, and the last review took eight weeks. You have 11 weeks, so whatever you ship has to be built and submitted in about three weeks, and then it has to clear review.

| Option | Build | Plus 8-week review | Fits in 11 weeks? |
|---|---|---|---|
| CRDT data layer | 9 wks | 17 wks | No |
| Queue and replay | 5 wks | 13 wks | No, unless review is under 6 weeks |
| Progressive web app | 6 wks | n/a | No. Their browsers are disabled and it can't go in the managed catalogue |
| Driftwell hosted sync | 3 wks | 11 wks | Zero slack, and blocked by the contract (see below) |
| Cached jobs plus offline forms | 2 wks | 10 wks | Yes, with about a week of slack |

Two further problems rule out the other options.

- **Driftwell** is not on the contract's sub-processor schedule, which today lists only you and your hosting provider. Job data would flow through a third party. You would need Harrowgate to amend the schedule, which is a legal and procurement exercise that won't finish in the weeks you have. Even if they agreed, a 3-week build leaves no margin for review. Sales likes the speed, but the speed isn't real here.
- **CRDTs** are also a poor fit for the data. The van stock count is a bounded resource that two technicians draw on at once. Automatic merging will converge on a number, but it can't stop the count going negative, and Harrowgate bills its cost centres from that count. This is a business-rule problem that merge semantics don't solve. Rasmus's instinct about the long-term architecture may be right, but it can't ship this season. Treat it as a separate decision for later.

## What to build in the 2 weeks, and the traps to design around

1. **Stock: send deltas, not totals.** Offline, record "part X used, quantity 1" as an event with a unique ID, and don't write a new count. The server applies events as decrements when they upload. Two technicians drawing from the same van then add up correctly in any order, and replays can't double-count. If the van goes below zero, flag it for a dispatcher to reconcile instead of silently rejecting the upload. Billing then stays correct to the unit. Show technicians a local stock estimate, clearly labelled as "since last sync".
2. **The 12-hour token will expire mid-outage.** Crews can be out for two days, so assume the token is dead for most of that time. Let the app open and keep working offline behind a local device unlock (the handset's PIN or biometric), with no server check. Queued items are authenticated when the technician signs in again after reconnecting, and the server should attribute each item to the user who recorded it. This doesn't change Harrowgate's token policy, but their security team should still confirm it is acceptable. Get that confirmation in week 1. Also confirm that the cached job data is encrypted at rest on the device.
3. **Cache enough to be useful.** Pull the day's jobs, site details and van parts list at sign-in, ideally with a refresh the night before. Crews going to a remote station should be told what hasn't been cached.
4. **Make uploads idempotent.** Every form and stock event carries a client-generated ID, and the server ignores duplicates. This is the piece that makes the later move to a full queue cheap.

## What to do on Monday and in week 1

- Ask Harrowgate IT for the review timeline for this specific release. Ask whether it can be a smaller or expedited review, since it adds no new data flows or third parties. Every week you gain here is slack.
- Aim to submit by the end of week 3 at the latest. Plan the build as 2 weeks, with the remaining time for testing in realistic dead zones, including a two-day airplane-mode run with two handsets on one van.
- Be clear with Harrowgate and with sales about what this delivers. Technicians can see their day's jobs and complete them offline. They can't create jobs or see other changes dispatchers make during an outage. The dispatcher console will lag until sync.

## What this doesn't give you, and what's next

Anything that changes jobs on the device mid-outage, such as reassignments or edits, waits for the later version. Because of the review cycle, a queue-and-replay release started right after this one (5 weeks build plus 8 review) would land around week 15, which is after the season starts. Tell Harrowgate that now, so it is a planned phase two and not a surprise. If their review turns out to take 5 to 6 weeks, queue-and-replay becomes feasible. In that case, start it in parallel using the same idempotent-event design.

## Assumptions and what would change my answer

- **The 8-week review applies to every release**, including small ones. If Harrowgate can turn a small release around in 2 to 3 weeks, queue-and-replay moves into reach, and so does a staged plan with the forms first and the queue second.
- **Offline completion alone meets what Harrowgate asked for.** I'm assuming "work offline" means technicians can finish their jobs and log parts without signal. If they need to receive new or changed jobs mid-outage, that is a different requirement, and you should find that out this week.
- **Your estimates are right.** The 2-week figure is the least risky of the five, but add a few days of buffer for the stock-event and auth work above, because that is where the hidden effort is.
- The decision is firm for this season. After the season, decide between queue-and-replay and the CRDT rebuild on evidence from real field use.
