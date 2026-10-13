Short version: I wouldn't run all four fully in parallel and expect a clean merge. The packages differ, but the four jobs share a database column, a type, a migration sequence and a driver behaviour. Below are the couplings I found, a staging that keeps four agents busy anyway, then the four prompts and the Friday merge plan.

## Where the "different packages" assumption breaks

1. **Billing depends on pricing's new type.** Invoices read amounts through the pricing package, so `Money` changing from `number` to `{ minor, currency }` breaks billing's code. Billing can't compile or test against the old `Money`. It needs the new type up front.
2. **The Kestrel upgrade touches everything.** It is repo-wide and changes how numeric columns come back (strings). It will edit files in pricing, billing and scripts, so it will conflict with the other three. It also interacts with the money change. `quotes.amount` is numeric today, so after the upgrade it arrives as a string. After the pricing migration it is a bigint, and Node's Postgres drivers typically return bigint as a string too. Whatever parsing the pricing agent writes has to hold under both Kestrel versions.
3. **The migration numbers collide.** Pricing (quotes.amount) and billing (invoices.currency) will both create 0042 on their own branches. Kestrel may also need one. Each branch passes CI alone and the merge breaks on duplicate numbers. Assign them now.
4. **The backfill and the column migration are the same job, and the plan as written loses data.** A plain `ALTER COLUMN amount TYPE bigint` on numeric(12,4) rounds to whole units. 18.3350 becomes 18, not 1834. The conversion needs an explicit scale (`* 100` for EUR and DKK) in the same step. The backfill script also can't be tested by CI: CI builds a fresh, empty database from migrations, so the 3.1M-row path never runs there.
5. **Rounding is a correctness trap.** Finance wants half-to-even, and the code uses `Math.round` (half away from zero on positives). Your own data shows the difference. 7.1250 to two decimals is 7.12 under half-to-even and 7.13 under `Math.round`. 18.3350 is 18.34 under both, because the 3 is odd and rounds up. In floating point, 18.335 * 100 is not reliably 1833.5, so a float-based conversion can land on the wrong side. Do the conversion in Postgres `numeric` or on decimal strings, never `number` math. Postgres `round(numeric)` is half away from zero, so it is also wrong here. Use a custom half-even step.
6. **A 3.1M-row type change takes a heavy lock.** `ALTER ... TYPE` rewrites the table under an exclusive lock. Prefer expand/contract: add `amount_minor bigint` (nullable), backfill in batches, then switch reads and drop the old column in a later release.

## Recommended staging (still four agents)

- **Day 0, 1 hour, you or one agent:** write the contract below and commit it to main. It holds the `Money` type, the rounding helper signature, the migration number allocation and the expand/contract column plan. All four worktrees branch from that commit.
- **Wave 1, parallel:** A (Kestrel 5), B (pricing), and C (billing, coding against the contract). D (backfill) writes and unit-tests the script against fixtures.
- **Wave 2, sequential:** merge in the order given in the merge plan, with a full CI run after each merge.

Allocation of migration numbers:
- 0042: pricing adds `quotes.amount_minor bigint` and `quotes.currency` (expand).
- 0043: billing adds `invoices.currency`.
- 0044: the contract step (drop old `amount`, set not null). It ships only after the backfill has run in production, so it is not part of Friday's merge.
- Kestrel gets no migration. If it needs one, it takes 0045.

Shared contract (put it in `docs/money-contract.md` on main):
- `type Money = { minor: number; currency: string }`. `minor` must be a safe integer. Reject non-integers and values above `Number.MAX_SAFE_INTEGER` when parsing.
- Minor-unit exponent comes from a currency table in `packages/pricing` (EUR=2, DKK=2). Never hardcode 100.
- `roundHalfEven` is the only rounding function allowed. It works on decimal strings or integers, not floats.
- DB values for numeric and bigint columns are parsed through one helper in pricing (`parseDbAmount(value: string | number | bigint)`), which works under Kestrel 4 and 5.
- Existing quotes without a currency are treated as EUR. Confirm this with finance.

## Prompt 1: Kestrel ORM 4.x to 5.x

> You are upgrading Kestrel ORM from 4.x to 5.x across the TypeScript monorepo, in your own git worktree on branch `kestrel-5`. The goal is a mechanical, behaviour-preserving upgrade that merges first.
>
> Rules:
> - Do not change any money semantics, schema or migrations. Do not add migrations. If you think you need one, stop and report.
> - The headline breaking change is that numeric/decimal columns now return strings instead of numbers. Find every read of a numeric/decimal column (start with `quotes.amount` and any `invoices` amount columns). Do not fix them with `Number(x)` or `parseFloat`, because that reintroduces floats. Route them through a single temporary adapter, `packages/pricing/src/db-amount.ts`, exporting `parseDbAmount(value: string | number | bigint): number` that accepts both forms and throws on non-finite or non-numeric input. Keep the current numeric semantics for now. Another agent will replace the internals.
> - Also read the full changelog for other breaking changes (transactions, query builder, type exports, result shapes) and list the ones you handled.
> - Keep each edit minimal in pricing and billing so rebases by other agents stay small. Do not reformat files you don't need to change.
> - Run every package's tests and the full CI against a database built from the migrations on your branch.
>
> Deliver: a green branch, a short note listing every numeric read site you changed, and any behaviour change you could not preserve.

## Prompt 2: pricing, integer minor units

> You own `packages/pricing` and the `quotes` table change, in a worktree on branch `pricing-minor-units`. Read `docs/money-contract.md` first and follow it exactly.
>
> Tasks:
> 1. Change `Money` from `number` to `{ minor: number; currency: string }`. Add a currency exponent table (EUR=2, DKK=2) and constructors/formatters that use it. No arithmetic on floats anywhere.
> 2. Replace every `Math.round` in pricing with `roundHalfEven`. Finance's auditors approved half-to-even, so this is a requirement. Add tests with exact cases: 7.1250 to 2 decimals gives 7.12, 7.1350 gives 7.14, 18.3350 gives 18.34, 18.3250 gives 18.32, 0.005 gives 0.00, and negative mirrors (-7.1250 gives -7.12). Implement it on decimal strings or integers. Explain how you avoid float error for 18.335.
> 3. Add migration `db/migrations/0042_quotes_amount_minor.sql`, which must use exactly that number. It adds `quotes.amount_minor bigint` (nullable) and `quotes.currency text` (default `'EUR'`, not null). Do not alter or drop `quotes.amount` here. Do not do the data conversion in this migration, because there are 3.1M rows and a separate script will do it in batches. Make the migration safe to run on a fresh database.
> 4. Write a SQL function or a documented query, tested in Postgres, that converts a numeric(12,4) value to minor units with half-even rounding. The backfill agent will reuse it. Do not use Postgres `round()` for this, because it rounds half away from zero. Test it on values like 18.3350 and 7.1250.
> 5. Update reads and writes of quotes so they use `amount_minor` when it is present and fall back to the legacy `amount` (via `parseDbAmount`) when it is null. This keeps the system correct during the backfill.
>
> Do not touch apps/billing, scripts/backfill or the Kestrel version. If your type change breaks billing, list the broken call sites in your handoff note and do not fix them. Run the pricing tests against a fresh DB built from your branch's migrations.

## Prompt 3: billing, multi-currency invoice PDFs

> You own `apps/billing`, in a worktree on branch `billing-multicurrency`. Read `docs/money-contract.md` first. Pricing is changing in parallel, so code against the contract and not against the current `Money`.
>
> Tasks:
> 1. Add migration `db/migrations/0043_invoices_currency.sql` (use exactly that number): `invoices.currency text not null default 'EUR'`, with a check for supported currencies (EUR, DKK). Do not touch other tables.
> 2. Generate invoice PDFs in EUR or DKK. Use the `Intl` APIs with the invoice's currency, with locale-correct separators for Danish (1.234,56 kr.) and euro formats. Amounts must be taken as `Money` from the pricing package and never converted through `number` division except through pricing's formatter. No arithmetic on amounts in billing. If you need totals or tax, call a pricing function, and list any function you need that doesn't exist.
> 3. An invoice must never mix currencies. Add a guard and tests for line items with a different currency than the invoice.
> 4. Until pricing lands, create a local test stub of the contract's `Money` type in `apps/billing/test/` and mark it clearly. Do not edit `packages/pricing`.
> 5. Tests: PDF snapshot tests for one EUR and one DKK invoice, plus the guard. Run them against a fresh DB built from your branch's migrations.
>
> In your handoff, list every place billing touches `Money` or amount columns so it can be re-checked after pricing and Kestrel are merged.

## Prompt 4: backfill script

> You own `scripts/backfill`, in a worktree on branch `backfill-minor-units`. You write and test the script. You do not run it against production.
>
> Context: `quotes.amount` is numeric(12,4) and holds about 3.1M rows. Some values have four decimals (for example 18.3350 and 7.1250) because partner rate cards were stored that way. Pricing is adding `quotes.amount_minor bigint` (migration 0042). Do not create or edit migrations.
>
> Requirements:
> 1. For each row with `amount_minor IS NULL`, set `amount_minor` to the amount in minor units (scale 2 for EUR and DKK, from the pricing exponent table), rounded half-to-even, which finance requires. 7.1250 gives 712, 18.3350 gives 1834, 18.3250 gives 1832. Do the arithmetic in Postgres `numeric` or on the string value. Never use JS `number`, and never Postgres `round()` (it rounds half away from zero).
> 2. Batch by primary-key ranges (for example 10,000 rows per batch, in separate transactions), so locks stay short. The script must be idempotent and resumable: re-running it only touches rows where `amount_minor IS NULL`. Log progress and row counts.
> 3. Add a dry-run mode that reports how many rows would change, and a list of rows whose fourth decimal means the rounding mode matters (the exact ties, where half-even and half-away disagree). Print a count and a sample so finance can review them.
> 4. Add a verification query: count of rows where `amount_minor` is not equal to the half-even rounding of `amount * 100`, expected 0. Also report the maximum absolute rounding difference, which must be under half a minor unit.
> 5. Tests: use a fresh DB with a few hundred rows that include ties, negative values, zero, the max 12-digit value and nulls. CI can't exercise 3.1M rows, so also include a documented rehearsal procedure to run on a production-sized copy of the data, with expected duration.
> 6. Read through the database layer only in the way the Kestrel 5 note says (numeric columns come back as strings). Prefer raw SQL for the conversion so the library version doesn't matter.
>
> Handoff: usage docs, the dry-run output on your test data, and the questions that need finance's answer (are negative quotes possible? Are there quotes in currencies other than EUR?).

## Merge plan for Friday

**Before Friday**
- Wednesday: agents hand off. Everyone rebases onto main to catch drift.
- Thursday: do a trial merge in a throwaway branch in the order below, and run full CI. Friday should be a repeat of Thursday.
- Ask finance two questions now: what currency do existing quotes have (assumed EUR), and whether they have a view on the tie cases (the dry-run report).

**Merge order, with CI after each step**
1. **Kestrel 5** first. It is the widest change and the others must sit on top of it. After it merges, the pricing, billing and backfill branches rebase onto main. Conflicts should be small if the agent kept edits minimal.
2. **Pricing** second. It brings migration 0042 and the new `Money`. After merging, run the full repo build: type errors in billing show exactly where billing has to adapt. Check that migrations apply cleanly from empty and that 0042 is the next number after 0041.
3. **Billing** third. Rebase onto main, replace the test stub with the real `Money`, and fix any compile errors. Migration 0043 follows 0042. Run billing's PDF snapshot tests.
4. **Backfill** last. It only adds a script, so it should merge without conflicts. Merging it does not run it.

**After merge**
- Staging: run a copy of production data (or a representative slice with at least all the tie rows), run the backfill dry run, then the real run, then the verification query (expect 0 mismatches). Time it so you know the production window.
- Production deploy order: deploy the code that reads `amount_minor` with fallback to `amount` (pricing), run migrations 0042 and 0043, run the backfill, run the verification, and only after that ship 0044 (set `amount_minor` not null, drop `amount`) in a later release. The fallback means old and new rows both work during the backfill.
- The Denmark launch is next month, so 0044 doesn't need to be on Friday's path. Keep it out of this merge so you have a rollback.

**Rollback**
- The expand migrations (0042 and 0043) only add columns, so they are safe to leave in place if you revert code.
- Revert the merges in reverse order. Revert Kestrel last, because reverting it first would put string-parsing code back on top of old behaviour.
- Do not drop `quotes.amount` until you have spent at least one release cycle on the new column.

**Things to watch in review**
- Any use of `Math.round`, `toFixed`, `parseFloat`, `Number()` on money.
- Any duplicate migration number.
- Any bigint read that doesn't go through `parseDbAmount`.
- Any test that only passes because CI's database is empty.

Assumptions I made: EUR and DKK both use two decimals, existing quotes are EUR, and the monorepo's tests already run per package. If any of these is wrong, the prompts above need small changes (mainly the exponent table and the default currency).
