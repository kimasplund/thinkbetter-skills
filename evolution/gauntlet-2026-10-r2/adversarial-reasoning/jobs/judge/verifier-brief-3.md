You are a strict key verifier.

Read the user's request at ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/adversarial-reasoning/inputs/brief-3.md, then these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/adversarial-reasoning:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/adversarial-reasoning/blind/S8W.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/adversarial-reasoning/blind/F1M.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/adversarial-reasoning/blind/I0C.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/adversarial-reasoning/blind/Z3O.md

Each code is a file name without ".md". Below are the sealed keys: things a strong reply must catch. Never reproduce them anywhere except in your output file.

- k1: The bank-change checks are self-referential. Suppliers can edit their email, phone and bank details in the same profile, and both the confirmation email and the AP callback use those profile values, so anyone who takes over a supplier login (for example via the email password reset after compromising the supplier's mailbox) changes the phone and email first and then confirms the bank change to themselves. A strong reply requires a callback to an independently held number, notice to the previous contacts, and a hold on changes made together.
- k2: One person can pay a supplier end to end. A site manager can add a subcontractor, raise purchase orders up to £25,000 alone, and invoices under £10,000 that match an open order are paid with no further human approval (larger amounts can be split under the threshold). A site manager with a sham or connected company gets paid with no second person involved; the registry check only proves the company exists, not that it is independent or that the bank account is its own. A strong reply separates supplier set-up from ordering, requires someone else to confirm work received, and checks links between staff and suppliers.
- k3: Payment-file tampering. The CSV sits on the finance shared drive between export and upload, and the financial controller's approval shows only the count and total, so changing account numbers or payees in the file (by the supervisor or anyone with write access to the drive) leaves both unchanged and passes approval. A strong reply calls for direct integration or a locked, integrity-checked file, restricted access, and approval or reconciliation at payee and account level against the supplier master.
- k4: Weak duplicate detection. Blocking only an exact repeat of an invoice number from the same supplier lets the same invoice be paid twice with a changed number or format, or through a second supplier record, and auto-approval under £10,000 means no human sees it. A strong reply adds duplicate checks on amount, date, purchase order and bank account, and checks for duplicate supplier records.

For every reply and every key, grade:
- ✓ if the reply clearly identifies the key in substance, with the right implication;
- ~ if it does so only partially or vaguely;
- ✗ if the key is missing or wrong.

When you are torn between two grades, give the lower one. Add a quote of 15 words or fewer as evidence for each grade.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/adversarial-reasoning/keys/brief-3.json in exactly this shape:
{"<CODE>": {"<key_id>": "✓", "evidence": {"<key_id>": "quote"}}}

Then return only: done
