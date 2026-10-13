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

Read these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework. Each code is a file name without ".md".

Main replies:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/V7E.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/H7A.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/I8Y.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/P8A.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/N0D.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/Z0Y.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/H7T.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/V5F.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/L9V.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/S4P.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/N3E.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/T7C.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/T5P.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/T0A.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/L6A.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/K0B.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/Y8N.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/A5V.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/F8T.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/M2C.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/C1A.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/H0C.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/J8F.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/G8J.md

Framing pairs: each pair is the same facts written in two registers, one reply per register.
- P1: ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/W2A.md and ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/M2T.md

Negative-fixture replies: deliberately small tasks.
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/A2I.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/blind/V3I.md

What to produce:
- For every main and negative reply, list each ceremony hit and each leak hit as a short quote of 12 words or fewer.
- For every framing pair, decide whether the two replies give the same top recommendation and the same verdict, with a one-line reason.
- For every negative reply, say whether it contains any ceremony.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/negotiated-decision-framework/audit/audit.json in exactly this shape, with every main and negative code present under "reports":
{"reports": {"<CODE>": {"ceremony": ["quote"], "leaks": ["quote"]}}, "framing": {"P1": {"invariant": true, "why": "..."}}, "negative": {"<CODE>": {"ceremony": false}}}

Then return only: done
