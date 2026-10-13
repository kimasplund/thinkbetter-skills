Short version: three of the four can run in parallel, but not as four independent worktrees with a Friday merge. Package boundaries don't match the real dependencies here, and a clean merge is unlikely as the plan stands. Below are the couplings I found, the fixes that make parallel work safe, then the four prompts and the merge plan.

## Why the work isn't as independent as it looks

1. **The Kestrel upgrade touches every package.** Task 3 is repo-wide by definition, so it overlaps files in tasks 1, 2 and 4. It also changes how the other tasks read numeric columns: with 5.x, `quotes.amount` arrives as a string like `"18.3350"`. Pricing code that does `Money = number` arithmetic on it will break, or worse, silently concatenate. Each of the other three agents would be coding against 4.x behaviour in its own worktree, and CI on each branch would pass for the wrong reason.
2. **Billing depends on pricing's new `Money` shape.** Billing reads amounts through the pricing package. If it is built against the old `number` type, it won't compile after merge. It needs the new type in its worktree from the start.
3. **Migration number collision.** Tasks 1 and 2 both add a migration, and both will take 0042. Reserve the numbers up front: 0042 for pricing, 0043 for the billing `currency` column. Since CI builds the database from the migrations on each branch, each branch passes alone and the collision only shows up at merge.
4. **Tasks 1 and 4 contradict each other.** If the `quotes.amount` migration alters the column type in place, Postgres rewrites 3.1M rows inside the migration, takes a heavy lock, and has already converted the data. The backfill "run after the column change" then has nothing left to do, or double-converts. The in-place cast is also not minor units: `numeric(12,4)` to `bigint` rounds half away from zero and keeps the major units. 18.3350 would become 18, not 1834. Use expand/contract instead:
   - 0042 adds `quotes.amount_minor bigint NULL` and `quotes.currency text NULL`.
   - The backfill populates them in batches.
   - A later migration (not Friday) sets NOT NULL, switches reads, and drops the old column.
5. **Rounding mode is a hidden requirement.** Finance wants half-to-even, and the code uses `Math.round` everywhere (which rounds half up). Your own data shows why it matters: 7.1250 to two decimals is 7.12 under half-to-even but 7.13 under `Math.round`, and 18.3350 becomes 18.34 (the tie goes to the even digit). Float arithmetic also makes ties unreliable, because 18.335 is not exactly representable. So the rounding has to be done on decimal strings or integers, never on floats. One shared helper must be used by the pricing code, the billing code and the backfill. If each agent writes its own, they will disagree.
6. **Decisions you need to make before launching** (I've put in a default for each so the agents aren't blocked):
   - Minor-unit exponent: assumed 2 for both EUR and DKK. Converting four-decimal rate-card values to 2 decimals loses information. If partner rate cards need four decimals, either keep a scale of 4 or store rate cards separately. I've assumed 2 with half-to-even and a logged list of rows where rounding changed the value.
   - Currency for existing quotes: assumed EUR.
   - Backfill lock and batch behaviour on 3.1M rows: assumed batches of 10k keyed by primary key, resumable, with a dry-run mode.

## Recommended structure

**Step 0 (you or one agent, about half a day, on main before anything else): the contract commit.** It contains:
- The `Money` type `{ minor: number; currency: string }` plus the half-to-even helper signature, for example `roundHalfEven(decimalString, exponent): number`, with its unit tests. Use string/BigInt arithmetic. Note that `minor: number` is safe up to 2^53 minor units, which is plenty here.
- The reserved migration numbers.
- A short `docs/money-contract.md` stating the rules above.

**Task 3 (Kestrel 5) goes first, and merges to main before the others get far.** Run it as its own worktree starting now. Everyone else rebases on it as soon as it lands (target Tuesday). Alternatively, have the others work on Kestrel 4.x and accept a bigger rebase, but I don't recommend that.

**Then tasks 1, 2 and 4 in parallel**, each branching from main after step 0, with billing and backfill coding against the contract types and the pricing helper.

## The four agent prompts

Common preamble for all four:

> You are working in the Larkspur dispatch monorepo (TypeScript, Postgres, Kestrel ORM) in your own git worktree. Read `docs/money-contract.md` first. Stay inside the files listed for your task; if you need a change elsewhere, stop and write it to `NOTES.md` instead of making it. Migrations are in `db/migrations`; the latest is 0041, and you may only create the migration number assigned to you. All rounding is half-to-even, done on decimal strings or integers, never `Math.round` and never float arithmetic. Run the package tests and the lint before you finish, and report what you changed, what you couldn't verify, and any decisions you made on the contract's open points.

**Agent 1 (Kestrel 4.x to 5.x, repo-wide, merges first)**

> Upgrade Kestrel ORM from 4.x to 5.x across the whole repo. Read the 5.x changelog fully, not only the headline. The headline breaking change is that numeric/decimal columns now return strings instead of numbers. Find every read of a numeric/decimal column (`quotes.amount`, `invoices` amounts and anything else) and make the code handle strings correctly: parse with a decimal-safe method, never `parseFloat`/`Number()` followed by arithmetic. Where code currently treats these as `number`, add a thin typed adapter and leave a `TODO(money)` comment rather than redesigning, because the pricing agent is changing the money types in parallel. Do not touch migrations. Add or adjust tests that assert a numeric column such as `18.3350` round-trips exactly. Deliver a list of every file you touched so the others can predict conflicts.

**Agent 2 (packages/pricing)**

> In `packages/pricing`, change `Money` from `number` to `{ minor: number; currency: string }` and update all pricing code and tests. Replace every `Math.round` with the shared half-to-even helper from the contract (the tests must cover ties, for example 7.1250 to 7.12 and 18.3350 to 18.34, negative values, and zero). Create migration 0042 using expand/contract: add nullable `quotes.amount_minor bigint` and `quotes.currency text`. Do not alter or drop `quotes.amount` and do not backfill in the migration. Export the helper and any conversion functions (`fromDecimalString`, `toDecimalString`) so billing and the backfill script use them. Keep the old column readable so the code can be deployed before the backfill runs. Touch only `packages/pricing` and migration 0042.

**Agent 3 (apps/billing)**

> In `apps/billing`, add multi-currency invoice PDFs (EUR and DKK at launch). Create migration 0043 adding `invoices.currency` (text, NOT NULL with a default of EUR, so existing rows are valid). Read amounts only through the pricing package using the new `Money` type from the contract; never format a number by hand. Format by currency using `Intl.NumberFormat` with the currency's exponent, and make sure the currency shown always comes from the invoice, not a global setting. Add tests with DKK and EUR invoices and a rounding tie case. If pricing hasn't merged yet, code against the contract types and note which imports need rewiring. Touch only `apps/billing` and migration 0043.

**Agent 4 (scripts/backfill)**

> In `scripts/backfill`, write a one-off script that populates `quotes.amount_minor` and `quotes.currency` from `quotes.amount` for the roughly 3.1M historical rows. Requirements: process in batches of 10k keyed by primary key; be resumable and idempotent (only update rows where `amount_minor IS NULL`); use the pricing package's half-to-even helper on the decimal string from the database (never floats); set currency to EUR for existing rows; support `--dry-run`; log progress; and output a report of every row where rounding changed the value (for example 7.1250 to 7.12) so Finance can review it. After the run, verify that row count equals the converted count and that `sum(amount)` matches `sum(amount_minor)/100` to within the documented rounding differences. Test it against a fixture including 18.3350, 7.1250, zero and a large 12-digit value. It must not run in CI automatically. Touch only `scripts/backfill`.

## Merge plan

1. **Now to Tuesday:** contract commit, then Agent 1 starts. Agents 2, 3 and 4 start once the contract is on main. Don't wait for Kestrel to start them, but plan to rebase.
2. **Tuesday:** merge Agent 1 after full CI. Rebase 2, 3 and 4 on main and re-run their tests.
3. **Thursday (a day earlier than your plan):** merge Agent 2 (pricing and migration 0042). Rebase 3 and 4 on it, replace stubs with the real imports, and re-run CI.
4. **Friday:** merge Agent 3, then Agent 4. After each merge, build a fresh database from all migrations and run the entire test suite, not only that package's tests, because per-branch CI can't catch cross-package breakage.
5. **Pre-merge checks for each branch:** diff the file list against what the agent was allowed to touch; check that migration numbers are 0042 and 0043 with no gaps and no duplicates; grep for `Math.round`, `parseFloat` and `Number(` in money paths.
6. **Deployment order (separate from merging):** apply 0042 and 0043, deploy the code (which still tolerates a null `amount_minor`), run the backfill with `--dry-run` and review the rounding report with Finance, run it for real, then ship a follow-up migration that makes the columns NOT NULL and drops the old `amount`. Don't do the final step on Friday. Test the backfill on a copy of production data first.
7. **Rollback:** because 0042 and 0043 only add columns, they can stay in place if you roll the code back. Don't drop the old column until at least a week after the backfill, and after you've checked that Denmark's first invoices look right.

If you tell me the answers to the open points in section 6 (exponent, existing-quote currency, and what to do about four-decimal rate cards), I can adjust the prompts to match.
