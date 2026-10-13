**Short answer:** Mirela is right about what has to go, and Anders is right about what has to survive. Both of them are arguing about the wrong object. The audit finding is about *standing write access*. It says nothing about engineers being unable to touch the ledger during an incident. Your logs show you can remove the first without losing the second.

## What the finding actually requires

The finding reads "standing write access to the production ledger database." Auditors will want to see that writes happen only through a controlled, logged, time-bound path, and that nobody holds a permanent ability to write. They will not need engineers to lose all database access. Mirela's "remove all access by 31 January" goes further than the finding does, and that extra reach is what makes Anders's incident-response objection serious.

## What your own numbers say

- **Reads are not the problem.** About 12,900 of 14,200 sessions (91%) were SELECT-only, mostly support engineers checking a transaction's status. Removing that access would hurt support for no audit gain. It should be fixed by reducing exposure, not by blocking it. Either give support a status lookup (a read replica, a masked view or a small internal tool) or keep reads on a standing read-only role with logging. Decide which with Mirela based on whether the ledger holds data she considers sensitive on read.
- **Writes are rare and highly repetitive.** Only 310 sessions wrote data, and 270 of those were the on-call engineer during an incident. In 29 of the 38 Sev-1 fixes (76%), the write was one of three statements: re-queue a stuck payout batch, release a settlement lock, or correct an FX rounding row. Those three do not need an engineer typing SQL into a production shell. They can be packaged as named, parameterised, pre-reviewed operations.
- **The other 9 Sev-1 fixes** (plus the roughly 40 non-incident write sessions) are the true "unknown SQL" cases. They are the ones that need a genuine break-glass path.

## What I'd tell them on Monday

**1. Standing write access ends on 31 January, for everyone.** That gives Mirela her date and closes the finding as written. Nobody keeps a permanent write role on the ledger.

**2. The three common fixes become runbook actions.** Build them as stored procedures or a small internal tool: re-queue payout batch, release settlement lock, correct FX rounding row. Each one takes validated parameters, runs as a service identity, logs who invoked it and why, and can be invoked by the on-call engineer without any access request. This covers about three quarters of Sev-1 writes at close to today's speed, and it is *safer* than today, because the engineer can no longer run an unreviewed UPDATE by accident at 3 am. Have Mirela's team review each of the three procedures once, up front, instead of reviewing every use.

**3. Everything else goes through break-glass, using the proxy you already have.** You issue time-limited, logged grants for the card-vault cluster. Extend that to the ledger, and fix the thing Anders is right about, which is that the grants are slow at 3 am. Options, in order of preference:
- Make the grant automatic when the engineer is the acknowledged on-call for an open Sev-1, with no human approver in the loop. The control is that the incident exists, the engineer is on the rota, the grant is short (for example 60 to 120 minutes) and every statement is recorded.
- For non-incident writes, or anyone who is not on call, require a second approver.
- Review every break-glass use the next business day. A recurring review is the evidence auditors actually look for.

Before 31 January, time the grant flow end to end. If it takes more than a minute or two for an on-call engineer, the grant flow isn't ready yet, and that is the thing to fix first.

**4. Reads.** Treat these as a separate decision. Don't let the read-access question hold up the write change. If the ledger reads are sensitive, move support onto a replica or tool by April. If not, keep a standing read-only role with logging, and be prepared to justify that to the auditors.

## On Anders's risk and Mirela's date

- Anders's fear that this will "cripple incident response" is true of a blanket removal. It is not true of this design, where about three quarters of the writes get no slower and the rest add a short automated grant. Ask him to define the acceptance test: for example, median Sev-1 time-to-fix stays within a few minutes of 22 on a game-day drill. That turns the argument into a measurement.
- Mirela's 31 January date is feasible for the standing-access removal only if the three runbook actions and the on-call auto-grant exist by then. If they don't, do not remove access in a gap with nothing behind it. Schedule a date by which both are ready, and tell the auditors the plan and the date. The follow-up review is in April, and a documented, partly implemented remediation with dates is usually better received than a rushed one that causes an outage.

## What this does not settle

- **The 9 non-routine Sev-1s are slower under break-glass.** Even an automated grant adds some delay, and these are the hardest incidents. Accept that cost knowingly, and review these cases to see whether any should become a fourth runbook action.
- **Runbook actions can themselves be misused.** Whoever can invoke them can still change ledger state. Limit who can call them, rate-limit them and alert on unusual use.
- **The 22-minute median includes diagnosis**, not just the write, so the grant delay will not add 22 minutes to anything. But I'm assuming here that your grant flow can be made fast. Test that assumption with a drill before you commit to the date.
- **Assumptions I made:** the ledger database can sit behind the same access proxy as the card vault, and the on-call rota is reliable enough to drive an automatic grant. If either is false, the timeline moves.

**Confidence: about 80%** that this closes the finding and keeps incident response intact. The main uncertainty is how fast the break-glass grant can be made in practice, and how the auditors view an automatic on-call grant. Ask Mirela to confirm that with them early.
