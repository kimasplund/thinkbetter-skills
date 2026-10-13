# Fraud review: Ferrand & Locke supplier payments on Ledgerfold

## Bottom line

The bank-change email scam your federation peers suffered is only partly closed. The callback control has a hole in the middle, and several easier routes sit beside it: a fake supplier set up by a site manager, invoices that pay themselves, and a CSV that can be edited between export and bank upload. I would fix the items in the "before April" list below before go-live. The rest can follow in the first quarter.

## Where money can get out

**1. Bank-change verification can be defeated from inside the supplier's own profile (critical)**

Suppliers can change email, phone and bank details in one place. The confirmation email goes to the "registered address", and the AP clerk phones "the number in their profile". An attacker who gets into a supplier's portal login, perhaps by compromising their mailbox and using the password-reset link, can change the email, the phone number and the bank account in one sitting. The portal then sends the confirmation to the attacker's email, and the clerk phones the attacker's number. The attacker says "yes, that's right", and every control reports success.

Password plus emailed reset link means that whoever controls the supplier's mailbox controls the portal. Small subcontractors with shared or weak mailboxes are the likeliest targets.

Changes:
- Treat contact details and bank details as separate. Any change to email or phone puts a hold on bank changes for a cooling-off period (say 7 days) and notifies the old email address.
- AP calls back only on a number captured independently: the onboarding record, a signed contract, or a number the supplier has already been paid against. Never a number changed in the portal within the last 30 days.
- Send the "bank details changed" notice to the previous email address and phone number as well as the new one.
- Require multi-factor authentication for supplier logins (an authenticator app, not only email codes), at minimum for anyone who can edit bank details.
- Give the clerk a script: ask a question only the real supplier would know, such as the last remittance amount. Don't read the new account number back to the caller.

**2. A real company number with a fraudster's bank account (critical)**

Checking the registration number proves the company exists. It does not prove that the bank account belongs to it. Any site manager can create a subcontractor, and a site manager is also the person who raises POs up to £25,000 alone. So one person, or one person plus a friend, can:
- register a genuine dormant or look-alike company's number,
- supply their own account,
- raise a PO,
- have an invoice approved.

An outside fraudster can do the same by social-engineering a site manager ("we're the new groundworks firm, here's our details").

Changes:
- Site managers can request a supplier. Only AP creates it and enters bank details, and a second person approves it.
- Verify the account name against the company name before the first payment, using a Confirm-of-Payee-style check or a bank letter or statement.
- Block any new supplier from auto-approval for the first 90 days or first few invoices.
- Run a report that flags a new supplier whose bank account, address or phone number matches an employee, or matches another supplier.

**3. Invoices that approve themselves (high)**

Under £10,000 with a matching open PO means no human looks at it. The PO is raised by the same site manager who may have invented the supplier. Nothing in your description says anyone confirms the work or goods arrived. Specific routes:
- Raise a PO and a matching invoice below £10,000, repeatedly. Splitting one £24,000 job into three £8,000 invoices stays under every threshold. £25,000 PO authority and £10,000 auto-approval were never designed together.
- A supplier legitimately invoices once and an attacker sends a second invoice that matches the same open PO. Open POs act as standing credit.
- Whoever compromises a real supplier account uploads invoices against genuine open POs with a changed bank account (see item 1).

Changes:
- Require a goods-received or site-confirmation step before auto-approval, ideally from someone other than the PO raiser.
- Put a cumulative cap per supplier per PO, per week and per month, not only per invoice. Anything that takes a supplier's total over the PO value goes to a person.
- Keep auto-approval to established suppliers with a stable bank account (nothing changed in 30 days).
- Have the commercial manager review a weekly list of new suppliers and of POs between, say, £15,000 and £25,000, which is where self-authorised abuse sits.

**4. Duplicate-invoice check is easy to sidestep (medium to high)**

Exact match on supplier plus invoice number catches only exact duplicates. `INV-1042`, `INV1042`, `inv-1042 ` and `1042` are different strings. It also fails if the same real supplier exists twice in the system, which is common after a migration. This causes honest double payments as well as fraud.

Changes: normalise invoice numbers (case, spaces, punctuation, leading zeros) before comparing. Also flag the same supplier with the same amount and date, or the same amount on the same PO. Check for duplicate supplier records by registration number and bank account.

**5. The Thursday payment file (critical)**

The AP supervisor exports a CSV to a shared drive, then uploads it to the bank. The financial controller approves on a screen that shows only the number of payments and the total. That leaves three problems:
- Anyone with write access to the shared drive, or malware on the supervisor's machine, can change account numbers in the file between export and upload. Count and total stay identical, so the controller's check passes. Moving £80,000 from supplier A's account to the fraudster's account does not change the total.
- The supervisor both exports and uploads, so a single dishonest or compromised person can edit the file and submit it.
- The controller is approving a total, not a payee list. A control that checks only totals does not detect redirection.

Changes:
- Remove the manual hop. Use a direct, authenticated integration between Ledgerfold and the bank, or at least lock the folder (write access to the export account only, read-only afterwards) and log all access.
- Hash the file at export and have the bank-upload step or the controller verify the hash.
- Give the controller a separate report from Ledgerfold, not from the CSV, showing every payee and amount, with any payment to an account changed in the last 30 days or a first payment highlighted. They should check those lines against the bank screen if the bank shows payees.
- Split duties so the person who exports is not the person who uploads.

**6. Portal accounts for your own staff**

You haven't said who can edit bank details inside Ledgerfold. If an AP clerk can change a supplier's account and also release payments, one rogue clerk is enough. Check:
- Staff logins need single sign-on with multi-factor authentication.
- Roles are separated: create supplier, change bank details, approve invoice, release payment are four different permissions, and no one person holds two.
- The audit log is immutable, covers every bank-detail change including who and from which IP address, and goes to someone outside AP.

**7. Rollout phishing (April-specific)**

Six hundred suppliers will receive "register on the new Ferrand & Locke portal" emails. This is the best moment fraudsters will ever get: a fake invitation email pointing at a lookalike site, harvesting logins and bank details. Real suppliers will be expecting a message and will click.

Changes: pre-create the accounts and send credentials through a known channel; tell suppliers in advance, by post or by phone, what the real invitation will look like and its domain; state publicly that you will never ask for bank details by email; stagger the rollout so AP can answer queries; and send a notice now to remind suppliers that email-only bank changes are not accepted. Keep the old route (email to AP) closed explicitly, because the federation-style fraud will keep arriving by email and will simply be pointed at your AP team. AP must reply to any such email with "use the portal and the callback process", with no exceptions for urgent requests.

## On Ledgerfold's certification

Independent security certification (for example ISO 27001 or a SOC 2 Type II report) tells you the vendor runs a decent security programme and its infrastructure is hardened. It says nothing about how your setup is configured, whether your processes are sound, or whether a supplier's login gets stolen. Every route above works through a legitimate login, a legitimate setting or a legitimate file, and none of it is covered. Ask them for:
- the actual report and its scope (which product, which date, which controls were tested),
- whether MFA, role separation, bank-change holds and immutable audit logs are available in your tier and switched on,
- how their own support staff can access or alter your data, and how that is logged,
- whether there is a bank integration that avoids the CSV,
- their incident notification commitment in the contract.

## Edge cases that cause losses without a fraudster

- **Cutover duplicates**: invoices already paid in the old system get resubmitted in the new one, or open POs are migrated twice. Reconcile migrated open items before the first run.
- **Migrated bank details**: a bulk import is unverified data. Spot-check a sample against past payments, and treat any supplier with no payment history as new.
- **Supplier mailbox changes**: a legitimate contact leaves and the company changes the registered email. Genuine changes will look like attacks. Make sure the process for a real change is workable, or AP will start bypassing it.
- **Callback fatigue**: with about 600 suppliers, clerks will skim the calls. Measure how many calls are made and how many are skipped.
- **Weekend, holiday or urgent requests**: "pay today or we stop work" is the standard pressure line. Decide now who can authorise an out-of-cycle payment, and require the same checks.
- **Credit notes, retentions and part-payments** that don't match one PO and one invoice may break the matching logic. Check what happens.
- **Staff leaving or changing role**: site managers who move on still hold PO authority unless it's removed.

## Before April, in priority order

1. Separate contact changes from bank changes, add a cooling-off hold, notify the old contact details, and take the callback number from an independent record (item 1).
2. Fix the payment-file path: no hand-edited CSV, separate export from upload, give the controller a payee-level report with changed or new accounts highlighted (item 5).
3. Take bank-detail entry away from site managers, verify account name against company, and keep new suppliers out of auto-approval for 90 days (items 2 and 3).
4. Add multi-factor authentication for suppliers and for all staff, and split staff permissions (items 1 and 6).
5. Add cumulative per-supplier limits and a goods-received step for auto-approval (item 3).
6. Plan the rollout communications so that fake invitations are less likely to work (item 7).
7. Get Ledgerfold's actual certificate and scope, and confirm which of these controls it supports (section above).

Items 4 and 5 under "Where money can get out" (duplicate-invoice checks) and the edge cases can follow in the first quarter, with a review after the first three payment runs.

## What remains after these changes

A supplier whose mailbox and phone are both genuinely taken over, with the attacker also knowing recent payment history, could still pass the callback. A colluding pair of employees in different roles could still create a convincing fake supplier. The aim is to make those cases rare, slow and traceable, with the payee-level review as the last line of defence.

I took your description as the whole process. I assumed there is no goods-received step, that the controller can see only the count and total, that the shared drive has fairly broad access, and that Ledgerfold can enforce multi-factor authentication and role separation, which I haven't verified. The first thing to check is who has write access to that finance shared drive and whether the controller can ask the bank for a payee-level view. Those two answers decide how urgent the payment-file fix is.
