## Recommendation

Propose two decisions instead of one. Odalys's goals are real, but the single "move onto our platform" plan bundles two separable things with very different risk.

1. **Commit to moving the infrastructure by end of next year.** Run Lanternway's Elixir services on your cloud and Kubernetes, behind your shared identity, billing, observability and deployment tooling. Keep the Elixir code.
2. **Make the routing-engine rewrite a gated decision, not a given.** Decide in about 12 months whether to rewrite, on evidence: on-call load, hiring difficulty, cost to integrate, and how the engine behaves on your platform. Until then, the routing engine stays in Elixir behind a stable API.

This delivers most of what Odalys is after. The $900k is mostly duplicated infrastructure and tooling, and the infrastructure move captures that without touching the routing code. The "one codebase" goal exists to let sales bundle, and bundling needs one contract, one login, one invoice, one API surface and one support path. Those don't require a single language. Her goal also changes shape: it becomes "one platform, one product experience" instead of "one codebase".

## Why the facts point this way

- **The cloud commit changes the money.** You are about $1.2M a year under committed spend. Workloads moved onto your provider count toward that commit, so the move may be worth more than the $900k duplication saving. Ask finance for the actual number before the offsite. If the shortfall is penalized, this is probably the strongest argument in the room, and it works for the infrastructure move and says nothing in favor of a rewrite.
- **The rewrite is the part that endangers the money you've already spent.** Ilse's earn-out depends on her product's revenue through next December, so a rewrite in that window attacks her payout directly. The two engineers who wrote the routing engine are the people you would need to do it, and their retention grants vest in one tranche next April. If you ask them to rewrite their own work, you give them reason to cash out and leave in April. A rewrite also risks losing the knowledge in the engine, which is the thing you paid for.
- **Pellworth constrains the cloud move.** Pellworth is 31% of Lanternway's revenue, renewed for three years, and holds a 120-day notice right on new subprocessors. Moving providers almost certainly adds one, unless your provider is already on their list. Check with legal this week. If notice is needed, send it early enough that the cutover date is at least 120 days out, and treat Pellworth's security team as a stakeholder, not a formality. A surprise would put 31% of the revenue, and Ilse's earn-out, at risk. I'm assuming your provider isn't already on their list. If it is, this eases.

## What each party needs, and what they get

**Odalys (CTO)** needs savings, a bundle that sales can sell, and a credible integration story. She gets a dated infrastructure move, a bundle roadmap with milestones (single sign-on, unified billing, one API gateway, a combined SKU), and a rewrite decision with explicit criteria. She gives up the assumption that a rewrite happens by default.

**Your platform team** wants a coherent stack and not to own a foreign runtime forever. They get ownership of the migration, Kubernetes and platform standards, and a real shot at the rewrite case, since the gate is open and the evidence will be collected. They give up an early rewrite. Be honest with them that they might lose the argument later too, and set the gate criteria now so it isn't relitigated every quarter.

**Lanternway engineers** want to avoid a risky rewrite and keep ownership of the engine. They get a commitment not to rewrite this year, a decision-making role in the gate criteria, and ownership of the hardest migration work. They give up the idea that the status quo is permanent: the infrastructure moves, and the rewrite question stays open.

**Ilse** wants her earn-out protected and a say in her product's future. Her interests and the company's are partly in conflict here, because migration risk lands on her revenue while the savings land on yours. She gets a written protection: for example, migration-related downtime or customer disruption is excluded from the earn-out calculation, or the earn-out measurement is adjusted if you cause a slip. She gives up control over the infrastructure choice. This needs legal and finance, and I'd raise it with her before the offsite, not at it. Anything touching deal terms should go through counsel.

## Retention is the biggest hidden risk

A single tranche vesting next April, with the infrastructure move running through the following year, means the people the migration depends on can leave right at the start. Consider a second grant for the routing engine authors and the key migration engineers, vesting at migration milestones across next year (for example, at cutover and six months after). This costs real money, so compare it with the risk: losing the two engine authors would cost far more than the grant. Do it before April, not after.

## How to get genuine commitment, not toleration

1. **Talk to people individually before the offsite.** Start with Ilse, then the two engineering leads, then Odalys. Ask each what success and failure look like for them. The offsite should confirm a plan that people have already shaped, not surprise anyone. In three weeks, there is time for one round of one-on-ones and one revision.
2. **Bring Odalys the finance number first.** She is the sponsor, and you want her seeing the cloud commit math and the earn-out and retention risks before she sees any recommendation. Frame it as a way to reach her goals with less risk and not as pushback on her plan. If she wants a rewrite regardless, you need to know that early.
3. **Put Lanternway's engineers into the design.** Ask a few of them, including a routing engine author, to co-write the migration plan and the rewrite-gate criteria. People back what they helped write. It also tests whether the plan is feasible.
4. **Make the gate concrete.** Write down what evidence would lead to a rewrite, who decides, and when. That keeps the platform team from feeling stonewalled and the Lanternway engineers from feeling ambushed.
5. **Show the commitments in writing.** Customer-facing dates, Pellworth notice, earn-out protection, retention terms, owners and milestones. Verbal agreement from an offsite fades, and people who feel they gave something up check that the other side kept its part.
6. **Set a review point.** Revisit at roughly six months, with an agreed way to handle disagreement: the trio of you, Odalys and Ilse, with Odalys deciding if you can't agree and the reasoning recorded.

## What I would bring to the offsite

- A one-page recommendation: infrastructure moves by end of next year, rewrite decided by gate, bundle delivered through shared services.
- The finance numbers: duplication savings, cloud commit shortfall absorbed, migration cost, retention cost.
- A timeline showing Pellworth notice, the April vest, the earn-out period and the cutover plan on one calendar.
- The rewrite-gate criteria, written with both engineering teams.
- A risk list with owners: Pellworth, key-person loss, earn-out disruption, bundle slippage.

## Things I couldn't verify

I don't know the terms of the earn-out, whether your provider is already on Pellworth's subprocessor list, whether the commit shortfall carries a penalty, or whether Odalys would accept a deferred rewrite. The first three can be answered in a week. The last decides how you run the conversation, so test it with her privately before the room.

I'm fairly confident the split recommendation is right. I'm less sure about the details of the earn-out and retention terms, which depend on contracts I haven't seen.
