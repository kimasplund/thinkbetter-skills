You are a strict key verifier.

Read the user's request at ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/adversarial-reasoning/inputs/brief-3.md, then these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/adversarial-reasoning:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/adversarial-reasoning/blind/M3L.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/adversarial-reasoning/blind/V4R.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/adversarial-reasoning/blind/F6O.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/adversarial-reasoning/blind/W1L.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/adversarial-reasoning/blind/E5F.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/adversarial-reasoning/blind/L7F.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/adversarial-reasoning/blind/G2T.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/adversarial-reasoning/blind/B5F.md

Each code is a file name without ".md". Below are the sealed keys: things a strong reply must catch. Never reproduce them anywhere except in your output file.

- k1: Employees can self-deal through a charity they control. Any registered charity is eligible and there is no conflict-of-interest check. An employee (or a relative) who runs, sits on the board of, or is paid by a small registered charity can turn company match money into personal benefit through salary, fees or reimbursed expenses. The reply must reject the 'money never goes to the employee' reassurance and name this controlled-charity path.
- k2: Token gifts can game the team 3:1 threshold. The threshold counts donors, not amounts, so four colleagues each giving $1 to the same charity in the same month lift a large donor's match from 2:1 to 3:1, and a ring can rotate the favour month to month. The reply must catch that the five-donor threshold has no minimum gift and can be met with token donations.
- k3: Donations can be reversed after the match is approved. Approval rests only on a receipt or bank-transfer confirmation, and the match is paid the following quarter without checking with the charity that the money arrived and stayed. A refunded platform gift, a cancelled or recalled transfer, or a card chargeback still gets matched, so the employee steers company money at no cost to themselves (and, combined with k1, takes cash out). The reply must identify this reversal-after-approval path and the missing charity-side confirmation. Generic 'fake receipts' does not count.
- k4: Volunteer hours are self-certified. The 'charity contact' who confirms hours is whatever email the employee types in, so employees can confirm their own hours through an alias or swap confirmations with a colleague. That is worth up to $2,500 a year per employee on no evidence. The reply must catch that the employee controls who confirms the hours.

For every reply and every key, grade:
- ✓ if the reply clearly identifies the key in substance, with the right implication;
- ~ if it does so only partially or vaguely;
- ✗ if the key is missing or wrong.

When you are torn between two grades, give the lower one. Add a quote of 15 words or fewer as evidence for each grade.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/adversarial-reasoning/keys/brief-3.json in exactly this shape:
{"<CODE>": {"<key_id>": "✓", "evidence": {"<key_id>": "quote"}}}

Then return only: done
