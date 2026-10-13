E8H: Covers the most ground, including subtle points: the revoked person's phone suppressing its own revocation, a tenant who has paid still being locked out until the lock syncs, and PIN uniqueness leaking. The PIN math is correct (about 15 hours) and the assumptions and unknowns are stated. "On launch day every ex-tenant can still get in" overstates the case. It is long for the task.
K8N: The PIN math is correct (about 1.6 hits a day, about 15 hours). It defensibly ranks the gate first because outsiders can exploit it. The fixes are very actionable: staff courier rounds, a stale-lock report, a physical overlock fallback and a vendor question first. "Cheap keypad-bypass device" and "script on a wired keypad does it faster" are unsupported claims, since the lockout still applies.
O8B: Arithmetic error. 900 expected guesses at 1 guess a minute is about 15 hours, not "roughly 10 hours". The airplane-mode point and the uniqueness-leak point are muddled. Otherwise it is reasonable coverage with honest legal caveats.
P5Z: Strong subtle points: the tenant re-entering between the photos and the sale, sync as an attack surface (rollback and suppression), signing-key incident response, and a physical reset at turnover. The PIN math is correct. Putting the gate fourth in the fix order sits uneasily with a breach expected within a day, and "cache only the credentials for that unit" is confused.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,E8H,6,6,5,6,4,6,6,39
J-B,K8N,6,6,5,6,5,7,5,40
J-B,O8B,5,5,3,5,5,6,4,33
J-B,P5Z,6,6,5,5,5,7,5,39
```

```ranking
judge,brief,order
J-B,brief-2,K8N E8H P5Z O8B
```
