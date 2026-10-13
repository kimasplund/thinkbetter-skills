Here is the review, with the biggest gaps first. Your controls look sensible on paper, but several of them rely on data the attacker can change.

**1. The bank-change check can be defeated from inside the portal (highest risk)**
- A supplier can edit their email, phone number and bank details in the same profile. Someone who takes over one supplier login can change the email and phone first, then change the bank details. The confirmation email goes to the new address, and your clerk calls the new number. Both checks then pass.
- Email plus a reset link is a weak login for accounts that control payments. Anyone who gets into a supplier's mailbox gets the portal account too. That is the usual route in the fake bank-change cases your federation has seen.
- Fixes:
  - Treat contact email and phone as protected fields, with the same checks as bank details.
  - Never call a number that was changed within the last 30 to 90 days. Use the number recorded at onboarding, from a contract or a verified source.
  - Require MFA for suppliers, and for any bank, email or phone change.
  - Put a payment hold of a few days after any change, and alert on a bank change shortly after a password reset.
  - Check that the account name matches the legal entity. Use bank account verification (confirmation of payee) if your bank offers it.
  - Make the AP clerk who calls someone other than the clerk who processes the change. Log the call outcome in the portal.

**2. Fake or collusive suppliers**
- Any site manager can create a supplier, and a site manager can also raise a PO up to £25k. The registration number check only proves that a real company exists. It doesn't prove that the person who set up the supplier owns that company or its bank account.
- The auto-approval rule makes this worse. A fake supplier with a PO under £25k can submit invoices under £10k, which pay with no human review. Splitting a £24k PO into three invoices of £8k would also pass.
- Fixes:
  - Separate who can create a supplier from who can raise POs and approve receipts.
  - Have AP verify new suppliers independently: bank account name against the company, director check, and a callback to a number from the public record.
  - Block payment until verification is complete.
  - Cap cumulative auto-approval per supplier, per PO and per week, not just per invoice.
  - Require goods-received or site sign-off confirmation before auto-approval.
  - Sample-review auto-approved invoices for new suppliers, and check for duplicate bank accounts and for bank accounts shared with employees.

**3. The duplicate invoice check is too narrow**
- It only matches the exact invoice number from the same supplier. `INV-001`, `INV001`, `inv-001 ` and `0001` can all slip past it. The same invoice can also be re-sent under a different supplier record, such as a duplicate vendor.
- Fixes:
  - Normalise invoice numbers by stripping case, spaces and punctuation, and compare them.
  - Also flag matches on amount plus date, and on supplier plus amount plus PO.
  - Look for duplicate supplier records that share a bank account or registration number.

**4. The payment-run handoff is the weakest link**
- The CSV sits on a shared drive between the export and the upload, so anyone with write access can edit it. The controller approves on count and total only. An attacker or insider could change account numbers, or redirect one payment to their own account and reduce another so the total still matches. The same person exports and uploads, so nobody else sees the file in between.
- Fixes:
  - Restrict the folder to the people who need it and log access.
  - Generate a hash of the file at export, and have a second person verify it before upload. An API or direct bank integration with no manual file step is better.
  - Give the controller a payee-level report to approve, not just a count and a total. At minimum it should show new or changed bank accounts, payments over a threshold, and first payments to a supplier.
  - Hold payments to changed accounts until the controller approves them explicitly.
  - Have someone other than the person who prepared the run do the upload or the approval.

**5. Ledgerfold's certification**
- A security certificate such as ISO 27001 or SOC 2 covers how Ledgerfold runs its platform. It does not cover how you configure it. Every gap above is a configuration or process issue.
- Ask Ledgerfold for the actual report and its scope, and check what it covers:
  - Does the scope include the supplier portal?
  - Is MFA available, and which roles can change which fields?
  - What do the audit logs and alerting cover?
  - How are admin and support access controlled?
- Also ask how they would notify you of a breach.

**6. Other items to check**
- Use least-privilege roles, and review who holds admin access. Log and alert on changes to supplier data.
- Check the process for staff leavers and for adding and removing users.
- Make the finance team aware of invoice impersonation and fake bank-change emails that arrive outside the portal. Make sure a request by email or phone alone can never change bank details.
- Run a pre-go-live test, with someone playing attacker against a test supplier account.

**Priority before April**
1. Lock down contact details, use an onboarding-sourced callback number, and require MFA.
2. Separate supplier creation from PO raising, and verify new suppliers independently.
3. Cap cumulative auto-approvals and tighten duplicate detection.
4. Secure the CSV handoff and give the controller a payee-level view.
5. Get Ledgerfold's certification scope and ask the configuration questions.

I assumed the portal's real permissions match your description. Check this in a demo or test environment, because default settings often differ from the plan.
