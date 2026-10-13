**Recommendation: commit the team to option 4, the read-only job cache with offline completion forms, uploaded later.** It is the only option that can ship before winter storm season. Build it so the part-logging data is safe to merge, which I cover below.

## The deciding constraint is Harrowgate's review, not build time

Every new app version goes through Harrowgate's IT review, and the last one took eight weeks. You have 11 weeks. So the real test is whether the build is finished and submitted early enough for review to end before storm season.

| Option | Build | + 8-week review | Fits in 11 weeks? | Other blockers |
|---|---|---|---|---|
| CRDT data layer | 9 wks | 17 wks | No, by 6 weeks | Largest rewrite, highest risk |
| Driftwell hosted sync | 3 wks | 11 wks | Zero slack | Driftwell is a new sub-processor. The contract limits job-data processing to you and your host, so you would need a contract amendment from Harrowgate first. |
| Action queue and replay | 5 wks | 13 wks | No, by 2 weeks | Ordering and conflict handling for stock |
| Read-only cache + offline forms | 2 wks | 10 wks | Yes, 1 week spare | Needs the design points below |
| PWA | 6 wks | n/a | No | Harrowgate disables the browser on its handsets, and the PWA would also be a new app version. It cannot run there at all. |

Three of the options fail on arithmetic alone. Driftwell fails twice: it lands exactly on the deadline, and it needs a contractual change that Harrowgate has no reason to rush. Your sales team likes its speed, but the data-processing clause makes it a bet on a legal approval you don't control.

You also get one release, not several. Anything you want in the storm-season version has to be in the first submission. "Ship the small thing, then iterate" doesn't work when each iteration costs eight weeks of review.

## Three design points that make the simple option safe

**1. Stock counts must merge as changes, not as overwrites.** Two technicians share a van and both log parts offline, possibly for two days. If each handset uploads "stock is now 14", the second upload erases the first. Have each completion form upload "used 3 of part X" with a unique ID, and have the server apply it as a subtraction. Duplicates are ignored, so retries can't double-bill. Counts can go briefly negative or low. That is acceptable if the console flags it for reconciliation rather than rejecting the upload, because Harrowgate bills its cost centres from these numbers. This is the same problem a CRDT would solve, and for a plain decrement counter it needs one server rule, not a rewrite.

**2. Plan for the 12-hour token expiry.** After a day or two without signal, the sign-in token will have expired, and the security team won't change that. The app must let a technician keep working and saving forms offline without a valid server token. Uploads must happen only after a fresh sign-in on reconnect. Offline access needs a local unlock, such as the device PIN or biometrics, and the data on the handset must be encrypted. Ask Harrowgate's security team now whether that design is acceptable. A surprise from them during review would cost you the window.

**3. Accept that cached jobs go stale.** If a dispatcher reassigns or cancels a job while a crew is out of signal, the crew won't know. Show a "last synced" time on every screen. On upload, have the server accept the completion and flag any conflict for the dispatcher to resolve. That is manageable with pairs working different jobs, and you can describe it to Harrowgate honestly.

## How to run the next 11 weeks

- **Weeks 1-2:** build the cache, the forms, the delta-based stock upload and the offline unlock.
- **Submit to Harrowgate's review by the end of week 3 at the latest.** That leaves one spare week. Open the conversation with their IT team on Monday, before you have a build, so they can schedule the slot and raise concerns early. Ask whether a narrow, offline-only update can get a faster track.
- **While review runs:** harden, test with real signal loss, and prepare a rollout plan with Harrowgate. You can keep working on the next version, but it won't reach their handsets before the storms.
- **After storm season:** queue-and-replay is the natural second release if crews need to edit assignments or see live data offline. You'll have real usage data to say whether it's needed. I would not start a CRDT rebuild on this evidence.

## Talking to Rasmus and sales

- **Rasmus:** the CRDT idea isn't wrong, but nine weeks plus review misses the date by six weeks. For a stock counter, an ID-keyed delta gets you the same safety.
- **Sales:** tell Harrowgate that crews can complete jobs and log parts with no signal, and sync when they return. Don't promise live offline editing of assignments.

## What could still change this

- **If Harrowgate's review is faster or slower than eight weeks,** the margin changes. At ten weeks you have no spare time, so the early submission matters more. Confirm the likely duration this week.
- **If crews must receive new jobs or change assignments while offline,** a read-only cache won't be enough. I assumed they only need to work the day's jobs and fill in completion forms, as in your description.
- **If Harrowgate's security team rejects offline access with a local unlock,** the whole plan needs rethinking. That is why I would ask them first.

Your fallback is also your plan: do the 2-week option well, submit early, and use the remaining time on testing rather than on features.
