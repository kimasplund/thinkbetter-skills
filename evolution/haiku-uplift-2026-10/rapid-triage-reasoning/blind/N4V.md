**Short answer:** Pause the rollout now. Pull 6.0 from the update feed and hold the 16:00 launch email. Test Abort on a few locks, then decide on Abort at 14:50. Do not email all 210,000 customers.

**Why not Abort right now:** Abort reflashes about 21,000 locks with 5.8. Your QA team has already seen a 5.8 flash that left a unit unable to boot until someone opened it and reflashed it by cable. Abort also may not fix the locks that are already stuck. Spend ten minutes proving it works first.

**Timeline**

- **14:25: Pause the rollout in the console.** This stops the automatic widening to 50% at 15:00. The 21,000 locks already on 6.0 stay where they are, and Pause is reversible.
- **14:27: Stop 6.0 from being served.** Remove 6.0 as the newest published firmware so that "Update now" and "Check for update" can only deliver 5.8. Confirm this with a test account or device. This is the one step that can push 6.0 to every customer without anyone choosing it, so it matters more than the email itself.
- **14:28: Hold the 16:00 launch email.** Its "Update now" button would otherwise install whatever is newest. Once the feed is fixed, the email is harmless, but it is better to hold it until the stall cause is known.
- **14:35: Test Abort.** Tomas should run Abort on one spare lock on 6.0 and, if the console can reach it, one stuck lock. Confirm the lock boots, the motor drives the bolt fully out and back, and the lock reports 5.8. Have the cable-reflash recovery path ready on a bench unit before any batch runs.
- **14:45: Customer message to the right people only.** Send a targeted email to the 6.0 owners from fleet data and to the 160 customers who filed tickets. Tell them the thumb-turn works. If the bolt is stuck retracted, they should turn the thumb-turn to throw the bolt and secure the door, and contact support if it still won't lock. Do not send the 210,000-customer blast. Most of those customers are not on 6.0, and the blast would create call volume and alarm without changing any door's risk. Confirm the ticket data really points only to 6.0 before sending.
- **14:50: Decide Abort.**
  - If the test is clean, run Abort in batches. Start with about 1,000 locks, watch boot failures and new stall tickets for 10 minutes, then run the rest.
  - If the test fails or the stuck lock doesn't respond, keep the rollout paused and plan field recovery for the stuck locks instead.
- **14:55: Leave a written decision for the CTO.** Record what was paused, what was pulled, whether Abort ran, and who holds Abort authority until 18:00. Tomas or whoever you name should own the decision if the stall rate rises.

**Quality floor for tonight:** No new locks get 6.0, the 15:00 widening is stopped, and every customer with a stuck bolt has a manual way to secure the door.

**Assumptions I made:** Pause freezes the rollout at the current 21,000 locks. You can change the firmware feed yourself. The stall is specific to 6.0. Abort can reach locks that are stalled.

**Follow-up (after tonight)**
- Find the motor stall cause in 6.0 (root cause analysis before any re-release).
- Explain why 160 tickets arrived before anyone paused the rollout, and add an alert or hold tied to ticket rate.
- Remove the automatic 15:00 widening, or make it require a sign-off.
- Add a guard so a bench or production unit cannot be flashed with the wrong version.
- Decide how the locks that stalled will be recovered, and whether 6.0 comes back at all.
- Brief the CTO at 18:00 with the 14:55 note.
