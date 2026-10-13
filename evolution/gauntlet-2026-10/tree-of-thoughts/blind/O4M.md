**Recommendation: commit to the 2-week option, cached jobs plus offline completion forms. Add one thing to it: part usage must be logged as individual events, not as a stock number the phone overwrites. Submit that build to Harrowgate's IT review by the end of week 2, and treat week 3 as the hard latest.**

**Why the review decides this**

Every new app version goes through Harrowgate's IT review, and the last one took eight weeks. You have 11 weeks. So the date that matters is when you can submit a build, not when the feature is "done". The latest submission date that still lands before storm season is about week 3.

| Option | Build time | Earliest approved (build + 8 weeks) | Fits 11 weeks? |
|---|---|---|---|
| Cached jobs + offline forms | 2 wks | week 10 | Yes, about 1 week of slack |
| Driftwell | 3 wks | week 11 | Zero slack, and a contract problem (below) |
| Action queue + replay | 5 wks | week 13 | No |
| PWA | 6 wks | n/a | No: their handsets have the browser disabled and only install from the managed catalogue |
| CRDT data layer | 9 wks | week 17 | No |

Only the 2-week option leaves any margin. Rasmus's CRDT rebuild is probably a good long-term architecture, but it would reach the crews around week 17, in the middle of the season it was meant to cover.

**Driftwell has a second problem**

Harrowgate's contract limits processing of job data to the sub-processors in its schedule, which today is you and your hosting provider. Driftwell would be a new sub-processor handling their job data. That needs a contract amendment and probably a security review on their side, and the review clock for the app starts only after the build exists. It also still ships inside a new app version, so it gets no shortcut on the 8 weeks. It would need legal sign-off to even start, and sales can't promise that.

**Make the 2-week option hold up in the field**

Your context has three details that a plain offline-forms build would get wrong.

1. **Stock counts.** Two technicians draw from the same van on separate handsets, and Harrowgate bills its cost centres from those counts. If each phone caches "stock = 40" and uploads "stock = 37", the second upload overwrites the first and the billing is wrong. Instead, each part logged offline should be an event: a client-generated unique ID, van, part, quantity, technician, and device timestamp. The server applies the events as decrements and ignores any ID it has already seen, so a retry can't double-count. Show the cached van count as an estimate while offline. When the totals go negative or don't match a physical count after sync, flag them for review rather than silently correcting them. Decrements add up in any order, so you don't need a CRDT for this.
2. **The 12-hour token against two days offline.** The token will have expired by the time a crew reconnects, and Harrowgate won't extend it. So don't depend on it offline. Let the app open and accept entries on the device using the phone's own lock, store each entry with the technician's identity, and require a normal sign-in on reconnect. The server then accepts uploads under that fresh sign-in but records the original technician and timestamps. Confirm this with Harrowgate's security team this week. You aren't asking them to change the token lifetime, only to accept that entries are captured offline and authenticated at upload. If they say no, you need to know in week 1, not week 9.
3. **Stale jobs.** A job can be reassigned or cancelled by a dispatcher while a crew is out of signal. Decide up front what happens when a completion arrives for a job that has changed. The simplest rule is to accept it, mark it as a conflict, and send it to a dispatcher queue. Have the app show how old the cached data is, so crews and dispatchers aren't misled.

**What you give up**

Technicians can't create new jobs offline, can't see changes dispatchers make during the outage, and can't reassign work between the two handsets in a pair. For pumping-station visits, working a known list of jobs and recording what was done and what was used covers most of what Harrowgate is likely asking for. Check that with them, because "works offline" may mean something broader to them than it does to you.

**Next steps**

- **Monday:** commit the team to this scope and freeze it. Any feature added later costs another 8-week review, so anything you'd regret leaving out has to go in this build or wait until after the season.
- **This week:** tell Harrowgate's IT contact the review submission date now and ask whether they can run a lighter or faster review for a build like this. Also ask them to confirm the token approach above. Neither costs you anything, and either answer could change your plan.
- **Week 2 (week 3 at the latest):** submit the build. Plan to use the slack for review questions and resubmissions, not for new features.
- **After the build is submitted:** start the queue-and-replay or CRDT work as the follow-up release. It would reach Harrowgate through a later review cycle, which suits it better as a post-season upgrade than a storm-season dependency.

**Where this could be wrong**

- If Harrowgate's IT will review a build much faster than eight weeks, the 5-week queue option becomes possible and gives crews more. Only they can tell you.
- If their security team won't accept offline entry under an expired token, none of the offline options work as written. This is the first thing to check.
- I assumed the 8-week review is typical and not a one-off. If the next one takes longer, even the 2-week option is at risk, which is why I'd submit as early as you can.
