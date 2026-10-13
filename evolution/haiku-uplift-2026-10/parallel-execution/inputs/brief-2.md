We're a team of five maintaining the dispatch platform at Larkspur Couriers: a TypeScript monorepo on Postgres with Kestrel ORM. I want to run four coding agents at the same time, each in its own git worktree, and merge everything on Friday. The work sits in different packages, so I'm expecting a clean merge.

1. packages/pricing: replace float money with integer minor units. The `Money` type changes from `number` to `{ minor: number; currency: string }`. Add a migration converting `quotes.amount` from numeric(12,4) to bigint.
2. apps/billing: multi-currency invoice PDFs, since we launch in Denmark next month with DKK alongside EUR. Needs a `currency` column on `invoices`. Invoices read amounts through the pricing package.
3. Upgrade Kestrel ORM from 4.x to 5.x across the repo. The changelog's headline breaking change is that numeric/decimal columns now come back as strings instead of JS numbers.
4. scripts/backfill: a one-off script that converts the 3.1M historical quote rows to minor units, run after the column change.

Other context:

- Migrations live in db/migrations and are numbered sequentially. The latest is 0041.
- Finance wants all rounding to be half-to-even, because that's what the auditors signed off on in the 2024 review. Today the pricing code uses Math.round everywhere.
- CI runs each package's tests against a fresh database built from the migrations on that branch.
- Historical quotes include values like 18.3350 and 7.1250, because some partner rate cards were stored at four decimals.

Could you write the four agent prompts, and the merge plan for Friday?
