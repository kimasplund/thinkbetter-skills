## Short answer

Propose a two-stage plan. Stage one moves Lanternway onto your cloud, tooling and customer-facing surface by the end of next year, and leaves the Elixir routing engine alone. Stage two is a rewrite decision, made later, with a defined test and with Lanternway's engineers co-owning it. This gets Odalys most of her business case, keeps Ilse's earnout and the retention grants from fighting your plan, and gives the platform team real work now instead of a promise.

The reason it works is that Odalys's two goals, cost and bundling, are separate from the means she has picked, which is a rewrite in Go. Neither goal needs one language.

## What each person needs

- **Odalys** needs the duplicated spend gone and a bundle sales can sell, both by the end of next year. She does not need Go as such. A recommendation that delivers both with less risk is easier for her to accept than one that waters down her ask.
- **Your platform team** wants one coherent platform and, probably, a say in how it is built. The rewrite is how they see getting that. They also fear running two stacks indefinitely, and that is a fair fear.
- **Lanternway's engineers** are protecting a working product, and the two who wrote the routing engine are protecting their own work. They are probably also asking whether there is a place for them here. Their "riskiest thing we could do" claim is a risk argument, not a refusal. Treat it that way and ask them to name the specific risks.
- **Ilse** is paid through next December on her product's revenue. Anything that disrupts routing in 2027 costs her money directly, and she will not say so unless asked. She also needs to know she still has real authority over her product and not just a title.

## Facts that decide the plan

1. **The $1.2M under-commit changes the cost math.** You are already paying for cloud capacity you are not using. Running Lanternway's workloads on your provider uses up that commitment, so part of the $900k becomes a real saving, or at least stops being a double payment. The Elixir services can run on Kubernetes as they are. Ask finance for two numbers: how much of the $900k is hosting, how much is tooling and licences, and how much is people. The rewrite only helps with the last category, and only slowly. If the hosting and tooling share is large, stage one captures most of the saving.
2. **Pellworth is 31% of Lanternway's revenue and holds a 120-day subprocessor notice right.** Moving Lanternway's data to your cloud provider may add that provider as a subprocessor, depending on what is already listed and what Pellworth's contract treats as a subprocessor. Have legal read the contract this week. If notice is required, put the notice date on the critical path and send it early. A late notice could stall the migration or sour a three-year renewal that was only signed in May. Replacing the routing services with new Go code could also raise questions with their security team, and that is another reason to move infrastructure first.
3. **The earnout and the retention vest end around the same time as your deadline.** Earnout runs to December. Retention vests once, in April. A rewrite would take the routing engineers' time through the period when they are free to leave and Ilse's revenue is being measured. A single April cliff also means that after April you have little hold on the people you can least afford to lose. That makes retention an urgent subject whatever you decide.
4. **A change to how Ilse's product is run may affect the purchase agreement.** Check the earnout terms before the offsite. Some deals oblige the buyer to operate the business in good faith or not to take actions meant to reduce the earnout. If your plan could reduce her revenue, expect her lawyer to raise it. It is better to deal with this before she asks.

## What to propose

**Stage one, through the end of next year: one platform, one front door, no rewrite of the routing engine.**
- Move Lanternway's hosting, CI/CD, observability, identity, and security tooling onto your platform. Run the Elixir services on your Kubernetes setup. Retire the second cloud account and the duplicate tools.
- Build one customer-facing layer: shared login, a single API gateway, joint billing and a single bundled product listing. This delivers "sales can bundle the two products" without the engine moving.
- Staff the migration with platform engineers working alongside Lanternway engineers, and give the platform team the lead on the shared infrastructure. They get a large, visible job.
- Sequence the work so the services that touch Pellworth move last, and only after notice has been given and the 120 days have passed, if notice is required.

**Stage two, decided at a fixed review in the second half of next year: whether and how to bring routing into Go.**
- Write down the test now, with Lanternway's engineers in the room. For example: hiring and on-call burden of maintaining Elixir, performance and cost per route, and defect rates. If the test shows a rewrite pays for itself, do it gradually, one service at a time, with the old and new versions running together and results compared, starting with the least critical component.
- If the test does not support a rewrite, you have an answer that the platform team helped write, and not a veto.
- Do not start any routing rewrite before Ilse's earnout period ends unless she agrees.

State openly what this costs. You keep two languages for longer. The cost of Elixir hiring and support stays. The platform team does not get its rewrite on its timeline. The saving is likely less than the full $900k in the first year. Odalys should see those numbers rather than discover them later.

## How to get real commitment

**Before the offsite (you have three weeks):**
- **Week 1.** Meet each person alone, not in a group: Odalys, Ilse, the head of your platform team, and the two routing engineers. Ask each of them what success looks like in 12 months and what would make them quietly resist. Ask Odalys whether the savings number or the single codebase matters more to her, because the answer decides which concessions are cheap. Take the finance breakdown and the legal read of the Pellworth contract and the earnout in the same week.
- **Week 2.** Hold a joint working session with Ilse, the routing engineers and the platform lead. Give them the problem, which is cost, bundling and risk, and ask them to improve your draft, not approve it. People support what they have changed. A small design spike on moving one non-critical Elixir service onto your Kubernetes setup would give you evidence in place of opinion.
- **Week 3.** Pre-wire Odalys. She should not meet the compromise for the first time at the offsite. Walk her through the cost, date and risk trade-offs, and confirm she can accept stage two as a gated decision.

**What to offer, and to whom:**
- **Ilse.** A written commitment, reviewed by legal, that migration work will not be scheduled in ways that put her revenue at risk without her consent, and an agreed way to adjust earnout measurement if a company-driven change does hurt revenue. She also gets a real decision right on the order of work for her product, and a seat in leadership planning. Do not promise terms you do not control: the earnout and retention terms are for the CEO, CFO and counsel, so bring them in early.
- **The routing engineers.** Handle retention before April, not after. Options to put to HR and finance include a second grant that vests over the migration period or on milestones, and a defined technical role in the stage-two decision. Offer these because their knowledge matters and not as a trap. If it looks like a way to keep them from leaving, they will notice.
- **The platform team.** Ownership of the shared platform and the migration plan, a clear route to Go for new services and for any routing components that pass the stage-two test, and an agreement that Lanternway engineers are peers on the platform, not guests.
- **Odalys.** A dated plan, a savings figure from finance with its assumptions, a bundle that sales can sell, and a decision point so the rewrite question is answered by evidence on a known date.

**At the offsite:**
- Present it as one decision with named owners and dates, not a menu. Have Ilse and the lead routing engineer present part of it themselves.
- Ask for each person's level of support out loud. "Can you live with this" and "will you argue for this" are different questions. For Ilse and the platform lead you want the second answer. If someone says they can only accept it, ask what would move them, and note it.
- Write down what was decided, who owns each piece, and what would cause you to reopen it (a missed date, an incident, a revenue dip beyond an agreed threshold). Without that, the rewrite debate will return in every planning cycle.

**After the offsite:**
- Hold a monthly review of three numbers: dollars of duplicated spend retired, Ilse's product revenue and incident rate, and attrition among Lanternway engineers. If one of them turns bad, the group has already agreed what happens next.
- Agree who decides when you and Ilse disagree. Name a person, probably Odalys, and a time limit, so the argument does not drag on.

## Risks to watch

- Odalys may read the staged plan as a retreat. Counter it by showing her the savings captured by the end of next year and the dated decision on the rewrite.
- The platform team may treat stage two as a delay on the rewrite. A test written jointly, with an actual date, is the best answer.
- The routing engineers may leave in April whatever you do. Reduce the damage by getting their knowledge into documentation and pairing with platform engineers during the migration, and decide on retention in the next few weeks.
- Pellworth could object to the cloud move. Learn what their contract says before you tell them anything, then go to them early with a plain account of what is changing and what is not.

## Assumptions I made

I assumed that your provider is not yet a subprocessor for Lanternway's customers, that Elixir services can run on your Kubernetes platform without major changes, and that most of the $900k is hosting and tooling. If the last is wrong, and most of the cost is people, the case for the rewrite becomes stronger and stage two should be given more weight. I also assumed the earnout and retention terms can be amended with the CEO and CFO. Check each of these before the offsite, because each changes the recommendation if it turns out false.
