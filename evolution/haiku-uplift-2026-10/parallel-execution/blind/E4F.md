I can write the four prompts and a merge plan, but I don't think the plan as described will merge cleanly on Friday. The four pieces are coupled, and two of them will collide in the database layer. I've assumed a sequence below, and I've flagged the decisions your team needs to make first.

## Why four parallel worktrees will conflict

1. **Migration numbering.** Items 1 and 2 both need a migration after 0041. If both agents create `0042_*.sql`, the merge breaks, and CI builds each branch's database from its own migrations. Assign numbers up front: pricing gets 0042, billing gets 0043. The backfill (item 4) is a script, not a migration, so it takes no number.
2. **Item 2 depends on item 1.** Billing reads amounts through `Money`, and `Money` changes shape in item 1. An agent working on billing in parallel will code against a type that does not exist yet.
3. **Item 3 touches item 1.** Kestrel 5 returns numeric columns as strings. `quotes.amount` is numeric today, so pricing code that reads it will break under Kestrel 5 whether or not item 1 is done. Item 1 also changes that column to bigint, and the changelog does not say what Kestrel 5 returns for bigint. Check the changelog before the pricing agent writes any parsing code.
4. **Item 4 and the item 1 migration overlap.** If the migration converts `amount` to minor units with a `USING` clause, the backfill has nothing left to do. If the backfill converts the rows, the migration must not also scale them. Choose one, or the 3.1M rows get multiplied twice.

## Decisions to make before any agent starts

- **Precision of minor units.** `numeric(12,4)` holds four decimals, and historical values such as 18.3350 and 7.1250 use them. Minor units for EUR and DKK are cents, which hold two. Converting 18.3350 gives 1833.5 cents, and 7.1250 gives 712.5 cents. Half-to-even rounds these to 1834 and 712. Finance should confirm that rounding to the cent is what the auditors approved. If they want the sub-cent value kept, `bigint` at cents is the wrong type, and the design needs a scale of 10^4 or a second column.
- **Audit trail.** Before the migration, keep the original `numeric(12,4)` values in a column such as `amount_legacy`, or in an archive table. Auditors will want to reconcile old and new amounts, and the backfill cannot be undone without it.
- **Rounding.** Math.round rounds halves toward positive infinity, so -2.5 becomes -2, not -2 under half-to-even. Pricing needs one shared `roundHalfEven` helper. Do not write a per-call-site fix. The helper needs tests for 18.3350, 7.1250, negative values, and values that are not halves.
- **Currency exponents.** Code that uses `/100` assumes every currency has two decimals. DKK and EUR do, but `Money` takes an arbitrary `currency` string. Put the exponent in a lookup table and fail loudly on unknown currencies.

## Recommended sequence

Run these in separate worktrees, but merge in this order:

1. Item 3 (Kestrel 5) first, on its own, with the existing tests passing. This isolates the string-vs-number change.
2. Item 1 (pricing and migration 0042), rebased onto the Kestrel branch.
3. Item 2 (billing and migration 0043), rebased onto item 1. Start it only after item 1's `Money` type is merged, or give it a stub of the new type.
4. Item 4 (backfill), last. Run it only on a staging copy first, then in production after the column change is deployed.

Agents 1 and 3 can run at the same time. Agent 2 should wait. Agent 4 can be written in parallel, but must not run until the migration exists.

## Agent prompts

### Agent A: Kestrel 5 upgrade (worktree `kestrel-5`)

```
Upgrade Kestrel ORM from 4.x to 5.x across the monorepo.

Read the Kestrel 5 changelog first. Note every breaking change, not only the headline one: numeric/decimal columns now return strings instead of numbers.

Do:
- Bump the version in every package.json that depends on Kestrel. Keep one version across the repo.
- Find every read of a numeric/decimal column and make it parse explicitly. Do not use parseFloat in money code. Leave a TODO for the pricing package if the value is money, because item 1 changes that column.
- Fix type errors and failing tests. Do not change any business logic.
- Do not create or edit migrations under db/migrations. Do not touch packages/pricing money types.

Run each package's tests against a fresh database built from the migrations in this branch. Report the changelog items you found that affect this repo, and the list of files you changed.
```

### Agent B: pricing minor units (worktree `pricing-minor-units`)

```
Replace floating-point money with integer minor units in packages/pricing.

Change Money from number to { minor: number; currency: string }. Minor units are the smallest unit of the currency. Use the exponent table in packages/pricing (create it if missing): 2 for EUR and DKK. Fail loudly on an unknown currency.

Add a rounding helper roundHalfEven(x: number): number. Replace every Math.round in the pricing package with it. Add tests for:
- 18.3350 -> 1834 (the value is 1833.5 cents, and half-to-even goes to the even neighbour)
- 7.1250 -> 712
- negative halves
- non-half values

Migration: create db/migrations/0042_quotes_amount_minor_units.sql. It must:
1. Add amount_legacy numeric(12,4) and copy the old amount into it.
2. Convert amount to bigint in minor units with half-to-even rounding.

Do NOT run the backfill script in this migration. Item 4 handles historical rows, and the decision on which of these does the conversion is recorded in the plan. Stop and report if you think the migration needs to do the work itself, rather than leaving it to the backfill.

Use only migration number 0042. Do not touch apps/billing or scripts/backfill. Run the pricing tests against a fresh database built from migrations up to 0042.
```

### Agent C: multi-currency invoice PDFs (worktree `billing-dkk`)

```
Add multi-currency support to invoice PDFs in apps/billing. DKK launches next month alongside EUR.

Start from the origin/main pricing package or the branch that merged item 1. Read Money in packages/pricing and use it. Do not reimplement money formatting in billing.

Do:
- Add a currency column to invoices. Create db/migrations/0043_invoices_currency.sql. Default to 'EUR' for existing rows. Make it NOT NULL after the default is set.
- Show amounts on the PDF with the invoice currency, using the currency's exponent for decimal places and locale-appropriate formatting.
- Add tests for an EUR invoice and a DKK invoice.

Do not edit packages/pricing or db/migrations other than 0043. Do not run the backfill. If Money does not yet have the new shape when you start, stub it in a local file marked TEMP and say so in your report.
```

### Agent D: historical backfill (worktree `backfill-minor-units`)

```
Write scripts/backfill/quotes-minor-units.ts: a one-off script that converts historical quote rows to minor units.

Context: about 3.1M rows in quotes. Values may have four decimals (for example 18.3350). Rounding must be half-to-even, using the shared roundHalfEven helper from packages/pricing. Do not reimplement it.

Requirements:
- Process in batches by primary key (for example 10,000 rows per batch), each in its own transaction. Make it resumable from the last completed key.
- Idempotent: check whether a row is already converted before touching it. Do not double-scale a row if the script runs twice.
- Dry-run mode that reports row counts and a sample of before/after values without writing.
- Read from amount_legacy, not from amount, so that a partially failed run can be reconciled.
- Log the total count of rows changed and any mismatch between amount_legacy and the converted value.

Do NOT run it against any database. Write it and its tests only. Tests must run against a small fixture, not the full table. The script should refuse to run unless migration 0042 has been applied.
```

## Merge plan for Friday

1. Confirm the three decisions above with finance: sub-cent precision, the audit-column approach, and the rounding rule for negatives. Do this before the agents start, because the answers change the migration.
2. Merge A (Kestrel 5). Run the full test suite on main. Stop if anything fails.
3. Rebase B (pricing) on main, confirm migration 0042 is the only new migration, and merge. Run CI on a fresh database.
4. Rebase C (billing) on main. Confirm migration 0043 is the next number and that 0042 is already present. Replace any TEMP stub with the real `Money` type. Merge and run CI.
5. Merge D (backfill). It is a script, so it changes no schema. Run it on a staging copy with dry-run first, then compare totals against `amount_legacy`.
6. Production order: deploy the migrations, then run the backfill, then deploy the code that reads minor units. Code that reads the new column must not be live before the backfill finishes.

Any conflicts should be in the shared lockfile or the Kestrel version bump. If a conflict appears in `packages/pricing` or `db/migrations`, stop and check the sequence, because that means two agents are doing the same work.
