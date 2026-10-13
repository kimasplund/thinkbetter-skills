**Recommendation: TimescaleDB, self-hosted on a single well-provisioned node (with a replica), with ClickHouse as the planned escape hatch if the workload outgrows it.**

## Why TimescaleDB wins

Your hard constraints are SQL access, a team of 3 who know Postgres, and 200k writes/second held for 90 days. That is about 17 billion points a day and roughly 1.5 trillion points at steady state. Three things follow from that.

- **It is Postgres.** Same wire protocol, drivers, `psql`, pg_dump/WAL tooling, monitoring, and extensions (PostGIS, etc.). Your team's existing knowledge carries over, so you pay almost no learning cost. With three people, operational familiarity is worth more than a benchmark lead.
- **It handles the two things plain Postgres struggles with at this volume.**
  - Hypertables automatically chunk by time, so recent data stays in a small hot set of indexes.
  - Native columnar compression typically shrinks time-series data 10-20x. Without it, 1.5 trillion rows at even ~40 bytes each (with index overhead, more) is tens of terabytes. With it, you are in the low single-digit terabytes.
- **Retention is a metadata operation.** A retention policy drops whole chunks after 90 days. This is instant and does not cause the vacuum and bloat problems that `DELETE` would on a table this size.

## Why the others lost

- **ClickHouse** is the strongest on raw ingest and scan speed, and it would handle 200k points/s with room to spare. It loses on fit. Its SQL dialect has real differences from Postgres, and it has no transactions in the usual sense. Updates and deletes are awkward, and operating it (merges, parts, partitioning keys, replication via Keeper) is a new skill set for a Postgres team. It is the right answer if you expect to grow 5-10x or run heavy cross-device analytics. It is more than you need now.
- **InfluxDB** is purpose-built for this workload, but it is the weakest match for your hard requirement. Older versions (1.x, 2.x) query through InfluxQL or Flux, not SQL. Version 3 adds SQL, but it is a newer engine with a different operational model, and your team would be starting from zero on it. It satisfies the requirement on paper but gives up the Postgres familiarity advantage.
- **Plain Postgres with partitioning** is the lowest-risk option for skills, and it works at lower rates. At 200k rows/s you would be managing partition creation and dropping yourself (pg_partman or cron), with no compression, heavy WAL volume, and index maintenance competing with ingest. It is borderline-feasible only with aggressive tuning and few indexes, and storage cost would be many times higher. Timescale gives you what this approach would reach for anyway, with less hand-rolled machinery.

## How to run it

1. **Ingest in large batches.** Use `COPY` or multi-row inserts of thousands of rows, from several parallel writers. Single-row inserts will not reach 200k/s on any of these options.
2. **Keep indexes minimal.** Typically one on `(device_id, time DESC)`. Every extra index costs ingest throughput.
3. **Pick chunk size deliberately.** Aim for chunks whose active indexes fit comfortably in RAM, often 1 day or less at this rate.
4. **Compress after a short delay.** For example, compress chunks older than 1-2 days, segmenting by `device_id` and ordering by time. Keep recent data uncompressed for fast writes.
5. **Add a retention policy** at 90 days.
6. **Use continuous aggregates** for dashboards (1-minute and 1-hour rollups), so queries rarely touch raw data.
7. **Provision for it.** Fast NVMe storage, plenty of RAM, and a streaming replica for failover. WAL volume at this rate is substantial.

## Uncertainties and what to verify

- **Throughput on your hardware and schema.** 200k points/s is well within what Timescale reports on a single node with batched inserts, but it depends on row width, number of tags and columns, and index count. Run a load test with your real payload shape before committing. This is the one assumption that could change the answer.
- **Point size.** I assumed narrow rows (timestamp, device ID, a few numeric values). If each "point" is wide or carries JSON, storage and ingest cost rise sharply.
- **Query patterns.** I assumed mostly recent-window and per-device queries, plus some aggregates. If analysts will routinely scan the full 90 days across all devices, ClickHouse becomes more attractive.
- **Licensing.** Compression and continuous aggregates are under Timescale's community license. That is fine for self-hosting and internal use, but check it if you plan to offer a database service to others.

**Switch trigger:** if the load test cannot sustain about 1.5-2x your target rate (200k/s) on hardware you are willing to pay for, or ingest is expected to grow well beyond that, move to ClickHouse. Keep the schema simple and the ingest path behind a thin writer service so a migration stays cheap.
