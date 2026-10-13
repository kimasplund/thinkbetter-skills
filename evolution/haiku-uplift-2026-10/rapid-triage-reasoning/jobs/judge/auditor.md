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

Read these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning. Each code is a file name without ".md".

Replies:
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/C0S.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/A8D.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/W1B.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/N4V.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/R3O.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/C0P.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/K3B.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/E0L.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/Y8Z.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/L1B.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/Q3T.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/F4E.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/Q9D.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/K3C.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/U8X.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/M8R.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/A9M.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/R1T.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/J6G.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/F3Q.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/G0N.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/H5Y.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/H3O.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/blind/A1G.md

What to produce: for every reply, list each ceremony hit and each leak hit as a verbatim quote of 12 words or fewer, copied exactly from that reply: no paraphrase and no added description. Every quote is checked against the reply it is listed under.

Write JSON to ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/rapid-triage-reasoning/audit/audit.json in exactly this shape, with every code present under "reports":
{"reports": {"<CODE>": {"ceremony": ["quote"], "leaks": ["quote"]}}}

Then return only: done
