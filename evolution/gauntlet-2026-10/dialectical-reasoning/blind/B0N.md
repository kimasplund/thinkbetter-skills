**Short answer:** Both are right about something, and neither position is the one to adopt. The audit finding is about *standing write access*, not about all access. Your own data shows you can close it without crippling incident response.

**What each side has right**

- Mirela is right that standing write access to a ledger is a real control failure, and that the finding must be closed by April. Her 31 January date is also reasonable if it applies to *standing write*.
- Anders is right that incident response depends on fast production writes: 38 of 41 Sev-1s were fixed that way, with a 22-minute median. Losing that speed in a payments processor costs real money and customer trust.
- Where they talk past each other: Mirela is asking for "all access" removed, but the finding only says "write." Anders is defending "direct access," but what his data defends is a small set of fast, *available* writes.

**What your numbers say**

- 91% of sessions are SELECT-only, mostly support checking transaction status. These don't need to be touched for the finding. Removing them would hurt support for no audit gain. (Reads of the ledger may still need to be logged or masked, so check that with Mirela, but that is a separate question.)
- Only 310 of 14,200 sessions (about 2%) wrote data, and 270 of those were on-call during incidents. That is about 40 writes outside incidents, which should be easy to move into a ticketed or change-managed path.
- In 29 of the 38 Sev-1 fixes (76%), the write was one of three statements: re-queue a stuck payout batch, release a settlement lock, or correct an FX rounding row. These can be turned into pre-approved, reviewed, parameterised actions (stored procedures or a small runbook tool) that run under a service identity, with every execution logged. No human holds raw write access, and the fix takes seconds.
- The remaining 9 Sev-1s needed ad hoc writes. That's the case for a break-glass path.

**Recommended design**

1. **Remove standing write access** for all engineers by 31 January. This satisfies Mirela's date and the finding itself.
2. **Build the three common fixes as audited actions**, callable by the on-call engineer without a grant. Aim to have these live before the cutover, since they cover most of the incident writes. Add a second-person confirmation for the riskiest ones (the FX row correction, for instance) if the auditors will expect it.
3. **Break-glass for everything else**: on-call can self-grant time-limited write access (say 1-2 hours) with a mandatory reason and incident ID, with automatic alerting to security and a post-incident review of every use. Reuse your existing access proxy, since it already issues time-limited, logged grants for the card-vault cluster.
4. **Fix the 3 am friction**: Anders says the card-vault grants are slow. Find out why (approval wait, MFA, tooling?) and design the ledger flow so the on-call engineer's own request is enough, with review afterwards rather than approval beforehand. Test it with a game day at night before cutover.
5. **Keep read access** for support, ideally through a read replica or masked views, and with logging. Treat that as a follow-up, not part of the finding.

**Things I'd check before Monday (I'm assuming these, since I can't verify them)**

- Whether the auditors will accept self-approved, time-limited, logged break-glass access with after-the-fact review. Ask them now, not in April. This is the biggest risk to the plan.
- Whether the 270 incident-time write sessions were mostly the three common statements. If so, the automated actions may cover more than 76%.
- How many of the roughly 40 non-incident write sessions were routine and can be turned into a normal change process.
- Whether the proxy can support the ledger database without major work. If not, give the work a firm date, and use a stopgap such as an on-call-only role that is enabled only while an incident is open.

**What to tell them on Monday**

*To both:* "We are closing the finding by removing standing write access, not by removing all access. The decision is made; the debate now is about implementation."

*To Mirela:* "You get your 31 January date for standing write access. I'm not removing read access this month, because it isn't what the auditors flagged. In exchange, I need you to agree the break-glass design with the auditors this week."

*To Anders:* "Nobody keeps raw write access, but you won't lose speed on the cases that matter. The three common fixes become one-command actions, and the rest go through a self-service break-glass that you will help design and test at 3 am. If the 22-minute median gets worse after cutover, we revisit the design, not the control."

*Owners and dates:* Anders owns the three automated actions and the on-call grant flow. Mirela owns the audit conversation and the alerting. Draft by the end of next week; night-time game day before cutover; a 30-day review of every break-glass use after cutover.

**On retention:** Anders' worry about losing senior people is a real signal about how this is delivered. Involving him in the design, rather than handing him a restriction, is likely the best mitigation.
