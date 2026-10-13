Short version: don't expect a clean merge from these four as scoped. They touch different directories, but they share a data contract (the `quotes.amount` column and the `Money` type), a migration number sequence, and a rounding rule. Two of the four can't be correct without the others. Below are the dependencies I found, a reshaped plan that still gives you four parallel agents, then the prompts and the Friday merge plan.

## Where the "independent packages" assumption breaks

1. **Migration numbering.** Tasks 1 and 2 both add migrations, and both will take 0042. Git won't flag a conflict if the filenames differ (for example `0042_quotes_bigint.sql` and `0042_invoices_currency.sql`). You get two 0042s that fail or apply in an undefined order. Reserve numbers now: 0042 for pricing, 0043 for billing.
2. **Kestrel 5 changes how every numeric column reads (task 3).** Numeric columns come back as strings. Today `quotes.amount` is numeric(12,4), so until task 1's migration lands, pricing reads strings. After it, the column is bigint, and bigint may also come back as a string or a `bigint`, depending on the driver. Task 3 also touches pricing and billing code, which are the other agents' files. Each branch's CI builds the DB from that branch's own migrations, so each agent tests against a different schema and the green results won't hold together after the merge.
3. **Billing reads amounts through pricing (task 2).** The `Money` type change (`number` to `{ minor, currency }`) breaks every billing call site. Billing can't be written against the old type, and it can't be built against the new one until pricing exists. Billing also needs `currency` to be real in `Money`, which task 1 defines.
4. **The backfill (task 4) duplicates the migration.** Task 1 already converts `quotes.amount` from numeric(12,4) to bigint. That cast converts the 3.1M rows. If the backfill runs "after the column change", the data is already converted, and running it again would multiply every value by 100. One of them has to own the conversion.
5. **Rounding.** Finance wants half-to-even, but today the code uses `Math.round`, and the old values are four-decimal numerics. Your examples show why this matters: 18.3350 is 1833.5 minor units, which half-to-even rounds to 1834 (even), and 7.1250 is 712.5, which rounds to 712. `Math.round` gives 1834 and 713. Float math also makes `18.335 * 100` come out as 1833.4999..., so the result depends on the method. Convert from the decimal string with integer arithmetic. Never multiply floats. Whichever agent writes the conversion must use this rule, and the migration SQL and the TypeScript backfill must agree exactly. Postgres `round(numeric)` rounds half away from zero, not half-to-even, so the SQL needs explicit handling.
6. **Precision loss is a product decision.** Moving four-decimal partner rates to two-decimal minor units loses information on rows like 18.3350. Decide before any agent starts: (a) round the stored historical quotes to 2 decimals (half-to-even, with an audit table of the original values), or (b) store a higher-precision scale for quotes. This also affects JPY-type currencies (0 decimals) and anything else with a different exponent. I'd choose (a) with the original numeric values kept in a side table, but finance should confirm, since the auditors signed off on the rounding rule and not on dropping the extra digits.
7. **Operational risk.** An `ALTER COLUMN TYPE` on 3.1M rows takes an exclusive lock and rewrites the table. Run it in a maintenance window or use the add-column, backfill, swap pattern. This ties into the backfill question in point 4.

## Reshaped plan: one contract step, then parallel work, then a stacked merge

**Step 0 (Monday, one person or one agent, about half a day): the contract.** Merge this to `main` before the agents start, so every worktree branches from it:
- The new `Money` type, `{ minor: number; currency: string }`, with `fromDecimalString`, `toDecimalString` and a half-to-even rounding helper, plus unit tests that include 18.3350 -> 1834, 7.1250 -> 712, negative values and 0.5 cases. Everyone uses this one helper.
- Reserved migration numbers: 0042 (pricing: quotes bigint), 0043 (billing: invoices currency). Everything else needs a new number from the owner.
- The decision on point 6, and the decision on who owns the data conversion (point 4).
- Optionally, a Kestrel 5 compatibility shim: a single `readNumeric(row.col)` / `readMoney()` function in pricing that accepts a string or a number. Both old and new ORM versions then work.

**Which tasks truly run in parallel after Step 0:**

| Agent | Package | Depends on | Owns migration |
|---|---|---|---|
| A: pricing | packages/pricing | Step 0 | 0042 (schema change and data conversion, or schema only, see below) |
| B: billing | apps/billing | Step 0 types (stubbed pricing) | 0043 |
| C: Kestrel 5 | repo-wide, mechanical | Step 0 shim | none |
| D: backfill | scripts/backfill | Step 0, A's migration design | none |

My recommended split of the conversion work (point 4): the **migration does the schema change only** if you use the add-column pattern (`amount_minor bigint` added in 0042, `amount` kept), and the **backfill script fills it** in batches (for example 50k rows, resumable, idempotent). A later migration (0044, after verification) drops `amount` and renames. If you would rather have a single in-place `ALTER ... USING`, then delete task 4. It's one statement, but it needs the maintenance window. Pick one. Don't do both.

Task C (Kestrel) is the one that conflicts with everything. Run it **last** or keep it small: it merges after A and B, not in parallel with them. If you want it in parallel, restrict it to dependency bumps, config and files nobody else touches, and have it open a second PR for numeric handling after A and B land.

## The four agent prompts

Give each agent its own worktree (`git worktree add ../wt-<name> -b <branch> main`, branched after Step 0). Paste the shared preamble into every prompt.

**Shared preamble**

> You are working in the Larkspur Couriers dispatch monorepo (TypeScript, Postgres, Kestrel ORM). You work in your own git worktree and branch. Only edit files in the paths named in your task. If you need a change outside them, stop and write it down in `HANDOFF.md` in your worktree root instead of making it. Shared rules: (1) `Money` is `{ minor: number; currency: string }`; use the helpers from `packages/pricing/src/money` and never do float arithmetic on money. (2) All rounding is half-to-even (banker's rounding). Never use `Math.round` for money. Postgres `round()` is NOT half-to-even; write the SQL explicitly. Test cases: 18.3350 -> 1834 minor, 7.1250 -> 712 minor. (3) Migrations are in `db/migrations`, numbered sequentially; the latest is 0041. You may only create the migration number assigned to you. (4) CI builds a fresh database from your branch's migrations, so your tests must pass on your branch alone, and you must also state which other branches' migrations they assume. (5) Finish with a summary of the files changed, the tests you ran and their output, and any assumption you couldn't verify.

**Agent A: pricing (`packages/pricing`, migration 0042)**

> Task: replace float money with integer minor units in `packages/pricing`. Change the `Money` type from `number` to `{ minor: number; currency: string }`. Update every function in the package, its public exports and its tests. Replace each `Math.round` with the half-to-even helper. Add migration `db/migrations/0042_quotes_amount_minor.sql`. [Use the option chosen in Step 0: add `amount_minor bigint` and keep `amount`; or convert in place with `ALTER COLUMN ... TYPE bigint USING`.] If you convert, the SQL must apply half-to-even rounding itself and handle the four-decimal values (18.3350 -> 1834, 7.1250 -> 712). Add a migration test with a fixture of at least 20 rows covering ties, negatives, 0.0050 and the maximum numeric(12,4) value. State the currency exponent assumption for DKK and EUR (2) and make the exponent a table lookup, not a constant. Do not edit apps/billing or scripts/backfill. In `HANDOFF.md`, list every exported symbol whose signature changed, so billing can adapt.

**Agent B: billing (`apps/billing`, migration 0043)**

> Task: multi-currency invoice PDFs (EUR and DKK) in `apps/billing`. Add migration `db/migrations/0043_invoices_currency.sql`, adding `currency` (char(3), NOT NULL, default 'EUR' to cover existing rows, and a CHECK limiting it to supported codes). Read amounts through the pricing package using the new `Money` type; until agent A's branch merges, code against the type from Step 0 on `main`. Format amounts per currency (DKK: `1.234,50 kr.`; EUR per the locale used today; keep the formatting in one function and test both). Never convert between currencies in this task. If an invoice and its quotes have different currencies, fail with a clear error. Add tests, including a PDF snapshot for each currency. Do not edit packages/pricing or other migrations. List in `HANDOFF.md` every call into pricing that you expect to change.

**Agent C: Kestrel 5 upgrade (repo-wide, no migration)**

> Task: upgrade Kestrel ORM from 4.x to 5.x. The headline breaking change: numeric/decimal columns are now returned as strings instead of JS numbers. Bump the dependency, update config and call sites, and fix type errors. Scope control: in `packages/pricing` and `apps/billing`, change only the minimum needed to compile, and put every numeric-handling change behind the `readNumeric()` helper from Step 0; do not rewrite money logic there. Search the repo for every place a numeric/decimal column is read, and produce a table in `HANDOFF.md`: file, column, old type, new type, and how it was handled. Include bigint columns, since the 5.x driver may return them as strings or `bigint` too, and check this against the real driver, not the changelog. Do not add migrations. Run the full test suite on a database built from main's migrations.

**Agent D: backfill (`scripts/backfill`)**

> Task: write a one-off script that converts the historical `quotes` rows (about 3.1M) to minor units. First read the design in Step 0 and A's `HANDOFF.md` (if present) to confirm whether the column conversion is in migration 0042 or in your script, and if the migration already converts the data, stop and report that rather than writing a script that double-converts. Otherwise: process in batches of 50,000 by primary-key range, resumable (record the last processed id), idempotent (never convert a row twice; use a `NULL` check on the target column or a status marker), with a `--dry-run` that prints counts and sample conversions and a `--verify` mode that recomputes and compares. Parse numeric values from their decimal string form. Use integer or `BigInt` arithmetic and the half-to-even helper. Never use float multiplication. Log every row where rounding changed the value (for example 18.3350 -> 1834) to an audit table or file. Test with a fixture that has ties (18.3350, 7.1250), negatives, nulls and values at the column limits. Do not edit packages/pricing or migrations.

## Friday merge plan

Merge in dependency order, one branch at a time, re-running CI after each. Don't merge everything at once.

1. **Thursday, dry run.** Create an integration branch `integration/dispatch-minor-units` from `main`. Merge A, then B, then D, then C into it locally and check what conflicts. Fix problems on the integration branch, not on the agents' branches. Build a fresh database from the integration branch's migrations and run all package tests. Also run D's dry-run on a copy of production data (or a 3.1M-row synthetic table that includes the ties).
2. **Friday, A first.** Review the diff for any `Math.round` left in pricing. Confirm migration 0042 is the only new migration. Merge to `main`, then run CI.
3. **B second.** Rebase on `main`, replace the Step 0 stub calls with the real pricing calls, and check migration 0043 applies after 0042. Merge.
4. **D third.** Rebase and confirm the dry-run output matches the audit expectations. Merge the script, but don't run it in production yet.
5. **C last.** Rebase C onto the merged `main`. The numeric-handling table from `HANDOFF.md` is your checklist, and the real risk is a column that now returns a string and gets added or compared as one (`"1834" + 1`). Run the full suite and then a smoke test against a staging database.
6. **Release order in production** (a separate step from the merge): deploy A's migration -> run D's backfill with `--verify` -> deploy B and C together or C first, whichever your staging tests support -> later, a cleanup migration that drops the old column.

**Go/no-go checks before deploying:**
- A grep for `Math.round` in money paths returns nothing.
- The golden cases (18.3350 -> 1834, 7.1250 -> 712) pass in TypeScript and in SQL.
- The migration sequence on the integration branch is 0042, 0043 with no duplicates or gaps.
- Backfill `--verify` shows 0 mismatches over all 3.1M rows.
- You have a rollback path: the original `amount` values stay in the table (or the audit table) until the cleanup migration.
- DKK invoices render correctly for one real quote end to end.

## Questions I'd settle before Monday

- Do you keep four-decimal precision for historical quotes, or round to two? Does finance accept that?
- Migration converts in place, or add-column plus backfill? This decides whether task 4 exists.
- Is a maintenance window acceptable for the 3.1M-row table rewrite?
- Do quotes already carry a currency? `Money` needs one, so if `quotes` has no currency column, you have a fifth change (a currency column on `quotes`) and it belongs to agent A.
- I assumed the DKK/EUR exponent of 2 and that nothing converts between currencies. Tell me if either is wrong.
