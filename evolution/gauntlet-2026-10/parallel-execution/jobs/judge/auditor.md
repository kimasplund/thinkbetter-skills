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

Read these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution. Each code is a file name without ".md".

Main replies:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/J5U.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/C3X.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/M4J.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/A2V.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/P6E.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/I2X.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/P6Z.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/I0J.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/Y0I.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/Q3S.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/R3S.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/H3U.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/P1Z.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/M9C.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/E2X.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/P2H.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/E0S.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/Q2L.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/L9A.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/C3H.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/N3R.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/V5L.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/H6T.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/C0D.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/Q5J.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/S1U.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/K0T.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/N8O.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/J2U.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/O4R.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/L7C.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/J3I.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/T9W.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/L6T.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/E0N.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/Q9R.md

Framing pairs: each pair is the same facts written in two registers, one reply per register.
- P1: ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/N7E.md and ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/Y7M.md
- P2: ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/L1V.md and ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/E4C.md

Negative-fixture replies: deliberately small tasks.
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/Y5V.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/H1D.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/Y5D.md

What to produce:
- For every main and negative reply, list each ceremony hit and each leak hit as a short quote of 12 words or fewer.
- For every framing pair, decide whether the two replies give the same top recommendation and the same verdict, with a one-line reason.
- For every negative reply, say whether it contains any ceremony.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/audit/audit.json in exactly this shape, with every main and negative code present under "reports":
{"reports": {"<CODE>": {"ceremony": ["quote"], "leaks": ["quote"]}}, "framing": {"P1": {"invariant": true, "why": "..."}}, "negative": {"<CODE>": {"ceremony": false}}}

Then return only: done
