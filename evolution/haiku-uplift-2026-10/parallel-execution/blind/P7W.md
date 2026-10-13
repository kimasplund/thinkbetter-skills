I wrote the four prompts and a merge plan, but I wouldn't expect a clean merge as the work is currently split. The packages differ, but the four tasks depend on each other through the Money type, the quotes column, the Kestrel numeric behavior and the migration numbers. Here is what I'd change first, then the prompts.

## Where the four tasks collide

1. **Task 1's migration and task 4's backfill both convert the data.** If the migration alters `quotes.amount` from numeric(12,4) to bigint, Postgres does the cast itself. It rounds half away from zero, and it keeps the integer part of a value like 18.3350 as 18 unless you multiply first. The backfill then has nothing left to convert. It would also run an `ALTER ... TYPE` that rewrites and locks 3.1M rows.
   - Use expand/contract instead. Migration 0042 adds `quotes.amount_minor bigint NULL` and `quotes.currency text`. The backfill fills them in batches. A later migration (after the backfill has run in production) sets NOT NULL and drops or renames the old column.
   - The "convert amount to bigint" migration then splits into an additive one now and a destructive one after the backfill.
2. **Migration numbers.** Tasks 1 and 2 both need a migration, and probably 3 and 4 do too. All four branches would create `0042_*`. Reserve numbers up front:
   - 0042: task 1, quotes `amount_minor` and `currency`
   - 0043: task 2, `invoices.currency`
   - 0044: reserved for the contract step (NOT NULL and drop old), merged only after the backfill has run
   - If task 3 needs a migration, it takes 0045.
   - CI builds a fresh DB from each branch's migrations, so each branch will pass alone. Gaps and duplicates will only show up after the merge, so add a CI check for duplicate or non-sequential numbers on the integration branch.
3. **Task 2 depends on task 1's `Money` type.** Billing reads amounts through the pricing package, so it either codes against the old `number` or against a type that doesn't exist yet. Agree the interface now: a small `Money` contract (`{ minor: number; currency: string }`, plus `fromDecimalString`, `toDecimalString`, `add`, `multiply(rate)` and `round`). Land that contract first, even as a stub, and have tasks 2 and 4 import it.
4. **Task 3 touches the repo broadly and changes numeric reads.** Kestrel 5 returns numeric/decimal as strings. That is a runtime change that type-checks in many places and breaks silently (`"18.3350" + 1` is `"18.33501"`). It overlaps with every package that reads quotes or invoices, including the code in tasks 1, 2 and 4. Do it first, or at least land it early on its own, so the others rebase onto it. Also note that bigint (int8) comes back from `pg` as a string by default, which matters for task 1.
5. **Rounding.** Finance wants half-to-even and the code uses `Math.round` everywhere. Whoever does task 1 owns this, but tasks 2 and 4 must call the shared helper and not write their own rounding.
   - Do not do half-to-even on floats. 18.335 × 100 is not exactly 1833.5 in binary floating point. Parse the decimal string into integer minor units with string or bigint arithmetic and decide ties there.
   - The historical data has real ties. 18.3350 to 2 decimals is a tie, so half-to-even gives 18.34. 7.1250 is also a tie, so half-to-even gives 7.12, where `Math.round` gave 7.13. The backfill will therefore differ from old behavior on some rows. Get finance to confirm that is intended, and have the backfill log every row where the result differs from `Math.round`.
6. **Minor-unit exponent.** EUR and DKK both use 2 decimals, so the scale is 100. Don't hardcode it. Put an exponent per currency in one table in pricing. Four-decimal rate-card values need an explicit decision: round once, at the conversion, with half-to-even.

## Suggested order

- **Day 0 (before spawning):** you or one person writes the `Money` contract and rounding helper stub, reserves the migration numbers, and decides the expand/contract split. Commit this to `main`, then create the worktrees from that commit.
- **Wave 1 (parallel):** task 3 (Kestrel) and task 1 (pricing and 0042).
- **Wave 2 (parallel, after wave 1 is merged or rebased onto):** task 2 (billing) and task 4 (backfill script).
- If you need all four running at once, accept that tasks 2 and 4 are built against the contract, and expect a rebase after tasks 1 and 3 land.

Doing it this way costs a day of ordering and avoids a Friday of conflicts.

## Agent prompts

All four prompts start with this shared preamble.

> Context: Larkspur Couriers dispatch platform. TypeScript monorepo, Postgres, Kestrel ORM. You are working in your own git worktree on your own branch. Do not edit files outside your listed scope; if you need a change elsewhere, write it up in `HANDOFF.md` at the repo root of your worktree and carry on. Shared decisions: (a) `Money` is `{ minor: number; currency: string }`. (b) Rounding is half-to-even, done on decimal strings or integers, never on floats. (c) Currency exponents come from the single table in `packages/pricing` (EUR 2, DKK 2). (d) Migration numbers are fixed: 0042 task 1, 0043 task 2, 0044 reserved for the contract step, 0045 task 3 if needed. Do not use any other number. (e) Run your package's tests and type-check before finishing, and list anything you could not verify.

**Prompt 1: pricing (packages/pricing)**

> Replace float money with integer minor units in `packages/pricing`. Change `Money` from `number` to `{ minor: number; currency: string }`. Add a currency exponent table and helpers: `fromDecimalString(str, currency)`, `toDecimalString(money)`, `add`, `subtract`, `multiply(money, rate)`. All rounding must be half-to-even, implemented on decimal strings or bigint, and never through float multiplication. Replace every `Math.round` in the package. Add tests for ties, including 18.3350 and 7.1250 at 2 decimals (expect 18.34 and 7.12), negative values, zero, and values with fewer than 4 decimals. Add migration `db/migrations/0042_*` that is additive only: `quotes.amount_minor bigint NULL` and `quotes.currency text NULL`. Do not drop or alter `quotes.amount`. Do not write the backfill. Export the public API from the package index and document the contract in a short README section. Keep the old float API behind a deprecated alias only if other packages need it to compile, and list who uses it in `HANDOFF.md`. Note that Kestrel 5 returns numeric columns as strings, and `pg` returns bigint as a string: parse these with `fromDecimalString`, and do not use `Number()`.

**Prompt 2: billing (apps/billing)**

> Add multi-currency invoice PDFs to `apps/billing` for a Denmark launch (DKK alongside EUR). Add migration `db/migrations/0043_*` adding `invoices.currency text` (backfill existing rows to 'EUR' in the migration, then NOT NULL). Read amounts only through the `Money` type and helpers from `packages/pricing`; if the contract is not merged yet, import against the agreed signature and stub it locally under a clearly marked temporary file. Render amounts with the right formatting per currency and locale (DKK: `1.234,56 kr.` style, EUR as per the invoice locale), using the exponent from the pricing table. Do not do any arithmetic on floats and do not write your own rounding. Add tests for a DKK invoice, an EUR invoice, and rounding on line totals and VAT. Only edit `apps/billing` and your own migration.

**Prompt 3: Kestrel upgrade (repo-wide)**

> Upgrade Kestrel ORM from 4.x to 5.x across the repo. The headline breaking change is that numeric/decimal columns are now returned as strings instead of numbers. Before changing code, grep for every model and query that reads a numeric/decimal column (quotes, invoices, anything else) and list them in `HANDOFF.md`. Fix each site so the string is handled explicitly: no arithmetic, comparison or `+` on the raw value, no implicit `Number()`. Where the money code is being rewritten on another branch (`packages/pricing`, `apps/billing`, `scripts/backfill`), make the smallest change that compiles and keeps tests passing, and flag it in `HANDOFF.md` so it can be reconciled. Read the full changelog for other breaking changes, not just the headline one, and check the Kestrel migration runner and any date, JSON and bigint behavior. Do not change schema. Run the full test suite against a fresh database built from the migrations. Land this as a small, self-contained set of commits so the others can rebase onto it.

**Prompt 4: backfill (scripts/backfill)**

> Write a one-off script in `scripts/backfill` that converts the roughly 3.1M historical `quotes` rows to minor units, filling `quotes.amount_minor` and `quotes.currency` from `quotes.amount` (these columns are added by migration 0042 on another branch; assume them). Requirements: batched by primary key range (for example 10k rows), resumable (selects only rows where `amount_minor IS NULL`), idempotent, safe to run while the app is live, with a `--dry-run` mode and a progress log. Use `fromDecimalString` from `packages/pricing`; read `amount` as a string (Kestrel 5 returns numeric as string) and never use floats. Half-to-even at 2 decimals. Values with 4 decimals are normal (for example 18.3350 and 7.1250). Write a row to a `backfill_rounding_log` file or table for every row whose result differs from `Math.round`, so finance can review. After each run, print a verification report: rows converted, rows remaining, and a sum check comparing `SUM(amount)` against `SUM(amount_minor)/100` per currency. Do not drop or alter `quotes.amount`. Test on a fixture database with ties, nulls, zero, negatives and a 4-decimal value.

## Merge plan for Friday

1. **Thursday freeze.** Each agent branch has green CI and its `HANDOFF.md`. Review the four `HANDOFF.md` files first, since they list the cross-branch conflicts.
2. **Create an integration branch** from `main` and merge in this order: contract/Day 0 commit, task 3 (Kestrel), task 1 (pricing and 0042), task 2 (billing and 0043), task 4 (backfill). After each merge, run the full test suite on a fresh database built from all migrations, not just the changed package.
3. **Resolve the expected conflicts:** places where task 3 patched money code that task 1 replaced (take task 1's version, keep task 3's string parsing); billing's local stub (delete it); the migration directory (check the numbering is 0042, 0043, with no duplicates).
4. **Check behavior, not just compilation.** Add a test that fails if any numeric column is used in arithmetic as a string, and one that checks half-to-even on 18.3350 and 7.1250 end to end.
5. **Deploy order in production:** (1) migrations 0042 and 0043 (additive, safe); (2) application code that writes both `amount` and `amount_minor`; (3) the backfill, run first with `--dry-run` on a production snapshot, then live; (4) verify the report and have finance sign off on the rounding-difference log; (5) the contract migration 0044 (NOT NULL, drop or rename `amount`), as a separate later change. Do not ship 0044 on Friday.
6. **Rollback:** everything through step 4 is additive, so rollback is a code revert. Only 0044 is destructive, which is why it waits.

## Assumptions

- Currencies are only EUR and DKK today, both with 2 decimals.
- Existing quotes are all EUR (the `currency` column is new), so the backfill sets currency to 'EUR' unless a source column says otherwise. Please confirm this.
- Kestrel 5 migrations still run the same way. Check against the full changelog.
- Finance should confirm that tie rows moving by one cent (for example 7.125 to 7.12) is acceptable, since it differs from what customers were charged before.
