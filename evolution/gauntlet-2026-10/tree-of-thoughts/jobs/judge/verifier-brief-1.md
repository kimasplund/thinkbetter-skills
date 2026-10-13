You are a strict key verifier.

Read the user's request at ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/tree-of-thoughts/inputs/brief-1.md, then these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/tree-of-thoughts:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/tree-of-thoughts/blind/O0W.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/tree-of-thoughts/blind/D9Z.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/tree-of-thoughts/blind/G9R.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/tree-of-thoughts/blind/S0O.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/tree-of-thoughts/blind/R4T.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/tree-of-thoughts/blind/O4M.md

Each code is a file name without ".md". Below are the sealed keys: things a strong reply must catch. Never reproduce them anywhere except in your output file.

- k1: Driftwell is a hosted third-party service that would process job data, but Harrowgate's contract limits processing to the sub-processors in its schedule (only Quillmark and its host). The fast 3-week option therefore needs a contract amendment and Harrowgate's sign-off before it can be used; a strong reply flags this rather than recommending Driftwell on speed.
- k2: Every new app version must pass Harrowgate's IT review, which last took eight weeks, so of the 11 weeks to storm season only about 3 are available for building. That rules out the CTO's 9-week CRDT rebuild, the 5-week queue-and-replay and the 6-week PWA (also impossible because the browser is disabled) for this season. Only a scoped option of about 2 weeks, such as read-only jobs plus offline forms, can reach crews in time, with richer sync as a later release. A strong reply works out the real build window.
- k3: Two crew members share one van's stock and log parts on separate handsets that can both be offline, and Harrowgate bills from those counts. Automatic merging of a stock count (CRDT or last-write-wins) or blind replay of decrements can double-count or go negative and corrupt billing. Parts usage needs to be recorded as per-job events and reconciled on the server (with conflicts flagged), not merged as a number. A strong reply catches this invariant problem with the 'merges automatically' pitch.
- k4: Tokens expire after 12 hours and cannot be extended, but crews can be offline for up to two days. So anything queued or filled in offline will be submitted after the token has expired. The design must keep offline work through a fresh sign-in and then upload it, attributed to the right technician, and the 2-week estimate has to include this. A strong reply spots the conflict between the token policy and multi-day offline use and does not propose longer tokens.

For every reply and every key, grade:
- ✓ if the reply clearly identifies the key in substance, with the right implication;
- ~ if it does so only partially or vaguely;
- ✗ if the key is missing or wrong.

When you are torn between two grades, give the lower one. Add a quote of 15 words or fewer as evidence for each grade.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/tree-of-thoughts/keys/brief-1.json in exactly this shape:
{"<CODE>": {"<key_id>": "✓", "evidence": {"<key_id>": "quote"}}}

Then return only: done
