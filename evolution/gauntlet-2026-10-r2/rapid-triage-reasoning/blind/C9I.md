**Short version: Pause now, not Abort. Stop the 16:00 email, or at least its button. Warn only the roughly 21,000 locks on 6.0. Hold Abort until the downgrade path is proven safe.**

**14:25-14:35: contain it**
1. **Hit Pause in the rollout console now.** Don't wait for 15:00. This stops the auto-widening to 50% and costs nothing. It's reversible, and it stops the problem from growing.
2. **Stop the 16:00 launch email, or remove the "Update now" button.** This is the biggest hidden risk. That button and the app's "Check for update" install the newest published firmware whatever the rollout stage. Pause doesn't stop them. The email would push 6.0 to up to 210,000 locks in an hour. Call Marketing now and have them hold the send. If the email must go, it needs to go with no button and no 6.0 mention.
3. **Also stop the app from offering 6.0.** If your release tooling can unpublish 6.0 as "latest" or pin the latest to 5.8 for non-cohort locks, do that too. Ask Tomas whether it's possible. If not, the email hold is your only protection, so confirm Marketing has actually held it.

**14:35-14:50: get facts in parallel**
- **Tomas:** Don't abort yet. The bench incident suggests a 6.0 to 5.8 downgrade can leave a lock unbootable, and one lock had to be opened and reflashed by cable. Abort would run that path on about 21,000 locks at once. If it bricks even a small share, you'd have many dead locks, on top of the failed bolts you have now. Ask him two things. Is the downgrade safe, and was the bench failure specific to that unit? And can he find the cause fast? Look for a common factor among the 160 tickets: hardware revision, battery level, temperature, door type, or install date.
- **Tomas:** Have him test Abort's downgrade on a few internal units (5 to 10) now. This is the evidence that decides whether Abort is an option.
- **Hanne:** Pull the ticket data. How many distinct locks are affected, and what share of the 21,000 is that? Also check the failure rate before and after noon, and whether it's growing. 160 tickets means a lower bound on affected locks, since many owners won't write in.
- **Hanne:** Get the failure confirmed as "stalls and leaves the bolt retracted". That means the door is unlocked, which is a security problem, not just an annoyance.

**14:50-15:00: decide**
- **If the downgrade tests clean and the failures keep climbing:** Abort is justified, but do it as a staged rollback, not all at once if the console allows it. Do it with CTO sign-off if you can reach them. Otherwise it's your call as head of product, with Tomas's agreement.
- **If the downgrade is unproven or failed on any test unit:** stay paused. Don't abort. Look for a targeted fix, such as a hotfix 6.0.1 for the affected cohort.
- **If failures are concentrated in one hardware group:** consider stopping only that group.

**Customer communication**
- **Don't email all 210,000 customers.** 90% of them aren't on 6.0 and have nothing to check. It would swamp support and alarm people for no reason.
- **Do email or push-notify the roughly 21,000 on 6.0 tonight.** Say what's happening, tell them to check that the bolt has fully extended when they lock up, that the thumb-turn works by hand as a fallback, and give them a support link. Keep it factual and calm. Hanne is right that people need to know tonight, but only the people at risk.
- **Give support a short script and the workaround now.** Have them use it for the 160 open tickets too.
- **Message the CTO** with a three-line status. They land at 18:00 and shouldn't be surprised.

**Why not each option as proposed**
- **Tomas's immediate Abort:** it risks a mass failed downgrade, and it adds a second incident to the first.
- **Hanne's full-fleet email:** wrong audience, and it adds load.
- **Doing nothing until the CTO lands:** 15:00 auto-widening and the 16:00 button would both make this worse before then.

**Assumptions:** Pause really does hold the cohort and doesn't push anything. The 160 tickets are all genuine 6.0 owners. Marketing can still hold the 16:00 send. If any of those is wrong, tell me and I'll adjust the plan.
