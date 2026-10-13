Your four tasks aren't independent, so I wouldn't expect a clean merge. Several conflicts won't show up as git conflicts. They'll show up as CI failures or wrong data after Friday. Below are the conflicts, a restructured plan, the four prompts, and the merge plan.

## Where the "different packages" assumption breaks

1. **Migration number collision.** Pricing (amount to bigint) and billing (`invoices.currency`) will both take 0042. Git won't flag it because the filenames differ, but the sequence will be broken. Pre-assign numbers: pricing gets 0042, billing gets 0043, and backfill gets 0044 only if it needs one.
2. **CI builds the database from each branch's migrations.** Billing tests need the pricing `Money` type and the pricing schema, which don't exist on the billing branch. Backfill tests need the new column, which exists only on the pricing branch. Each branch therefore fails in isolation, or passes against a schema that differs from the merged one.
3. **The Kestrel 5 upgrade changes the data pricing reads.** Numeric columns become strings, and the pricing code assumes numbers. Billing reads amounts through pricing, and backfill reads the old numeric column. Anything that does `row.amount * 100` becomes string coercion and works by accident or fails quietly. The upgrade touches every package, so it will conflict with all three other branches.
4. **The in-place `ALTER ... TYPE bigint` can't be rounded half-to-even.** `quotes.amount` has to become bigint, but the values have to be multiplied by 10^exponent first. A `USING round(amount*100)` clause uses Postgres numeric rounding, which is half away from zero, not half-to-even. It also leaves the backfill with nothing to do, or with already-wrong values.
   - Finance requires half-to-even. 18.3350 becomes 1834 (half-to-even). Math.round and Postgres `round` give 1834 for this one, but 7.1250 becomes 712 under half-to-even, where half-up gives 713.
   - On 3.1M rows, a type change rewrites the table under an exclusive lock.
   - **Fix: expand/contract.** Migration 0042 adds a nullable `amount_minor bigint` and a currency column if one is needed. The backfill fills it in batches. A later migration (after Friday) makes it NOT NULL and drops `amount`. The pricing code reads `amount_minor`, with a fallback to the old column until the backfill is verified.
5. **Floats can't be rounded correctly.** 18.335 isn't exactly representable as a double, so `Math.round(x*100)` or any float path gives arbitrary results on ties. Rounding must run on decimal strings (the Kestrel 5 string output is useful here) or in SQL on numeric. Never go through `number`.
6. **Where does currency come from for historical quotes?** `Money` needs one, but I don't see a currency on `quotes`. I'm assuming all historical quotes are EUR. If that's wrong, tell me, because it changes the migration and the backfill.
7. **Four decimals to two is lossy.** Rate cards stored at four decimals (e.g. 18.3350) lose precision at 2 decimals. EUR and DKK both use 2 minor digits, so that's fine for the currency, but finance should confirm that rounding at conversion, rather than at 4 decimals, is acceptable. Have the backfill log how many rows were non-trivially rounded.
8. **bigint through node-pg arrives as a string.** `minor: number` is safe up to 2^53, which is fine here, but the parse must be explicit and must reject values outside the safe range.

## Recommended structure

Run the work in waves. The first wave is not fully parallel.

- **Wave 0 (Mon morning, about half a day, one agent or a person): contract and scaffolding.**
  - Land the `Money` type and a `roundHalfEven` / `toMinor(decimalString, currency)` utility in pricing, with tests for 18.3350 to 1834, 7.1250 to 712, and negatives.
  - Reserve migration numbers.
  - Agree the schema: `quotes.amount_minor`, `quotes.currency`, `invoices.currency`.
  - The other three agents start from this base.
- **Wave 1 (parallel):**
  - Agent A: pricing consumers and migration 0042.
  - Agent B: billing.
  - Agent C: Kestrel upgrade.
  - Agent D: backfill script, written and tested against a fixture database, not run on production.
- **Wave 2 (integration, Thursday):** merge in the order below and run the full suite.

Of the four, the Kestrel upgrade has the widest footprint. If you can, merge it first, on Tuesday, and have the other three rebase onto it. That removes the biggest source of surprise.

## The four agent prompts

Give each agent the shared section first.

**Shared preamble (paste at the top of every prompt)**

> Repo: TypeScript monorepo, Postgres, Kestrel ORM. You work in your own git worktree on your own branch. Do not edit files outside your area except as listed. Rules for everyone:
> - Money is `{ minor: number; currency: string }`. Rounding is always half-to-even, never `Math.round`, and never through floating-point `number`. Use `toMinor`/`roundHalfEven` from packages/pricing (from Wave 0).
> - Migration numbers are fixed: 0042 = pricing, 0043 = billing, 0044 = reserved. Do not take another number. Latest existing is 0041.
> - Schema contract: `quotes.amount_minor bigint` (nullable until the backfill completes), `quotes.currency text`, `invoices.currency text`. The old `quotes.amount numeric(12,4)` stays until after Friday.
> - CI builds a fresh database from the migrations on your branch. If your tests need something from another branch, stub it behind an interface and say so in your final report.
> - Finish with a report: files changed, migrations added, assumptions, anything that will conflict with the other three tasks.

**Prompt 1: packages/pricing**

> Task: replace float money with integer minor units in packages/pricing.
> - Change `Money` from `number` to `{ minor: number; currency: string }`. Replace every `Math.round` with half-to-even rounding on decimal strings. Currency exponent comes from a table (EUR 2, DKK 2), not hardcoded.
> - Add migration 0042: add nullable `quotes.amount_minor bigint` and `quotes.currency text`. Do NOT alter or drop `quotes.amount`, and do not convert the type in place (3.1M rows, lock, and Postgres round() is not half-to-even).
> - Read from `amount_minor` when present, otherwise convert from `amount` via `toMinor`. Parse bigint results (which arrive as strings) explicitly and throw if outside Number.MAX_SAFE_INTEGER.
> - Tests must cover ties and near-ties: 18.3350 gives 1834, 7.1250 gives 712, 0.005 gives 0, 0.015 gives 2, negatives, and strings with 4 decimals.
> - Export the public API that billing will consume and document it in the package README. Do not touch apps/billing or scripts/backfill.

**Prompt 2: apps/billing**

> Task: multi-currency invoice PDFs (EUR and DKK).
> - Add migration 0043: `invoices.currency text NOT NULL DEFAULT 'EUR'`. Do not create or edit 0042.
> - Render PDFs using the currency's exponent and symbol/format (DKK formatting differs from EUR, so use `Intl.NumberFormat` with the currency code, not manual string building). Never add amounts across different currencies; throw on a mismatch.
> - Read amounts only through the pricing package's public API. Pricing is being changed in parallel, so code against the `Money` shape `{ minor, currency }` and a thin adapter in apps/billing; do not copy pricing logic. Totals are summed in minor units as integers.
> - Tests: EUR and DKK invoices, mixed-currency rejection, rounding on line items that need it.
> - Do not touch packages/pricing or other migrations.

**Prompt 3: Kestrel ORM 4.x to 5.x**

> Task: upgrade Kestrel from 4.x to 5.x across the whole repo.
> - Read the full changelog, not just the headline. The known breaking change is that numeric/decimal columns now return strings instead of numbers. Find every read site (grep for each model and raw query touching numeric columns, including quotes.amount) and make it handle strings explicitly. Do not convert with `Number()` or unary `+` on money values. Hand the decimal string to the pricing conversion utilities where they exist, otherwise leave a clearly marked TODO and a typed wrapper.
> - Also check bigint handling, date/timestamp handling, migration runner behavior, and any query-builder changes.
> - Do not change business logic, rounding, or the Money type. Do not add migrations. Keep the diff mechanical so it can merge first.
> - Run every package's tests. In your report, list every call site that reads numeric columns, grouped by package.

**Prompt 4: scripts/backfill**

> Task: a one-off script to populate `quotes.amount_minor` and `quotes.currency` for about 3.1M historical rows.
> - Process in keyset-paginated batches (e.g. 5,000 rows by primary key), one transaction per batch, idempotent and resumable (only rows where `amount_minor IS NULL`). Have a `--dry-run`, a `--limit`, and progress logging.
> - Read `amount` as a decimal string (Kestrel 5 behavior; never go through a JS number). Convert with `toMinor` from packages/pricing using half-to-even. If pricing isn't available yet, implement the same rule locally behind an interface and flag it.
> - Currency for historical rows: assume EUR unless the data says otherwise. Make it a CLI parameter.
> - Verification: the script ends with a report, e.g. count converted, count where the 4-decimal value was rounded (any nonzero remainder), count of ties, and a check that `amount_minor/100` is within 0.005 of `amount` for every row. Fail loudly on any discrepancy.
> - Tests against a fixture database built from migrations through 0042, including 18.3350 and 7.1250 and values with zero decimals. Do not add migrations. Do not touch other packages.

## Friday merge plan

**Order** (rebase each branch onto the one before it, rerun CI after each merge):

1. **Kestrel upgrade (Tuesday ideally, no later than Wednesday).** Full test suite on all packages. The other branches rebase onto it.
2. **Pricing + 0042.** Verify migrations apply to a copy of production-sized data. Check lock times.
3. **Billing + 0043.** Check the migration number is unique and `Money` use matches.
4. **Backfill.** Merge the script, but do not run it yet.

**Checks before merging:**
- Run a script that lists `db/migrations` and fails on duplicate or gapped numbers.
- Rebuild a fresh database from the merged branch and run all packages' tests (not each branch's tests separately).
- Grep for `Math.round`, `Number(` and `parseFloat` near money fields; there should be none.
- Run the rounding tests (1834 and 712 as above) on the merged code.

**Production sequence (not Friday's merge):**
1. Deploy migrations 0042 and 0043, which are additive.
2. Deploy the code, which reads `amount_minor` with the fallback.
3. Dry-run the backfill on a production snapshot and review the report, including the count of rounded rows (show finance).
4. Run the backfill off-peak and monitor it.
5. Verify all rows are non-null and reconcile totals against the old column.
6. In a later release, add a migration to make `amount_minor` NOT NULL and drop `amount`.

Given the Denmark launch next month, I'd rather keep the destructive step out of Friday's release and have the billing code ready for DKK first.

## Things to confirm

- Is every historical quote EUR? If not, where does currency live?
- Does finance accept rounding 4-decimal rate-card values to 2 decimals at conversion?
- Can the Kestrel upgrade merge early (Tuesday or Wednesday)? It's the biggest lever on merge risk.
