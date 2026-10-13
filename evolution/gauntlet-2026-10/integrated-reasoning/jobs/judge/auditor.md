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

Read these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning. Each code is a file name without ".md".

Main replies:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/T4P.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/V6K.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/N8J.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/I9X.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/B4J.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/B9E.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/L8W.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/C8X.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/D3S.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/J2J.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/Y5O.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/P6F.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/Z0T.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/G1K.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/X5P.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/D1D.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/K5G.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/J8J.md

Framing pairs: each pair is the same facts written in two registers, one reply per register.
- P1: ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/T3T.md and ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/L3U.md
- P2: ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/N0S.md and ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/Y0D.md

Negative-fixture replies: deliberately small tasks.
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/C1F.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/Y9R.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/blind/L0R.md

What to produce:
- For every main and negative reply, list each ceremony hit and each leak hit as a short quote of 12 words or fewer.
- For every framing pair, decide whether the two replies give the same top recommendation and the same verdict, with a one-line reason.
- For every negative reply, say whether it contains any ceremony.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/audit/audit.json in exactly this shape, with every main and negative code present under "reports":
{"reports": {"<CODE>": {"ceremony": ["quote"], "leaks": ["quote"]}}, "framing": {"P1": {"invariant": true, "why": "..."}}, "negative": {"<CODE>": {"ceremony": false}}}

Then return only: done
