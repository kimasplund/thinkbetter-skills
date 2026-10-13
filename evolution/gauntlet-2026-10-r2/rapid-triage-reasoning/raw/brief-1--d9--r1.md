**Short version: Pause now, stop anything else from pushing 6.0 out, warn only the roughly 21,000 owners on 6.0, and don't Abort until someone has shown the 6.0 to 5.8 downgrade is safe.**

## Why not Abort yet
Abort reinstalls 5.8 on every lock already on 6.0, and that's about 21,000 doors. Your QA incident suggests a 6.0 to 5.8 flash can leave a lock that won't boot, and the fix there was opening the unit and reflashing by cable. That was one bench unit and I don't know the cause, but it's the only evidence you have about the downgrade path. If it generalizes, Abort turns a "door doesn't lock, thumb-turn works" problem into thousands of dead locks. You can't undo that. Pause can be undone. Tomas may be right in the end, but only once the downgrade has been checked.

## Why not email all 210,000
About 189,000 customers aren't on 6.0 and have nothing to check. A fleet-wide alert would flood support and scare people, and it would still miss the real risk (see the next section). Hanne is right on one point. A bolt that stays retracted is a security problem, so the 6.0 owners need to hear tonight. Send it to them only.

## The trap: Pause doesn't stop 6.0 spreading
The "Update now" button in the 16:00 launch email, and "Check for update" in the app, install the newest published firmware regardless of rollout stage. Pausing at 10% won't stop either one. Once the email goes out, tens of thousands of people could install 6.0 on their own. So:

- **Hold or pull the 16:00 marketing email.** Ask marketing now. This is the most urgent item after Pause.
- **Stop 6.0 being "the newest published firmware" for the self-serve path.** Ask Tomas whether you can unpublish it, or mark 5.8 as current for non-staged devices, without touching locks already on 6.0. If he can't do that, the email hold is your only protection, so confirm it in writing.

## Timeline

**Now to 14:35**
1. Press Pause. Confirm in the console that the 15:00 widening is cancelled. Don't wait for 15:00 to do this.
2. Message marketing to stop the 16:00 send, and get a yes back.
3. Ask Tomas to start on two things in parallel: (a) can the self-serve update path be blocked, and (b) test the 6.0 to 5.8 downgrade on several bench units, ideally ones that stall in the same way. Only the units in (b) can tell you whether Abort is safe.

**14:35 to 14:50**
4. Ask Tomas and Hanne for the facts that would change this plan:
   - Are the 160 stalls spread across hardware revisions, batches, temperatures, door types or battery levels, or clustered in one? A cluster means a narrower fix.
   - Is the stall transient, so that a retry or power cycle clears it, or does it persist?
   - Does a stalled lock report it to the backend? If it does, you can find affected locks directly.
   - Is the fingerprint feature itself the trigger? If it can be disabled remotely, that may be safer than a downgrade.
5. Draft the targeted message to 6.0 owners. Say plainly that the door may not lock, how to check (look at the bolt, use the thumb-turn to lock by hand), and that the fix is in progress. Do not tell them to uninstall anything. Have Hanne check it for tone and have someone check it for security-sensitive wording.

**14:50 to 15:00**
6. Send the 6.0-owner message (push notification and email) if Hanne and you agree. This is the right call even without the CTO, because the harm is physical and happens tonight. If you'd rather have sign-off, text the CTO now so a reply is waiting when they land.
7. Give support a short script and a way to tag these tickets, so you can count how fast they're growing. 160 tickets from about 21,000 locks since noon is roughly 0.8%, and I don't know how fast it's rising.

## Decision rules for later
- **If bench tests show the downgrade is safe and the stall is common or getting worse:** Abort, ideally in batches so a bad result shows up early.
- **If the downgrade fails or is unclear:** don't Abort. Keep the pause, push a 6.0.1 fix or a remote workaround, and rely on owner messaging until it ships.
- **If it turns out to be a narrow cluster:** target only those locks with a fix or a rollback.

## Assumptions
I'm assuming Pause really does stop all further staged pushes, that you have no way to remotely lock the bolt, and that the CTO can't be reached until 18:00. If you can reach them by satellite wifi or through a deputy, a two-line message is worth sending. Say that you paused, that you're holding the email, and that you're not aborting yet because of the downgrade risk.

## What I would do in your seat
In the next five minutes: press Pause, tell marketing to hold the email, and ask Tomas for a downgrade test on the bench. Everything else can follow from those three.
