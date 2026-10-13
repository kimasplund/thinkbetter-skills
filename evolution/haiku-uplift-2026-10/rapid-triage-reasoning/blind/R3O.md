Here is a plan for the next 35 minutes. I can't see your systems, so I've listed the assumptions I'm making at the end.

**The biggest gap: Pause alone does not stop the update path.** The 16:00 launch email and the app's "Check for update" both install the newest published firmware, whatever the rollout stage. If 6.0 is still the newest published version at 16:00, you will push 6.0 to locks outside the 10% cohort, and the stall problem spreads. So the first two actions are about the update path, not only the console.

**14:25 to 14:30: Pause the rollout now.** This stops the automatic widening to 50% at 15:00. It does not reverse anything. Locks already on 6.0 keep their current state. Do not Abort yet (see below).

**14:30 to 14:35: Stop the 16:00 email and the "Update now" path.**
- Ask marketing to cancel or hold the 16:00 launch send. If they can't cancel it, ask them to remove the "Update now" button.
- Unpublish 6.0 as the newest firmware, or make sure 5.8 is the newest published version, so "Check for update" stops offering 6.0. Confirm with Tomas that setting 5.8 as newest won't trigger unintended downgrades on locks that are already on 5.8.

**14:35 to 14:45: Give support a holding script for the 160 tickets.** If the bolt stays retracted, the door is unlocked. Tell customers to secure the door with the thumb-turn by hand, and to avoid the app's auto-lock until the fix is announced. Ask support to tag each ticket with the lock's firmware version and serial range, so you can confirm the 6.0 cohort is the only one affected.

**14:45 to 14:55: Tomas and QA check Abort before anyone runs it.** The bench incident is the warning sign. A 5.8 image flashed onto a 6.0 unit left it unable to boot. Before a fleet-wide Abort reinstalls 5.8 on every 6.0 lock, test that exact path (6.0, stalled motor, reflash to 5.8) on a bench unit. If it can brick a stalled lock, Abort is more dangerous than the stall.

**14:55 to 15:00: Decide.**
- If the bench test shows 5.8 reinstalls cleanly from a stalled state, Abort is the right fix. Run it on the 6.0 cohort, but expect field visits for locks that stalled hard.
- If it doesn't, keep the rollout paused, keep the update path closed, and push a targeted support and hardware fix plan instead.
- Either way, the rollout must not widen at 15:00. Confirm that the console shows it paused.

**Do not email all 210,000 customers tonight.** Most of them are not on 6.0 and have no symptom. A mass message would cause panic, flood support, and probably drive more people to the update button. Instead, send a short message only to the roughly 21,000 locks on 6.0 (or the subset with tickets). It should cover the stall symptom, the thumb-turn workaround, and "do not update the app until we say so." Hanne can draft it now and send it after the decision at 15:00.

**Before 18:00, brief the CTO** with: rollout paused at 10%; update path closed; 160 tickets since noon; Abort decision and bench result; customer message status; and the time of the next decision point (suggest 17:00).

**Assumptions:**
- Pause stops widening but leaves locks already on 6.0 running.
- You can unpublish or change the newest published firmware quickly.
- The 5.8 reinstall path is the same one used by Abort, so the bench test covers it.
- The 160 tickets are all 6.0 owners, as your message states.

If you tell me which of these are wrong, I can rework the plan.
