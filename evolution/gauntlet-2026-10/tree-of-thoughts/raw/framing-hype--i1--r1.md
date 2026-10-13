Go with the 2-week option (cache the day's jobs read-only, let technicians fill in completion forms offline, upload later). It is the only one that reliably gets into Harrowgate's hands before storm season. Before Monday, I'd change what the team commits to, because the calendar is tighter than 11 weeks.

**The constraint that decides this: the IT review**

Every new version goes through Harrowgate's managed-catalogue review, and the last one took eight weeks. So the real build deadline is about week 3, not week 11. Anything that isn't built and submitted by then is unlikely to be on their handsets in time.

| Option | Build | Plus 8-week review | Verdict |
|---|---|---|---|
| Read-only cache + offline forms | 2 wks | 10 wks | Fits, with about a week of slack |
| Hosted sync (Driftwell) | 3 wks | 11 wks | Zero slack, and has a contract problem (below) |
| Queue and replay | 5 wks | 13 wks | Misses the deadline |
| CRDT data layer | 9 wks | 17 wks | Misses it by a wide margin |
| Progressive web app | 6 wks | n/a | Not viable: Harrowgate's handsets have the browser disabled |

**Why the faster-looking options don't work**

- **Driftwell:** Job data would flow through a third party that isn't in the contract's sub-processor schedule. That likely needs a contract amendment with your biggest customer, and their security team has already shown they're strict. Even if they agree, 3 weeks plus 8 weeks of review uses the whole window with no margin for a rejection or a resubmission.
- **CRDT rebuild:** It's the most elegant option, and I can see why Rasmus likes it, but it can't land in time. It's also a poor fit for the problem, because the hard case here is stock counts, not text merging (see below).
- **PWA:** Dead on arrival, since the browser is disabled on their devices.

**Two problems the plan must handle, whichever option you pick**

1. **Sign-in tokens expire after 12 hours, and crews can be offline for two days.** Harrowgate won't change that. The app has to let a technician keep working and recording data on the device after the token expires. Their work then uploads only after they sign in again on reconnect. So the app must not discard or reject data captured under an expired token. Design this with their security team now, because they may have views on how long locally stored data can sit unprotected on a handset. Encrypt the local store, and expect to explain that.
2. **Two technicians draw from the same van, each on their own handset, and Harrowgate bills from the counts.** If each phone writes "stock is now 14", the last upload wins and parts get lost from the billing record. Have the app record each part use as its own event ("used 2 of part X, at this time, by this technician, on this job") and let the server subtract them when they arrive. Never upload an absolute count. Two offline phones can legitimately drive a van's count below zero. Decide now what happens then, for example flag it for a dispatcher instead of rejecting the upload. Because cost centres are charged from these numbers, ask Harrowgate how they want discrepancies handled.

The event-style design costs almost nothing to build into the 2-week version. It is also exactly what the queue-and-replay option would need later, so nothing is wasted.

**What I'd commit to on Monday**

- Build the read-only cache plus offline completion forms and part-use logging as events, in about 2 weeks, and put it in front of Harrowgate's IT review as early as you can, ideally by the end of week 2 or 3.
- Contact Harrowgate's IT this week. Ask whether the review can be started early or expedited, whether it takes eight weeks every time, and whether smaller updates get a lighter process. This is the biggest risk in the plan and it's mostly out of your hands. Ask Harrowgate for their expected dates, since a repeat of the eight-week review leaves you only about a week of slack.
- Confirm with Harrowgate what crews actually need offline. This plan covers viewing the day's jobs and recording completions and parts used. It does not cover creating or changing jobs, or dispatcher reassignments, while they are out of signal. If a station is out of signal for two days, a dispatcher can't push changes to the crew anyway, but check that crews don't need to edit other things.
- Start the queue-and-replay work after the first release, as a second version for later in the year. If Harrowgate's review is slow, that is where the extra capability goes. The CRDT idea can be revisited then if you hit real multi-device conflicts.

**What I'd want you to check, because I'm assuming it**

- That the eight-week review time is typical and not an outlier, and that it starts at submission.
- That "completion forms offline" is what Harrowgate means by "the app working offline". If their crews need to open and update jobs more fully, the 2-week option is not enough, and you'd have to talk to them about phasing before storm season rather than hoping.
- That your own estimates of 2 and 3 weeks hold up. They come from a three-person mobile team, and a slip of a week or two on the 2-week option still fits. A similar slip on the other options does not.

I know this isn't the exciting option on the menu. But it's the one that gets offline mode working for your biggest customer on time, and it leaves you a base to build the richer version on afterwards.
