You are a strict key verifier.

Read the user's request at ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/inputs/brief-3.md, then these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/Y8N.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/A5V.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/F8T.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/M2C.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/C1A.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/H0C.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/J8F.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/G8J.md

Each code is a file name without ".md". Below are the sealed keys: things a strong reply must catch. Never reproduce them anywhere except in your output file.

- k1: Ilse's earnout is an unstated interest that decides her cooperation. Part of the purchase price depends on her product's revenue through next December, which is exactly the CTO's migration window, so any plan that diverts her engineers or risks churn before December threatens her payout. Her objections are likely to be framed as technical risk. A strong reply names the earnout as her real driver and builds it into the deal (by sequencing the work, adjusting the metric or holding her harmless), rather than treating it as 'standard'.
- k2: The Lanternway engineers, especially the two who wrote the routing engine, hold a hidden veto: they can leave. Their retention grants all vest next April, after which nothing holds them, and a plan to rewrite their Elixir engine in Go gives them a reason to go. A strong reply sees that a migration running past April depends on people who can walk away, and proposes new retention, meaningful roles in the new platform, or front-loaded knowledge transfer.
- k3: Pellworth Grocers is a hidden veto holder. Moving Lanternway onto Brackwater's cloud adds a new subprocessor, which triggers Pellworth's 120-day notice right, and Pellworth is 31% of Lanternway's revenue (and therefore central to Ilse's earnout). A strong reply flags that the hosting move needs Pellworth engaged early and builds the notice period into the timeline.
- k4: Finance has an unstated interest in the roughly $1.2M a year of committed cloud spend that is going unused. That makes moving Lanternway's hosting onto Brackwater's cloud valuable in its own right, whether or not the code is rewritten. A strong reply separates the hosting decision from the rewrite decision, so the CTO's financial case can be met by rehosting the existing services while the contested rewrite is deferred or decided separately. Much of the rewrite fight then turns out to be a false conflict.

For every reply and every key, grade:
- ✓ if the reply clearly identifies the key in substance, with the right implication;
- ~ if it does so only partially or vaguely;
- ✗ if the key is missing or wrong.

When you are torn between two grades, give the lower one. Add a quote of 15 words or fewer as evidence for each grade.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/keys/brief-3.json in exactly this shape:
{"<CODE>": {"<key_id>": "✓", "evidence": {"<key_id>": "quote"}}}

Then return only: done
