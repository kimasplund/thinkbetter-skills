## Most likely cause: the new enterprise customer's business-hours load is saturating something shared

Latency up about 11x while error rate and database CPU stay flat means requests are succeeding but waiting: queueing for workers or connections, lock or I/O waits, or a slow call in the request path. It is not a failing query or a compute-bound database. The 09:00–17:00 UTC window and the Monday onboarding are the strongest clues.

### Candidate causes

| # | Candidate | Fits the facts | Against | Status |
|---|---|---|---|---|
| A | The enterprise tenant's integration sends heavy traffic during its working hours and saturates shared worker, connection, or rate-limit capacity | Starts with onboarding, only in their hours, errors flat (queueing, not failing) | Needs their volume to be large enough to matter | Leading |
| B | An endpoint the tenant calls (large list, export, or N+1 query) is slow on their larger dataset | Tied to their data; onset matches onboarding | Would look like one endpoint, not a global rise | Strong |
| C | Lock or connection waits from the tenant's bulk writes | Explains normal CPU: time is spent waiting, not computing | Needs lock or wait-event evidence | Possible |
| D | A slow outbound call in the request path, such as the tenant's SSO, a webhook, or a third-party lookup | Business-hours only if the dependency is used by them | Requires the call to sit in the request path | Possible |
| E | Cache eviction from the new tenant's data, sending more reads to slower storage | Timing fits | Usually shows up as database load, which is normal | Less likely |
| F | Shared infrastructure contention (noisy neighbour, CPU steal, load balancer or egress throttling) | Time-correlated | Would not start with the tenant's onboarding | Less likely |
| G | Measurement change (new sampling, moved timer, new middleware) | Explains a sudden jump | Would not produce a business-hours-only shape | Low |
| H | A batch or scheduled job that runs in business hours | Time window fits | Nothing changed on Tuesday to start it | Low |
| U | Something not on this list | — | — | Kept open until the checks below run |

Already ruled out by the facts: a code deploy (none happened), and database compute saturation (CPU is normal, so a slow-query CPU explanation is weak).

### Checks, in order

1. **Split p95 by tenant or API key, and by endpoint, for Monday through Wednesday.** If the slowdown sits in the enterprise tenant's requests, A or B is the cause. If all tenants are equally slow, drop A and B and move to F and G. This single split separates most of the candidates.
2. **Compare the tenant's request rate with the latency curve minute by minute.** A tight correlation supports A. Latency rising while their rate stays flat rules A out.
3. **Look at a trace of the slowest endpoint and its time breakdown.** Time spent acquiring a pool connection points to A or C. A database span with lock-wait events points to C. Time in an outbound call points to D. One large query per request points to B.
4. **Check database wait events and lock waits between 09:00 and 17:00 UTC** (not CPU). Sessions waiting on locks or I/O point to C.
5. **Check application connection-pool and worker-queue metrics** (acquire wait time, queue depth, thread utilization). Saturation at the business-hours peak points to A.
6. **Check per-host CPU steal and load balancer metrics.** If both are flat, F is out.

The fastest first step is check 1. It takes one query and separates A and B from the rest.

### Fixes once confirmed

- **A:** per-tenant rate limits, or a separate pool or queue for that tenant; ask the customer to batch requests or use bulk endpoints.
- **B:** add an index, pagination, or caching for that endpoint.
- **C:** shorten transactions, batch the writes, and set a lock timeout.
- **D:** add timeouts and caching on that call.

### Confidence

About 60% that A or B is the cause, based on the timing and the onboarding. Two candidates still stand, so the tenant split and the endpoint trace should settle it before anyone changes configuration. If the tenant split shows no difference, the cause is outside the tenant, and F and G need to be reopened.
