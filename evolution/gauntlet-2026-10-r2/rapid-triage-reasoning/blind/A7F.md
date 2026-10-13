Pause the rollout now, and don't Abort yet.

**Now to 14:35**
1. **Click Pause.** It's reversible and holds the rollout at 10%, so the automatic widening to 50% at 15:00 can't happen. It costs you nothing. Abort is the control you can't take back.
2. **Stop the 16:00 marketing email, or remove the "Update now" button from it.** This is the most urgent item after Pause. That button, like "Check for update" in the app, installs the newest published firmware whatever stage the rollout is at. The email would push 6.0 to all 210,000 customers, which makes Pause pointless. Ask Marketing to hold the email or send it without the button. Ask engineering whether you can unpublish 6.0 as the "newest" version or gate it to the staged cohort. The in-app "Check for update" button has the same problem, so that gating question matters even if the email is held.

**Why not Abort now**
- Abort reinstalls 5.8 on about 21,000 locks that are already on 6.0. Your own QA incident suggests that downgrade path is unsafe. A bench unit flashed with 5.8 while on 6.0 wouldn't boot, and it needed a cable reflash after the case was opened.
- One bricked bench unit is a small sample, so it doesn't prove the downgrade fails. It is enough to rule out running that downgrade on 21,000 doors without testing it first.
- Locks that are currently stalling but still working could end up dead. Bricked locks are worse than a bolt that sometimes stays retracted.
- Tomas's instinct to get 6.0 off the fleet may still be right. Make it a decision you take after Pause, once you know the downgrade is safe.

**14:35 to 14:50: engineering questions for Tomas**
- Can he test Abort/downgrade on a few 6.0 units, including ones that are stalling, and see whether they boot?
- Is the stall tied to something you can see, such as a hardware revision, a battery level, a temperature or a door type? If so, you can target the fix.
- Can a fix be hotfixed forward as 6.0.1 instead of rolling back? Forward fixes may be safer than a downgrade.
- Does he agree 160 tickets from about 21,000 locks is real? That is under 1%, but a lock that fails to lock is a security failure, so treat it as serious.

**Communication: a middle path between Hanne's plan and none**
- Don't email all 210,000 customers tonight. About 189,000 of them are on 5.8 and aren't affected, so it would cause alarm and a flood of tickets for no benefit.
- Do send a targeted message to the roughly 21,000 customers on 6.0, by email, push or in-app, tonight. Say that if the bolt stalls and the door doesn't lock, they should lock it by hand with the thumb-turn and check the door before leaving or going to bed. Say you're working on it and will update them.
- Send Hanne a short holding line for support now, so agents give consistent advice and log the affected units.
- Hold the wider email until you know more. Escalate it if the facts turn out worse, for example if the stall affects locks that aren't on 6.0.

**Before 15:00**
- Confirm on the console that the status reads Paused and not just "scheduled".
- Try to reach the CTO. Even in flight, someone may be able to reach them by message or through their assistant. If not, decide without them. Pause, hold the email and send the targeted notice are all low-regret and within your authority. Leave the Abort decision for 18:00 or for when Tomas has test data.
- Write a short note on what you did and why, so the CTO can review it when they land.

**Assumptions**
- Pause really does hold the cohort at its current version.
- The 160 tickets are mostly the same fault.
- Your install base is about 210,000, with about 21,000 on 6.0.

This is a bad moment in a big week, but pausing and holding the email contains it. The launch can still happen once there's a fix.
