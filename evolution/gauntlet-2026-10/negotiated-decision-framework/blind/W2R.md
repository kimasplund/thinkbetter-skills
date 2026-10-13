**Recommendation: split the decision in two.** Move Lanternway's infrastructure onto your platform, and keep the Elixir routing engine. Don't commit to a Go rewrite now. Decide on the rewrite later, using evidence from the migration.

**Why this split works**

Odalys's case has three parts: $900k of duplicated cost, one codebase for bundling, and a unified platform. Most of the money and the bundling comes from consolidating infrastructure, not from the language.
- **Cost:** Moving to your cloud provider, one tooling stack and shared CI, observability and on-call removes most of the duplication. You are also about $1.2M a year under your committed spend. Workloads moved onto that commitment use money you have already promised to pay, so the net saving may be bigger than $900k. Ask finance to model this, because it could be your strongest number.
- **Bundling:** Sales needs shared identity, billing, APIs and a single contract. It doesn't need one language. Elixir services behind a clean API can be bundled fine.
- **Rewrite risk:** The routing engine is the product, and Ilse's earnout depends on its revenue through next December. A rewrite puts correctness and performance at risk in the same window. The people who understand the engine are the two engineers whose retention grants vest in April, and a rewrite plan gives them a reason to leave on that date.

**Constraints to put in the proposal**
1. **Pellworth (31% of Lanternway revenue).** Check this first. If a cloud move adds a subprocessor for their data, you owe 120 days' notice before cutover. Work backward from that date. Confirm with legal whether your provider is already an approved subprocessor for Pellworth data. Plan Pellworth's workloads as the last to move, and consider telling their security team early.
2. **Earnout.** Any migration that causes outages or slows product work hits Ilse's payout directly, and she will see that. Offer to protect it, for example by excluding migration-caused disruption from the revenue calculation or adjusting the measurement. Get legal and finance to confirm what is possible. Without this, you can't honestly ask her to back the plan.
3. **April vest.** Plan the retention conversation now. Consider a second retention layer, such as a grant that vests after migration milestones, for the two engine authors and other key engineers. Make them owners of the migration design.
4. **Timeline.** "End of next year" is workable for infrastructure. Put the Pellworth notice period, the April vest and the December earnout date on one timeline, and keep the riskiest cutovers away from the earnout's final quarter where you can.

**Proposed shape (three phases)**
- **Phase 1, now to about Q2:** Shared tooling, CI/CD, observability, security baseline and identity. Lanternway stays on its own cloud. Plan the migration in detail, with Lanternway's engineers co-authoring it.
- **Phase 2, mid-year to the fourth quarter:** Move workloads to your cloud in stages, starting with non-critical ones. Run in parallel with rollback options. Pellworth moves last, after notice.
- **Phase 3, a decision gate after migration:** Decide per component whether to rewrite, keep or wrap. The decision uses real data: operating cost, incident rates, hiring difficulty and how hard integration proved. If Go is still warranted for some services, do it incrementally, with the new service running next to the old one and compared against it. Don't do a big-bang rewrite.

**Getting real commitment**

You said you want people genuinely behind the plan, so how you bring them in matters as much as the content.
- **Before the offsite:** Meet Odalys first. Tell her you support her goal, show how the split delivers it, and ask which of her goals a rewrite specifically serves. Then talk to Ilse and the Lanternway tech leads one on one, before any group session. Ask what would make them confident, what they fear, and what they'd need on earnout protection. Meet your platform team's lead too. Their appetite for a rewrite is a legitimate engineering preference, and the phase 3 gate gives it a fair route.
- **Co-design:** Ask Lanternway's leads and the platform team to jointly define the phase 3 gate criteria and the migration plan. People commit to what they helped build.
- **Make the trade explicit.** Each side gives something. Odalys gets a dated consolidation and a savings number. Ilse gets earnout protection and decision rights over her product's architecture. The platform team gets a defined path to a rewrite if the data supports it. Lanternway's engineers get no forced rewrite and a retention bridge.
- **At the offsite:** Present options, not a verdict. Show the full rewrite, the migrate-first option and the do-nothing option against cost, risk, earnout exposure, attrition and timeline. Recommend migrate-first, and invite Ilse and the tech leads to present their part.
- **Test commitment, not just agreement.** Ask each party to state what they will do in the next 30 days. Write down the decision rights, the gate criteria and what would change the plan.

**Assumptions and open items**
- I'm assuming the earnout and Pellworth contract terms are as you described. Legal needs to confirm the subprocessor wording and whether your provider already counts as one.
- Your $900k figure needs a breakdown into cloud, tooling and licences, so you can say which parts a migration actually removes.
- If the platform team's rewrite case rests on hiring Go engineers or on performance, put those arguments to the phase 3 gate with numbers rather than dismissing them.

The one-line pitch for the offsite: "We capture the savings and the bundle on Odalys's timeline, protect Ilse's earnout and the people who built the engine, and let evidence decide the rewrite."
