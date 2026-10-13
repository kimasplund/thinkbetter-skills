Your instinct that the money never reaches an employee's pocket is the main gap. The rules keep the company's money out of employee hands directly, but they do nothing to stop it reaching employees indirectly through the charity. The realistic headline is not "employee steals match", it is "company paid $X to a charity run by an employee or their friends". Below, attacks first, then controls. I have assumed volunteer grants come from the same $1.2M pool, and that the cap counts per calendar year.

## Where a smart attacker goes

**1. Round-trip through a cooperating charity.** Donate $2,500 to a charity that agrees to refund $2,500 (or pay it back as "consulting", "events" or "expenses"). The employee's net cost is zero and the company pays $5,000 in matches to that charity. The charity can be a real registered one that simply agrees to cooperate. The donation receipt and the refund are both invisible to your system.

**2. Employee-founded or friend-run charities.** Registration on the national register is cheap and slow to check. Someone registers a small charity, uses it as the recipient of matches and volunteer grants, and then uses the money for salaries, rent, or spending on people connected to it. Eligibility is "on the register", which is a weak test of legitimacy.

**3. Self-attested volunteer hours.** The employee types in the contact's email. They can enter an address they control, confirm their own hours, and earn $500 per 20 hours, up to $2,500 per year per charity. The same hours can also be claimed by several colleagues from one team event.

**4. Forged or reused receipts.** OCR checks that the text on a receipt matches what the employee typed. It does not check that the receipt is real. A PDF bank-transfer confirmation can be edited in minutes. The same receipt can be uploaded by several employees, or a receipt number can be reused across years.

**5. Splitting to stay under HR review.** HR reviews matches over $2,000. At 2:1 that is any donation over $1,000. An employee can split a donation into several receipts that each stay under the threshold, and the $5,000 cap can be exceeded if cap checks run before the earlier approvals have updated the total (a race condition at approval time).

**6. Gaming the 3:1 kicker.** Five employees donating to the same charity in a month each get 3:1. A small group can coordinate small donations to trigger it, and can also fund each other's donations, so the kicker is cheap to trigger and the group controls which charity receives it. The kicker also gives a strong incentive to herd people toward one or two charities.

**7. Year-end timing.** Matches are paid the quarter after approval. Donations near 31 December can be approved in January and counted against the wrong year, or used to get two years' worth of cap room, depending on whether the cap counts by donation date, approval date, or payment date. Nothing in your design says which.

**8. Budget exposure you may not have modelled.** At $5,000 per employee, $1.2M covers only about 240 fully matched employees. The theoretical maximum across 3,800 staff is $19M in matches plus $9.5M in volunteer grants. A modest uptake can exhaust the pool early in the year, which causes its own headline and the question of who gets cut off.

**9. Charity-status changes after payment.** A charity can be revoked or dissolved after you have paid. The nightly register pull only protects you at the moment of payment, and quarterly payment gives a window in which status can change.

**10. Reputational eligibility.** Every registered charity is eligible, including ones under investigation, ones in active media scandals, and ones whose politics or practices your company would not want to fund. The headline risk is that your program pays them.

## Controls I would add

**Budget and cap design**
- Set a hard annual pool and a rule for what happens when it runs out (pro-rata, first-come, or pause). Publish the rule before launch.
- Apply the $5,000 cap across all donation dates in the calendar year, using the donation date on the receipt. Enforce it at approval time inside a single transaction so parallel approvals cannot exceed it.
- Aggregate reviews per employee per year and per employee per charity per month, not per receipt. Trigger HR review on the aggregate total.

**Charity eligibility**
- Require the charity to be registered for at least 12 months, and re-check status on the payment date, not only on the nightly pull.
- Compare each charity's bank account against the register where the register publishes one. Pay only to that account, and hold payments for a fixed period (60 days or so) to allow reversal.
- Maintain a company exclusion list and a policy on what you will not fund, published before launch.
- Cross-check the charity's listed trustees and directors against your employee roster and bank details. Require employees to declare any role at a charity they donate to or volunteer with, and treat undeclared roles as a policy breach.
- Check whether the charity's bank account or address matches any employee's details, and flag matches.

**Receipts and evidence**
- Prefer direct platform APIs (including Givelark) to get transaction IDs, rather than accepting PDFs.
- For bank transfers, require a bank-side confirmation (the payee account and transaction reference), or ask the charity to confirm receipt of the donation directly.
- Deduplicate on transaction ID and on charity-plus-amount-plus-date across all employees and years.
- Reject donations dated outside the program year.

**Round-trip and refund detection**
- Ask charities to confirm each match they receive, and to report refunds, fees paid back to donors, or payments to any employee.
- Require the donation to come from the employee's own account. Run periodic checks that the donor's name matches the bank account used.
- Check annually whether any charity receiving matches made payments to employees, using AP data.

**The 3:1 kicker**
- Count "five donors" as five unrelated people. Use shared address, bank account, manager, device, or email domain to exclude linked donors.
- Set a minimum donation size for counting toward the five.
- Cap the kicker at a total monthly amount per charity, so a coordinated group cannot unlock unlimited uplift.
- Report kicker activity to your finance team monthly so unusual clusters show up.

**Volunteer grants**
- Require the charity contact email to be on the charity's own website or register entry. Better still, send the verification to that address yourself, rather than trusting what the employee typed.
- Require dated, per-event hour logs, and dedupe hours across employees attending the same event.
- Grant only to charities that have passed the same eligibility checks as the match program.
- Pay after approval with the same hold period as matches.

**Governance and monitoring**
- Separate duties: whoever edits the charity list must not approve payments. Keep an audit log of changes.
- Run a quarterly review of the top 20 recipients by amount and frequency, and check for concentration.
- Publish the rules, caps and pool status openly. Transparency reduces the damage from a headline, because the story becomes "the program worked as designed and we caught it".
- Set up a reporting route for employees to flag suspicious donations or charities, and keep a clawback clause in the charity terms.

## Assumptions to check
- Whether volunteer grants come from the $1.2M pool.
- Whether the cap counts by donation date, approval date, or payment date.
- What your national register publishes (trustees, bank details, registration date). Those fields determine how many of the controls above are possible.
- Whether any cooperating charity could be a registered "political" or advocacy body in your jurisdiction, which could have separate legal rules.

The three controls I would not launch without: (a) aggregated, cap-enforced approvals, (b) charity-side confirmation of receipts with a payment hold, and (c) a trustee and director cross-check against the employee roster.
