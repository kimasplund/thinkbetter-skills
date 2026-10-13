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
  - internal scoring or confidence arithmetic shown to the user;
  - numbering of the method's own stages or phases.

  Headings about the user's content are not leaks.

Read these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination. Each code is a file name without ".md".

Main replies:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/Z5V.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/X7W.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/R1W.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/P0Y.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/L1K.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/J5O.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/F2Q.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/W6Z.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/S6C.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/Y3E.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/P9I.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/N2A.md

Framing pairs: each pair is the same facts written in two registers, one reply per register.
- P1: ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/L0J.md and ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/Q6K.md

Negative-fixture replies: deliberately small tasks.
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/B9Q.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/blind/M0C.md

What to produce:
- For every main and negative reply, list each ceremony hit and each leak hit as a short quote of 12 words or fewer.
- For every framing pair, decide whether the two replies give the same top recommendation and the same verdict, with a one-line reason.
- For every negative reply, say whether it contains any ceremony.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/audit/audit.json in exactly this shape, with every main and negative code present under "reports":
{"reports": {"<CODE>": {"ceremony": ["quote"], "leaks": ["quote"]}}, "framing": {"P1": {"invariant": true, "why": "..."}}, "negative": {"<CODE>": {"ceremony": false}}}

Then return only: done
