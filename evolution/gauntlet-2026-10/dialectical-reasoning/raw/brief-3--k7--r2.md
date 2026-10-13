**Short answer:** Both are right about something, and neither position is the one to adopt. The finding is about *standing write* access to the ledger. It isn't about all database access. Your own data shows you can close it without crippling incident response.

**What each side has right**

- Mirela is right that standing write access to a production ledger is the thing auditors will not accept, and April is a hard deadline. Doing nothing, or only documenting it, won't close the finding.
- Anders is right that removing *all* access, including reads, would hurt. 91% of your sessions are SELECT-only, mostly support checking ticket status. And 38 of 41 Sev-1s were fixed through direct access in a median of 22 minutes. Losing that speed in a payments incident has real customer and financial cost.

**Where they are talking past each other**

They are arguing about "access" as one thing. Your logs split it into three very different things:

1. **Reads (about 91% of sessions).** The finding doesn't mention reads. Move support onto a read replica or a masked, read-only view with no write path. This removes most of the access volume and carries little audit risk. Check that the replica doesn't expose card data or other sensitive fields.
2. **Routine incident writes.** In 29 of 38 Sev-1 fixes, the write was one of three statements: re-queue a payout batch, release a settlement lock, or correct an FX rounding row. These are predictable, so they can be turned into reviewed, parameterized runbook actions (stored procedures or a small ops tool) that run under a service identity and log who ran them and why. Engineers then need no raw write access for about 76% of Sev-1 fixes.
3. **Novel writes (the remaining ~9 Sev-1s plus other cases).** These need real, ad hoc access. Give it as a time-limited, logged, break-glass grant, not a standing one.

**Proposal for Monday**

- Remove standing write access to the ledger. Mirela gets what the finding actually asks for, and that is the part you can show the auditors.
- Keep broad read access through a replica or masked view. Anders keeps the workflow that most engineers use daily.
- Build the three runbook actions first. They cover most incidents and should be fast, with one command or button and no approval step in the on-call path.
- Extend the existing access proxy to the ledger for break-glass writes. It already issues time-limited, logged grants for the card-vault cluster, so you aren't building from scratch. Anders's complaint that those grants are slow at 3 am is real, so fix that as part of the work:
  - The on-call engineer self-approves during a declared incident, with a mandatory reason and incident ID.
  - Review happens after the fact, within 1 business day, by a second person.
  - Grants last about 1 to 2 hours and are fully logged with session recording.
  - Measure grant time. Set a target of under 2 minutes and test it with an on-call drill.
- Look at the 270 on-call write sessions. Ask whether that many sessions for 38 Sev-1s means long or repeated sessions, or non-Sev-1 writes. Also look at the remaining 40 write sessions by non-on-call people. Understanding those tells you what else needs a path.

**Dates**

A hard cut on 31 January for everything is not necessary or wise. A phased plan fits better:
- By 31 January: standing write access removed for the ledger, replaced by break-glass grants (extending the proxy is the quickest way to do this), plus read access moved to the replica. This gives Mirela her date for the part the audit cares about.
- February to March: runbook actions for the three common fixes, then drills.
- Early April: collect evidence, such as grant logs, review records and the access list, so the follow-up review has proof, not a promise.

If the break-glass path can't be ready and tested by 31 January, don't remove write access without it. Take it to Mirela as an explicit trade-off, and agree on compensating controls in the meantime (for example, every write session recorded and reviewed within a day). Ask her whether the auditors would accept that interim position. I can't tell from here, so confirm it with them.

**How to say it to them**

- To Mirela: "We're removing standing write access by 31 January, which is the finding. We're doing it with controls the auditors can verify, not by removing reads and not by taking away the ability to respond to incidents."
- To Anders: "Standing write access goes away. In exchange, the three common fixes become one-step runbook actions, and break-glass self-approval will be fast. You have my commitment to measure 3 am grant time, and to change the design if it is slow."

**Risks to watch**

- Retention: Anders expects to lose senior people. A faster, better-designed process helps more than a promise does, and engineers who dislike the change should be involved in building the tooling.
- Break-glass can become the new standing access if it's easy to abuse. Watch grant counts and review them monthly.
- Self-approval during an incident may draw auditor scrutiny, so the after-the-fact review needs to actually happen and be documented.
- The data is one year of logs. Three common fixes may not cover next year's incidents, so keep the break-glass path.

**Assumptions:** I assumed the ledger can have a replica or masked view, and that the proxy can be extended to the ledger cluster. If either is wrong, the timeline moves and you'll want to tell Mirela early.
