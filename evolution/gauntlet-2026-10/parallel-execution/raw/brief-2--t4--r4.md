Four agents can run at once, but the merge won't be clean. Some of the work isn't independent even though it sits in different packages. I'd change a few things before launching, then use the prompts and plan below.

## Where the four tasks collide

1. **Agent 4 is built on the wrong migration.** `ALTER COLUMN amount TYPE bigint` on a numeric(12,4) column casts in place. 18.3350 becomes 18, with no x100 scaling, and Postgres rounds half away from zero. The historical data would be destroyed before the backfill runs. It also rewrites 3.1M rows under an exclusive lock. Use expand/contract instead:
   - Migration A adds `quotes.amount_minor bigint NULL` (and `currency` if quotes don't have one).
   - The backfill fills it in batches.
   - A later migration, after verification, sets NOT NULL, switches reads, and drops `amount`.
   - Agent 1 therefore ships only migration A on Friday. The drop comes in a follow-up release.

2. **Migration numbers will collide.** Agents 1 and 2 will both take 0042, and the Kestrel agent may as well. CI builds a fresh DB per branch, so each branch passes alone and the merged result breaks. Reserve numbers now: 0042 for pricing (`quotes.amount_minor`), 0043 for billing (`invoices.currency`), and 0044+ for Kestrel only if it needs one. Agents must not take any other number.

3. **Kestrel 5 changes how numerics come back.** Decimals arrive as strings. That hits `quotes.amount` reads in pricing, and invoice amounts in billing. Agents 1 and 2 will be coding against the 4.x behaviour (JS numbers) while Agent 3 changes it underneath them. Each of them will pass its own tests on its own branch.
   - Land Kestrel first, or at least first among the merges, in its own PR.
   - Tell Agents 1 and 2 to treat DB numerics as strings and parse them with a decimal parser, never `Number()` or `parseFloat`. Then they're correct on both 4.x and 5.x.
   - `amount_minor` as bigint may also come back as a string (or a BigInt) under Kestrel 5. Agent 3 must document what it returns, and Agent 1 must handle both.

4. **Billing depends on the pricing API.** Agent 2 reads amounts through the pricing package, so it can't build against `{ minor, currency }` until that type exists. Have Agent 1 commit the `Money` type and helper signatures (`fromDecimalString`, `add`, `format`, `exponentFor(currency)`) as the very first commit. Merge that to main today, and have Agent 2 branch from it. This is the one hard dependency, and it's cheap to fix.

5. **Rounding changes the money.** Half-to-even is a behaviour change, not just a refactor.
   - 18.3350 at 2 decimals is 1833.5 minor units, so half-even gives 1834 (Math.round also gives 1834).
   - 7.1250 is 712.5 minor units, so half-even gives 712, where Math.round gives 713. That's a one-cent difference on a legitimate historical row.
   - In floats, 18.335 * 100 is 1833.4999999999998, so a float-based path rounds wrongly regardless of mode.
   - Do the rounding on the decimal string or on integers, never through a float multiply.
   - Pricing and the backfill must share one rounding function. Agent 4 should import it from pricing, not reimplement it.

6. **Four-decimal values lose precision at two-decimal minor units.** Ask finance to confirm that 18.3350 becoming 18.34 is acceptable, or whether those partner rate cards need a finer scale. The per-currency exponent also matters: DKK and EUR are both 2, but build it as a lookup anyway. I've assumed historical quotes are all EUR, so please confirm that.

## Revised sequence

- **Today:** Agent 1 commits the `Money` contract and the shared rounding function; this merges to main immediately. Agent 3 (Kestrel) starts at the same time.
- **Days 1-3, in parallel:** Agent 1 (rest of pricing plus migration 0042), Agent 2 (billing, from the contract commit), Agent 3 (Kestrel), and Agent 4 (backfill script, written and tested against a seeded DB, not run).
- **Merge order on Friday:** Kestrel, then pricing, then billing, then backfill. Rebase each branch onto the previous one before merging.
- **After Friday:** run the backfill on staging, then production. This is a separate step from the merge.

## Agent prompts

**Shared preamble (put at the top of all four prompts)**

> You work in your own git worktree of the Larkspur dispatch monorepo (TypeScript, Postgres, Kestrel ORM). Only edit files in your assigned area, with the exceptions listed. Migrations live in db/migrations; you may only create the migration numbers assigned to you. Never use floats for money: parse database numerics as strings, and do rounding on decimal strings or integers, half-to-even (banker's rounding), never `Math.round`. Run your package's tests against a DB built from your branch's migrations. End with a report: files changed, decisions made, assumptions, anything another agent must know.

**Agent 1: packages/pricing**

> Task: replace float money with integer minor units.
> 1. First commit, by itself: change `Money` to `{ minor: number; currency: string }` and export the helper signatures (`fromDecimalString(str, currency)`, `toDecimalString`, `add`, `subtract`, `multiplyRate`, `format`, `exponentFor(currency)`). Add one exported `roundHalfEven` function working on integers or decimal strings. Add tests for 18.3350 -> 1834 and 7.1250 -> 712 (2-decimal minor units), plus negatives and exact halves. Tell me when this commit is ready, because Agent 2 and Agent 4 depend on it.
> 2. Then migrate the rest of pricing. Replace every `Math.round` with `roundHalfEven`. Treat `minor` as a safe integer and reject values beyond it.
> 3. Migration 0042 (the only number you may use): add `quotes.amount_minor bigint NULL`. Do not alter or drop `quotes.amount`; a backfill will populate the new column on 3.1M rows later. Include a currency column on quotes only if one doesn't exist; state which you found.
> 4. Read `quotes.amount` as a string. Be tolerant of both Kestrel 4.x (number) and 5.x (string) return types.
> 5. Report any callers outside pricing that break from the type change.

**Agent 2: apps/billing**

> Task: multi-currency invoice PDFs (EUR and DKK).
> Branch from the commit where Agent 1 published the `Money` contract. Use only the pricing package's public API for amounts; do not do your own arithmetic or rounding.
> 1. Migration 0043 (the only number you may use): add `invoices.currency` (text, NOT NULL with a default of 'EUR' for existing rows, with a check constraint on allowed codes).
> 2. Render PDFs using `format` and `exponentFor` from pricing, with the right locale conventions for DKK (for example `1.234,56 kr.`) and EUR. Ensure the PDF font supports the characters needed.
> 3. Treat DB numerics as strings; never use `Number()` on them.
> 4. Test cases: EUR invoice, DKK invoice, mixed-currency line items rejected with a clear error, and rounding at exact halves.
> 5. Do not edit packages/pricing. If you need a change there, list it in your report.

**Agent 3: Kestrel ORM 4.x to 5.x**

> Task: upgrade across the whole repo.
> 1. Upgrade, fix compile errors and test failures. Keep changes mechanical and minimal. Do not refactor money logic; Agents 1 and 2 are changing it concurrently, so avoid unnecessary edits in packages/pricing and apps/billing and keep any edits there tiny.
> 2. The headline change is that numeric/decimal columns now return strings. Find every place that depends on them being numbers (arithmetic, comparisons, `toFixed`, JSON serialization, sorting). Fix with minimal, explicit string handling, not `Number()` or `parseFloat` on money. List each site in your report.
> 3. Check and document what bigint columns return in 5.x (string, BigInt, or number), and whether 3.1M-row batch/stream reading changed.
> 4. Verify the migration runner still works and that the 0001-0041 migrations apply cleanly to a fresh DB. If you need a migration, use 0044 and tell me why.
> 5. This PR merges first, so keep it self-contained and green on its own.

**Agent 4: scripts/backfill**

> Task: a one-off script converting historical quotes to minor units.
> 1. Populate `quotes.amount_minor` from `quotes.amount` (the column from migration 0042, which Agent 1 is adding; use that name and stub it locally in a fixture until it lands). Do not alter or drop `amount`.
> 2. Import `fromDecimalString` and `roundHalfEven` from packages/pricing once Agent 1's contract commit is available. Do not write your own rounding. Read amounts as strings, converting in SQL with `amount::text` if needed.
> 3. Requirements: batched by primary-key range (about 10k rows), resumable, idempotent (only rows where `amount_minor IS NULL`), a `--dry-run` mode, a `--currency` default of EUR with a clear error if a quote's currency is unknown, a progress log, and short transactions to avoid long locks on 3.1M rows.
> 4. Verification pass: count of unconverted rows, and a sample comparison of `amount_minor` against `amount` at the right scale. Report rows where rounding actually changed the value (any 4-decimal values with a nonzero third or fourth digit) and write them to a CSV for finance.
> 5. Tests on a seeded DB, including 18.3350 -> 1834, 7.1250 -> 712, zero, negatives, and very large values. Do not run against real data.

## Friday merge plan

1. **Thursday: dry-run integration.** Create an `integration` branch from main. Merge the four branches in this order: Kestrel, pricing, billing, backfill. Build a fresh DB from the combined migrations (0042 and 0043 must apply cleanly), run the full test suite, and fix conflicts there, not on main.
2. **Friday merge order:** Kestrel (it needs only its own CI), then pricing rebased on it, then billing rebased on pricing, then backfill. Rebase after each merge and re-run CI each time.
3. **Gates before each merge:** zero `Math.round` left in money paths (grep), zero `Number(`/`parseFloat` on DB numerics, and no duplicate migration numbers.
4. **Deploy order:** deploy the code first and apply migrations 0042 and 0043 (both additive and safe). Do not deploy anything that reads `amount_minor` as authoritative yet.
5. **Backfill:** run on staging, review the rounding-change CSV with finance, then run on production in off-peak hours. Verify zero NULL `amount_minor` rows.
6. **Follow-up release:** switch reads to `amount_minor`, then drop `amount` in a later migration.
7. **Rollback:** Kestrel and code merges are revertible. Since migrations are additive, rolling back costs nothing but a redeploy.

## Questions to settle before launch

- Is 2-decimal rounding of the four-decimal rate-card values acceptable to finance?
- Are all historical quotes EUR?
- Does `quotes` already have a currency column?
- Is the Denmark launch date firm? If so, billing is the critical path, so put your best agent on the pricing contract commit.
