Four agents can run in parallel, but not all at once from the same base, and the merge will not be clean. The four items are in different packages, but they depend on each other:

- Item 2 (billing) reads `Money`, so it depends on the type change in item 1.
- Item 3 (Kestrel 5) changes how every numeric column is read, including `quotes.amount`. It also changes `package.json` and the lockfile, which every worktree would touch.
- Item 4 (backfill) needs the item 1 migration applied and the item 3 string handling in place.

Running all four at once from current main will produce conflicts in `packages/pricing`, in the lockfile, and at every `Money` call site. The sequencing below still uses four agents, in two waves of two.

## Sequencing

**Wave 1 (parallel, one worktree each, from current main)**
- Agent A: pricing and migration (item 1)
- Agent C: Kestrel 5 upgrade (item 3)

Merge C first, since it is mechanical and wide. Then rebase A onto main and merge it.

**Wave 2 (parallel, branched from main after wave 1 merges)**
- Agent B: billing multi-currency (item 2)
- Agent D: backfill script (item 4). It is written and tested against a staging copy and is not run against production until the migration is deployed.

## Decisions to confirm before Friday

I could not check the repo or the Kestrel 5 changelog, so these are assumptions.

1. **Minor unit precision.** Two-decimal minor units (cents, øre) is the natural reading, but rate cards carry four decimals (18.3350, 7.1250). At two decimals, 18.3350 becomes 1833.5 minor units, which half-to-even takes to 1834. 7.1250 becomes 712.5, which becomes 712. Sub-cent amounts are lost, so totals change. Finance should confirm this. I recommend keeping the original `numeric(12,4)` value in an audit column so the rounding can be re-derived later.

2. **Migration shape.** An in-place `ALTER COLUMN ... TYPE bigint` does not fit the plan. Postgres casts numeric to bigint by rounding half away from zero, not half-to-even, and it discards the decimals before the backfill can read them. I recommend the following instead. Migration 0042 adds `amount_minor bigint` and leaves `amount` alone. The backfill fills `amount_minor`. A later migration drops `amount` after the code has switched over.

3. **Migration numbers.** The latest is 0041. Agent A takes 0042. Agent B must check main when it starts in wave 2 and take the next free number. A duplicate number breaks the fresh-database CI build.

4. **Rounding.** `Math.round` rounds .5 toward positive infinity, so -2.5 becomes -2. Half-to-even needs its own helper. Every existing `Math.round` call site will change output on .5 cases, so finance should review the expected deltas. Where possible, do the arithmetic in integers, because float intermediates can land x.5 cases on the wrong side.

5. **Default currency.** I assume every existing invoice is EUR. Agent B backfills `currency = 'EUR'` explicitly in its migration.

## Agent prompts

Each agent runs with `isolation: worktree`.

**Agent A (pricing and migration)**

```
You are working in a git worktree of the Larkspur Couriers dispatch monorepo (TypeScript, Postgres, Kestrel ORM).

Scope: packages/pricing and one new migration. Do not edit apps/billing or scripts/backfill. You may edit call sites of Money outside packages/pricing only where needed to keep the repo type-checking. List every such file in your report.

1. Change Money from number to { minor: number; currency: string }. minor is an integer count of minor units (cents or øre for EUR and DKK). Provide fromMajor(amount: string, currency), toMajor, add (same currency only; throw otherwise), and format. Parse decimal strings exactly. Do not go through float.
2. Add packages/pricing/src/rounding.ts exporting roundHalfEven. Replace every Math.round in packages/pricing with it. Add tests for 0.5, 1.5, 2.5, -2.5, -3.5, and values that are .5 only after float error. Afterwards, grep to confirm there is no Math.round left in packages/pricing.
3. Add db/migrations/0042_quote_minor_units.sql. It adds quotes.amount_minor bigint, nullable. Do not alter or drop quotes.amount, and do not use ALTER COLUMN TYPE. The migration must apply cleanly to a fresh database built from migrations 0001 through 0042.
4. Run the package tests against a fresh database built from the migrations on this branch.

Report: files changed, call sites outside pricing you changed, the exported signatures other agents depend on (Money, fromMajor, roundHalfEven), and test results.
```

**Agent B (billing, wave 2)**

```
You are working in a git worktree of the Larkspur Couriers dispatch monorepo. Your branch starts from main, which now contains the pricing changes and the Kestrel 5 upgrade.

Scope: apps/billing and one new migration. Do not edit packages/pricing except to import from it.

1. Check the highest-numbered file in db/migrations on main and use the next number for your migration. It adds invoices.currency text not null, backfills existing rows to 'EUR', and adds a check constraint allowing only 'EUR' and 'DKK'.
2. Read all invoice amounts through the Money type and format helpers from packages/pricing. Never read quotes.amount or amount_minor directly in billing code.
3. Render invoice PDFs in the invoice's currency. Mixed-currency invoices are rejected with an error.
4. Tests: snapshot or fixture tests for one EUR and one DKK invoice, and a test that a mixed-currency invoice is rejected. Run them against a fresh database built from the migrations on this branch.

Report: migration number used, files changed, and test results.
```

**Agent C (Kestrel 5 upgrade, wave 1)**

```
You are working in a git worktree of the Larkspur Couriers dispatch monorepo (TypeScript, Postgres, Kestrel ORM).

Scope: upgrade Kestrel ORM from 4.x to 5.x across the whole repo. Read the 5.x changelog and migration guide first. The headline breaking change is that numeric and decimal columns now return strings, not JS numbers.

1. Find every numeric and decimal column in the schema, not just quotes.amount. Find every read site.
2. Fix each read site. Convert at the boundary with an explicit parser. Look for places where a string now behaves differently, such as + concatenation, comparisons, or sums done in JS.
3. Do not change pricing math in packages/pricing beyond what the string change forces. Agent A is changing that package at the same time, so keep those edits minimal and list them.
4. Do not add or change migrations.
5. Run every package's tests against a fresh database built from the migrations on this branch.

Report: the upgrade diff summary, every numeric and decimal column with its read sites, and every place that relied on a numeric value being a JS number.
```

**Agent D (backfill, wave 2)**

```
You are working in a git worktree of the Larkspur Couriers dispatch monorepo. Your branch starts from main, which now contains the migration that adds quotes.amount_minor and the pricing helpers.

Scope: scripts/backfill only.

1. Write a one-off script that fills quotes.amount_minor for every row where it is null. Use the Money helpers and roundHalfEven from packages/pricing. Convert from the decimal string exactly, by moving the decimal point and rounding the remainder half-to-even. Do not convert via float.
2. Process rows in batches of 5,000, ordered by id. Each batch runs in its own transaction. The script is idempotent: it only touches rows where amount_minor is null.
3. Support --dry-run, which prints row counts and per-currency totals and writes nothing.
4. Verification: for every row, |amount_minor - amount * 100| must be at most 0.5. Report the number of exact .5 ties, the per-currency totals before and after, and the difference.
5. Test with fixtures that include 18.3350, 7.1250, and exact .5 cases. Do not run the script against production. Add a unit test so CI exercises it on a fresh database.

Report: the script's path, test results, and the dry-run output on the fixtures.
```

## Friday merge plan

1. Freeze main for the merge window. No direct commits.
2. Merge C (Kestrel 5). CI green for every package.
3. Rebase A onto main, resolve conflicts, and merge. CI green.
4. Rebase B onto main, confirm its migration number is the next free one, and merge. CI green.
5. Merge D.
6. After each merge, run the type check across the monorepo, each package's tests on a fresh database, `grep -r "Math.round" packages/pricing` (expect no output), and a search for remaining numeric string-handling problems.
7. Rollout order: apply migrations to staging. Run the backfill dry run on staging and compare per-currency totals against the pre-migration totals. Run the backfill for real on staging, then on production in off-hours batches. Switch reads to amount_minor. Drop amount in a later migration, after a release cycle.
8. Rollback: the migrations are additive, so rolling back means dropping the new columns. The backfill is idempotent, so it can be re-run safely.

Because the backfill is a script and not a migration, CI will not exercise it on its own. Its unit test in step 5 covers that gap.
