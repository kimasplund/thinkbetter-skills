The "money only goes to registered charities" assumption is the weakest part of the design. It covers the pocketing risk less well than you think, and it does nothing for the headline risk. The budget has no hard ceiling either. Here is where I would attack, ranked by what I would worry about most.

## Top attack paths

**1. The program can commit far more than $1.2M.**
- Each of 3,800 people can draw up to $5,000 in matches, so the theoretical liability is about $19M. Payment lags a quarter behind approval, so you can owe money you no longer have.
- A modest pile-on would exhaust the budget. About 240 people maxing out is enough, and so is a viral internal campaign in the first weeks of January.
- Volunteer grants sit outside the cap as I read it, and the design doesn't say whether the $2,500 limit is per employee or per charity.
- Control: set a hard program-level ceiling, and say in the policy that matches are subject to funds available. Accrue liability on approval rather than on payment. Pro-rate or queue matches when you hit 80% of budget. State the volunteer-grant cap and make it count against the same ceiling.

**2. Charities that belong to someone.**
- Anyone can register a small charity. An employee, a relative, a friend or a vendor can then route donations to it. A $2,500 donation at 2:1 yields a $5,000 match to an organisation the donor controls. Charities can pay salaries, rent or "consulting fees" to their own trustees.
- The register tells you a charity is legal. It does not tell you the charity is independent of the donor.
- A related case is round-tripping. A charity gives the donor a receipt, then quietly returns the money or provides a benefit. The employee ends up with a tax deduction and a free match for the charity.
- Control: ask employees to declare any role, family tie or paid relationship with the charity. Block matches where the charity is a board, family or employer-linked body. Add a minimum age since registration (for example 12 months) and a minimum income or filing history before first eligibility. Flag a charity whose match income from your program is large relative to its total reported income. Run a conflict-of-interest check, including a procurement and customer-relationship check (see 6).

**3. Fabricated or recycled receipts.**
- OCR on amount, date and charity name proves only that a document says those things. Bank-transfer confirmations are easy to edit. Nothing ties a receipt to the employee's own money.
- Likely abuses:
  - Reusing one receipt, or the same donation claimed twice by a couple.
  - Claiming a donation made by someone else, such as a friend or parent, so outsiders get access to your 2:1.
  - Claiming a donation that was refunded or charged back after the match was approved.
  - Pooled "donations" that pass through one employee's account.
- Givelark-style platforms add their own gaps. Some receipts show a payment to the platform or to a personal fundraiser page, not to the charity.
- Control:
  - Require the donor name on the receipt to match the employee.
  - Deduplicate on a receipt-hash, transaction ID, amount plus date plus charity, and across household members.
  - Prefer platform data (an API or a verified feed) over uploaded images.
  - Hold the match until the refund window has closed. The quarter lag already gives you this, so use it.
  - Have the charity confirm receipt at payment. Spot-audit a random 5 to 10% of receipts, and audit every employee who claims close to the cap.

**4. The 3:1 clustering rule is an invitation to coordinate.**
- Five people can agree in a chat to give to the same charity in a month, and every one of them gets a 50% richer match. Donors can arrange this deliberately, including with charities they control (see 2). Charity fundraisers can also advertise it.
- It is also a headline engine. Five or more staff piling into one charity, even a lawful one, creates a visible spike of company money that you did not choose.
- Control: either drop the 3:1 tier or cap the bonus at a fixed dollar amount per charity per month. If you keep it, count distinct donors only after approval, exclude linked donors, and apply it only to a vetted list. Review any charity that triggers the tier before the money goes out.

**5. Structuring under the $2,000 review line.**
- Anything below $2,000 is auto-approved, so splitting is trivial: several $900 donations to the same charity on different days, or the same donation spread across several platform receipts. This also hides an unusual charity from review.
- The review line is per match, so a single person can reach the $5,000 cap with no human ever looking.
- Control: aggregate review by employee and by charity over a rolling window. A review trigger should fire on the total per charity per year, on first-time charities, on a charity new to the program, and on any charity receiving matches from more than a handful of employees. Auto-approval should be limited to charities on a vetted list.

**6. Headline risk: legal but indefensible recipients.**
- "Any registered charity" includes organisations that are controversial, politically aligned, under regulator investigation, or linked to hate groups or extremism. It may also include charities whose registration is revoked or suspended, or which are sanctioned.
- A nightly register pull helps only if you re-check before paying. Payment is a quarter after approval, so a charity's status can change in between.
- Lookalike names are another route. A charity can closely mimic a well-known one, and OCR matching on the name alone won't catch that.
- Bribery by proxy deserves a separate line. A customer's decision-maker, a regulator or a public official sits on a charity's board, and an employee in sales or procurement routes company-matched money there. The money reaches a registered charity and the optics are still bad.
- Control:
  - Use an allow-list with a screening step, or a block-list plus category exclusions (political, lobbying, religious proselytising if that suits your values, and any charity under regulatory action).
  - Run sanctions and adverse-media screening on first match to any new charity.
  - Re-verify registration status on the payment date, and pay only to bank details taken from the register or confirmed with the charity, never entered by the employee.
  - Set an escalation path and a statement ready for the press in advance.
  - Decide now whether you publish match totals by charity. Publishing helps with transparency but also exposes you.

**7. Volunteer grants rely on a fakeable confirmation.**
- The employee types the confirming contact's email. They can enter their own second address, a friend or a relative. If the charity is theirs (see 2), they can confirm the hours themselves.
- $500 for 20 hours is $25 an hour of company money for unverifiable time. Hours could also overlap with paid work time or with another employer's program, and a volunteer role on the charity's board might not count as volunteering at all.
- Control: send the confirmation to an address on the charity's registered domain, or to a contact on the register, never one typed by the employee. Require a signed hours log, with a date range and a named supervisor. Reject confirmers who share a surname or address with the employee. Limit volunteer grants to vetted charities, and require manager visibility where hours fall in work time.

## Edge cases worth a rule

- Matching at year end: a donation made on 31 December versus a receipt dated the next day. Define which date counts.
- Refunds, chargebacks and cancelled recurring gifts after approval.
- Donations in foreign currency or to foreign charities, and exchange-rate disputes.
- Employees who leave before payment, and employees who change status mid-year.
- Anonymous or in-memory-of donations where the receipt lacks the donor's name.
- Duplicate registered charities, mergers and name changes in the register.
- Cap boundary: the $5,000 cap with 3:1 can leave a leftover amount. Decide whether it carries over.
- Employees in sanctioned countries, or charities that operate there.
- Tax receipts: the company may be implicated if employees claim deductions on gifts that were returned.

## What I would do first

1. Set a program ceiling and accrual accounting, and fix the volunteer-cap wording. This is cheap and removes the largest exposure.
2. Replace "every registered charity" with an allow-list, or at least screening before first match, plus status re-verification on payment day.
3. Drop or restrain the 3:1 tier. It adds more risk than it adds generosity.
4. Move review from per-match to per-employee and per-charity totals.
5. Require donor-name matching, deduplication and a conflict-of-interest declaration.
6. Move volunteer confirmation to verified charity contacts.
7. Audit a random sample each quarter, and report the findings to finance.

## What remains after these controls

- A determined insider with a real, independent-looking charity and genuine money can still get a legitimate-looking match. You will catch that mainly through pattern monitoring, not at the door.
- A lawful charity can still become controversial after you pay it. The remedy is a published policy that lets you suspend future matches, and a communications plan.
- Verification costs staff time. Tier it so the common case stays automatic and only the unusual ones get reviewed.

I have assumed the $5,000 limit is on match dollars as you wrote it, that the bank-transfer confirmations are uploaded images, and that finance has not already set a program ceiling outside this design. If any of those is wrong, the order above changes a little, but the top three items stand.
