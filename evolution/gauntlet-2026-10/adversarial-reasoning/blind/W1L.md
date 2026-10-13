The assumption to challenge first is "money only goes to registered charities, so nobody pockets it." Registration shows a charity is legal. It doesn't show that the money does good, or that no one connected to the donor benefits. Several attacks below put money in someone's pocket, and several others just make a headline. Roughly in order of how much I'd worry:

## Round-tripping through a charity the employee controls or benefits from (real money loss)

- **Attack:** An employee, or a relative, starts a small registered charity, or sits on the board of one, or is paid by one. The employee donates $2,500 and the program pays out $5,000 to that charity. The employee gets a tax receipt and the charity gets $7,500. If the charity pays a salary, rent or consulting fees to the family, the money has left the system. The 3:1 rate makes it worse: $1,250 of the employee's own money brings in $3,750.
- **Why it works:** The whole register is eligible and nobody checks relationships.
- **Controls:**
  - Require a conflict-of-interest declaration on each submission: "I, my family or my household are officers, employees, or paid contractors of this charity."
  - Cross-check the register's director and officer data, and the charity's address and bank details, against HR and payroll records.
  - Flag charities that receive matches from a small number of employees but a large dollar total.
  - Cap the total match any one charity can receive per year, for example 2-3% of the budget.

## Circular giving and 3:1 collusion (the threshold is a bounty on coordination)

- **Attack:** Five or more employees agree to give to the same charity in the same month. Each gets 3:1. Groups can rotate charities each month, or pool money so that only one person pays. Reimbursing each other, or having one person's card pay for several "donations", is hard to see on a receipt.
- **Attack:** Donate $1 or a few dollars from five accounts to trigger the 3:1 rate, then have a sixth person give a large amount in the same month. If the rule is "five donors," the size of those donations is irrelevant, so the rule can be gamed cheaply.
- **Why it works:** The threshold counts people, not dollars or independent behavior.
- **Controls:**
  - Drop the 3:1 tier, or fix it as a campaign the program picks, such as a disaster appeal or a named charity of the quarter.
  - If you keep it, set a minimum donation size per person for the tier, cap the uplift per charity per month, and apply it only to donations made on different days.
  - Look for patterns: the same group of employees repeatedly landing on the same charities, or the same donation amounts.
  - Treat the match as a pledge until it has been confirmed.

## Receipt fraud and "donation" that isn't one

- **Attack:** OCR confirms that the receipt is readable, not that it's genuine. Anyone can edit a PDF or generate a fake Givelark or bank-transfer confirmation with the right amount, date and charity name. A bank-transfer confirmation is a screenshot or PDF the employee produces, so it is especially easy to fake. A real receipt can also be submitted twice, or for a donation that was refunded or charged back, or a gift to a charity that was then returned.
- **Attack:** An employee pays for a ticket to a gala dinner, an auction purchase, or raffle tickets, then submits it as a donation. The "donation" received goods or services in return, which isn't a gift.
- **Controls:**
  - Check receipts against a unique reference (receipt number, transaction ID) and refuse duplicates across all employees and all years.
  - For online platforms, get the donor's confirmation through the platform's own verification link or API where possible.
  - Treat bank transfers as higher risk: require the charity's official receipt, and sample-check with the charity itself.
  - Require the employee to attest that no goods, services or benefits were received, and exclude event tickets and auctions.
  - Run a hold period before payment (you already pay the next quarter, which helps) so refunds can surface.
  - Audit a random sample of receipts, say 3-5%, by contacting the charity, and publish that you do this. That deters most casual fraud.

## Splitting to stay under the $2,000 review (a design flaw in your own threshold)

- **Attack:** "HR reviews any single match over $2,000; everything else is auto-approved." Someone submits several receipts of $999 each (a $2,000 match is $1,000 at 2:1, or about $667 at 3:1). All pass automatically, and the total is $5,000. With 3,800 staff, the unreviewed portion could be nearly the entire budget.
- **Controls:** Review on the cumulative total per employee, per charity and per period, not per match. Add randomized spot checks inside the auto-approved group so the threshold isn't a known target. Review every new charity and every charity above a cumulative dollar limit regardless of single-match size.

## The volunteer grant: an unverified honor system

- **Attack:** The employee enters the "contact at the charity" email, so the employee can supply their own, a friend's, a throwaway address or a lookalike domain. The "confirmation" is then fake. At $500 per 20 hours, up to $2,500 a year, with 3,800 staff, that is a cheap way to send $500 to a charity the employee chooses. Hours can also be claimed during paid work time or for activity that isn't volunteering (for example, a board seat or a paid role).
- **Controls:** Don't accept employee-entered contacts. Take the confirmation contact from the charity's public record, or send confirmations through a verified channel (the charity's registered email or phone). Require an attestation that the hours were unpaid and outside work time. Cap hours per month. Check that hours don't overlap with timesheets. Sample-audit.

## Headline risk: who the money goes to

This is the part you said you most care about, and "registered" is a weak filter here. Every registered charity is eligible, including:

- charities that are political or advocacy-oriented, or in contested areas, that staff, customers or the press would see as controversial;
- charities that have been sanctioned, revoked, under investigation or flagged by the regulator, or that are named in the news. The register is pulled nightly, but status changes lag;
- charities linked to hate groups, or to organizations whose purposes differ from the charity name or purpose (the name on the receipt matches, but the cause isn't what it seems);
- lookalike names ("Red Cros", a name nearly identical to a real one) that an OCR check on the name accepts;
- a donation to a charity that is a front for private benefit, such as a donor-advised pass-through.

A $1.2M program that matches at 2:1 to 3:1 can also be turned into a campaign tool. A coordinated group can use the 3:1 rule to direct tens of thousands of company dollars to a cause that embarrasses you.

**Controls:**
- Add an eligibility policy that is published and sits above the register: excluded categories (for example partisan political activity, hate groups, and charities with active regulatory action), and a way to decline individual charities.
- Screen new charities against regulator warnings, sanctions lists and adverse media before first payment.
- Hold payment to any charity first seen in the program until a person has looked at it.
- Write a short statement of the "who we won't fund" rule now. When a headline arrives, having a rule you applied consistently is the best defense.

## Smaller points

- **Timing and cap gaming:** The $5,000 cap is per calendar year and payment comes the next quarter, so December receipts, January 1 resets and the year-end crossover are exploitable. Define what date counts (donation date, approval date, payment date) and enforce one rule.
- **Budget exhaustion:** $1.2M at 3,800 staff is about $316 each. If the cap is $5,000 per person, a few hundred participants at the cap would use the whole budget (240 employees at $5,000 each is the full $1.2M). First come, first served means a small group can drain it early and leave everyone else with nothing. Decide whether you want a per-employee ceiling that you can actually afford, a monthly budget, or a pro-rata rule, and publish it.
- **Leavers and non-employees:** Check employment status at both approval and payment. Check that contractors and departed staff are handled.
- **Insider access:** Whoever can edit charity records, bank details or approvals in the portal needs separation of duties. Changing a charity's payment details should require a second person and a call-back to the charity.
- **Payments going to the wrong place:** Pay only to the bank account on the charity register or one verified by call-back, never an account supplied on a receipt or by the employee. Business email compromise (a fake "we've changed our bank details" message) is a classic attack on programs that pay many charities.
- **Privacy:** You hold donation receipts that reveal religion, health and politics. Limit access and retention.

## What I'd change first

1. Review cumulative amounts, not single matches, and add random sampling to auto-approval.
2. Remove or redesign the 3:1 five-donor rule; it is the easiest thing to game and the hardest to defend.
3. Add a conflict-of-interest declaration and a register-based relationship check.
4. Replace employee-entered volunteer contacts with charity-verified ones.
5. Add an eligibility policy and screening on top of "registered".
6. Detect duplicate receipts, and audit a sample of them against the charity.
7. Cap the share of the budget any one charity can receive, and decide how the budget is rationed so it can't be drained early.

Assumptions: I don't know your jurisdiction's register, your tax rules, or what your portal can integrate with. Some of the controls above (such as director cross-checks and platform verification) depend on what data is available, so treat them as a menu and prioritize by cost. I haven't seen your actual fraud history, so the likelihoods are my judgment, not data. A short pilot with the changes above, plus a post-quarter review of the highest-volume charities, would show you quickly which of these risks are real.
