**Short version: press Pause now, stop the 16:00 launch email, send a targeted notice to the ~21,000 owners on 6.0 only, and don't Abort yet. Neither Tomas's plan nor Hanne's is right as stated.**

**Why not Abort yet**
- Your QA incident is the warning. A bench unit already on 6.0 was flashed back to 5.8, wouldn't boot, and had to be opened and reflashed by cable. That is one unit, but it is exactly the downgrade Abort would run on about 21,000 locks. If even a small fraction brick, you would turn a "door doesn't lock, thumb-turn works" problem into dead locks on doors, with no remote fix.
- The current failure is annoying and a security risk, but it has a manual workaround. A bricked lock may not.
- Abort can't be undone, and Pause can. Pause costs you nothing except time.
- Abort may well be the right call later. Make it after someone has answered "is the 6.0 to 5.8 downgrade safe on production hardware?" That is a question for Tomas, today, not tomorrow.

**What to do, in order**

1. **Now (14:25-14:35): Pause the rollout.** This stops the automatic widening to 50% at 15:00, which is the most important thing you can do. Confirm in the console that the auto-widen is actually cancelled and not just delayed.
2. **Now: stop the 16:00 marketing email.** Cancel or postpone it. Ask Marketing to confirm in writing that it is held. The "Update now" button, and "Check for update" in the app, install the newest published firmware regardless of rollout stage. So Pause doesn't protect the other ~189,000 customers from the email or from the app. The email is the biggest exposure you have. If you can, also ask Tomas whether 6.0 can be un-published as "latest" so the app and button serve 5.8. If that is possible and safe, do it. If not, tell support that anyone tapping "Check for update" will get 6.0.
3. **By about 14:50: ask Tomas two things.**
   - Does the downgrade to 5.8 work on a lock that has already run 6.0? Test it on several bench units, including ones that have been through a 6.0 motor stall. Tell him you don't want the root cause yet, only whether Abort is safe.
   - Can he tell from logs which locks are stalling? Is it a hardware batch, a temperature or battery condition, or all units? Even a rough answer helps decide who to contact. 160 tickets out of about 21,000 is under 1% so far, but tickets lag behind actual failures. Treat that number as a floor.
4. **Hanne's email: yes to a notice, no to 210,000 people.** Roughly 189,000 customers don't have 6.0, and telling them to check their doors would cause panic and a flood of tickets for no benefit. Send a short, calm message only to the ~21,000 on 6.0 (target by firmware version). Say what is happening, that the thumb-turn lock still works by hand, to check the door is locked before leaving or going to bed, and not to update or change anything. Say a fix is coming. Send it in the evening if you can't get it out by about 15:30, but don't wait for the CTO. Have Hanne draft it now and have support brief agents with the same wording.
5. **Before 15:00: write a decision note for the CTO** (they land at 18:00). Include: what you did (Pause, email held), the ticket count and trend, the open question on downgrade safety, and the options. Make it readable in two minutes.

**Decision rule for tonight**
- If Tomas confirms the downgrade is safe on several units, Abort becomes reasonable, ideally with the CTO's agreement. You can also just keep the pause, if the failure is limited to a known subset and a fix is coming.
- If the downgrade is unsafe or untested, don't Abort. Keep 6.0 paused, notify the affected owners, and ship a 6.0.1 fix, or a targeted fix, instead.
- Escalate to Abort sooner if the ticket rate rises sharply, or if you get any report of someone being locked out or a door left open in a harmful situation.

**Assumptions**
I'm assuming Pause really does hold at 10%, that you can segment the customer list by firmware version, and that Marketing can stop the email. If any of these is false, tell me and the plan changes. Pause and the email are the two actions that can't wait.

**What I'd do first, right now:** click Pause, message Marketing to hold the 16:00 send, then message Tomas with the downgrade question.
