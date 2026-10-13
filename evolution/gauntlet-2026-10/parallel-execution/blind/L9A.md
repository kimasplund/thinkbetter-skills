Running the four agents in parallel is fine, but the work isn't independent, and a clean merge on Friday is unlikely unless you settle a few things first. Package boundaries don't separate these tasks, because the dependencies run through the shared `Money` type, the `quotes` column and the migration sequence.

## Why the merge won't be clean as planned

1. **Billing depends on pricing.** Invoices read amounts through the pricing package, and `Money` changes shape from `number` to `{ minor, currency }`. An agent working in `apps/billing` against the old `Money` will produce code that compiles on its branch and breaks at merge.
2. **The Kestrel upgrade touches everything.** It is repo-wide, and numeric columns will come back as strings. That hits pricing's reads of `quotes.amount` (still numeric until the migration lands), billing's reads, and the backfill script's reads of the 3.1M rows. It will also edit the same files the pricing agent edits.
3. **Migration number collision.** The pricing agent and the billing agent will both create `0042`. The Kestrel agent might add one too. Migrations are sequential and CI builds a fresh database per branch, so two `0042` files will break CI at merge.
4. **Backfill can't be tested in isolation.** CI builds each branch's database from that branch's migrations, so the backfill branch won't have the new column or type unless it contains the pricing migration.
5. **Rounding is a trap in two places.** Postgres `round()` on numeric rounds half away from zero, not half to even. A migration written as `ALTER ... USING round(amount * 100)::bigint` therefore violates the auditors' rule. Your own examples show it:
   - 18.3350 -> 1833.5 minor units -> half-even gives 1834, and `round()` also gives 1834.
   - 7.1250 -> 712.5 -> half-even gives **712**, and `Math.round`/`round()` give **713**.
   - Float math makes it worse. 18.335 as a double may be 18.33499999..., so `Math.round(x * 100)` is unreliable. Do the conversion on decimal strings or integers, never via floats.
6. **Four-decimal data may not fit two-decimal minor units.** Values like 18.3350 mean some quotes will lose precision when they go to 2-decimal minor units (EUR and DKK both have 2). That is a business decision, not an implementation detail (see Decisions below).
7. **The migration and the backfill overlap.** If the migration alters the type in place, it has to convert the data, so the backfill script is redundant or conflicts with it. An in-place `ALTER COLUMN TYPE` on 3.1M rows also rewrites the table under an exclusive lock.

## Decisions to make before launching agents

- **Precision.** Are quotes allowed to lose the sub-cent digits (round half-even to 2 decimals), or do you need to keep 4-decimal precision? If you keep it, minor units would have to be 1/10000 of a unit, which changes the `Money` semantics. I assume the first option below.
- **Migration strategy.** I recommend expand/contract, which makes your backfill script real work:
  - `0042`: add `quotes.amount_minor bigint NULL`.
  - Backfill script: fill `amount_minor` in batches with half-even rounding.
  - `0044` (after the backfill is verified, after Friday if needed): set `NOT NULL`, switch reads, drop `amount`.
  - If you would rather do an in-place `ALTER`, delete task 4's batching and put an explicit half-even `USING` expression in the migration.
- **Reserved migration numbers.** `0042` is pricing, `0043` is billing (`invoices.currency`), and `0044` is reserved for the contract step. The Kestrel agent gets none and must say so if it needs one.
- **Rounding module.** Pricing owns one `roundHalfEven` helper over integers or decimal strings. Nobody else writes rounding code.
- **Bigint handling.** Confirm how Kestrel 5.x returns `bigint` columns. If it returns strings, `amount_minor` needs the same parsing as numerics.

## Revised sequencing

The four agents can still run at once, but not on equal footing:

- **Day 0 (about an hour, by you or one agent).** Commit a shared contract to `main`: the new `Money` type definition, the `roundHalfEven` signature with test vectors, and the reserved migration numbers. All four worktrees branch from that commit.
- **Kestrel (task 3) lands first**, merged to `main` as soon as it is green, and the other three rebase onto it. It is the widest change and the most likely to conflict.
- **Pricing (task 1)** merges second.
- **Billing (task 2)** merges third, rebased on pricing.
- **Backfill (task 4)** merges last, tested against a database built from the merged migrations.
- Give agents a mid-week checkpoint (Wednesday) to rebase onto whatever has merged, so Friday isn't the first time the branches meet.

## Agent prompts

**Shared preamble for all four.** Prepend this to each:

> You work in a TypeScript monorepo (Postgres, Kestrel ORM) for Larkspur Couriers, in your own git worktree. Three other agents work in parallel on other tasks. Rules: (1) Edit only the paths listed for you. If you need a change elsewhere, stop and record it under "Needs from others" in your final report. (2) Money rounding is always half-to-even (the auditors signed off on it in the 2024 review). Never use `Math.round` or Postgres `round()` on money, and never do money math through floating point. Use the shared `roundHalfEven` from `packages/pricing`. (3) Migrations are numbered sequentially in `db/migrations`; the latest on `main` is 0041. Use only the number assigned to you. (4) CI builds a fresh database from the migrations on your branch, so your tests must pass with only your branch's migrations. (5) Historical quotes include values like 18.3350 and 7.1250. Expected results to 2 decimals under half-even: 18.3350 -> 18.34, 7.1250 -> 7.12. (6) Commit in small steps and finish with a report: what changed, files touched outside your list, assumptions, open questions.

**Agent 1: pricing**

> Task: In `packages/pricing`, change `Money` from `number` to `{ minor: number; currency: string }` (integer minor units). Replace all float money arithmetic with integer arithmetic. Replace every `Math.round` in the package with `roundHalfEven`, implemented on integers or decimal strings with no float intermediate. Add a parse helper that takes a decimal string such as "18.3350" (as Kestrel 5.x will return numerics) and produces minor units for a currency with 2 decimals, applying half-even. Add migration `0042_quotes_amount_minor.sql`: add `quotes.amount_minor bigint NULL` (do not alter or drop `amount`; the contract step is 0044, owned by someone else later). Update quote reads and writes to populate and use `amount_minor`. Export the public API that billing needs and document it in the package README. Tests must cover ties (7.1250 -> 712, 18.3350 -> 1834 minor units), negative values, zero, and values near 2^53. Allowed paths: `packages/pricing/**`, `db/migrations/0042_*`.

**Agent 2: billing**

> Task: In `apps/billing`, make invoice PDFs multi-currency (EUR and DKK at launch; we go live in Denmark next month). Add migration `0043_invoices_currency.sql` adding `invoices.currency` (text, NOT NULL, default 'EUR', with a check on the allowed codes). Format amounts with the correct currency symbol, separators and number of decimals per currency. Read amounts only through the pricing package's `Money` type (`{ minor, currency }`). Do not do your own rounding or conversion. Until pricing lands, code against the contract on `main`; stub the pricing package inside your tests, not in `packages/pricing`. Test PDFs for EUR, DKK and a mixed batch. Allowed paths: `apps/billing/**`, `db/migrations/0043_*`.

**Agent 3: Kestrel upgrade**

> Task: Upgrade Kestrel ORM from 4.x to 5.x across the repo. The headline breaking change is that numeric/decimal columns now return as strings, not JS numbers. Work through the full changelog, not just that item. Find every place a numeric or decimal column is read (grep model definitions, queries, raw SQL, and tests), especially `quotes.amount` and any invoice amounts. Make each read handle the string explicitly. Do not use `Number()` or `parseFloat` on money, because that reintroduces float error; pass the string through to a decimal-string-safe path or a clearly marked adapter. Check how 5.x returns `bigint` columns and report it. Do not change `Money`, rounding logic or business behavior. Make the minimum change to keep behavior identical. You may touch any package, but keep edits mechanical and keep each commit small, so the other branches can rebase onto yours. You get no migration number. Run the full test suite and report any change in observable behavior.

**Agent 4: backfill**

> Task: In `scripts/backfill`, write a one-off script that fills `quotes.amount_minor` for the ~3.1M historical rows from `quotes.amount` (numeric(12,4)). Requirements: read `amount` as a decimal string; convert to minor units for the quote's currency using half-even rounding (7.1250 -> 712, 18.3350 -> 1834; use the pricing helper once it is on `main`, otherwise a local copy with the same test vectors); process in keyset-paginated batches (e.g. 5k rows, ordered by primary key) in short transactions; make it idempotent (only rows where `amount_minor IS NULL`) and resumable; log progress and a final count; support `--dry-run`, which reports how many rows would lose sub-cent precision (amount has non-zero digits beyond 2 decimals) and prints a sample. Never use `Math.round` or float math. After the run, verify that the number of NULL `amount_minor` rows is 0 and that half-even rounding of amount*100 matches `amount_minor` on a sample. Tests: use a fresh DB built from the migrations (this branch needs 0042, so cherry-pick or rebase onto pricing before running them, and record that). Allowed paths: `scripts/backfill/**`.

## Merge plan for Friday

1. **Thursday.** Freeze feature work. Each agent rebases onto current `main` and pushes. You run the full CI on each branch.
2. **Merge order**, running the full test suite and building a fresh DB from migrations after each merge:
   1. Kestrel upgrade. Run the whole monorepo suite. Do not continue if any money read now yields a string unhandled.
   2. Pricing. Rebase it onto Kestrel first; the conflicts will be in reads of `quotes.amount`. Check that migrations apply cleanly in order: 0041, then 0042.
   3. Billing. Rebase it onto pricing, replace its test stubs with the real pricing package, and check 0043 follows 0042.
   4. Backfill. Rebase it onto the merged `main`, and run its tests against the full migration chain.
3. **Staging rehearsal.** Restore a production snapshot (or at least a few hundred thousand rows, including 18.3350 and 7.1250). Apply the migrations, run the backfill with `--dry-run` and then for real, and check:
   - zero NULL `amount_minor` rows;
   - spot checks of the tie cases (712 and 1834);
   - the count of rows that lost sub-cent precision, signed off by finance;
   - batch timing, so you know the production window.
4. **Production.** Deploy code that can read both columns, apply 0042 and 0043, run the backfill, verify, then apply 0044 (`NOT NULL`, drop `amount`) in a later release, once finance signs off. Keep the old column for now so you can roll back.
5. **Finance check.** Send finance the half-even test vectors and the precision-loss count before 0044.

## Things to watch

- If a merge conflict in the money code is resolved by keeping either side's version without checking, the likely result is a `Math.round` surviving somewhere. Grep for `Math.round` in money code before and after the merge.
- The DKK launch is next month, so billing (and its 0043) is the only piece that is time-critical. If anything slips, ship that and the migration, and leave the pricing contract step for later.
- I assumed 2-decimal minor units for both currencies, an integer `minor` in the safe-integer range, and that the quotes have a currency available to the backfill. If quotes have no currency column today, the backfill needs a default (probably EUR); tell me and I'll adjust prompts 1 and 4.
