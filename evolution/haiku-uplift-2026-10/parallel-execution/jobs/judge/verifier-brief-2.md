You are a strict key verifier.

Read the user's request at ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/parallel-execution/inputs/brief-2.md, then these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/parallel-execution:
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/parallel-execution/blind/L9S.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/parallel-execution/blind/A8R.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/parallel-execution/blind/P7W.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/parallel-execution/blind/E4F.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/parallel-execution/blind/L6Z.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/parallel-execution/blind/E3F.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/parallel-execution/blind/F3J.md
- ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/parallel-execution/blind/Z0E.md

Each code is a file name without ".md". Below are the sealed keys: things a strong reply must catch. Never reproduce them anywhere except in your output file.

- k1: The ORM upgrade (task 3) silently interacts with the money conversion (task 1) and the backfill (task 4). In v5, numeric columns come back as strings, so code written and tested in the task 1 or task 4 worktree against v4 numbers will pass CI there and break after merging (string concatenation, lexical comparison, NaN). A strong reply sequences the ORM upgrade first or tells tasks 1 and 4 to target v5 string semantics explicitly. It does not assume that different packages means independent work.
- k2: The backfill (task 4) must use the same half-to-even rounding helper that task 1 introduces. Historical values such as 18.3350 and 7.1250 are exact ties, so a backfill using Math.round or its own rounding produces amounts a cent off from what the live code computes, which breaks the auditor-approved rule. A strong reply makes task 4 depend on task 1's shared rounding function, or defines that function before fan-out.
- k3: The migration order destroys data. Converting quotes.amount from numeric(12,4) to bigint in place casts 18.3350 to 18 and loses the minor units before a backfill that runs 'after the column change' can read them. A strong reply requires an expand, backfill, contract sequence (add a new minor-units column, backfill it from the old numeric column, then switch over and drop the old column), or makes the conversion itself multiply by 100 with half-even rounding inside the migration.
- k4: Tasks 1 and 2 both add a migration, and each worktree will name it 0042. Each branch's CI builds a fresh database from its own migrations and passes, but on Friday the merge produces two 0042 files with undefined ordering. A strong reply reserves migration numbers (or orders them) before fan-out, or makes one task own all the migrations.

For every reply and every key, grade:
- ✓ if the reply clearly identifies the key in substance, with the right implication;
- ~ if it does so only partially or vaguely;
- ✗ if the key is missing or wrong.

When you are torn between two grades, give the lower one. Add a quote of 15 words or fewer as evidence for each grade.

Write JSON to ~/projects/thinkbetter-skills/evolution/haiku-uplift-2026-10/parallel-execution/keys/brief-2.json in exactly this shape:
{"<CODE>": {"<key_id>": "✓", "evidence": {"<key_id>": "quote"}}}

Then return only: done
