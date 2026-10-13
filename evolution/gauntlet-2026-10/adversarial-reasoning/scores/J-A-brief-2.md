Notes (J-A, brief-2)

- R1L: Correctly leads with revocation, and its gate maths is right. It flags that maintenance codes cannot be revoked offline. "Gate keypads are typically online" is an unsupported assumption, and some sections are padding (privacy, migration, two priority lists).
- N5P: Strong and actionable. It suggests a physical hasp until gateways are in, requiring unit number plus PIN, a timed priority plan and honest residual risk. It states the per-keypad lockout as fact.
- F1L: Accurate gate maths and clear points on the courier withholding updates and the log. Ranking the gate first is defensible but debatable, since the gate gives site access, not unit access. Good split of confidence and an interim fallback.
- L1S: Good coverage of revocation and logs, but the gate maths is wrong: it says about 1 hit per 600 days when its own figures (1 in 900, 1,440 guesses a day) give about 1.6 a day. That error leads it to put the gate last.
- E8H: The most complete reply. It covers framing through the gate PIN, the revoked person blocking their own revocation, opening a unit on a stale state in both directions, and lost phones. Clear severities, a stated confidence and named unknowns. Somewhat long.
- O8B: Says airplane mode "doesn't matter", which misses that the revoked person's phone can be the courier. Its "about 10 hours" contradicts the 1-per-minute rate (about 15 hours). The PIN-uniqueness leak argument is muddled. The sync-age monitoring idea is useful.
- P5Z: Solid. Correct gate maths, a reset at unit turnover, and a check that the lock is really in the denied state before relying on the photos. Its stated assumptions are thin.
- K8N: Clear bottom line. Good points on starved logs, false attribution at the gate, unrevokable offline codes and stale-lock alerts. It puts the gate first, and adds an unsupported "keypad-bypass device" and "helpers without limit". It lists its assumptions well at the end.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,R1L,6,5,5,5,4,7,5,37
J-A,N5P,6,6,6,7,5,7,5,42
J-A,F1L,5,6,5,6,5,7,6,40
J-A,L1S,4,5,2,5,4,7,3,30
J-A,E8H,7,6,6,6,4,7,6,42
J-A,O8B,4,5,3,5,4,7,4,32
J-A,P5Z,6,5,5,5,5,7,5,38
J-A,K8N,6,6,5,6,4,7,5,39
```

```ranking
judge,brief,order
J-A,brief-2,E8H N5P F1L K8N P5Z R1L O8B L1S
```
