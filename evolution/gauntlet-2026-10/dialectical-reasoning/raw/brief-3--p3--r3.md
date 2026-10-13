# Corvane Pay: closing the ledger access finding

## Short answer

Mirela and Anders are each right about something, and each is wrong about the scope of the fix.

- Mirela is right that standing write access to the ledger can't stay. That is what the finding says, and engineers fixing production by hand on a standing grant is a real control gap in a payments processor.
- Anders is right that removing all access would hurt incident response. Last year engineers fixed 38 of 41 Sev-1 incidents with direct database access, at a median of 22 minutes.
- The finding is about standing write access, not about database access. Your own logs show those are very different populations, so the two positions don't have to collide.

## What your logs say

- 91% of the 14,200 sessions (about 12,900) were SELECT-only, mostly support checking a transaction's status. They are the bulk of the access and have almost nothing to do with the finding or with incidents.
- Only 310 sessions (about 2%) wrote data, and 270 of those were on-call engineers during incidents. That leaves about 40 writes outside an incident. Those 40 are the ones to review first, because nobody can yet explain them.
- In 29 of the 38 Sev-1 fixes, the write was one of three known statements: re-queue a stuck payout batch, release a settlement lock, or correct an FX rounding row. These are routine operations that happen to be done through a raw database session. They don't need raw write access.
- Only about 9 incident fixes in a year (plus the 3 Sev-1s not fixed through the database) needed an ad hoc write. That is rare enough to put behind a stronger control than the other cases.
- One gap in the numbers: 91% read-only plus 2% writes leaves roughly 7% of sessions (about 970) I can't classify from what you gave me. Find out what they are before Monday. They may be mixed or administrative sessions that change the picture.

## Proposal: three tiers of access

**1. Reads: keep them, but not on the raw ledger.**
Support's status checks should go through a read replica or a masked view, or a read-only role with no write grant, with sessions logged. This keeps the 91% working and takes it out of the finding. Whether auditors also want reads on sensitive fields restricted is a question for them (see the last section).

**2. The three common fixes: turn them into audited operations.**
Wrap the payout re-queue, the settlement-lock release and the FX rounding correction as reviewed procedures or runbook commands. The on-call engineer runs them with parameters, and the tool performs the write under a service identity. Each run is logged with who ran it, why, and which incident it was tied to. No database grant is needed and nothing is slow at 3 am. This covers about 29 of 38 incident fixes, and it is an improvement over today, because a reviewed procedure can't also issue a stray `UPDATE`.

**3. Everything else: break-glass through the proxy you already run.**
The proxy already issues time-limited, logged grants for the card-vault cluster. Extend it to the ledger, but fix what makes those grants slow at 3 am:
- Make the grant self-service once a Sev-1 is declared and tied to the incident ticket, with no human approver in the loop. Target under 2 minutes.
- Limit it to the on-call engineer and the incident commander, with a short expiry (for example 1 to 2 hours) and full statement logging.
- Add a second-person review of the session within 24 hours, which is the compensating control. Review after the fact, not approval beforehand, so it doesn't add time during the incident.
- Alert the security channel whenever a grant is issued.

The cost to incident response is about the grant time for roughly 9 incidents a year, plus whatever the procedures save on the other 29. If the grant takes 2 minutes, the 22-minute median barely moves.

## What to tell them on Monday

**To Mirela:** Standing write access to the production ledger ends by 31 January. There will be no engineer accounts with write permission. Every write is either a reviewed procedure or a time-limited, logged, incident-linked grant with after-the-fact review. That is a defensible answer to the finding, and it produces evidence the auditors can sample. Full removal of every form of access isn't needed to close this finding, and it would give you no more assurance than this does.

**To Anders:** Incident response keeps a write path. The 29 routine fixes get faster and safer, and the rare ad hoc fix goes through a break-glass grant that you will help design so it works at 3 am. Your job is to specify the grant flow and the procedures and to own the target time. If it can't be made fast enough, the numbers will show it and we revisit.

**To both:** One owner for each tier, a date for each, and a rule that nobody reopens the argument until the April review is done.

## Timeline

- Before Monday: classify the roughly 970 unclassified sessions and the 40 non-incident writes.
- By mid-December: ship the three procedures and extend the proxy grant to the ledger. Run a game-day test of a 3 am grant.
- By 31 January: revoke all standing write access. Leave the read path in place.
- February to April: collect the evidence (grant logs, reviews, a few real incidents). The auditors will want to see the control working, not just configured, so you need at least a couple of months of operating history before April.

## Risks and open points

- **Break-glass can become standing access under another name.** Watch for grants issued on weak pretexts or reviews that get skipped. Report grant volume and review completion monthly, and treat a rising count as a signal to build another procedure.
- **The auditors may not accept this design.** Show them the plan now, not in April. Ask specifically whether read access to ledger data needs restricting and whether after-the-fact review is acceptable for break-glass.
- **Procedures can be wrong.** The three wrapped fixes need code review, tests and parameter limits (for example, a cap on the size of an FX correction), or you move the risk rather than remove it.
- **Retention.** Anders's concern about losing senior people is real, but the proposal addresses its cause: engineers keep the ability to fix production quickly, and what they lose is the unlogged, unreviewed way of doing it.

I'd put my confidence at about 75% that this closes the finding and keeps incident times near where they are. It depends on the auditors accepting after-the-fact review and on the grant flow really working in under 2 minutes at 3 am, and neither is tested yet.
