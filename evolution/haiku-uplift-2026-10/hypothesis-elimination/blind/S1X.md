Neither temps nor a CRM rollback is the right first move. The evidence points to the IVR change from October 3.

**What is most likely happening**

Before October 3, the IVR collected the caller's date of birth and postcode. Agents got callers who were already partly verified. On October 3 you removed those prompts, but your rule still says every caller passes ID checks before a policy is discussed. So agents now run that verification themselves, live, at the start of every call. That is extra talk time in the first couple of minutes, which is what QA heard. It is also the only change that lines up with the timing:

- The jump starts on October 3, the day of the IVR refresh. It does not follow the CRM release (October 2) and it does not follow the flood claims, which began in late September.
- AHT did not recover on October 10 to 24, even though the CRM patch went in on October 9. So the CRM is not the driver.
- Motor-only calls rose by the same amount as flood calls. Flood complexity cannot explain that.
- Tenured and new agents rose by the same 1.7 to 1.9 minutes. New starters being slower would show up as a gap between the two groups, and there isn't one. The 18 new agents are also a small share of about 140, so they cannot account for a rise of this size.
- Hold and after-call work are flat. All the extra time is in talk time, which fits verbal verification.

**Why temps won't help**

Temps add capacity. They do not shorten calls. If every call now carries roughly 1.8 extra minutes of verification, adding staff only spreads that cost across more people.

**What to do**

1. Confirm it before changing anything. Pull call-level data for October 3 to 24 and split talk time into the first two minutes and the rest. Check whether the first-two-minute segment is where the increase sits, and whether it is the same for motor and flood calls. Forty QA calls is a useful signal but a small sample.
2. Restore the verification data earlier in the journey. Options, in rough order of preference: put the date of birth and postcode prompts back in the IVR, or have the IVR pass the caller's identifiers into the CRM so agents see a pre-filled check to confirm rather than collecting the details from scratch. Ask the IVR vendor which option is cheapest to build.
3. Accept the trade-off if you keep the shorter IVR. Abandonment fell from 9% to 4%, so more callers now reach an agent. That is a real gain, but it adds workload, and it may explain part of the answer-time miss independently of handle time. Measure it rather than assuming.
4. Leave the CRM alone for now, since its patch appears to have worked. Keep the temps as a contingency for the answer-time target while the verification fix is built.

**Assumptions**

I have assumed the IVR change is the only one that altered what agents do at the start of a call, and that the verification rules are applied to every caller in the same way. If the call-level data shows the extra time sits somewhere other than the first two minutes, the conclusion changes and the CRM and flood explanations need another look.
