**Recommendation: TimescaleDB** (PostgreSQL with time-series extensions), run on a single well-sized node first, with a load test before you commit.

**Why it wins for your constraints**

- **SQL and the team:** It is Postgres, so your three engineers keep their existing skills, tooling, drivers, and migrations. SQL access is a hard requirement, and this is the only candidate where SQL is the native interface rather than a second dialect or a newer query layer.
- **Retention math:** 200k points/s is about 17 billion points a day, or roughly 1.5 trillion points across 90 days. Plain Postgres can hold that volume with partitioning, but row storage and index maintenance make it expensive, and compression is weak. TimescaleDB's columnar compression on older chunks typically shrinks time-series data by an order of magnitude, which is what makes 90 days affordable. Confirm the ratio on your real data.
- **Ingest:** At 200k/s the write path must be batched (COPY or multi-row inserts, ideally 5k to 10k rows per batch) and sized to the instance. This is achievable on one large node, but it is the number most likely to fail, so it has to be tested rather than assumed.

**Why not the others**

- **ClickHouse:** The strongest raw ingest and compression, and it speaks SQL. It is the runner-up and the right choice if ingest grows well past this target or storage cost dominates. Against you: a different SQL dialect, weaker support for row-level updates and relational joins, and a new operational model for a team of three.
- **InfluxDB:** Good ingest, but the SQL layer is newer and less mature than the rest of the field, and the team has no operational history with it. The SQL requirement fits, but the ecosystem risk is higher than the others.
- **Plain Postgres with partitioning:** Simplest on paper, and the team knows it. But at this volume, storage cost, vacuum and index overhead, and the lack of native compression make it the weakest on both cost and sustained write throughput.

**Confidence: about 75%.** The main uncertainty is the shape of the data, not the choice of engine.

**What would change the answer**

- Sustained ingest is well above 200k/s, or the cost of storage at 90 days is too high even with compression: move to ClickHouse.
- Queries are mostly large aggregations over many series and rarely touch individual rows: ClickHouse becomes stronger.
- Points have very high tag cardinality: check the TimescaleDB chunk and index design before committing.

**Before committing**

1. Load test TimescaleDB on a node sized for your target, using realistic batch sizes and at least 2x the target rate for a sustained period.
2. Measure the compressed size of a few days of real data and extrapolate to 90 days.
3. Run your ten most important queries against the test data and check latency.
4. If any of these fail, run the same test on ClickHouse before you decide.
