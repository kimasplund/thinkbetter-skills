**Short version:** propose consolidating the platform, not the codebase. Move Lanternway's infrastructure and tooling onto your cloud and Kubernetes on a staged timeline, keep the Elixir routing engine, and get the bundling benefit through a shared API, identity and billing layer. Take the Go rewrite off the table for now and put it on a gated "revisit" decision. This gives Odalys most of what she is after, and it is much easier for Ilse and the engineers to commit to.

## Why this shape

Odalys's case has three parts: the $900k a year of duplicated cost, a single codebase, and the ability to bundle. They don't all require the same thing.

- **The cost savings come mostly from infrastructure and tooling.** Elixir runs fine in containers on Kubernetes, so the $900k doesn't depend on a rewrite. (This is an assumption. Ask Lanternway what the $900k is made of. If a large share is people or licences tied to the stack, the picture changes.)
- **The cloud move has a second payoff.** You are about $1.2M a year under your committed spend. Moving Lanternway's workloads onto your provider uses commitment you are already paying for. Your real saving may therefore be larger than $900k, and it makes the infrastructure move easy to defend to finance. Check with finance how much of the shortfall Lanternway's workloads could absorb.
- **Bundling needs a common surface, not a common language.** Single sign-on, one customer and tenant model, unified billing, and a consistent API in front of both products are what sales needs. Those can ship well before any rewrite.
- **The rewrite is the part with the worst risk-to-benefit ratio.** The engineers who wrote the routing engine are the people you most need to keep, and a rewrite is the thing they say is riskiest. The rewrite's benefit (one language) is mostly a hiring and maintenance convenience, not revenue.

## Constraints that shape the plan

1. **Pellworth (31% of Lanternway's revenue).** Moving clouds very likely adds your provider as a subprocessor, or changes where their data is processed. You agreed to give 120 days' notice before adding a subprocessor. So the notice clock is on the critical path, and the migration of anything touching Pellworth data can't start cutover until 120 days after notice. Have legal read the clause this week. Then plan Pellworth's workloads as a deliberate, last or near-last wave, and consider approaching their security team early and collaboratively instead of just sending a notice. A botched move on a customer that renewed for three years in May is the most expensive failure available.
2. **Ilse's earnout runs through next December.** A big migration or rewrite during that window can depress her product's revenue through outages, slowed feature work, or customer churn, and she'd bear the cost personally. If you ask her to commit to a plan that puts her payout at risk, you will get compliance at best. Either protect the earnout explicitly (for example, agree how migration-related disruption is treated in the calculation, with legal and finance involved) or sequence the risky work after the measurement period. Raise this with her openly before the offsite instead of waiting for her to raise it.
3. **The April retention vest.** A single tranche means the engineers are free to leave right after it. Two of them wrote most of the routing engine, which makes them a single point of failure. Whatever you decide, the plan should include a second retention mechanism that runs past April (a follow-on grant or milestones tied to the migration), and a deliberate knowledge-sharing effort, such as pairing platform engineers with the routing engine's authors, so the engine stops depending on two people.
4. **"End of next year" is a deadline, not a fact.** Treat it as the target for infrastructure consolidation and stage the work so that it holds under the constraints above.

## Proposed phasing

- **Now to the offsite:** Confirm the $900k breakdown and the commitment-spend absorption with finance. Get legal's reading of the Pellworth clause and the earnout terms. Talk one-on-one with Ilse, and with the two routing-engine authors.
- **Phase 1 (first half of next year):** Shared identity, billing and API surface, plus shared tooling (CI, observability, secrets). Containerise Lanternway services and stand up a parallel environment on your cloud. This is mostly reversible and mostly invisible to customers.
- **Phase 2:** Migrate non-Pellworth workloads in waves, each with rollback criteria. Send the Pellworth subprocessor notice early enough that cutover isn't gated on it.
- **Phase 3 (end of next year):** Pellworth workloads, decommission the old cloud, and capture the savings.
- **Rewrite:** Not in the plan. Set a decision point after the earnout period and the infrastructure move. Decide then, using evidence (hiring difficulty, incident rates, change velocity in the Elixir code), whether any selected services should move to Go, one at a time, behind stable interfaces.

## How to get real commitment

Commitment comes from people having shaped the plan and having their main risk addressed, not from a persuasive presentation.

- **Before the offsite, not at it.** Meet Ilse and the Lanternway engineering leads individually, state what you're leaning toward, and ask what would make it fail. Use their answers to change the plan. A plan they can point to and say "that part is mine" is worth far more than a polished one.
- **Give each party what they need.**
  - Odalys: the savings, the unified customer experience, and a firm date for infrastructure consolidation, which she can show the board.
  - Ilse: protection of her earnout, a say in sequencing, and ownership of the routing roadmap.
  - Lanternway engineers: no forced rewrite, a clear role in the platform, and retention beyond April.
  - Your platform team: a meaningful, high-visibility job (the platform build, the migration tooling, the shared services), and an honest, evidence-based path to the Go question later. They agreed to the rewrite, so tell them first and explain the reasoning instead of letting them find out in the room.
- **Be explicit about what you gave up.** Tell Odalys that single codebase is deferred, not abandoned, and why. Tell the platform team the same.
- **Make the decision criteria visible.** Agree up front on what would trigger a rewrite later, so nobody feels the question has been buried.
- **Define a joint working group** with members from both teams, and with Ilse, owning the migration plan and reporting progress, so the plan belongs to people on both sides.
- **At the offsite**, present a recommendation with the trade-offs and open risks stated, and ask for specific commitments from each person. Remember that the aim is explicit agreement on the plan and on what is deferred.

## Risks I'd name in the room

- The Pellworth notice period slips and delays cutover.
- Key engineers leave after April regardless.
- The earnout creates a conflict of interest between Ilse's payout and the migration timeline. Surface it and handle it openly.
- The savings estimate turns out smaller than $900k once the migration cost itself is counted. Include one-time migration cost in the case.

If you can tell me what makes up the $900k, what the Pellworth contract says on data location, and what the earnout formula looks like, I can tighten this into a one-page version for the offsite.
