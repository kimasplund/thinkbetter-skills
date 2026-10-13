# Handover Templates

Filled-in examples of the hand-off record from SKILL.md for common pairs of reasoning skills. Each shows only the fields that matter most for that pair; the full template still applies.

## Contents

- [breadth-of-thought to tree-of-thoughts](#breadth-of-thought-to-tree-of-thoughts)
- [tree-of-thoughts to adversarial-reasoning](#tree-of-thoughts-to-adversarial-reasoning)
- [hypothesis-elimination to tree-of-thoughts](#hypothesis-elimination-to-tree-of-thoughts)
- [self-reflecting-chain to hypothesis-elimination](#self-reflecting-chain-to-hypothesis-elimination)
- [adversarial-reasoning to hypothesis-elimination](#adversarial-reasoning-to-hypothesis-elimination)
- [Which pattern hands off well to which](#which-pattern-hands-off-well-to-which)
- [Common mistakes](#common-mistakes)

## breadth-of-thought to tree-of-thoughts

Explore, then optimize among the top candidates.

- **Findings so far:** three retained approaches (A 72%, B 78%, C 68%), each with its main strength and risk.
- **Ruled out:** the pruned approaches, each with its fatal blocker.
- **Next:** tree-of-thoughts uses A, B and C as its first-level branches and scores them on the stated criteria (e.g. latency, cost, scalability).

## tree-of-thoughts to adversarial-reasoning

Select, then validate before committing.

- **Findings so far:** the winning path (e.g. JWT, RS256 signing, keys served from a key endpoint, secrets in a vault) and why it won.
- **Assumptions:** the ones the winner depends on (e.g. vault availability above 99.9%, internal network latency under 10 ms). These are the attack targets.
- **Ruled out:** alternative architectures already evaluated; do not re-open them.
- **Next:** adversarial-reasoning attacks the security boundaries, failure modes and edge cases of the winner.

## hypothesis-elimination to tree-of-thoughts

Diagnose, then choose a fix.

- **Findings so far:** confirmed cause (e.g. payment gateway p99 latency rose from 50 ms to 800 ms) with the evidence that discriminated it from the other hypotheses.
- **Constraints:** limits discovered during diagnosis (e.g. the vendor cannot be changed).
- **Open questions:** acceptable latency degradation; budget for extra infrastructure.
- **Next:** tree-of-thoughts treats "mitigate external API latency" as the problem and generates fix options as its first-level branches.

## self-reflecting-chain to hypothesis-elimination

A step-by-step trace hit a dead end.

- **Findings so far:** the steps that held (e.g. event handler found, it calls the form validator) and the step where backtracking failed (validation logic unclear, confidence down to ~35%).
- **Ruled out:** the parts of the chain known to be correct, so the search can narrow.
- **Next:** hypothesis-elimination starts from seeds around the failure point (validation passes incorrectly, throws silently, races).

## adversarial-reasoning to hypothesis-elimination

An attack succeeded; find how the weakness got in.

- **Findings so far:** the working attack (e.g. JWT algorithm confusion, switching RS256 to HS256 and signing with the public key) and its impact.
- **Open questions:** was algorithm validation ever present, and when did it go?
- **Next:** hypothesis-elimination tests seeds such as "never implemented", "removed in a refactor", "library upgrade changed the default", "configuration override".

## Which pattern hands off well to which

| From | Best hand-off to | Why |
|------|------------------|-----|
| breadth-of-thought | tree-of-thoughts, hypothesis-elimination | Exploration done; optimize or diagnose |
| tree-of-thoughts | adversarial-reasoning, self-reflecting-chain | Winner found; validate it or trace its implementation |
| hypothesis-elimination | tree-of-thoughts, self-reflecting-chain | Cause found; choose a fix or trace the mechanism |
| self-reflecting-chain | hypothesis-elimination, tree-of-thoughts | Trace done or stuck; test hypotheses or compare branches |
| adversarial-reasoning | hypothesis-elimination, tree-of-thoughts | Attack found; trace its origin or evaluate fixes |
| dialectical-reasoning | tree-of-thoughts, negotiated-decision-framework | Synthesis reached; optimize it or align stakeholders |
| analogical-transfer | breadth-of-thought, tree-of-thoughts | Analogy found; explore adaptations or pick the best |
| rapid-triage-reasoning | hypothesis-elimination, tree-of-thoughts | Situation stable; find the root cause or revisit the decision |
| negotiated-decision-framework | tree-of-thoughts, dialectical-reasoning | Stakeholders aligned; optimize or resolve leftover tension |

Every hand-off still obeys the cycle rule in SKILL.md: no pattern twice in one chain, at most 5 patterns.

## Common mistakes

- **Hand-off without state.** "Found some good options, evaluate them" forces the next pattern to start over. Pass the findings, evidence and rule-outs.
- **Losing the evidence chain.** Passing option names without the reasons they survived lets weak options back in.
- **Confidence inflation.** Each pattern nudging confidence up until it reads 99%. A hand-off never raises confidence; only independent agreement does, capped at 95%.
- **Ignoring rule-outs.** The receiving pattern re-explores what the previous one pruned. Trust earlier conclusions unless new evidence appears.
