Here is a plan for the next 35 minutes. I've assumed the console works as you described, that the 16:00 email and the app's "Check for update" can be stopped by you or someone on your team, and that you have authority to make these calls while the CTO is in the air. If any assumption is wrong, tell me and I'll adjust.

**Do now (14:25 to 14:30): Pause the rollout.**
Pause stops the 15:00 widening to 50% and holds the 10% cohort where it is. It's reversible and doesn't touch locks that already have 6.0. Don't Abort yet (see below).

**Do by 14:35: Stop the 6.0 push paths.**
- Cancel or hold the 16:00 launch email. It has an "Update now" button that installs whatever is newest, so it would push 6.0 to all customers.
- Make sure "Check for update" in the app can't serve 6.0. The usual fix is to unpublish 6.0 or make 5.8 the newest published firmware. Confirm with whoever runs the publishing pipeline that this doesn't break the paused cohort.

**Hold Hanne's 210,000-customer email.**
A blanket "check your doors tonight" message to everyone causes alarm without giving people a fix, and most customers aren't affected. Instead, send a short, targeted notice to 6.0 owners, and use it only once the symptom is confirmed. Its core content: if the bolt doesn't extend when you lock from the app, the door is not locked. Check it by hand with the thumb-turn, don't rely on the app to confirm, and contact support. Have Hanne draft it now so it can go out quickly, and have legal or safety review it, since this is a security device.

**Why not Abort right now (Tomas's position).**
Abort reflashes 5.8 onto about 21,000 locks, and QA has already shown that a wrong or interrupted 5.8 flash can leave a unit that won't boot and needs a cable reflash. Abort could convert a stall problem into a bricked-lock problem across the fleet. Keep it as the fallback, not the first move. Tomas is right that you should stop exposure now; Pause does that without the rollback risk.

**By 14:50: Get the facts that decide Abort.**
- Tomas: pull telemetry from the stalled locks (motor current or stall events, hardware batch, firmware version, temperature if logged). Check whether the stalls cluster by batch or by hardware revision.
- Support: count unique affected locks from the 160 tickets, and compare against the 21,000 on 6.0 to estimate the failure rate.
- Tomas or QA: test the 5.8 reflash by cable on a 6.0 bench unit, in the same way the field units would be reflashed. Don't run Abort on the fleet until this succeeds.

**By 14:55: Make a decision and name an owner.**
If the stall rate is high and the 5.8 rollback is proven, Abort. If the rate is low and clustered, keep the pause and narrow the fix. Either way, you make the call and record it. Name yourself as decision owner in writing, and tell the CTO's office so the decision is clear when they land at 18:00.

**At 15:00:** Confirm in the console that the rollout is still paused at 10% and didn't widen.

**Escalation:** Because this is a deadbolt that may not lock, tell your safety or incident lead now, and check whether any regulator or consumer-safety reporting obligation applies. That reporting clock may not wait until the CTO lands.

Summary of the next 35 minutes: pause, stop the 16:00 email and the app update path, hold the blast email and prepare a targeted notice, gather the telemetry and the rollback test, then decide Abort or hold by 14:55.
