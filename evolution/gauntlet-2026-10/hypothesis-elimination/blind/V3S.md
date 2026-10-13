Neither. The most likely cause is the IVR change on October 3, which moved the date-of-birth and postcode collection from the IVR to your agents. Your own data points to it fairly directly.

**What the data rules out**

| Candidate | Why it doesn't fit |
|---|---|
| 18 new agents | Tenured and new agents rose by the same 1.7 to 1.9 minutes. A new-starter effect would hit the new group harder. They also went live on September 26, a week before the jump. |
| CRM release 14.1 | IT's patch on October 9 restored load times, but AHT for October 10-24 matches October 3-9. If slow screens were the cause, the fix should have moved it. Slow screens would also tend to show up in after-call work and hold, which are flat. |
| Flood claims | Floods are about 11% of calls, so they can't lift the average by about 30%. Motor-only calls rose by the same amount. |
| Hold or wrap-up changes | Hold and after-call work are flat. All of the increase is talk time. |
| Verification rules | Unchanged. But the rule is that every caller passes ID checks, and the IVR used to do part of that work. |

**What fits**

- The timing matches. The jump starts on October 3, the day the IVR changed, and it is a step change that has held for three weeks. A staffing or training effect would be gradual.
- The mechanism is simple. Callers now reach an agent without having given date of birth or postcode. The agent still has to pass ID checks, so they ask for both on the call, then wait while the caller answers, repeats and corrects. That plausibly adds 1.5 to 2 minutes of talk time, and it would affect every agent equally, which is what you see.
- QA's finding fits. The extra time is mostly in the first couple of minutes, before the caller gets to the claim.
- Abandonment fell from 9% to 4%. About 5% more callers now reach an agent, and some of them are the ones who used to hang up at the old prompts. They may be less prepared or more reluctant to answer, which can make the opening longer still.

I'm assuming "talk time" includes the opening ID exchange, and that QA's sample of 40 was not unusually skewed. Both are worth confirming.

**Why the two proposals are wrong**

- A CRM rollback targets a problem that has already been patched, and it carries its own risk. It is unlikely to move AHT.
- Twelve temps would add capacity to a workload that has grown for a reason you can remove. Temps also run slower at first, so they would add to AHT. At best this is an expensive and slow way to cover for a process change.

**How to confirm it quickly**

1. Have QA, or speech analytics, time the opening segment (greeting through ID complete) on calls from September and on calls from after October 3. If the cause is what I think, that segment grew by about the whole 1.8 minutes and the rest of the call didn't change.
2. Check whether AHT differs between callers who passed through the new IVR and callers who were transferred or came in another way. If you have any callers who still get the old prompts, that is a ready-made comparison.
3. If you can, restore the date-of-birth and postcode prompts for a share of traffic for a few days and compare AHT, abandonment and answer time.

**What to do about it**

- Put the prompts back in a shorter form. Options include collecting only one of the two items, asking for the policy number or using caller-ID matching to pre-identify known callers, and passing the captured data to the agent screen so they confirm rather than ask.
- Keep what is good in the refresh. The shorter menu and the lower abandonment are real gains. The aim is to keep the abandonment gain and recover the handle time.
- Weigh the trade-off honestly. The vendor's data showed callers hang up at those prompts, so restoring them may bring some of the 9% abandonment back. Even so, a 5-point abandonment gain is worth less than a 30% rise in handle time that causes you to miss answer-time targets every afternoon. Check the net effect on answered calls and answer time, not abandonment alone.
- Hold off on both the temps and the rollback until the opening-segment timing is in. If it doesn't show the effect, I'd come back to the data. The next candidates would be the new-caller mix and any change in how the IVR passes information to the agent screen.

For the board, the short version is that the increase is a process change that moved work from the IVR to the agents, not a staffing or software problem, and the fix is in the IVR design.
