**Short version: press Pause now, not Abort. Stop the 16:00 email and the "Update now" / "Check for update" paths from pushing 6.0. Message only the roughly 21,000 owners on 6.0, not all 210,000. Have Tomas test the 5.8 downgrade on bench units before anyone presses Abort.**

## Why not Abort

Abort reinstalls 5.8 on every lock already on 6.0. Your own QA incident shows what that can do. A bench unit on 6.0 was flashed with 5.8, wouldn't boot, and had to be opened up and reflashed by cable. We don't know whether that was a one-off or a general problem with going from 6.0 back to 5.8. If it's general, Abort could turn about 21,000 locks that currently lock by hand into 21,000 locks that won't boot. Many of those locks are on doors, and the fix would be a cable reflash on each one. That can't be undone.

Pause is fully reversible. It holds the rollout at 10% and stops the automatic widening to 50% at 15:00. It gets you most of what Abort would, because the problem stops growing, and it doesn't carry the risk of bricking locks.

The cost of waiting is real but bounded. The 160 affected owners have bolts that stay retracted, so their doors don't lock. That is a security problem, but the thumb-turn works, so people can lock by hand. That is much better than locks that won't boot.

## Next 35 minutes

**Now to 14:35**
1. **Pause the rollout** in the console. Confirm it shows as paused, and confirm the 15:00 widening is cancelled.
2. **Stop the other routes to 6.0.** Pause doesn't touch them. The 16:00 "Update now" button and the app's "Check for update" both install the newest published firmware at any rollout stage. Find out who can do one of these before 15:00:
   - unpublish 6.0 as the newest version, or mark it not-latest, so those paths serve 5.8; or
   - if that isn't possible, hold the 16:00 launch email and turn off the "Check for update" install for 6.0.
   If nobody can do either by 15:00, tell marketing to pull the 16:00 email. The email is the largest risk to you, because it could put 6.0 on far more than 10% of locks in an hour.
3. **Ask marketing** to hold the 16:00 launch email until you say otherwise.

**14:35 to 15:00**
4. **Tomas runs the downgrade check.** On 3 to 5 bench units running 6.0, including ones from different hardware revisions or batches if he has them, install 5.8 the same way Abort would. Success means they boot and lock normally. He should also try to reproduce the stall on 6.0 and note anything the stalled locks have in common, such as hardware revision, battery level, door type or region, but that comes second.
5. **Hanne sends a targeted message.** Send it by email or push to the owners on 6.0, about 21,000, not to all 210,000. The other 189,000 are not on 6.0 and have nothing to check. Alarming them creates a support flood and no benefit. The message should say:
   - some locks on firmware 6.0 may not fully lock;
   - check that the bolt is extended, and if not, turn the thumb-turn by hand;
   - do this tonight and whenever they leave the house;
   - a fix is coming, and don't try to update or downgrade the lock yourself.
   If you can tell which owners are on 6.0, send to all of them. If you can only tell who has contacted support, send to those 160 first and widen as soon as you can.
6. **Support prep.** Give Hanne a short script and a macro: lock by hand, we're working on it, no action needed on the firmware.

**15:00 to 15:30**
7. Check that the rollout is paused and that no widening happened. Check the ticket count. If it keeps climbing quickly even with the rollout paused, that points to a wider problem in 6.0, such as something that appears over time, and makes the downgrade decision more urgent.

## The decision to make after the downgrade test

Fix a time for it now: Tomas reports at **15:45**, and you decide by **16:00**.
- **Downgrade is clean on every unit tested:** Abort becomes a reasonable choice. The best version is to wait for Tomas to confirm that, then abort. If you can, abort in batches or only on locks showing the stall.
- **Any unit fails to boot, or Tomas isn't sure:** stay paused. Do not abort. Keep the 160 owners on hand-locking and have Tomas build a 6.0.x fix that goes out to the 10% group, and if it's possible, have him build a safe rollback path.
- **Tests aren't done by 16:00:** stay paused. That is the safe default.

Neither answer needs the CTO. If Abort looks risky and you want a second opinion, send the CTO a three-line message now (paused, Abort risk, decision at 16:00) so they have it when they land at 18:00. Don't wait for them to start moving.

## What I'm assuming
- Pause really does stop the 15:00 widening and doesn't push anything new.
- You can tell which locks are on 6.0, and you can email or push to them.
- The bench unit that failed to boot was a straightforward 6.0 to 5.8 flash, not some mistake in how it was flashed. If Tomas knows it was a one-off, say so, and the Abort case gets stronger.

## Afterwards
- Find the root cause of the stall tomorrow. This is a good job for Tomas, and he can do it with the paused 10% group.
- Review why QA found the 5.8 boot failure and it didn't reach the Abort decision, so that rollback is tested before the next release.
- Make "Update now" and "Check for update" respect the rollout stage.
- Count the owners who had a door unlocked, and consider a goodwill gesture.
