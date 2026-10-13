Pause now, do not Abort, and stop the 16:00 email. Those three moves cover the next 35 minutes.

**Why not Abort (Tomas's plan)**
Abort pushes 5.8 onto about 21,000 locks that are already on 6.0. Your own QA bench unit shows what a 6.0 to 5.8 downgrade can do: it wouldn't boot and needed the case opened and a cable reflash. If that happens even occasionally across 21,000 locks, you turn a 160-ticket problem into dead locks on doors, with no remote fix. Abort can't be undone and you don't know the downgrade is safe. Keep it as a later option, only after engineering has tested the downgrade on real units.

**Why Pause is right**
It stops the 15:00 widening to 50%, so the affected group stays near 21,000 instead of reaching about 105,000. It is fully reversible: you can resume at any time. Locks already on 6.0 stay as they are, and the thumb-turn still works, so the failure is a door that doesn't lock, not a door that traps anyone.

**Do these in order**

1. **Now to 14:35: Pause the rollout.** Confirm in the console that it shows as held, and screenshot it. Don't wait for the CTO. This is reversible and clearly within your remit. Send them a text now so they see it when they land.

2. **By 14:45: Stop or hold the 16:00 marketing email.** This matters as much as the Pause. "Update now" and "Check for update" install the newest published firmware regardless of rollout stage. Pause doesn't stop them. A launch email to every customer would push 6.0 onto up to 210,000 locks, including people who never entered the rollout. Ask Marketing to postpone it. In parallel, ask engineering whether the console can pull 6.0 from the manual update path or pin that path to 5.8. If it can, do that as well. Until you have confirmed it, treat the email as blocked. If you have people who could trigger the in-app "Check for update", consider it as well: any in-app banner or push prompt should be held too.

3. **By 14:50: Get engineering on two questions.** First, what do the 160 affected locks have in common (hardware revision, battery level, cold temperature, a particular door type, or the fingerprint-unlock path)? Second, is a downgrade from 6.0 to 5.8 safe, and on which units? Ask Tomas to test it on a few bench units tonight, not on the fleet. His urgency is right, but the cause hunt can start now while the fleet stays untouched.

4. **By 15:00: Check that the Pause held, then decide on customer contact.**
   Hanne's instinct is right, but the audience is wrong. Only 6.0 owners (about 21,000) can have this fault. Emailing all 210,000 people tonight scares 189,000 customers whose locks are fine, and it will make the news. Send a short, targeted message tonight to the 6.0 group, by email and push: if the bolt stalls and the door doesn't lock, turn the thumb-turn by hand to lock it; check the door before going to bed or leaving home; here is how to reach support. Don't promise a fix date yet. Have Hanne review the wording and put a clear tag on these tickets so you can track the count.

5. **Before 15:30: Brief the people who need to know.** Support (a short script and the tag), Marketing (hold the email), and the CTO (a summary for when they land at 18:00: what you paused, what you held, what you decided not to do and why).

**What to do tonight and tomorrow**
- Watch the ticket count each hour. If it climbs fast, say 160 to 400 or more, you are looking at a wider fault and may need to push the message further, including a phone or push route for people who don't read email.
- With the CTO back at 18:00, decide on the remediation: a 6.0.1 fix built on the cause, or a tested downgrade for the affected group only. Whichever it is, roll it out in small stages, not all at once.
- Add a note to review afterwards: how a failure that stalls the motor passed QA, and why the downgrade path was never tested.
- The launch email can go out once there is a fix, with a new date.

**What you give up**
The 6.0 launch slips by days, and the fingerprint-unlock news waits. That is a marketing cost you can recover. A bricked fleet or a wave of unlocked doors is not.

Assumptions: you have the authority to pause and to hold marketing sends, and the Pause control behaves as described. If the console shows the rollout as "held" but the 50% step is still scheduled, treat that as not paused and escalate to engineering at once.
