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

Read these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain. Each code is a file name without ".md".

Main replies:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/U7K.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/H7Q.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/A5T.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/D7L.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/K4S.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/V9D.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/G4Z.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/Q2U.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/O4F.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/I0A.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/D4F.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/B7R.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/U9L.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/A1P.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/C2I.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/I6I.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/D9V.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/B9B.md

Framing pairs: each pair is the same facts written in two registers, one reply per register.
- P1: ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/S1L.md and ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/B6X.md
- P2: ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/F0K.md and ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/K0M.md
- P3: ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/K2O.md and ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/J0P.md

Negative-fixture replies: deliberately small tasks.
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/N8Z.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/J8P.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/blind/V3C.md

What to produce:
- For every main and negative reply, list each ceremony hit and each leak hit as a verbatim quote of 12 words or fewer, copied exactly from that reply: no paraphrase and no added description. Every quote is checked against the reply it is listed under.
- For every framing pair, decide whether the two replies give the same top recommendation and the same verdict, with a one-line reason.
- For every negative reply, say whether it contains any ceremony.

Do not list framing replies under "reports"; judge them only under "framing".

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10-r3/self-reflecting-chain/audit/audit.json in exactly this shape, with every main and negative code present under "reports":
{"reports": {"<CODE>": {"ceremony": ["quote"], "leaks": ["quote"]}}, "framing": {"P1": {"invariant": true, "why": "..."}}, "negative": {"<CODE>": {"ceremony": false}}}

Then return only: done
