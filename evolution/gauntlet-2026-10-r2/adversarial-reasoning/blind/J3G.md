# Where money could leave Ferrand & Locke, and what to change before April

## Short answer

Don't ship as designed. The bank-change check is the control everyone is relying on, and it has a hole you can drive through: the contact details used to verify a bank change are editable in the same profile, by the same login, as the bank details. Three other routes are at least as likely to cost you money: a fake supplier created through the site-manager route, invoices that never meet a second pair of eyes, and a payment CSV that can be altered between export and upload. All of these can be fixed with configuration and process changes before April.

## The routes, ranked

### 1. Taking over one supplier login defeats the bank-change check (critical)

Suppliers log in with email and password, and reset by email link. In the profile they can change email, phone and bank details. So an attacker who gets into a supplier's mailbox, or reuses a leaked password, can:

1. Log in (or reset the password through the compromised mailbox).
2. Change the contact email to one they control.
3. Change the phone number to one they control.
4. Change the bank details.

The portal then sends its confirmation to the "registered address", which is now the attacker's. Your AP clerk then phones "the number in their profile", which is the attacker's too, and the attacker confirms politely. Both of your checks are answered by the fraudster. This is the same loss your federation peers suffered, with one extra step.

Change before April:
- Verify bank changes against contact details recorded at onboarding or before the change request began, never against details that can be edited in the same session. The phone number for the callback should come from a source the supplier can't edit, such as the contract, a previous remittance, or the number you already had on file.
- Make email and phone changes high-risk events in their own right. Verify them by callback to the old number, notify the old email, and impose a cooling-off period (for example 5 working days with no payment to a new account after any contact or bank change).
- Require multi-factor authentication for supplier logins, at least for anyone who can edit bank details. Email-link-only resets are the weakest link here.
- Confirm that the new account name matches the registered company name, using confirmation-of-payee or a bank-account verification service. Reject or escalate on mismatch.
- Tell suppliers and clerks that bank changes arriving by email, phone or post outside the portal are never actioned. Without that rule the old fraud simply bypasses the portal.
- Have the callback script ask the clerk to speak to a named person from a known list, and give clerks explicit permission to refuse and escalate when pressured.

### 2. A fake supplier, added in good faith or otherwise (critical)

Any site manager can add a new subcontractor. AP checks the registration number against the public register. That proves a company exists with that number. It doesn't prove the bank account belongs to it, or that anyone at the company asked to be paid. Anyone can quote a real, healthy company's number and supply their own sort code. A dishonest or phished site manager, or a stranger posing as a subcontractor on site, can create the record.

Combine this with routes 3 and 4 and one person can create a supplier, raise a purchase order and have an invoice paid without anyone else looking.

Change before April:
- Let site managers request a supplier, but have AP (not the requester) create and activate it.
- Verify the bank account independently of the supplier's own paperwork: a confirmation-of-payee check, plus a callback to a number found from the register or your own previous dealings, not the number on the form.
- Hold the first payment to any new supplier for manual review by someone other than the requester.
- Check the register for company status and age, and for recent changes of directors or registered address. A long-dormant company that suddenly has a new address and a new bank account is a classic hijack.
- Report weekly on new suppliers and who created them.

### 3. Small invoices go through with no human review (high)

Anything under £10,000 that matches an open purchase order is paid automatically. The site manager can raise purchase orders up to £25,000 alone. So the approval for sub-£10k invoices is effectively the same person who raised the order, and nobody confirms the work happened.

Ways it is abused:
- **Insider or phished site manager:** raises a £24,000 PO to a fake or colluding supplier, then the supplier submits invoices of £9,900 each. Each one clears automatically. Three invoices clear before anybody sees a total.
- **PO splitting:** orders kept just under £25,000 so the commercial manager never signs.
- **Open POs left running:** an old PO with remaining balance is a standing licence for invoices.

Change before April:
- Auto-approve only when there is a matching goods-received or work-certified confirmation from someone other than the PO raiser (a three-way match), and only up to a cumulative cap per PO and per supplier per month.
- Aggregate: apply the £10k and £25k limits to the total value per supplier over a rolling period, not per document.
- Review and close stale POs; flag invoices against POs older than a set age.
- Make site managers' PO limits apply to the combined total for the same supplier and project.
- Sample a fixed percentage of auto-approved invoices every month for after-the-fact review.

### 4. The payment file can be altered before the bank sees it (high)

Each Thursday the AP supervisor exports a CSV to a shared drive and then uploads it. The financial controller approves in the bank portal, but the screen shows only the number of payments and the total. Anyone with write access to that shared drive, or the supervisor themselves, or malware on the supervisor's PC, can change account numbers in the file between export and upload. The count and total stay the same, so the approval screen shows nothing wrong. A fraudster can also change one amount up and another down by the same sum.

Change before April:
- Move to a direct, authenticated integration between Ledgerfold and the bank, or at minimum restrict the folder to the supervisor and a named deputy with write access logged, and make the file read-only after export.
- Produce a hash or control total from the export and have a second person check that the uploaded file matches. The totals should include a hash of account numbers, not only counts and sums.
- Give the approver a payee-level report that highlights every payment to an account that is new or changed in the last 30 days, and every payment above a set size, and require them to compare it to the bank screen.
- Separate duties: the person who changes bank details, the person who exports, and the person who approves should be three different people. The supervisor should not be able to edit supplier master data.
- Check that the bank's approval and release can't be done from the same machine or session as the upload.

### 5. Duplicate-invoice check is easy to sidestep (medium)

The portal rejects the same invoice number from the same supplier. A supplier, or an attacker using a taken-over login, only needs to resubmit as "INV-0042", "INV0042", "inv 42 " or with a trailing letter. The same genuine invoice can also be submitted twice by two different routes (once through the portal and once by email to the site). It will then be paid twice, and this happens by honest mistake as well as fraud.

Change: normalise invoice numbers (strip spaces, case and punctuation) and also match on supplier, amount and date within a window. Flag, don't just reject. Also forbid invoices arriving outside the portal once it is live.

### 6. Fraud aimed at the move itself (medium, time-limited)

When you announce the portal, every one of your 600 suppliers will get an email asking them to register. That is a gift to phishers, who can send a lookalike message pointing at a lookalike site to harvest passwords and then run route 1. Expect this in the weeks around April.

Change: announce the portal from a single, known domain; tell suppliers you will never ask for a password by email; consider invitation links tied to the registered contact only; review the first month's bank changes more heavily than usual.

### 7. "Independently certified" doesn't cover your setup (medium)

A certification such as ISO 27001 or SOC 2 says something about how Ledgerfold runs its platform. It doesn't cover how you configure it, who has admin rights in your tenant, whether MFA is switched on, or how your people behave. Most of the losses above happen inside a certified product.

Ask Ledgerfold before April:
- What is the scope and date of the certificate, and is the supplier portal in scope?
- Can MFA be mandated for suppliers and for your own users? Can bank-detail changes require approval by two people?
- What logging is available for profile and bank changes, and can it feed your monitoring?
- Who at Ledgerfold can see or change your tenant, and how is that access logged?
- How do they handle a customer reporting a suspected account takeover, and at what hours?

## Detection: if something gets through

- Daily list of bank-detail, email and phone changes, reviewed by someone outside AP.
- Alert on a payment to an account first used in the last 30 days, a bank account shared by two suppliers, or an account that matches an employee's.
- Alert on a login from a new country or device followed by a profile change within minutes.
- Agree in advance who calls the bank to recall a payment, and the target time. Fast recall is often the difference between recovering and not recovering the money.

## Other awkward cases to test

- A genuine supplier changes banks (merger, new account) during a busy week, so clerks learn to wave changes through.
- A supplier's staff member leaves and still has portal access.
- The clerk who does callbacks is on leave, and cover skips the step.
- Two suppliers trade under similar names, and a payment goes to the wrong one.
- Retentions, credit notes and part-payments that break the match rules.
- The Thursday run is late or the file is re-exported, so two versions exist.

## What to do first

1. Decouple contact verification from the editable profile and add MFA (route 1).
2. Move supplier creation and bank verification to AP with an independent check (route 2).
3. Add a payee-level approval view and file integrity control to the payment run (route 4).
4. Tighten auto-approval with goods-received matching and cumulative limits (route 3).
5. Put the rest in place before go-live, and ask Ledgerfold the scope questions this week.

## What risk is left

Even with all of this, a determined fraudster who compromises a supplier's real staff, or bribes an employee, can still get a payment through for a short time. The aim is that it is caught within days, in a small amount, and not paid in one Thursday run of six figures. Collusion between two senior people is not fully covered here.

What I took from your brief: I treated the written process as exactly what will be run, and I assumed the portal has no multi-factor option switched on, no two-person approval for bank changes and no integration with the bank, because none was mentioned. I also assumed the financial controller can't see payee-level detail on the bank's approval screen, as you described. If any of those is wrong, the ranking of routes 1 and 4 changes. Check first what the portal lets you configure for bank changes and logins, because that decides how much of route 1 can be closed in software and how much has to be process.
