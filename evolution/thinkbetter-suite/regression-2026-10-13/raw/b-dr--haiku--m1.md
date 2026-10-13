# Pre-merge review vs. merge-then-review: Two Positions and a Way Through

## Mandatory review on every pull request

The case for gating every change is that review catches defects while they are cheap to fix. A second person reads the diff before it touches shared code, which catches the bugs that the author is blind to, spreads knowledge of the codebase across the team, and creates a record of why a change was made. Teams that have been burned by a bad merge reach for this because the incident is vivid and the cost of a rollback is easy to see.

What this side gets right: review is a real safety control, and "we'll look at it later" tends to mean "nobody looks at it." Once review becomes optional, it quietly erodes.

Where it is strongest: code that is hard to reverse (data migrations, auth, billing, anything touching money or personal data), and code from people who are new to the codebase.

## Merge immediately, review afterward

The case for merging first is that waiting costs something real. A PR that sits for a day blocks the author, goes stale against main, and piles up merge conflicts. Review that happens after merge is still review, and it is often sharper because the reviewer is looking at what is actually running. Teams on this side have usually been burned by slowness: changes that took a week to land, people batching work into large risky releases, and reviewers who rubber-stamp under pressure anyway.

What this side gets right: review latency is itself a defect source, because big batched changes are harder to review well than small ones. Fast feedback from production is a form of review that a diff cannot give.

Where it is strongest: small, reversible changes with good test coverage and fast rollback.

## Where they collide

The two sides are not really arguing about whether review matters. They disagree about when the review happens and what it is allowed to block. A blanket rule either way fails the same way: mandatory review on everything makes trivial changes wait for a human who adds little, and merge-first on everything lets a risky change reach production before anyone has looked at it. Both sides cite real incidents, which tells you that the incidents differ in kind. Some came from changes that should have been reviewed before shipping, and some came from review that was slow enough to push people into bigger batches. A single policy cannot prevent both.

## Resolution: Risk-tiered review with a fast lane

Make the review requirement depend on what a change can break and how easily it can be undone, not on a team-wide rule.

- **Gate before merge** when the change is hard to reverse or touches sensitive areas: schema migrations, authentication and authorization, payments, data deletion, infrastructure config. One approving review is required, and these changes stay small enough to get a same-day review.
- **Merge first, review within a set window** for small, reversible changes that are covered by tests and can be rolled back quickly. The author ships, the reviewer reads the change within a fixed time (for example, the same working day), and anything the reviewer flags becomes a follow-up fix with priority.
- **Keep the fast lane honest** by making it conditional. Automated checks (tests, linters, security scanning) must pass before any merge. A change that touches a gated area or exceeds a size threshold drops back into the gated lane automatically, which can be enforced with path rules in the review tooling.
- **Fix the latency that drove people to merge first.** Set a review turnaround target for gated PRs, keep PRs small, and have someone own the review queue. Much of the appeal of merge-first is really a complaint about waiting, and removing the wait removes much of the pressure.
- **Measure both failure types.** Track escaped defects that a gated review would plausibly have caught, and track PR age and batch size. If the first rises, tighten the fast lane's criteria. If the second rises, the problem is review speed, not the policy.

Why this keeps the strengths of both: the risky changes still get a human read before they can hurt anyone, which is what the first side needs. The low-risk changes ship quickly and get reviewed right after, which is what the second side needs. Review becomes a function of risk, not a ritual applied to everything.

## What stays unresolved

- The line between "small and reversible" and "risky" will be argued over, and it will sometimes be drawn wrong. Expect to revisit the criteria after the first few escaped defects.
- Post-merge review depends on someone actually doing it. If the review window slips in practice, the fast lane quietly becomes no review at all, and the first side's concern returns.
- If your incidents are mostly from one specific kind of change, such as a particular service or a class of config edits, the right split may be narrower than described here. Pull the last ten incidents from each side and check which lane they would have landed in. That check would change the answer if the incidents cluster differently than the debate assumes.
