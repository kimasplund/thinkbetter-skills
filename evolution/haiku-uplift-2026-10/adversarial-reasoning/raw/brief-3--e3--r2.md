Here is how I would attack the relaunch, starting with the attacks most likely to end up in a headline, then the controls I would add. I've assumed the register lookup is a live national register with no manual vetting, that "employee" means anyone on the 3,800-person payroll, and that the volunteer grant has no separate HR review. Tell me if any of that is wrong, because it changes the ranking.

**1. Your "money never reaches the employee" assumption is weaker than it looks.**
A donation can be routed back to the donor. An employee gives $1,000 to a charity they, a relative or a friend control. That charity returns $900 as a "consulting fee", "expense refund" or "event payment". The employee nets $900 out, has spent $100, and has collected a $2,000 match. The money did go to a registered charity at the start, which is exactly why the headline would be so bad.
- Control: require that the donor is not an officer, trustee, employee or paid contractor of the charity, and collect a declaration. Cross-check employee names against the charity's published trustee and officer lists.
- Control: flag any charity that receives repeated donations from one employee, or from a small group of employees, and then pays money to any of them.

**2. Receipts are the weakest link.**
OCR confirms what is printed on the receipt, not that money moved. A bank-transfer confirmation is an ordinary PDF or screenshot that is easy to edit. Givelark receipts are easy to imitate. Duplicates are also likely: the same receipt filed by two people, or by one person in two months.
- Control: match every receipt to a transaction ID, and verify it directly with the charity or the platform (API or confirmation email to a known address) before paying.
- Control: deduplicate on transaction ID, bank reference and charity plus amount plus date, across all employees and years.
- Control: for bank transfers, check the statement line against the account, not the uploaded image.

**3. Splitting avoids HR review.**
HR reviews a single match over $2,000. A $1,000 donation earns a $2,000 match, which is exactly at the line, and an employee can split a larger gift into several smaller receipts that each stay under the threshold. Each one is then auto-approved.
- Control: apply the review threshold to the total matched per employee per charity per month, not per receipt.

**4. The five-donor rule can be gamed by a ring.**
Five colleagues, or friends who are colleagues, can each give a small amount to a charity the group controls. Everyone's match rises to 3:1 and the cap is the only limit. Because the 3:1 rate applies to all five matches, this is the most efficient way to move company money, and it is easy to coordinate.
- Control: count only donors who have no link to the charity (see point 1), require a minimum donation size before the bonus applies, and review any charity whose donor count jumps suddenly.
- Control: pay the bonus in the quarter after a monthly review, not immediately, so a ring that disbands can be caught.

**5. Volunteer grants are the most open door.**
The employee types in the contact's email address, so an employee can enter their own address, or one they control, and confirm any number of hours. There is no stated limit on the number of charities, so one employee can open several "volunteer" relationships, each earning up to $2,500 a year. This is the least-reviewed part of the scheme and the one most likely to be discovered by a journalist searching for the charity name.
- Control: the contact email must match the charity's domain or the contact on the national register. Send a confirmation to that address and require a reply.
- Control: limit each employee to a fixed number of charities per year, and require the charity to submit its hour confirmations directly, not through the employee.
- Control: route all grants through the same HR review as matches.

**6. Payment redirection and lookalike charities.**
Matches are paid straight to charities, so someone who can change a charity's bank details (or register a near-identical name) can redirect a payment. The nightly register pull also means a charity that was deregistered after approval may still get paid.
- Control: verify bank details by callback to a number already held on file, not from the portal. Hold payment for 14 days after any change.
- Control: check the register status again on the payment date, and flag names that are one or two letters away from an existing charity.

**7. Budget exposure is larger than the cap suggests.**
At 2:1 each employee can earn $5,000 of match, which needs a $2,500 donation. At 3:1 the same cap is reached with about $1,667. A few hundred employees hitting the cap would exhaust the $1.2M in the first months, leaving the scheme unfunded for the rest of the year and creating a second headline ("budget gone by March").
- Control: a monthly spend ceiling, with a published rule for what happens when it is reached.

**Summary of the controls I would add before launch, in priority order:**
1. Verify each receipt directly with the charity or platform, and match it to a bank line.
2. Apply the HR review and the donor-count rules to aggregates per employee per charity, not per receipt.
3. Require a conflict-of-interest declaration and cross-check against charity officer lists.
4. Verify volunteer contacts on the charity's domain or register entry, and cap charities per employee per year.
5. Lock charity bank details behind a callback check and a waiting period.
6. Set a monthly spend ceiling and a published overflow rule.
7. Pilot in one region for a quarter, with a dashboard for clustering and duplicate alerts.

**What remains after these controls:** A determined, well-coordinated group of insiders who are willing to hold money in a charity they own for a while could still extract value, and the scheme cannot fully prevent that. The best protection against the headline is detection plus a public, written rule set that shows you looked for these abuses before launch.
