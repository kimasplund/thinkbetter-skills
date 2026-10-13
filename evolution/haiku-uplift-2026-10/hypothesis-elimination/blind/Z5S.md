Neither option is supported by the data. Based on what you've described, the most likely cause is the October 3 IVR change, specifically dropping the date-of-birth and postcode prompts.

**Why the IVR change fits and the others don't**

| Candidate | What it predicts | What the data shows | Verdict |
|---|---|---|---|
| New agents (Sept 26) | Increase concentrated in new starters | Tenured and new agents rose by the same 1.7–1.9 min | Ruled out |
| CRM release 14.1 / Oct 9 patch | Jump starts Oct 2, and drops or levels off after the Oct 9 patch | Jump starts Oct 3, and Oct 10–24 is the same as Oct 3–9 | Ruled out, or at most a minor contributor |
| Harnley floods | Increase concentrated in flood calls | Motor-only calls rose by the same amount | Ruled out |
| IVR refresh (Oct 3) | Jump starts Oct 3, extra time is early in the call, talk time only | Jump starts Oct 3, all of the increase is talk time, extra time is in the first couple of minutes | Strongest fit |

The mechanism is straightforward. Your verification rules have not changed, so every caller still has to pass ID checks before an agent discusses a policy. The IVR used to collect date of birth and postcode before the call reached an agent. Now the agent collects them live, which adds roughly the two minutes QA heard in the first part of the call. Hold and after-call work are flat because the work itself hasn't changed, only where it happens. The fact that the IVR also cut abandonment means more callers reach agents, but that doesn't change how long each call takes.

**Why temps are the wrong fix**

Adding 12 temps would not reduce handle time. New starters are not the cause, since tenured agents slowed by the same amount. Temps would add more agents with the same per-call time, so they would only help if the queue is short-staffed, and handle time would stay at 7.9 minutes.

**Why rolling back the CRM is unlikely to help**

The CRM slowdown started on October 2, but the jump started on October 3, and it did not recover after the October 9 patch. If slow screens were the cause, the October 9 fix should have brought handle time down. It didn't.

**What to do**

1. Confirm before you change anything. Pull a sample of recordings or timestamps from October 3 onward and measure how long the identity check takes from the moment the call connects. A larger sample than 40 calls would make this solid.
2. Compare handle time for calls that come through the IVR before and after October 3, if your telephony data lets you split them.
3. If the check is the cause, restore the date-of-birth and postcode prompts in the IVR, or collect them through a faster self-service step, and keep the verification rule as it is. Watch whether handle time returns to about 6.1 minutes within a week. Abandonment may rise somewhat, so weigh that against the handle-time gain.
4. Keep the CRM patch under review, but don't roll it back on this evidence.

**Assumptions**

- Your telephony data separates talk time from hold and after-call work, as your numbers suggest.
- The October 3 IVR change went live for all callers on that date, not gradually.
- Nothing else changed in the contact centre around October 3, such as call routing or scripts.
