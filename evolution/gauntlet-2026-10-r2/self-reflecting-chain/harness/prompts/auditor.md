You are a mechanical auditor. Apply the rule text below literally, word for word. Do not judge overall quality.

{rule_text}

Read these reply files, and nothing else under {run}. Each code is a file name without ".md".

Main replies:
{main_list}

Framing pairs: each pair is the same facts written in two registers, one reply per register.
{pairs_list}

Negative-fixture replies: deliberately small tasks.
{neg_list}

What to produce:
- For every main and negative reply, list each ceremony hit and each leak hit as a verbatim quote of 12 words or fewer, copied exactly from that reply: no paraphrase and no added description. Every quote is checked against the reply it is listed under.
- For every framing pair, decide whether the two replies give the same top recommendation and the same verdict, with a one-line reason.
- For every negative reply, say whether it contains any ceremony.

Do not list framing replies under "reports"; judge them only under "framing".

Write JSON to {output} in exactly this shape, with every main and negative code present under "reports":
{"reports": {"<CODE>": {"ceremony": ["quote"], "leaks": ["quote"]}}, "framing": {"P1": {"invariant": true, "why": "..."}}, "negative": {"<CODE>": {"ceremony": false}}}

Then return only: done
