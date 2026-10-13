**Decision: roll back now.** Start the rollback immediately and do not wait on the hotfix.

**Why**

- **Rollback** finishes in about 6 minutes. Checkout would be back around minute 10 of the outage, so roughly $12k more is lost.
- **Hotfix** needs about 15 minutes to write and ship, plus verification time that the estimate does not include. Checkout would be back around minute 19 or later, so roughly $30k more is lost, and an untested fix could fail again.
- Rolling back works whether or not the null-pointer bug is the real cause. It is also fully reversible: you can redeploy the new release once the fix is ready.

**Quality floor:** checkout accepts payments again, with no new errors in the logs for 5 minutes after the rollback.

**Sacrifice:** the release's features are off until the fix ships.

**Parallel, if someone is free:** keep working on the null-pointer hotfix on a branch. Do not deploy it until it passes staging or a smoke test.

**Follow-up**
- [ ] Confirm checkout error rate is back to baseline after rollback.
- [ ] Reproduce the null-pointer bug and confirm it is the cause.
- [ ] Ship the fix, then redeploy with a canary or staged rollout.
- [ ] Add a check for this failure to the pre-deploy tests.
- [ ] Write a short incident record: the deploy, the outage window, the revenue impact, and the decision.
