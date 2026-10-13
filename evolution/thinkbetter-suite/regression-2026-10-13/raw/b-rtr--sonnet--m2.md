**Roll back now.**

Why:

| Option | Time to fix | Added loss at $2k/min | Risk |
|---|---|---|---|
| Rollback | about 6 min | about $12k | Low. It restores the last known-good state. |
| Hotfix | about 15 min | about $30k | Higher. The null-pointer cause is only suspected, and a wrong guess costs another cycle. |

Rollback is about $18k cheaper even if the hotfix works the first time. It is also the safer bet, because the outage began right after a deploy and a rollback doesn't depend on your diagnosis being right.

**Do this:**
1. Start the rollback immediately and say so in the incident channel.
2. At the 3-minute mark, confirm it is progressing. If it is stuck or failing, escalate to the person who owns deploys instead of switching to the hotfix.
3. When it finishes, test a real checkout end to end and watch the error rate and order volume return to normal.
4. In parallel, have one engineer start on the null-pointer fix on a branch. Don't ship it until it has been tested against the failing path and a rollback plan exists.

**Caveats to check as you go:**
- If the deploy included a database migration that isn't backward compatible, rollback may not be clean. Check that in the first 30 seconds. If it's a problem, tell me and the answer changes.
- The null-pointer bug is still an unconfirmed suspect. Don't treat it as the root cause until the logs show it.

**Follow-up after recovery:**
- [ ] Confirm the root cause from logs and the diff.
- [ ] Add a test covering the null-pointer path.
- [ ] Review why the deploy had no canary or automatic rollback. A 4-minute outage should have tripped an alert and a revert automatically.
- [ ] Write a short post-incident note covering the timeline, the decision, and the roughly $12k of loss during the rollback.
