Pause the rollout now, hold the 16:00 launch email, and warn only the roughly 21,000 owners on 6.0. Don't Abort yet, and don't email all 210,000 customers.

**Why Pause and not Abort**
- Pause is fully reversible. It stops the 15:00 widening, so the problem stays at 10% of the fleet. You can resume or abort later.
- Abort is not reversible, and it carries a risk you've already seen. Your QA bench unit went from 6.0 to 5.8 and wouldn't boot until it was opened and reflashed by cable. Abort does that same downgrade to every lock on 6.0.
- If even a small share of those downgrades fail, you could turn about 21,000 locks that sometimes don't lock into some that are bricked. Many would need a physical repair.
- Abort is a bigger decision than Tomas's "now, find the cause tomorrow" suggests. It's one to make with the CTO and with evidence from a downgrade test. Pausing costs you nothing in the meantime.

**The 16:00 email and the "Update now" button**
- Pause only holds the staged rollout. Your "Update now" button and the app's "Check for update" install the newest published firmware at any stage.
- If 6.0 is the newest published build, the email would push it to up to 210,000 locks within hours. That is the bigger exposure.
- Before 15:00, find out whether Pause also blocks manual updates. Ask whoever owns the console and update server, which is probably Tomas.
- If it doesn't, have 5.8 re-marked as the current published version, or have manual installs of 6.0 disabled. Do whichever is fastest.
- Either way, tell Marketing now to hold the 16:00 email. Rescheduling a launch email costs almost nothing. Sending it costs a lot.

**Hanne's email**
- She's right that people need to be told. A bolt that stays retracted means an unlocked door, and that is a security problem.
- But only the 6.0 owners are affected. Emailing all 210,000 customers causes panic and a support flood among people who have nothing wrong.
- Send a targeted message to the 6.0 owners, and in-app if you can, as soon as the wording is ready. Use the earliest time you can manage rather than waiting for the evening.
- It should say that the motor may stall and leave the bolt retracted, so check that your door is actually locked and use the thumb-turn by hand if it isn't. It should say the update is paused and a fix is being worked on. It should not tell people to downgrade or reflash anything themselves.
- Give Hanne's team a short support script and ask her to draft the message.

**Timeline**

| Time | Action |
|---|---|
| By 14:35 | Press Pause. Confirm in the console that the 50% step is cancelled. |
| By 14:40 | Ask Tomas whether manual updates can still install 6.0, and how to stop that. Tell Marketing to hold the 16:00 email. |
| By 14:50 | Hanne sends you the draft message to 6.0 owners. Have Tomas check it for accuracy. |
| By 15:00 | Re-check the console. The rollout should still be paused and no widening should have happened. |
| 15:00 to 16:00 | Send the targeted message. Confirm the 16:00 email is held. |
| 15:00 onward | Tomas starts on the cause using the 160 tickets: firmware versions, lock hardware revisions, battery levels, and whether the stalls happen after fingerprint unlock. In parallel, test the 6.0 to 5.8 downgrade on several bench units across hardware revisions. |
| 18:00 | Brief the CTO and decide between Abort, a 6.0.1 hotfix, or staying paused. |

**Things to check**
- 160 tickets out of about 21,000 locks is under 1% of those on 6.0, but tickets undercount real failures. Ask Hanne how fast the count is rising since noon.
- The 160 reports may share a hardware revision or other trait. If they do, you may be able to block the update just for those locks instead of aborting everywhere.
- If tickets spike or you hear of a break-in tied to an unlocked door, escalate to the CTO by phone at once. Don't wait until 18:00.
- If the CTO or a deputy is reachable by message during the flight, send them a three-line summary now.

**Follow-up**
- Write up why the 5.8 reflash bricked the bench unit. This is the main thing blocking a safe rollback.
- Review why a firmware motor fault passed QA.
- Make the "Update now" button respect the rollout stage.
