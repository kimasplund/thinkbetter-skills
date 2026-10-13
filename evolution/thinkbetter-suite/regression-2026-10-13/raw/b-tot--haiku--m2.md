**Recommendation: ClickHouse**, with plain Postgres ruled out and TimescaleDB as the fallback if the load turns out to be much smaller.

**Why the volume decides this**

200,000 points per second is about 17 billion points a day. Kept for 90 days, that is roughly 1.5 trillion rows. At that scale the question is less "which database has time-series features" and more "which engine stores and scans this cheaply on a small team's hardware."

- **Plain Postgres with partitioning** is the familiar choice, but it is the weakest fit. Partitioned heap tables with indexes struggle to absorb this write rate, and dropping 90-day-old partitions is easy but scanning and aggregating across trillions of rows is slow and expensive. Your team's Postgres skills help, but they don't fix the engine.
- **TimescaleDB** is the closest to what your team knows: it is Postgres with hypertables, native compression, and continuous aggregates. It can ingest well on one large node, but at 200k/s sustained you would be pushing a single machine hard, and horizontal scaling is limited compared with the alternatives. It is the right answer if the real rate is closer to 20k to 50k/s.
- **InfluxDB** handles this ingest rate and has SQL in its current version, but its ecosystem and query model have shifted across versions, which adds risk for a three-person team that needs stable SQL access.
- **ClickHouse** is built for exactly this shape: very high insert throughput in batches, columnar compression that typically shrinks time-series data by an order of magnitude, a TTL clause that enforces the 90-day retention automatically, and horizontal scaling by sharding and replication. It meets the hard SQL requirement.

**The cost you accept with ClickHouse**

Its SQL dialect differs from Postgres in places, and the operational model (MergeTree tuning, replication coordination) is new to the team. Three people can run it, but expect a learning period of a few weeks, and budget for it.

**What makes it work**

- Insert in large batches (thousands of rows per insert, or use async inserts). Single-row inserts are the usual way this fails.
- Order the table by `(device_id, timestamp)` so per-device queries read contiguous data.
- Set `TTL timestamp + INTERVAL 90 DAY` so retention needs no cron job.
- Use materialized views for the rollups you query most, rather than scanning raw points.
- Avoid row updates and deletes; treat the table as append-only.

**Assumptions and what would change the answer**

- I assumed 200k/s is sustained, not a peak, and that points are small (a device ID, a timestamp, a few numeric fields). If the average is well below that, TimescaleDB becomes the better choice because it keeps the team on Postgres.
- If the team cannot take on a second database engine at all, TimescaleDB is the compromise: slightly lower ceiling, no new operational model.

**Next step:** load-test the top candidate with a realistic payload for a day before committing. Measure sustained inserts, compressed storage per million points, and your three slowest real queries.

Confidence: about 80%, mostly dependent on the sustained rate and the actual query mix.
