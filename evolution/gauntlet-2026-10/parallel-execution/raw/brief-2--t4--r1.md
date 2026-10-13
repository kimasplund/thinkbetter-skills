Don't run all four fully in parallel and expect a clean merge. The packages are different, but the work is coupled in five places. Below is a way to keep four agents running and a merge plan that survives Friday.

## Where the four tasks collide

1. **Migration numbers.** Tasks 1 and 2 both need migration 0042, and Task 4 may need one too. Git won't flag the clash because the filenames differ, but the numbering breaks. Each branch's CI builds a fresh database from its own migrations, so every branch would pass alone and fail once merged.
2. **Money's shape.** Task 2 reads amounts through the pricing package. If pricing changes `Money` to `{ minor, currency }` and billing is written against the old `number`, billing breaks the moment they merge. Billing needs the new type from day one.
3. **Kestrel 5 returns decimals as strings.** This hits Tasks 1, 2 and 4. After the upgrade, `quotes.amount` (numeric) arrives as `"18.3350"`. Pricing code that does `amount * 100` would silently coerce. Check whether `bigint` also comes back as a string, since many Postgres drivers do that to avoid precision loss. Do that check before anyone writes parsing code.
4. **Task 4 can't be tested on its own.** The backfill runs after the column change, but CI builds from each branch's migrations. On its own branch, the backfill has no new column to run against.
5. **Task 1 changes the data as well as the type.** Altering `numeric(12,4)` to `bigint` in place would silently round 3.1M rows, and with Postgres's default rounding that isn't half-to-even. The backfill would then have nothing left to convert. Pick one path for the data (see "Decisions to make first").

## Rounding

Finance requires half-to-even. Replacing `Math.round` doesn't achieve that by itself, because `Math.round` is half-up, so the tie cases come out wrong.

- Your own data shows the tie case. 18.3350 at 2 decimals is a tie, and half-to-even gives 18.34 because 4 is even. 7.1250 gives 7.12, because 2 is even. Half-up gives 7.13 for the second.
- Never do this in floats. 18.335 isn't exactly representable, so a float can land on either side of the tie. Parse the string or decimal value and round with integer or decimal arithmetic.
- Postgres `round(numeric, n)` rounds half away from zero, not half-to-even. A plain `USING round(amount * 100)::bigint` in SQL gets the ties wrong. Either do the rounding in the script with a tested half-to-even function, or write the SQL explicitly.
- Not every currency has 2 minor units (EUR and DKK do, but JPY has 0 and KWD has 3). Look up the exponent per currency instead of hardcoding 100.

## Decisions to make first (Monday, before agents start)

- **Data migration strategy.** I recommend expand and contract. Migration 0042 adds a nullable `amount_minor bigint` and a `currency` column on `quotes`. The backfill fills it in batches. A later migration (after the backfill is verified) makes it NOT NULL and drops or retires `amount`. This is safer for 3.1M rows than an in-place type change, which takes a heavy lock and rewrites the table. It also gives Task 4 something to run against.
- **Currency of historical quotes.** Which currency are the existing quotes in? If it's all EUR before Denmark, the backfill sets `currency='EUR'`. If not, Task 4 needs a source for it.
- **Migration numbers, reserved up front.** 0042 is pricing (add `amount_minor` and `currency` on quotes). 0043 is billing (`invoices.currency`). 0044 is reserved for the finalize step (NOT NULL and drop).
- **The shared Money contract**, a small file of types and helpers that all agents get (see Step 0).
- **Rollout order.** The backfill touches production data, so a dry run on a production-sized copy needs to be in the plan.

## Step 0: a shared base branch (about half a day, done by one person)

Create `integration` from main containing only:

- the `Money` type and a `roundHalfEven` helper with tests covering 18.3350, 7.1250, 0.005, negatives, and a tie in each direction
- a currency exponent table (EUR 2, DKK 2, and so on)
- the reserved migration numbers, noted in the README
- one shared helper that parses Kestrel's decimal strings, so no agent writes their own

Every agent branches from `integration`, not from main. This removes collisions 1 and 2 and most of 3.

## Waves

- **Wave 1 (parallel):** Agent A (Kestrel upgrade) and Agent B (pricing and migration 0042). Kestrel touches everything, so merge it first, and pricing is the foundation for the others.
- **Wave 2 (parallel, branching from wave 1 merged):** Agent C (billing) and Agent D (backfill).

If you must start all four on day one, Agents C and D can start against the Step 0 contract but must rebase onto the merged wave 1 before their final test run. Don't count on them being merge-ready until then.

## The four agent prompts

Give every agent this common header:

> Repo: Larkspur dispatch platform, TypeScript monorepo, Postgres, Kestrel ORM. Work in your own git worktree on a branch from `integration`. Do not edit files outside your listed scope. If you need a change outside it, write it in `HANDOFF.md` at your worktree root and stop on that item. Money rules: money is `{ minor: number; currency: string }`, in integer minor units. All rounding is half-to-even using `roundHalfEven` from the shared helper, never `Math.round`. Never use floating-point arithmetic on amounts. Database numeric/decimal values may arrive as strings; parse them with the shared parse helper. Migrations are numbered sequentially: use only the number assigned to you. CI builds a fresh database from your branch's migrations, so your tests must pass from scratch. Finish by listing the files changed, the tests added, any assumptions, and anything you could not verify.

**Agent A: Kestrel 4.x to 5.x**
> Scope: dependency versions and ORM call sites across the repo, with mechanical changes only. No behavior changes to business logic. First, read the 5.x changelog fully and list every breaking change, not just the headline. Confirm in a test against a real Postgres what types Kestrel 5 returns for numeric(12,4), bigint and numeric columns, and record that in `HANDOFF.md`. Wherever code reads a numeric/decimal column and does arithmetic, convert through the shared parse helper, and add a test that fails if a string reaches arithmetic. Do not change the `Money` type or pricing logic beyond this. Done when every package's tests pass on a fresh database.

**Agent B: pricing, integer minor units**
> Scope: packages/pricing and `db/migrations/0042_*`. Change `Money` usage to `{ minor, currency }`. Replace every `Math.round` with `roundHalfEven` and add tests, including ties (18.3350 to 18.34, 7.1250 to 7.12, plus negatives). Migration 0042 adds nullable `quotes.amount_minor bigint` and `quotes.currency` (do not alter or drop `amount`). Do not convert existing rows; that is the backfill's job. Quote creation writes both `amount` and `amount_minor` so old and new readers agree during rollout. Export a stable public API (`Money`, constructors, formatters) and document it in `HANDOFF.md`, since billing depends on it. Done when pricing tests pass on a fresh database.

**Agent C: billing multi-currency PDFs (starts after B's API is merged or stable)**
> Scope: apps/billing and `db/migrations/0043_*`. Add `invoices.currency` (NOT NULL with a default of 'EUR' for existing rows, which assumes all existing invoices are EUR; flag this in `HANDOFF.md`). Read all amounts through the pricing package's `Money` only; do no money arithmetic locally. PDF formatting must use the currency's exponent and locale rules for EUR and DKK (Danish formatting uses a comma decimal and a period thousands separator). Add tests for both currencies, including a rounding tie. Do not modify packages/pricing.

**Agent D: backfill script**
> Scope: scripts/backfill only. Write a one-off, idempotent, resumable script that fills `quotes.amount_minor` and `quotes.currency` from `amount` for the roughly 3.1M historical rows. Process in primary-key batches (for example 10,000 rows), each in its own transaction, only rows where `amount_minor IS NULL`, so it can be stopped and restarted safely. Read `amount` as a string and convert with exact decimal math and `roundHalfEven`, using the currency exponent. Never go through a JS float. Support `--dry-run`, which writes nothing and reports counts, how many rows needed rounding, and the first 20 tie cases. After a real run, verify: zero rows with NULL `amount_minor`, and a sampled check that `amount_minor` equals the expected value for known ties (18.3350 to 1834, 7.1250 to 712). Log progress. Test against a fixture table that includes the tie rows and rows with four-decimal values.

## Merge plan for Friday

1. **Thursday, freeze.** Each agent stops and posts its `HANDOFF.md`. Review the handoffs for scope violations before merging anything.
2. **Merge order into `integration`:** Kestrel (A), then pricing (B), then billing (C), then backfill (D). After each merge, rebuild a fresh database from all migrations and run the full test suite. Fix on the spot rather than stacking merges.
3. **Check migration numbers.** Confirm the sequence is 0041, 0042, 0043 with no gaps or duplicates. A quick `ls db/migrations` check as a CI step is worth adding.
4. **Check the cross-cutting rules** with a repo-wide search: no `Math.round` on money, no `parseFloat` or `Number(` applied to decimal columns, no arithmetic on a value that might be a string.
5. **Rehearse the backfill** on a restored production-sized copy: dry run, then a real run, then the verification queries. Record the duration so you can plan the production window.
6. **Production order:** deploy migration 0042 and the new code (which dual-writes), run the backfill, verify, then ship the finalize migration (0044) separately, not on Friday. Only after that does anything read `amount_minor` exclusively.
7. **Rollback:** because `amount` is kept until 0044, rolling back the code needs no data restore. Don't drop `amount` in the same release.

## What could still go wrong

- Kestrel 5 may change other things beyond decimals (query builder, transactions, date handling). Agent A's job is to find these, so give them time to do it.
- Decide who owns the rounding policy for the four-decimal partner rate cards (rounding at the line level versus the invoice total can differ by a cent).
- The assumption that existing quotes and invoices are EUR is mine. If it's wrong, Agents B, C and D each need the true source.
- Five people reviewing four branches in one day is tight. If you can, review each branch as it lands instead of all on Friday.
