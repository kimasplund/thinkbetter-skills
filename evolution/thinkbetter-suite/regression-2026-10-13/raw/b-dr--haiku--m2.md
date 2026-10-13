The two camps are both right about different kinds of change. The mistake is treating "review" as one thing applied uniformly. Make the review depth depend on what a change can break, and make post-merge review a real control instead of a hope.

**What each side is protecting**

- **Mandatory pre-merge review** protects against changes whose mistakes are expensive or hard to undo: auth, payments, data migrations, shared infrastructure, public APIs. A bad change there can hit customers before anyone looks at it again, and the incidents your mandatory-review colleagues cite are probably in this group.
- **Merge-then-review** protects against the cost of waiting. When every change queues for a reviewer, small fixes sit for days, people batch large changes, and large changes are the ones that are actually hard to review well. Those costs are real, and the incidents your velocity colleagues cite are probably partly caused by big, rushed batches.

Neither side is wrong about its own failure mode. Where they go wrong is applying their rule to changes it doesn't fit.

**The synthesis: tier the review by blast radius**

1. **Define two or three tiers in writing.** For example:
   - *High risk* (auth, payments, migrations, shared config, public API contracts, anything touching data deletion): blocking review by someone who owns that area. No merge without approval.
   - *Standard* (ordinary feature and bug work inside a service): one approval, and the change may merge once automated checks pass. Reviewer is expected within a set time, such as one working day.
   - *Trivial* (docs, copy, dependency patch bumps, config behind a flag): merge on green checks, reviewed afterward by sampling.

2. **Make post-merge review a real control.** "Review afterward" fails in practice when nobody owns the queue. Require that every change merged without pre-review appears in a visible review queue, that someone is assigned to it, and that a change which fails review gets reverted or fixed within a set window. Track how many post-merge reviews find real problems. If that number is high, move that class of change up a tier.

3. **Put the safety in the release path, not only in the review.** Feature flags for anything user-visible, canary or staged rollout, and automated rollback on error-rate or latency regression. Much of what the velocity side wants is safe mostly because a bad change can be turned off in minutes, not because someone looked at it.

4. **Make automated checks the minimum bar for everything.** Tests, linting, type checks, and a security scan run before any merge, including the fast path. This is where the strict camp gets most of what it actually wants for ordinary changes.

5. **Review the review.** Every few weeks, look at the incidents that happened. Ask whether each one came from a change that was in the wrong tier. Adjust the tier list. This keeps the arrangement honest in both directions: if fast-path merges keep causing incidents, the strict side has evidence; if blocking review is catching nothing in a class of change, the velocity side has evidence.

**Why this holds up to both camps**

- The strict side keeps mandatory review exactly where a mistake is costly, and gets automated gates everywhere else.
- The velocity side keeps fast merges for the large majority of changes, with a reviewer named and a deadline attached instead of a vague "review later."

**What it does not solve**

- Tiering takes effort to maintain, and people will argue about which tier a change belongs in. Settle the rules once, in writing, and let the tier be set by the author with a reviewer able to escalate.
- Post-merge review only works if reviewers have time. If the team cannot staff the queue, the fast path quietly becomes no review at all. Check that capacity exists before adopting it.
- A change that looks small but touches a sensitive area will sometimes be misclassified. The escalation rule covers this, but it will still happen.

**A first step this week:** agree on the high-risk list (the areas where a bad change is most expensive), and turn on the fast path only for changes outside it, with automated checks required for both.
