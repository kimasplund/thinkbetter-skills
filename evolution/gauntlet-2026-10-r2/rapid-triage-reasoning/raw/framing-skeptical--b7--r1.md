Your plan is better than you think. Press Pause now, not Abort, and don't send the all-customer email. Then use the next 35 minutes to close the one gap Pause doesn't cover, which is the 16:00 "Update now" button.

**Why Pause and not Abort**

- Pause holds the rollout at 10% and stops the 15:00 widening to 50%. That removes the main way this gets worse, and you can undo it with one click.
- Abort downgrades about 21,000 locks from 6.0 to 5.8. You already have evidence that a 6.0-to-5.8 flash can leave a lock that won't boot and needs a cable reflash. That was one bench unit, so I don't know how often it happens. If it happens even occasionally, Abort turns a door that won't lock into a door that won't open, and the fix means a truck roll or a return. You can't undo that. Tomas's instinct to stop 6.0 is right, but Abort is the wrong way to do it until someone tests the downgrade.
- The current harm is real and contained. About 160 tickets against about 21,000 locks is under 1%. The thumb-turn still locks the door by hand. Owners can work around it once they know.

**Next 35 minutes**

1. **14:25-14:30: Pause the rollout.** Confirm in the console that the 15:00 widening is cancelled.
2. **By 14:40: Stop the 16:00 email and the update button.** This is the gap. The "Update now" button and the app's "Check for update" install the newest published firmware whatever the rollout stage, so Pause alone doesn't protect the other 189,000 customers. Ask marketing to hold the email now. Ask whoever runs the console or the app whether you can unpublish 6.0 as the latest version or switch off the update prompt. If you can't do that by 15:30, hold the email anyway. A late launch email is cheap. A lock that stops locking on 189,000 more doors is not.
3. **By 14:45: Start a bench test of Abort.** Have Tomas put a few 6.0 units through the same 6.0-to-5.8 downgrade the console would run. Also have him check whether the stall happens only on one hardware batch, or on one motor or lock revision. Either answer shapes the next step.
4. **By 15:00: Tell the 6.0 owners, not everyone.** Send a short email and app notice to the roughly 21,000 locks on 6.0. Say the motor may stall and leave the bolt retracted, ask them to check the door after locking, and tell them to turn the thumb-turn by hand if it doesn't engage. Don't tell them to downgrade. Hanne's concern is valid, but a notice to all 210,000 customers will send 189,000 people who aren't affected to check their doors, and it will flood support. A targeted notice protects the people at risk.
5. **15:00-15:30: Check the numbers.** Compare the ticket rate on 6.0 against what 5.8 usually gets. Are tickets still coming in, and at what rate per hour? If the rate is rising, the 6.0 owners' notice becomes more urgent. If the tickets are mostly one hardware revision, you can limit the notice and any remedy to those units.

**The call at about 15:30, after the bench test**

- **If the downgrade is clean on every unit tested:** Abort is safe, at least for the affected units. Ship it, or ask Tomas to downgrade only the hardware batch that stalls.
- **If any unit fails to boot after the downgrade:** Don't Abort. Keep the rollout paused and ask Tomas to build a fixed 6.0.1. Ask support to handle the stall with the thumb-turn workaround in the meantime.
- **If you can't test in time:** Stay paused. Waiting costs very little, because the rollout is on hold and owners have the workaround.

**What I'm assuming**

- The console's Pause really stops the 15:00 widening. Check that on screen.
- The tickets are about 6.0 and not a hardware or batch issue that 5.8 shares.
- The bench unit's boot failure was real and not a one-off of how QA flashed it. If Tomas can show that quickly, Abort becomes much more reasonable.

**Follow-ups**

- Reach the CTO at 18:00 with the facts: what was paused, what was held, and what the bench test showed.
- Find the cause of the motor stall tomorrow.
- Find out why 6.0 shipped without a tested downgrade path.
- Change the console so the update button respects rollout stages.
