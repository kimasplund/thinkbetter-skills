**Most likely cause: the new enterprise customer's traffic is saturating a shared resource that isn't database CPU.** That resource is probably DB connections, lock contention, a cache, or a worker/thread pool. I can't confirm this from the data you gave me, but it fits every fact you listed and the alternatives fit worse. Below is what I ruled out, what is still open, and the checks that will settle it.

I assumed one API tier, one primary database and no scheduled changes you haven't mentioned.

## What the facts rule out

| Candidate | Verdict | Why |
|---|---|---|
| Code or config regression | Very unlikely | No deploys. A regression wouldn't switch off at 17:00 UTC either. |
| Database CPU saturation | Eliminated | CPU is normal. This does not clear the database: connection waits, locks, I/O and bad plans all leave CPU flat. |
| Downstream outage or dependency failure | Unlikely | Errors are flat. A failing dependency usually adds timeouts or retries. A uniformly slow one is possible, but it wouldn't track 09:00-17:00 UTC so neatly. |
| Memory leak or slow resource exhaustion | Eliminated | A leak grows steadily and doesn't reset every evening. |
| Cron job or backup | Unlikely | Those usually run off-hours. A job pinned to 09:00-17:00 UTC is possible but would have to be new. |
| Random infrastructure degradation (noisy host, network) | Unlikely | The sharp 09:00-17:00 UTC window points to a load-driven cause. |
| Attack or abusive traffic | Possible, low | Would likely show in error rate or request mix. |
| **Traffic or load shift from the new customer** | **Leading** | See below. |

## Why the new customer is the leading suspect

- The 09:00-17:00 UTC window is a business-hours load shape. Latency that tracks the working day points to load, not a fixed fault.
- The only thing that changed is the customer onboarded Monday. The rise starting Tuesday fits a customer who finished setup, imported data, or went live with real users a day after signing.
- Flat errors with 10x latency means requests are queuing or waiting, not failing. That happens with saturated pools, lock waits, or slow queries on a large tenant.

Mechanisms that fit, from most to least likely:

1. **Connection pool or thread pool saturation.** Their traffic holds connections longer, so everyone else waits for a free one. DB CPU stays low.
2. **Heavy or unindexed queries on one large tenant.** Their data volume makes list or search endpoints slow. This hurts everyone only if those queries hold locks, fill the pool, or evict cache.
3. **Lock or row contention.** Bulk writes or syncs from that customer block shared tables.
4. **Cache thrashing.** A large new tenant's keys evict the working set, so hit rates fall.
5. **Rate limiter, auth or tenant-config lookup.** An enterprise feature such as SSO, audit logging or webhooks adds a slow synchronous step.

One thing could contradict the leading theory. If the customer's integration is small and low-volume, the customer is likely a coincidence. In that case look at a traffic source you haven't mentioned, such as a partner or a scheduled client behavior.

## Checks that separate these, in order

1. **Latency by tenant.** Split p95 by customer ID or API key for 09:00-17:00 UTC.
   - If the new customer's requests are slow and others are normal, the cause is specific to that tenant's endpoints or data.
   - If everyone is slow equally, the cause is shared saturation. Go to step 2.
2. **Request volume by tenant and endpoint, Monday vs. today.** Check whether one customer or one endpoint accounts for most of the growth. Compare per-endpoint p95 from before and after.
3. **Pool and queue metrics.** Look at DB connections in use vs. max, pool wait time, app thread/worker utilization, and queue depth. Pool wait time that tracks the latency rise nearly confirms the saturation theory.
4. **Slow query log or `pg_stat_statements` equivalent**, restricted to the window. Look at total time, not just CPU. Check for lock waits (`pg_locks` / `SHOW ENGINE INNODB STATUS`) and for any new query that appeared since Monday.
5. **Cache hit rate over the past week.** A drop starting Tuesday supports thrashing.
6. **Trace a slow request.** Where the time goes (waiting for a connection, executing a query, or a downstream call) settles the question for that request.

## Confirm and fix

- **Confirm:** throttle or temporarily route the new customer's traffic, or pause their bulk jobs. If p95 returns toward 80ms within minutes, that's the cause. If you can replay their traffic in staging, latency should reproduce.
- **If it's pool saturation:** raise the pool size or add a read replica, and set per-tenant concurrency limits so one tenant can't starve others.
- **If it's slow queries:** add the missing index or paginate the endpoint.
- **If it's contention:** move their bulk writes to a queue or off-peak.
- **Longer term:** add per-tenant latency dashboards and alerts. Raise the question of rate limits and capacity planning in the next customer onboarding checklist.

If the tenant split in step 1 shows the new customer is not the slow one, send me that result, the pool metrics, and the top slow queries, and I'll narrow it further.
