## Hand-off: caching options to Redis stress-test

Exploration is done. Below is the hand-off for the next phase, which stress-tests Redis as the leading option. The next phase can start from this record alone.

### Handover record

```json
{
  "$schema": "reasoning-handover-v1",
  "handover_id": "001-bot-to-ar",
  "source_pattern": { "name": "BoT", "version": "1.0" },
  "target_pattern": {
    "name": "AR",
    "version": "1.0",
    "recommended_entry_point": "attack-redis-cluster"
  },
  "context_transfer": {
    "problem_understanding": "Choose a caching layer for the product catalog.",
    "constraints_identified": [
      "Product catalog reads dominate the workload",
      "Ops burden must stay low (small team)"
    ],
    "assumptions_made": [
      "Stale data is tolerable for some catalog fields",
      "Redis cluster is operable by the current team"
    ]
  },
  "deliverables": {
    "type": "approaches",
    "items": [
      {
        "id": "approach-1",
        "name": "Redis cluster",
        "confidence": 0.60,
        "status": "retained",
        "strengths": ["Fast", "Shared across pods"],
        "weaknesses": ["Adds ops burden"]
      },
      {
        "id": "approach-2",
        "name": "CDN edge caching",
        "confidence": 0.45,
        "status": "retained",
        "strengths": ["Cheap"],
        "weaknesses": ["Stale-data risk"]
      },
      {
        "id": "approach-3",
        "name": "In-process LRU",
        "confidence": 0.40,
        "status": "retained",
        "strengths": ["Simple"],
        "weaknesses": ["Does not share across pods"]
      }
    ],
    "confidence_scores": { "approach-1": 0.55 }
  },
  "evidence_chain": {
    "sources_used": ["Exploration findings from the prior phase"],
    "key_findings": [
      "Redis leads at moderate confidence",
      "CDN and in-process LRU each fail one key requirement"
    ],
    "reference_paths": []
  },
  "recommendations": {
    "focus_areas": [
      "Operational failure modes of a Redis cluster (failover, eviction, memory limits, network partitions)",
      "Cost and ops burden of running the cluster",
      "Cache stampede and invalidation behavior on catalog updates"
    ],
    "avoid_areas": [
      "Re-exploring CDN-only or in-process-only designs unless Redis fails the stress test"
    ],
    "open_questions": [
      "What staleness window does the catalog tolerate?",
      "Who owns on-call for the cluster?",
      "What is the expected peak read rate?"
    ]
  },
  "metadata": {
    "branches_explored": 3,
    "branches_retained": 3,
    "confidence_at_handover": 0.55
  }
}
```

Confidence was carried over at 0.55. That is the stated 0.60 for Redis less a 5% scope-narrowing discount. It stays above the 0.40 floor and below the 0.90 ceiling.

### Starting the stress-test phase

1. **Target:** Redis cluster for the product catalog.
2. **Attack angles:** node failure and failover, cache stampede on a cold start, stale reads after catalog updates, memory exhaustion and eviction, network partition between app pods and the cluster, and cost growth with traffic.
3. **Pass criteria:** Redis holds if each attack has a mitigation that keeps the ops burden acceptable. If Redis fails an attack that no mitigation fixes, fall back to the next approach in the list above.
4. **Open questions to answer first:** the three items under `open_questions` above.

I did not write the `.reasoning/` session files. The hand-off above is the full state and can be pasted into the next phase.
