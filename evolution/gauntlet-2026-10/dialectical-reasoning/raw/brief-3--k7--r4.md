Short answer: both are right about what they are protecting, and neither position is the fix. The finding is about *standing write access*, not about database access in general. That lets you close it without cutting engineers off from the database.

**What each side has right**

- Mirela is right that standing write access to a ledger is the thing auditors flag, and that "we trust our engineers" is not a control. A 31 January deadline for removing the standing access is reasonable, and it leaves you about two months of margin before April.
- Anders is right that incident response depends on fast writes. 38 of 41 Sev-1s were fixed through the database at a 22-minute median. Removing all access would make that slower, and the attrition risk is real.

**What your data says**

- 91% of sessions were SELECT-only. Most of this access is support engineers checking a transaction's status. That is a read problem, and it has nothing to do with the finding.
- Only 310 of 14,200 sessions (about 2%) wrote data. 270 of those were on-call engineers during incidents. The remaining 40 or so are unexplained, and you should find out what they were before Monday.
- In 29 of the 38 Sev-1 fixes (76%), the write was one of three statements: re-queue a payout batch, release a settlement lock, or correct an FX rounding row. These are known, repeatable operations.

The pattern is that nearly all the risk (writes) is in a small, predictable set of actions, while nearly all the volume (reads) is low risk. Blanket removal and blanket retention both ignore this.

**Proposal to take on Monday**

1. **Remove standing write access for everyone by 31 January.** This gives Mirela the control the finding asks for. Standing read access can stay, but check that the ledger tables don't expose sensitive fields. Mask or restrict those if they do.
2. **Turn the three common fixes into pre-approved, audited operations.** Put them behind runbook tooling, such as stored procedures or a small service with fixed parameters. The on-call engineer triggers them, nobody needs a database grant, and each call is logged with the incident ID. That covers about three quarters of Sev-1 writes with no manual grant step. It is also easier for auditors to accept than a human with raw write access.
3. **Use break-glass for the remaining writes.** You already have the access proxy that issues time-limited, logged grants for the card vault. Extend it to the ledger. Anders's complaint that the grants are slow at 3 am is a design problem you can fix:
   - Let the on-call engineer self-approve during a declared incident, with the incident ticket as the required justification. A second approver is needed only after the fact.
   - Pre-authenticate the on-call rotation so a grant takes seconds, and time-box it (for example 1 to 2 hours).
   - Record full session logs and have someone review every break-glass use within one business day.
4. **Measure it.** Time a grant request end to end in a drill. If the median is more than a minute or two, fix that first. Track Sev-1 time-to-resolve after the change against the 22-minute baseline.

**What to say to each of them**

- To Mirela, you will have no standing write access by 31 January, every write will be attributable to a named person and an incident, and you will deliver evidence for the April review (logs, review records, the access policy). Ask her to agree that incident-bound, self-approved, time-limited grants count as compliant. Confirm this with the auditors early rather than assuming it.
- To Anders, the three common fixes become one-command operations, and break-glass will be tuned to take seconds at 3 am. His team owns the grant-speed target and the tooling for the three operations. If the Sev-1 resolution time gets materially worse in the pilot, you adjust.

**Risks and caveats**

- I'm assuming the auditors accept just-in-time access with after-the-fact review as closing "standing" access. This is typical, but check it with them now.
- The three-statement tooling takes engineering time. If it can't be ready by 31 January, ship break-glass first and the tooling second. Break-glass alone already removes the standing access.
- Self-approval invites abuse, so the post-use review matters. Without it, Mirela will rightly object.
- I don't know what the roughly 40 non-incident write sessions were. If they are routine data fixes, they probably need their own ticketed process.
- Support engineers need to keep their read access for tickets, ideally through a read replica or a status-lookup tool rather than the production ledger.

**Bottom line**

Neither of them should "win". Mirela wins on the principle (no standing write access), Anders wins on the outcome (fast incident response), and the design above keeps both. Present it as one joint plan with a pilot and measurable success criteria rather than a ruling in either direction.
