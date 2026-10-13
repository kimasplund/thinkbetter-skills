# Hand-off 1: Caching exploration → adversarial stress-test of Redis

**Problem statement:** Choose a caching approach for the product catalog. Exploration is finished; the leading candidate is a Redis cluster. The next phase stress-tests Redis before any commitment.

**Constraints and success criteria:** The approach must serve the product catalog with fast reads. Operational burden must be acceptable for the team. Stale-data risk must be understood. Cross-pod sharing matters, because cache state should not diverge between pods.

**Chain so far:** breadth-of-thought (exploration) → adversarial-reasoning (stress-test of Redis)

**Pattern used:** breadth-of-thought (assumed from the phase name "exploring caching options"), completed through option enumeration and first-pass evaluation. Stress-testing has not started.

**Findings so far:**
- Redis cluster is fast and leads the field. Evidence: exploration phase comparison.
- Redis cluster adds ongoing operational burden. Evidence: exploration phase comparison.
- CDN edge caching is cheap but carries stale-data risk. Evidence: exploration phase comparison.
- In-process LRU is simple but does not share state across pods. Evidence: exploration phase comparison.

**Ruled out (do not re-explore):**
- None were eliminated outright. CDN edge caching and in-process LRU were demoted behind Redis, but remain on record as fallbacks.

**Assumptions:**
- The product catalog is read-heavy.
- The team can absorb some Redis operations work.

**Open questions:**
- How much operational load can the team carry for a Redis cluster?
- What staleness window is acceptable for catalog data, and does it rule out CDN edge caching?
- Does the expected pod count make the in-process LRU's lack of sharing a real problem?
- What failure modes does a Redis cluster outage create for the catalog, and is there a degraded-mode path?

**Confidence:** 55% — basis: the user stated moderate confidence in Redis. Exploration covered the main options, but no stress-testing or measurement has happened yet. Confidence is capped by the 10% floor and 95% ceiling and is not raised by this hand-off.

**Next:** adversarial-reasoning should start at the attack-surface step, focused on how Redis fails. Priority areas are cluster failover and split brain, stale or poisoned cache entries, cache stampede on cold start, memory exhaustion and eviction behavior, and operational error by the team. Compare each failure against the CDN and in-process LRU fallbacks.
