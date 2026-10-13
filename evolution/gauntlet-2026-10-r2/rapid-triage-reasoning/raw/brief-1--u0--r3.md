**Short version: press Pause now, do not press Abort, hold the 16:00 email, and send a targeted warning (not a fleet-wide one) to the roughly 21,000 owners on 6.0.**

## Why not Abort (yet)

Abort pushes 5.8 onto every lock already on 6.0. Your own QA incident is the warning: a 6.0 unit that got 5.8 flashed on top wouldn't boot, and it took opening the case and reflashing by cable to recover. You have one data point that a 6.0 to 5.8 downgrade can brick a lock, and no time to find out whether that was a one-off. Abort could turn 160 locks that don't lock into up to 21,000 dead locks, some of them possibly needing a physical repair. It is also the one action you can't take back. Tomas's instinct to stop the spread is right, but Pause does that without the downgrade risk.

## Why not email all 210,000 tonight

About 189,000 of those customers aren't on 6.0 and can't have this fault. A fleet-wide "check your doors" email causes panic and a support flood, and it won't reach the people at risk any faster. Hanne's instinct to warn affected owners is right, though, because a bolt left retracted is a real security problem. Narrow it to the 6.0 owners.

## Do in this order

**Now to 14:35**
1. **Pause the rollout.** It's reversible and it stops the 15:00 jump to 50%. Check on the console that it shows "paused" and that the 50% step is no longer scheduled.
2. **Stop the 16:00 marketing email.** Its "Update now" button, like "Check for update" in the app, installs the newest published firmware whatever the rollout stage. Pause may not stop those paths, so the email would push 6.0 to anyone who clicks. Ask marketing to pull or postpone it now, and don't wait for the CTO.
3. **Close the same hole in the app.** Ask Tomas whether the newest-published pointer can be set back to 5.8, or 6.0 unpublished, without touching locks that already have it. If he can't confirm that within a few minutes, treat the in-app button as live. Add a banner or temporarily disable the update check, and tell support to warn anyone who asks.

**14:35 to 14:50**
4. **Ask Tomas for two quick answers instead of a full cause hunt.** (a) Do the failures cluster by hardware revision, motor type, door/temperature, or by an earlier firmware version? That gives you the affected slice. (b) Has anyone tested a 6.0 to 5.8 downgrade on spare units, and can it be done on 2 or 3 bench units tonight? Those answers decide the next move.
5. **Draft the warning to 6.0 owners** (see below) and have it ready to send by about 15:15, once you've confirmed who is on 6.0.

**15:00 to 15:35**
6. Confirm the pause held and no new locks took 6.0. Check whether the ticket rate is still climbing. If it's climbing faster than the share of locks on 6.0 would predict, tell support to put the warning first on their phone and chat scripts.
7. **Send the warning to everyone on 6.0**, not the whole fleet. Keep it short:
   - Some locks on the new firmware may fail to extend the bolt fully, so the door may not lock.
   - After locking, check that the bolt is extended, or turn the thumb-turn by hand. The thumb-turn still works.
   - Please don't update further. We're working on a fix. We'll email you again by [time tomorrow].
8. Give support a macro with that same text plus an escalation path for people who can't lock their door.

## Who decides what

You can make these calls alone: Pause, holding the email, and the targeted notice. They are reversible, and the CTO would almost certainly agree. Leave Abort or any downgrade for the CTO at 18:00, or for Tomas after the bench test, unless things get materially worse before then (for example, a lock that failed to lock then got broken into, or failures spreading beyond the current slice). Send the CTO a short message now so it's waiting when they land: what you paused, what you held, why you didn't abort, and the decision you need from them.

## What I'm assuming

- Pause keeps already-updated locks on 6.0 and doesn't move them back. If it does anything else, tell me and I'd change the plan.
- 160 tickets against about 21,000 locks is under 1%, but tickets are a lagging count, so the real number is higher.
- The "Update now" and "Check for update" paths ignore the staged rollout, as you described.

## Follow-up for tonight and tomorrow

- Find the root cause of the motor stall, using the hardware slice from step 4.
- Test the downgrade path on bench units before anyone uses Abort, and find out exactly why the bench unit wouldn't boot.
- Decide the fix path with the CTO: a 6.0.1 patch pushed to affected locks is probably safer than a downgrade, if the cause turns out to be simple.
- Fix the gap where the button installs the newest firmware regardless of rollout stage, so marketing emails can't bypass a staged release again.
- Reschedule the launch email only after the fix is out.

**If you only do three things in the next 10 minutes: Pause, stop the 16:00 email, and message the CTO.**
