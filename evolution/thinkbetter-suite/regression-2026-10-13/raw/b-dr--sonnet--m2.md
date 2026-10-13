I'm assuming a typical product team: a mix of low-risk and high-risk code, and CI that already runs tests and linting. Adjust the specifics if that's wrong.

## Recommendation

Make review mandatory before merge for code where a mistake is expensive or hard to undo. Let everything else merge immediately, with review within a fixed time after. Decide which path a change takes by its risk, not by who wrote it or how urgent it feels.

## Why each side is right

**Review before merge** fits the incidents where bad code reached production and was costly or slow to reverse: security holes, data migrations, billing logic, auth, public API contracts. A reviewer catching these before merge is cheap. Cleaning them up afterward is not, and some can't be undone at all (leaked data, corrupted rows, charged customers). Pre-merge review also enforces knowledge sharing, because nobody can skip it.

**Merge first, review after** fits the incidents where work sat in a queue for days, authors context-switched, branches drifted into conflicts, and small fixes waited behind large ones. Most changes (copy, config tweaks, small refactors, internal tooling, well-tested bug fixes) are low risk and easy to revert. Blocking them taxes everyone to guard against a few.

## Why a simple split doesn't work

"Review half the PRs" or "review when you feel like it" fails because the author is the worst judge of their own risk, and the PRs that feel safe are the ones that hurt. A single global rule fails the other way: whichever you pick, you re-live the other side's incidents. The real question is not "review or no review" but "how reversible is this change, and how quickly would we notice it breaking?"

## The position

**1. Two lanes, chosen by a written, mostly automatic rule.**

*Gated lane (review before merge).* A change goes here if it touches any of:
- auth, permissions, secrets, or payment/billing code
- database migrations or anything that rewrites or deletes data
- public APIs, shared schemas, or infrastructure/deploy config
- paths listed in CODEOWNERS as sensitive
- a diff above an agreed size (say 400 lines), since big diffs hide problems

Enforce this in tooling: CODEOWNERS plus branch protection on those paths, so the gate applies automatically rather than by judgment.

*Fast lane (merge now, review after).* Everything else, provided CI is green. Requirements:
- The change is behind a feature flag, or can be reverted with one click.
- Tests and linting pass.
- Review happens within one working day. The PR stays open for comments, and findings become follow-up fixes.

**2. Make the fast lane safe, not just fast.**
- Auto-assign a reviewer on merge and track "merged but not yet reviewed" as a visible count. If it grows past a threshold (say 5 items or anything older than 24 hours), the team stops merging fast-lane work until it clears. This is what keeps "review afterward" from quietly becoming "never".
- Make revert a routine, practiced action with no blame attached.

**3. Make the gated lane fast, not just strict.**
- Target first response within 4 working hours on gated PRs, and treat that as a team commitment.
- Keep gated PRs small. Split risky changes from mechanical ones so the risky part is short and the mechanical part rides the fast lane.
- Allow one reviewer, not two, except for the highest-risk paths.

**4. Let the lanes adjust from evidence.**
Every few weeks, look at incidents and near-misses:
- If a fast-lane change caused a serious incident, add its path or type of change to the gated list.
- If a gated path produced no review findings over several months, consider moving it to the fast lane.

That turns the argument from "who is right" into "what does our own incident data say," which is the one thing both sides already agree is real.

## What this keeps and what it costs

Keeps from the review-first side: no unreviewed change can reach the code where damage is irreversible.
Keeps from the merge-first side: most changes ship without waiting, and the queue only holds work that deserves it.

Costs and open risks:
- Someone has to maintain the gated list, and the first version will be wrong in both directions. Expect to revise it in the first month or two.
- Post-merge review is weaker than pre-merge review because the pressure to fix things is lower. The backlog cap is the main defense, and it only works if the team actually honors it.
- A change that looks like fast-lane work can still cause a surprise (for example a small config change with large effects). Feature flags and fast reverts limit the damage but don't remove it.
- If your team lacks reliable CI or any ability to roll back quickly, the fast lane isn't safe yet. Fix that first, and until then make the gated lane broader.

## Suggested next step

Have each side list the incidents they cited and tag each one: would this change have been in the gated lane under the rules above? If the gated list catches the review-first side's incidents and the fast lane's reversibility rules would have spared the merge-first side's delays, you have your agreement. Where an incident doesn't fit either, that's the rule to adjust.
