I'd change the plan before launching, because these four tasks will not merge cleanly. Below are the problems, a revised structure, the four prompts and the Friday merge plan.

## Why the merge won't be clean

1. **Task 4 contradicts task 1.** Task 1's migration turns `quotes.amount` into bigint. Postgres would cast the existing values in place and round them, so 18.3350 and 7.1250 would be rounded by Postgres, not by your half-to-even code. Once that happens the backfill has nothing left to convert. Use expand/contract instead:
   - Migration A adds a nullable `amount_minor bigint` (plus `currency` on quotes, if quotes need one).
   - The backfill script fills it in batches.
   - Migration B, after the backfill is verified, makes it NOT NULL and drops or renames the old column.
   - CI builds from an empty database, so it will never exercise the 3.1M-row path. The backfill needs its own test against seeded awkward values.
2. **Task 3 touches everything.** Kestrel 5 returns numeric columns as strings. That changes the behaviour of pricing, billing and the backfill. It is also a repo-wide change, so it will conflict textually with the other three.
3. **Task 2 depends on task 1.** Billing reads amounts through pricing, and `Money` is changing shape. Billing can't be finished against the old type.
4. **Migration numbers will collide.** Tasks 1, 2 and probably 4 all want 0042. CI builds from the migrations on each branch, so a collision only shows up at merge. Reserve numbers now.
5. **Half-to-even changes real values.** 7.1250 at two decimals is 712.5 minor units. Math.round gives 713 and half-to-even gives 712. 18.3350 is also a tie. In floating point, `18.335 * 100` is not exactly 1833.5, so the result depends on float noise. All conversions must parse the decimal string and round with integer or decimal arithmetic, never multiply floats.
6. **Decisions you need to make first (I've assumed answers):**
   - The 4-decimal rate cards lose precision at 2-decimal minor units. I assumed they round half-to-even to the currency's exponent, with the original value kept in an archive column or table until finance signs off. If quotes need sub-cent precision, minor units are the wrong model.
   - `currency` on historical quotes: I assumed EUR.
   - Currency exponent comes from a table (EUR and DKK are both 2), not a hardcoded 100.
   - JSON and API boundaries need a plan, because `Money` changes from number to object.

## Revised sequencing

Don't run all four in parallel with an unplanned merge. Use a short foundation phase, then parallel work.

- **Day 0, shared contract (one agent or you, about half a day):** merge to main the `Money` type, the half-to-even rounding helper with tests, the currency exponent table, and the reserved migration numbers.
- **Parallel from that base:**
  - Agent A (Kestrel upgrade) goes first and merges first, or at least early. It is the widest change, so everyone else should rebase onto it.
  - Agent B (pricing) and Agent C (billing) run in parallel after the contract merges. C codes against the contract types.
  - Agent D (backfill) writes and tests the script against the expand column.
- **Reserved migrations:** 0042 is the pricing expand (`amount_minor`, quotes `currency`). 0043 is `invoices.currency`. 0044 is the contract step, applied only after the production backfill. The backfill adds no migration.

## Agent prompts

**Shared preamble for all four**
You work in your own git worktree on the Larkspur dispatch monorepo (TypeScript, Postgres, Kestrel ORM). Other agents are changing other packages at the same time. Stay inside your listed paths. If you need a change outside them, write it in `NOTES.md` instead of making it. Use only the migration number assigned to you. All rounding is half-to-even, never `Math.round`. Never convert decimals by multiplying floats. Parse the decimal string and use integer or decimal arithmetic. Run your package tests (CI builds a fresh database from your branch's migrations) before finishing. Finish with a summary of what changed, assumptions made and open questions.

**Agent A: Kestrel 4.x to 5.x**
Paths: dependency manifests and every Kestrel call site in the repo, with minimal edits. Upgrade Kestrel to 5.x. The headline change is that numeric/decimal columns now return strings instead of numbers. Find every read of a numeric or decimal column (quotes.amount, invoice amounts, anything else) and make it explicit, using a small shared `parseDecimal` helper that returns a string or decimal and never a float. Do not change `Money` or the pricing logic. Do not add migrations. Keep the diff small and mechanical so other branches can rebase onto it. Add tests that assert the string behaviour. Deliverable: a list of every numeric-column call site you touched.

**Agent B: pricing, integer minor units**
Paths: packages/pricing, migration 0042. Change `Money` to `{ minor: number; currency: string }`, using the shared contract. Replace all float arithmetic and every `Math.round` with the half-to-even helper. Use the currency exponent table, not a hardcoded 100. Write migration 0042 to add `quotes.amount_minor bigint NULL` and `quotes.currency text`. Do not drop or alter `quotes.amount`, because the backfill needs the original 4-decimal values. Dual-read during the transition: use `amount_minor` when set, otherwise convert from `amount` with the same rounding. Tests must cover the tie cases 7.1250 (712 in minor units for a 2-exponent currency) and 18.3350 (1834), plus negatives and zero. Do not touch apps/billing. Export a stable API that billing can consume.

**Agent C: billing, multi-currency invoice PDFs**
Paths: apps/billing, migration 0043. Add `invoices.currency` (NOT NULL, default 'EUR' for existing rows) in migration 0043. Render invoice PDFs in EUR and DKK with correct formatting (DKK uses a comma decimal and the "kr." symbol or ISO code per the locale; make the locale explicit and tested). Read amounts only through the pricing package's `Money` API. Until pricing merges, code against the contract types and stub with a local test double. Never do arithmetic on amounts in billing. Tests: snapshot PDFs or rendered text for EUR and DKK, and a case where an invoice's currency differs from the default.

**Agent D: backfill script**
Paths: scripts/backfill only. Write an idempotent, resumable script that fills `quotes.amount_minor` and `quotes.currency` (EUR) from `quotes.amount` for roughly 3.1M rows. Process in keyset-paginated batches by primary key, each in its own transaction. Support `--dry-run` and `--batch-size`, log progress, and be safe to rerun (only touch rows where `amount_minor IS NULL`). Parse `amount` as a string (Kestrel 5 returns strings) and round half-to-even to the currency exponent. Use the shared rounding helper, not floats. Record rows whose rounding was lossy (more than the currency exponent in significant decimals) to a report file, because finance needs these. Add a verification mode that checks counts and confirms no NULLs remain. Tests with seeded values: 18.3350, 7.1250, 0.0050, 0.0000, negatives, and a large value. Do not write a migration.

## Friday merge plan

1. **Thursday, freeze and rehearse.** Create an integration branch off main. Have a human read each agent's `NOTES.md` for cross-boundary requests.
2. **Merge order**, running the full test suite and a fresh-database migration build after each step:
   1. Contract, if not already on main.
   2. Agent A (Kestrel). Rebase B, C and D onto it, then fix any string-vs-number fallout.
   3. Agent B (pricing, 0042).
   4. Agent C (billing, 0043). Replace its test double with the real pricing API.
   5. Agent D (backfill).
3. **Checks on the integration branch:**
   - Migrations are sequential with no gaps or duplicates (0042 and 0043 only).
   - `grep` shows no `Math.round` left in money paths and no float multiplication on amounts.
   - The tie cases give half-even results end to end.
   - A rehearsal of the backfill on a restored copy of production or a large seeded table. Check the runtime, the lossy-row report and the NULL count.
4. **Deploy order.** Ship the expand migrations and the code that dual-reads. Run the backfill and verify it. Then ship migration 0044 (NOT NULL and drop or rename the old column) in a later release, so rollback stays possible.
5. **Rollback.** The expand step is additive and safe to leave in place. Keep the old `amount` column until finance has accepted the lossy report.

## Things to confirm with finance and the team

- Is rounding the 4-decimal rate cards to 2 decimals acceptable? Otherwise the design needs a different precision.
- Should the Denmark launch use DKK display only, or also DKK-priced quotes?
- Is half-to-even applied at conversion time as well as in future arithmetic? I've assumed both.
