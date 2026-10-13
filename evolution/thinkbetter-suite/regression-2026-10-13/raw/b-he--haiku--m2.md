**Most likely cause:** the new enterprise customer's daytime traffic is saturating a shared resource, most likely the database connection pool or worker threads. Requests then wait in a queue instead of failing.

That fits every clue you gave:
- The slowdown is confined to 09:00–17:00 UTC, when that customer's users are active.
- It started after the customer was onboarded on Monday.
- The error rate is flat, so requests are slow rather than failing.
- Database CPU is normal, so the database is not working hard. The application is more likely waiting for a connection.

**Ranked causes**

| # | Likely cause | Why it fits | Why it might be wrong | Check first |
|---|---|---|---|---|
| 1 | Connection pool or worker saturation from the new tenant's load | Time window, onboarding date, normal DB CPU, flat errors | The pool may not be the real limit | Pool wait time, and active vs. max connections, 09–17 vs. off-hours |
| 2 | Slow queries on the new tenant's data (missing index, large scans, lock waits) | Onboarding adds a large dataset, and slow queries don't always show up as high CPU | Would normally show as higher DB latency | Slow query log filtered by tenant ID; lock wait time |
| 3 | A slow dependency called on the tenant's requests (SSO, webhooks, email, file storage) | Enterprise features often add these calls | Usually produces timeouts and errors, which are not present | Per-span breakdown of p95 by downstream service |
| 4 | Retry or polling storm from the customer's integration | Daytime-only, new integration, errors stay flat because retries succeed | Request rate would look visibly higher | Request rate per API key or tenant |
| 5 | Cache thrash: the new tenant's keys evict shared entries | Evictions cause slow reads without errors | Cache hit ratio would drop | Hit ratio and eviction count, before vs. after Monday |
| 6 | Infrastructure change that is not a code deploy: config flag, autoscaling, one slow instance behind the load balancer, noisy neighbour | Rules out code deploys only | Would usually affect all tenants at all hours | Latency per instance; config and feature-flag change log |

**Cheapest checks first**

1. Split p95 by tenant or API key, and by hour. If the new tenant accounts for the slowdown and other tenants are normal, causes 1–5 are in play. If every tenant is slow, cause 6 moves up.
2. Compare business-hours and off-hours p95 for the same endpoints. Normal off-hours confirms a load-dependent cause.
3. Check pool wait time. If requests spend the extra time waiting for a connection, the cause is cause 1. Raise the pool size or add a per-tenant limit.
4. Trace one slow request end to end. Find where the extra ~820 ms goes. A single trace usually separates causes 1, 2 and 3.
5. Only if 1–4 are negative: check per-instance latency and the config and flag history.

**Confidence:** about 60% that the cause is load-driven resource contention from the new tenant (causes 1 or 2 most likely). The cause is not confirmed. I don't have access to your metrics, so this rests only on the facts you gave. Step 1 and step 4 should settle it.
