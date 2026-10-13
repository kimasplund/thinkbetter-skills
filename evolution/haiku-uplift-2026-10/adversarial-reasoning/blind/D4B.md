# Abuse review: Tolvane donation match relaunch

## Summary
- **Target**: the January 1 donation match and volunteer grant design, with a $1.2M annual budget.
- **Critical findings**:
  1. **The budget is not capped.** At the stated per-employee limits, theoretical exposure is about $19.0M in matches (3,800 × $5,000) plus up to $9.5M in volunteer grants (3,800 × $2,500). The $1.2M budget runs out after roughly 240 employees reach the match cap. This is the largest financial risk, and it needs no attacker at all.
  2. **Volunteer grants can be confirmed by the person claiming them.** The employee types in the charity contact's email, so they can enter an address they control.
  3. **Nothing verifies that money was actually given or that it reached the right account.** Receipts are checked as images, and payment details for each charity are not verified.
- **Recommendation**: Fix before launch. The intent is sound (registered charities only, no cash to employees), but the controls below need to be in place before January.

## Attack paths, ranked

### 1. Kickback loop with a cooperating charity (high)
An employee donates, say, $1,667 to a charity they are in league with. At 3:1 that produces the full $5,000 match, paid to the charity. The charity then returns the donor's money in cash, with a share of the match going to the employee. The company's money stays with a charity that nobody has checked is spending it on charitable work. The assumption that money "never goes to the employee" fails because the charity can pay them back indirectly.
- **Countermeasures**: Accept donations only where the transaction itself is verified (platform or bank data, see item 2). Review charities that receive many matched donations from employees who then show refunds or unusual inflows. Add a clawback clause for charities found to be returning donations. Audit the top recipients each year.

### 2. Fake or altered receipts (high)
OCR confirms the amount, date and name printed on an image. It does not confirm that a payment happened. Bank-transfer confirmations can be edited in any PDF tool, and online giving receipts can be recreated. The same real receipt can also be uploaded by several people or reused in later years.
- **Countermeasures**: Deduplicate on the platform transaction ID and the bank reference. Verify against the platform's data or the bank feed, not the uploaded image. Reject screenshots that lack a transaction ID. Where a charity issues sequential receipt numbers, check them against that sequence. Hold approval until reconciliation has run.

### 3. Boost gaming through collusion (high)
The 3:1 boost is triggered by a count of people (five employees), not by money. Five colluding staff can each give $1 to a charity of their choice and every one of them gets 3:1. The donors' own money is small, so the cost of steering the boost to a chosen charity is low, and it can be repeated every month.
- **Countermeasures**: Set a minimum donation amount before a donor counts toward the threshold. Count only distinct verified donors, excluding those who share a bank account, address or portal login. Cap the total boosted match per charity per month. Require review the first time a charity triggers the boost.

### 4. Volunteer grant fabrication (high)
The employee supplies the contact email, so a self-controlled address can confirm any hours. At 20 hours for $500 ($25 an hour), the grant is worth a lot for little effort. Up to $2,500 a year per charity can then be claimed, and several charities can be used.
- **Countermeasures**: Take the contact from the charity's entry in the national register, not from the employee. Send confirmation to a domain-matched address and require a charity-side confirmation, either through the charity's own login or a phone call to a number from the register. Block cases where the employee is also an officer or contact of the charity. Cap hours per charity per year, and compare claimed hours with calendar or badge data where available. Consider paying a lower rate per verified hour.

### 5. Payment redirection (medium-high)
The money goes "straight to the charity", so the question is which bank account it goes to. If the portal stores bank details that any user can edit, or if a dormant charity's details change, payments can be diverted to a fraudster.
- **Countermeasures**: Take bank details from the register or verify them by callback. Require dual approval for any change. Verify the first payment to any new payee by phone. Run a payment review before each quarterly payout.

### 6. Threshold splitting (medium)
HR reviews single matches over $2,000, which means a $1,000 donation at 2:1 or about $667 at 3:1. Employees can split a gift across several receipts or charities to stay under that line.
- **Countermeasures**: Apply the review threshold to each employee's total approved matches per month and per year, not to each match. Flag several donations to the same charity on the same day.

### 7. Year-end and cutoff gaming (medium)
The calendar-year cap and the calendar-month boost both depend on dates. Donations made on 31 December can be uploaded in January, receipts can be backdated, and time zones can move a donation across a month boundary.
- **Countermeasures**: Define the donation date as the transaction date from the source data. Set a receipt upload deadline (for example, 60 days after the donation). Do not approve backdated claims after the year closes.

### 8. Insider abuse (medium)
Program staff and HR reviewers can create accounts, change charity records and approve matches. A single person could do all three.
- **Countermeasures**: Separate duties so that no one can both create a charity record and approve a payment to it. Keep an audit log of approvals and data changes. Review access rights each quarter.

### 9. Reputational exposure from an eligible charity (medium, but high headline risk)
Every registered charity is eligible, so the company could end up matching money to a charity later exposed as fraudulent, extremist, or deregistered between the donation and payment. This is the risk the user is most concerned about.
- **Countermeasures**: Create a leadership-approved exclusion list with written criteria. Check the register status both at approval and at payment. Put a public FAQ and a short escalation process in place before launch. Review a charity the first time it receives a large donation.

## Budget exposure

| Item | Theoretical maximum | Notes |
|---|---|---|
| Matches | $19.0M | 3,800 employees × $5,000 cap |
| Volunteer grants | $9.5M | 3,800 employees × $2,500 cap |
| Stated budget | $1.2M | Exhausted by about 240 employees at the match cap |

- **Countermeasures**: Set a hard program cap and a per-charity monthly cap. Decide in advance what happens when the budget runs out (pro rata, first come, or pause). Keep a reserve for approved late receipts.

## Edge cases
- A charity merges or renames during the year, so the OCR name check fails or matches the wrong entity.
- A charity is deregistered between donation and payment.
- Donations in foreign currency, or bank confirmations in another language.
- Handwritten or faded receipts that OCR cannot read, which may fall into a manual path without the normal checks.
- An employee leaves in Q4 after donating. The design should say whether the match is still paid.
- Household members share one bank account, so they may be counted as separate donors or wrongly merged.
- A platform refund or chargeback arrives after the match has been paid.
- The annual cap is reached partway through a month, so the order in which matches are applied needs a rule.
- Volunteer hours that span the year-end boundary.

## Residual risk
- Collusion among five or more people remains possible at low cost. The thresholds make it harder but do not remove it.
- Any eligible charity can later become a reputational problem, however good its register entry looks. Only an exclusion policy and monitoring reduce this, and they cannot remove it.
- Volunteer hour inflation is reduced by verification but not eliminated, because the hours are self-reported.
- Manual HR review covers only a sample of matches, so some fraud will be approved automatically.

## Priorities before January 1
1. Hard budget caps for the program and for each charity.
2. Payee verification and dual approval for bank-detail changes.
3. Donation evidence verified against platform or bank data, with deduplication.
4. Volunteer contacts taken from the register and confirmed independently.
5. Review thresholds applied to totals, and safeguards on the boost.

## Confidence: 70%
- Based only on the description. I have not seen the portal, the payment process, the register fields, the HR review workflow or the volunteer confirmation process.
- Assumed: payments are made by bank transfer from a company account, the portal stores each charity's bank details, and there is no existing fraud or audit team in the program.
