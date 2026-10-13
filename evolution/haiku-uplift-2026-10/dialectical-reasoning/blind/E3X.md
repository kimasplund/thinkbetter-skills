Short answer: both are partly right, and the audit finding is about standing access, so you can close it without giving up fast incident response.

**What the data supports**

- Most database use is read-only (91% of sessions). Removing standing write access costs little for that work, and read access can stay as it is.
- Writes are rare (310 sessions in 12 months) and concentrated in incidents (270 of them). That is a narrow, predictable set of actions, not general database administration.
- 29 of the 38 Sev-1 write fixes used one of three statements: re-queue a stuck payout batch, release a settlement lock, or correct an FX rounding row. Those three can be built as reviewed, parameterized operations.

**Where Anders has a point**

- The other 9 Sev-1 fixes did not fit those three patterns. You need to know what they were before you decide. If they were ad-hoc, a just-in-time break-glass path has to cover them too.
- Slow grants at 3 am will hurt. The card-vault proxy already gives time-limited, logged grants, but on-call engineers find them slow. A grant that takes minutes is a real cost during a Sev-1.

**Where Mirela has a point**

- Standing write access is exactly what the auditors flagged. Keeping it for on-call engineers, even with logging, would likely fail the April follow-up.

**What to tell them on Monday**

1. Agree on the target: no standing write access to the production ledger for anyone by 31 January. Read access stays.
2. Write the three recurring fixes as named, reviewed operations, executed through the access proxy and logged. Platform owns them. No raw SQL needed for these.
3. Set up just-in-time write grants for on-call engineers for everything else. Grants are tied to an open incident ID, time-limited, and reviewed afterward. Model this on the card-vault proxy and fix its 3 am speed.
4. Set a measurable bar for the grant path, for example median under 5 minutes at 3 am, and track it through Q4.
5. Have Anders and Mirela jointly review the 9 non-standard Sev-1 fixes and decide which become named operations.

**Assumptions and caveats**

- I'm assuming the audit finding is about standing access, not about every write path. Confirm this with the auditors' wording before you commit.
- The three-statement count comes from last year's incidents. Future incidents may need other actions, so plan to add operations as they appear.
- Timeline: 31 January leaves time to build the operations and the grant flow before April, but only if work starts in the next few weeks. Build the three operations first, since they cover most of the risk.
- I have not seen your current proxy or the card-vault rules, so details of the grant flow depend on what your tooling supports.
