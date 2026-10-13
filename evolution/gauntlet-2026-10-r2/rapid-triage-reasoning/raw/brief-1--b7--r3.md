**Short version: press Pause now, not Abort. Stop the 16:00 email (or at least its button). Warn only the roughly 21,000 owners on 6.0, not all 210,000. Hold Abort until Tomas has tested it on a few real units.**

## Why not Abort yet

Abort downgrades every lock already on 6.0 to 5.8. Your own QA incident shows what a 6.0 to 5.8 flash can do: a unit wouldn't boot until someone opened it and reflashed it by cable. You don't yet know whether that was a one-off mistake or something every downgrade risks. If it's the latter, Abort could turn 160 locks with a stalled motor into thousands of dead locks, and you can't undo that from the console. The thumb-turn works by hand, so the current fault is bad but survivable. Don't swap it for a risk you haven't measured.

## Why Pause is the right move

- It's fully reversible. You can resume or abort later.
- It stops the 15:00 widening to 50%, which would roughly multiply the exposed locks by five.
- It costs nothing while you work out the cause.

## Do these in order

**Now, 14:25 to 14:35**
1. **Pause the rollout.** Confirm the console shows it as paused and that the 15:00 auto-widen is gone. Don't leave this until 14:55.
2. **Stop the 16:00 email.** This one is easy to miss. "Update now" and "Check for update" install the newest published firmware regardless of rollout stage. Pause doesn't stop them. At 16:00, tens of thousands of customers could be pushed onto 6.0 straight from the email.
   - Best option: ask engineering whether 6.0 can be un-published, or the "newest" pointer moved back to 5.8, so those buttons stop offering it. Also check that the in-app "Check for update" is covered.
   - If that can't be confirmed by about 15:30, pull or delay the marketing send. A launch email is easy to resend later.
   - Tell marketing now, and name someone who has to confirm back to you.

**14:35 to 15:00**
3. **Tomas has two quick jobs.**
   - Ask him to find out whether the bench failure was specific to that unit or something a normal 6.0 to 5.8 downgrade can do. He probably knows already. Ask him how confident he is and why.
   - Ask him to pull the stall pattern from the 160 tickets: which hardware revision, which battery level, which door type, and whether it's every 6.0 lock or only some. Check whether the 160 are spread across the 21,000 or clustered in one hardware variant.
4. **Hanne: a targeted notice, not the all-customer email.** Only about 21,000 customers are on 6.0. The other 189,000 have nothing to check, and a fleet-wide "check your doors tonight" would cause panic and a flood of tickets. Send the 6.0 owners a short message:
   - Some locks on the new firmware may stall and leave the bolt retracted.
   - Check that the door is actually locked.
   - Use the thumb-turn if it isn't.
   - Don't tap "Update" again.
   - Here's how to reach support.
   
   Send it by in-app notice or push first, with email too if that's fast. Give support a short script and a way to flag a lock as faulty.

**By about 15:30**
5. **Decide on Abort with data, not by default.** If Tomas can reflash one or two spare units from 6.0 to 5.8 the way Abort would, and they boot and lock normally, Abort becomes a reasonable choice and you can run it for the affected cohort.
   - If the downgrade fails or he can't test, keep the rollout paused and look for a 6.0.1 fix. Meanwhile support handles the affected owners one by one.
6. **Get a decision-maker on record.** Your CTO is in the air until 18:00. Send a short message now so they see it on landing: what you paused, why you didn't abort, what happens with the email, and what's still open. If someone else has authority over a downgrade in that window, tell them what you've done too.

## What to do if things change

- If new tickets arrive faster, or you get reports of a lock failing to lock at night while people are home, escalate on the support and safety side. Consider a stronger customer message and offering a replacement or a technician.
- If you find the stall is linked to one hardware variant, you can restrict 6.0 to the others and keep it paused for that one.
- If Abort tests clean and the fault is spreading, abort in batches, not all at once, so a bad outcome stays small.

## Afterwards (tomorrow, not tonight)

- Root cause for the motor stall.
- A fix and a re-staged rollout, starting small again.
- A rule that the update buttons follow the rollout stage, so "Update now" can't bypass a staged release.
- A tested rollback path before the next release.
- A proper review of how you ended up with a rollback you didn't trust.

## Assumptions

- I'm assuming Pause really does halt only the auto-widening, and that existing 6.0 locks keep running 6.0.
- I'm assuming the 160 tickets are a floor. Many owners won't report, so the real number is higher.
- If you can confirm any of this faster than I've guessed, adjust accordingly.
