Short version: "money only goes to registered charities" is the weakest assumption in the design. Registration proves a charity exists, not that it is arm's-length from the employee, and several rules here can be gamed to extract value or embarrassment. Here are the attacks I'd expect, roughly by severity, with controls.

## Assumptions
- The $5,000 cap is on matches (so up to $2,500 of employee giving at 2:1, or about $1,667 at 3:1).
- Worst-case exposure: 3,800 x $5,000 = $19M against a $1.2M budget, so budget exhaustion is itself a risk.
- "Registered" means on the national register, with no further screening.

## 1. Pocketing the money indirectly (the "never to the employee" assumption)
- **Related-party charities.** An employee (or a relative) starts a tiny registered charity, or sits on its board, pays themselves salary, rent or "consulting" from it. Every match funds that. Cheap to set up, hard to see.
- **Charities with private benefit.** Donor-advised funds, school or club foundations (your child's school, a hunt club, a private golf-course trust), religious or membership bodies where the donor gets tickets, tuition offsets, naming rights or a gala seat. The match is effectively a subsidy of personal spending.
- **Round-tripping.** A friendly charity returns funds to the donor via a refund, "program grant" or a reimbursed expense.
- Controls: a conflict-of-interest declaration on each submission (board, officer, family, paid relationship); exclude donor-advised funds, private foundations and charities with an employee-linked officer unless approved; exclude donations with a received benefit (require the receipt to show the net-of-benefit amount); a new-charity cooling period (e.g. registered 12+ months, minimum filed annual return, minimum revenue); flag charities whose match receipts are dominated by Tolvane.

## 2. The 3:1 five-donor rule is a coordination exploit
- Five people agree to hit one charity in a month; the multiplier rises on everyone. With 3,800 staff, a group of friends can steer a captured or related charity into 3:1 trivially, or a single person can recruit four colluding or fake accounts.
- It also rewards the mundane: one viral campaign creates a spike and a budget cliff.
- Controls: the threshold must be a share of distinct, unrelated donors, not a count of five; drop the multiplier or cap it per charity per month (e.g. $25k of total matches); require donors to be in different departments/managers or not share a household; make 3:1 apply only to pre-approved campaigns; delay the bonus until the month-end reconciliation so it cannot be seen and gamed in real time.

## 3. Receipts and OCR
- OCR checks amount, date and charity name, which are exactly the fields a forger edits. Editing a PDF, reusing one receipt across years or employees, or screenshotting a small gift and inflating the number all pass.
- Bank-transfer confirmations are the weakest evidence: they show a payment to an account, not that the account belongs to that charity or that it was a gift. An employee can send money to themselves or a relative's account with a charity name in the reference field.
- Givelark-style platforms: fake or lookalike "platform" receipts, and platforms that charge fees or route to non-charities.
- Pledges, refunded donations, recurring gifts later cancelled, and chargebacks all leave a paid match with no real donation behind it.
- Controls: duplicate detection (hash, amount+date+charity+employee, across employees); accept only from an allow-list of platforms, ideally via API or verified email forwarding rather than uploads; for bank transfers, require the charity's published account details to match the payee; hold the match until after the refund/chargeback window; claw back on refund; sample-audit a random percentage (including auto-approved ones) with a penalty policy so the audit has teeth; metadata checks on PDFs.

## 4. Splitting around the $2,000 manual-review threshold
- Auto-approval below $2,000 per match means an employee files several $1,900 matches (or many small receipts) to the same or related charities and never reaches a human. At $5,000 per head, two or three splits get nearly all the way through.
- Controls: review on a cumulative basis (per employee per charity per period, and per charity across employees), not per match; add risk-triggered review (new charity, charity with related parties, unusual frequency, round amounts, donation made on the last day of the quarter); a charity-level cap.

## 5. "Every registered charity is eligible" — the headline risk
- The nightly register pull is a feature that makes a headline: the match could fund an extremist or hate-linked group, a controversial political or advocacy body, a charity under investigation or with revoked/suspended status, a sanctioned or terrorist-financing-linked organisation, or a charity with disputed use of funds. Also a charity whose status changed between donation and payment, which can be up to a quarter later.
- Employees can also simply pick causes the company would not want its name on; the logo goes on the cheque.
- Controls: an eligibility policy that is stricter than "registered" (exclude political, lobbying, religious proselytising if that is your policy, and so on); sanctions and watch-list screening; re-check status immediately before payment; a pending-review bucket for anything with adverse media or a regulator action; a published exclusion list and a fast-removal process; an appeal path so exclusions are not arbitrary; a communications holding statement ready in advance.

## 6. Volunteer grants
- Confirmation comes from a contact whose email the employee enters. That is self-attested: the employee can enter a friend's, a second address of their own, or a spoofed domain. Hours can be inflated, and 20 hours at 25 hours of "volunteering" per year is cheap to fake.
- Related-party risk again: volunteering with your own charity pays that charity $500 repeatedly. Up to $2,500 per employee, so 3,800 staff x $2,500 = $9.5M of potential exposure, nearly eight times the whole budget.
- Controls: confirmation by a verified channel (email from the charity's domain as listed in the register, or a one-time link sent to a contact looked up independently, not typed by the employee); confirmer cannot share an email domain with the employee or be a relative; spot-check calls; per-charity annual cap on volunteer grants; require a manager attestation if the activity was in work time (otherwise you may be paying for paid volunteer time twice).

## 7. Budget and timing
- With no program-level cap, 3:1 boosts, volunteer grants and heavy early claims can exhaust $1.2M early in the year. Late joiners then get nothing, which is a fairness story of its own. Matches paid next quarter make forecasting harder and allow charity changes in the gap.
- Controls: monthly budget pacing and a hard stop with a published waitlist rule; real-time commitment tracking; reserve a contingency; reduced match ratios once 70-80% is committed; a lower per-employee cap in the first year (e.g. $2,500) and then raise it.

## 8. Privacy, tax and legal
- The portal holds who gave to which cause, which can reveal religion, health or politics. Restrict access and retain it for as short a time as needed.
- Check the tax treatment of the match, whether it is a donation by the company or a benefit to the employee, and whether your jurisdiction restricts corporate gifts to political or sanctioned organisations. This is worth a legal read before launch.

## What I'd do first (priority order)
1. Replace "any registered charity" with a rule set: related-party declaration, exclusion categories, minimum age and filings, and a pre-payment status and sanctions re-check.
2. Redo the 3:1 rule as a capped, distinct-donor, campaign-based bonus (or drop it for year one).
3. Move review from per-match to cumulative/risk-based and add random audit of auto-approvals.
4. Tighten evidence: platform allow-list, bank-transfer payee check, duplicate detection, clawback after refund window.
5. Fix volunteer verification and cap per charity.
6. Add budget pacing and a hard stop.
7. Prepare a one-page incident playbook: who decides, how to pause the program, how you pay out or reverse, and what you say publicly.

A cheap way to test all this before launch: run a one-hour red-team session where finance and two employees each try to get a $1,000+ match to a charity they control or an unsuitable one, using only the portal as designed. Whatever gets through is your first fix list.
