Assumptions: one quarter of engineering capacity is the scarce resource, the three features are real commitments to named customers, and the cloud cut is a budget number finance has to hit this year. If any of those are wrong, the plan below shifts, but the shape should hold.

## The core move

Right now the three asks look like they compete for the same engineers. They mostly don't, once you ask what each VP needs underneath the request.

| VP | Stated ask | What they probably need | What would make them block |
|---|---|---|---|
| Engineering | Q3 for tech debt | Velocity and reliability back; not another quarter of "later" | Debt work cut again, or treated as a leftover |
| Sales | Three customer features | Deals and renewals that are at risk or waiting on specific commitments | Having to tell customers "no" or "not this year" with nothing in hand |
| Finance | 15% cloud cut | A credible, measurable path to the number, ideally with a date | Savings that are promised but not visible in the bill |

Three things connect these:

- Much of the cloud overspend usually comes from the same debt engineering wants to fix: oversized instances, unused environments, inefficient queries, no autoscaling. Debt paydown can be the cloud-cost program, if you aim it that way.
- Sales doesn't need three features shipped in Q3. It needs each customer to have a believable answer. Those are different things, and the gap between them is where you have room to trade.
- Everyone shares one goal: the company hits its year without a crisis, and nobody gets surprised.

## Proposed plan

**1. Aim Q3 debt work at cost first.**
Engineering gets the quarter, but the first priority within it is debt that cuts cloud spend: rightsizing, shutting down idle resources, storage tiering, fixing the worst-cost services. Debt that doesn't touch cost goes second. Engineering keeps the quarter. Finance gets a delivery vehicle for the savings.

**2. Fund one feature in Q3, with a protected slice.**
Reserve a fixed share of capacity (a starting point is 20 to 25 percent) for the single feature with the most revenue attached. Sales picks it, but has to back the choice with the deal or renewal value at stake. The other two features get firm Q4 slots with dates and scope, plus a customer-ready message. Where a customer truly can't wait, check whether a smaller version or a workaround covers the need.

**3. Make the 15% staged and visible.**
Ask finance to accept a path instead of a single end-of-quarter cliff. For example, roughly 5 to 6 percent from quick wins by the end of Q3, the rest by the end of Q4 or Q1 as the heavier debt work lands. Cloud cost gets reported monthly by service so the savings are visible, not asserted. Finance gets the number, plus a way to check it.

**4. Add an agreed rule for surprises.**
If savings are running behind at the midpoint, the protected feature slice shrinks. If a large deal needs a Q4 feature pulled forward, it gets pulled only by swapping something equivalent out, with all three VPs informed. This makes the plan hard to quietly erode.

## What each person gives and gets

| | Gets | Gives |
|---|---|---|
| Engineering | The quarter, aimed at debt with a cost story that makes it harder to cut | About a quarter of capacity to one feature; a prioritization rule inside the debt list |
| Sales | One feature now, two with dates, a message for customers | Three features in Q3 |
| Finance | A funded, tracked path to 15% | The full cut by end of Q3; some savings arrive in Q4 |

## How to get all three to sign

- **Talk to each one separately first.** Don't present this cold in a group meeting where anyone can block. Ask each: "What does a good outcome look like for you, and what would make you say no?" Check my assumptions about their needs against what they tell you.
- **Test the linking claim before you rely on it.** Have an engineer or the infrastructure lead spend a day identifying how much of the cloud bill is addressable by debt work, and rough dollar figures. If it covers most of 15 percent, the plan is strong. If it covers a third, finance needs a different lever (reserved capacity, vendor commitments, cutting a low-value workload), and that becomes a fourth item in the package.
- **Get Sales's real deal data.** Ask which of the three features is tied to a signed or imminent contract, and what the customer was actually told. If all three are contractual with Q3 dates, the plan needs a bigger feature slice and the debt scope shrinks. Better to find that now.
- **Then one joint session.** Open with the shared goal, show the table above, and ask for a specific response: "Can you live with this, and if not, what is the smallest change that would fix it?" You want each of them to say they can support it, not merely that they won't fight it.
- **Write it down.** One page: what's committed, dates, the surprise rule, and a review at the six-week mark. This prevents the plan being reopened every time someone feels pressure.

## Where this could still fail

- The cost savings don't materialize at the level assumed. Mitigation: the day of analysis up front, and the midpoint rule.
- Sales has a customer with a hard Q3 deadline that you don't know about yet. Mitigation: ask before you propose.
- One VP agrees in the room and doesn't follow through. Mitigation: monthly shared reporting of cost, feature progress and debt work, visible to all three.
- If they truly can't agree, escalate to the CEO with this as your recommendation and a clear list of what each side objects to, instead of letting the roadmap stall.

If you can tell me the contract status of the three features and what share of the cloud bill is waste, I can tighten the numbers and the Q3/Q4 split.
