Decision needed by 15:00. Your 15:00 auto-widen is the most urgent item, and the 16:00 launch email is the second. Here is the plan for the next 35 minutes, in order.

**Do now (14:25-14:30): Pause the rollout.**
Pause holds the 10% cohort where it is and stops the 15:00 widen to 50%. It is fully reversible, so it's the right first move regardless of what you decide about Abort. Confirm in the console that the state shows Paused and that the 15:00 widen is cancelled, not just scheduled to be skipped.

**Do now (14:25-14:30): Stop the 6.0 push paths.**
"Update now" in the 16:00 email and "Check for update" in the app both install the newest published firmware at any rollout stage. Paused rollout does not stop them. Unless you change what the latest published version is, the 16:00 email will push 6.0 to up to 210,000 locks while the rollout is paused. Get firmware ops to set the published latest back to 5.8, or pull the launch email. Do one of these before 16:00 and check that a test device gets 5.8 from "Check for update."

**14:30-14:40: Size the problem and test the rollback.**
- Pull the stall rate for the 21,000 locks on 6.0 and how many of the 160 tickets map to them. Ask whether the stall is consistent (every lock) or intermittent.
- Ask Tomas to run the 5.8 reinstall on two or three 6.0 bench units and confirm each one locks and unlocks afterward. Include a power cycle. The bench unit that was flashed with 5.8 by mistake would not boot until it was reflashed by cable, so a mass Abort without this test risks bricking locks that need a physical visit to fix.
- Assumption: I don't know whether that bench failure was a 5.8 image problem or a flashing-procedure problem. Tomas needs to answer that before Abort goes to the whole cohort.

**14:40-14:50: Tell customers the right thing, to the right people.**
- Don't email all 210,000 customers. Most of them are not on 6.0 and a broad "check your doors tonight" notice will cause alarm without helping. Send a targeted notice only to 6.0 owners, using app or account data.
- Suggested text: "Some Wren locks on firmware 6.0 may not lock fully. If your bolt stays retracted, use the thumb-turn to lock the door by hand. Do not install 6.0 for now. We will send an update as soon as we have a fix." Ask support to put the same text in a macro for the 160 tickets.
- Also ask support to hold the "Update now" wording until the 16:00 email is fixed.

**14:50-15:00: Decide.**
Tomas and Hanne both need to be in the room with whoever can approve on behalf of the company while the CTO is in the air. Ask the CTO's delegate now who that is, so the decision isn't stuck.
- If the bench test passes and the stall rate confirms the cause is in 6.0: Abort on the affected cohort, in batches, with a watch on the first batch.
- If the bench test fails, or the data is unclear: keep the rollout paused and do not Abort. Pausing already protects the other 190,000 customers and the 16:00 email is handled. The affected locks still have a manual workaround (thumb-turn).

Neither Abort nor Pause fixes the locks already stalled on 6.0. Customers with a stalled lock need the thumb-turn, and any lock that can't be reinstalled needs a service visit.

**After the crisis (follow-up list):**
- Find the root cause of the motor stall in 6.0 (the fingerprint unlock path is the likely suspect, but this is unconfirmed).
- Find out why the bench unit got 5.8 by mistake, and add a check that stops a mismatched image from being flashed onto 6.0 hardware.
- Find out why "Check for update" and the launch email can install a firmware that isn't in the current rollout stage. This needs a fix before any future staged rollout.
- Review the QA sign-off. It passed with a bench unit in a state that no customer device is in.
- Write up the decision record: what was decided at 15:00, by whom, and what new information would change it.
