Neither. The evidence points to the IVR refresh on October 3, and I'd hold off on both the temps and the rollback.

**What's going on (most likely)**

The IVR used to collect date of birth and postcode before the call reached an agent. Those prompts are gone. Your verification rules haven't changed, so every caller still has to pass ID checks. Agents now have to collect that information by voice, at the start of the call, and that work now lands in talk time. A 1.7 to 1.9 minute increase is about what you'd expect for asking, hearing and keying in a DOB and postcode, plus the repeats and corrections that come with it. The IVR also shed some callers who hung up at those prompts. Abandonment fell from 9% to 4%, so more calls now reach agents. That adds to the volume problem.

**Why the other explanations fail**

- **New agents (18 starters):** The rise is the same for tenured and new agents. New starters also run only about a minute slower, and they are 18 of 140 agents, so they can't explain a 1.8 minute rise across everyone. They also went live on September 26, a week before the jump.
- **CRM 14.1:** The rise began October 3, not October 2, and it didn't change after IT's October 9 patch. AHT for October 10-24 matches October 3-9, even though load times are reportedly back to normal. Slow screens would also tend to show up in after-call work or hold, and those are flat.
- **Floods:** Flood claims are about 11% of calls, and motor-only calls rose by the same amount. The floods can add a little to the average but they aren't the cause.
- **Talk-time only, early in the call:** QA found the extra time in the first couple of minutes, before the caller reaches the claim. That is the verification stage. It rules out claim complexity, system lag mid-call and wrap-up work.

The timing, the flat step-change pattern, the effect on every agent group and call type, and the location of the extra time within the call all match the IVR change. Nothing else matches all of them.

**What I'd do**

1. **Don't roll back the CRM.** It won't help, and it carries its own risk.
2. **Don't hire 12 temps yet.** If the cause is fixable, you'd be paying for capacity you only need because of a process gap. Temps may still be a short-term bridge for afternoon answer times if you can't fix this quickly.
3. **Confirm the cause in a day or two.** Pull the handle-time breakdown for the first 2 minutes on a sample of calls from before and after October 3. Compare the time agents spend on ID checks. Ask 5 to 10 agents what they now do at the start of the call. Compare calls the IVR still authenticates, if any, with those it doesn't.
4. **Fix it at the front.** The options are:
   - Restore only the DOB and postcode capture in the IVR, perhaps as a shorter, better-designed step (for example keypad entry rather than speech).
   - Pass the IVR-captured data to the agent's screen so it's pre-filled.
   - Have the IVR do the first verification step for known callers, such as matching the calling number.
   - Streamline the agent's verification script and CRM fields so it takes less time.

   The vendor was right that those prompts caused hang-ups, so the aim is to keep the abandonment gain while moving the data collection out of agent time. Some of the 5-point abandonment drop is also callers who were previously lost now reaching agents, so part of the cost of the gain is real.
5. **Tell the board** that the AHT rise is the cost of moving verification from the IVR to agents. Abandonment fell from 9% to 4% as a trade-off. The decision is how to get both benefits, not how to staff around the loss.

**Caveats**

I'm inferring this from the summary you gave me, not from the call data. If the first-two-minutes check shows the extra time is something else, such as greeting scripts or the new voice prompting more confusion, the same approach applies: fix the front of the call. If it shows nothing there, revisit the CRM, but the post-patch data makes that unlikely. If answer times can't wait for the fix, a smaller, short-term temp bridge is a reasonable hedge, but treat it as temporary.
