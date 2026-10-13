I'd push back on running all four at once. Your "clean merge" expectation holds for the file layout, but these four tasks depend on each other in ways that will break at merge time or in CI. Below is a phased plan, then the four prompts, then the Friday merge plan.

## Why not fully parallel

- **Task 4 depends on task 1.** The backfill converts rows into the new column type and units. It can't be written or run until the Money representation and the migration are settled.
- **Task 2 depends on task 1.** Invoices read amounts through `packages/pricing`, so billing code written against the old `number` Money type will not compile after task 1 lands.
- **Tasks 1 and 3 both touch `packages/pricing`.** Task 3 changes how numeric columns are read (strings, not numbers), and task 1 changes the Money type. Both will edit the same mapping and arithmetic code, so they are not in separate packages.
- **Tasks 1 and 2 both need a migration.** Task 1 converts `quotes.amount` and task 2 adds `invoices.currency`. Both would claim `0042`. The CI runs each branch against a fresh database built from its migrations, so the numbering collision will show up as a failure, not just a rename.
- **Rounding is decided in the wrong place.** Finance wants half-to-even everywhere, and the code uses `Math.round` (half toward +infinity). Two agents touching rounding will make different choices unless one owner decides the helper first.

## Phased plan

- **Phase 0 (you, about 30 minutes, before any agent starts):** decide the minor-unit scale, the rounding helper signature, and the migration numbers. Write these down in a shared decisions file that every agent reads.
- **Phase 1 (parallel):** task 1 (pricing and migration `0042`) and task 3 (Kestrel upgrade in worktrees, but it must rebase onto task 1 for pricing files). Task 3 can start on everything outside `packages/pricing` now.
- **Phase 2:** task 2 (billing, migration `0043`), started after task 1's Money type is merged to a integration branch.
- **Phase 3:** task 4 (backfill script), run only after the column change migrations have been applied in a staging database.

## Decisions to make before Phase 0 ends

1. **Minor-unit scale.** EUR and DKK have two minor digits (cents, øre). The historical values `18.3350` and `7.1250` have four decimals. Converting to cents loses precision, so either:
   - store `bigint` at a finer scale (for example 1/10000 of a unit, which matches the existing numeric(12,4)), and then document that `minor` is not always cents, or
   - round to cents at conversion and record the rounding delta per row so finance can audit it.
   Finance has to choose. I'd recommend the second for the audit trail, but this is their call.
2. **Rounding helper.** One function, `roundHalfToEven(value, scale)`, in `packages/pricing`. Replace every `Math.round` call with it. Be careful: half-to-even on binary floats is still subject to float error, so the input should already be a decimal string or integer, not a float.
3. **Migration numbers.** Assign `0042` to the pricing change and `0043` to the billing change now. Kestrel's 5.x migration tooling may also generate migrations; check that first.
4. **Currency default.** Existing invoices need `currency` backfilled to `EUR`. Confirm this in the migration, not in the backfill script.

## The four agent prompts

Each agent runs in its own worktree (`isolation: worktree`). Each reads the decisions file first and must not edit files outside its scope.

**Agent 1, pricing (Phase 1)**

> You are working in the dispatch monorepo (TypeScript, Postgres, Kestrel ORM 4.x). Scope: `packages/pricing` and `db/migrations/0042_*.sql` only. Do not touch other packages.
> 1. Change `Money` from `number` to `{ minor: number; currency: string }`. Use integer arithmetic only.
> 2. Replace every `Math.round` in this package with `roundHalfToEven` from the decisions file. Add unit tests for ties (0.5 rounds to even), negative values, and the values 18.3350 and 7.1250.
> 3. Write migration `0042` converting `quotes.amount` from `numeric(12,4)` to `bigint` using the scale in the decisions file. Do not convert data here; that's task 4.
> 4. Run `packages/pricing` tests against a fresh database built from migrations 0001 to 0042.
> 5. Report: files changed, the exact `Money` type signature, and any place the old number API is still used outside this package (list them, don't fix them).

**Agent 2, Kestrel upgrade (Phase 1, pricing files deferred)**

> You are working in the dispatch monorepo. Scope: the Kestrel ORM package version across the repo, and all code outside `packages/pricing`.
> 1. Upgrade Kestrel from 4.x to 5.x. Read the 5.x changelog and list every breaking change, not only the headline one.
> 2. Find every numeric/decimal column read in the repo. Because they now return strings, add explicit parsing at the boundary, not inside arithmetic code.
> 3. Do not edit `packages/pricing`. Instead, list the exact lines there that need changes and send them to the integration step.
> 4. Run each package's tests against a fresh database.
> 5. Report: the version bump, the list of breaking changes, every read site changed, and the pricing lines left for later.

**Agent 3, billing (Phase 2)**

> You are working in `apps/billing`, after task 1 is merged to the integration branch. Scope: `apps/billing` and `db/migrations/0043_*.sql`.
> 1. Write migration `0043` adding `invoices.currency` as `text not null default 'EUR'` (existing rows get EUR).
> 2. Generate multi-currency PDFs for EUR and DKK. Format amounts with the currency's minor-unit scale from the decisions file, not hardcoded two decimals.
> 3. Read amounts only through the pricing package's `Money` API. Do not parse or divide amounts yourself.
> 4. Add tests for a DKK invoice, an EUR invoice, and a legacy row with no explicit currency.
> 5. Report: files changed, the PDF formatting rules used, and test results against a fresh database built from 0001 to 0043.

**Agent 4, backfill (Phase 3)**

> You are writing `scripts/backfill`, a one-off script that converts the 3.1M historical `quotes` rows from the old `numeric(12,4)` values into the new `bigint` minor units. Run it only after migrations 0042 and 0043 are applied.
> 1. Process in batches of 5,000 keyed on primary key. Each batch runs in its own transaction, so it can be resumed after a failure.
> 2. Use `roundHalfToEven` from the pricing package. Do not reimplement rounding.
> 3. Write a per-row log of any row where rounding changed the value, for finance to review.
> 4. Make it idempotent: rows already converted are skipped (use a marker column or a check on the stored type; decide which and state it).
> 5. Test on a copy of 10,000 rows, including 18.3350 and 7.1250. Do not run against production.
> 6. Report: batch size, idempotency method, row count tested, rounding-delta count.

## Friday merge plan

1. **Merge order:** pricing (Agent 1) first, then Kestrel upgrade (Agent 2) rebased onto it, then billing (Agent 3), then the backfill script (Agent 4). Don't merge in parallel.
2. **Migrations:** check that `0042` and `0043` are the only new migration files and that no other numbers were claimed. Run the full migration chain on a fresh database after each merge, not only at the end.
3. **Conflicts to expect:** `packages/pricing` (tasks 1 and 2 both touch it), the Kestrel lockfile (task 2 may change generated types), and any shared `Money` helper. Resolve pricing conflicts by keeping task 1's version and re-applying task 2's read-site parsing on top.
4. **Gate after each merge:** the package tests for every touched package, plus a fresh-database build from migrations. Do not merge the next step until the gate passes.
5. **Backfill last, on staging:** run task 4 on a staging copy of production, compare the sum of converted amounts against the sum of the old numeric values (the difference should equal the logged rounding delta), and only then schedule production.
6. **Finance sign-off:** before production backfill, finance reviews the rounding-delta log and approves the minor-unit scale decision.

## Assumptions I made

- Kestrel 5.x ships with a migration generator, so you may not need to hand-write the Kestrel-side schema changes. Verify against the 5.x docs.
- The four tasks run in one repo with one shared CI configuration.
- "Friday" is the single merge window, so the phased plan fits before it.
- I have not seen the codebase, so the file paths beyond those you named are unknown. The agent prompts ask them to list what they find, not assume.
