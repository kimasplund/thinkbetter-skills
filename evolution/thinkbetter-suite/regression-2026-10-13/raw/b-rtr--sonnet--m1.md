# Decision Record: Checkout down after deploy

## Constraints
- **Deadline**: Now. Every minute costs about $2k, and about $8k is already gone.
- **Cost of delay**: Deliberating for 2 more minutes costs about $4k, which is as much as the gap between the options.
- **Quality floor**: Checkout back up as fast as possible. Root cause can wait.

## Options Considered
1. Roll back the deploy. About 6 min, fully reversible (you can redeploy later). Remaining loss is about $12k.
2. Ship the null-pointer hotfix. About 15 min, and it only works if the suspected bug is the real one. Remaining loss is about $30k, and more if the guess is wrong.
3. Wait and diagnose further. Open-ended, about $2k per minute, with no end date.

## Decision
**Chosen**: Roll back now.
**Rationale**: It is the fastest path to recovery and the cheapest, saving at least $18k against the hotfix. It doesn't depend on the null-pointer guess being right. The outage started right after the deploy, so rolling back is a strong bet, and you can undo it if it's wrong.
**How sure**: Fairly sure. It could be wrong if the rollback touches a migration or schema change that isn't backward compatible, or if the outage has a cause other than the deploy, such as a dependency that failed at the same time. Check for a migration before you start, and check checkout health 1 to 2 minutes into the rollback.

## Execution
- Start the rollback immediately.
- Have someone else start the hotfix in parallel. This costs no downtime, and it will be ready to ship once the fix is verified in staging.
- At about 3 minutes, confirm the rollback is progressing and error rates are dropping. At about 6 minutes, run a test checkout. If checkout is still failing after the rollback, the deploy wasn't the cause, so stop work on the hotfix and look at dependencies and infrastructure.

## Follow-up Required
- [ ] Confirm the null-pointer theory from logs and stack traces against the rolled-back build.
- [ ] Test the hotfix in staging and release it behind a canary or staged rollout.
- [ ] Add a deploy check that exercises checkout, and an automatic rollback if checkout errors spike after a release.
- [ ] Write up the incident: the roughly 10 minutes of downtime, the revenue impact, and how long detection took after the deploy.
