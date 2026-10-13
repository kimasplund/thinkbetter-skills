**Recommendation: consolidate the infrastructure now, keep Elixir for now, and make the rewrite a gated decision rather than a starting assumption.**

## What I'd propose to Odalys

**1. Move Lanternway onto your cloud and Kubernetes, with the Elixir services unchanged.**
- Most of the $900k is probably duplicated hosting, tooling and licences, not language. A runtime move captures that without touching routing logic.
- The $1.2M you're under-running on your committed spend changes the math. Lanternway's workloads would use spend you're already paying for, so the real saving is larger than the line-item comparison suggests. Ask finance for the figure: Lanternway's current cloud bill against your shortfall.
- Elixir containerizes and runs on Kubernetes without trouble, so "different language" doesn't block this.

**2. Start the Pellworth process in the first week, not the last.**
- Moving Lanternway's data to your provider almost certainly adds a subprocessor, which triggers the 120-day notice. Have legal confirm that.
- Pellworth is 31% of Lanternway's revenue, a three-year renewal, and it feeds Ilse's earnout. A botched notice or an outage for them is the single most expensive failure available.
- Send the notice early, give their security team a clear migration plan, and keep Pellworth's workloads in the last cutover wave. Working back from the 120 days, your end-of-next-year date holds for the infrastructure move, with room for slips.

**3. Get the "one product" benefit through integration, not a shared codebase.**
- Sales needs one contract, one login, one API surface, one invoice and one set of dashboards. Put those on your platform: identity, billing, API gateway and observability.
- That delivers the bundle without a single line of routing code being rewritten.

**4. Decide on the rewrite at a checkpoint, with criteria agreed in advance.**
- Set the review for after the infrastructure move and the April vest, roughly Q2 to Q3 next year.
- Agree the criteria now, and let Lanternway's engineers help write them. Examples are:
  - a measured operating-cost or reliability gap that only a rewrite closes;
  - hiring or on-call pain specific to Elixir;
  - a feature roadmap the current engine can't support.
- If the criteria are met, do it incrementally, one routing component at a time, with the old and new running side by side. Don't do a big-bang replacement. If they aren't met, you've saved a year of risk.

This doesn't say no to your platform team. It says not yet, and it says what evidence would change the answer. It also gives Odalys most of her business case on her timeline. The part it defers is the part that carries the most risk and contributes the least to the $900k.

## Why the rewrite is the wrong first move

- **Key-person risk.** Two engineers wrote most of the routing engine. Their retention grants vest in one tranche next April. After that, nothing holds them, and a rewrite would have them reimplementing their own work for a team that plans to replace it. That is how you lose them.
- **Revenue risk.** Ilse's earnout depends on her product's revenue through next December, and Pellworth is nearly a third of it. A rewrite that causes regressions in routing quality puts the earnout, the renewal and the acquisition's value at risk together.
- **Her incentives.** Asking Ilse to endorse something that could cut her own payout is unrealistic. Ask for her endorsement only of a plan that protects her number.

## Getting real commitment

The offsite is in three weeks. Win the people before the room, and use the offsite to ratify.

**Week 1: private conversations, in this order.**
- **Odalys.** Test the proposal against what she actually needs, which I'd guess is the savings, the bundle and a clean integration story. If those are met, the codebase may matter less to her than it sounds. Ask directly: "If you got the $900k and the bundle by end of next year, would one codebase still be a requirement?" If yes, find out why.
- **Ilse.** Ask what would make her endorse this, and share the Pellworth sequencing plan. Her key worries will be the earnout and her team. Put the earnout on the table yourself: any migration plan should carry explicit protection, such as a metric or schedule adjustment if migration activity depresses revenue. That is a legal and finance question, so involve them now, because the terms are theirs to change, not yours. Don't try to resolve it at the offsite.
- **The two routing engineers, and a few other senior Lanternway engineers.** Listen first. Ask what they'd need to see before a rewrite became a good idea. Then give them a real role in writing the checkpoint criteria and designing the infrastructure move.
- **Your platform team lead.** Be straight with them: the rewrite isn't cancelled but gated. Give them ownership of the infrastructure migration and the shared identity, billing and API layer. That is visible, significant work, and it is the prerequisite for any rewrite. The criteria also give them a legitimate route to the rewrite if the evidence supports it.

**Week 2: one document, co-authored.**
- Write the proposal with one named person from each side contributing, so nobody meets it for the first time at the offsite.
- Include the cost case (with finance), a phased timeline, the Pellworth notice schedule, and the checkpoint criteria.
- State the open risks, including what you don't yet know, such as the exact split of the $900k.

**Week 3: the offsite.**
- Present it as one plan with a clear owner for each piece, not as a compromise between two camps. Odalys opens with the business goals, Ilse speaks on the customer and earnout protections, the platform lead on the migration, and a Lanternway engineer on the checkpoint criteria.
- End with explicit commitments, not nods. Ask each person: "What do you need to be able to champion this, and what are you committing to?" Record the answers.

**Retention.**
- Because everything vests in April, I'd ask Odalys to consider a second, smaller retention grant tied to infrastructure-migration milestones, so the incentive to stay runs through the move rather than ending before it. Your HR and finance partners need to size it.
- Do not pair retention with a rewrite commitment.

## Risks and what I'd watch

- **Odalys insists on the rewrite anyway.** Then propose the incremental version with side-by-side running, Pellworth workloads last, and the engineers' sign-off at each stage. Make sure she hears the specific risk, which is losing the two people who built the engine in the April window.
- **Ilse's earnout gets squeezed.** If the terms can't be adjusted, move the Pellworth cutover until after the measurement period ends in December.
- **Pellworth's security team objects to the new subprocessor.** Early notice lets you find that out in month one, not month four.
- **Savings come in lower than $900k.** Get the actual breakdown before the offsite.

## Assumptions I made

I don't know the earnout mechanics, how much of the $900k is cloud versus tooling, or whether Pellworth's contract treats your cloud provider as a new subprocessor. Check all three with finance and legal in week one. The recommendation holds unless the savings turn out to depend mostly on eliminating the Elixir codebase, which I'd be surprised by but would want confirmed.
