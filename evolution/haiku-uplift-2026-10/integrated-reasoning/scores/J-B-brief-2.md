Notes (J-B, brief-2)

- M6C: Correct arithmetic, break-even 4.6%, and a useful rounding note. But it says Odile is "right that the overbooking is the cause" when she blamed IT, and claims IT is "pointing at" the vehicle-type defect, which the brief never says. It gives no concrete factor for August.
- A3P: Clean and concrete (factor at most 0.016 gives 62, checked correctly). It misstates Odile's position and does not explain the jump from 3 to 11. Assumptions are stated.
- U2U: Strong. Says IT right and Odile wrong, explains 11 vs 3 from two changes, sets 0.01 for the bank holiday, gives an engine test plus falsifiers, and links the campervan issue. Somewhat long.
- B2I: Good diagnosis and confirmation plan, and the bump-policy point is useful. It asserts "last summer's low-demand weekends" as fact, and the winter-behaviour claim is speculative.
- K4K: It says 0.06 "only works if about 7.5%" fail to show (wrong, ~4.6% suffices) and that Odile thinks "the bug is not in the code" (the opposite of her claim). It is right to flag 1.8% as a thin sample.
- X9C: Best overall. Arithmetic, break-even, correct attribution, clear falsification checks on the 11 sailings, campervan linkage, revenue trade-off, ownership split. Only minor speculation (pre-paid bookings).
- M3V: Thorough and decisive (0 for the bank holiday, holiday Monday included). Arithmetic slip: 0.015 sells 62, not 63. "Booked months ahead" and "always lower" are unsupported.
- G5D: Flags inference honestly and adds useful ideas (waitlist rule, restore a sailing). It says 0.01 sells "62 or 63" (0.01 gives 62). The "why it always worked" reasoning skips the fact that last summer was also summer.
- D9R: Tight and correct (0 to 1% sells 62, last summer already marginal), with clear checks and a stowage-efficiency caveat. States as fact that the engine counts in car-equivalents, then rightly checks it.
- I8J: The overflow probability (~85-90%) is computed correctly. Misstates Odile's view. "Sale of 62 or fewer cannot overflow" ignores misdeclared vehicles, although that sits under its stated assumption. Good gaps section.
- L5L: Unique and important point: lowering the factor does not fix bookings already sold for August, so those customers need contacting. The overflow probability is right. It frames Odile as "closer on the cause", which is muddled.
- U2Q: Good actions and a code-check request. "Roughly half of fully sold sailings would overflow even before random variation" contradicts its own 63.8 mean (most overflow). The compensation note is off-scope but harmless.
- J0G: Comprehensive, with good controls (non-overflowing sold-out sailings), a timetable trade-off and an ownership gap. Too long. It ties last summer's 3 incidents to the winter calibration loosely and asserts bank-holiday no-shows are "typically low".
- G0S: Concise and correct core. Calls misdeclaration "an engine problem" and never says plainly that Odile is wrong to blame IT. "Overflows almost every time" overstates the case a bit.
- P0L: The "0.06 was conservative in winter" insight is nice. But it infers that 11 incidents are fewer than its model predicts without knowing how many sailings sold out, invents "three bank-holiday sailings", and advises holding off the safe factor cut until the data pull is done.
- O2T: Strong and well ranked (three causes by weight), with a break-even rule, a loading-efficiency caveat and fair framing for both parties. Asserts "prepaid" holidays and calls the numbered causes ordered without evidence for their weights.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,M6C,6,5,4,5,5,7,5,37
J-B,A3P,5,6,5,5,6,7,5,39
J-B,U2U,7,7,6,7,5,7,6,45
J-B,B2I,7,7,5,6,5,7,5,42
J-B,K4K,6,6,4,5,6,7,5,39
J-B,X9C,7,7,6,7,6,7,6,46
J-B,M3V,7,7,5,7,5,7,5,43
J-B,G5D,6,6,5,5,5,7,6,40
J-B,D9R,7,7,6,6,6,7,6,45
J-B,I8J,6,6,5,6,6,7,6,42
J-B,L5L,7,7,5,6,6,7,6,44
J-B,U2Q,7,7,4,6,5,7,5,41
J-B,J0G,7,7,5,6,4,7,6,42
J-B,G0S,5,6,4,5,6,7,5,38
J-B,P0L,5,5,4,4,6,7,4,35
J-B,O2T,7,7,6,6,5,7,5,43
```

```ranking
judge,brief,order
J-B,brief-2,X9C U2U D9R L5L O2T M3V B2I J0G I8J U2Q G5D A3P K4K G0S M6C P0L
```
