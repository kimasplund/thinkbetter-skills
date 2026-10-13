**Short answer: neither the temps nor the CRM rollback. The most likely cause is the IVR change on October 3. When you dropped the date-of-birth and postcode prompts, the ID check didn't go away. It moved onto the agent's live time.**

## Why the other explanations don't hold

| Candidate | What the evidence says | Verdict |
|---|---|---|
| New agents (live Sept 26) | AHT rose by the same 1.7-1.9 min for tenured and new agents. A new-starter effect would hit the new group harder. They also went live a week before the jump. | Ruled out |
| Harnley floods | Flood calls are about 11% of volume. Motor-only calls rose by the same amount, and 11% of calls can't produce a ~30% rise overall. | Ruled out |
| CRM 14.1 slow screens | The jump starts October 3, not October 2. The October 9 patch fixed load times, but AHT for October 10-24 matches October 3-9, so the fix changed nothing. Hold and after-call work, where screen lag would show up, are flat. QA puts the extra time before the claim is discussed. | Very unlikely |
| Not enough staff | Short staffing doesn't lengthen the average call. It lengthens queues. It's a consequence of the higher AHT, not the cause. | Ruled out as a cause |
| Call mix or harder callers | The rise is uniform across call types, and it is all talk time. | Ruled out as the main driver |
| IVR refresh, October 3 | Timing matches to the day. The rise is flat and persistent. It is uniform across agent tenure and call type. It sits in the first couple of minutes of the call, before the claim. It also matches the specific change: prompts removed that captured identity data up front. | Leading cause |

## What is probably happening

Your verification rules are unchanged, so every caller still has to pass ID checks. Before October 3, the IVR collected date of birth and postcode, and agents likely confirmed them against the account in a few seconds. Now agents ask for them, key them in and match them themselves. That is plausibly 1.5-2 minutes of extra talk time on every call, which fits the 1.7-1.9 minute rise. It would be the same for tenured and new agents and for motor and flood claims. It would add no hold or after-call time.

There is a second, smaller effect. Abandonment fell from 9% to 4%, so about 5% more callers now reach an agent. Some of them would have hung up at the old prompts. That adds to the workload and is a good result for customers. It doesn't explain the AHT jump, because it wouldn't make every call longer.

The IVR change is a clear fit but not yet proven. Two checks would settle it quickly:

1. **Time the first part of the call.** Have QA or your speech analytics tool measure the time from answer to ID-verified on those 40 calls, and on a sample of September calls if you have recordings. If the gap is about 1.5-2 minutes, that is your cause.
2. **Look at October 2 and 3 separately.** Check AHT by day, and by the hour of the IVR go-live. A step change at the IVR switch-over, not at the CRM release, would rule out the CRM.

A further test is to route a small share of calls (say 10-20%) through the old date-of-birth and postcode prompts for a few days. If AHT on that group goes back toward 6.1, the cause is confirmed.

## What I'd recommend

- **Don't hire 12 temps.** The extra workload is about 30% (7.9 against 6.1 minutes). On 140 agents that is roughly 40 agents' worth of time, so 12 temps wouldn't close it. Temps would also be paid to do an avoidable step by hand on every call, and they'd be slower still while new.
- **Don't roll back the CRM.** The October 9 patch already fixed the slow screens, and AHT didn't move. A rollback would cost you a release cycle and fix nothing.
- **Fix the ID capture in the IVR.** Bring back the date-of-birth and postcode prompts, but place them after the caller has chosen a menu option, or ask for only one of them. The vendor's data shows where callers hung up, so you can test which prompt caused most of the drop-off. If the system can match the caller's phone number to an account, offer a "Is this the number on your policy?" shortcut instead. Aim to keep abandonment near 4-5% while giving back most of the 1.8 minutes.
- **Meanwhile, cover the afternoons.** If you need a stop-gap before the IVR fix, overtime or shifting breaks and training away from the afternoon peak is cheaper and more reversible than hiring.

I'm assuming the prompts you removed fed data to the agent's screen. If they didn't, the extra time may come from something else in the new IVR flow, such as the longer hand-off or callers arriving less prepared. The timing check in step 1 would show that too.
