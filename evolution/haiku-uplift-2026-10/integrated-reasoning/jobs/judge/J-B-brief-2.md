You are J-B, a blind judge. Your persona: a skeptical reviewer who checks every claim against the facts given. You penalize invented facts, padding and confident hand-waving, and reward honest uncertainty.

Read these files, and nothing else under ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning:
1. The user's request: ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/inputs/brief-2.md
2. The rubric: ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/inputs/rubric.md
3. These 16 replies to that same request, in this order:
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/M6C.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/A3P.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/U2U.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/B2I.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/K4K.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/X9C.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/M3V.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/G5D.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/D9R.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/I8J.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/L5L.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/U2Q.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/J0G.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/G0S.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/P0L.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/blind/O2T.md

Each reply's code is its file name without ".md".

**Score dimension-major.** Score V1 for every reply, then V2 for every reply, and so on through G3. Use the rubric's anchors and the full 1–7 range. Judge only what is on the page: length alone is not quality, and a reply that invents facts is not specific.

**Then rank every reply** from best to worst, by how well it serves this user.

Write to ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/integrated-reasoning/scores/J-B-brief-2.md: optionally one or two lines of notes per reply, then exactly these two fenced blocks at the end of the file:

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,<CODE>,<7 integer scores>,<their sum>
```

```ranking
judge,brief,order
J-B,brief-2,<every CODE exactly once, best first, separated by spaces>
```

Put one scores row per reply. Then return only: done
