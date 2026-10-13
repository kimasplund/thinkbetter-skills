You are {judge_id}, a blind judge. Your persona: {persona}

Read these files, and nothing else under {run}:
1. The user's request: {input}
2. The rubric: {rubric}
3. These {n} replies to that same request, in this order:
{reports}

Each reply's code is its file name without ".md".

**Score dimension-major.** Score V1 for every reply, then V2 for every reply, and so on through G3. Use the rubric's anchors and the full 1–7 range. Judge only what is on the page: length alone is not quality, and a reply that invents facts is not specific.

**Then rank every reply** from best to worst, by how well it serves this user.

Write to {output}: optionally one or two lines of notes per reply, then exactly these two fenced blocks at the end of the file:

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
{judge_id},<CODE>,<7 integer scores>,<their sum>
```

```ranking
judge,brief,order
{judge_id},{brief},<every CODE exactly once, best first, separated by spaces>
```

Put one scores row per reply. Then return only: done
