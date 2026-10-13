I wouldn't expect a clean merge here. The four jobs sit in different directories, but they share a type, a database column and a library. Below are the conflicts I found, a revised plan, the four prompts, and the Friday merge plan.

## Where the "different packages" assumption breaks

1. **Migration number collision.** Three jobs want a migration: pricing (`quotes.amount` to bigint), billing (`invoices.currency`) and possibly the ORM upgrade. All three will pick 0042. Git will merge the files without complaint, but the numbering is broken, and CI only builds from each branch's own migrations, so nobody will see it until Friday. Fix: reserve numbers now. Pricing gets 0042, billing 0043, and the ORM gets none unless it truly needs one (0044 if so).
2. **The `Money` change is not confined to packages/pricing.** Billing reads amounts through pricing, and the Kestrel upgrade touches every call site that reads numeric columns. If pricing changes `Money` to `{ minor, currency }` while billing is still written against `number`, billing breaks at merge time. Fix: pricing agrees the new `Money` interface up front (below) and merges it first. Billing codes against that interface from day one.
3. **Kestrel 5 returns numeric/decimal as strings, and this interacts directly with the money work.** The old pricing code probably did arithmetic on `number` values that were really numerics. After the upgrade those become strings, and `"18.3350" + 1` silently concatenates. Pricing's rewrite and the ORM upgrade both touch the same read paths (the quote and invoice repositories). Fix: the ORM upgrade merges first, so pricing is built on the post-5.x behavior. The upgrade can be tested in isolation, because nothing in it depends on the other three jobs.
4. **The backfill is not independent of the migration.** As written, the migration converts `numeric(12,4)` to `bigint` in place, and the backfill is a separate script that runs afterwards. By then the column has already been cast to bigint, and the fractional digits are gone or rounded by Postgres. Postgres rounds numeric half away from zero, not half-to-even. The 4-decimal historical values show what goes wrong:
   - 18.3350 is 1833.5 minor units (2-decimal currency). Half-to-even gives 1834. Math.round also gives 1834, so these agree.
   - 7.1250 is 712.5 minor units. Half-to-even gives 712. Math.round and Postgres `ROUND` give 713, so these disagree by one minor unit. Finance's audit position is half-to-even, so 713 would be wrong.
   - Across 3.1M rows, any partner rate card stored at 3 or 4 decimals will hit this.

   So the conversion must not be a plain `ALTER COLUMN ... TYPE bigint USING amount*100` or `ROUND(...)`. The ordering "change the column, then backfill" has to change too (see the plan).
5. **Half-to-even has to be applied in two places that must agree.** The TypeScript pricing code (currently `Math.round` everywhere, which is half-up for positives and half-toward-positive-infinity for negatives) and the SQL/backfill conversion. Without one shared definition they will drift. Fix: pricing owns a single `roundHalfEven` helper with tests, the backfill imports it, and the SQL path uses an explicit half-even expression, not `ROUND`. A tie is detected when `abs(x*100 - trunc(x*100)) = 0.5` exactly, which is safe in `numeric` but not in floats. Don't ever do this conversion through JS floats: 7.125 is exact in binary, but many other 4-decimal values are not.
6. **Currency of historical rows is unknown.** `quotes.amount` has no currency today. Minor-unit exponent depends on currency (EUR and DKK are both 2, but a hard-coded 100 is a trap if another currency ever appears). I assume every historical quote is EUR and that this is a decision someone on the team must confirm. If that is wrong, the backfill needs a source for currency.
7. **CI cannot catch the backfill's problems.** CI builds a fresh, empty database from migrations. 3.1M rows of real data, including awkward partner rate cards, never appear in it. The backfill needs its own fixtures and a dry-run mode, run against a production snapshot.
8. **Locking.** An in-place `ALTER COLUMN TYPE` on a 3.1M-row table rewrites it under an exclusive lock. If you can't tolerate that downtime, use an expand/contract approach instead.

## Recommended approach to the migration and backfill

Instead of "migrate the column, then backfill":

1. Migration 0042 adds a nullable `quotes.amount_minor bigint` (and `quotes.currency text`), without touching `amount`. It is instant and safe.
2. The backfill script fills `amount_minor` in batches by primary key range, using exact numeric math and half-to-even. It is idempotent (`WHERE amount_minor IS NULL`), resumable, and logs a checksum.
3. After the backfill is verified, a later migration (0044 or later) sets `amount_minor NOT NULL`, switches reads over, and drops or renames the old `amount`.

The code switches to `amount_minor` in the same release as the verified backfill. If you really want the single in-place `ALTER` and can accept the lock, then the conversion expression must live in the migration itself, with the half-even logic written in SQL. In that case the backfill job disappears, because it would be redundant. Either way, "alter first, backfill after" loses the data. This is the single most important thing to settle before the agents start.

## Revised sequencing

Four agents running at once is still fine for writing code. The merge order is what has to change:

| Order | Job | Why |
|---|---|---|
| 1 | Kestrel 5 upgrade | Foundation for everything else. Changes read behavior for numerics. |
| 2 | Pricing / Money | Defines the type and `roundHalfEven`. Owns migration 0042. |
| 3 | Billing | Consumes the new `Money`. Owns migration 0043. |
| 4 | Backfill | Needs 0042's column and the shared rounding helper. Runs against production only after a verified dry-run. |

Each agent still works in its own worktree today. But agents 2, 3 and 4 should start from the agreed interface below, and should rebase onto the upgrade branch as soon as it is ready (ideally midweek, not Friday).

## Shared contract (paste into every prompt)

```ts
// packages/pricing/src/money.ts
export type Money = { minor: number; currency: string };  // minor must be a safe integer
export function roundHalfEven(x: Decimal-or-string-or-bigint-safe input): bigint-or-number; // pricing owns this
export function toMinor(amount: string, currency: string): Money;  // amount as decimal STRING, never a float
export function fromMinor(m: Money): string;                       // decimal string for display/DB
export function currencyExponent(currency: string): number;        // EUR=2, DKK=2
```

Rules:
- Money values never pass through floating point when converting from DB values. DB numerics arrive as strings (Kestrel 5), and bigint columns may also arrive as strings. Parse explicitly and check `Number.isSafeInteger`.
- All rounding is half-to-even. `Math.round` must not be used for money.
- Migration numbers: 0042 pricing, 0043 billing, 0044+ reserved for ORM or follow-up. Do not take a number you were not assigned.
- Each branch must pass CI from a fresh database built only from its own migrations, and must also pass when rebased on top of the others.

## The four prompts

### Agent 1: Kestrel ORM 4.x to 5.x

```
You are upgrading Kestrel ORM from 4.x to 5.x across the Larkspur Couriers dispatch monorepo (TypeScript, Postgres). Work in your own git worktree on branch orm-5.

Goal: the whole repo builds and all package tests pass on Kestrel 5.x, with no behavior changes other than those the upgrade forces.

Known breaking change: numeric/decimal columns now return strings instead of JS numbers. Find every place that reads a numeric/decimal column (quotes.amount is the main one, but audit all of them, including raw queries and repository/mapper code) and make the handling explicit: parse at the repository boundary, and keep the existing external types (still `number` for now) so other packages do not change. Do NOT convert money to the new Money type: another agent owns that change in packages/pricing. Add a clear comment on each parse site, and keep the parsing in as few places as possible so the pricing agent can find and replace them.

Watch for silent failures: `"18.3350" + 1` concatenates, comparisons and sort order on strings differ from numbers, and JSON serialization may change. Read the full changelog, not just the headline item, and list every other breaking change you hit.

Constraints:
- Do not create migrations unless the upgrade strictly requires one. If it does, use number 0044, not 0042 or 0043.
- Do not touch apps/billing business logic or packages/pricing logic beyond what is needed to compile and pass tests.
- Add tests that assert a numeric column round-trips with the correct value (including values like 18.3350 and 7.1250).

Deliverables: a PR-ready branch, and a short written note listing every call site where numeric values are now parsed, any other breaking changes, and anything you could not resolve. Aim to have this ready by Tuesday so the others can rebase on it.
```

### Agent 2: packages/pricing integer minor units

```
You are changing money handling in packages/pricing of the Larkspur Couriers dispatch monorepo (TypeScript, Postgres, Kestrel ORM) from floats to integer minor units. Work in your own git worktree on branch pricing-minor-units.

Change: the `Money` type goes from `number` to `{ minor: number; currency: string }`. Implement the shared contract (Money, roundHalfEven, toMinor, fromMinor, currencyExponent) in packages/pricing/src/money.ts exactly as specified below. Other agents depend on these signatures, so do not change them without flagging it.

[paste shared contract and rules here]

Rounding: finance requires half-to-even everywhere (auditors signed this off in 2024). The code currently uses Math.round everywhere. Replace every use in pricing. Implement roundHalfEven on exact decimal input (strings or integers), never on floats. Write tests at the ties: 7.1250 EUR is 712 minor units (not 713); 18.3350 EUR is 1834; 0.005 is 0; 0.015 is 2; also negatives, and DKK.

Migration: add db/migrations/0042 (use exactly this number). Use the expand approach: add nullable `quotes.amount_minor bigint` and `quotes.currency text`, and leave `quotes.amount numeric(12,4)` untouched for now. Do NOT alter or drop `amount`, and do NOT convert existing rows in the migration; a separate backfill agent owns that, and the final NOT NULL/drop step is a later migration. (If the team decides on an in-place ALTER instead, the conversion must use an explicit half-to-even SQL expression, not ROUND, which rounds ties away from zero.)

Note: Kestrel is being upgraded to 5.x by another agent, so numeric/decimal columns will come back as strings. Write the repository code against string input from the start (parse explicitly, check Number.isSafeInteger for bigint values).

Constraints:
- Update callers inside packages/pricing. Do not edit apps/billing; list the exported API changes billing must adapt to.
- CI builds a fresh database from your branch's migrations: make sure tests pass with only 0042 added.
- No floating point on any DB-to-Money path.

Deliverables: branch ready for review, tests for rounding and conversion, and a note describing the public API changes.
```

### Agent 3: apps/billing multi-currency invoice PDFs

```
You are adding multi-currency invoice PDFs to apps/billing in the Larkspur Couriers dispatch monorepo (TypeScript, Postgres, Kestrel ORM). We launch in Denmark next month, so DKK must work alongside EUR. Work in your own git worktree on branch billing-multicurrency.

Tasks:
1. Migration: add db/migrations/0043 (use exactly this number) adding a `currency` column to `invoices`. Decide default and constraints (for example NOT NULL with default 'EUR', check against a supported-currency list) and explain your choice, remembering existing invoices are EUR.
2. Render invoice PDFs in the invoice's currency: correct symbol/code, decimal separator and grouping per locale (da-DK uses "1.234,56 kr."), correct number of minor-unit digits, and correct totals and VAT/tax lines.
3. Read all amounts through the pricing package. Another agent is changing `Money` in packages/pricing to `{ minor: number; currency: string }` with the helper functions described in the contract below. Code against that contract now; until their branch lands, use a thin local adapter or stub that matches the contract so you can compile, and keep the stub in one clearly marked file to delete at merge.

[paste shared contract and rules here]

Constraints:
- Do not do your own money arithmetic or rounding with floats or Math.round. Any rounding goes through the pricing package's roundHalfEven.
- Do not edit packages/pricing. If you need something it does not provide, write it down in your handoff note.
- Mixed-currency invoices should be rejected explicitly, not silently summed.
- Kestrel is being upgraded to 5.x (numeric columns return strings); do not add code that assumes numerics are JS numbers.

Deliverables: branch ready for review, tests including a DKK and an EUR invoice, a PDF snapshot or golden-file test, and a handoff note listing the stub to delete and the pricing API you depend on.
```

### Agent 4: scripts/backfill

```
You are writing a one-off backfill script in scripts/backfill for the Larkspur Couriers dispatch monorepo (TypeScript, Postgres, Kestrel ORM). Work in your own git worktree on branch backfill-minor-units.

Purpose: convert about 3.1M historical rows in `quotes` from decimal `amount numeric(12,4)` to integer minor units in `amount_minor bigint` (plus `currency`), as added by migration 0042 from the pricing agent. Do not write migrations yourself.

Critical requirements:
- Historical values include 4-decimal figures such as 18.3350 and 7.1250 (partner rate cards). Rounding must be half-to-even: 7.1250 EUR becomes 712 minor units, not 713; 18.3350 becomes 1834. Never use JS floats or Math.round. Operate on the exact decimal string, or do the conversion in SQL with exact numeric arithmetic and an explicit tie check (ROUND on numeric rounds ties away from zero and is NOT acceptable). Import roundHalfEven/toMinor from packages/pricing once available; until then use a local copy with a comment pointing to the contract, and delete it at merge.
- Assume currency is EUR for all historical rows, but make this an explicit, logged, overridable parameter. Flag in your note that someone must confirm this.
- Process in batches by primary-key range (for example 5,000 to 20,000 rows), each in its own transaction, so it does not hold long locks or bloat WAL. Idempotent (only rows where amount_minor IS NULL), resumable after a crash, safe to run twice.
- Dry-run mode that changes nothing and reports: row count, how many rows hit an exact tie (i.e. rows where half-to-even differs from half-up), min/max, and rows that cannot be represented (overflow, NULL, non-finite). Real mode ends with a verification pass: every row has amount_minor, and for each row amount_minor equals the expected value; print counts and a checksum.
- Kestrel 5 returns numeric columns as strings. Treat all DB numerics as strings.
- Do not drop or modify `amount`.

Testing: CI uses an empty database, so write fixtures yourself covering ties (x.xx50 and x.xx5 with both even and odd preceding digits), negatives, zero, max value, trailing zeros, and a few thousand random rows checked against an independent reference implementation. Document how to run a dry-run against a production snapshot before any real run.

Deliverables: branch ready for review, a runbook (how to dry-run, run, verify, roll back), and a note listing assumptions.
```

## Friday merge plan

**Before anyone starts (today):**
- Decide expand/contract versus in-place for `quotes.amount`, confirm EUR for historical rows, and confirm the migration numbers (0042, 0043, 0044+). Put the shared contract in one place everyone can see.

**Midweek (Tuesday/Wednesday):**
- Merge the Kestrel 5 upgrade into main first. Everyone else rebases onto it. This surfaces conflicts while there is still time to fix them.
- Merge pricing next if it is ready. Billing and backfill then rebase onto it and delete their stubs/local copies.

**Friday:**
1. Verify main is green after the Kestrel merge.
2. Merge pricing (0042). Run CI from a fresh database.
3. Rebase billing onto main. Delete the pricing stub, confirm its migration is still 0043, and merge. Run CI.
4. Rebase backfill onto main, delete the local rounding copy, and merge. Run its tests.
5. Check the migration directory by hand: 0041, 0042, 0043, ... with no gaps or duplicates.
6. Run the whole test suite on main, and run a build of the combined result against a database built from all migrations.

**After merge (not Friday afternoon):**
- Do not run the backfill in production on Friday. Dry-run it against a production snapshot first, review the tie counts with finance, and run it in a quiet window with someone watching.
- Only after verification, ship the later migration that makes `amount_minor` NOT NULL and retires `amount`.
- Hold the DKK launch behind the backfill and billing being verified in production.

**Risks to watch:**
- A Friday merge of four large branches leaves no room to fix problems. Merging the upgrade and pricing earlier removes most of the risk.
- Money arriving as a string from the DB and being treated as a number (any remaining `+` on a DB value).
- Any leftover `Math.round` on money. A grep for it across the repo should come back empty in money code before merge.

**Assumptions I made:** historical quotes are all EUR with a two-digit minor unit; the team can tolerate an expand/contract migration rather than an immediate in-place ALTER; Kestrel 5 does not itself require a migration.
