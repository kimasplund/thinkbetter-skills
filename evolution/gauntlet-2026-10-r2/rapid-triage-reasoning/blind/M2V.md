**Short version: press Pause now, not Abort. Stop the 16:00 email's "Update now" button from reaching anyone. Warn only the roughly 21,000 owners who have 6.0, and have Tomas test the rollback on spare locks before anyone commits to Abort.**

**Why not Abort right now**

Abort puts 5.8 on every lock that is already on 6.0. Your own QA incident shows that putting 5.8 on a 6.0 unit left it unable to boot until someone opened it and reflashed it by cable. That was one bench unit, so we don't know if it's a general downgrade problem. But if it is, Abort could turn about 21,000 locks that mostly work into bricks, and you can't undo that from the console. Right now you have a fault that hits under 1% of the 6.0 locks (160 tickets against about 21,000) and has a manual workaround. Abort risks a much worse outcome for everyone, and you can't reverse it. Pause costs you nothing and can be undone.

**Next 35 minutes**

1. **Now (by 14:30): press Pause.** This stops the automatic widening to 50% at 15:00. Confirm that the console shows "paused" rather than assuming it. It does not fix the locks already on 6.0, but it caps the problem at the current fleet.

2. **By 14:40: close the back door to 6.0.** Pause does not stop "Update now" or "Check for update" in the app, because both install the newest published firmware at any stage. Ask whoever owns the release pipeline to do the first of these that works:
   - Make 5.8 the version those buttons install, or unpublish 6.0 as the latest.
   - If that isn't possible in time, tell marketing to delay the 16:00 email. A short delay costs you a launch email. A send to 210,000 customers could push 6.0 onto most of the fleet.

   Whichever you do, tell support that anyone pressing "Check for update" may get 6.0 until this is closed.

3. **By 15:15: send Hanne's message, but only to the roughly 21,000 owners who have 6.0.** The other ~189,000 customers are not affected, and telling them to check their doors tonight would cause panic and a ticket flood for no reason. The message should say:
   - Some locks on this update may stall and leave the bolt retracted.
   - How to check the door.
   - That the thumb-turn works by hand.
   - That a fix is coming.

   Hanne can also phone or push-notify anyone who has already filed a ticket.

4. **Start now, report by ~15:45: Tomas answers one question, "Can a 6.0 lock safely take 5.8?"** Have him try the rollback on a few spare or office units that are on 6.0 (I'm assuming you have some, and that you can start a rollback on a single device). He should also pull the 160 tickets to look for a pattern: hardware revision, batch, region, or whether the lock was mid-update. That is a quick look, not root-cause analysis.

5. **At about 15:45, decide on Abort based on Tomas's answer.**
   - **Rollback boots cleanly on every test unit:** Abort is now a reasonable option. I'd still rather target it at the affected pattern, if there is one, than abort the whole fleet.
   - **Any test unit fails to boot, or you can't test in time:** do not Abort. Stay paused, keep warning owners, and put the cable-reflash risk in front of the CTO.
   - **You can't reach an answer by 15:45:** stay on Pause. The cost of waiting is that some already-affected owners leave a door unlocked until the answer comes, which is why the message in step 3 has to go out first.

6. **By 18:00: brief the CTO** on what you did and why, and what is still open. If new tickets are arriving faster than before, say so at once. A rising rate is the one thing that would make me reconsider a fleet-wide rollback sooner.

**What you are giving up:** the 6.0 launch date and the 16:00 email timing, and you are leaving the affected locks on a bad version until the rollback is proven safe. I think that is the right trade, since you can recover from a delay but not from a bricked fleet.

**Assumptions:** the console's Pause really does stop the 15:00 widening and is reversible, the 160 tickets are all the same symptom, and the bench unit's failure was a downgrade problem and not a one-off mistake. If Tomas or QA can show that last one is a one-off, step 5 gets much easier.

**Afterwards**
- Find the cause of the stall (Tomas, tomorrow).
- Decide whether the rollback path needs a fix before any future staged rollout.
- Add a rule that the "Update now" button can't bypass a paused rollout.
