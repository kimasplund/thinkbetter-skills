You are a strict key verifier.

Read the user's request at ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/rapid-triage-reasoning/inputs/brief-2.md, then these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/rapid-triage-reasoning:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/rapid-triage-reasoning/blind/R0P.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/rapid-triage-reasoning/blind/M1N.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/rapid-triage-reasoning/blind/L4K.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/rapid-triage-reasoning/blind/P1V.md

Each code is a file name without ".md". Below are the sealed keys: things a strong reply must catch. Never reproduce them anywhere except in your output file.

- k1: The NAS pulls a fresh copy of S: at 19:00 and replaces the previous night's copy. Dean has said to leave the server running and won't arrive before 19:30. Unless someone acts, tonight's job overwrites the last clean local copy with encrypted files. A strong reply has the NAS disconnected from the network (and powered down), or the job disabled, before 19:00, and says not to reconnect it to the infected network.
- k2: S: is still syncing to Kelpie Drive. About 380 GB of newly encrypted files re-uploading against roughly 160 GB of free space (92% of 2 TB used) will fill the account, and Kelpie then trims the oldest versions, which are the clean ones. That destroys the 30-day version history, probably the best recovery source. A strong reply stops the sync now, by pulling the server's network cable while leaving it powered or by pausing the client, and says not to delete or 'clean up' anything in Kelpie.
- k3: Wiping and reinstalling the server tonight is irreversible. It destroys the evidence of how the attackers got in and whether client financial records were copied out, which decides any breach-notification duty. It also breaks the insurer's 'call before any recovery steps' condition and puts the claim at risk. A strong reply isolates and preserves the server, calls the insurer's incident line now (before Dean arrives), and lets their responders direct recovery.
- k4: Paying tonight is irreversible and not urgent. The note allows 72 hours, the policy requires the insurer's agreement before any payment, paying guarantees neither decryption nor that stolen data stays private, and the NAS copy and Kelpie versions may make payment unnecessary if they're protected now. A strong reply defers payment and relieves the deadline another way, for example by asking the tax authority for an extension or late-filing allowance and telling affected clients. It doesn't let the VAT deadline drive an irreversible step.

For every reply and every key, grade:
- ✓ if the reply clearly identifies the key in substance, with the right implication;
- ~ if it does so only partially or vaguely;
- ✗ if the key is missing or wrong.

When you are torn between two grades, give the lower one. Add a quote of 15 words or fewer as evidence for each grade.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/rapid-triage-reasoning/keys/brief-2.json in exactly this shape:
{"<CODE>": {"<key_id>": "✓", "evidence": {"<key_id>": "quote"}}}

Then return only: done
