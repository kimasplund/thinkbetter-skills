**Recommendation: commit the team to option 4 (read-only cache of the day's jobs, offline completion forms, upload on reconnect). Build it so part usage is recorded as individual events rather than as a changed stock number. Ship that first, and treat the action queue as a later release.**

The deciding constraint is Harrowgate's IT review, not engineering effort. Every new app version goes through an eight-week review, and the last one took eight weeks. You have 11 weeks. A build that isn't submitted by about week 3 can't be live before storm season, however good it is. Your estimates only matter once you add the review time.

| Option | Build | Earliest live (build + 8-week review) | Verdict |
|---|---|---|---|
| Cache + offline forms | 2 wks | ~week 10 | Fits, with about a week of slack |
| Hosted sync (Driftwell) | 3 wks | ~week 11 | No slack, and a contract problem (below) |
| Action queue + replay | 5 wks | ~week 13 | Misses the date unless the review is shortened |
| PWA | 6 wks | n/a | Not possible: Harrowgate's handsets have the browser disabled and only install from the managed catalogue |
| CRDT data layer | 9 wks | ~week 17 | Misses by about six weeks |

**Why not the others**
- **PWA:** it can't run on those handsets at all.
- **CRDT rebuild:** Rasmus's instinct is sound as a long-term direction, but it can't ship in time. It also fits your stock problem poorly. Two technicians drawing from one van is a shared counter with a floor of zero, and automatic merging will happily produce a van with minus three filters. Harrowgate bills cost centres from those counts, so you want an explicit record of who used what, not a silently merged number.
- **Driftwell:** your contract limits processing of job data to the sub-processors in its schedule, which today is you and your hosting provider. Adding Driftwell means a contract amendment and probably a security review on Harrowgate's side, before or alongside the app review. With 3 weeks of build and 8 of review you'd have no slack at all, and the amendment sits outside your control. It also adds $24,000 a year and a dependency for your largest customer. Sales likes the speed, but the speed is lost to the review and the paperwork.
- **Action queue:** it is the best long-term fit for this problem. At 5 weeks it lands around week 13 if the review takes its usual eight, which is too late.

**What makes option 4 safe to commit to**
1. **Parts as events.** Record each part as "technician X used 2 of part Y on job Z at time T" and apply these to the van's stock when they upload. Don't send a new stock number. Two crew members logging offline against the same van then never overwrite each other, and the totals Harrowgate bills from stay correct. Decide now what happens if the sum goes negative: accept it and flag it for the van's owner to reconcile. Offline, the app can only show the stock as of the last sync, so tell technicians the number is approximate until they reconnect.
2. **The 12-hour token.** A two-day outage means the token will expire while the technician is offline. Don't make offline work depend on it. Let the app open and save forms offline behind the device's own lock, keep completed forms in encrypted local storage, and ask for a fresh sign-in on reconnect before uploading. Test this case first, because it is the most likely thing to fail in the field. Don't ask Harrowgate to change the token lifetime.
3. **Cache scope.** Cache the day's jobs plus whatever the technician needs to finish them: site details, part catalogue and the van's last known stock. Let them download the next day's jobs before heading out, since a two-day trip needs two days of data.
4. **Idempotent upload.** Give each form and each part event a unique ID generated on the device, so a retry after a dropped connection can't double-count stock.

**What to do on Monday**
- Commit to option 4 and set a hard internal date to submit to Harrowgate's catalogue by the end of week 2.
- Contact Harrowgate's IT team this week. Tell them a submission is coming, ask whether the review can be expedited given the storm deadline, and ask what they need in the package so it isn't bounced for missing documents. Review time is your biggest schedule risk, so it needs an owner. That owner can't be the mobile team.
- Aim to submit even earlier than week 2 if you can, and keep scope to the four items above. Anything added after submission means a new review.
- Start the action queue (option 3) straight after submission, with the same event model as its base. Aim to submit it for review by around week 7, so it can replace the form-based flow after storm season without another rewrite. Revisit the CRDT idea after that, once you have field data on how often crews actually conflict.

**What this doesn't give you.** Technicians can read the day's jobs and complete them offline, but they can't create new jobs or reassign work mid-trip, and dispatchers won't see progress until crews reconnect. For remote pumping stations with scheduled work, that is probably what Harrowgate needs. Confirm it with them on Monday, because it is the one assumption here I couldn't check. If they need to create jobs offline, the answer changes to the action queue and you would have to negotiate the review timeline.

**Confidence:** about 80%. The ranking is robust to the build estimates, because even if the mobile team is off by a week the other options still miss the date. What could change it is Harrowgate telling you the review can be much shorter, in which case the action queue becomes viable. The risk to this plan is the review running longer than eight weeks, which is why submitting early matters more than anything else.
