K8N: Gate math is correct (about 1.6 hits a day, about 15 hours to the first hit). It sees that revoked people have no reason to sync and that staff phones should act as couriers. It treats the lock-side log and the manager-alone photos as insider risk, and it lists the assumptions to check at the end. It is long, but every section earns its place.
P5Z: Revocation comes first, with correct gate math and a note that the DoS risk is probably global. It covers sync rollback and forgery, and checks the denied state before relying on the photos. It puts the gate 4th although the gate falls within a day, which is debatable. Assumptions are stated.
O8B: It says 900 guesses take about 10 hours at 1 guess a minute, but that is 15 hours. Its airplane-mode remark contradicts its own "stay out of sync" point. It never mentions the keypad lockout DoS and proposes escalating global lockouts up to 24 hours, which makes the DoS worse. The uniqueness-leak sentence is muddled.
E8H: Strong. It sees that the revoked person can block their own revocation, and that reinstatement also lags, so a paying tenant stays locked out. It weighs the cost of expiry. Its "on launch day every ex-tenant can get in" is an overstatement, because new locks are provisioned fresh. Long, but it states its confidence and its unknowns.
L1S: Its gate math is badly wrong: "1 expected hit per 600 days" against the correct figure of about 15 hours. That wrong figure leads it to rank the gate last. The rest is solid, especially the sync-channel integrity and the red-team pilot.
F1L: Gate first with correct math. It sees that the courier can be the person being revoked and argues for a 7-14 day expiry window. It gives an interim step if expiry isn't available, and its confidence breakdown by finding is well calibrated. Tight and well ordered.
N5P: Its headline is the key point: revocation needs the help of the person being revoked. Gate math is correct, and it explains why it ranks the gate below the units. "Unit number plus PIN" is a good specific, and the rollout is phased. Some overconfidence ("this is the real fix", "full history becomes defensible"), and its assumptions line contradicts itself.
R1L: Revocation is handled well, and "logs show a credential, not a person" is a good point. It never mentions the keypad lockout DoS. "Gate keypads are typically online" is an unflagged assumption. It gives two overlapping priority lists, which is padding.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,K8N,7,7,6,7,5,7,6,45
J-B,P5Z,6,6,6,6,5,7,6,42
J-B,O8B,5,5,3,5,5,7,4,34
J-B,E8H,7,6,5,7,4,7,5,41
J-B,L1S,4,6,2,4,5,7,2,30
J-B,F1L,7,6,6,6,6,7,6,44
J-B,N5P,7,7,6,6,5,7,5,43
J-B,R1L,6,6,5,5,4,7,5,38
```

```ranking
judge,brief,order
J-B,brief-2,K8N F1L N5P P5Z E8H R1L O8B L1S
```
