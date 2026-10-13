# Pull Request Review: Two Positions and a Way Through

I'm assuming a typical product team with CI, a main branch that deploys, and the ability to revert quickly. If you ship firmware or handle regulated data, shift the lines below toward the stricter side.

## Review before merge on every PR

This side has seen what happens when nobody looks. A bad migration, a leaked credential, an auth check quietly removed. Each of these got through because the author was too close to the change. Review before merge is the only point where a second pair of eyes can stop damage instead of reporting it. It also spreads knowledge of the codebase, keeps conventions from drifting, and makes the author explain their reasoning. After a change is merged and deployed, "we'll look at it later" tends to mean never. Reviewers also lose the leverage to ask for changes once the code is live and others build on it.

## Merge now, review after

This side has seen what happens when review becomes a queue. A one-line fix waits two days. Authors context-switch, branches go stale and conflict, small improvements stop being worth the effort, and people batch changes into larger PRs that are harder to review well. Blanket review also trains reviewers to rubber-stamp. A reviewer who skims thirty trivial diffs a week gives a weaker check on the dangerous one. With good CI, feature flags and fast rollback, the cost of a mistake on most changes is small and the cost of waiting is paid every day.

## Where They Collide

Both camps are right about different changes. The incidents cited on each side most likely come from different kinds of change: the "should have been reviewed" incidents involve changes that are hard to undo or hard to see (data, auth, money, infrastructure), and the "review killed us" incidents involve changes that are small, easy to revert, and low in blast radius.

A simple compromise such as "review half the PRs" or "review if you feel like it" fails because it leaves the sorting to individual judgment in the moment, which is exactly when people under deadline pressure misjudge. It also keeps the costs of both: still a queue, still gaps. The real disagreement is not review versus speed. It is that one uniform rule is being applied to changes with very different risk.

## Resolution: Review Scaled to Risk, with a Safety Net Behind It

Sort changes by how costly they are to get wrong and how hard they are to undo, then match the review to that, with a fast after-the-fact check on the rest.

**Tier 1: Review before merge (blocking).** Changes that are irreversible or high blast radius:
- Database schema or data migrations
- Auth, permissions, secrets, payments, anything touching personal data
- Infrastructure, deploy pipeline, CI config
- Public API or contract changes
- Changes to shared core libraries
- Any PR over a size threshold (for example 400 changed lines), because large diffs hide problems

Make the path paved: path-based ownership rules (CODEOWNERS) enforce this automatically so nobody has to decide. Set a response target, such as first review within 4 working hours, and treat missing it as a team problem rather than an author problem.

**Tier 2: Merge on green, review within a day (non-blocking).** Everything else: small, reversible changes in ordinary application code, docs, tests, copy, dependency patch bumps. Conditions to qualify:
- CI passes, including tests and linters
- Change is behind a flag or can be reverted with a single command
- Author tags a reviewer, who reviews within one working day

If the post-merge review finds a problem, it is fixed forward or reverted, and the finding is logged.

**Tier 3: Trivial, review optional.** Typos, comments, formatting handled by tooling.

**Rules that make it hold:**
1. Tiering is decided by file paths and size, not by the author's opinion. Authors may escalate a PR to Tier 1 but never demote one.
2. Pre-merge review is kept short by design: reviewers check correctness and risk, not style, which the linter owns.
3. Post-merge review has teeth. Unreviewed Tier 2 merges older than a day are surfaced on a dashboard or in standup, so "later" does not become "never."
4. Use incidents to adjust the tiers. When a Tier 2 change causes a real incident, ask what about it should have been Tier 1 and move that path or pattern up. When Tier 1 review repeatedly catches nothing in some area, consider moving it down.
5. Review the review: once a month, check how many post-merge reviews found real issues and how long Tier 1 PRs waited. Those two numbers tell you whether the line is in the right place.

**What each side keeps.** The review-first camp gets a hard gate exactly where their incidents happened, and the gate cannot be skipped by someone in a hurry. The merge-fast camp gets near-zero wait on the bulk of changes, smaller PRs, and reviewer attention concentrated where it matters. Both get a way to fix the line when it turns out to be wrong.

## What Stays Unresolved

- The boundary will be argued over. Whether a given area is Tier 1 or Tier 2 is a judgment call, and some people will feel the line is too strict or too loose. The monthly check keeps that argument tied to data.
- Post-merge review is weaker than pre-merge review for what it catches, because the code is already live. If your rollback is slow or your tests are thin, Tier 2 is riskier than it looks, and you should shrink it until CI and rollback improve.
- Small teams of two or three may find that the tiering overhead exceeds its value, and simply reviewing everything quickly is better.
- Review debt can still accumulate in Tier 2 if the team gets busy. The dashboard helps only if someone looks at it.
- What would change this answer: a regulatory requirement for independent review of all changes (then everything is Tier 1 and the work moves to making review fast), or a track record showing Tier 2 incidents at a rate the team will not accept.

A sensible way to start is a four-week trial with the Tier 1 list above, then adjust it using the first month's incidents and review wait times.
