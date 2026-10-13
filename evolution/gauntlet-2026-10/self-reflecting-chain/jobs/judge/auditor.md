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

Read these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain. Each code is a file name without ".md".

Main replies:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/C1P.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/X1P.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/W0S.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/A9R.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/L6X.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/N3G.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/H3L.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/C3C.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/J5K.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/J7C.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/F8P.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/F1Z.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/Y0R.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/Q2K.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/Z4D.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/X4M.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/M2M.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/M9Z.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/K6Z.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/S7V.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/T9Q.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/D3M.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/S4Y.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/E5C.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/I3O.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/L8B.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/E0J.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/H9O.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/L7X.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/Z8I.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/N0U.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/H2K.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/L5Y.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/S5L.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/Y1E.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/W1R.md

Framing pairs: each pair is the same facts written in two registers, one reply per register.
- P1: ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/H2W.md and ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/V3U.md
- P2: ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/Y9E.md and ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/M0K.md

Negative-fixture replies: deliberately small tasks.
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/A4B.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/X1J.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/blind/S5C.md

What to produce:
- For every main and negative reply, list each ceremony hit and each leak hit as a short quote of 12 words or fewer.
- For every framing pair, decide whether the two replies give the same top recommendation and the same verdict, with a one-line reason.
- For every negative reply, say whether it contains any ceremony.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/audit/audit.json in exactly this shape, with every main and negative code present under "reports":
{"reports": {"<CODE>": {"ceremony": ["quote"], "leaks": ["quote"]}}, "framing": {"P1": {"invariant": true, "why": "..."}}, "negative": {"<CODE>": {"ceremony": false}}}

Then return only: done
