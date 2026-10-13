# Four agent prompts and the Friday merge plan

Short version: the four worktrees will probably merge cleanly as text, but they are not independent. The packages are separate directories, but the work is coupled in three places:

- **Money type.** Work 1 changes it and work 2 reads it, so billing code written against the old shape will break on merge.
- **Kestrel 5.** Work 3 touches every read of a numeric column, including the `quotes.amount` reads that work 1 changes.
- **Migration numbers.** Work 1 and work 2 both need new migrations. If both branches pick `0042`, CI on the merged branch will fail on a duplicate.

So I would not merge four branches at once on Friday. The plan below sequences them and fixes the shared contract up front.

I have not read the repo, so the points below are assumptions to check.

## Decisions to make before any agent starts

1. **Scale of minor units for quotes.** EUR and DKK both have 2 decimal places, so cents are the obvious minor unit. But historical `quotes.amount` values have 4 decimals (18.3350, 7.1250), so converting to cents means rounding. Two options:
   - (a) Minor unit = cents. Round once, half-to-even, at conversion. Sub-cent precision is lost, which Finance must accept.
   - (b) Minor unit = 1/10,000 for quotes, which is exact for the existing data. Round to cents only when producing invoice amounts.
   Ask Finance which one the audit trail needs. The rest of the plan assumes (a) unless you say otherwise.
2. **Rounding function.** Postgres `round()` on numeric rounds half away from zero, so the migration must not do rounding in SQL. Do all half-to-even rounding in one TypeScript function in `packages/pricing` (say `roundHalfEven`). Check the examples: 18.3350 to cents gives 18.34 under half-to-even and 18.34 under `Math.round`, but 7.1250 gives 7.12 under half-to-even and 7.13 under `Math.round`. Changing rounding will change historical totals, so decide whether past invoices are re-issued or left as they are.
3. **Migration plan for `quotes.amount`.** A single `ALTER ... TYPE bigint` over 3.1M rows takes a long lock and gives no rollback. Recommended: migration 0042 adds `amount_minor bigint`, the backfill fills it, and a later step swaps the columns. This changes the brief slightly, so confirm it.
4. **Migration numbers.** Pricing takes `0042`, billing takes `0043`. Kestrel should not need one. Write these into the prompts below.

## Shared contract (paste into every prompt)

```
Money = { minor: number; currency: string }   // minor units; number is safe here (values far below 2^53)
Supported currencies: EUR (exponent 2), DKK (exponent 2)
Rounding: roundHalfEven(value, scale) from packages/pricing. Do not use Math.round.
Migrations: pricing uses db/migrations/0042_*.sql; billing uses db/migrations/0043_*.sql. Do not create other numbers.
Kestrel: 5.x. numeric/decimal columns return strings; parse explicitly.
Do not edit files outside your scope. If you need something outside it, stop and report it.
```

## Agent 1: pricing (branch `pricing-minor-units`, own worktree)

```
You are working in a git worktree of the Larkspur Couriers dispatch monorepo (TypeScript, Postgres, Kestrel ORM).

Scope: packages/pricing and db/migrations/0042_*.sql only. Do not touch apps/billing or scripts/backfill.

Task:
1. Change Money from number to { minor: number; currency: string }. Update every call site in packages/pricing.
2. Add roundHalfEven(value, scale) and use it everywhere Math.round is used today. Add unit tests with these cases: 18.3350 -> 18.34, 7.1250 -> 7.12, 2.5 -> 2, 3.5 -> 4, negative values, and values already on the grid.
3. Write migration 0042 that changes quotes.amount from numeric(12,4) to bigint under the minor-unit scale agreed in the decisions section. Do the conversion without SQL rounding. Do not backfill historical rows here; that is scripts/backfill.
4. Run the package tests against a fresh database built from migrations on your branch.

Report: the files changed, the test results, and any call site you were unsure about.
```

## Agent 2: billing (branch `billing-dkk-invoices`, own worktree)

```
You are working in a git worktree of the Larkspur Couriers dispatch monorepo (TypeScript, Postgres, Kestrel ORM).

Scope: apps/billing and db/migrations/0043_*.sql only. Do not change packages/pricing; code against the shared Money contract. Until agent 1 lands, use a local type stub with the same shape and mark it clearly.

Task:
1. Write migration 0043 that adds invoices.currency text not null, with a check constraint allowing only EUR and DKK. Backfill existing rows to 'EUR' explicitly in the migration. Do not rely on a silent default.
2. Render invoice PDFs in the invoice currency. Format amounts from minor units using the currency's exponent, with Intl.NumberFormat and the currency code. Use the invoice locale for DKK (da-DK) and EUR.
3. Do not use Math.round. Use roundHalfEven from packages/pricing once it is available.
4. Add tests for DKK and EUR invoices, a mixed-currency batch, and a row with an unknown currency (it should fail, not default).

Report: the files changed, the test results, and which stubs must be replaced after pricing merges.
```

## Agent 3: Kestrel upgrade (branch `kestrel-5`, own worktree)

```
You are working in a git worktree of the Larkspur Couriers dispatch monorepo (TypeScript, Postgres, Kestrel ORM).

Scope: all packages' Kestrel dependency declarations and lockfile, plus any code that reads numeric or decimal columns through Kestrel. Do not add migrations.

Task:
1. Upgrade Kestrel from 4.x to 5.x across the repo. Read the 5.x changelog and check whether bigint columns also come back as strings.
2. Find every read of a numeric or decimal column (grep the schema for numeric, decimal, and the Kestrel column helpers). Make each one parse explicitly. Do not use parseFloat for money. Money values must be parsed to integers or left as minor units.
3. Run every package's tests against a fresh database built from migrations.

Report: the changelog items that affected the repo, every read site you changed, and any read site you were unsure about.
```

## Agent 4: backfill (branch `backfill-quotes-minor`, own worktree)

```
You are working in a git worktree of the Larkspur Couriers dispatch monorepo (TypeScript, Postgres, Kestrel ORM).

Scope: scripts/backfill only. Depend on the Money contract and roundHalfEven from packages/pricing; do not edit those packages.

Task: write a one-off script that converts the 3.1M historical quote rows to minor units. It runs after migration 0042 has been applied.
1. Batch by primary key (keyset pagination, for example 5,000 rows per transaction). Make it resumable from the last committed id.
2. Make it idempotent: rows that already have their minor value are skipped.
3. Add a --dry-run mode that prints counts and a sample of conversions, including 18.3350 and 7.1250.
4. Add a verification step: total rows converted equals total rows, and no null minor values remain.
5. Do not add it to db/migrations. Do not run it against production. Its tests should use a small fixture.

Report: how to run it, the batch size used, and the verification output on the fixture.
```

## Friday merge plan

Do this in order. Do not merge all four in parallel.

1. **Thursday.** Settle the decisions above. Confirm migration numbers 0042 and 0043 are reserved.
2. **Kestrel 5 first (branch 3).** It changes the lockfile and read sites across the repo, so it is the most conflict-prone and should land on main first. Merge only when all package tests pass on a fresh database.
3. **Pricing second (branch 1), rebased onto the Kestrel merge.** It adds migration 0042 and defines Money and roundHalfEven. Run its tests, then grep the repo for remaining `Math.round` calls on money.
4. **Billing third (branch 2), rebased onto pricing.** Replace the local Money stub with the real type. Add migration 0043. Run billing tests with a fresh database.
5. **Backfill last (branch 4).** Run it against a staging copy of the database first, checking row counts and a sample against the dry-run output. Schedule the production run in a maintenance window, or use the add-column-then-swap plan so the app keeps working during the backfill.

After each merge, run in this order:
- the full typecheck,
- each package's tests on a fresh database built from the migrations on that branch,
- `grep` for `Math.round`, `parseFloat`, and direct numeric reads in money code.

Expect the first failures to come from billing reading numeric values as strings, even when the merge itself is clean.

## Risks I would not skip

- **Finance rounding change.** Moving from `Math.round` to half-to-even changes historical amounts. Get sign-off before running the backfill.
- **Currency defaults.** Do not let existing invoices pick up a currency by default. Set it explicitly to EUR.
- **Backfill lock.** A direct type change on 3.1M rows will lock the table for a long time. Use the add-then-swap plan or a maintenance window.
