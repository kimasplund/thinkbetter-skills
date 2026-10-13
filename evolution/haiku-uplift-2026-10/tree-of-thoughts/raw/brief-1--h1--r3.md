**Recommendation: commit Monday to option 4 (read-only cache of the day's jobs, plus offline completion forms), extended slightly so parts usage is logged as queued events. Ship it in about 3 weeks. Don't start the CRDT rebuild or the PWA.**

**The constraint that decides this is Harrowgate's app review.**
- The last review took 8 weeks and you have 11. A build that reaches their managed catalogue after about week 3 will probably miss storm season.
- That leaves room for one reviewed release, with little slack for a rejection or a resubmission.
- The 5-week, 6-week and 9-week options can't make it, however good they are technically.

**Why the other options fail**
- **PWA (6 weeks):** Harrowgate's handsets have the browser disabled and only install from the managed catalogue. It can't run there.
- **CRDT rebuild (9 weeks):** it misses the review window. It also solves the wrong problem. Merging concurrent edits isn't the hard part here. Stock counts are, and a CRDT counter can still go negative or disagree with what was physically taken from the van. Rasmus's instinct is sound as a long-term direction, but it can't be the winter answer.
- **Queue and replay (5 weeks):** it is the right architecture, but at 5 weeks plus 8 weeks of review you land at week 13 or later.
- **Driftwell (3 weeks):** the timing works, but the contract only permits processing job data by the sub-processors listed in its schedule, which today means you and your hosting provider. Adding Driftwell needs a contract amendment with Harrowgate, and likely their security review too. That's your largest customer, and you'd be asking for it on the critical path. It also doesn't remove the app review. Don't commit to it unless Harrowgate agrees in writing this week.

**Make option 4 cover what Harrowgate actually needs.**

1. **Sign-in tokens expire after 12 hours and crews can be out for 2 days.**
   - Let the technician unlock the cached data locally with a device PIN or biometric, with no server token needed.
   - Store completions locally, and require a fresh sign-in on reconnect before anything uploads.
   - Don't try to extend the token lifetime, because their security team has said no.
   - Check with Harrowgate that locally cached job data on the handset is acceptable. It should be encrypted at rest.
2. **Parts and stock.** Two technicians in one van each log parts on their own handset, and Harrowgate bills cost centres from those counts.
   - Don't upload an absolute count. Log each part as an event ("used 2 of part X on job Y by tech Z at time T").
   - Give each event a unique ID so retries can't double-count.
   - Have the server apply the events as decrements on reconnect.
   - Treat a van going below zero as a flag for review, not a rejection. The part was physically used.
   - This is a small extension of option 4, roughly one extra week. Your team should confirm that.
3. **Conflicts.** Dispatchers may reassign or change a job while a technician is offline. For v1, record the technician's completion and flag a changed or cancelled job to the dispatcher on sync rather than silently overwriting.

**Timeline**
- Weeks 1 to 3: build and internal test, including a real airplane-mode test with two handsets sharing one van's stock.
- Week 3: submit to Harrowgate's IT review. Ask them now whether an expedited review is possible, since their own storm-season deadline depends on it.
- Weeks 3 to 11: review, plus a buffer. Use the time to build the proper queue-and-replay layer (option 3) for a second release.

If the review runs the full 8 weeks, approval lands around week 11. That is tight, so the expedite request is the most important thing to start on Monday.

**Assumptions**
- The estimates from your mobile team are accurate.
- The 8-week review applies to any new version of the app.
- Technicians mainly need to see their jobs, complete them and log parts, not create or reassign jobs offline. If crews must edit jobs freely offline, the answer shifts toward queue-and-replay and the timeline gets very tight.

**Monday message to the team:** "We're shipping offline-read plus completion forms with event-based parts logging, submitting to Harrowgate review by week 3. Queue-and-replay follows as release 2. No CRDT or PWA this cycle."
