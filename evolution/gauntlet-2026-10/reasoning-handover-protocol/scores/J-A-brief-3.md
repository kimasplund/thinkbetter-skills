I8O: Solid and correct. Puts EC first, works out the gas remaining and the motor timing, and asks for drain/slab data and the predecessor's notes. Never mentions the BER lag or the chance that the 40% vent limit is a fixable fault. "Remove affected fruit so it doesn't distract the plant" is weak.
A0M: Tight and owner-voiced. Pulls the EC thread first, checks whether the 40% vent limit is a fault or a setting (cheap, non-obvious), suggests truss thinning, notes the BER lag, and ends with a clear confidence statement. Very actionable.
A6N: Correct but thin. No first-week plan, no BER-lag point and few concrete checks. The 65% confidence figure and the euro-loss question help.
X4C: The most thorough. Flags that the data is 6+ weeks old, checks emitters, raises the euro value of the losses, notes the BER lag, and asks whether Clean Leaf also covers fungicides/biologicals (important under 92-95% RH). Good day-by-day plan. Repeats the motor and gas points and runs long.
I5Q: Sharp point: were the lab samples taken from the C3 line or a shared tank? Also notes the EC may be a deliberate steering choice. But the week arithmetic is wrong (week 42 to week 2 is about 12 weeks, not 14-15), and the options are explicitly "not recommendations".
R8Y: Rigorous. Trust table, meter calibration, design changes so the EC and humidity effects can be told apart, count BER by truss date to find a trigger, ask whether the existing motors can be adjusted, and "don't reopen the diagnosis". Calibrated confidence. A little long, with section cross-references.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,I8O,5,5,5,5,5,7,6,38
J-A,A0M,6,6,6,6,6,7,6,43
J-A,A6N,5,4,5,5,6,6,5,36
J-A,X4C,6,6,6,6,4,6,7,41
J-A,I5Q,6,5,5,5,5,7,5,38
J-A,R8Y,6,6,7,6,5,6,7,43
```

```ranking
judge,brief,order
J-A,brief-3,R8Y A0M X4C I5Q I8O A6N
```
