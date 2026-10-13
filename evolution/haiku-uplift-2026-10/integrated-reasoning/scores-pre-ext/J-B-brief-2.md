Notes (J-B, brief-2)

- K4K: Correct arithmetic, and 0.01 -> 62 is right. But it says "Odile is right that ... the bug is not in the code", and the brief says the opposite: she claims an IT fault. It never explains why the same factor caused only 3 incidents last summer. No confidence stated.
- U2U: Strong decision support: a test booking to confirm the cap of 65, a declared-vs-actual type check, and what would change its mind. "Weekend no-shows fell, because the 7.5% came from a Nov-Feb sample" is a non sequitur, since last summer's rate is unknown. The "~15% I'm holding back" is light confidence arithmetic.
- B2I: Catches the subtle point that the same factor ran last summer, and that low-demand weekends hid it. Gives the 4.6% break-even, correct settings for 0.00 and 0.02, an afternoon-long confirmation plan, and a bumping policy. "Winter foot-traffic" is a small invented detail.
- U2Q: Solid and actionable, with good assumptions. "Roughly half of fully sold sailings would overflow even before random variation" is muddled: an expected 63.8 means most overflow, and the overflow rate is itself the variation. "11 in a few weeks" misreads the timeline.
- A3P: Concise. 0.016 -> 62 and "overflows whenever fewer than three fail to show" are both correct. It misreads Odile ("right that overbooking is the cause") and treats the timetable cut as merely a question, which underweights a main driver.
- O2T: The broadest diagnosis: ranked causes, a check that incidents began on 1 June, a no-show comparison before and after, a loading-efficiency caveat and a factor <= no-show rule. Saying Odile is wrong that it "always worked" is a slight misreading. It is long, with a meeting script.
- I8J: The most rigorous on uncertainty. Its ~85-90% overflow probability at 65 sold checks out. Its 25-30% at 63 sold is a little low (I get about 32%). Clear sold-vs-boarded test to settle the dispute. Also misreads Odile ("right that the factor is the cause").
- G5D: Raises useful points: restore a weekend sailing, and add a waitlist rule. But "0.00 to 0.01 (sell 62 or 63)" is wrong, because 0.01 sells 62. It claims the factor explains why the problem "started with the summer timetable", yet that same factor ran last summer too. Its logic on counting bookings vs weights is muddled.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,K4K,4,5,3,5,6,7,4,34
J-B,U2U,5,6,4,7,5,5,5,37
J-B,B2I,6,6,5,6,5,7,5,40
J-B,U2Q,5,6,4,6,5,7,5,38
J-B,A3P,4,5,4,5,6,7,6,37
J-B,O2T,6,6,5,6,4,7,5,39
J-B,I8J,5,5,5,6,6,7,6,40
J-B,G5D,5,5,3,5,6,7,5,36
```

```ranking
judge,brief,order
J-B,brief-2,B2I I8J O2T U2Q U2U A3P G5D K4K
```
