**Short answer:** Don't propose "migrate everything by end of next year" or "rewrite in Go." Propose a staged convergence: move the platform layer first (cloud, CI/CD, observability, identity, data), keep the Elixir routing engine running as-is, and make the rewrite-or-keep decision on evidence in a later gate. Then build the commitment by letting Ilse and the Lanternway leads help design the gates, rather than presenting them with a finished plan.

## Why the facts point this way

1. **The $900k saving is mostly not in the rewrite.** Duplicated infrastructure and tooling (cloud, CI, monitoring, security tooling) can be consolidated by moving the runtime and operations onto your platform without changing the language. A rewrite adds cost and risk to a saving you can mostly get without it. Ask finance to split the $900k into infrastructure, tooling and people, because I'm guessing at the split.
2. **The $1.2M annual commit shortfall changes the economics.** You are already paying for cloud capacity you aren't using. Moving Lanternway's workloads onto your provider could absorb part of that shortfall, so the net saving from migrating infrastructure may be larger than the headline. It also gives a good reason to do the infrastructure move first. Check what the contract counts toward the commit, and whether the shortfall is penalized or rolls over.
3. **Pellworth is a hard constraint, not a detail.** Lanternway is 31% of... its revenue comes from one customer who just renewed for three years and has a contractual 120-day notice requirement before any new subprocessor. Moving Lanternway to your cloud provider likely adds a subprocessor, so you must give Pellworth 120 days' notice, and their security team may want to review it. Put that on the critical path. Talk to Pellworth early, through the account owner and not through a legal notice, and treat the migration date as no earlier than notice plus 120 days. Verify whether your provider is already on their list through your own product, and whether the contract language covers moves between regions or providers.
4. **The earn-out creates a conflict of interest that you should state openly.** Ilse's payout depends on her product's revenue through next December. A rewrite or migration that distracts engineers or causes outages directly lowers her payout. She also controls whether her team commits. Neither side should pretend this isn't happening. Decide with legal and finance how the earn-out is protected, for example by excluding migration-caused revenue impact, or by agreeing that migration work won't be a reason for a shortfall. Without this, her support is not credible, and her team will see it.
5. **Retention vests in one tranche next April.** After that date, the people who wrote the routing engine have no financial reason to stay. A rewrite plan that depends on them is a plan that depends on people who may leave. That argues for two things. First, put in place a second retention mechanism (new grants vesting over the migration, tied to milestones) before April, not after. Second, spread engine knowledge now (documentation, pairing with the platform team, and a named backup for each of the two authors). The "bus factor" is the biggest technical risk here, bigger than the language.
6. **Both sides are partly right.** Odalys is right that two stacks, clouds and codebases are expensive and that bundling needs a coherent product. Lanternway's engineers are right that rewriting a working optimization engine is high-risk, especially one with two key authors and a revenue-linked earn-out. The platform team's Go rewrite is a means, not the goal. Separate the goals (cost, one product surface, one operating model) from the solution (Go).

## What I'd propose at the offsite

**Goal, in Odalys's terms:** one operating platform and one customer-facing product surface by end of next year, with the cost savings realized, without putting Lanternway's revenue or people at risk.

**Phase 1 (now to roughly Q2): prepare and protect.**
- Start Pellworth notice and conversation. Fix the date constraint.
- Agree the earn-out protections and the new retention arrangement.
- Document and spread knowledge of the routing engine.
- Define success measures together: cost, reliability (SLOs), latency or route quality, and delivery.

**Phase 2 (mid-year onward): move the platform, not the engine.**
- Run the Elixir services on your Kubernetes and cloud, and adopt your CI/CD, observability, security and identity. Elixir runs fine in containers.
- Put an API gateway or shared interfaces in front so sales can bundle: single sign-on, single billing, a common API. That meets the bundling goal without a common codebase.
- Track the actual savings and the commit absorption.

**Phase 3 (a decision gate, around the end of Phase 2): decide on the engine.**
- Options: keep Elixir as a supported language in the company, rewrite incrementally (strangler pattern, service by service, with shadow traffic comparing results), or leave it.
- Decide using data: how hard it is to hire and support Elixir, incident rates, cost of the remaining duplication, and the team's views. Write the criteria now so that the gate is not a re-fight.
- If a rewrite is chosen, do it after the earn-out period ends (past next December) and the retention is secured, and one service at a time with a rollback.

Be honest with Odalys that this may mean "fully on our platform" is met by the platform layer and not by language uniformity. If she insists the codebase be Go, the cost of that insistence is the risk above, and she should choose it knowingly.

## How to get real commitment

- **Before the offsite, talk to people one at a time.** Meet Ilse privately first, then Lanternway's two engine authors and tech lead, then your platform lead, then Odalys. Ask what each needs and what they fear. Do not first present the plan in a group.
- **Name interests, not positions.** Odalys wants savings and a bundle. Ilse wants her earn-out and her team's future. Lanternway's engineers want to avoid a risky rewrite and a loss of status. Platform wants a coherent stack and meaningful work. The staged plan gives each a visible win.
- **Give Lanternway real decision rights.** Let Ilse and a Lanternway engineering lead co-own the migration plan and the Phase 3 criteria. Have them set the technical gates. People commit to plans they helped write.
- **Give the platform team a real job.** They lead the infrastructure move and build the shared tooling, which is substantial. Make clear the Go rewrite isn't rejected, only deferred and made evidence-based. Platform should also be part of the Elixir assessment, with a fair test.
- **Make it safe to say no.** Agree in advance what happens if a gate fails: the schedule moves and nobody is blamed. Commitment is weak if the only allowed answer is yes.
- **Put the commitments in writing.** Owners, dates, measures, what happens if Pellworth's notice or the earn-out protections slip, and a monthly review with both teams present.
- **At the offsite, ask for a decision on a small number of things:** the phased approach, the Pellworth plan, the earn-out and retention protections, and the Phase 3 criteria. Do not ask for the language decision.

## Things I'm assuming or can't see

- That the Elixir engine can run in your Kubernetes environment without major issues (very likely, but have Lanternway validate it).
- That retention grants and the earn-out can be adjusted by leadership and legal.
- That a new cloud provider counts as a subprocessor change for Pellworth. Check the contract.
- That the $900k figure includes the cost of people. If it assumes headcount reductions, that will damage trust and retention, so be careful how it is communicated, especially before April.
- I haven't seen the quality of the engine's code or the platform team's capacity. Both could change the Phase 3 answer.

If you can only do three things in the next three weeks, do these: get the Pellworth contract language checked, meet Ilse and the two engine authors privately, and get finance's breakdown of the $900k and the commit shortfall.
