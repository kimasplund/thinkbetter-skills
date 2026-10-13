**Short version: press Pause now, do not press Abort yet, stop the 16:00 email, and warn only the roughly 21,000 owners on 6.0, not all 210,000.**

## Why not Abort yet

Abort reinstalls 5.8 over 6.0 on every lock on 6.0. Your QA incident is the warning sign. A bench unit that went from 6.0 back to 5.8 wouldn't boot and had to be opened and reflashed by cable. That is one data point, but it is exactly the path Abort would run on about 21,000 locks. If the downgrade bricks even a few percent, you turn 160 locks that don't latch (and still work by thumb-turn) into hundreds or thousands of dead locks on doors, with no remote fix. You can't undo Abort. You can undo Pause.

Pause also holds everything Abort would hold. The only thing it doesn't do is roll back the locks already affected.

## The next 35 minutes

**Now (14:25 to 14:30)**
1. Press **Pause**. This stops the 15:00 widening to 50%. Don't wait for anyone's agreement on this; it's reversible and nobody has a good argument against it.
2. Message Marketing: **hold the 16:00 email.** The "Update now" button and the app's "Check for update" install the newest published firmware regardless of rollout stage. Pause doesn't stop those. Sent to 210,000 customers, that email would push 6.0 onto every lock that taps it. This is the biggest way things get worse today, and it is entirely in your control.
3. Ask engineering for the same protection at the source: can 6.0 be taken out of the "newest published" slot, or can the update check be limited to the rollout cohort? If that takes a deploy you can't do safely before 16:00, the email hold is your backstop, and the same applies to anyone who opens the app and taps "Check for update". Get a yes or no on this by 14:45.

**14:30 to 14:50: get facts**
4. Tomas: test the downgrade on real hardware, not by reasoning. Take several units on 6.0, ideally a few hardware revisions, flash 5.8 the way Abort would, and see whether they boot. That decides whether Abort is a fix or a second incident. Ask him also whether a safer rollback exists, such as a patched 6.0.1 or a flag that disables the fingerprint-unlock motor path.
5. Support or data: pull what separates the 160 from the rest. Hardware revision, battery level or voltage, region and temperature, door type, fingerprint feature use. Also whether the ticket rate is rising or flat since noon. 160 of 21,000 is under 1%, but it's a lock that fails to secure a door, so treat it as serious. A rate that is accelerating, or a single hardware revision accounting for most cases, changes the plan.
6. Write down what you know and don't. You'll need it for the CTO at 18:00.

**14:50 to 15:00: decide and confirm**
7. Confirm in the console that the rollout is actually held at 10% and the 15:00 widening is off. Check the status afterwards; don't assume.
8. Decide on Abort based on step 4:
   - Downgrade boots cleanly on every test unit: Abort is reasonable, ideally staged if the console allows it, starting with a small group and watching.
   - Any failure to boot: **don't Abort.** Stay paused, ship a fix forward, and tell affected owners about the thumb-turn workaround.
   - No result by 15:00: stay paused. Waiting costs you little, since the rollout is held and the affected locks still work by hand.

## Customer communication

Hanne is right that people need to know, because a door that doesn't lock is a safety issue. But 210,000 is the wrong audience. Only the ~21,000 on 6.0 are affected, and an alarming email to everyone, including 189,000 people with no problem, will flood support and may push more people to update or to factory-reset.

- Send to the **6.0 cohort only**, this evening, once step 3 is settled so the email doesn't invite them to do something worse.
- Content: some 6.0 locks may not fully extend the bolt, so check that your door is actually locked; the thumb-turn works by hand; don't re-flash or reset; we're working on it and will update you by [time]; how to reach support.
- Give support a short script and a macro for the 160 existing tickets now. They can use it before the email goes out.
- If you can, add an in-app banner for 6.0 owners. It reaches people sooner than email.

If the pattern points to a specific hardware revision or condition, narrow the audience further and make the message more specific.

## Things to do afterwards

- Brief the CTO at 18:00 with: what was held, what's known, what the downgrade test showed, and the decision still open (Abort vs fix forward).
- Find the root cause of the stall (motor current limit, timing in the fingerprint unlock path, cold or low battery).
- Fix the structural gap: "Update now" and "Check for update" shouldn't bypass a staged rollout, and the launch email shouldn't have been scheduled against an unfinished rollout.
- Treat downgrade safety as a release requirement. The QA bench failure should have been a blocker or a ticket, not an anecdote.
- Once Pause is released, the 50% step only goes ahead after the cause is understood.

## Assumptions

I assumed Pause really does hold at 10% and that the console can't be bypassed some other way, that the email tool can be stopped by Marketing quickly, and that nothing in the 160 tickets reports a door being found unlocked with someone harmed. If any of those is wrong, say so and the plan shifts.
