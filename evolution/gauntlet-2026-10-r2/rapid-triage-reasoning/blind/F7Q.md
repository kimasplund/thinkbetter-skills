You have a workable plan. Neither Tomas nor Hanne has the right first move, and the 16:00 email is a bigger risk than either of them mentioned.

**Do now, by 14:40**

1. **Press Pause.** It holds the rollout at 10% and stops the 15:00 widening. It costs almost nothing and you can undo it. Do it now rather than at 14:59.
2. **Don't press Abort yet.** Abort reinstalls 5.8 on about 21,000 locks that are already on 6.0. Your own QA incident suggests that downgrade path is dangerous. A unit that went from 6.0 to 5.8 wouldn't boot and had to be opened and reflashed by cable. I don't know whether that was a one-off or a real 6.0-to-5.8 incompatibility, but the evidence points to the second. A mass downgrade could turn 160 stalled bolts into thousands of bricked locks. Ask Tomas one question: has the 6.0-to-5.8 downgrade been tested on production-like units, and what happened? If the answer is "yes, it works, and the bench failure was a one-off", Abort becomes a reasonable option. If nobody knows, don't press it.
3. **Stop the 16:00 marketing email, or remove the "Update now" button.** The button and the in-app "Check for update" install the newest published firmware whatever stage the rollout is at. They would put 6.0 on every customer's lock, 210,000 in total, however the rollout console is set. Pause does not protect you from this. Ask Tomas or whoever owns the release pipeline whether Pause also stops these paths. If they can't say with certainty, assume it doesn't. Then either unpublish 6.0 as the newest version, or hold the email. Holding the email is the safer one and needs only a message to marketing.

**Do by 15:00**

4. **Get the facts that decide between Abort and staying paused.** Ask Tomas to answer these:
   - Is the failure tied to something specific, such as lock hardware revision, battery level, temperature, or whether the fingerprint feature is enabled? 160 tickets from about 21,000 locks is under 1%, but I don't know how many of those locks have actually cycled the motor since updating, so the true failure rate could be higher.
   - Is there a safe remote fix for locks that are already affected?
5. **Send a targeted notice to 6.0 owners only.** That is about 21,000 customers, not Hanne's 210,000. Tell them to check that the door locked, that the thumb-turn works by hand, and how to report a problem. Hanne is right that a door that doesn't lock is a real security issue, and customers should know tonight. But 90% of customers don't have 6.0 and the notice would only frighten them. If you can't segment by firmware version in time, send it as an in-app or push message to 6.0 users, which is easier to target than email.
6. **Prepare support.** Give them a script, a way to tag tickets, and an escalation path for customers who say their door is unlocked and they can't fix it.

**CTO**

Don't wait for 18:00. Send a short written summary now: what's happening, what you've done (Pause, email held), and what's still open (Abort or not). Ask for a delegated decision-maker while they're in the air. If someone else has authority, such as a VP of engineering, tell them as well. Pause and hold-the-email are low-risk enough that you can do them on your own authority. Abort is the decision to reserve for someone senior, after the downgrade question is answered.

**Assumptions I'm making**

- The 160 tickets are really from 6.0 owners, and ticket volume is rising rather than levelling off.
- Pause doesn't touch locks already updated.
- I can't see your console or logs, so check the Pause behavior yourself.

**Short version**

Pause now. Hold the 16:00 email or pull its button. Ask Tomas whether the downgrade is safe before anyone presses Abort. Send a targeted notice to 6.0 owners only. Brief the CTO in writing now.
