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

Read these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning. Each code is a file name without ".md".

Main replies:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/Y1T.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/S1S.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/Q3C.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/M0I.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/F2E.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/M1L.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/L0S.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/M4Z.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/C4F.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/H9Z.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/P5I.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/E2V.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/M1S.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/C5N.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/Z6X.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/C3U.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/K9D.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/B0N.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/E6Z.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/W0J.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/I9A.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/C7S.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/Y3U.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/E6E.md

Framing pairs: each pair is the same facts written in two registers, one reply per register.
- P1: ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/M5W.md and ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/S2N.md

Negative-fixture replies: deliberately small tasks.
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/A3V.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/blind/C3N.md

What to produce:
- For every main and negative reply, list each ceremony hit and each leak hit as a short quote of 12 words or fewer.
- For every framing pair, decide whether the two replies give the same top recommendation and the same verdict, with a one-line reason.
- For every negative reply, say whether it contains any ceremony.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/audit/audit.json in exactly this shape, with every main and negative code present under "reports":
{"reports": {"<CODE>": {"ceremony": ["quote"], "leaks": ["quote"]}}, "framing": {"P1": {"invariant": true, "why": "..."}}, "negative": {"<CODE>": {"ceremony": false}}}

Then return only: done
