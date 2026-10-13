You are a mechanical auditor. Apply the rule text below literally, word for word. Do not judge overall quality.

**Auditor rule text (quoted verbatim to the auditor):**
- **Ceremony:** a ceremony hit is any of the following, in a reply's user-facing text:
  - a section that restates the question;
  - a heading or label that describes the method rather than the content;
  - a summary that repeats earlier sections without adding information;
  - a template field left in place with nothing new in it;
  - a decision-record or report scaffold on a task that needed a direct answer.
- **Leak:** a leak hit is any of the following:
  - the name of a reasoning method, framework or skill (for example "tree of thoughts", "breadth-of-thought", "dialectical", "premortem", "hypothesis elimination");
  - an acronym for one;
  - internal scoring schemes, rating tables or confidence arithmetic shown to the user (a plain statement of how confident the reply is, in words or a single figure, is calibration and is not a leak);
  - numbering of the method's own stages or phases.

  Headings about the user's content are not leaks.

Read these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol. Each code is a file name without ".md".

Main replies:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/U5O.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/C8D.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/R6X.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/J0O.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/V2S.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/G3U.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/H5E.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/B8D.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/T5A.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/T4S.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/A5N.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/P2L.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/I8O.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/A0M.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/A6N.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/X4C.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/I5Q.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/R8Y.md

Framing pairs: each pair is the same facts written in two registers, one reply per register.
- P1: ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/H2H.md and ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/Q8U.md
- P2: ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/Z7M.md and ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/N0M.md

Negative-fixture replies: deliberately small tasks.
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/T1Z.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/I5G.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/blind/K5J.md

What to produce:
- For every main and negative reply, list each ceremony hit and each leak hit as a short quote of 12 words or fewer.
- For every framing pair, decide whether the two replies give the same top recommendation and the same verdict, with a one-line reason.
- For every negative reply, say whether it contains any ceremony.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/audit/audit.json in exactly this shape, with every main and negative code present under "reports":
{"reports": {"<CODE>": {"ceremony": ["quote"], "leaks": ["quote"]}}, "framing": {"P1": {"invariant": true, "why": "..."}}, "negative": {"<CODE>": {"ceremony": false}}}

Then return only: done
