Neither. The evidence points to the IVR refresh on October 3, and in particular the dropped date-of-birth and postcode prompts. I would not hire temps or roll back the CRM yet.

**Why the IVR is the best fit**

- **Timing.** AHT jumped on October 3, the day the IVR changed. The new agents went live on September 26 and the CRM release was October 2. Neither lines up with the jump.
- **Tenured and new agents rose by the same amount.** If the new starters were the cause, tenured staff would be unaffected. This rules out the new-agent explanation.
- **Motor-only calls rose by the same amount.** This rules out the floods, which don't touch motor calls.
- **The CRM patch changed nothing.** IT patched on October 9 and says load times are normal. AHT for October 10–24 still matches October 3–9. A CRM slowdown would also tend to show up in after-call work and hold, and those are flat. A rollback is unlikely to help.
- **All of the increase is talk time, in the first couple of minutes before the claim.** That is the identification step. The IVR used to collect date of birth and postcode, and agents now have to ask for them on the call. Asking and keying in two extra details, repeating them, and sorting out mismatches plausibly adds about 1.7 to 1.9 minutes. Your verification rules didn't change, so the same checks are now done by agents and not by the IVR.
- **The 4% abandonment figure fits too.** Callers who used to hang up at the prompts now stay in the queue and reach an agent. That means more calls, with longer talk time each, landing on the same headcount. That would explain the afternoon answer-time misses.

**What the IVR change did to the numbers.** Fewer abandoned calls is good for customers, but it moved the work onto agents. The vendor's finding that most callers hung up at those prompts may be accurate. The cost is that your agents now carry that work.

**Why not the temps or the CRM rollback**

- Temps would add capacity, but they wouldn't fix the cause, and new starters are slower. You would pay to staff a process problem. Some extra capacity may still be needed once the cause is fixed. Calculate that after the fix.
- A CRM rollback carries risk and disruption, and the evidence doesn't point at the CRM.

**What I'd do**

1. **Confirm it quickly.** Have QA tag the first two minutes of the 40 calls you already have. Check whether the extra time is agents collecting date of birth and postcode. Compare the average ID-check duration with a few calls from before October 3 if you have recordings. Look at whether calls that previously abandoned at the prompts now have unusually long ID phases.
2. **Check whether the ID data can be gathered earlier.** Options include restoring the date-of-birth and postcode prompts only for callers who need them, offering them as optional keypad entry, or using caller-ID matching to pre-populate the record so the agent only confirms. Ask the vendor whether a shorter version, such as postcode only, keeps abandonment low.
3. **Measure the trade-off.** Abandonment fell from 9% to 4%, but AHT rose by about 30%. Compare the cost of the extra handle time with the value of the retained callers. A partial restoration may be best.
4. **Cover the afternoons in the meantime.** If you need relief before the fix, use overtime or shift changes for the afternoon peaks, not 12 permanent temps.

**Assumptions and caveats.** I can't see the call recordings or the system data, so this is the best-supported explanation and not a proven one. Two things would change my view. First, if QA finds the early minutes are spent waiting for screens, then the CRM is back in play. Second, if the ID phase didn't lengthen, I would look at the IVR's handoff, such as callers being misrouted or hearing a longer greeting. The pattern as described, though, points firmly at the IVR change.
