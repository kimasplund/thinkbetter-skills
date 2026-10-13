Neither the temps nor the CRM rollback is the right fix first. The best-supported cause is the IVR refresh on October 3.

**What is most likely going on**

On October 3 you dropped the date-of-birth and postcode prompts from the IVR. Your verification rules haven't changed, so every caller still has to pass ID checks before an agent discusses a policy. Those checks now happen on the agent's call, not in the IVR. The extra talk time is the agent asking for and confirming those details in the first couple of minutes, which is what QA heard.

The pattern fits this:
- **Timing:** AHT moved on October 3, the same day as the IVR change. It did not move on September 26 when the new agents went live.
- **Where the time is:** all of the increase is talk time, and it is concentrated in the opening minutes. Hold and after-call work are flat, so the agents are not slower at the claim itself.
- **Who is affected:** tenured and new agents rose by the same amount, and motor-only calls rose too. Floods are about 11% of calls and have nothing to do with motor calls, so they cannot explain the whole rise.
- **Why it stays:** the new IVR is permanent, so the increase persists. That matches October 10–24 being the same as October 3–9.

**Why not the other two explanations**

- **Temps:** New agents went live on September 26, but AHT rose by the same amount for tenured staff. Temps would add capacity, not reduce handle time, and would not address a cause that is hitting everyone.
- **CRM rollback:** The slow-screen problem was reported on October 2 and patched on October 9. AHT did not drop after the patch, and it stayed flat through October 10–24. A slow CRM would also show up as hold or after-call work, and those are flat. A rollback is an expensive change to make on the strength of that evidence.
- **Floods:** The flood claims are complicated, but motor calls rose by the same amount, so floods are at most a minor contributor.

**Caveats**

This is a strong hypothesis, not a proven cause. QA's 40-call sample is small, and "mostly in the first couple of minutes" was not measured against a baseline. Also, the IVR now lets more callers through (abandonment fell from 9% to 4%), so more calls reach agents, and some of the change could be a different call mix.

**How to confirm it this week**

1. Pull talk time split into the opening segment (call start to claim discussion) and the rest, for October 1–2 against October 3–24. If the opening segment carries the whole rise, the hypothesis holds.
2. Check whether ID verification is now on the agent's call for callers who used to pass the IVR prompts. Also check whether the agent screen shows the caller's details, so the agent does not need to ask for them again.
3. Listen to about 20 calls from before and 20 from after October 3, timing the verification step specifically.

**Possible fixes, if confirmed**

- Restore the date-of-birth and postcode capture in the IVR, or pass the verified details to the agent screen, so verification takes seconds instead of a minute or more. Test whether this keeps the abandonment gain. The abandonment fall suggests the drop-off was in the prompts, so a shorter prompt (for example, one combined prompt) may keep most of both benefits.
- Give agents a short, scripted verification flow while you test the above.

Do not hire temps for this. Do not roll back the CRM on current evidence. Check the IVR verification step first, because it is the only change that lines up with the timing, the spread across agent groups, and the pattern in the talk time.
