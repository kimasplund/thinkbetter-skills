**Short version:** the design is more exposed than "money only goes to registered charities" suggests. A registered charity can be controlled by the person who asked for the match, so the money can still reach someone's pocket. The bigger risks are probably the 3:1 trigger, the $2,000 review line, the receipts you accept, and the volunteer grants. Several of these can also produce the headline you're worried about, with no fraud involved.

## Where I'd attack it, most serious first

**1. Charities the employee controls or benefits from.** Everything on the national register is eligible, and registration says little about who benefits. An employee, a relative or a friend can run a small registered charity, such as a family foundation, a sports club or a parent-run school fund. The employee donates $2,500 and the company adds $5,000 (2:1, up to the cap). The charity then pays a salary, "expenses" or a consultancy fee to the insider. The match is on its way to a private pocket by the second hop. Variants:
- Donations where the donor gets something back: gala tickets, tuition-linked "fees", memberships, raffle entries.
- A charity that quietly refunds or kicks back part of the gift.
- The employee's own charity or a relative's, with no conflict-of-interest declaration.

**2. The 3:1 trigger works as a coordination prize.** "Five employees, same charity, same month" is easy to hit on purpose.
- A group of friends, or a Slack or WhatsApp channel, can each give a small amount to a favoured charity. Every match rises 50% on all of their money, and the only price is the 3:1 trigger itself.
- Five colluding employees can hand a charity they jointly control up to 3x their gifts each month.
- Controversial causes can organise this too. A few dozen staff pushing a political, religious or campaign charity to the threshold every month would produce exactly the story you fear: "Tolvane tops up gifts to X at 3:1."
- The trigger also leaks information. If a charity "reaches five" and that is visible, staff can infer who gave to what.

**3. The $2,000 review line is a published, splittable threshold.** Anything under it is auto-approved.
- A 2:1 match of $1,999 is a $1,000 gift. Someone can stay under the line on every receipt and still reach the $5,000 cap through several gifts, several charities, or several months.
- Receipts can be split across household members. Nothing in the design stops two employees in one household each donating to the same family-run charity.
- The line applies per match, not per charity. So a charity can receive many auto-approved matches that add up to a lot, and nothing is reviewed in aggregate.

**4. Receipts are easy to fake, and the checks are shallow.**
- OCR confirms that the text on a document looks right. It can't tell whether the money moved. An edited PDF, a screenshot or an AI-generated receipt passes if the amount, date and charity name are correct.
- Bank-transfer confirmations are the weakest evidence you accept. They're easy to fabricate and show only that a transfer was initiated.
- Online platform receipts, Givelark included, can be edited. A donation can also be made and then refunded, charged back, or recalled after the match is approved. You only pay a quarter later, so you have time to catch this, but only if you look.
- The same receipt can be submitted twice by one person, or by two spouses.
- Nothing checks that the donation was made in the calendar year, or after Jan 1, or by the employee (rather than a relative, a company, or an anonymous fund).

**5. Volunteer grants are self-certified.** The employee types in the charity contact's email, so the "confirmation" can go to the employee's own second address, a friend, or a family member at the charity. At 20 hours per $500, up to $2,500 per charity per year, a person with a charity they control can claim the maximum with no real hours. Also unclear: whether the grants count against the $5,000 cap or the $1.2M budget. If they don't, they're a second, uncapped channel.

**6. The budget is far smaller than the exposure.** 3,800 staff at $5,000 each is $19M of theoretical match against a $1.2M budget. Unless there is an explicit cap and a stated rule for when it runs out, you risk:
- A rush in the first weeks of January, so the budget is gone by spring and the late, genuine donors are the ones who lose out.
- A payout rule nobody can explain when funds run short.
- Heavy gaming by a handful of people early on, which crowds out ordinary participation.

**7. Charity status can change before you pay.** Matches are paid in the quarter after approval, and eligibility comes from a nightly pull. In that gap a charity can be deregistered, put under investigation, suspended, or named in a news story. If your system pays on the original approval, you may send money to an organisation that is under a regulator's inquiry, on the sanctions list, or linked to extremism or fraud. Each of those is a headline.

**8. Payment diversion.** Matches go straight to the charity, so someone will try to change where the money goes: a fake email that "updates the charity's bank details", an inside change to a payee record, or a sham charity with a lookalike name. Without a check on the account the payment lands in, this is the classic business-email-compromise route.

**9. Insider and process risks.**
- The employee giving program owner, the HR reviewers and the portal admins all have power over approvals. One person can approve, edit payees, and release payments unless duties are split.
- Executives and senior staff matching to charities connected to clients or suppliers can look like pay-to-play.
- Donations from newly hired staff, leavers, contractors or temps (if they have portal access) are open questions in the rules.
- The portal holds a list of who gave to which cause: religious, political, health-related. A leak or an over-broad report to managers is itself an incident.

## Controls I'd add (ordered by value for effort)

| Priority | Control | What it stops |
|---|---|---|
| 1 | **Replace "every registered charity" with an eligibility screen.** Minimum registration age and income, not deregistered or under investigation, not on sanctions or watch lists, and an exclusion list for political parties, campaign groups and anything your board wants out. Re-check status on payment day, not just at approval. | #1, #7 and most headline risks |
| 2 | **Conflict-of-interest declaration, with consequences.** At submission the employee states they, a relative or a business partner is not an officer, trustee, employee or beneficiary of the charity. Cross-check trustee names against employee and vendor records. Anything that gives the donor a benefit (tickets, tuition, membership) is ineligible. | #1 |
| 3 | **Drop or rework the 3:1 trigger.** The simplest option is to remove it. If you keep it, apply it only to a short pre-approved list of campaigns (disaster appeals, an annual charity of the year), not to whatever five people choose. Don't show which charities are close to the threshold. | #2 |
| 4 | **Review by aggregate, not per receipt.** Review anything over $2,000 per employee per quarter, per charity per month, or per household/IP/bank account. Add random sampling of auto-approved matches (say 5 to 10%) and don't publish the threshold. | #3 |
| 5 | **Stronger evidence.** Accept receipts only from platforms you have verified (an API or a verification link, with a reference number you can check), and treat bank-transfer confirmations as supporting evidence only, not proof, unless the charity confirms. Hold payment until the refund window has passed. Hash receipts to catch duplicates. Require a charity-issued tax receipt above a set amount. | #4 |
| 6 | **Volunteer hours confirmed independently.** The charity confirms through an address from the register or your own vendor-style onboarding, never one the employee typed in. Reject free-mail domains and an address on the employee's own domain or surname. Count the grants inside the cap and the budget. | #5 |
| 7 | **Hard budget rules.** Set per-quarter pacing (for example 25% of the budget per quarter), a per-charity ceiling (say 5 to 10% of the annual budget), and a written statement of what happens when the budget runs out. Publish it to staff before launch. | #6, and the headline "ran out in March" |
| 8 | **Pay safely.** Take bank details from the register or a verified onboarding call, not from the employee or an email. Require a call-back on any change. Split duties so the person who approves isn't the person who changes payees or releases payments. | #8, #9 |
| 9 | **Privacy and disclosure.** Limit who can see per-employee donations, aggregate the reporting, and decide now what you'll say if a charity is controversial. | #9 |
| 10 | **Clawback clause in the terms.** If a match was obtained through a false receipt or an undeclared conflict, the company can recover it and take disciplinary action. | Deterrence for all of the above |

## What to ask before launch
1. Who decides which charities are out of scope, and who answers the journalist's call about one that slipped through?
2. What does finance consider "abuse": an employee profiting, or any match that embarrasses the company? The controls differ.
3. Are the volunteer grants inside the $5,000 cap and the $1.2M budget? The design doesn't say.
4. Can you pilot for a quarter, using manual review on everything, and then loosen up? It's much easier to relax controls than to add them after a story breaks.

## Residual risk
Even with all of this, you can't fully verify that a donation was genuine, or that a charity's spending is proper. A determined insider with a real, well-run charity can still divert some value. The realistic goal is to make abuse small, slow and detectable, and to make sure that if it happens, you found it first. I'd rate the confidence in this list as moderate to high on the categories, and lower on likelihood. I don't know your register's data quality, your platform contracts, or how much of your workforce is already active in giving.
