I'd change the plan before launching four agents. The packages are separate, but the four jobs are not independent, and a clean merge on Friday is unlikely as things stand. Prompts and a merge plan follow the problems.

## Why four parallel worktrees won't merge cleanly

1. **The backfill (4) can't work after the migration (1) as written.** If a migration alters `quotes.amount` from numeric(12,4) to bigint, Postgres casts and rounds the values in place (round-half-away-from-zero). The 4-decimal history is gone before the backfill sees it, and the cast doesn't know the scale. 18.3350 would become 18, not 1834. Use expand/contract instead:
   - Migration A adds `quotes.amount_minor bigint NULL` and `quotes.currency`.
   - The backfill fills `amount_minor` in batches.
   - Migration B, in a later release, sets NOT NULL, switches reads, and drops the old column.

   On 3.1M rows, a single `ALTER COLUMN TYPE` also rewrites the table under an ACCESS EXCLUSIVE lock, which is another reason to avoid it.

2. **Rounding hits real data.** Finance wants half-to-even, and your history has values like 7.1250 and 18.3350. Converting to 2-decimal minor units, 7.1250 becomes 712.5, which is 712 under half-to-even but 713 under `Math.round`. 18.3350 becomes 1833.5, which is 1834 under half-to-even. Do not compute this in JS floats. 18.335 * 100 is not exactly 1833.5, so the result would depend on the float. Do the conversion in SQL on the numeric type, or with string and BigInt arithmetic, and never through `number`. Keep a rounding helper in one place (pricing) and ban `Math.round` on money. Decide up front whether the scale is currency-dependent (EUR and DKK are both 2 decimals, but don't hardcode that) and what happens to quotes stored at four decimals. Rounding them at all is a finance decision you should get signed off in writing.

3. **Migration numbering will collide.** The pricing, billing and backfill work each want 0042. CI builds a fresh database from each branch's migrations, so two branches that both add 0042 pass alone and break on merge. Reserve numbers now: 0042 for pricing (`amount_minor`, `quotes.currency`), 0043 for billing (`invoices.currency`), and 0044 reserved for the later contract step. Agents must not pick their own.

4. **The Kestrel 5 upgrade (3) touches everything.** Numeric columns now return strings, so pricing, billing and backfill all read money through changed code. Billing also reads amounts through pricing, whose `Money` type is changing underneath it. The upgrade will conflict with all three other branches, and a bigint column probably also comes back as a string, so the Money parsing has to handle that. Run it first, alone, on a branch that changes behavior as little as possible. Then branch the others from it.

5. **Billing depends on the new `Money` shape.** Without it, the billing agent either builds against the old type, which means rework, or invents its own. Land a stub of the new `Money` type and the rounding helper first.

Also confirm that `quotes` has a currency at all. If it doesn't, the backfill needs a rule (for example, all history is EUR), and you should check that rule against the data.

## Recommended sequencing

- **Day 1, merge before anything else:**
  - Agent C, the Kestrel 5 upgrade, with no behavior changes. Fix string-vs-number reads with explicit parsing, and run the full test suite.
  - A small "foundation" commit with the new `Money` type, the half-to-even helper and its tests, and the reserved migration numbers.
- **Then in parallel from that base:** pricing (A), billing (B), and the backfill script (D) written and tested against a staging copy.
- **Merge order:** Kestrel, then pricing, then billing, then backfill. Run the backfill in production only after pricing's migration A is deployed. Deploy migration B only after the backfill is verified.

If you really want all four running at once, start them from the foundation commit on top of the Kestrel branch, and accept that the Kestrel agent finishes first.

## Agent prompts

Common preamble for all four:

> You are working in your own git worktree of the Larkspur dispatch monorepo (TypeScript, Postgres, Kestrel ORM). Stay inside your assigned paths. If you need a change outside them, stop and write it up instead of making it. Migrations are in db/migrations, numbered sequentially; the latest is 0041. Use only the number assigned to you. Never use `Math.round` or floating-point arithmetic on money. All money rounding is half-to-even (banker's rounding), imported from the shared helper in packages/pricing. CI builds a fresh database from your branch's migrations, so run each package's tests that way. Commit in small steps and finish with a summary listing files touched, migrations added, open questions and anything you could not verify.

**Agent C: Kestrel 4.x to 5.x (runs first)**

> Upgrade Kestrel ORM from 4.x to 5.x across the repo. Make no functional changes beyond what the upgrade requires. The headline breaking change is that numeric/decimal columns now return strings instead of numbers. Find every read of a numeric/decimal column (start with quotes.amount and anything in pricing, billing and scripts). Make each one parse explicitly, so behavior is unchanged for callers. Do not use `parseFloat` and then arithmetic on money; where precision matters, keep the string or use a decimal-safe parse. Read the full changelog, not just the headline, and list every other breaking change you hit. Add or extend tests that prove a numeric column round-trips with four decimals (for example 18.3350 and 7.1250). Run the full suite in every package. Do not add migrations. Report any code path you could not cover with tests.

**Agent A: packages/pricing (migration 0042)**

> Branch from the Kestrel 5 + foundation commit. Change `Money` from `number` to `{ minor: number; currency: string }`, and update all uses inside packages/pricing. Use `Number.isSafeInteger` guards, and flag any place a value could exceed the safe range. Rounding must be half-to-even, via the shared helper, with tests including 7.1250 to 712 and 18.3350 to 1834 at two decimals, plus negatives and exact ties. Write migration 0042 as expand only: add `quotes.amount_minor bigint NULL` and `quotes.currency text`, and leave `quotes.amount` untouched. Do not alter or drop the old column. Make code write both columns and read `amount_minor` with fallback to the old one until the backfill is done. Export a documented public API, since apps/billing depends on it. State your assumption about the minor-unit scale per currency and where it is defined. Do not touch apps/billing or scripts.

**Agent B: apps/billing (migration 0043)**

> Branch from the Kestrel 5 + foundation commit. Implement multi-currency invoice PDFs (EUR and DKK at minimum; the Denmark launch is next month). Write migration 0043 to add `invoices.currency` (NOT NULL with a safe default or backfill for existing rows; state which). Read all amounts only through the packages/pricing API and the new `Money` shape (`{ minor, currency }`). Do not do your own arithmetic or rounding on amounts. Format with Intl using the invoice's currency and the right locale for DKK (decimal comma, symbol placement), and add snapshot tests for EUR and DKK PDFs. Until pricing lands, code against the foundation `Money` stub. Do not edit packages/pricing; list anything you need from it.

**Agent D: scripts/backfill**

> Branch from the Kestrel 5 + foundation commit. Write a one-off, re-runnable script that fills `quotes.amount_minor` from `quotes.amount` for roughly 3.1M historical rows. Requirements: process in keyset-paginated batches (for example 10k rows by primary key), each in its own transaction; idempotent (only rows where `amount_minor IS NULL`); resumable; a `--dry-run` that reports counts and anomalies without writing; progress logging; and a final verification query that checks no NULLs remain and that `amount_minor` equals the half-to-even rounding of `amount` times 10^scale. Do the arithmetic on the numeric type in SQL or with string/BigInt, never through JS floats. Report how many rows needed rounding (those with more than 2 meaningful decimals, such as 18.3350 and 7.1250) and output them to a CSV for finance review. For `currency`, assume EUR unless a column says otherwise, and make that a flag. Test against a database built from the migrations on the branch, with seeded tie cases. Do not write migrations, and do not drop any column.

## Friday merge plan

1. **Before Friday:** get finance's written confirmation of half-to-even for the historical conversion, the minor-unit scale, and what to do with 4-decimal rate-card values. Reserve migration numbers 0042 and 0043 (and 0044 for the contract step).
2. **Merge Kestrel (C)** into main first. Run the full CI and a smoke test against a staging copy of production data.
3. **Rebase A, B and D** onto main. Resolve conflicts in favour of the Kestrel parsing, then re-run each package's tests against a fresh database built from the merged migrations. Do this after every merge, not just on the last one.
4. **Merge pricing (A),** then rebase billing onto it, switch off the `Money` stub, and merge billing (B).
5. **Merge the backfill (D).** The script is dead code until it's run. Check for duplicate or out-of-order migration numbers (a quick script over db/migrations catches this).
6. **Full integration run:** the entire monorepo suite on a fresh database from the final migrations, plus one end-to-end test that creates a quote, converts it and generates a DKK invoice.
7. **Deploy order:** migrations 0042 and 0043, then the backfill on staging (check timing and the CSV), then the backfill on production in off-peak hours, then verification queries. Only then ship the contract migration (switch reads to `amount_minor`, set NOT NULL, drop `amount`) as its own release. Keep the rollback plan: the old column stays until verification passes.

Assumptions: 2-decimal minor units for EUR and DKK, all historical quotes in EUR, and a roughly one-week window. If any of these is wrong, tell me and I'll adjust the prompts.
