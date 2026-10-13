Short answer: neither. The most likely cause is the October 3 IVR change. Agents now have to collect the date of birth and postcode that the IVR used to collect, and that adds about 1.8 minutes of talk time to every call.

**Why the other explanations don't fit**

- **New agents:** the 18 new starters would raise AHT for new agents, and only a little for the team overall. You see the same 1.7 to 1.9 minute rise for tenured and new agents, so this isn't it.
- **CRM 14.1:** slow screens would mostly show up as hold time and after-call work, and the problem should have eased after the October 9 patch. All of the increase is talk time, hold and after-call work are flat, and AHT for October 10-24 matches October 3-9. A rollback would cost you a disruptive change and fix nothing.
- **Floods:** flood calls are about 11% of volume, so they couldn't produce a rise this large across all calls. Motor-only calls rose by the same amount, which rules them out.
- **Timing:** the step change starts on October 3, the day of the IVR refresh, not on September 26 or October 2.

**Why the IVR fits**

- Your rules say every caller passes ID checks before the policy is discussed. The IVR used to capture DOB and postcode before the call reached an agent. Since October 3 the agent has to ask for them, wait for the caller to answer, sometimes repeat them, and key them in.
- That matches QA's finding that the extra time is in the first couple of minutes, before the claim. It also matches the extra time being talk time, because the agent is now speaking with the caller during that stretch.
- It affects every call type and every agent equally, which is what you see.
- The size is plausible. About 1.8 minutes (roughly 110 seconds) is realistic for asking, hearing and confirming two ID fields, especially with stressed claimants and an unfamiliar flow.

**The abandonment drop is part of the same story**

Abandonment fell from 9% to 4%. That means more callers now reach an agent, roughly 5% more of the offered calls. Some of those would have hung up at the old prompts and may be less prepared. So the IVR change has made each call longer and has also increased the number of calls agents answer. Together those explain why you miss the answer-time target in the afternoons, when volume peaks. Fewer abandons is good, but the vendor's figures counted only that gain and not the handling cost.

**What I would do**

1. **Confirm it this week, which is cheap.** Ask QA to time the identification segment on a sample of calls from before and after October 3. Check whether AHT rose across all hours or only in busy ones. If your telephony system can split a call into segments, compare the time to first policy lookup. I expect around 1.5 to 2 minutes added to the opening.
2. **Fix it at the source.** Put DOB and postcode capture back into the IVR, but in a shorter form, such as keypad entry rather than speech. Or have the IVR collect only a policy number or caller ID match and pre-populate the CRM screen. Ask the vendor why abandonment fell, because the cause may be the speech recognition or the length of the menu and not the ID questions. You may be able to keep the shorter menu and the new voice and bring back only the data capture.
3. **Test before rolling out.** Route a share of calls, say 20%, through the revised IVR and compare AHT and abandonment with the current flow. You are trying to keep the abandonment gain while recovering most of the 1.8 minutes.
4. **Temps:** don't hire 12 yet. If the fix recovers the time, you won't need them. If the fix is slow, a small, short-term top-up for afternoon peaks is a reasonable stopgap. As a rough check, 140 agents at 6.1 versus 7.9 minutes is about a 30% capacity loss, so staffing to cover it permanently would take far more than 12 people. That is another reason to fix the cause.
5. **CRM:** leave 14.1 in place. Keep an eye on load times, but the data gives no case for a rollback.

**Assumptions and caveats**

I don't have call-segment data, so this is the best-supported explanation and not a proven one. If the timing test shows the opening hasn't lengthened, the next thing to check is whether the new IVR is passing wrong or incomplete data to agents, or whether callers are arriving more confused after the new menu. The main point is that the evidence points to a process change on October 3 that adds work to every call, not to staffing or to the CRM.
