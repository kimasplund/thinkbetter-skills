You are a mechanical auditor. Apply the rule text below literally, word for word. Do not judge overall quality.

{rule_text}

Read these reply files, and nothing else under {run}. Each code is a file name without ".md".

Replies:
{main_list}

What to produce: for every reply, list each ceremony hit and each leak hit as a verbatim quote of 12 words or fewer, copied exactly from that reply: no paraphrase and no added description. Every quote is checked against the reply it is listed under.

Write JSON to {output} in exactly this shape, with every code present under "reports":
{"reports": {"<CODE>": {"ceremony": ["quote"], "leaks": ["quote"]}}}

Then return only: done
