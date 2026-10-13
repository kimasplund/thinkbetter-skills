I'm VP of engineering at Corvane Pay, a payments processor with 60 engineers. Our annual audit came back with one major finding: "Engineers hold standing write access to the production ledger database." It has to be closed before the auditors' follow-up review in April.

Our CISO, Mirela Dorn, wants all production database access removed from engineers by 31 January. Our head of platform, Anders Velk, says that would cripple incident response. Engineers fixed 38 of our 41 Sev-1 incidents last year through direct database access, at a median of 22 minutes, and he expects to lose senior people over it. They've been arguing about this for a month.

From our access logs for the past 12 months:

- 14,200 database sessions in total. 91% ran only SELECT queries, mostly support engineers checking a transaction's status for a customer ticket.
- 310 sessions wrote data; 270 of them were the on-call engineer during an incident.
- In 29 of those 38 Sev-1 fixes, the write was one of three statements: re-queueing a stuck payout batch, releasing a settlement lock, or correcting an FX rounding row.

Other context: our access proxy already issues time-limited, logged grants for the card-vault cluster, which we locked down in 2023 to meet card-data rules. Anders says on-call engineers find those grants slow to get at 3 am.

Who's right, and what do I tell them on Monday?
