Notes:
- P5Z: Leads with revocation and gets the gate PIN arithmetic right (about 1.6 expected hits a day). It catches that photos may be taken while the overlock has not yet reached the lock. It points back to "point 1" and "sections 1 and 3", but its headings are not numbered. Solid and actionable.
- O8B: Good coverage and a sync-age monitoring idea. It contains errors, though: 900 guesses at 1 per minute is about 15 hours, not 10. It also says airplane mode "doesn't matter", but a phone with signal would deliver the revocation. The "uniqueness leak" point is muddled.
- K8N: It recommends not rolling out as specified and orders the fixes clearly. Strong extras: revoke gate PINs at overlock, block helpers from adding helpers, keep a physical overlock fallback, and its closing assumptions name the cheapest first question to put to the vendor. Some colour is unsupported ("script on a wired keypad", "keypad-bypass device"), and it assumes US state lien law.
- E8H: The deepest adversarial insight. The revoked person's own phone can suppress the update; the attacker frames an innocent tenant; auction listings tip off burglars; a tenant who has paid stays locked out; it needs per-lock keys and rollback protection. It handles the expiry lockout trade-off and the residual risk well and states its unknowns. The edge-case list adds a little length.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,P5Z,6,6,5,6,5,6,6,40
J-A,O8B,5,6,4,6,5,6,5,37
J-A,K8N,6,6,5,7,5,7,5,41
J-A,E8H,7,6,6,7,5,6,6,43
```

```ranking
judge,brief,order
J-A,brief-2,E8H K8N P5Z O8B
```
