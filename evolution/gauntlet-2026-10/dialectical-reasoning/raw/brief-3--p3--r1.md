Neither of them is right as stated, and you don't have to choose between them.

**Where each is right**
- **Mirela is right about the finding.** The finding is about standing write access. Your logs show how little of it gets used: 310 write sessions out of 14,200 (about 2%), and 270 of those were on-call engineers during incidents. The other 40 are unexplained. Standing write is far broader than the work needs, and auditors will not accept "we trust our engineers."
- **Mirela is wrong that all access must go by 31 January.** The finding doesn't require that. Removing the 91% read-only use, which is mostly support checking ticket status, doesn't reduce write risk. It would only push support onto escalations.
- **Anders is right that incident response depends on fast database action.** 38 of 41 Sev-1s were fixed that way, with a 22-minute median. Any design that adds friction at 3 am will cost real money and real people.
- **Anders is wrong that the answer is all or nothing.** In 29 of those 38 fixes the write was one of three known statements: re-queue a stuck payout batch, release a settlement lock, or correct an FX rounding row. Those don't need an engineer holding open write access. They need a controlled way to run three actions.

**What to tell them on Monday**
Standing write access to the ledger ends by 31 January, which meets Mirela's date. Incident capability is replaced, not removed, in three tiers.

1. **Routine writes become pre-approved actions.** Package the three statements as reviewed, parameterised procedures or runbook commands. The on-call engineer runs one with a ticket or incident ID. It is fully logged, and the engineer needs no database grant. Mirela's team reviews the actions once, in advance, instead of reviewing every use. This covers about 76% of the Sev-1 fixes (29 of 38) with almost no added delay.
2. **Anything else needs an emergency grant from the access proxy you already run.** The proxy already issues time-limited, logged grants for the card vault. For the remaining 9 Sev-1 fixes, use the same mechanism with a different approval rule:
   - The on-call engineer self-approves while an incident is open, and the grant is tied to the incident ID.
   - It expires automatically, in about 2 to 4 hours.
   - The security channel is notified immediately.
   - A second person reviews every use the next business day.

   Anders's objection that card-vault grants are slow at 3 am is an objection to that workflow, not to the idea. Fix the workflow: a pre-authenticated request path and a target of under 2 minutes to get a grant. Don't carry over the card-vault approval steps.
3. **Reads get their own treatment.** Don't remove them in this round, since the finding is about writes. Do move routine support lookups to a read replica or a masked status view, so they don't touch the ledger primary. Then tighten ledger-primary reads to on-call and a short named list. Mirela will probably want this eventually, and it is easier to do once the write path is settled.

**Do these before committing to the plan**
- **Measure the emergency grant path.** Run a night-time drill with on-call engineers and time it from page to a working write. If the added delay is more than a few minutes on the 9 non-routine fixes, fix it before cutover. The 22-minute median is the number to protect.
- **Explain the 40 write sessions outside incidents.** If they are migrations, backfills or manual corrections, they need a change-ticket path, not an incident path. Also check the roughly 7% of sessions that are neither read-only nor writes. That is about 970 sessions the breakdown doesn't account for, possibly mixed or administrative.
- **Check the 9 non-routine fixes for repeats.** If any recurs, turn it into a fourth pre-approved action.
- **Plan for evidence.** The auditors return in April. Two months of logs showing zero standing write grants, every action tied to an incident ID, and reviews completed will close the finding. A policy document alone won't.

**Suggested timeline**
- Weeks 1 to 3: build and review the three actions, and set up the emergency grant rule.
- Weeks 4 to 6: run the drill, fix the friction, and publish a short runbook.
- By 31 January: revoke standing write access.
- February to March: collect the review evidence.

**On the risk of losing senior people**
Tell Anders directly that the on-call path is being designed with his team, and that its success measure is the 22-minute median holding. People leave over unsafe or humiliating processes, and a fast, well-designed one is neither. Tell Mirela that she gets the outcome she needs by the date she set, with evidence that holds up. She doesn't get a blanket removal of access, which the data doesn't justify.

**Main assumption**
This assumes the proxy can attach a grant to an incident ID and notify automatically. If it can't, that is the first engineering task, and it is more important than the 31 January date.
