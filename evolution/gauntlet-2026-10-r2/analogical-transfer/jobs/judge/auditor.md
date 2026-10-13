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

Read these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer. Each code is a file name without ".md".

Main replies:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/J1A.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/T1U.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/W4I.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/T1H.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/C0N.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/B1V.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/R0I.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/C2F.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/I1T.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/P8D.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/M6Q.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/L1I.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/Q0V.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/B5C.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/K9R.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/G7T.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/V9L.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/A0V.md

Framing pairs: each pair is the same facts written in two registers, one reply per register.
- P1: ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/M9G.md and ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/L7O.md
- P2: ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/D7K.md and ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/T7L.md
- P3: ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/I8G.md and ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/G6N.md

Negative-fixture replies: deliberately small tasks.
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/V0K.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/I6R.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/blind/R9V.md

What to produce:
- For every main and negative reply, list each ceremony hit and each leak hit as a verbatim quote of 12 words or fewer, copied exactly from that reply: no paraphrase and no added description. Every quote is checked against the reply it is listed under.
- For every framing pair, decide whether the two replies give the same top recommendation and the same verdict, with a one-line reason.
- For every negative reply, say whether it contains any ceremony.

Do not list framing replies under "reports"; judge them only under "framing".

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r2/analogical-transfer/audit/audit.json in exactly this shape, with every main and negative code present under "reports":
{"reports": {"<CODE>": {"ceremony": ["quote"], "leaks": ["quote"]}}, "framing": {"P1": {"invariant": true, "why": "..."}}, "negative": {"<CODE>": {"ceremony": false}}}

Then return only: done
