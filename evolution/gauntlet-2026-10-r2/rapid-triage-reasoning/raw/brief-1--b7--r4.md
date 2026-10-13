**Short version: press Pause now, not Abort. Stop the 16:00 email (or its button). Warn only the roughly 21,000 owners who are on 6.0, not all 210,000. Then run a quick bench test to decide whether Abort is safe.**

**1. Pause now (14:25-14:30).**
- Pause holds the rollout at 10% and stops the automatic widening to 50% at 15:00. You can undo it with one click, so it costs almost nothing.
- It doesn't help the locks already on 6.0. That's fine for now, because the thumb-turn still works by hand and you have time to decide about those.

**2. Don't hit Abort yet.**
- Abort sends 5.8 to every lock on 6.0, about 21,000 of them. It can't be undone once it starts.
- Your own QA incident is the warning. A unit that was on 6.0 and got flashed with 5.8 wouldn't boot, and it took opening the case and reflashing by cable to recover it. Nobody yet knows whether that was a one-off mistake or whether a 6.0 to 5.8 downgrade is unsafe in general.
- If it is unsafe, Abort could turn 160 stalling locks into thousands of dead locks on front doors. Those would need hardware recovery.
- Tomas's instinct to roll back is reasonable. But the cost of being wrong is large and can't be reversed, while waiting 30 minutes costs little because the rollout is paused.

**3. Run the downgrade check by 14:55.**
- Ask Tomas and QA to find out exactly how that bench unit failed. Was it a plain OTA-style downgrade or a manual flash? Is there a version-rollback restriction or a bootloader or settings-format change in 6.0?
- At the same time, have them downgrade two or three bench units from 6.0 to 5.8 through the same path Abort uses.
- If the downgrades boot and work, Abort is safe. Press it at about 15:00 and you're done with the rollback.
- If a unit fails to boot, or you can't tell, leave the rollout paused and don't Abort. Tomas should then start on a 6.0.1 fix, and support should handle the affected locks individually.
- If neither answer is clear by 15:00, stay paused. A pause can wait until the CTO lands at 18:00.

**4. Fix the 16:00 email.**
- The "Update now" button and the app's "Check for update" install the newest published firmware regardless of rollout stage. So Pause does not protect the other 189,000 locks from 6.0. Anyone can pull it in themselves, and the 16:00 email would push tens of thousands of people toward it.
- Ask marketing to hold the email now. If they can't hold it, they should strip the button or the 6.0 mention.
- Also ask engineering today whether 6.0 can be un-published, or marked as not-latest, so that the in-app check serves 5.8. That closes the same hole for anyone already in the app.

**5. Warn only the 6.0 owners, and do it now rather than tonight.**
- Hanne is right that people with a lock that won't latch need to know. But 90% of your customers are on 5.8 and have no problem. A 210,000-person "check your doors" email would alarm them for no reason. It would also drive people into the app, where "Check for update" would install 6.0.
- Send a push notification and email to the roughly 21,000 on 6.0 this afternoon. Say the bolt can sometimes stall and stay retracted, and tell them to check the door is actually locked and to turn the thumb-turn by hand if it isn't. Add that a fix is coming, and give a support link.
- Keep the wording plain and say nothing about the cause, since you don't know it yet.
- Have Hanne's team prepare a macro for the 160 existing tickets and anyone who writes in after the notice.

**6. Hand over to the CTO at 18:00 with:**
- the ticket count and how it has changed over time (160 since noon is about 0.8% of 6.0 locks),
- the downgrade test result,
- whether the email was held, and whether the rollout is paused or aborted.

**Follow-up for tomorrow:**
- Find the cause of the motor stall. Check whether it clusters by hardware revision, battery level, door type, or temperature.
- Decide on a fix (6.0.1) or a rollback, based on the test result.
- Add a rule so the "newest published" button respects the rollout stage.
- Add a downgrade test to the release checklist.
- Check that the pause threshold on failure tickets is set low enough to catch this sooner next time.
