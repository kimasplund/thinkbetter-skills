# Where this match program is weakest, and what to add

**Short version:** "The money never reaches the employee" is the assumption I'd challenge first. Money can reach the employee's family, friends or business through a charity they control. The 3:1 rule and the volunteer grants are the easiest places to push this program. Ship it only with the controls under "Before January 1". The design is not safe as it stands.

## Why "it only goes to charities" doesn't protect you

Every registered charity is eligible, and registering one is cheap. Someone smart will use that.

**1. The round trip through a charity they control (highest risk).**
- An employee, or a relative, runs a small registered charity. The employee donates $1,667. At 3:1 that draws the full $5,000 match.
- The charity then pays a salary, consulting fees, rent or a "program" contract back to the family. Net result: $1,667 in, $6,667 to a vehicle they control.
- A looser version needs no relative. A friendly charity returns part of the gift, or gives the donor a gala ticket, a dinner or a child's tuition-style benefit. Matched gifts for goods or services are a known abuse.
- Scale: $1.2M is exhausted by 240 people maxing out. Two or three dozen colluding employees could take a visible share of the pool.
- The register tells you a charity is registered. It does not tell you who runs it or whether it does anything.

**2. The 3:1 trigger is a coordination prize.**
- Five employees giving to one charity in a month raises everyone's rate. Five friends, or five people with a shared interest, can set this off at will. It also invites one person to recruit four others.
- Cheap abuse: a person with a small charity of their own gets four colleagues to each give $50 for a month. The match rises from 2:1 to 3:1 and the charity is paid.
- Headline risk: an advocacy group organizes a campaign among your staff to push a polarizing or fringe cause over the threshold. The story becomes "Tolvane gave $X to [controversial group] at premium rates".
- Add that an employee can split a gift across five "donors": family accounts and friends can be used to reach the five.

**3. Receipts are weak evidence.**
- OCR confirms that text on a document looks right. It does not confirm that money moved. Anyone can now make a convincing receipt with an image editor or generative tools.
- Bank-transfer confirmations are the weakest accepted proof. They are screenshots or PDFs the employee supplies, with no one verifying the other end.
- A single genuine receipt can be reused, by the same employee in another month or by a colleague who edits the name.
- Platform gifts can be refunded or charged back after you approve the match. Your match is paid, the donor's money returns, and the charity keeps both.
- Gifts can also be funneled through a donor-advised fund or platform that hides who the real recipient is.

**4. Splitting beats the manual review.**
- Only a single match over $2,000 gets human eyes. At 2:1 that is any donation up to $1,000, and at 3:1 any donation up to about $666. Anyone who reads the policy can split gifts below the line. The $5,000 cap can therefore be taken with every item auto-approved.
- The review trigger looks at one item at a time. It does not look at the pattern: totals by employee, by charity, by month.

**5. Volunteer grants are the softest part.**
- The confirming contact is an email address the employee types in. Nothing stops it being their own second address, a spouse, or a friend at the charity. A fake sign-off needs no technical skill.
- $500 per 20 hours is a payout for a claim nobody observes. It is also an easy way to reward a connected charity.
- It is unclear whether the $2,500 cap is per employee or per charity, and whether it sits inside the $1.2M. If it is per employee and outside the budget, the worst case is 3,800 x $2,500 = $9.5M. Decide this now.
- Volunteer hours done on company time, or hours already counted toward another employer, school or court-ordered requirement, can be claimed twice.

**6. Eligibility through a nightly register pull creates embarrassing gaps.**
- A charity can be revoked, suspended, under investigation or sanctioned after the last pull. Payment happens a quarter after approval, so the status you checked may not be the status when you pay.
- Lookalike names ("Red Cross Relief Fund" against the real organization) pass an OCR name check, so a match could go to the wrong entity.
- "Registered" includes legitimate-but-contentious causes: political lobbying, hate-adjacent groups, fringe religious bodies, charities with sham fundraising. You have no content rule, so you are implicitly endorsing all of them.
- Payment details are the other risk. If bank details can be changed or come from the employee's claim rather than the register, someone can redirect a quarterly payment. This is ordinary payment fraud, and it needs a call-back check.

**7. Conflicts of interest for an engineering firm.**
- A donation to a charity favored by a client, regulator, procurement officer or public official can look like a bribe with company money added. The match makes it your money.
- Senior staff or HR/program administrators can steer matches to charities they sit on the board of. The administrators approving batches are themselves an insider risk.

**8. Budget and timing.**
- Maximum exposure is 3,800 x $5,000 = $19M against a $1.2M budget. If it is first come, first served, the budget could be gone early in the year, and late joiners hear "sorry". That is a reputational problem as well as a financial one.
- Receipts from late December with early January processing dates will double-dip across years unless the date rule is firm. Define which date counts: gift date or approval date.
- The payout lag leaves the company holding a liability it has promised but not yet paid.

## Controls, in order of value

**Before January 1**
1. **Replace "every registered charity" with an eligibility screen.** The register is the starting list. Add: minimum age and filing history (for example, at least two years of filed accounts), a minimum share of spending on program rather than on insiders, and no related party. Flag for review any charity first appearing in your portal.
2. **Require a conflict declaration on every gift.** The employee declares that neither they, a relative, nor a business partner is an officer, trustee, employee or contractor of the charity. Staff need to know a false declaration is a disciplinary matter. This is the single most effective deterrent for the round-trip.
3. **Check the other end of the receipt.** Accept platform gifts through a direct integration or a verification link (Givelark and similar). For bank transfers, require the charity's own acknowledgement, which you verify against contacts from the register, not from the employee.
4. **Cap the whole picture, not the item.** Review on the total per employee, per charity, per quarter. A tripwire of $2,000 aggregate per charity per employee, or a count of more than three receipts to the same charity in a month, goes to a person.
5. **Remove or rebuild the 3:1 tier.** The simplest fix is to drop it. If you keep it, use a published, company-chosen list of campaign charities for a given month instead of a self-triggering threshold. If the threshold stays, count only distinct people with no shared household or manager chain, and cap the premium per charity per year.
6. **Set a per-charity annual ceiling** (for example, no charity receives more than 1% to 2% of the pool, or a fixed dollar amount). This limits any one vehicle, whether fraudulent or just controversial.
7. **Fix the volunteer grant.** Verify the contact through the charity's registered address or phone, not the one the employee gives. Use a charity-issued confirmation, not an email reply. Cap per charity as well as per employee, and put the program inside the budget with a stated limit.
8. **Pay safely.** Pay to bank details taken from the register or a verified onboarding step, never from the employee's claim. Re-check registration status on the payment day. Call back to confirm any bank detail change.
9. **Add a content policy.** A short exclusion list (political parties and campaigns, groups designated or sanctioned by government, groups the company decides it will not fund) written down before launch. Without it, you will be making the decision under press pressure.
10. **Budget controls.** Allocate by quarter, publish a waitlist rule, and decide the cross-year date rule.

**After launch**
- Monthly report to finance and legal showing the top charities by dollars, new charities, charities with several donors clustered in the same month, and employees at or close to the cap.
- Spot-check 5% to 10% of auto-approved receipts against the source each quarter, selected at random. Publicizing that checks happen deters more than catching.
- Hold payments for 30 days after approval, long enough for most refunds and chargebacks. Claw back matches on refunded gifts, and say so in the terms.
- Give employees and charities a simple route to report suspected abuse, and name the person who decides. Reserve the right to withhold, recover and discipline.
- Put gifts to charities connected to clients, officials or regulators through a compliance check.

## What I'd tell finance

- The most likely loss is not a dramatic fraud. It is a modest number of people drawing the cap through charities they are close to, and a polarizing campaign hitting the 3:1 threshold. Both are cheap to run and hard to explain afterwards.
- With the eligibility screen, the conflict declaration, third-party receipt verification and the 3:1 change, most of the realistic abuse is closed. Volunteer grants are the next most important fix, because as drafted they pay out on a claim nobody checks.
- Residual risk after these controls: a determined person with a clean-looking third-party charity and an arm's-length relationship will still get through occasionally. Aggregate reporting and clawback terms are there so you notice it and can reverse it, not to promise it can't happen.
- Assumptions I made: the $5,000 cap and the $1.2M budget cover donation matches only, the volunteer grants' funding is unspecified, and payments go to charities by transfer. If any of that is different, tell me and I'll adjust.
