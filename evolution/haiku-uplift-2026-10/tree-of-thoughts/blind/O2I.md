**Recommendation: commit the team to option 4, the read-only job cache with offline completion forms, starting Monday. It is the only option that can plausibly reach Harrowgate's handsets before storm season.**

**The deciding constraint is Harrowgate's IT review, not build time.** Every new app version goes through an 8-week review, and your last one took exactly that. You have 11 weeks, so the app has to be submitted for review within about 3 weeks. Here is what each option looks like against that:

| Option | Build | Plus 8-week review | Fits in 11 weeks? | Other blockers |
|---|---|---|---|---|
| CRDT data layer | 9 wks | 17 wks | No | Also the riskiest rewrite |
| Driftwell hosted sync | 3 wks | 11 wks | Zero slack | Driftwell is not a listed sub-processor. Using it breaks the contract until Harrowgate agrees to amend the schedule, and that is a second approval on the same critical path. |
| Queue and replay | 5 wks | 13 wks | No | |
| Offline cache and forms | 2 wks | 10 wks | Yes, with 1 week spare | |
| PWA | 6 wks | n/a | No | Harrowgate's handsets have the browser disabled, so it cannot run there at all. |

Driftwell is the closest runner-up, and it is what sales will push. It has no slack, and it needs a contract amendment. Harrowgate's security team has already shown it won't bend on tokens, so I wouldn't bet the date on them adding a vendor. If the amendment came through quickly it would still only match option 4's timeline, at a monthly cost and with a new vendor holding job data.

**Option 4 only works if you design four things up front.** They are small, but they are where it would otherwise fail.

1. **Parts and van stock.** Two technicians share one van and each logs parts offline. If each handset uploads "stock is now N", the second upload overwrites the first and Harrowgate's cost-centre billing is wrong. Instead, send each part use as its own record with an ID generated on the handset, and have the server subtract it from the van count. Duplicate uploads are then harmless, and two handsets can't clobber each other. Expect van counts to go briefly negative or stale until both phones sync. Decide now how the console shows that, and tell Harrowgate's billing contact.
2. **Sign-in.** Tokens expire after 12 hours and crews can be out for 2 days, so a token will often be dead when they reconnect. Decide with Harrowgate's security team, this week, how an offline session works. Two likely shapes: the app unlocks locally with the handset's existing PIN or biometric, then re-authenticates on reconnect, and the server accepts the stored forms only after that fresh sign-in. The 12-hour rule stays untouched, but they have to agree to the shape. Also confirm that unsent completion data stored on the phone must be encrypted at rest.
3. **Conflicts.** A dispatcher may reassign or cancel a job while a technician is out of signal. Keep it simple: on upload, the server accepts the completion, flags the job for dispatcher review if it was changed in the meantime, and never silently drops a technician's work.
4. **Duplicate work.** Pairs share jobs. Either allow only one completion form per job (second one flagged) or merge them in the console. Pick one.

**What technicians lose:** they can read the day's jobs and file completions offline, but they can't take on new jobs, edit assignments or see live changes until they have signal. For pumping-station work, where the job list is known in the morning, that is probably acceptable. Check this with a Harrowgate crew lead before Monday, because it is the one assumption the whole plan depends on.

**Schedule that protects the date:**
- **Weeks 1 to 2:** build the cache, forms and upload with the part-record design above.
- **End of week 3 at the latest:** submit to Harrowgate IT. Use week 3 for testing with airplane mode and a 48-hour dead-token scenario.
- **Weeks 4 to 11:** review. Ask their IT team now whether they can pre-review or fast-track a small change, since the clock matters more than the code. Ask whether a staged or pilot release to one crew is allowed. Any slip in the review beyond 8 weeks costs you the date, and there is no fallback that is faster.

**Rasmus and sales.** Both have a fair point, and the plan gives each something. Rasmus's CRDT merge is a good long-term answer to the two-handset stock problem, but at 9 weeks plus review it can't ship this winter. Schedule it as the next release after storm season, using what you learn from real offline use. Queue and replay (option 3) is the sensible step in between. Sales gets a clear message for Harrowgate: offline completion is arriving before storm season, and fuller offline editing follows.

**Open questions, in order of risk:**
1. Will Harrowgate IT's review really be 8 weeks again, or can it be shortened?
2. Will their security team accept the offline sign-in shape?
3. Can crews work from a morning job list?

If the answer to the first is "longer than 8 weeks", nothing you can build will fix that. Escalate to Harrowgate immediately, because it affects the date more than any engineering choice.
