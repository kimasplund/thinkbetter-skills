Neither is right. The most likely cause is the October 3 IVR change. Your agents are now collecting the date of birth and postcode by voice at the start of every call, because the IVR no longer does it.

**Why the IVR change fits and the others don't**

| Suspect | What the data says | Verdict |
|---|---|---|
| New agents | The rise is the same, 1.7 to 1.9 minutes, for tenured and new agents. New starters would show a bigger rise. They also went live on September 26, a week before the jump. | Ruled out |
| Harnley floods | Motor-only calls rose by the same amount, and floods are only about 11% of calls. | Ruled out |
| CRM 14.1 | It went live October 2, but AHT jumped October 3. The October 9 patch changed nothing, because October 10-24 matches October 3-9. Slow screens would also tend to show up in hold time and after-call work, and both are flat. | Very unlikely as the main driver |
| IVR refresh | The timing matches to the day. The change hits every call type and every agent equally. The extra time is talk time, in the first couple of minutes, before the claim is discussed. | Best fit |

Your verification rules haven't changed, so every caller still has to pass ID checks. The IVR used to collect two of the data points automatically. Now the agent asks for them, the caller answers aloud, and the agent spells it back and keys it in, all within the handle time. About 1.8 minutes for two or three extra exchanges is plausible. It is also an even, flat cost per call, which matches the uniform rise you see.

A smaller second effect may be in play. IVR abandonment fell from 9% to 4%, so roughly 5% more callers now reach an agent. That adds volume, and it adds callers who were previously dropping out. Together with the longer calls, it explains why you miss the answer-time target in the afternoons, when the queue is already tightest.

**Why neither proposal fixes it**

- **12 temps.** Workload is roughly calls times handle time. Calls are up about 5% and handle time is up about 30% (6.1 to 7.9), so workload is up about 35%. Twelve temps add about 8% to a 140-agent floor. That wouldn't close the gap, and you'd be paying to do the ID-capture work by hand. The temps would also be new starters, who run slower at first.
- **CRM rollback.** The patch has already been out for two weeks with no effect on AHT. Rolling back adds risk and downtime and won't touch the cause.

**How to confirm it (a day or two of work)**

1. Pull the time from call connect to the start of the claim discussion, for calls in September and calls since October 3. QA's 40-call sample already points that way. If the gap is about 1.5-2 minutes, that settles it.
2. Check the same measure for tenured and new agents. It should be the same for both.
3. If you can, run a short test. Put the DOB and postcode prompts back on a share of IVR lines for a few days and compare AHT with the lines that don't have them. If the cause is what I think it is, AHT on the restored lines drops back toward 6.1.

**What I'd do**

- Don't bring in temps and don't roll back the CRM until the test is done.
- Ask the vendor and IT whether the IVR can capture the verification data in a less abandonment-heavy way. Options include a single prompt, matching on caller ID or policy number, or asking for the postcode only. Callers hung up at those prompts, but it was costing you less than the extra 1.8 minutes of agent time is costing you now.
- Decide the trade-off with numbers. The 5-point drop in abandonment is a real gain, but it matters only if the capacity to answer those calls exists. If the full set of prompts brings AHT back to 6.1 and abandonment up to 9%, compare that against the lighter option plus a few temps. Right now you have the benefit of the change and the cost of the change in different places on the dashboard.

**Caveats**

I'm assuming the agents are actually capturing the DOB and postcode by voice now and that nothing else in the script changed. Check that first with a few call recordings. If the first-two-minutes check shows no gap, I'm wrong, and the next place to look is the IVR hand-off itself, for example transfers that drop the caller's data or add a second greeting.
