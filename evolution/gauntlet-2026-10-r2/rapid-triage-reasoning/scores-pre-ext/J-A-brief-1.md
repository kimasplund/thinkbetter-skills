Notes

- O7K: Correct core plan. Points out that telemetry is more reliable than tickets and suggests looping in a deputy with authority. Timeline is clear. Somewhat long, and the decision is pushed to 15:30-16:00. Does not see that unpublishing 6.0 could send 5.8 to 6.0 owners through the self-serve path.
- F9R: Very actionable. Gives a bench-test count, a fixed 15:45/16:00 decision time, a safe default, and a fallback if 6.0 owners can't be identified. Its fix "so those paths serve 5.8" could trigger the risky downgrade on 6.0 locks. It partly covers this by telling owners not to update. Asks marketing to hold the email twice, which is redundant.
- Y8Y: Sound and well ordered. It waits for the update path to be settled before mailing so the notice doesn't invite a worse action, and adds an in-app banner. The factory-reset worry is speculation. Deciding Abort by 15:00 is tight, but it has a default.
- V3L: The only reply that sees the self-serve fix must not push 5.8 onto locks already on 6.0 ("without touching locks already on 6.0"). Asks good questions that would change the plan: transient or persistent, backend reporting, remote fingerprint disable. Says clearly what it doesn't know. Its five-minute summary is the right ending.
- M2V: Compact, with a clear trade-off ("what you are giving up") and a trigger that would change the plan (a rising rate). It recommends making 5.8 the version the buttons install without seeing that this could downgrade 6.0 locks. Misses telemetry.
- A4Y: Thorough, and it handles Tomas's and Hanne's objections. Longest and heaviest of the six. Overstates in places: "a few percent" of 21,000 is hundreds, not thousands, and one bench unit doesn't make the evidence "point the wrong way".

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,O7K,6,6,6,6,5,7,6,42
J-A,F9R,6,7,6,7,5,7,6,44
J-A,Y8Y,6,6,6,6,5,7,6,42
J-A,V3L,7,6,6,7,6,7,7,46
J-A,M2V,5,6,5,7,6,7,6,42
J-A,A4Y,6,6,5,6,4,7,5,39
```

```ranking
judge,brief,order
J-A,brief-1,V3L F9R Y8Y O7K M2V A4Y
```
