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

Read these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework. Each code is a file name without ".md".

Replies:
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/B9F.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/T0F.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/N8I.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/C3Z.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/A5K.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/D3L.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/M8Q.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/A1H.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/H0A.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/C6Y.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/Y3M.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/V2A.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/D1J.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/C4G.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/G5M.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/E5N.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/Y7R.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/R7A.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/J6J.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/W8N.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/C3I.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/Y0G.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/N7W.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/blind/P4Y.md

What to produce: for every reply, list each ceremony hit and each leak hit as a verbatim quote of 12 words or fewer, copied exactly from that reply: no paraphrase and no added description. Every quote is checked against the reply it is listed under.

Write JSON to ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/negotiated-decision-framework/audit/audit.json in exactly this shape, with every code present under "reports":
{"reports": {"<CODE>": {"ceremony": ["quote"], "leaks": ["quote"]}}}

Then return only: done
