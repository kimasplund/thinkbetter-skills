## Most likely cause

The new enterprise customer's traffic. The timing fits too well to ignore. The slowdown began the day after they onboarded, it follows business hours only, and nothing else changed. But your database CPU is normal and errors are flat, so this is not plain overload. The likely mechanism is that their usage hits a code path or data shape that is slow without being CPU-heavy. I'd put this at roughly 70% until you check the items below.

## What the evidence rules in and out

| Candidate | Verdict | Why |
|---|---|---|
| A bad deploy or config change | Ruled out | You report no deploys, and a deploy would not turn itself off at 17:00 UTC. |
| Database CPU saturation | Ruled out | CPU is normal. |
| Crashes, dependency outages, or retries failing | Mostly ruled out | The error rate is unchanged. A hard failure would show up there. |
| Cron or batch job colliding with peak hours | Unlikely | It would run at a fixed time, not for eight hours, and it would not start the day after an onboarding. |
| Infrastructure noise (noisy neighbor, network) | Unlikely | It would not follow business hours exactly, and it would likely have been noticed earlier than Tuesday. |
| General organic traffic growth | Weak | The step change on Tuesday and the 09:00-17:00 pattern are too sharp. |
| Enterprise customer's load or data | Leading | It matches the timing, and it explains why the database CPU looks fine. |

## Likely mechanisms (all consistent with normal DB CPU)

1. **Lock or row contention.** One tenant sends many concurrent writes or reads against the same rows or tables, and requests queue. This shows up as wait time, not CPU.
2. **Connection pool exhaustion.** Their concurrency uses up pool slots, and everyone else waits for a connection. The database looks idle while the API is stalled.
3. **Large tenant data and missing indexes.** Queries that were fine for small tenants now scan or return much more data. This is often IO-bound or memory-bound, not CPU-bound.
4. **Heavy or chatty requests.** Large payloads, big list endpoints, or an N+1 pattern in the code they exercise.
5. **Per-tenant limits or auth overhead.** SSO, audit logging, permission checks, or an external call that only enterprise accounts trigger.
6. **Cache hit rate drop.** Their access pattern evicts hot entries or bypasses the cache.

## How to confirm it (fastest first)

1. **Split p95 by tenant.** If the slow requests are mostly the new customer's, that settles it. If everyone is slow, the cause is shared and the customer is the trigger, not the victim (see 2 and 6).
2. **Split p95 by endpoint.** Find which endpoints regressed. Compare the list with what the new customer actually calls.
3. **Check database wait events, not CPU.** Look at lock waits, active connections versus pool size, and IO latency. Slow-query logs sorted by total time will show the offending query.
4. **Check app-side pool metrics.** Time spent waiting for a connection versus time executing the query.
5. **Compare their request rate with the latency curve** hour by hour since Monday. They should rise together.
6. **Quick test.** If you can, throttle or temporarily route the new customer's traffic separately. If p95 drops back toward 80ms, the cause is confirmed.

## What would change my mind

- If the slow requests are spread evenly across all tenants and none of the above shows up, look at shared resources with a business-hours pattern: a rate limiter, a shared cache, or a downstream service whose own load follows the same hours.
- If the regression predates Monday in any metric, the customer is a coincidence and I'd re-open the infrastructure and cron candidates.

## Assumptions

I have no logs or dashboards, so this is based only on the facts in your message. The ranking is a diagnosis from those facts, not a confirmed finding. The tenant split in step 1 should take only a few minutes and will tell you which branch you are on.
