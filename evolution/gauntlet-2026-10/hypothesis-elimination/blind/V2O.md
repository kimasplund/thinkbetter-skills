**Short answer: neither the temps nor the CRM rollback. The most likely cause is the IVR refresh on October 3. Dropping the date-of-birth and postcode prompts moved that data capture from the IVR to your agents' voices.**

## What the evidence rules out

| Candidate | What your data says | Verdict |
|---|---|---|
| New agents (live Sept 26) | Tenured and new agents rose by the same 1.7 to 1.9 minutes. New starters should be slower, and the gap should widen or shrink as they learn. | Ruled out as the cause. They add a small constant drag, about a minute each on 18 of 140 agents. |
| CRM 14.1 | Slow screens would show up as hold time and after-call work. Both are flat, and all the increase is talk time. AHT was also unchanged after the October 9 patch (Oct 10-24 equals Oct 3-9). | Ruled out. A rollback wouldn't move AHT. |
| Harnley floods | Motor-only calls rose by the same amount, and floods are only about 11% of October calls. | Ruled out as the main driver. They add a little to the mix. |
| Tougher verification | Your rules haven't changed. | Ruled out as a rule change. See below. |
| IVR refresh | The timing matches exactly (Oct 3). The extra time is in the first couple of minutes, before the claim. It hits every agent group and every call type, and it hasn't faded. | Fits everything. |

## The likely mechanism

Every caller still has to pass ID checks. Before October 3, the IVR collected date of birth and postcode, so the agent saw them on screen and only had to confirm. Now the agent asks for them, waits for the answers, keys them in, and handles the callers who stumble. About 1.7 to 1.9 minutes of extra talk time is plausible for that, especially with mis-hears and repeats. QA's finding that the time sits in the opening minutes fits this.

There is a second effect. Abandonment fell from 9% to 4%, so roughly 5 to 6% more calls now reach an agent than before, with no change in staffing. Some of those callers were the ones hanging up at the identity prompts. They are now being carried through the longest and most manual version of the call. So you have more calls and longer calls hitting the same 140 agents, which is why you miss the answer target in the afternoon peak.

## Check this before you act

I'm inferring this from your summary, not from direct measurement, so confirm it quickly:

1. Have QA, or a speech-analytics tool, time the segment from call connect to "identity verified" on 20 to 30 calls from September and 20 to 30 from October. If the gap is about 1.5 to 2 minutes, that settles it.
2. Check whether the AHT jump is the same on callers who passed ID with no friction. If it is, look at the greeting and the call opening scripts as well.
3. Check whether AHT is higher in the afternoon than in the morning. If it isn't, the problem is per call, not a volume spike.

If the opening segment is not longer, I'd go back to the new voice and shorter menu. A different greeting or call routing could change what callers say first. But the first test should show a clear difference.

## What I'd do

- **Don't roll back the CRM.** It would cost you a change window and risk, and the data says it won't help.
- **Don't hire 12 temps yet.** Temps would cover the symptom at ongoing cost, and they'd run slower than your tenured staff. If the answer-time miss is severe this week, use overtime or a short-term shift change, not a hiring commitment.
- **Fix the IVR.** The vendor was right that the prompts caused hang-ups, but the fix shouldn't push the work to agents. Options, roughly in order of effort:
  - Capture the postcode only, or only the date of birth, in the IVR, not both.
  - Use caller-ID matching to pre-fill the policy and ID details when the number is recognised, and only ask when it isn't.
  - Use a short, well-phrased prompt with keypad entry for the identifier, instead of speech.
  - Send an SMS link for ID capture for callers who can't do it by voice.
  
  Run the change as an A/B test on a share of calls, so you see AHT and abandonment together. The goal is to keep abandonment near 4% and get AHT back toward 6.1 minutes.
- **Keep the abandonment gain in view.** The board should know that part of the AHT cost is the price of 5 fewer lost calls per 100. If you get a partial fix, you may still need a few agent hours at peak, but size that after the fix, not before.

**Confidence:** about 75 to 80% that the IVR change is the main cause. The elimination of the other candidates is strong, and the IVR test above would move this to about 90%.
