Your instinct that money never reaches the employee is the weakest assumption in the design. Money can come back to people through the charity, and the "every registered charity is eligible" rule is also your biggest headline risk. Below are the attacks I'd expect, ranked, then the controls. I've assumed the match is paid from a fixed $1.2M pool and that "registered" means only that the charity appears on the national register.

## Ranked attacks

**1. The budget is not actually capped (certain, not an attack).**
3,800 employees x $5,000 is up to $19M of possible matches against a $1.2M budget. You hit the pool with only 240 employees maxing out. Because payment happens the quarter after approval, you could find out in Q2 that you have committed far more than you can pay. Nothing in the design says what happens then (first come, first served, pro-rating, or an overrun). Whatever you choose, an exhausted pool in March will be a story of its own, and it also rewards the people who rush in on January 2.

**2. Employee-controlled or friendly charity (the money does go back to a person).**
A registered charity can be a family foundation, a small community group, or a charity where the employee, a relative or a friend is a trustee or paid officer. The employee gives $1,667, the company adds $5,000 at 3:1, and the charity pays something back: salary, "expenses", a grant, tuition, event tickets, or a kickback to the donor. Net gain to the group is large and the trail looks clean. Registered status proves the charity exists. It says nothing about who benefits.
- Variants: donations that buy something (gala tickets, auction items, school fees, a membership with benefits), and charities that quietly refund the donation after the match is paid.

**3. The 3:1 ring.**
The five-donor trigger is cheap to hit. Five colleagues (or one person plus four friends, or a group chat) each give to the same charity in the same month. Each match rises from 2:1 to 3:1, so the incentive to coordinate is built in, and anyone who learns the rule can organise it. Combined with attack 2, five people donating about $8,300 in total can pull $25,000 in matches into a charity they control. Combined with a controversial charity, it is a mechanism for an organised internal campaign.
- Also check for the reverse: one person using five accounts or five family members' receipts.

**4. Forged or reusable receipts.**
OCR confirms that an amount, a date and a name appear on an image. It doesn't confirm that money moved. Anyone can edit a PDF, and a bank-transfer confirmation is the easiest document in the world to fake. Givelark-style platform receipts are trivial to recreate. Expect:
- fabricated receipts for donations that never happened (the match is paid to the real charity, so the employee only gains if they have a link to it as in attack 2, or if it is part of a ring);
- the same receipt submitted twice, or by a spouse and an employee;
- real donations that are later refunded or charged back, after the match is approved;
- old receipts from prior years or from a different currency.

**5. Threshold dodging on the $2,000 review.**
The review is triggered by a single match over $2,000. At 2:1 that is a $1,000 donation, at 3:1 about $667. Splitting into several $999 or $666 donations, over several days or charities, means nothing gets human eyes, and everything under the line is automatically approved. Your whole fraud defence for matched gifts is the OCR check plus this one threshold.

**6. Volunteer grants with a self-chosen verifier.**
The employee types in the email of the person who confirms their hours. That person can be a friend, a relative, a second email address the employee controls, or a lookalike domain. No hours are reviewed, and there is no cap beyond $2,500 a year, which is unclear: per employee, per charity or per charity overall? If it's per charity per employee, 3,800 people could generate a very large bill. Hours also aren't checked against working hours (someone "volunteering" 20 hours in a week they were also billing).

**7. Headline risk: a legal charity you would not want to be seen funding.**
"Every registered charity" includes advocacy groups on either side of political and social fights, charities under regulator investigation, controversial religious or ideological groups, groups with questionable fundraising, and charities connected to your executives or major clients. With the 3:1 trigger, a handful of employees could steer six figures to a group that a journalist or an employee on social media will find offensive. The register also lags: a charity being investigated or struck off might still be in your nightly pull. Nobody has to cheat for this one to go wrong.

**8. Lookalike and changed-payment-details charities.**
OCR matches the charity name from the receipt. A lookalike name ("Red Cross Relief Foundation" vs the real one), a name that changed, or a charity whose bank details were swapped between approval and payment (the payment is a quarter later) makes the payment itself a target. Business email compromise aimed at whoever handles charity payments is a real, low-tech route.

**9. Insider and process weaknesses.**
Whoever in HR or finance can approve, edit the eligible-charity list, or run payments can approve their own charity or friends' receipts. There is no separation between people who approve claims and those who release payments, and no log of who changed what. Departing employees raise a smaller question: do pending matches survive when someone leaves?

**10. Smaller edge cases to settle in policy.**
Year boundaries (December giving matched in January, or the monthly 3:1 count straddling month-end); donations made in other currencies or to foreign charities; donations made on a company card or paid by the company; donations by managers on behalf of subordinates; and what happens when a charity refuses the money.

## Controls I'd add, in priority order

**Before launch (these close the biggest gaps):**
1. **Hard budget controls.** Set a program-wide cap and a clear rule for when it runs out. Add a per-charity cap (for example, no more than 5 to 10% of the pool to any one charity) and a lower per-employee limit, such as $2,500 in year one. Report committed vs. paid spend weekly. Decide now whether the 3:1 rate is paid only while the budget is under a set percentage used.
2. **Eligibility screening beyond "is on the register".** Use an allow-list approach or an exclusion list: charity must be in good standing, registered for at least a year or two, have filed accounts, and not be under regulator action. Add a short review for any new charity that crosses a set amount (say $10,000 in matches). Re-check status at payment time, not just nightly. Publish a short eligibility policy and an exclusion list so you can point to a rule when someone asks why a group was or was not funded. A legal, non-partisan, non-discriminatory test is easier to defend than ad hoc decisions. Ask your legal team and communications lead to agree it.
3. **Conflict-of-interest declaration.** At each claim, the employee confirms that neither they nor a relative is a trustee, officer, employee or paid contractor of the charity, and that they received nothing of value in return (or state its value; match only the net amount). Make a false declaration a disciplinary matter. Cross-check against a short list of charities where staff are known to be trustees.
4. **Change the review threshold.** Review by aggregate, not by single match: total matched to one charity per quarter, total per employee, and any charity new to the program. Randomly sample 5 to 10% of auto-approved claims in addition to the threshold, and make the sample not predictable.
5. **Remove or redesign the 3:1 booster.** The simplest fix is to drop it. If you want to keep it as a feature, require donors from different departments/managers, ask for a minimum total from a minimum number of distinct donors, count only the donors who passed review, cap the extra match per charity per month, and compute the rate after the month closes, not live. Don't publish the exact trigger in a way that makes it easy to organise.

**Verification and payment:**
6. **Prove the donation happened.** Prefer a direct feed or a verified confirmation from the platform (ask Givelark and similar platforms whether they offer a confirmation API or can send receipts directly) over uploaded images. For bank transfers, require a statement line with the payee account, and check the payee account matches the charity's registered details. Detect duplicate receipt IDs and image hashes across all employees, not just per employee. Pay the match only after a holding period (30 to 60 days) to let refunds and chargebacks happen, and add a clause allowing clawback from the charity.
7. **Pay safely.** Pay only to bank details taken from the register or verified once with the charity by a call-back, never from the receipt or an email. Require a second person to approve any change in details. Keep claim approval and payment release with different people, and log every edit to the charity list and approval.
8. **Volunteer grants.** Have the charity confirm hours through a verified channel: a charity-side form or a one-time link sent to an address on the charity's own domain, taken from the register or the charity's website rather than typed by the employee. Reject free-mail addresses and the employee's own domain. Define the cap clearly (per employee, per charity, program-wide) and test the maximum exposure. Sample-check hours against the employee's work calendar.

**Detection (cheap and effective):**
9. Run monthly analytics and review the output: new charities with sudden spikes; many small donors giving the same amount at the same time; donors sharing an address, phone, manager or bank details; charities with a thin public footprint; claims submitted just below $2,000; lots of claims at month-end; and receipts that reuse formatting.
10. Add an easy channel for staff to report a suspicious charity or claim, and a clear statement that the program may investigate and recover funds.

**For the headline risk specifically:**
11. Write the one-page "who we will and won't match" policy, name the person who can pause a charity, and prepare a holding statement. Add a right in the terms to withhold, delay or recover a match from any charity for reputational or legal reasons. Use a short pause (a few days) to check any charity that gets an unusual number of claims in a week.

## What I'd do first
If you only have time for four things before January 1: the program-wide and per-charity caps (1), the eligibility and exclusion policy (2), the conflict declaration plus a holding period before payment (3 and 6), and either dropping the 3:1 booster or restricting it (5). The rest can follow in the first quarter, which suits you because payments don't go out until the quarter after approval. That delay is useful: it is your window to check, sample and claw back before any money leaves.

One assumption to confirm: I took the per-employee cap of $5,000 as applying to matches in total, so I'd also check how volunteer grants (which are paid to the charity, not matched against employee donations) count toward the $1.2M. If they are separate, the realistic total exposure is higher than the number you've been given.
