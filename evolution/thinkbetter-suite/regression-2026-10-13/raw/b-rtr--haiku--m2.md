**Decision: roll back now. Don't hotfix.**

**Why:**
- The outage started right after the deploy 20 minutes ago, so the deploy is the most likely cause. Rolling it back removes the change that broke checkout.
- Rollback finishes in about 6 minutes. The hotfix needs about 15 minutes to write and ship, and that doesn't include verification. From now, the hotfix path costs about $30k in lost revenue before the fix is live, against about $12k for the rollback.
- A rollback is easy to reverse. A hotfix written under this pressure, with a suspected null-pointer bug not yet confirmed, could fail and extend the outage.

**Steps:**
1. Start the rollback immediately.
2. Watch the checkout error rate and successful-payment rate. Both should recover within a few minutes of the rollback completing.
3. If checkout is still failing 10 minutes after the rollback starts, the deploy was not the only cause. Then look at the null-pointer path in the logs, and consider the hotfix as the next step.

**Assumptions to check while the rollback runs:**
- The rollback doesn't need a database migration reversal or a config change that would break on the older version. If it does, tell me and I'll reassess quickly.
- The null-pointer suspicion is a lead, not a confirmed cause. Don't ship the hotfix on that alone.

**Follow-up after checkout is stable:**
- Reproduce the null-pointer bug in staging and write the proper fix with a test.
- Add a deploy gate or canary for checkout so a bad release is caught before full rollout.
- Write a short incident record: deploy time, rollback time, duration, and lost revenue.
