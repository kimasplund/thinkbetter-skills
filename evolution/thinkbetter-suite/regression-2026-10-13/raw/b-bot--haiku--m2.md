## Ways to cut the $48k/month AWS bill by 40% without hurting latency

Target: about $19k/month saved, bringing the bill to roughly $29k. Assumptions: EC2 is $28.8k, RDS $9.6k, data transfer $5.8k, other $3.8k. Savings figures are rough estimates from typical outcomes; they overlap, so do not add them up directly.

### The options

| # | Approach | Where it applies | Est. monthly saving | Latency risk | Effort | Confidence it works in 2 quarters |
|---|---|---|---|---|---|---|
| 1 | **Rightsize EC2** (smaller instance types, fewer idle hosts, based on p95 CPU and memory) | EC2 | $5-8k | Low if sized to p95 with headroom | Low-medium | High |
| 2 | **Savings Plans / Reserved Instances** on the stable baseline, bought after rightsizing | EC2, RDS | $4-7k | None | Low (finance decision) | High |
| 3 | **Spot or mixed instances** for stateless, batch, or queue workers | EC2 (worker tier only) | $2-4k | Low for async work, high if on the request path | Medium | Medium-high |
| 4 | **Schedule non-production** to stop nights and weekends | Dev/staging EC2, RDS | $2-3k | None for production | Low | High |
| 5 | **Graviton (ARM) migration** for services that build cleanly on ARM | EC2, RDS | $2-3k | Usually neutral or better; needs load testing | Medium | Medium |
| 6 | **RDS right-sizing and storage** (instance class, gp3 storage, fewer idle read replicas, reserved DB instances) | RDS | $2-4k | Medium: verify query latency at the smaller class | Medium | Medium-high |
| 7 | **Cut data transfer** (gateway endpoints for S3/DynamoDB, fewer NAT gateway hops, same-AZ traffic, CDN for public assets) | Transfer | $1.5-2.5k | None, often improves latency | Low-medium | High |
| 8 | **Storage and other cleanup** (S3 lifecycle tiers, delete orphaned EBS volumes and old snapshots, shorter log retention) | Other | $1-1.5k | None | Low | High |
| 9 | **Caching in front of compute and DB** (CDN for cacheable API responses, Redis for hot reads) | EC2, RDS | $2-4k | Usually lowers latency; adds stale-data risk | Medium-high | Medium |
| 10 | **Move the workload to another cloud or host** | Everything | Large, but slow | High during migration | Very high | Low for two quarters |

Option 10 is set aside. A migration cannot be finished, tested, and cut over in two quarters without risking latency, so it fails the timeline. Everything else is viable.

### Four bundles, by trade-off profile

**Bundle A: Quick and risk-free (about $8-11k/month, about 20%)**
Options 4, 7, 8, plus the cheap parts of 1 and 6 (the most obviously idle instances and volumes).
- Pros: almost no latency risk, starts this week, funds the rest.
- Cons: falls short of 40% on its own.

**Bundle B: Commit-first (about $11-14k/month, about 25-30%)**
Savings Plans and RIs on current usage, then rightsizing only where it does not disturb the commitment.
- Pros: the biggest and fastest saving, almost no engineering time.
- Cons: locks in spend on the current shape of the fleet. If you rightsize later, you pay for commitments you no longer use. It can also hide poor sizing. Commit to a conservative share of the baseline only.

**Bundle C: Engineering-led efficiency (about $15-19k/month, about 35-40%)**
Options 1, 3 (worker tier), 5, 6, 7, 8, and 9 (where a hot path can be cached), in that order. Savings Plans on the resulting baseline in the last month.
- Pros: reaches the full target and improves unit economics, with latency gains from caching and transfer changes.
- Cons: needs a dedicated engineer for two quarters, and the Graviton and cache work carries real regression risk.

**Bundle D: Hybrid, recommended (about $18-21k/month, about 40%)**
1. Weeks 1-3: Bundle A. Measure p95 CPU, memory, and per-service cost with cost-allocation tags so you know where the money goes.
2. Weeks 4-10: rightsizing (1), RDS changes (6), and transfer and caching work (7, 9) on the hottest paths, with a latency canary and p95 alerts on every change.
3. Weeks 10-12: Savings Plans and RIs (2) sized to the post-rightsizing baseline, not today's bill.
4. Spot (3) and Graviton (5) only for workloads that pass a load test, scheduled as stretch goals.

Bundle D reaches the target with the least exposure to commitment lock-in and latency regressions.

### What decides which bundle you pick

- **Cost Explorer by service, account, and tag.** If EC2 is mostly idle, option 1 carries the plan. If it is busy, commitments and architecture matter more.
- **p95 CPU and memory per service.** Sizing decisions depend on this. Without it, rightsizing is guesswork.
- **Share of the EC2 bill that is steady.** Only a steady baseline should be committed.
- **Whether data transfer is NAT or cross-AZ.** If it is, option 7 is an easy win that can also reduce latency.

### Guardrails for any option

- Set p95 and p99 alarms per service before the first change, and roll each change out behind a canary.
- Keep a rollback path for every instance-class and storage change.
- Review the bill weekly against the target, not monthly.

### Not explored in depth

- Cutting features or traffic that drive cost (a product decision, not an infrastructure one).
- Negotiating an enterprise discount with AWS, which can be worth a few percent and is worth asking for once spend is known.
