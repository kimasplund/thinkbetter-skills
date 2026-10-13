# Premortem: DeployBoard — Product Hunt launch and the 100-team quit gate

**Horizon:** April 1, 2027 (your decision date, ~7 months out from a late-August 2026 present) · **Success was defined as:** "100 paying teams — $4,900 MRR — by April 1, 2027. That's the number I've set for deciding whether to quit my job."

**Note on the percentages:** shares of failure — "if this dies, this is what killed it" — not the probability the plan fails overall. They sum to ~100. **Overall chance this misses its success definition by the horizon:** ~85%.

**Assumptions I'm working from:**
- "Now" is late August 2026 (competitor shipped "last month," Stripe is "my September project").
- Nights-and-weekends = ~10–12 usable hours/week, of which support, marketing, and admin currently consume none — that changes at launch.
- US-based, at-will fintech employment; a standard broad IP-assignment clause is in force until proven otherwise.
- The $5,500/mo burn is personal only; the $25k cushion excludes business costs, health insurance premiums post-quit, and taxes.
- The 340 waitlist emails came from ~17,000 landing-page visitors over 5 months (340 ÷ 2%), source unstated — I treat the source as unknown and unpriced in the plan.
- The competitor is unnamed; I assume venture-typical behavior for a $2M-seeded dev-tool startup.

## 1. The Autopsy

**The strongest case for this plan:** Deployment status is genuinely fragmented across CI tools, and small teams are structurally underserved — the seeded competitor's $299/mo entry point abandons them, and a $49 flat team price is a 6x undercut with healthy gross margin. You have proof of execution stamina (8 months of nights and weekends, a working product you use yourself), a 340-person waitlist built with zero spend, and — rarest of all — a salaried validation period: you can test demand without betting a dollar of the $25k cushion, because the quit gate means the job funds the experiment. A Tuesday PH launch into a dev-tools-friendly community, a weekly blog, and active r/devops presence is a coherent, if modest, distribution plan. A smart person looks at this and sees a disciplined bootstrapper with a wedge price and a real product.

Six ways this died, ranked by probability. (Six, not seven: the champions mode was below Endorse-grade, so it was converted to a pre-launch checklist item and folded into #1's mechanism rather than padded into its own slot.)

### 1. The plan's own funnel arithmetic never reached 100 teams
**Probability:** ~40% — the top of the ladder, because the failure is visible in the plan's own numbers before anything external goes wrong: at the benchmark waitlist-to-paid rate of 2–5% (excellent, deposit-based waitlists reach 10–15%), 340 stale emails yield ~7–17 paying teams; a *featured* PH launch yields 1,000–5,000 visitors converting at 1–3% to leads and ~0.5–2% for B2B paid — call it 10–30 more; the blog and r/devops added single digits per month. The plan needed ~100 net adds in 5.5 months against 5–8%/mo small-team churn, i.e. ~130+ gross adds. Its channels plausibly produced 30–60. Reference class: bootstrapped B2B SaaS reaching its first ~$5k MRR typically takes 12–24 months *with* a working channel. Disanalogy: your ~3,400 visitors/month of organic landing traffic is better than the class median (pushes the number down); your stated channels — a from-zero blog and a subreddit whose self-promotion rules forbid link-dropping — are weaker than the class's successful cases (pushes it back up).
**Cause of death:** Demand existed, but the plan's three channels could not physically deliver 100 paying teams by April 1 — and nobody recomputed the funnel before committing to the date.
**How it unfolded:**
- September: Stripe consumed the month's weekends; no selling happened. The waitlist sat untouched for a sixth month, cooling.
- October 13: the PH launch went fine — 2,800 visitors, 61 trials, 14 paying teams by week's end, plus 9 from the waitlist blast. MRR: ~$1,130. It felt like traction.
- November: PH traffic decayed to <10% of launch day within the week, as it does. Blog posts 1–4 averaged tens of views — a new domain has no SEO. r/devops answers built karma but couldn't carry links. +8 teams.
- December: B2B froze for the holidays; the first churn cohort (teams that signed on launch-day curiosity) left. Net +2.
- January–February: a modest new-year bump, +10, then the channels plateaued at what they were: +6–8 gross/month against a growing churn base.
- April 1: 54 paying teams, $2,650 MRR. The number was missed; the quit decision deferred; the plan, as stated, failed.
**The assumption that allowed it:** That a launch event plus two unbuilt audiences is a distribution strategy — that "340 people on a waitlist" is 340 future customers rather than 340 emails whose conversion rate had never been measured against money.
**First warning sign:** Launch week itself — waitlist blast converting under 5% to paid, visible by October 20. There was no earlier instrument in the plan to detect it.

### 2. September slipped, and the launch shipped without activation
**Probability:** ~20% — reference class: solo side-project SaaS in its final pre-launch month, where billing, onboarding, and launch assets all compete for the same 40 hours and the last 10% of billing work (webhooks, proration, seat management, dunning) reliably takes half the time. Disanalogy: Stripe is the best-documented integration in the industry (pushes down); the plan schedules zero slack between "Stripe done" and "PH live" and never schedules onboarding at all (pushes hard up).
**Cause of death:** One person's nights and weekends were the entire budget, and the plan allocated September to billing as if October 13 couldn't move — so when billing ate the slack, onboarding and launch prep were what got cut.
**How it unfolded:**
- September: trial logic, seat counting, and webhook edge cases consumed three of four weekends. Onboarding — never scheduled — stayed unbuilt. The weekly blog cadence, the plan's only durable channel, paused in exactly the month it needed to ramp.
- Early October: faced with moving the PH date or launching half-plumbed, he kept the date. Billing worked for the happy path and broke on team invites and card failures.
- Launch week: signups arrived into an empty-state product with a README for onboarding. He spent launch week — the one week of maximum attention — fixing billing bugs instead of answering PH comments and converting trials.
- November: the support backlog and bug debt ate the build hours; blog cadence never restarted; the acquisition stall of mode #1 locked in two months earlier than it otherwise would have.
**The assumption that allowed it:** That the October 13 date was fixed and everything else was flexible — when in fact the date was the only cheap thing to move, and the unshipped billing was the expensive thing to fake.
**First warning sign:** Stripe not live in staging by September 20 — three weeks before the launch it gated.

### 3. The unread IP assignment agreement covered the side project
**Probability:** ~15% — the clause already exists, unread; fintech IP assignments are drafted maximally ("inventions relating to the employer's business or demonstrably anticipated R&D"), and a fintech large enough to have an internal platform/infra org has a colorable claim over a deployment-tracking tool. A judgment call — the reference class (IP disputes over employee side projects) is real but sparsely reported, because most settle quietly.
**Cause of death:** The plan's single legal dependency — the one document that determines who owns DeployBoard — was never read, and the product was launched publicly, under the founder's real name, while employed.
**How it unfolded:**
- August–October: the agreement sat in a drawer. The PH launch, the bylined blog, and the public r/devops answers created a dated, public record of who built DeployBoard and when.
- November–January: nothing happened — the silent phase. Revenue grew toward $2–3k MRR, which made DeployBoard worth claiming.
- February 2027: a former colleague at the employer mentioned the launch internally; or a routine conflict-of-interest disclosure surfaced it. HR and counsel reviewed the agreement and found the assignment clause covered "software relating to the Company's business" — and a fintech with a platform org plausibly builds internal deployment tooling (assumption, but the clause's breadth doesn't depend on it).
- March: the choice arrived fully formed: sign an acknowledgment assigning DeployBoard, resign and fund a dispute on a $25k cushion (a side-project IP fight runs $30–80k before it gets serious), or shut it down. He shut it down — or signed it away. Fifteen months of work ended as a line item in someone else's IP inventory.
**The assumption that allowed it:** That because he built it on his own time and his own laptop, it was his — the agreement's actual text was never consulted.
**First warning sign:** None exists inside the causal chain — that is what makes this mode the most dangerous. The only detection point is before launch: reading the document.

### 4. The launch worked, and success was the kill mechanism
**Probability:** ~10% — requires the launch to succeed first (conditional), but the plan ships with no onboarding flow and one support agent who has a day job, so the success-to-failure conversion is high.
**Cause of death:** Demand arrived faster than one employed person could serve it; the unbuilt onboarding flow — the plan's most glaring omission, never scheduled, never staffed — converted a successful launch into a churn cohort and a public reputation for unresponsiveness.
**How it unfolded:**
- October 13: the launch outperformed — #2 Product of the Day, 1,400 signups in 72 hours.
- October 14–25: teams invited their 10 seats into empty states; activation (first tracked deploy within 48h) ran at ~20%. Sixty support threads piled up against evenings only. First-response time stretched past 48 hours.
- November: the launch cohort churned at 12%/mo; the feature set, built around two specific managers' feedback, fit those two teams and missed the median user. Two public reviews mentioned "solo dev, abandonware risk."
- December–February: MRR peaked at $2,400 and declined. The r/devops goodwill inverted — the same community that watched him launch watched him not answer. The cohort that should have become case studies and referrals was gone, and rebuilding trust cost more than the launch bought.
**The assumption that allowed it:** That the risk was *not getting* users — so nothing in the plan (no onboarding, no support hours, no activation metric) was built for getting them.
**First warning sign:** Activation under 50% during launch week, visible by October 20 — but undetectable in practice, because no activation metric existed.

### 5. The compound scenario: the stall met the missing ELSE clause, and the plan became a zombie
**Probability:** ~10% — this is mode #1 and mode #2 co-occurring, which is their natural state: the capacity slip starves the channels, and the empty funnel hides the slip. Tied with #4 on the ladder; ranked below it because #4 is loud and recoverable in weeks, while this one is silent and consumes a year. (Tie-break: equal shares, ranked by detectability × reversibility.)
**Cause of death:** The two most likely modes interacted with a decision rule that defined success and silence but never defined failure — so April 1 produced not a decision but an extension, and the extension was where the plan actually died.
**How it unfolded:**
- September–October: the Stripe slip (mode #2) meant the PH launch went out without a paywall — "launch now, monetize in December." The launch produced 900 free signups, which he read as traction.
- December: the paywall shipped; conversion from the free cohort ran ~3%. The stall (mode #1) was now baked in, but two months of free-tier "growth" had hidden it.
- January–March: blog cadence slipped to biweekly, then monthly; support and bug debt ate the hours that selling needed. Growth: +4 teams/month.
- April 1: 41 paying teams — close enough to feel salvageable, far enough to forbid quitting. The rule had an IF and no ELSE, so he defaulted to "six more months."
- April–September 2027: a second year of nights and weekends began with less belief behind it. The product coasted. The burnout cost landed on the day job — the household's actual income — and surfaced in a mid-2027 performance review. The plan didn't die on April 1; it died by never being allowed to, and it took a piece of the salary with it.
**The assumption that allowed it:** That "the number I've set for deciding whether to quit" was a decision rule. It was half of one — a quit condition with no kill condition, no extend condition, and no date on which the extension itself would be re-decided.
**First warning sign:** The December paywall conversion number (~3%), visible by December 15 — the first moment money, rather than emails, measured demand.

### 6. The frame's blind spot: DeployBoard was a feature, and the category absorbed it
**Probability:** ~5% — kept despite the low share because it is low-probability, high-severity, and not mitigable from inside the plan's frame: the plan assumes "deployment-tracking dashboard" is a product category; if it is a feature of CI/CD platforms, no execution fix survives.
**Cause of death:** Unknown from inside the plan — that is the definition of this slot. The frame ("dashboard for small dev teams at $49") cannot see the question that kills it: *why wouldn't GitHub, GitLab, CircleCI — or the seeded competitor's free tier — just show this natively?* Every CI vendor already has the deployment data; the dashboard is a view over data they own. Stage 4 resolves this slot: the absorption move is the adversary's endgame, and its tripwire is in Stage 5.
**How it unfolded (sketch, resolved in Stage 4):** In Q1 2027, the competitor — or a platform — shipped deployment tracking as a free native view. The waitlist's pain evaporated into tooling the teams already paid for; $49/mo for a checkbox became indefensible; the blog's comparison keywords started ranking against pages that said "this is now built in."
**The assumption that allowed it:** That the competitor's $299/mo price was evidence of a market gap rather than evidence of where the money in this category actually lives — teams large enough to need cross-system deployment visibility, not small teams with one pipeline.
**First warning sign:** A competitor pricing-page change or a CI vendor's changelog entry — both observable quarterly, neither currently watched.

**Considered and cut:** the two "definitely pay" engineering managers (Accept-grade commitments — converted to pre-launch checklist item 2 and folded into #1's demand-evidence mechanism), a direct competitor price war (folded into #6 and Stage 4), a PH algorithm flop on launch day (a subset of #1's arithmetic — even a good launch doesn't make the number), the December B2B freeze (folded into #1's timeline), and moonlighting-policy termination risk (same unread document as #3 — one mode).

## 2. The Verdict

| # | Impact (1-5) | Feasibility (1-5) | I×F |
|---|---|---|---|
| 1. Funnel arithmetic | 5 | 5 | 25 |
| 2. September slip | 4 | 4 | 16 |
| 3. IP assignment | 5 | 3 | 15 |
| 4. Success kills | 4 | 2 | 8 |
| 5. Compound zombie | 4 | 3 | 12 |
| 6. Frame blind spot | 4 | 2 | 8 |

**Most likely:** #1 — highest feasibility among the high scorers, because it requires nothing to go wrong: it is the plan's own arithmetic on benchmark conversion rates. Every other mode is an event; this one is a computation.

**Most dangerous:** #3 — not #2, despite #2's higher I×F, because danger is weighted by silence × irreversibility. Mode #2 announces itself on September 20 and is recoverable by moving a date. Mode #3 has *no* first warning sign inside its causal chain: it is silent from August to February, and past the point of no return — a public launch under your name, revenue worth claiming, a paper trail of invention dates — it is not recoverable on a $25k cushion. It is also the only mode that can take the product away rather than merely kill it. The divergence between the table (I×F 15, third) and this pick is the silence term: feasibility is suppressed only because the clause might be benign, which a one-hour read would resolve.

**The hidden assumption:** found by convergence — modes #1, #4, and #5, three of the six, die unless the same belief holds: **that expressed interest is demand.** The waitlist emails are treated as future revenue (#1), the launch signups as future customers (#4), the free cohort as traction (#5), and the two verbal "definitely pay"s as validation (the cut champions mode feeding #1). Nothing in the plan has ever tested the belief against money — no pre-sale, no deposit, no paid pilot, no credit card on file. Three modes sharing one root belief is stronger evidence than any of their probabilities alone: the plan's load-bearing wall is an unpriced conversion rate.

**Fatal flaw:** the quit gate is below breakeven. $4,900 MRR gross is ~$4,550 net of Stripe fees and infra, before self-employment tax (~15% on the remainder), and before replacing employer health insurance ($600–900/mo for a individual plan). Quitting at the plan's own success number starts a bleed of roughly $2,200–2,500/month against the $25k cushion — about 10–11 months of runway at the moment of "success," before income tax widens it, with churn working against the MRR the whole way. The number that was supposed to make the quit decision safe doesn't fund the quit. Beneath it, the binding constraint the plan never addresses: distribution — one launch event and two unbuilt audiences cannot produce 100 teams by April 1 on any benchmark.

## 3. The Rebuild

**The revised plan:**

Phase 0 — Paper (now through September 15, before any more code): Read the IP assignment agreement and moonlighting policy this week; if ambiguous, pay for a one-hour employment-law consult and get a written carve-out before launching publicly under your name. Convert the two engineering managers to paper: ask each to sign a paid pilot — $29/mo founding rate, cancel anytime — by September 15. Run the waitlist pre-sale on September 1: a founding-member offer to all 340 ($29/mo locked for a year, first month refundable), measuring paid pre-orders, not replies.

Phase 1 — Soft launch (September 20 – October 6): Stripe live in staging by September 20, production by September 30. Onboard 10–20 waitlist teams manually in the last week of September; instrument activation (first tracked deploy within 48h). Build the onboarding checklist from what those teams trip on.

Phase 2 — PH as amplifier, not debut (October 13 only if Phase 0 and Phase 1 gates pass; otherwise move it — the date is the cheapest thing in the plan): launch with billing already proven on real teams and activation instrumentation live.

Phase 3 — Distribution reality (October – March): identify where the existing ~3,400 monthly landing visitors actually come from and double that source; treat the blog and r/devops as credibility, not acquisition; add one outbound motion (direct outreach to eng managers of 5–15-person teams on mixed CI tooling) at 5 hours/week. Track net adds weekly against a 100-team curve.

The decision rule, rebuilt (below): the quit gate moves from $4,900 gross MRR to a number that funds the quit, and the rule gains an ELSE and a kill condition.

**What changed and why:**

| Change | Failure mode it closes | What it costs |
|---|---|---|
| Read IP agreement + written carve-out before public launch | #3 | $0–500 (one consult) and possibly an awkward conversation |
| Convert both EMs to paid pilots by Sept 15 | cut champions mode / #1's evidence base | Two uncomfortable asks; the answer might be no |
| Waitlist pre-sale with money, Sept 1 | hidden assumption (interest = demand), #1 | A 340-email send; might falsify the plan |
| Soft-launch to waitlist before PH; PH only if billing proven | #2, #4 | 2–4 weeks of PH delay risk |
| Instrument activation; onboarding built from real stumbles | #4 | ~2 weekends of instrumenting instead of features |
| Quit gate raised to $8k MRR for 3 consecutive months + 12 months post-quit runway | fatal flaw | Moves the earliest quit date well past April 2027 |
| Add one outbound channel; diagnose existing traffic source | #1, #6 | 5 hrs/week that come out of feature building |
| Written kill/extend criteria dated Feb 1 and Apr 1 | #5 | Pre-committing to a number you might have to act on |

**Pre-launch checklist:**

1. **IP agreement.** *Check:* read the assignment and moonlighting clauses yourself; if either is ambiguous, one hour with an employment lawyer. *Walk away if:* the agreement assigns side projects broadly and the employer declines a written carve-out — every month of public work after that point builds value in something you may not own. Do not launch publicly until resolved.
2. **Champion paper test.** *Check:* ask both engineering managers to sign a paid pilot (founding rate, $29/mo) by September 15. *Walk away if:* both decline or ghost — the plan's entire demand evidence was two verbal commitments, and if they won't sign, the evidence is void; postpone PH, run 20 problem interviews with teams that don't know you, and rebuild positioning before any launch.
3. **Waitlist money test.** *Check:* September 1 founding-member offer to all 340; count paid pre-orders by September 15. *Walk away if:* fewer than 17 paid (5%) — benchmark waitlist-to-paid is 2–5% and this list is five months cold; below 5%, the funnel assumption behind the 100-team goal is broken and no launch date survives it.
4. **Billing dry run.** *Check:* Stripe in production with one real charge (a pilot customer, not a test card) by October 6. *Walk away if:* not live by October 6 — move the PH date. Launching without billing burns the one PH shot to acquire a free cohort whose conversion you'll never cleanly measure.
5. **Activation dry run.** *Check:* 10 waitlist teams onboarded manually by October 10; measure time-to-first-tracked-deploy. *Walk away if:* median time-to-value exceeds one hour — fix onboarding before inviting 1,400 strangers into the same empty room.

**Decision rule:** *Quit IF* DeployBoard has held ≥ $8,000 MRR (net of churn) for three consecutive months AND ≥ 12 months of personal runway remains in the cushion after the quit, *ELSE* keep the job and continue nights-and-weekends. *Kill or shelve DeployBoard, in writing, the week of February 1, 2027, IF* paying teams < 40 despite the soft launch and PH launch having both run — that is the stall pattern, and the rule exists so the stall doesn't get renamed "almost." Sequence note: the risky capability tests (demand with money, billing, activation) all run *before* the one irreversible step (public launch under your name while employed, and later the resignation); the rebuild does not split the difference on the quit gate — a lowered gate inherits the worst of both worlds: below-breakeven income *and* forfeited salary.

**How the rebuilt plan dies:** the rebuilt plan still runs on one person's 10–12 hours a week, and it just added selling, onboarding, and legal admin to the engineering — the new weakest joint is that Phase 0's paper work consumes September, the Stripe project slips into October, and the PH date moves anyway, now colliding with the December B2B freeze. The pre-sale can also kill the plan in September — which is the point of it, but it means the most likely outcome of the rebuild is a cheaper, earlier funeral.

**Residual risk:** even rebuilt and executed perfectly, the segment may not hold the goal — small dev teams churn fast and churn hardest at exactly the $49 price point, and 100 of them may simply not be reachable by one founder's channels at any date. The rebuild de-risks the *quit decision*; it does not guarantee the *business*.

## 4. The Adversary

**Playing:** the $2M-seeded competitor who shipped a similar product last month at $299/mo. Motivation: they must show a growth curve steep enough to raise a Series A in 12–18 months; total teams-on-platform is the metric they'll be judged on, which pulls them downmarket whether or not downmarket is profitable. Resources: a full team, a marketing budget, and investor networks that include PH hunters and newsletter audiences. Risk tolerance: high — a free or cheap tier that loses money is a rounding error against the raise. What they *can't* do: serve a 6-person team well at $299 unit economics (their support cost per small account is underwater), build genuine small-team community trust quickly, or care about you specifically — you are 0.03% of their market. Their best alternative: ignore the sub-$100 segment entirely and keep moving upmarket, which costs them nothing and is what they'll do unless you become visible — the PH launch is exactly the event that makes you visible.

**The kill chain:**
- **Probe (now – mid-September 2026):** they join your waitlist from a personal Gmail, read your landing copy and your r/devops comment history, and add "deployment tracking for small teams" and its long-tail variants to their SEO sprint. Cost to them: an afternoon.
- **Position (late September – October 6):** they announce a Starter tier — free under 5 seats, or $79/mo — framed "for small teams," timed to land two weeks before October 13 so the comparison posts write themselves before your launch. They are not responding to you; you are the reference customer segment in their Series A narrative.
- **Strike (October 6–13):** they schedule their own full PH launch (they haven't spent that bullet yet) the same week, with a professional hunter, investor networks, and a launch-week annual discount — arriving with 50× your supporter base on the one day your plan depends on.
- **Entrench (November 2026 – March 2027):** a one-click GitHub/GitLab integration, migration guides "from spreadsheets and solo tools," and paid spend on the exact comparison keywords your blog was slowly winning. Your waitlist growth halves with no visible attack.

**Detection opportunities:**
- *Probe:* waitlist signups from competitor corporate domains, or personal-domain signups that click every feature page — visible in a monthly waitlist export, first of each month.
- *Position:* any change to their pricing page or a changelog entry mentioning "starter," "free," or "small teams" — visible monthly, and weekly from September 20 onward.
- *Strike:* their listing appears on PH's upcoming-products page, or their investors begin posting launch teasers — visible October 6–12, before launch day.
- *Entrench:* their integration announcements; your landing-page conversion rate dropping while traffic holds — visible in your own analytics weekly from November.

**The move you'd never see coming:** they never fight you at all. In Q1 2027 the competitor is acquired by — or partners with — a CI/CD platform, and deployment tracking ships as a native, free view over data the platform already owns. The category you're launching into stops being a paid category; your $49 undercut of their $299 becomes an undercut of *free*. This is mode #6 resolved: the killer is a changelog entry on a platform blog you don't read, three months after your launch, and it invalidates the frame rather than competing inside it.

**What this means you should change:** (1) Differentiate on the thing platforms and the competitor structurally won't do — a single deployment view for small teams on *mixed* tooling (GitHub Actions + a Jenkins box + Vercel), where no single vendor's native view works. (2) Never anchor the plan to one launch date — soft-launch first so PH is an amplifier, not a debut they can spoil. (3) Start the pricing-page and changelog watch now (tripwires below), because the position move is only defensible if seen in September, not October.

## 5. The Tripwires

| Failure mode | Measurable signal | Threshold | Check on | If tripped |
|---|---|---|---|---|
| #1 Funnel arithmetic | Paid pre-orders from the Sept 1 founding-member email to the 340 waitlist | < 17 paid (5%) | Sept 15, 2026 | Postpone PH; run 20 discovery calls with stranger teams; rebuild the channel plan around whatever the calls reveal |
| #1 Funnel arithmetic | Net paying teams post-launch | < 12 by Nov 15, 2026 (pace → <60 by April) | Nov 15, 2026, then the 1st of each month | Add the outbound motion immediately and extend the 100-team horizon to Oct 2027, in writing, same week |
| #2 September slip | Stripe live in staging | Not live | Sept 20, 2026 | Cut scope: waitlist soft-launch only in Oct; move PH to Nov 10 |
| #2 September slip | Logged build hours | < 8 hrs/week for two consecutive weeks | Every Sunday, Sept–Oct | Same as above — the hours log is the leading indicator of the slip |
| #3 IP assignment (early chain — before any point of no return) | Agreement + moonlighting policy read | Unread | Aug 31, 2026 | Stop all public launch prep until read; if ambiguous, employment-law consult by Sept 12 |
| #3 IP assignment | Written carve-out (if clause is adverse) | Not obtained | Oct 6, 2026 | Do not launch publicly under your name; pause until resolved or restructured |
| #4 Success kills | Activation: % of new teams with first tracked deploy ≤ 48h | < 50% | Oct 20, 2026, then weekly | Freeze feature work; build onboarding from session recordings before any further promotion |
| #4 Success kills | Support first-response time | > 24h median | Weekly from Oct 13, 2026 | Throttle acquisition (pull blog CTAs, pause outreach) until caught up |
| #5 Compound zombie | December paywall conversion of free cohort | < 5% | Dec 15, 2026 | Treat demand as unproven; freeze the April 1 framing and re-decide the plan from the paid data |
| #5 Compound zombie | Paying teams at the written checkpoint | < 40 | Feb 1, 2027 | Execute the pre-written shelve/sell decision that same week — no silent extension |
| #6 Frame blind spot | CI/CD platform changelogs + competitor pricing page | Any native/free deployment-tracking release | Jan 2, 2027, then quarterly | Pivot positioning to the cross-tooling angle or exit; do not outspend a free feature |
| Adversary — probe | Waitlist export: competitor domains or probe-pattern signups | Any | 1st of each month | Assume the roadmap is read; stop publishing feature detail publicly |
| Adversary — position | Competitor pricing/changelog | Starter/free tier appears | Sept 1, then weekly from Sept 20 | Do not price-war; switch all messaging to mixed-tooling differentiation; test annual $490 plans |
| Adversary — strike | PH upcoming page + investor teaser posts | Competitor launch scheduled Oct 6–16 | Oct 6, 2026 | Move your date two weeks; never go head-to-head on their budget |
| Adversary — entrench | Your landing-page conversion with traffic held constant | Drops > 30% over any month | 1st of each month, Nov–Apr | Assume keyword/category capture; shift content to integration-specific long-tail they can't claim |

**Kill condition:** stop — not adjust — when either combination fires. (a) *Demand falsified:* the September 15 waitlist pre-sale converts under 5% AND both engineering managers decline a paid pilot — the two independent evidence streams the plan was built on are both void, and launching anyway is gambling the cushion's future, not testing a hypothesis. (b) *Ownership adverse:* the IP agreement assigns side projects AND the employer declines a written carve-out by October 6 — every month of public work after that adds value to an asset you don't own. Separately, the February 1 checkpoint (< 40 paying teams after both launches have run, with hours/week below 8 for the prior month) is the zombie-pattern kill: the decision happens in writing that week, because the combination of a stalled funnel and exhausted capacity is the one this plan's author is least equipped to see from inside.

---

If you want to go deeper on the single most dangerous failure mode — #3, the unread IP assignment, the one with no warning sign and no recovery — say so and I'll map the exact sequence: what to look for in the agreement, the carve-out conversation, and the restructures that do and don't hold up.
