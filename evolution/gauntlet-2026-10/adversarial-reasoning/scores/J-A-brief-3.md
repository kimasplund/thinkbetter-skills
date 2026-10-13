Notes

- M3L: Broad, well-ranked coverage including payment diversion, insider duties and privacy; the controls table is easy to act on. Minor slips: it says nothing checks the donation date (OCR does), and it reads the volunteer cap as per charity without flagging that.
- V4R: Puts budget exposure first and argues for it, with accrual on approval and pro-rating at 80%. Strong extras: bribery by proxy, Givelark personal fundraiser pages, donor-name matching. Flags the volunteer-cap ambiguity and says how the ranking would shift.
- F6O: Thorough and catches the $10 token trigger and the coercion risk. Has an arithmetic error ("a third of the money moving is the company's" when it is two thirds), omits payment diversion and separation of duties, and runs to 20 controls, which is heavy.
- W1L: Sound and specific. The best subtle point is five token donors unlocking 3:1 for a sixth, large donor. Covers BEC and separation of duties and is honest that the likelihoods are judgment. Small typo: the conflict declaration is missing "not".
- E5F: Decisive ("not safe as it stands") with a clear pre-launch list and specific tripwires. Flags the volunteer worst case of $9.5M. Error: it says after a refund "the charity keeps both". Engineering-firm bribery angle is relevant.
- L7F: The most comprehensive, with a useful "what I'd deprioritize" counter-case, but far too long. It asserts that the volunteer cap is per charity and then builds on that reading. The "one sentence for finance" is a run-on.
- G2T: The most complete threat model. Reasons well that forged receipts only pay off when combined with a linked charity, flags the volunteer-cap ambiguity, covers payment diversion and insiders, and uses the quarter lag as the window to check before money leaves. Slight overstatement that "a handful" could steer six figures.
- B5F: Compact, with a few sharp points (bank-transfer reference field, tax-receipt net amount, red-team test). Clipped and sometimes garbled (the "20 hours at 25 hours" sentence). Omits payment diversion and insider separation, and asserts there is no program cap.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,M3L,6,6,5,6,5,7,5,40
J-A,V4R,6,6,6,6,5,7,6,42
J-A,F6O,6,6,5,6,4,7,5,39
J-A,W1L,6,6,6,6,5,7,6,42
J-A,E5F,6,6,5,6,5,7,5,40
J-A,L7F,6,6,5,5,3,7,4,36
J-A,G2T,7,6,6,6,5,7,6,43
J-A,B5F,5,5,4,6,6,7,4,37
```

```ranking
judge,brief,order
J-A,brief-3,G2T V4R W1L M3L E5F F6O B5F L7F
```
