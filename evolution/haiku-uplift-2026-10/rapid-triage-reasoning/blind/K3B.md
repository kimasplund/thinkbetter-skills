**Short version: Pause now. Do not Abort yet. Stop the 16:00 email. Send a targeted notice only to the ~21,000 locks on 6.0. Decide on Abort once you have evidence, ideally with the CTO.**

**Why Pause first (do it in the next 5 minutes)**
- Pause stops the 15:00 widening to 50%, which would roughly put 105,000 locks at risk. It costs nothing and is reversible.
- Abort is not reversible and not free. It pushes 5.8 onto every 6.0 lock. Your own bench incident showed that a 6.0 unit flashed with 5.8 wouldn't boot and needed a cable reflash. If that is a downgrade-path problem, a mass Abort could brick up to 21,000 locks. Nobody has tested that path in the field. Tomas's instinct is reasonable, but the risk is that the fix is worse than the fault.
- The current fault is bad but bounded. The door doesn't lock, the thumb-turn works by hand, and 160 tickets across about 21,000 locks is under 1%. Pausing leaves that exposure where it is rather than growing it.

**Stop the 16:00 marketing email (do this by 14:45)**
- "Update now" and "Check for update" install the newest published firmware regardless of rollout stage. The email would let up to 210,000 customers bypass the staged rollout and install 6.0 in one hour. Pause doesn't prevent that.
- Ask marketing to hold or cancel the email now. Also ask engineering whether you can unpublish 6.0 as "latest", or gate the manual update path to the rollout cohort. If you can't, switch off the "Update now" button or delay the send.
- This is the most important item after Pause, because it is the only way to turn a 21,000-lock problem into a 210,000-lock one before the CTO lands.

**Communications: a targeted notice, not Hanne's all-customer email**
- Hanne is right that affected owners need to know tonight. A lock that doesn't secure the door is a safety and security issue. But 90% of customers are on the old firmware and aren't affected. Emailing all 210,000 causes panic and a support flood, and it announces a problem to the wrong people.
- Send to the ~21,000 owners on 6.0, by email and push: "Your lock may stall and leave the bolt retracted. After locking, check that the bolt is extended, or use the thumb-turn. We've paused the rollout and are working on it." Add a link or number for support.
- Give Hanne's team a short support script now: confirm the thumb-turn workaround, log the lock's firmware and hardware version, and don't promise a fix time.
- Draft this by 14:50. Hanne can send it at about 15:15 after you review the wording.

**Gather evidence for the Abort decision (14:30 to 15:30)**
Ask Tomas to answer these by about 15:30:
1. Is the stall tied to a hardware revision, a battery level, a temperature, a door or bolt type, or the fingerprint-unlock path? Cross-tab the 160 tickets by hardware and firmware variant.
2. Is the failure rate rising? Check the telemetry from the 21,000 locks for motor-stall events, which will be more reliable than tickets.
3. Does a 6.0 to 5.8 downgrade work on production hardware? Test it on several units on the bench, covering each hardware revision and both a fresh and a mid-operation state. Understand why the bench unit failed to boot.
4. Is there an alternative that avoids a downgrade, such as a hotfix 6.0.1 or a remote setting that disables the faulty feature?

**Decision rules**
- If the downgrade is proven safe and the stall rate is rising or severe, Abort, in batches if the console allows it, starting with the most affected hardware.
- If the downgrade is risky or unproven, don't Abort. Keep the rollout paused, notify affected owners, and ship a forward fix.
- If the stall is confined to one hardware segment, consider a targeted rollback or hotfix for that segment only.

**Who to tell, and when**
- Message the CTO now, so it's waiting when they land: what you did, why, and the one decision left (Abort versus forward fix). If there is a deputy or on-call exec with authority, loop them in now. Don't wait until 18:00 for a decision that affects customers' door security.
- Tell Tomas and Hanne what you decided and why. Give Tomas the downgrade question as his main task, since it's what makes his Abort option safe or unsafe.

**Timeline**
- 14:25 to 14:30: Pause the rollout. Confirm it shows as paused.
- 14:30 to 14:45: Stop or gate the 16:00 email and the "Update now" path. Message the CTO.
- 14:45 to 15:00: Verify the pause held at 15:00. Brief Tomas and Hanne. Draft the targeted notice and support script.
- 15:00 to 15:30: Tomas's diagnostics and downgrade test. Send the notice to 6.0 owners.
- 15:30 to 16:00: Make the call on Abort versus hotfix with the evidence. Keep the CTO updated.

**Assumptions:** I'm assuming that Pause does what its description says, that the 160 tickets are not yet confirmed as a single cause, and that "Update now" really can bypass the staging as you describe. Please check that last one, because the plan depends on it.
