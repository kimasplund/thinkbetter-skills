G2T: Puts budget overcommitment first and correctly calls it certain ($19M exposure, 240 maxed-out employees). Its arithmetic is right (five donors giving about $8,300 can pull $25k), and it flags that it is unclear whether the volunteer cap applies per employee or per charity. The "first four things" list and its use of the payment lag as a review window make it easy to act on. One small gap: it asserts there is no separation of duties without support.
M3L: Covers all the main attacks and lays the controls out clearly in a table. It also catches two less obvious points: the trigger leaks who gave to what, and the giving data is a privacy risk. Suggesting a one-quarter pilot with full manual review is a cheap way to reduce uncertainty. Weaknesses: it states the volunteer cap as "per charity" as if that were fact, and the "3x their gifts each month" line ignores the annual cap.
B5F: A compact reply that pairs each attack with its controls. Sharp points: a bank-transfer confirmation can show money sent to the employee's own account with the charity's name in the reference field, and the volunteer exposure is $9.5M with no donation needed. The one-hour red-team test is a good cheap check. One volunteer-hours line is garbled ("20 hours at 25 hours").
L7F: Thorough. Good points: a $5 donation counts toward the five-donor trigger, departing employees can submit claims before leaving, and it includes a useful "what I'd deprioritize" section. But it is much longer than needed, with 15 controls. It states the volunteer cap as per charity without flagging that this is an assumption, makes some unsupported generalisations, and its point that the 3:1 rule "rewards splitting" is muddled.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,G2T,6,6,6,6,5,7,6,42
J-A,M3L,5,6,5,6,5,7,5,39
J-A,B5F,6,6,5,6,6,7,5,41
J-A,L7F,6,6,5,6,3,7,4,37
```

```ranking
judge,brief,order
J-A,brief-3,G2T B5F M3L L7F
```
