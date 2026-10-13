Both Mirela and Anders are right about different parts of this, and the audit finding does not require choosing one of them. What the finding names is standing write access. Anders's concern is about having a fast, reliable way to write during an incident. Those are separate problems, so you can close the first without giving up the second.

**What the logs say**

- About 91% of sessions are read-only. Support engineers checking transaction status don't need write access at all, so removing it from them costs nothing.
- Writes are rare: 310 write sessions in 12 months, and 270 of them came from the on-call engineer during an incident.
- The writes that matter are narrow. In 29 of the 38 Sev-1 fixes, the write was one of three statements: re-queueing a stuck payout batch, releasing a settlement lock, or correcting an FX rounding row. The other 9 fixes are not described in what you sent, so I can't say what they needed.

**Mirela's position, and what it gets right**

Standing write access to a production ledger is exactly what the auditors flagged, and "we'll be careful" is not a control. Access that is permanent, unlogged to a specific purpose, and not tied to a person's current role is the thing to remove. Her 31 January date gives you time to demonstrate the change before the April review.

**Anders's position, and what it gets right**

Incident response is time-sensitive, and the fastest path for the three common fixes is direct database access. If on-call engineers have to wait for approvals at 3 am, the median of 22 minutes will get worse, and the people carrying that pager are the ones most likely to leave. He is also right that a blanket ban would push engineers toward workarounds that are harder to audit.

**Where they actually conflict**

The conflict is not "access versus no access." It is "standing access versus access granted at the moment it is needed, for a stated purpose, and recorded." Those are different controls, and the second can satisfy the auditors while keeping the speed Anders needs.

**What I would tell them on Monday**

1. **Remove standing write access to the production ledger for everyone.** Read-only access stays, which covers the 91% of sessions with no change.
2. **Turn the three incident statements into approved, parameterised runbook actions.** Re-queue a payout batch, release a settlement lock, correct an FX rounding row. Each takes an identifier and returns a before/after record. On-call engineers can run these directly with a time-limited, logged grant issued through the existing access proxy, the same mechanism the card-vault cluster already uses. This covers the 29 of 38 fixes that used these statements.
3. **Make the grant fast.** Pre-approve the on-call rota for these actions, so the grant is issued on pager acknowledgement with no ticket queue. Anders's complaint about slow grants at 3 am is a process problem and can be fixed without adding standing access.
4. **Keep a break-glass path for everything else.** Any other write needs a grant with a second approver, or a named senior engineer's approval, and a post-incident review. This handles the 9 unexplained fixes and any future cases the runbook does not cover.
5. **Review each write after the incident.** Every write gets a short record: who, what statement, which incident, and why. This is what the auditors will want to see.

**Why this should satisfy both of them**

Mirela gets a system where no engineer can write to the ledger outside a logged, time-limited, purpose-specific grant, which is what the finding asks for. Anders keeps the three fixes that resolved most of last year's Sev-1s, and the on-call engineer's path is shorter than the current direct access, because they run a known action rather than composing SQL under pressure.

**Residual risks**

- The runbook actions have to be right. A wrong parameter in a scripted release is still a production error, so each one needs tests and a dry-run mode.
- Some incidents will need an ad hoc write the runbook does not cover. Those will be slower, and that is intended, but you should expect a few painful nights before the runbook is complete.
- The 9 Sev-1 fixes not covered by the three statements need to be reviewed to see whether they point to more runbook actions.

**Before you commit to the date**

I am assuming the access proxy can issue grants scoped to specific actions and not only to a database role. If it can only grant a role, the runbook actions will need a thin service in front of the database, and that will take longer than the time before 31 January. Check that first, because it determines whether the January date is realistic.

Sincerely,
Your assistant
