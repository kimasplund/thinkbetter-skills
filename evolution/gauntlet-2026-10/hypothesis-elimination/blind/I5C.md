Neither the temps nor the CRM rollback looks right. The most likely cause is the IVR refresh on October 3. It removed the date-of-birth and postcode prompts, so agents now have to collect that information live, and that is adding time to every call.

**Why the IVR fits and the other changes don't**

- **Timing.** The jump starts on October 3, the day the IVR changed. The new agents went live on September 26 and the CRM release was October 2. Neither lines up with the step change.
- **New agents.** The increase is the same for tenured and new agents. If the new starters were the cause, the rise would be concentrated in them, and 18 agents out of 140 at about one extra minute would add only about 0.13 minutes to the average anyway.
- **CRM.** IT patched the load-time problem on October 9 and says it is fixed. AHT for October 10–24 is the same as for October 3–9, so the patch changed nothing. Slow screens would also usually show up as hold or after-call work, and both are flat.
- **Floods.** Motor-only calls rose by the same amount, and flood claims are only about 11% of calls. Even if they ran very long, they couldn't lift the whole average by 1.7 to 1.9 minutes.
- **Where the time goes.** All of it is talk time, mostly in the first couple of minutes before the caller reaches the claim. That is the identification stage, which is exactly what the IVR used to do before the call reached an agent.

You say the verification rules haven't changed. That is true of the policy, but the work has moved. Before October 3 the caller's date of birth and postcode were captured in the IVR, so agents were verifying against details that were already in front of them. Now agents ask for them by voice, and they have to listen, repeat, correct and key them in. Callers also tend to be stressed after a loss. That fits an extra 1.7 to 1.9 minutes of talk time, and it fits the effect being the same for everyone.

The IVR change also did what the vendor promised. Abandonment fell from 9% to 4%. That means more callers now reach an agent, so the afternoon answer-time misses may be partly a volume effect on top of the longer calls. The IVR change was good for callers who would have hung up. The cost is that it moved work onto agents.

**Why hiring temps is the wrong fix**

Temps would add capacity, but they would be staffing around a problem you can probably remove. They would also take weeks to train and would be slower at first. If the cause is the IVR, you'd be paying permanently for a change that can be adjusted.

**Why rolling back the CRM is the wrong fix**

The evidence doesn't point to it. The data shows no change after the patch, no change in hold or after-call work, and a start date that doesn't match. A rollback would carry risk and disruption for little or no gain.

**How to confirm it, quickly**

1. Ask QA to tag the same 40 calls, or a fresh sample, by what happens in the first two minutes. Check whether the agent is asking for date of birth and postcode, and how long that takes.
2. Compare the length of the opening segment for calls before and after October 3, if the call recordings or timestamps allow.
3. Check whether AHT rose only on call types where the agent now has to collect those details. The details are needed on nearly every call, so I would expect a broad rise, which is what you see.
4. If you can, run a short test: restore the date-of-birth and postcode prompts for a share of traffic, or for one time window, and compare AHT. This is the cleanest test.

**What to do if it is confirmed**

- Put back a shortened version of the prompts, for example postcode only, or a single prompt, if the vendor's drop-off data allows it. You want to keep most of the abandonment gain.
- Or give agents a faster way to capture the details, such as a standard opening script and a CRM field flow built for that step.
- Either way, measure the trade-off. Compare the cost of the extra 1.8 minutes per call against the value of 5 points fewer abandoned calls. Abandoned calls are not free, since those callers ring back or go elsewhere. It may be that the new IVR is still worth it even with the longer calls, and in that case a modest amount of extra capacity would be justified. Decide that after you know the cause, not before.

**What I'm assuming**

I'm assuming that agents now collect date of birth and postcode by voice, and that the CRM doesn't pre-fill them. If either is wrong, check that first. There may also be other changes in the new IVR, such as the new voice or shorter menus, that send callers to agents with less information, and the same test would reveal those.

**Bottom line for the board**

Don't approve the 12 temps or the rollback yet. The best explanation is that the IVR refresh moved identification work onto agents. Confirm it with a call sample and a short prompt test, then fix the IVR or the agent opening. If the gap remains after that, size any extra staffing from the new, confirmed numbers.
