Press Pause now, not at 14:59. Don't press Abort yet, and don't send the all-customer email. Hold the 16:00 marketing email.

**Why**

- **The fault is real and it affects security.** 160 tickets from about 21,000 locks is roughly 0.8%, and each one is a door that doesn't lock. The thumb-turn works, but only if the owner notices.
- **Pause is the only fully reversible move.** It stops the 15:00 jump to about 105,000 locks and costs you nothing you can't resume tomorrow.
- **Abort may not be reversible.** It pushes 5.8 onto every 6.0 lock. Your QA bench unit that went from 6.0 to 5.8 wouldn't boot and needed a cable reflash. That is one unit, and it may have been a bench quirk. But if it is a real 6.0 to 5.8 downgrade problem, Abort could brick up to 21,000 locks that currently work, mostly with doors that are locked and secure. You can't tell which it is from here, so don't gamble on it.
- **The 16:00 email is the biggest hazard.** "Update now" and "Check for update" install the newest published firmware at any rollout stage. Pause doesn't stop them. Sending that email to 210,000 customers could put 6.0 on far more locks than the 50% step you are trying to prevent.

**Next 35 minutes**

1. **Now:** Press Pause. Ask Marketing to hold the 16:00 send. If you can't get that, ask whoever owns the release to un-publish 6.0 as the "newest" version, or gate it for manual installs, before 16:00. Check that Pause really leaves the 6.0 build unavailable to the app's "Check for update".
2. **Now, in parallel (Tomas):** Test the downgrade on a few spare 6.0 locks. The question is whether 6.0 to 5.8 boots cleanly. Ask QA exactly what was different about the bricked bench unit. Be clear about what this test can settle. A clean result on a few units makes Abort lower-risk, but it doesn't prove the downgrade is safe for the whole fleet.
3. **By about 14:50:** Send the people on 6.0 only (about 21,000, not 210,000) a short message. Say the lock may stop partway, the bolt may stay retracted, and they should check the door tonight. Say the thumb-turn locks it by hand and that you are working on a fix. The other 189,000 are not at risk, and a fleet-wide alarm would flood support for no benefit. Hanne's instinct to warn people is right, but it should go to the affected group. Add an in-app banner if you can.
4. **Decision at 15:45:**
   - If the downgrade test is clean on several units and tickets are still climbing, Tomas can run Abort, preferably in batches, with the first batch watched before the rest go.
   - If the test fails or is inconclusive, leave the locks on 6.0 and ship a 6.0.1 fix instead. Support can keep guiding owners to the thumb-turn meanwhile.
   - If tickets have levelled off, stay paused and fix forward tomorrow.
   
   The CTO is in the air until 18:00. Decide this with Tomas and Hanne, write down who decided what, and brief the CTO on landing.

**Accepted cost:** The launch slips, and some of the 21,000 owners keep a flaky lock for a few hours. That is cheaper than 21,000 bricked locks or a 105,000-lock rollout.

**Follow-up**

- Find the motor-stall cause (firmware version, hardware revision, temperature or battery, any pattern in the 160 tickets).
- Fix the "Update now" behaviour so it respects the rollout stage.
- Make downgrade-safe testing part of release sign-off.
- Plan a re-launch email for when the fix is out.
