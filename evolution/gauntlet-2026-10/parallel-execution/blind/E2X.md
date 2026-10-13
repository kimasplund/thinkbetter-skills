I can write all four prompts and the merge plan, but I'd change the setup first. These four jobs are not independent, so "different packages, clean merge" probably won't hold. Four agents running blind to each other will give you a Friday merge full of semantic breakage, even if git reports no textual conflicts.

## Where the work is coupled

1. **Kestrel 5 changes the type pricing reads.** numeric/decimal columns come back as strings. Task 1 is rewriting how pricing reads and writes `quotes.amount`, and task 2 reads amounts through pricing. Both are built on the behaviour task 3 changes. One branch assumes numbers, another assumes strings, and the type checker won't catch it if the Kestrel typings are loose.
2. **Billing depends on the new `Money` shape.** Task 2 consumes `{ minor, currency }`. Until that contract is fixed, the billing agent will invent its own.
3. **Migration numbering collides.** Tasks 1 and 2 both add migrations, and each agent will pick 0042. Merging gives a duplicate number. Because CI builds a fresh database from each branch's migrations, the problem is hidden until Friday.
4. **CI on a single branch can't see the other branches' schema.** Billing tests need `quotes`/`currency` changes from pricing. The backfill needs the new column from task 1. Each branch will fail or mock around the gap.
5. **Tasks 1 and 4 overlap.** Task 1 says the migration converts `quotes.amount` from numeric(12,4) to bigint. Task 4 says a script converts 3.1M rows afterwards. An in-place `ALTER ... TYPE bigint` can't wait for a later script. It would convert (and round) every row inside the migration, with a long table lock and no chance to review the rounding.
6. **Rounding is a correctness trap, not a style choice.** Finance wants half-to-even. `Math.round` is half-up, and on floats it is also unreliable at ties. Your own examples show it:
   - 7.1250 is an exact tie at 2 decimals. Half-to-even gives 7.12. `Math.round(712.5)` gives 713.
   - 18.3350 is a tie at 3 decimals. Half-to-even to 2 decimals gives 18.34 because the preceding digit, 3, is odd. In floating point, 18.335 is stored as something like 18.33499999999999943, so float arithmetic can land on 18.33 or 18.34 for the wrong reason.
   - So the rounding must work on decimal strings or integers, never on float multiplication such as `amount * 100`. This matters most for the backfill and the migration, which both touch historical data. The Kestrel upgrade helps here, since values now arrive as exact strings.
7. **Minor-unit exponent is per currency.** EUR and DKK both use 2, but the code shouldn't hardcode 100. Use a currency table.
8. **Currency for historical quotes.** The existing rows have no currency. Assume EUR, since DKK is launching next month, but get this confirmed by a human before the backfill runs on production.

## Recommended structure

Don't start all four at once. Fix the shared contract first, then run in two waves.

**Step 0, Monday morning, one owner (about half a day).** Merge to the main branch, as a small PR:
- A `Money` type, a `CURRENCY_EXPONENT` table, and a pure `roundHalfEven(decimalString, exponent)` function in packages/pricing, with unit tests covering 7.1250 -> 7.12, 18.3350 -> 18.34, 0.5/1.5/2.5 style ties, and negatives.
- A `toMinor(decimalString, currency)` and `fromMinor` helper that use only strings and integers. No `Math.round`, no float multiplication.
- Reserved migration numbers: **0042** pricing, **0043** billing (`invoices.currency`), **0044** the finalisation swap after the backfill.
- An agreed policy for bigint in application code: treat as a string or `bigint` at the ORM boundary and convert deliberately. Do not rely on `number`.

**Wave 1 (parallel, Mon to Tue):** agent 3 (Kestrel upgrade) and agent 1 (pricing). They touch different things if scoped properly (see prompts).

**Wave 2 (parallel, Wed to Thu):** agent 2 (billing) and agent 4 (backfill), each branched from the merged result of wave 1, so they build on real code and a real schema.

This gives you most of the parallelism with far fewer surprises. If the Friday deadline is fixed, agents 2 and 4 can start in wave 1 against the Step 0 contract, but expect to rebase and re-test them on top of 1 and 3 before Thursday.

**Schema approach** (settles the overlap between tasks 1 and 4). Use expand, backfill, contract rather than one in-place type change:
- 0042: add `quotes.amount_minor bigint NULL` and `quotes.currency text NULL`. Fast, with no rewrite.
- Backfill script (task 4) fills them in batches.
- 0044: after verification, set NOT NULL, switch reads over, and drop or rename the old `amount` column.
- Fresh-database CI still works, since an empty table passes any constraint.

## Prompts

### Agent 3: Kestrel ORM 4.x to 5.x (first to merge)

> You are upgrading Kestrel ORM from 4.x to 5.x across the Larkspur dispatch TypeScript monorepo (Postgres). Work in your own git worktree on branch `kestrel-5`.
>
> Goal: a behaviour-preserving upgrade. The headline breaking change is that numeric/decimal columns now return strings instead of JS numbers. Read the full 5.x changelog and list every other breaking change before editing.
>
> Scope: dependency bumps, ORM config, and the minimum code needed to keep every package compiling and passing. Do NOT change the `Money` type, add migrations, touch invoice PDFs, or change rounding. Another agent is changing packages/pricing at the same time.
>
> Rules:
> 1. Find every place a numeric/decimal column is read (quotes.amount, invoices, anything else). Make the conversion explicit at the boundary, e.g. a single `parseDecimal` adapter, so existing callers still receive numbers for now. Do not scatter `Number(x)` calls, and do not use `parseFloat` on money values without a comment. Put the adapter in one file so the pricing agent can later replace it.
> 2. Also check bigint, `count()` and aggregate results (`sum`, `avg`), which are commonly strings in Postgres drivers. Add tests.
> 3. Keep changes inside packages/pricing to a minimum: only the adapter call sites, listed in your PR description.
> 4. Do not renumber or add anything in db/migrations.
> 5. Run each package's tests against a fresh database built from the migrations. All must pass.
>
> Deliverable: a PR description with (a) the list of breaking changes found and how each was handled, (b) every file touched in packages/pricing, (c) any place where behaviour could differ at runtime but is not covered by tests.

### Agent 1: pricing, integer minor units

> You are changing money handling in packages/pricing of the Larkspur dispatch monorepo (TypeScript, Postgres, Kestrel ORM). Work in your own git worktree, branched from main after the Step 0 contract PR.
>
> Goal: `Money` changes from `number` to `{ minor: number; currency: string }`. Amounts are integer minor units. Use the shared `CURRENCY_EXPONENT` table, never a hardcoded 100.
>
> Rules:
> 1. Rounding must be **half-to-even** everywhere (finance and the auditors require it). Replace every `Math.round` in pricing. Do not do money arithmetic by multiplying floats. Use the `roundHalfEven` / `toMinor` helpers from Step 0, which work on decimal strings and integers. Add tests for ties: 7.1250 -> 7.12, 18.3350 -> 18.34, 2.5 -> 2, 3.5 -> 4 at exponent 0, and negatives.
> 2. Percentages, tax and discount calculations must round once at the end of each defined step, and you must document where.
> 3. Use migration **0042** only, in the expand style: add `quotes.amount_minor bigint NULL` and `quotes.currency text NULL`. Do NOT alter or drop `quotes.amount` and do NOT backfill rows; the backfill script and migration 0044 handle that. Keep reads working from the old column until then, behind one clearly marked function.
> 4. Another agent is upgrading Kestrel (numeric columns now come back as strings). Write your column reads against string input, via the single adapter if it exists. Do not assume numbers.
> 5. Export a small, stable public API (type, constructors, add/subtract/multiply-by-rate, format). Billing will consume it. List every exported symbol in your PR description.
> 6. Check that integer minor units stay below Number.MAX_SAFE_INTEGER, or use bigint where they might not.
> 7. Run the package tests against a fresh database built from the migrations on your branch.

### Agent 2: apps/billing, multi-currency invoice PDFs

> You are adding multi-currency invoice PDFs to apps/billing in the Larkspur dispatch monorepo, for a Denmark launch next month (DKK alongside EUR). Start your worktree from main after the pricing and Kestrel branches have merged, so you build against the real `Money` type.
>
> Rules:
> 1. Use migration **0043**: add `invoices.currency` (text, NOT NULL with a default of `'EUR'` for existing rows, with a CHECK or foreign key against supported currencies). Do not use any other migration number.
> 2. Read amounts only through the pricing package's public API. Never read the old float amount or do your own arithmetic or rounding. If you need something pricing doesn't export, write it down in the PR description rather than adding it yourself.
> 3. PDF formatting: use the locale-aware formatter with the exponent from the currency table. Check DKK (decimal comma, `kr.` placement) and EUR. Test totals for invoices with 1, 2 and many line items, and confirm that line totals sum to the invoice total exactly (no penny drift from rounding per line versus on the total). State your choice and keep it consistent.
> 4. An invoice must never mix currencies. Fail loudly if line items disagree.
> 5. Numeric columns arrive as strings after the Kestrel upgrade; do not assume numbers.
> 6. Add snapshot or visual tests for one EUR and one DKK invoice.
> 7. Run billing's tests against a fresh database built from the migrations on your branch.

### Agent 4: scripts/backfill, historical quotes

> You are writing a one-off backfill script in scripts/backfill for the Larkspur dispatch monorepo. Start from main after the pricing branch (migration 0042) has merged. The script fills `quotes.amount_minor` and `quotes.currency` from `quotes.amount` for roughly 3.1M historical rows.
>
> Rules:
> 1. **Rounding is half-to-even, done on exact decimals.** Never convert through a JS float. Either do it in SQL on the numeric value or use the string-based `toMinor` helper. Known tricky inputs: 7.1250 -> 712 (not 713), 18.3350 -> 1834, plus four-decimal values from partner rate cards. Include a test fixture with such ties and with values like 0.0050, 0.0150, and negatives, if any exist.
> 2. Currency: assume EUR for all historical rows unless the data says otherwise. Make this an explicit, required CLI argument, not a silent default, because a human must confirm it before the production run.
> 3. Batch by primary key range (for example 5k to 20k rows per batch), one transaction per batch, with a configurable sleep, so you don't lock the table or bloat the WAL. Only touch rows where `amount_minor IS NULL`, so it is resumable and idempotent. Log progress and the last processed id.
> 4. Support `--dry-run`, which reports how many rows would change and how many are ties that rounding changed, plus the total rounding difference. Finance will want that number.
> 5. After the run, a verification mode must confirm: no NULLs left, row count unchanged, and for every row `amount_minor` equals the half-to-even rounding of `amount`. Report any mismatches.
> 6. Do NOT run migration 0044 (set NOT NULL, switch reads, drop the old column). Draft it separately and mark it as run only after verification.
> 7. Do not run this against production. Test it against a seeded database of at least a few hundred thousand rows, and report the timing.

## Merge plan for Friday

Order matters: **Kestrel (3), pricing (1), billing (2), backfill (4).**

**Before Friday**
- Wednesday: merge 3, then 1. After each, rebase the others and run the full CI.
- Thursday: merge 2 and 4 after rebasing. Friday should be a release day, not the first integration day.

**On each merge**
1. Check the migration directory: numbers 0042, 0043 and 0044 each appear once, in order, with no gaps and no duplicates. Add a CI check that fails on duplicates.
2. Rebuild a fresh database from migrations on the merged result and run **all** packages' tests, not just the one that changed.
3. Grep the merged tree for `Math.round`, `parseFloat`, and `* 100` on money paths. There should be none.
4. Run the rounding fixtures (7.1250, 18.3350, ties, negatives) end to end through the pricing code, the SQL migration and the backfill. All three must agree.
5. Type-check with strict mode to catch any remaining `number` versus `string` versus `Money` mismatches.

**Before the production backfill**
- Restore a recent production snapshot to staging, run the dry-run, and give finance the rounding-difference total.
- Confirm the currency assumption.
- Schedule the backfill off-peak, run it, run verification, then ship 0044 in a later deploy. Do not combine the backfill and 0044 in one release.
- Rollback: the old `amount` column stays until 0044, so reverting the application code is safe until then.

**Risks to watch**
- Billing launching DKK before the backfill and 0044 are done. Gate DKK on a feature flag.
- Anything outside these four packages reading quotes through raw SQL or the ORM. Grep for `quotes.amount` across the whole repo, including apps and scripts not listed here.
- Reports or exports that sum amounts, which will now silently mix minor and major units.

I assumed the monorepo has other consumers of `quotes.amount`, that EUR is the right historical currency, and that you want the old column kept until verification. If any of these is wrong, tell me and I'll adjust the prompts.
