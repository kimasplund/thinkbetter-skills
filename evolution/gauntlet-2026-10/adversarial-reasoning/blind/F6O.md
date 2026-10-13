Short version: "money only goes to registered charities" is the weakest assumption in the design. Registration proves a legal entity exists. It says nothing about who controls it, what it does, or whether the donor is connected to it. Below are the attacks I'd expect, roughly in order of how likely and how damaging they are, then the controls.

Assumptions: the $1.2M is the hard annual cap, matches are paid by Tolvane, and "registered" means on the national register as active. I haven't seen your portal, so check each point against how it actually works.

## Where a smart person would attack

**1. Self-dealing through a charity the employee controls (the main pocketing route, despite your assumption)**
- Anyone can register a small charity: a family foundation, a "community fund", a relative's association. The employee donates $2,500 and gets $5,000 in match, so $7,500 lands in an entity they or their family control. It can then pay salaries, rent or "expenses" to them.
- Related versions: donating to a charity where the employee, a spouse or a relative is a paid officer, or to a school or club that benefits their own child.
- The 2:1 ratio is the incentive. A third of the money moving is the company's.

**2. Coordinated 3:1 farming**
- The five-donor threshold is trivially gamed. Five colleagues, or one person with a few friends, each give $10 to the same charity in the same month and every match rises to 3:1. Five people can be recruited in a group chat.
- Worse, it can be used to steer the budget. A campaign inside the company ("everyone give $50 to X in March") routes a lot of corporate money to one cause, which is how a controversial organisation ends up with a six-figure Tolvane cheque.
- Look also at timing: donations clustered at month end or in the first days of a month so the threshold is hit with the minimum effort.

**3. Embarrassing recipients, which is your actual headline risk**
- "Every registered charity is eligible" includes organisations that are legal but toxic: political advocacy groups, hate-adjacent or extremist-linked groups, groups under regulator investigation, charities with a record of fraud, religious bodies that run contentious programs, and charities sanctioned or linked to sanctioned entities.
- A nightly register pull also means a charity can be eligible on the day of payment even if it was suspended, under inquiry or deregistered between receipt approval and the payout a quarter later.
- Mismatched names: a lookalike charity name ("Red Cross Foundation" vs the real one) that OCR name-matching passes.
- A cluster of ten staff all matching to the same single cause will be noticed by a journalist before it is noticed by you.

**4. Receipt fraud and "donations" that never happened**
- OCR checks that the text on a receipt looks right. It doesn't check that the money moved. Edited PDFs, screenshots, recycled receipts, and AI-generated receipts all pass this kind of check.
- The same receipt can be uploaded twice, by the same person or by two colleagues, or once this year and once next.
- Bank-transfer confirmations are especially weak. They're easy to edit, and the payee name can be anything the employee typed.
- Refunds and reversals: donate, get the match approved, then reclaim the gift (platforms and banks allow chargebacks). The company's match stays paid.
- Third-party platforms such as Givelark: a donor can be using the platform's "donate on behalf" or gift-card features, or donating to a platform-hosted fundraising page run by an individual rather than to the charity itself. Check what the receipt really shows as the recipient.

**5. Donating someone else's money, or round-tripping**
- A charity or a friend refunds the donation to the employee afterwards, or the employee is reimbursed in a "thank you" arrangement. The match is the profit.
- Donating with company expenses or a company card, or a vendor or customer paying staff to donate to their favourite cause (a soft bribery route that would be a real compliance problem).
- Pooling: one person funds donations in several employees' names to use up many people's caps at 3:1.

**6. Splitting to beat the manual review**
- The $2,000 review threshold applies to a single match. At 2:1, any donation under $1,000 is never reviewed, and at 3:1 the limit is about $667. Someone can submit many small receipts to the same charity and stay entirely in auto-approval.
- With 3,800 staff and a $5,000 cap, theoretical maximum exposure is far above $1.2M ($19M). The budget only holds if take-up is low, so the real issue is what happens when the money runs out: first come, first served creates a rush, a fairness complaint and an incentive to claim early and large.

**7. Volunteer grants are the softest part**
- Hours are confirmed by an email address the employee supplies. They can supply their own second address or a friend's. There's no independent check that the "contact" works at the charity at all.
- A charity they control can confirm 100 hours and receive $2,500 a year from Tolvane per employee with no donation required. Ten staff volunteering "with" the same family charity is $25,000 a year.
- Hours can be claimed during working time, or double counted if the company also pays for paid volunteer days.
- The grant is paid to the charity, with no cap per charity.

**8. Data, privacy and process issues**
- Receipts contain personal data (name, address, sometimes card or account details). Storing them is a data-protection liability.
- Reporting who gave to which cause reveals religious, political or health information about named staff. Be careful what HR and managers can see.
- Employees may feel pressure to give, especially when 3:1 depends on five donors, which raises a coercion risk when managers organise it.

## Controls I'd add (highest value first)

**Eligibility**
1. Move from "all registered charities" to an eligibility policy. Exclusions: charities that are political or campaigning bodies, have fewer than, say, two years of filed accounts, fall below an income threshold, are under regulator inquiry, or are on sanctions or terrorist watchlists. Add a list of excluded categories reviewed by a small committee (HR, legal, comms).
2. Re-check eligibility on the payout date, not just at approval. Hold payment if status has changed.
3. Add a conflict-of-interest declaration at submission: "I, my family or a close associate are not an officer, employee, trustee or paid supplier of this charity." Make it a signed attestation, with disciplinary consequences if false. Cross-check against register officer data where the register publishes it, and against Tolvane's own declared-interests records.
4. Add an exception route: any charity not in a pre-approved list goes through a quick manual look the first time it is claimed, and the outcome is saved for next time.

**Matching rules**
5. Replace the 3:1 trigger. The simplest fix is to remove it. If you want a campaign mechanic, make it a program HR designates: a named charity, a named period, a total cap for it, and no automatic trigger. This removes the group-chat gaming and the headline of an accidental windfall.
6. Add a per-charity cap, e.g. no more than 5% of the annual budget or $50,000 to any single charity, plus a per-donor minimum (to avoid $10 gaming) and a per-charity cap per employee.
7. Set a firm program-level budget control: monthly or quarterly allocations, and a clear rule for what happens when the budget is exhausted. Decide it now. Don't discover it in November.

**Receipt verification**
8. Prefer verified sources. Accept platform receipts only through a direct feed or a verifiable link or reference ID that you can check with the platform, and restrict bank transfers to cases where the payee account matches the charity's published details. Treat screenshots as low trust and send them to review.
9. Deduplicate: hash the receipt and compare transaction ID, amount, date and charity across all employees and years.
10. Add clawback language to the terms: the match is repayable (or deductible from future matches) if the donation is refunded, reversed or found false. Reconcile for reversals before paying, which the quarterly delay already helps with.
11. Check the platform's recipient. Make sure the funds go to the charity itself rather than to an individual's page, and decline gift-card style donations.

**Review thresholds**
12. Review by aggregate, not by single match. Trigger manual review on total per employee per charity, per charity per month, first-time charities, or any employee above, say, 50% of their cap. Keep random sampling (e.g. 5% of auto-approvals) so splitting isn't risk-free.
13. Add simple analytics run monthly: concentration by charity, a sudden jump in new charities, clusters of employees claiming the same charity from the same team or manager, repeated round amounts, and charities with an employee-related address, phone or bank detail.

**Volunteer grants**
14. Verify the contact independently: confirm the email domain matches the charity's published website, send the confirmation from a system link rather than relying on the employee-entered address, and don't allow the contact to share a surname, address or domain with the employee without review.
15. Cap per charity per year, restrict the grant to charities that pass the same eligibility screen, and require the charity to confirm hours with a short attestation (name, role, dates).
16. Spot-check a sample each quarter by phone.

**Governance and response**
17. Publish simple program terms: eligibility, conflicts, clawback, right to refuse any match, and the right to publish aggregate data. Employees agree on submission.
18. Name an owner for escalation. Have a short, pre-written response plan for the case where a recipient becomes a news story: who decides whether to pause payments, who talks to the press, and how you pause a charity quickly without penalising the other staff who gave in good faith.
19. Lock down the data: limit access to receipts, report only aggregate giving by cause to managers, and set a retention period.
20. Pilot for the first quarter with a lower cap, review the analytics, then widen it.

## If you only do five things

1. Drop or redesign the automatic 3:1 trigger.
2. Add an eligibility policy and a conflict-of-interest attestation, and re-check the charity's status at payout.
3. Add a per-charity cap and aggregate-based manual review in place of the $2,000 single-match rule.
4. Verify receipts at source and deduplicate, with clawback terms.
5. Fix volunteer-hour confirmation, since it needs no money from the employee and so is the cheapest thing to abuse.

I'd also test the design before launch by asking a colleague from internal audit to spend an afternoon trying to get a bad match approved. They'll find things that neither of us has listed here.
