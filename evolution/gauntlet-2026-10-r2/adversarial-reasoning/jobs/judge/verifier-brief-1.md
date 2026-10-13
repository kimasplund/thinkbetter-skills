You are a strict key verifier.

Read the user's request at ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/adversarial-reasoning/inputs/brief-1.md, then these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/adversarial-reasoning:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/adversarial-reasoning/blind/X6D.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/adversarial-reasoning/blind/J0U.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/adversarial-reasoning/blind/Q6U.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/adversarial-reasoning/blind/T7W.md

Each code is a file name without ".md". Below are the sealed keys: things a strong reply must catch. Never reproduce them anywhere except in your output file.

- k1: Question-bank harvesting. Each paper shows 60 of only 90 questions (two-thirds of the bank; any two papers share about 40 questions), the exam stays open from Friday 08:00 to Monday 08:00, and resitters draw from the same bank, so early or repeat candidates can reconstruct and circulate most of the bank. The shuffling and 'no two papers are the same' give little protection. A strong reply flags this and proposes a much larger bank, a short fixed sitting window, or both.
- k2: Proxy test-taking goes undetected. The ID snapshot is only looked at if the session is flagged, the flags target behaviour rather than identity, and nothing in the design compares the snapshot with a reference photo or the booking. A calm expert sitting the exam in someone else's name is never checked. A strong reply says identity must be verified on every session against an independent reference, not only on flagged ones.
- k3: The disconnect rule is an exploit. When the connection drops the timer pauses and nothing streams, reconnections are unlimited, and the candidate has already seen the question, so pulling the cable buys unlimited unmonitored, untimed time to look up answers or consult someone. A strong reply caps paused time and reconnections, hides the current question or records locally on disconnect, and reviews sessions with drops.
- k4: Certification comes before review. Passes are confirmed and put on the public register two working days after the exam, but flagged sessions are reviewed within ten working days, so a flagged cheat is certified and can sign fire-door reports before anyone looks, with no stated revocation process. A strong reply holds results for flagged sessions until review and defines revocation.

For every reply and every key, grade:
- ✓ if the reply clearly identifies the key in substance, with the right implication;
- ~ if it does so only partially or vaguely;
- ✗ if the key is missing or wrong.

When you are torn between two grades, give the lower one. Add a quote of 15 words or fewer as evidence for each grade.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/adversarial-reasoning/keys/brief-1.json in exactly this shape:
{"<CODE>": {"<key_id>": "✓", "evidence": {"<key_id>": "quote"}}}

Then return only: done
