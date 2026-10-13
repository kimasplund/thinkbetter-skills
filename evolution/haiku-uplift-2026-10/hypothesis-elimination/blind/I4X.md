The data points away from both the temps and the CRM rollback. The most likely cause is the October 3 IVR change: dropping the date-of-birth and postcode prompts moved identity verification onto the agents' calls, and that work lands in the first minutes of talk time, which is where QA hears the extra time.

**How the evidence sorts the candidates**

| Candidate | What the data says | Verdict |
|---|---|---|
| New agents (Sept 26 cohort) | AHT rose by the same 1.7 to 1.9 minutes for tenured agents as for new ones | Ruled out as the main cause |
| CRM release 14.1 / slow screens | Hold and after-call work are flat, so screen waits would show up there. AHT for Oct 10 to 24 matches Oct 3 to 9, after the Oct 9 patch, so a fix to load times would have brought AHT down. It did not | Unlikely |
| Harnley flood claims | Motor-only calls rose by the same amount, and flood claims are only about 11% of October calls | Cannot explain the rise |
| IVR refresh (Oct 3) | The jump starts on Oct 3 and holds steady after that. The change removed the DOB and postcode prompts, so agents now collect and check that information live. QA places the extra time in the first couple of minutes, before the claim is reached. Abandonment fell from 9% to 4%, so more callers now reach agents, which adds to the workload | Most likely |

Verification is unchanged: every caller still has to pass ID before a policy is discussed. What changed is who collects the details and when. Before, the IVR captured them; now an agent does, on every call, and that adds talk time that the abandonment figure does not show.

**What I would do**

1. Do not hire 12 temps yet. Extra capacity would cover the symptom at a higher cost, and new starters are not the driver.
2. Do not roll back CRM 14.1 on this evidence. The load-time fix seems to have worked, and the rise continued after it.
3. Restore the identity capture before the call reaches an agent. Keep the shorter menu and the new voice, but collect the DOB and postcode in the IVR, or pre-fill them from the caller's account lookup. This keeps the drop-off gains and removes the agent-side step.
4. Check the cause before committing money. Pull handle-time breakdowns for the verification step on calls from Oct 3 onward against September, and listen to a few more calls specifically on the opening minutes. If verification time has risen by about the size of the AHT increase, the IVR change explains it.

**Caveats**

- The 40 QA calls are a small sample. The step-level timing is a prediction I would test, not a finding.
- Part of the increase may come from a change in call mix. Callers who used to drop out at the date-of-birth prompt now reach agents, and some of them may have longer calls. The verification timing check should separate those two effects.

I'm fairly confident the IVR change is the main driver, but not certain. The timing check above would settle it within a day or two.
