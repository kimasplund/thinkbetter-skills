**Short version:** don't take a "rewrite or no rewrite" proposal to the offsite. Odalys's two goals are $900k of duplicated cost and a bundleable product. Neither needs the routing engine rewritten in Go. Propose three separate decisions: move the infrastructure now, integrate the product surface now, and make the rewrite a later decision with a defined test. Each of the three groups gets most of what it actually needs that way.

(I'm assuming "next April" and "next December" are both inside the same calendar year that Odalys's end-of-year deadline refers to. If the dates are different, the sequencing below shifts but the logic holds.)

## What each party needs

- **Odalys** needs a credible path to the cost savings and to a bundle sales can sell. "One codebase" is her means. She will probably give it up if the two real goals are met on a believable date.
- **Your platform team** wants a simpler estate and the chance to own the routing services. That is a legitimate wish, but it is a preference about how, not a business requirement.
- **Lanternway's engineers** are worried about breaking the thing that makes the company's money. Two of them hold the knowledge that matters most, and their grants vest in a single tranche in April. After that date they can leave at no cost to themselves.
- **Ilse** is the person to protect carefully. Part of her purchase price depends on her product's revenue through next December. A forced rewrite and migration landing in the same window puts her payout at risk from decisions she doesn't control. If she senses that, she'll resist whatever you propose, however politely. Her engineers will follow her lead.

## Three facts in your message that change the plan

1. **Pellworth.** They are 31% of Lanternway's revenue, signed for three years in May, and negotiated a 120-day notice requirement before you add a subprocessor. Moving Lanternway's workloads to your cloud almost certainly counts, or at least Pellworth's security team may say it does. Even if the two clouds are equally acceptable to them, notice has to go out four months before cutover for their data. Treat this as the critical path for the whole infrastructure move, and send the notice early, ideally well before the deadline pressure builds. Move Pellworth's workloads last. Have legal read the contract language now so you know whether this is a notice or a consent.
2. **The $1.2M of unused committed spend.** This is the strongest argument you have, and it supports moving infrastructure, not rewriting code. Workloads moved onto your cloud draw down a commitment you are already paying for. So the cash saving from retiring Lanternway's separate cloud bill is real, and the incremental cost on your side is close to zero. Ask finance to split the $900k into cloud, tooling and licences, and people/process overhead. I'd expect most of what is recoverable to sit in the first two, and neither depends on the language. This also gives you a reason to put the infrastructure move first.
3. **The April cliff.** A rewrite of the routing engine takes longer than six months, so the two people who wrote it would be gone before it ships. Lanternway's engineers are right that it is risky, and the risk is specific: the rewrite needs exactly the people the retention structure stops holding in April. Ask HR what comes after April for those two people and for the rest of the team. If the answer is nothing, fix that before you propose anything.

## What I'd propose

**1. Move the infrastructure, keep the Elixir code (start now, finish by the end of next year).**
Elixir runs fine on Kubernetes on your cloud. Lift the services onto your clusters, your CI, your observability and your secrets management, and retire the second cloud account and the duplicate tooling. This captures most of the savings, uses the committed spend, and leaves the routing engine untouched while the earnout runs. Sequence it so the lowest-risk services go first and Pellworth's workloads go last, after the notice period has run.

**2. Integrate the product surface (start now).**
Bundling needs one login, one billing and contract relationship, one customer-facing API gateway, a consistent UI shell, and shared data where the products overlap. It does not need one runtime. Give sales a concrete bundle date for this layer. Your platform team does the work, working with Lanternway's engineers, so their time goes into something with visible commercial value.

**3. Make the rewrite a decision with a test, not a commitment.**
Put the question of rewriting routing in Go on the calendar for a fixed review, say 6 to 9 months after the infrastructure move, and write down in advance what would justify it. Examples: hiring and on-call cost for Elixir that is materially higher than you can bear, a performance or scaling limit you can show, or integration work that keeps getting blocked by the language boundary. If the test is met, do it incrementally, one service at a time behind stable interfaces, led by the people who know the engine. If it isn't met, you've avoided the riskiest project of the year. Your platform team gets a real path to the work and a fair test, and Lanternway's engineers get a promise that evidence decides it, not seniority.

Be honest in the pitch about what this gives up. Two stacks will exist for longer than Odalys wanted, and there is a real cost to hiring and supporting both. State that cost as a number so she can weigh it against the rewrite's risk to a $900k-a-year decision and to 31% of Lanternway's revenue.

## Protecting the earnout and the people

- **Earnout:** ask legal and Ilse whether the purchase agreement already protects her revenue if integration work disrupts the product. If it doesn't, offer an adjustment that neutralises any revenue loss caused by your migration decisions, such as an agreed adjustment for downtime or customer losses attributable to the move. That is a cheap price for her real support, and it removes the conflict of interest in her having to defend a plan that could cost her money. This needs sign-off from Odalys and finance, so raise it in advance, not at the offsite.
- **Retention:** propose a second retention layer that pays out after the infrastructure move completes and after the next vesting milestone, not just in April. For the two routing authors, make it meaningful and tie it to knowledge transfer: documentation, pairing with your platform engineers, and runbooks. This turns a cliff into a reason to stay and teach.
- **Pellworth:** one named owner, a short written plan for the subprocessor notice, and an early heads-up to their security contact. Surprising a customer that did this much diligence would cost more than the whole migration saves.

## How to get real commitment, not tolerance

You have three weeks. Use them like this.

- **Week 1: talk to people one at a time before any meeting.** Start with Ilse, then her two routing engineers, then your platform lead, then Odalys. Don't present the proposal. Ask each what they would have to see for it to feel safe or worthwhile. Ilse and the engineers need to hear that the rewrite is not a precondition. Your platform lead needs to hear that the review has a real path to yes. Odalys needs to hear that the savings and the bundle are on the table with dates, and that you aren't dropping her goal.
- **Week 2: have a small group build the plan together.** Ilse, one Lanternway engineer, one platform engineer, and finance. Let them set the sequence, the milestones and the criteria for the rewrite review. People commit to what they helped design. Ask Lanternway's engineers to name the three things most likely to go wrong in the migration. Putting their risks into the plan is the clearest proof that you listened.
- **Week 3: pre-wire Odalys, then go to the offsite.** Before the room, make sure she has seen the numbers and the Pellworth constraint and has no surprises. At the offsite, present it as the plan the two teams built together, with Ilse and the engineering leads presenting their own parts, not you presenting for them.

To tell whether you have commitment or only compliance, watch for a few signs. Do Ilse and the Lanternway engineers volunteer risks, or only nod? Do they take owner roles in the plan? Does anyone keep reopening the rewrite after the decision? Write the decision and its review criteria down and circulate them the same day, so there is one reference point if it comes back up. If the platform team accepts the sequence but quietly stops doing the integration work, that is a sign they're waiting for the rewrite, and you should deal with it directly.

## What would change my recommendation

- Finance shows that most of the $900k is people and process overhead, not infrastructure. Then the case for a faster full integration gets stronger, and the retention and earnout terms matter even more.
- Pellworth's contract treats the cloud move as needing their consent, not just notice. Then the Pellworth workloads may stay where they are longer, and you'd want to talk to them early.
- Elixir hiring or on-call data is bad enough to justify the rewrite review earlier.
- Odalys will not move off "one codebase" under any conditions. Then the question for the offsite is no longer which plan but whether to accept the risk, and you should put the retention and earnout costs of that choice in front of her in plain numbers.

I'm moderately confident in the structure. Pellworth's timing, the earnout wording and the shape of the $900k are the three things I'd check first, because any of them could move the sequence.
