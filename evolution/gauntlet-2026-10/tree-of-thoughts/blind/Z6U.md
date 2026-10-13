**Go with option 4, the read-only job cache plus offline completion forms, and don't commit the team to anything bigger on Monday.** It's the only option that clearly lands before winter storm season. The deciding constraint is Harrowgate's app review, not engineering effort.

## The deadline is really about 3 weeks

Every new version of your app goes through Harrowgate's IT review, and the last one took eight weeks. You have 11 weeks, so the build has to be submitted to their catalogue by about week 3. Add each estimate to the review:

| Option | Build | Plus 8-week review | Verdict |
|---|---|---|---|
| CRDT data layer | 9 wks | 17 wks | Misses by 6 weeks |
| Action queue and replay | 5 wks | 13 wks | Misses by 2 weeks |
| Progressive web app | 6 wks | 14 wks | Misses, and it can't work (see below) |
| Driftwell hosted sync | 3 wks | 11 wks | Zero slack, plus a contract problem |
| Read-only cache plus forms | 2 wks | 10 wks | One week of slack |

Your estimates will also slip, and the review can slip too. Only the last row survives that.

## Why the other four fail

- **CRDT rebuild:** It misses the deadline by a wide margin. It also fixes the wrong problem. A CRDT merges edits to shared documents, but your hard data problem is a van's stock count, and merging two offline decrements automatically can still leave a negative count that Harrowgate bills from. Rasmus's enthusiasm is understandable. It's a reasonable thing to plan for next year, not for this deadline.
- **Progressive web app:** Harrowgate's handsets have the browser disabled and only install from their managed catalogue, so a PWA can't run on the devices that matter. It also needs a review.
- **Driftwell:** Three weeks is attractive, but your contract limits processing of job data to the sub-processors in its schedule, which is you and your hosting provider. Driftwell would be a third. You'd need Harrowgate's legal and security teams to agree to an amendment before any real job data touches it. That is a separate approval process on top of the app review, and it is outside your control. Sales liking the speed doesn't change that. Even if the amendment came through, the timeline has no room left.
- **Queue and replay:** This is the best long-term design of the bunch, but 5 weeks of build puts you at 13 weeks with the review.

## Two design points to get right in the 2-week build

These are the traps in the context you described, and a cheap option can still fail on them.

1. **Stock counts.** Two technicians draw from the same van, each offline for up to two days. If the app uploads "the van now has 14 of part X", the second upload overwrites the first and billing is wrong. Have the forms upload what was used ("used 2 of part X, technician A, job 123, at this time"). The server then applies those as decrements. Add a way to flag a van that goes negative, so someone reconciles it instead of a bad number flowing into Harrowgate's cost-centre billing.
2. **The 12-hour tokens against two days offline.** A technician's sign-in will expire while they're out of signal, and Harrowgate won't change that. The app must keep working on the device after expiry. That means no forced logout when the token lapses offline, and uploads that wait until the technician signs in again on reconnect. Check this with Harrowgate's security team early. They need to be comfortable with cached job data sitting on the handset for up to two days with an expired token, so ask about device encryption and local-unlock requirements now.

Also cache more than "the day's jobs". With two days out of signal, cache at least the next three days of assignments for that technician. Job forms should be keyed by job and technician, so both crew members can complete their own parts without colliding.

## What you give up, and what to say to Harrowgate

Technicians can't edit jobs offline, create new ones, or see dispatcher changes made while they're out of range. Before Monday, put one question to your Harrowgate contact: is read-only jobs plus offline completion forms and parts logging enough for crews at the pumping stations? If the real need is editing jobs in the field, you need to know now. I'd guess completion and parts logging are the core of it, but I'm assuming that.

## What I'd do this week

1. **Monday:** commit the team to option 4, with a target of submitting the build to Harrowgate's catalogue in about 2 weeks.
2. **Today or tomorrow:** ask Harrowgate's IT whether you can open the review early. For example, submit a pre-release, get the review checklist in advance, or find out what made the last review take eight weeks. If a reviewer can look at your security approach in parallel with development, your slack grows.
3. **Keep the bigger option for later.** Once this version is in the catalogue, queue-and-replay can follow as the next release, and it will also go through the 8-week review. Reuse the usage-based stock upload design so the follow-up isn't a rewrite.
4. **Tell Rasmus and Sales plainly.** The review cycle is why the fancier and faster-sounding options don't work, and that has nothing to do with their quality. The CRDT can be a post-storm-season project if you still want it.

This approach is less exciting than the others. It gives you the best chance of keeping Harrowgate, 40% of your revenue, happy before winter.
