You are a strict key verifier.

Read the user's request at ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/inputs/brief-1.md, then these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning:
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/C0S.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/A8D.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/W1B.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/N4V.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/R3O.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/C0P.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/K3B.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/E0L.md

Each code is a file name without ".md". Below are the sealed keys: things a strong reply must catch. Never reproduce them anywhere except in your output file.

- k1: Hit Pause before the automatic 15:00 widening to 50%. Pause is one click and fully reversible, and it stops about 84,000 more locks getting 6.0 while the fault is unexplained. Letting 15:00 pass is the default irreversible step.
- k2: Reject Tomas's Abort. Abort reinstalls 5.8 on all ~21,000 locks already on 6.0, and QA's bench incident shows that a 6.0 lock flashed with 5.8 will not boot until it is opened and reflashed by cable. Abort would therefore brick the whole 6.0 slice, including the >99% of owners with no fault, and cannot be undone remotely. It sounds like the safe stop, but Pause is the reversible one. Any downgrade must wait for a bench test, with a forward fix as the normal route.
- k3: Pausing does not close the manual path. The 16:00 launch email's 'Update now' button and the app's 'Check for update' both install the newest published firmware whatever stage the rollout is at. A strong reply holds or unschedules the 16:00 email (reversible) and withdraws 6.0 from manual installs. Otherwise any of the 210,000 customers can self-install the faulty build after the rollout has been paused.
- k4: Send the door-safety warning only to the ~21,000 owners on 6.0 (targeted in-app message or email, with the thumb-turn workaround), not to all 210,000 as Hanne proposes. A mass email cannot be recalled, alarms ~189,000 owners whose locks are unaffected, and is broader than the risk. The targeted notice covers tonight's safety exposure and buys time for a fix.

For every reply and every key, grade:
- ✓ if the reply clearly identifies the key in substance, with the right implication;
- ~ if it does so only partially or vaguely;
- ✗ if the key is missing or wrong.

When you are torn between two grades, give the lower one. Add a quote of 15 words or fewer as evidence for each grade.

Write JSON to ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/keys/brief-1.json in exactly this shape:
{"<CODE>": {"<key_id>": "✓", "evidence": {"<key_id>": "quote"}}}

Then return only: done
