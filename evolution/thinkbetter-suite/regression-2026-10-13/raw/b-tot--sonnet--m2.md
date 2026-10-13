## Recommendation: TimescaleDB, with ClickHouse as the fallback

For a team of 3 who know Postgres and need SQL, TimescaleDB is the best fit. It is Postgres, so your drivers, tooling and mental model carry over. It also adds what plain Postgres lacks at this volume: automatic time partitioning, native compression, and cheap retention.

### The numbers that drive the decision

- 200k points/s is about 17 billion points per day.
- Over 90 days that is about 1.5 trillion rows live at any time.
- In vanilla Postgres a narrow row (timestamp, device id, value) costs roughly 40-50 bytes with tuple header and index. That comes to 60-80 TB before replicas. This is why plain Postgres drops out, even though it could probably ingest the rate.
- Columnar compression typically cuts time-series data 10-20x. Treat the range as an estimate until you test it on your own data. That would put you at a few TB to low tens of TB.

### How the four candidates compare

| | Ingest at 200k/s | Storage over 90 days | SQL | Team ramp-up | Retention |
|---|---|---|---|---|---|
| **TimescaleDB** | Feasible on one well-sized node with batched COPY; multi-node or sharding only if your rows are wide | Good with compression | Full Postgres | Very low | `drop_chunks` on a policy, instant |
| **ClickHouse** | Best of the four, with lots of headroom | Best (often the smallest) | Own dialect, close to ANSI but not Postgres | Medium: new ops model, merges, batch-insert discipline | TTL, easy |
| **InfluxDB** | Strong | Good | Only in the newer 3.x line; older versions use InfluxQL or Flux | Medium to high, plus version-maturity risk | Built in |
| **Plain Postgres + partitioning** | Borderline; vacuum, index maintenance and WAL become the bottleneck | Poor: no compression | Full | None | Drop partitions, but you manage them yourself |

### Why not the others

- **Plain Postgres with partitioning:** You would hand-build partition management and live with 5-10x the storage and I/O. You would end up rebuilding a worse Timescale.
- **InfluxDB:** The SQL requirement is only well served by the newest major version, and its ecosystem and query features are still moving. You would also give up the Postgres knowledge your team already has.
- **ClickHouse:** It is technically the strongest on raw ingest and compression, so it is a real contender. It loses because of the learning curve for 3 people, the non-Postgres SQL dialect, and the operational behaviour you must learn (async merges, small-batch inserts hurting, a weaker story for single-row updates and joins). The hard requirement is SQL access, and ClickHouse meets it, but in an unfamiliar dialect.

### What to do with Timescale

1. Use a hypertable partitioned on time, with device id as a secondary space dimension only if you measure a benefit. Choose chunks of roughly 6-12 hours, so a chunk's indexes fit in memory.
2. Keep indexes minimal: the (device_id, time) one only. Every extra index costs you ingest rate.
3. Ingest in batches of thousands of rows, using COPY or multi-row inserts from a few parallel writers. Do not insert row by row.
4. Enable compression on chunks older than about a day, with `segmentby = device_id` and `orderby = time`.
5. Add a retention policy at 90 days.
6. Use continuous aggregates for dashboards, so queries rarely scan raw data.
7. Plan the hardware: NVMe, plenty of RAM, and a streaming replica for HA.

### Check this before you commit

Spend a week benchmarking with your real payload shape, not synthetic narrow rows:

- Sustain 250k points/s (25% headroom) for 24 hours while running your typical dashboard queries at the same time.
- Measure the compression ratio and the p95 query latency on 7 days of data.
- If you cannot sustain the rate on one node, or the compressed size is much larger than expected, move to ClickHouse. The data volume and write profile are exactly what it is built for, and the SQL requirement is still met.

### Assumptions

- Each "point" is one narrow row (timestamp, device id, one or a few values). If points are wide, with dozens of metrics each, ClickHouse becomes more attractive.
- A single region and a single cluster, with batching available at the writers.
- Reads are mostly recent-window dashboards and per-device lookups, not heavy ad-hoc scans across all 1.5 trillion rows. If heavy full-history analytics matter, that also pushes toward ClickHouse.
- A self-hosted or managed Timescale deployment works for you. The compression and continuous aggregate features sit under Timescale's own license, which is fine for your use but should be checked against your plans.

**Confidence: about 75%.** The elimination of plain Postgres and InfluxDB is solid. The Timescale versus ClickHouse call depends on your row width and query mix, which I had to assume, so the benchmark above is what settles it.
