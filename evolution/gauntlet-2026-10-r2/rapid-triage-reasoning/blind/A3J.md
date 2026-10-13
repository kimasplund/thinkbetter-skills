You have a workable plan. The short version: Pause now, don't Abort yet, stop the 16:00 email, and warn only the people on 6.0.

**Why not Abort (Tomas)**
Abort reinstalls 5.8 on every lock already on 6.0. Your own bench unit shows what that downgrade can do: it flashed 5.8 over 6.0 and wouldn't boot until someone opened it and reflashed it by cable. If that happens to even a few percent of 21,000 locks, you've turned a stalled-bolt problem into a pile of dead locks that need hands-on repair. You can't undo that. Abort is the one irreversible control you have, so don't use it until someone has shown the downgrade path is safe. That might be the right call later. It shouldn't be a blind call made in the next 30 minutes.

**Why not email all 210,000 (Hanne)**
About 189,000 of those customers aren't on 6.0 and can't have this fault. A fleet-wide "check your doors tonight" alarms them for no reason, and it will flood support. The people at risk are the roughly 21,000 on 6.0. Reach them directly instead.

**What to do, in order**

1. **Now to 14:35: press Pause.** It's fully reversible and it stops the 15:00 widening to 50%, which would take the problem from about 21,000 locks to about 105,000. This is the one thing that has to happen before 15:00. Pause only holds the rollout, though. It may not stop anything else (see step 2).

2. **By 14:45: stop the 16:00 marketing email.** Hold it or pull the "Update now" button. The button and the app's "Check for update" install the newest published firmware whatever stage the rollout is at. So even a paused rollout can be bypassed, and a launch email to every customer could push 6.0 onto most of the fleet within hours. Ask Tomas whether the console can unpublish 6.0 or move the "latest" pointer back to 5.8 so those buttons stop offering 6.0. I'm assuming Pause doesn't do that. If nobody can confirm either way, treat the buttons as live and keep the email held.

3. **By 14:55: warn the 6.0 owners only.** Use app push and email to that group, not the whole customer base. Keep the message short:
   - Some Wren locks on firmware 6.0 may not fully lock.
   - Check the bolt after locking.
   - If it stays retracted, lock it by hand with the thumb-turn.
   - We're working on a fix.
   Give support the same wording and a one-line script so tickets get consistent answers. This is a lock, so the real risk is a door left unlocked overnight. That's why the warning shouldn't wait for tomorrow.

4. **By 15:30: get a read on scale.** 160 tickets out of about 21,000 is under 1%, but tickets lag and understate. Ask Tomas to pull any telemetry on motor stalls from the 6.0 locks, and check whether the tickets share a hardware revision, a door type or a battery level. Ask support to tag every new ticket. This tells you whether it's a small subset or the whole 6.0 population.

5. **By 18:00 (CTO lands): bring one clear decision.** Send the CTO a short message now with what you've done. Then the decision for 18:00 is whether to Abort, ship a fix, or keep paused. Before anyone presses Abort, Tomas needs to test the 6.0 to 5.8 downgrade on several spare units, including the exact path the bench unit failed on. If the downgrade is safe, Abort becomes a reasonable choice. If it isn't, you hold at Pause, warn owners, and push a 6.0.x fix.

**Things to write down as you go**
- The time you paused, who did it, and what you told customers.
- Whether the "Update now" button was actually blocked. Confirm this rather than assuming.
- The open question of how the downgrade bricked a bench unit. This is a separate risk from the stalling bug, and it affects every future rollback.
- The root cause of the stall. It's tomorrow's work, and nothing above depends on it.

**What you're giving up**
- 6.0 owners stay on the buggy firmware until a fix or a safe rollback exists. The hand-lock warning covers the gap.
- The launch slips. That's cheap compared with unlocked doors.
- If the numbers at 15:30 look much worse than 160 tickets, move the Abort test up and tell the CTO.

If you only have time to do two things before 15:00, do steps 1 and 2.
