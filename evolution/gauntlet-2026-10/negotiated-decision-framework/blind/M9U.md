**Recommendation: move Lanternway's infrastructure and tooling onto your platform by the end of next year, keep the Elixir routing engine, and make the rewrite a separate decision with its own gate.**

I'm assuming "your cloud" is the committed-spend provider, and that Lanternway's customer data would move with the infrastructure.

**Why this beats both camps' positions**

Odalys's case has two parts, and they separate cleanly:
- **The $900k of duplicated infrastructure and tooling** comes mostly from running a second cloud, a second CI/observability stack and a second set of vendor contracts. You can remove that without rewriting any code. Elixir/BEAM services run fine in containers on Kubernetes.
- **Bundling for sales** needs shared identity, billing, a unified API and a common customer experience. It doesn't need one codebase. Customers don't see the language.

The rewrite adds little to either goal. It carries the most risk, and it lands on the people and contracts that are most exposed this year.

**The constraints that should shape the plan**

- **Cloud commit.** You're about $1.2M a year under your committed spend. Moving Lanternway's workloads onto that commitment is worth more than the $900k suggests, because that capacity is already paid for. Ask finance for the real number: the avoided Lanternway cloud bill, minus the shortfall you would otherwise pay, minus one-time migration cost. This could make the case for infra consolidation clear on its own, and it is your strongest point at the offsite.
- **Pellworth (31% of Lanternway revenue).** A new cloud provider is probably a new subprocessor for their data, which triggers the 120-day notice. Send that notice early and treat it as a gating item. Check the contract wording on whether a hosting change counts, and don't assume it doesn't. Don't move Pellworth's workloads until the notice period has run. Move other customers first.
- **Ilse's earnout (through next December).** Her payout depends on revenue in the same window as the migration. A migration or rewrite that causes outages or slows the roadmap directly costs her money, so she has a conflict of interest that no one should ask her to ignore. Either sequence the risky cutovers after the earnout window, or have legal and finance agree in writing that migration-caused revenue disruption is adjusted for. Resolve this before asking for her commitment.
- **Retention vesting next April.** Everyone vests in one tranche. After April, the two engineers who wrote the routing engine are free to leave, and a rewrite plan is exactly the kind of thing that makes them go. You are about to hit a cliff either way. Consider a second, longer retention layer (for example a grant vesting at 12 and 24 months, tied to the migration milestones) offered before April, not after.
- **Rewrite risk.** The routing engine is the product's core, and two people know it best. A Go rewrite means a long period with two engines and a risk of regressions in route quality, which customers notice quickly. The platform team is right that long-term maintainability matters. They just don't have to answer that question now.

**Proposed plan**

1. **Phase 1 (now to about mid next year).** Common tooling, CI, observability and identity. Containerize the Lanternway services onto Kubernetes on your cloud. Ship a unified API and billing layer so sales can bundle. Send the subprocessor notice.
2. **Phase 2 (through the end of next year).** Complete the cutover, with Pellworth last, after the notice period and after agreeing the plan with their security team. Decommission the old cloud and tooling.
3. **Rewrite gate (revisit in about 9 to 12 months).** Decide on evidence: how hard is the Elixir service to operate and hire for on your platform, what do the routing engineers want, and has the engine become a bottleneck? A partial path is also an option, such as new components in Go behind the existing interfaces, with no big-bang rewrite.

Be upfront with Odalys about what this gives up: one codebase is not delivered, and the rewrite becomes an option rather than a commitment. If she needs a single codebase for a reason beyond bundling, such as hiring or security posture, that reason should be stated and tested at the offsite.

**How to get real commitment**

- **Talk to Ilse and the two routing engineers before the offsite**, separately and in private. Ask what would make this plan safe for them and what they'd change. Offer concrete things: the earnout protection, the retention layer, and a say in the rewrite gate criteria. Commitment comes from changing the plan and the incentives so it is actually safe for them. Persuasion alone won't do it.
- **Bring your platform team along with a real role.** They get ownership of the platform migration, the unified API and the rewrite-gate evaluation, which is more interesting work than a rewrite nobody trusts. Ask them to help define the gate criteria so they own the outcome.
- **Pre-wire Odalys.** Show her the finance number and the dependency map (Pellworth notice, earnout, April vest) at least a week before the offsite, so she isn't surprised in the room. Frame the plan as delivering her two goals sooner and more safely, with the rewrite deferred rather than rejected.
- **At the offsite**, present the decision with named owners for each phase, the milestones, the kill or continue criteria for the rewrite gate, and what each group has agreed to. Ask each person for a clear yes or a specific concern, not silence. A concern raised in the room is cheaper than one raised in month six.
- **Write down the decisions and reopen conditions**, for example "if routing latency or hiring becomes a problem, we revisit the rewrite at the gate." That makes it easier for the skeptics to commit, since they know when the question gets reopened.

**Things to check before you finalize**
- The exact Pellworth contract language on subprocessors and hosting changes.
- Legal's reading of the earnout terms on integration-caused disruption.
- Finance's real savings figure given the committed-spend shortfall.
- Whether any other Lanternway customers have similar data-handling clauses.

If you tell me which of these you can confirm, I can tighten the plan and draft the offsite one-pager.
