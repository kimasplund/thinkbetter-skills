# Recommended Agreement: Q3 Roadmap (Tech Debt, Customer Features, Cloud Cost)

Assumptions, since I can't check them: Q3 is one quarter of fixed engineering capacity, the three customer features are real asks tied to named accounts or deals, and a meaningful share of cloud spend is waste or over-provisioning that engineering work could remove. If these are wrong, the shape of the deal below still holds but the percentages shift.

## Stakeholder Landscape

Each VP has a veto, so you need a plan all three can accept, not the one that scores best on average. Each is asking for something specific, but the need underneath is different.

| Stakeholder | Stated position | Underlying interest | Power | What would make them block |
|---|---|---|---|---|
| VP Engineering | Q3 for tech debt | Protect delivery speed and reliability, stop the team burning out, avoid a debt crisis later | High (controls capacity) | Another quarter of "next quarter" promises; debt work cut to a token amount |
| VP Sales | Three customer-requested features | Close or keep specific revenue; credibility with customers who were told "soon" | High (can escalate via revenue and customers) | Features that slip with no date, or ship so late the deals are gone |
| VP Finance | 15% cloud cut | Hit a margin or budget target; predictable spend | High (controls budget and can freeze spend) | No visible savings number, or savings that depend on a "later" that never arrives |

## Zones of Agreement

- All three want the company to be healthier at the end of Q3 than at the start: more revenue, lower cost, a team that can still ship.
- Much of the tech debt and the cloud bill are probably the same thing. Over-provisioned infrastructure, inefficient queries, unused environments and legacy services are debt and cost at once.
- Nobody wants a roadmap that gets reopened in week six. All three would trade some of what they asked for to have a plan that holds.

Foundation statement to open the meeting with: "We all need Q3 to protect revenue, lower cost, and leave the platform able to ship in Q4. The question is sequencing and who funds what, not whether any of these matter."

## Conflicts Addressed

| Conflict | Type | Resolution |
|---|---|---|
| Engineering vs Finance: debt time vs cost cut | Mostly false | Define the debt work so the first slice is cost-reducing (rightsizing, decommissioning, caching, storage tiering). Engineering gets debt paid; Finance gets savings. |
| Engineering vs Sales: capacity for debt vs features | Resource | Split capacity explicitly and sequence by customer deadline. Do not fight over the whole quarter. |
| Sales vs Finance: new features usually raise cloud spend | Interest | Set a cost budget per feature and count its spend against the 15% target, so the cost of growth is visible rather than hidden. |
| "Which three features, how big?" | Possibly false | Ask Sales which deal or renewal each feature protects and by when. Often one feature is the real blocker and the others are nice-to-have, or one can ship as a smaller version. |

## Proposed Agreement

A split quarter with a cost-first start and gates that release the next tranche of work.

Suggested capacity split (adjust to your real numbers):
- About 40% to debt work, with the first half of that explicitly targeted at cost-reducing items.
- About 45% to customer features, ordered by the date each customer or deal needs it.
- About 15% held as buffer for incidents and estimate misses, so nobody gets surprised mid-quarter.

Sequence:
1. **Weeks 1-3: quick wins and scoping.** Engineering delivers the cheapest cloud savings first (idle resources, rightsizing, retention policies). In parallel, Sales brings deal-by-deal deadlines for each feature, and engineering returns sized estimates, including a smaller "version one" of each.
2. **Weeks 4-9: the biggest feature or two, plus the main debt items.** The feature tied to the earliest, largest revenue ships first. Debt work that unblocks the later features is pulled forward, because it speeds Sales' own delivery.
3. **Weeks 10-13: remaining feature(s), debt completion, and savings reconciliation.** Any feature that can't fit is committed to a specific early-Q4 slot, not left as "later".

Finance target: instead of one fixed 15% by end of Q3, agree a ramp (for example, 5% by week 4, 10% by week 8, 15% run-rate by quarter end), with the savings measured against a named baseline. If cost-reducing debt work delivers less than planned, the gap is closed by a pre-agreed list of further cuts (for example, non-production environments), so Finance isn't relying on hope.

### Value Distribution

| Stakeholder | What they get | What they give |
|---|---|---|
| Engineering | A protected, named share of the quarter for debt, with the first items justified by dollars, which makes them hard to cut later | Not all of Q3; the debt scope is trimmed to what also helps cost or unblocks features |
| Sales | Features sequenced by real customer deadlines, a committed Q4 date for anything that slips, and a cleaner estimate up front | Not all three on the original dates; possibly a smaller first version of one or two |
| Finance | A visible, measured savings ramp and a fallback list if it falls short | Accepting a ramp instead of the full 15% on day one; accepting that some feature spend is counted inside the target rather than excluded |

## Commitments and Conditions

- Each VP states in writing what they will defend if challenged by their own team or by the CEO.
- Joint checkpoint at week 4 and week 8, with three numbers: savings achieved vs ramp, feature progress vs date, debt items completed vs plan.
- If savings are behind ramp at week 8, the pre-agreed fallback cuts trigger automatically. If a feature estimate grows by more than an agreed threshold (say 25%), Sales and Engineering decide together between cutting scope and moving the date, and Finance is told the cost impact.
- Any change to the split needs all three VPs. No one reallocates quietly.
- Disagreements go to a named tiebreaker (the CEO or COO) with a one-page recommendation, not a debate in the roadmap meeting.

## Implementation Notes

- **Don't start with the whole deal in a group meeting.** Meet each VP separately first, ask what success looks like for them and which part they'd give up last. Then test the draft with each so nobody sees a surprise in the room.
- **Get the facts that dissolve fights before the meeting:** the revenue and deadline behind each feature (from Sales), the cost impact of each debt item (from Engineering and Finance), and the cloud baseline Finance will measure against.
- **Let each VP present their own part** of the plan. People defend what they've announced.
- **Offer a visible give from each side.** Engineering's offer to start with cost-saving debt work is the main concession that makes Finance and Sales comfortable, so lead with it.
- Circulate a one-page summary right after the meeting, with the numbers, the checkpoints and the fallback triggers, so there's a single record to point to later.

## Risks to the Agreement

- **Sales commits dates to customers before estimates exist.** Weakest point. Mitigation: no customer-facing date until Engineering has sized it in weeks 1-3.
- **Finance's 15% turns out unreachable through debt work alone.** Mitigation: the fallback cut list is agreed now, so the conversation at week 8 is mechanical rather than a new negotiation.
- **Engineering treats the debt share as untouchable and pads it.** Mitigation: tie each debt item to a cost or delivery-speed outcome and review it at the checkpoints.
- **Scope creep from "just one more feature."** Mitigation: the buffer and the rule that changes need all three VPs.
- **Someone agrees in the room but doesn't implement, or reopens it with the CEO.** Mitigation: written commitments, named owners per workstream, and the pre-agreed tiebreaker so an end-run has no new ground to stand on.
- **If the real constraint is different** (for example, one feature is worth far more than the others, or the cloud target is a hard board commitment), say so early. The split changes, but the approach of making each side's give visible and gated does not.
