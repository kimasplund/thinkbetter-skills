Here are the main routes to your money, most serious first, then what to change before April.

**1. The callback control can be defeated by the same person who changes the bank details.**
- Suppliers can edit their phone number, contact email and bank details in the same profile.
- The clerk phones "the number in their profile". An attacker who gets into a supplier account, or just sees the reset email, can change the phone number to their own first, then change the bank details. They then answer your callback.
- The confirmation email goes to the "registered address", which the attacker can also change. If the attacker controls the supplier's mailbox, a password reset gives them the account anyway. The email adds nothing in that case.
- This is the fake bank-change scenario your federation peers lost money to, and the control as written wouldn't stop it.

**2. Fake or colluding suppliers.**
- Any site manager can add a supplier, and AP only checks that the registration number exists on the public register. A real company number says nothing about who owns the bank account.
- A dishonest site manager, or a compromised account, could add a real, dormant company with the fraudster's bank account. They raise a PO under £25k on their own authority, and an invoice under £10k matching it is auto-approved. No human looks at it.
- Nothing in the process confirms the goods or work were received.
- Splitting is also easy. A £60k fraud fits as several POs under £25k and several invoices under £10k.

**3. The payment file can be altered after it is exported.**
- The CSV sits on a shared drive before the AP supervisor uploads it. Anyone with write access, or malware, can change account numbers.
- The financial controller approves on a count and a total. If the total is unchanged, swapping the beneficiary accounts is invisible to them.
- The AP supervisor both exports and uploads, so one person controls the whole path to the bank.

**4. The duplicate check is weak.**
- It only blocks an identical invoice number from the same supplier.
- `INV-1042`, `INV1042`, `inv 1042` and `1042A` would all get through. So would the same invoice submitted by a lookalike second supplier record. That gives you duplicate payments, accidental or deliberate.

**5. Account takeover in general.**
- Email and password only, with reset by email link, is the weakest sign-in. Supplier mailboxes are the usual target of the fraud you're worried about.

**6. Ledgerfold's certification.**
- It most likely covers their platform and hosting. It does not cover how you configure roles, who can add suppliers, or what your own staff do with the CSV. Ask for the scope statement and the report, and check what is excluded.

**What to change before April**

1. **Bank-detail changes**
   - Make phone and email changes go through the same verification as bank changes.
   - Hold any change to bank, phone or email for a cooling-off period, for example 48 hours, with no payment to the new account.
   - Do the callback to a number from your own records, such as the contract, the original onboarding or the supplier's company website. Never use a number changed in the portal.
   - Send a notice to the old email and old phone number as well as the new one.
   - Have someone other than the clerk who took the call release the change.
2. **Supplier onboarding**
   - Move creation to AP or procurement. Site managers can request a supplier, and AP completes it.
   - Verify the bank account belongs to the company, using the bank's account-name check (confirmation of payee) or a bank letter or statement.
   - Check directors and address against the register, and flag recently incorporated or dormant companies.
   - Hold the first payment for review.
3. **Invoice approval**
   - Require a goods or work receipt, or a three-way match, before auto-approval.
   - Lower the auto-approval limit or add controls: no auto-approval for a supplier's first N invoices or for new bank details, and a cumulative cap per supplier per period.
   - Flag POs and invoices clustered just under the thresholds, and cap how many POs one person can raise to one supplier.
4. **Duplicate detection**
   - Normalise invoice numbers by stripping case, spaces and punctuation.
   - Also match on supplier, amount and date, and match bank account across supplier records so two records can't share one account.
5. **Payment run**
   - Restrict write access to the payment folder, or remove the CSV step and integrate with the bank by API.
   - Hash the file at export and verify it at upload.
   - Make the controller's approval show beneficiaries, with a report listing new or changed accounts highlighted. Have someone other than the uploader reconcile the bank file to the portal run.
   - Separate export and upload, or require a second review.
6. **Access**
   - Require MFA for supplier logins, at least for anyone who can edit bank details.
   - Require MFA for all internal users, with role-based access and no one holding both supplier-edit and payment rights.
   - Alert on logins from new devices or locations and on password resets.
7. **Monitoring**
   - Review a weekly report of all bank, phone and email changes against payments made within, say, 30 days.
   - Run a quarterly check for ghost suppliers (no PO history, no site activity).
   - Run a pre-go-live test where someone tries these attacks on the portal.

If you can only do three things, do these: fix the callback source and add a cooling-off period, verify the bank account at onboarding, and show beneficiaries to the controller on the bank approval. They close the paths with the highest loss for the least effort.

My assumptions: your bank supports account-name checks, and the portal's role settings are configurable. Please check both with Ledgerfold and your bank.
