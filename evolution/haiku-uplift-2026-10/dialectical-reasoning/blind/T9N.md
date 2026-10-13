Short answer: both Mirela and Anders are right about different parts of this, and the audit finding can be closed without giving up the incident fix path. Remove standing write access for engineers. Replace it with narrow, time-limited, logged write grants that on-call engineers can get in minutes. Make read-only access the default for everyone else.

**Where each of them is right**

- Mirela is right that standing write access is what the auditors flagged. Whether it gets used 310 times or 3 times a year, the standing capability is the finding.
- Anders is right that direct database access is what fixed 38 of 41 Sev-1 incidents, at a 22-minute median. Removing the path with no replacement would slow incident response and would likely push out the people you least want to lose.

**What the logs say**

- 91% of the 14,200 sessions were read-only, mostly support checking transaction status. These people do not need write access at all, so removing it from them costs nothing.
- Writes are concentrated. 270 of the 310 write sessions were on-call engineers during an incident.
- 29 of the 38 Sev-1 fixes used one of three statements: re-queueing a stuck payout batch, releasing a settlement lock, or correcting an FX rounding row. That is a short, known list, so it can be built as named operations instead of ad hoc SQL.

**Proposed plan**

1. Now: remove standing write access on the production ledger for all engineers. Keep read-only access for support and on-call.
2. Before 31 January: build the three common fixes as named runbook actions. Each one runs only its own statement, takes parameters, is logged, and is granted per incident through the access proxy. Ideally this needs no ticket.
3. Before 31 January: set up a break-glass grant for the remaining writes, which are the ad hoc Sev-1 fixes. It should require an open incident ID, approval from the on-call lead or a secondary, a time limit (about 60 minutes is a reasonable starting point), and session recording. Reuse the card-vault grant mechanism, since the auditors and the CISO already accept it there.
4. Address Anders' 3 am complaint directly. If the incident ID is linked to an open Sev-1 in the paging system, the grant can be approved automatically. Track time-to-grant as a metric, with a target to be agreed (for example, under 5 minutes).
5. Run a drill on a non-production copy or a Sev-2 scenario in December or early January, so the first real use is not on 31 January.

**What to tell them on Monday**

- To Mirela: standing write access goes by 31 January, with no exceptions for standing access. Incident writes move to time-limited, logged, scoped grants. The audit finding closes on that change.
- To Anders: incident write access stays, but it becomes scoped and pre-approved. The three common fixes get built first, and the platform team owns making grants fast at 3 am.
- To both: name an owner and a date for each of the three runbook actions and for the break-glass tooling, and schedule the drill now.

**Assumptions I made**

- The access proxy can issue grants for the ledger database the way it does for the card vault.
- The nine Sev-1 writes outside the three common statements can be handled case by case through break-glass.
- The auditors will accept time-limited, logged, per-incident grants as closing "standing write access." Confirm this with them before April, using the card-vault precedent.

**Residual tension**

Some future Sev-1 will need a write outside the three runbook actions, and those will take longer than 22 minutes because of the approval step. Some on-call engineers will still find grants slower than direct access did. Those costs are the price of closing the finding, and the goal is to keep them small and measured, not to eliminate them.
