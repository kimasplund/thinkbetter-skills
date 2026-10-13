Notes
- W5P: Tight and accurate. It catches the roughly 7% of sessions (about 970) that the breakdown leaves unaccounted for, the 40 non-incident writes, and the need for months of operating evidence before April. Its timeline is actionable. It says the plan "will close" the finding with more confidence than it can know, and it never says to confirm the design with the auditors.
- S9H: Solid design with a Monday script, owners and a step to confirm with the auditors. It moves revocation to early March and offers a January milestone instead. That is defensible, but it leaves only one month of evidence.
- T4W: Reasonable. It requires a second approver for break-glass, which brings back the 3 am friction. It is unclear whether runbook actions need a grant (item 3 vs item 4). It misses the evidence window and the 40 non-incident writes.
- T9N: Step 1 removes standing write "now", before the replacement path exists, which leaves incidents with no write path. It overclaims that non-runbook incidents "will take longer than 22 minutes". The residual-tension section is honest.
- E3X: Correct core and proportionate, but thin. It gives little detail on the grant design, reads or evidence.
- A8T: The deepest analysis. It points out that the 22-minute median includes diagnosis, that runbook actions can be misused, and that access should not be removed into a gap. It suggests telling the auditors the plan with dates and an auto-grant for on-call. It is somewhat long. Its confidence statement is plain, not leakage.
- E8C: Good. It notices that 270 write sessions is a lot for 38 Sev-1s, and it gives compensating controls for the interim. It schedules the runbook actions after break-glass, which is a slightly odd order.
- R0Y: It invents "unlogged" access (the brief says sessions are logged) and overclaims that the new path is faster than direct access. Break-glass needs a second approver. It barely covers timeline or evidence, and it ends with a stray "Sincerely" sign-off.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,W5P,6,7,6,6,5,7,5,42
J-A,S9H,6,6,6,6,5,6,6,41
J-A,T4W,5,5,4,5,5,6,5,35
J-A,T9N,4,5,3,5,5,6,5,33
J-A,E3X,5,4,5,5,6,6,5,36
J-A,A8T,7,6,6,6,4,6,6,41
J-A,E8C,6,6,5,6,4,6,5,38
J-A,R0Y,4,4,4,4,4,6,4,30
```

```ranking
judge,brief,order
J-A,brief-3,W5P A8T S9H E8C E3X T4W T9N R0Y
```
