**Short version: Pause now, do not Abort, stop the 16:00 email and the update button from reaching anyone else, and send a targeted notice to the ~21,000 locks on 6.0 only. Hold Abort until Tomas can show that 6.0 to 5.8 is safe.**

## Why not Abort (Tomas's plan)

Your own QA incident is the warning. A bench unit that was on 6.0 and got flashed with 5.8 would not boot and had to be opened and reflashed by cable. Abort does that same downgrade on about 21,000 locks you can't open. If the failure repeats even a few percent of the time, you've turned 160 doors that won't lock into thousands of dead locks that need hardware service. Abort is the one action here you can't undo, so it needs evidence first. Right now the evidence points the wrong way.

## Why not the all-customer email (Hanne's plan)

About 190,000 of those customers aren't on 6.0 and have no problem. Telling them to check their doors tonight will flood support and scare people who are fine. Hanne is right about one thing: affected owners need to hear tonight, because a door that won't lock is a real security problem.

## Do this, in order

**14:25 to 14:35. Pause the rollout.**
- This holds it at 10% and stops the automatic widening to 50% at 15:00, which is your hard deadline. It's fully reversible: you can resume later.
- Confirm on the console that it shows Paused, and screenshot it.

**14:35 to 14:50. Stop 6.0 reaching anyone else through the back door.**
- The "Update now" button and the app's "Check for update" install the newest published firmware regardless of rollout stage. Pause alone does not protect the other 90% of the fleet from those. Ask Tomas or whoever owns publishing whether 6.0 can be unpublished, or marked as not the latest, or the update path gated to staged cohorts. If yes, do it now.
- Tell Marketing to hold the 16:00 launch email, or at minimum remove the button. If you can't confirm the update path is closed, the email must not go. An email to every customer with an install button, after 160 tickets, is the biggest way this gets worse before 18:00.
- If neither can be done in time, make the email not send and ask Marketing to confirm that in writing.

**14:50 to 15:00. Get facts from the 160 tickets (Hanne's team, 10 minutes).**
- Do the affected locks share a hardware revision, a battery level, a door type, a region, or a prior firmware version? Did the stalls start at a certain time after update?
- Is 160 out of 21,000 (about 0.8%) still climbing? Since noon is about 2.5 hours, so check whether the rate is rising.
- Have Tomas look at motor-stall logs for those units. This is information gathering, not a root cause hunt.

**By about 15:30. Send a notice to 6.0 owners only.**
- Target the ~21,000 locks that took 6.0. Say plainly: the door may not lock after the update; check it tonight; the thumb-turn works by hand; you are looking into it; no action needed to stay on the current version; do not reinstall or reset the lock. Do not tell people to roll back themselves.
- Push the same message as an in-app banner to those users if you can.
- Give support a short script with the manual lock steps so tickets are fast.

**Get a decision on rollback while you wait.**
- Ask Tomas now: is 6.0 to 5.8 a supported downgrade? Does the bench failure come from a bootloader, partition or version-lock problem? Can he reproduce the downgrade on two or three bench units in the next hour? If the downgrade is safe, a staged rollback (a small batch first, never all 21,000) can happen tonight or tomorrow. If it isn't, the fix will have to be a 6.0.1 forward, and Abort stays off the table.
- If the rate of stalls climbs sharply before then, don't Abort unilaterally. Escalate to the CTO via whoever can reach them on the flight Wi-Fi or at landing, and tighten the owner notice.

## Decide this yourself, now

The CTO lands at 18:00, which is after your 15:00 deadline and after the 16:00 email. You can't wait. Pause is low-regret and reversible, and holding a launch email is low-regret too. Make those calls and note them. Don't let Abort or a mass email be decided under time pressure by default.

## Likely objections

- Tomas: "Stalling doors are a safety issue, abort fixes it." Reply: it fixes it for most units and bricks some, and the thumb-turn works by hand, so the interim risk is manageable with notice. Ask him to prove the downgrade is safe, which is faster than recovering from bricks.
- Hanne: "People may leave doors unlocked tonight." Reply: yes, which is why 6.0 owners get a notice tonight. The other 190,000 aren't exposed.

## Follow-up after 18:00

- Cause of the motor stall (Tomas): look at fingerprint-unlock timing, motor current limits and battery voltage, based on the shared traits of the affected units.
- Safe downgrade path or 6.0.1, and a rollback test on bench units before any fleet action.
- Fix the process gap: Update now and Check for update ignored staged rollout. The launch email should have been conditional on the rollout reaching 100%.
- Review QA: the downgrade failure was seen at sign-off and not treated as a blocker.
- Decide when the rollout resumes: only after the stall is understood and a fix or safe rollback exists.
