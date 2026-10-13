Short version: the "money only goes to registered charities" assumption is the weakest part of the design. Registration proves a charity exists. It doesn't prove the money ends up somewhere you'd defend in a headline, or that the donor is at arm's length from the recipient. Below are the attacks I'd expect, roughly ordered by likelihood and damage, then controls.

Assumptions: the $5,000 cap is on matches (so up to $2,500 of employee giving at 2:1, or about $1,667 at 3:1). The $1.2M budget works out to about $316 per employee, so a small number of heavy users could exhaust it. Quarterly payouts mean fraud is found before money moves only if you actually review before paying.

## Pocketing the money (it is possible)

- **Charity the employee controls.** Anyone can register a tiny charity, or already runs one (a family foundation, a school booster club, a church, a "friends of" group). The employee donates $2,500, you pay $5,000, and the charity pays the employee's salary, rent or "expenses". Small registered charities with no independent oversight are common. A smart insider could do this with their own entity.
- **Round-tripping.** The charity gives back the donation (a gift, a "scholarship", a purchased service, an event ticket). Donation platforms and bank transfers make this easy, because no one checks that the money stayed with the charity.
- **Benefit-in-return donations.** Gala dinners, auctions, school tuition "donations", and memberships are partly or wholly purchases. The receipt shows the full amount. OCR checks amount, date and name, not whether the donor got something back.
- **Donor-advised funds and pass-throughs.** Donations to intermediaries (giving platforms, DAFs, fiscal sponsors) may route onward to anywhere.

## Cheap, fake or recycled receipts

- OCR verifies that the text looks right, not that the money moved. Anyone can generate a receipt with a PDF editor or an AI image tool, and a bank-transfer confirmation is a screenshot.
- **Donation never made, or refunded.** Donate, claim the match, then reverse the card payment or request a platform refund. Your check never sees it.
- **Same receipt reused** by the same employee, or shared with a colleague (a spouse who also works there), or submitted in two years.
- **Someone else's donation.** Claiming a spouse's, parent's or company's gift as yours, or donating with company money or a corporate card.
- **Backdating.** Receipts dated in the prior year, or before employment, if the date check is only "looks plausible".

## The 5-donor 3:1 threshold is an obvious gaming target

- Five employees, one charity, one month unlocks a 50% richer match for all of them. A group of friends, or one person with four accomplices, can trigger it on demand for a charity they favor. Tiny donations ($5 each) count the same as $500 ones, so the threshold costs almost nothing to meet.
- Rings can be organized in an internal chat channel, which also makes this a visible, shareable exploit. It will spread once someone posts it.
- Sock-puppets: family members or contractors with portal accounts, if eligibility isn't tied to payroll.
- Combined with the per-employee cap, it rewards splitting: a person gets effectively more match per dollar by coordinating.

## The "every registered charity is eligible" decision (the headline risk)

This is the one I'd treat as most likely to produce a headline, and it's unrelated to fraud.

- A nightly pull of the national register will include political advocacy organizations, groups tied to hate or extremism, anti-vaccine or other contested causes, organizations under investigation, those that have been sanctioned or lost status, and charities with high fundraising or administrative costs. A matched gift of $5,000 to any of them, publicly disclosed, is an embarrassing story, whatever the donor's intent.
- Also: charities that were registered when you pulled them and deregistered later, or whose status is revoked between receipt approval and payment (up to a quarter later).
- Name collisions and lookalikes: a fraudulent entity with a name close to a famous charity, or a legitimate charity's name on a receipt from an imposter's bank account.
- Sanctions and terrorism-financing risk for charities with overseas operations. This is a legal matter, not just reputational, so ask your counsel.
- Employees can also donate to causes that conflict with company positions or customers, which then shows up as "Tolvane matched X".

## Gaming the approval thresholds

- **Structure under $2,000.** The manual review applies per single match. Splitting into several receipts to the same charity, across days, avoids review entirely. At 2:1 a $999 donation produces a $1,998 match that sails through. Repeated, that gets to the $5,000 cap with no human ever looking.
- **Receipt splitting at the platform level** (many small gifts through Givelark to one charity) also dodges any per-receipt scrutiny.
- Auto-approval means the first time a human sees the pattern is after payment, unless you build aggregate reviews.
- The threshold is public to anyone who has read the policy, which they have.

## Volunteer grants are the softest control in the design

- **Hours are confirmed by an email address the employee types.** That is self-attestation. The "contact" can be a friend, a relative, a personal alias, or the employee's own second email account at a lookalike domain. There is no verification that the person works at the charity.
- It pairs naturally with attack 1: an employee-run charity "confirms" 100 hours, and the company pays $2,500 a year per charity to it, with no donation required.
- Hours can be inflated, duplicated across employees, or performed on company time (double-dipping on paid volunteer leave, if you offer it).
- The cap is $2,500 per charity per year, but I don't see a cap on the number of charities. An employee could spread across many to extract much more. Check whether the total budget exposure is bounded.

## Budget and program-level exposure

- **Budget exhaustion.** $1.2M over 3,800 staff, with a generous 2:1 and 3:1 match and a $5,000 per-person cap. If 240 people hit the cap, the budget is gone. What happens when it runs out in, say, September? First-come-first-served favors those who rush on January 1, and that includes abusers.
- **Timing:** payouts a quarter later mean year-end rushes create a liability spike, and the liability may fall into a different fiscal year than the receipt.
- **Concentration:** one charity receiving a large fraction of your budget is a red flag in itself, and a sign of rings.
- **Departing employees:** they can submit a flurry before leaving, and the match gets paid after they've gone, so you have no leverage.
- **Tax and accounting:** matches triggered by payroll-linked behaviour have implications (for example, if a charity gives goods or services back), so check with finance and tax advisers.

## Insider and process risks

- Anyone in HR with review rights sees the spending patterns, and a reviewer can approve for friends. Single reviewer is a weakness.
- Portal accounts: can an administrator edit an approved record? Can the charity bank details be changed between approval and payment? Payment diversion (an attacker changing a charity's bank details) is a classic fraud, and "pay the charity" means someone holds a payee list.
- Privacy: publishing or logging who gave to what reveals sensitive information (religious, political, health). A leak is also a headline.

## Controls I would add, in priority order

**Do before January 1**

1. **Replace "every registered charity" with an eligibility gate.** Start with an allow-list policy: registered and in good standing, minimum age (for example 2+ years filing), published financials, and a ceiling on admin and fundraising cost. Exclude by category (political, lobbying, religious worship if that's your policy, anything with a sanctions or watch-list hit). Re-check status at payment time, not only at approval. Give employees a clear "not eligible, here's why" message and an appeal path.
2. **Conflict-of-interest declaration and related-party block.** The employee must attest that they, their family and household have no role (officer, trustee, employee, paid contractor) and no personal benefit from the charity. Screen against payroll data and the register's officer lists where available. Make false declarations a disciplinary matter, since that gives the rule real teeth.
3. **Aggregate review rules instead of a single-match threshold.** Review triggers should look at cumulative match per employee per charity per quarter and per year, not per receipt. Review any charity that is new to the program, any charity receiving more than a set sum or more than N donors, and a random sample (5 to 10 percent) of auto-approved items, so that the sample deters gaming.
4. **Fix the 3:1 rule.** Either remove it, or require a minimum donation per person (for example $50), count distinct individuals (not households), exclude donors who share a household or manager chain, cap the bonus per charity per month, and apply it only after the month closes (not in real time, so people can't see how many more they need). A simpler, safer alternative is a campaign-based boost for charities that you choose.
5. **Strengthen the volunteer grant.** Verify the confirmer: use an email at the charity's own domain taken from the register or the charity's website, not typed by the employee. Send the confirmation request from the system, to the charity's registered contact. Cap total volunteer grants per employee per year and the number of charities. Bar the confirmer from being a relative, and bar charities in which the employee holds a role.
6. **Define and publish the rules on benefit-in-return.** The matched amount excludes the value of goods, services, tickets, tuition or memberships received. Require the charity's tax-receipt amount (the deductible portion), not the gross payment, as the matchable amount.

**Verification of the gift itself**

7. Require an official charity tax receipt with a receipt number, and check it against the donor's name. Cross-check with the platform (Givelark and others) through its API or a verified-receipt link where possible, or limit accepted platforms to ones you can verify. Bank transfer confirmations alone should be weaker evidence: require the charity's receipt too.
8. Duplicate detection: hash the receipt, and check on receipt number, charity, amount and date. Flag the same card or bank fingerprint across employees.
9. **Hold period before payout** (you already have a quarter). Use it: payment should depend on the gift not having been refunded or charged back, with confirmation from the charity or the platform where available.
10. Add a clawback clause to the policy for refunded gifts and for false claims.

**Payment and operations**

11. Pay only to bank details verified from the register or by call-back, never details supplied on a receipt. Changes to payee details require a second person.
12. Segregation of duties: the people who run the program shouldn't approve their own matches or those of their reports. Two reviewers over a value threshold.
13. **Budget governance.** Set per-quarter spending limits, monthly dashboards, and a rule for what happens when the budget runs out (pro-rata, or a waitlist). Cap per-charity totals (for example 5 percent of budget) and an annual cap on any single charity.
14. Monitoring: simple dashboards would catch most of this, for example top charities by dollars and by new-donor count, charities that appear for the first time, employees at or near the cap, the number of receipts just under $2,000, clusters of employees who donate to the same charity in the same week, and charities with a connection to employees (shared addresses).
15. Privacy and communications: keep individual giving data restricted, publish only aggregates, and prepare a short statement for the likely questions ("how do you choose charities?", "do you match politically contested groups?"). Having a considered policy in hand is the best defense against the headline you are worried about.

## What I would deprioritize

- Obsessing over receipt forgery in isolation. It matters, but the structural issues (self-dealing charities, the 3:1 trigger, the unverified volunteer contact, and open eligibility) are cheaper for an attacker and bigger in dollars.
- Heavy-handed controls on ordinary donors. Most of your 3,800 people are honest, and the aim is to make abuse awkward, not to make giving a chore. Many of these controls only bite on exceptions (new charities, large totals, related parties).

## One sentence for finance

The money doesn't reach the employee directly, but a charity the employee controls, a coordinated group of five, or a friendly "volunteer contact" can each turn the match into personal benefit or into donations that Tolvane would not choose to be associated with, so tighten charity eligibility, add related-party declarations, replace the per-receipt review threshold with aggregate rules, and verify volunteer confirmers independently.

If you can tell me the jurisdiction, the specific register, and whether you publish matched gifts, I can tighten the eligibility rules and the legal points.
