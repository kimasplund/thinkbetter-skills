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

Read these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol. Each code is a file name without ".md".

Replies:
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/O0K.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/Q0P.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/U3G.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/Y4M.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/W3U.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/B8F.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/F5J.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/V5Y.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/B3A.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/R0A.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/J5P.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/K8H.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/C2A.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/R0J.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/Q6M.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/F5R.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/A8H.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/G8Y.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/L8Q.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/G3I.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/R3J.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/V7O.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/W9A.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/blind/N0W.md

What to produce: for every reply, list each ceremony hit and each leak hit as a verbatim quote of 12 words or fewer, copied exactly from that reply: no paraphrase and no added description. Every quote is checked against the reply it is listed under.

Write JSON to ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/reasoning-handover-protocol/audit/audit.json in exactly this shape, with every code present under "reports":
{"reports": {"<CODE>": {"ceremony": ["quote"], "leaks": ["quote"]}}}

Then return only: done
