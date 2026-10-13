Your instinct that "the money only goes to charities" is the weak spot. The charity recipient is not where most of the abuse happens. The abuse happens at the employee end: getting money into a charity the employee can influence, getting paid for hours that never happened, and draining the budget early. Here is how I would attack it, ranked by how likely I think it is to produce a headline or a loss, followed by controls.

Assumptions I've made: "registered charity" means the national register confirms registration only, not that the charity is legitimate or independent of the employee. The volunteer grant cap of "$2,500 a year" could be per charity or per employee; I've treated it as ambiguous and flagged it below. Figures are rough and based on what you gave me.

## Where I would attack

**1. Volunteer grants are self-certified.** The employee enters the contact's email, and nothing checks that the contact is a real person at the charity. An employee can enter their own address, a friend's, or a free webmail address they control, log 20 hours per $500, and send the grant to any registered charity, including one they or a friend run. Padding hours is cheap. If the $2,500 cap is per charity, one employee can claim $2,500 from each of several charities, which is up to $12,500 a year with no money spent. If it is per employee across all charities, the ceiling is $2,500 times 3,800 staff, roughly $9.5M, far above your $1.2M budget.

**2. Budget exhaustion.** The per-employee cap is $5,000 of matches, which needs a $2,500 donation at 2:1. Your $1.2M budget is used up by only 240 employees at full cap. Coordinated employees, or a few keen ones in Q1, can drain the budget before most staff get anything, and the quarterly payout lag hides the drain until it is too late. There is no company-wide ceiling or pacing rule in the design.

**3. Collusion to trigger the 3:1 bonus.** Five people who agree to give to the same charity in the same month each get 3:1. Five colleagues can do this in an afternoon, and it cuts the donor's cost to reach the cap from $2,500 to about $1,667. The boost also rewards clustering on a single charity, which is the pattern you most want to avoid.

**4. Sham or captured charities.** A registered charity can be run by the employee, a relative, or a friend, or it can be dormant or newly registered. Matches flow straight to its bank account, and money can come back to the employee through fees, "gifts", or other arrangements. The register check does not catch any of this. A conflict-of-interest question on the form does not either, unless someone checks it.

**5. Threshold splitting.** HR reviews matches over $2,000, which is a donation of about $1,000 at 2:1 or about $667 at 3:1. Splitting one gift across two charities or two receipts keeps each match under the threshold and auto-approves it. The review rule is per match, not per employee or per charity, so it does not see the total.

**6. Receipt forgery and reuse.** OCR confirms that the text on a receipt says what the employee typed. It does not confirm the receipt is real. Screenshots, edited PDFs, and bank-transfer confirmations are easy to fake. Platform receipts from Givelark and similar services may be easy to reproduce. The same real receipt can also be uploaded by two employees or twice by one, and a receipt from December can be reused in January if the year check is weak.

**7. Donate, get matched, then refund.** The match is paid in the quarter after approval. If the donation is refunded or charged back after the match is paid, the employee keeps the match and the charity keeps the match, unless you have a clawback. Nothing in the design checks for refunds before payment.

**8. Insider and payee-change risk.** HR staff can approve their own matches or those of relatives, and portal admins can change charity lists or payee bank details. A changed bank account for a charity is the classic route for diverting a payment, and the design does not say payee changes need a second approver.

**9. Reputational exposure from the charity list itself.** "Every registered charity is eligible" means advocacy bodies, politically sensitive groups, and organisations that later lose registration or are investigated are all eligible automatically. A match to a charity that is later found to be fraudulent or extreme would be the headline you are worried about, even if no money was misdirected.

## Controls I would add

**Volunteer grants**
- Send hour confirmation from the charity's own domain, matched to the website on its register entry, to HR directly. Reject free webmail and any address at the employee's own company.
- Require a minimum period of prior activity for a charity before it can receive grants, and exclude charities registered in the last 12 months.
- Set a per-employee annual grant cap in total, and a per-charity cap, and decide which one you mean.
- Ask the employee to declare any role at the charity, and check against the employee directory.

**Budget and pacing**
- Set a hard company-wide annual ceiling with a pause switch, and a monthly pacing limit so no single month can consume more than a fixed share of the budget.
- Consider a lower per-employee cap in the first year, or a pro-rata rule if the budget runs short.

**The 3:1 boost**
- Either remove it, or cap total matches per charity per month, so a cluster cannot reach a large sum.
- Flag clusters for review: several employees giving to the same charity in the same month, sharing a device, address, or payment method.

**Thresholds**
- Apply the $2,000 review to the employee's cumulative matches per month or per year, not to each match, and to the charity's total per month.
- Add a random audit sample of automatically approved matches, for example 5 percent.

**Receipts**
- Prefer verification from the source: a bank or card feed, a platform API or confirmation sent directly from the platform, or the charity confirming receipt to HR directly.
- Deduplicate on transaction ID, amount, date, and charity across all employees, and reject anything dated outside the match year.

**Refunds and payment timing**
- Hold each match for a refund window, for example 60 to 90 days, before paying, or check for refunds or chargebacks immediately before payment.
- Include a clawback clause in the policy and in the charity agreement.

**Payees and segregation of duties**
- Verify each charity's bank details by a call-back to a number from the register, not one supplied in the portal.
- Require two people to approve any change to payee bank details, with a waiting period before the change takes effect.
- Prevent anyone in HR or finance from approving matches for themselves or for relatives, and log all approvals and list changes.

**Charity eligibility**
- Agree an exclusion policy with your board or leadership, for example for political, hate-related, or recently investigated organisations, and review the list each quarter rather than relying on the register alone.

**Before launch**
- Run a pilot in Q1 with a small budget and a few departments, and look at the outlier report before scaling up.
- Check with finance whether matches and volunteer grants have tax or reporting consequences in your jurisdiction. I have not assessed that.

If I had to pick the three to fix first, they would be the self-certified volunteer hours, the lack of an aggregate budget ceiling, and the payee bank-detail controls. Those carry the most money and the most embarrassing failure modes.
