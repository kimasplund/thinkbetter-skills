# Follow-up: negotiated-decision-framework (gauntlet 2026-10)

Post-hoc forensic review of the closed round. The verdict (NOT VALIDATED) stands; nothing here re-scores it. The tested arm (`arms/f8/SKILL.md`, v2.2.1) is byte-identical to the shipped `skills/negotiated-decision-framework/SKILL.md`.

Arm map: f8 = new (skill), i0 = none. Blind codes per brief:

| brief | skill (r1..r4) | no skill (r1..r4) |
|---|---|---|
| 1 ski hill | V5F, Z0Y, N0D, H7A | H7T, I8Y, V7E, P8A |
| 2 hospital | K0B, L9V, T0A, T7C | T5P, S4P, N3E, L6A |
| 3 acquisition | A5V, F8T, G8J, M2C | J8F, Y8N, H0C, C1A |

## 1. Is the improvement real?

**Partly. The direction is real; the size is probably overstated.**

What holds up:
- **V4 decision usefulness is positive in both run batches:** +0.58 on r1/r2 and +1.00 on r3/r4. **V2 specificity** is also positive in both (+0.25, +0.92). V1 and V3 flip sign between the batches (V1 −0.08 → +0.67, V3 −0.42 → +1.08), so they are noise.
- **Rankings are 5–1.** J-A placed the skill arm ahead on all three briefs (mean position 3.75/2.5/3.0 vs 5.25/6.5/6.0). J-B placed it ahead on briefs 2 and 3 and behind on brief 1.
- **Keys** (0.96 vs 0.90): the gain is concentrated where the planted keys needed arithmetic or a link between facts.
  - Brief 1, k2 (140/410 is a blocking third): the skill arm got ✓ 4 of 4 and the no-skill arm ✓ 2 of 4 (V7E, P8A and H7T scored ~). N0D says "The 140 debenture holders are 34% of the membership... can block the deal on their own."
  - Brief 1, k3 (volunteers as a hidden veto): ✓ 2 of 4 vs 1 of 4. N0D says "They aren't in the offer at all, yet the hill can't open without certified patrollers."
  - Brief 2, k4 (the union's real interest is the suspended premium): ✓ 3, ✗ 1 vs ~ 4. For example, K0B writes "Consider whether restoring the specialty premium, even temporarily, is on the table."
  - Brief 3: both arms got 4 of 4 on every key (ceiling).
- **Concrete things the skill replies did better, per the judges:**
  - V5F gives the clearest bottom line: "wouldn't bring the offer to the AGM in its current form", plus what would change that (J-A V4 7).
  - N0D (J-A ranked it first, "the most actionable reply") gives ranked asks, a week-by-week sequence and "If Alderline won't move". It also has the separable-interest insight: Dariusz's need for release from the guarantee "can be met in ways that don't depend on the deal passing".
  - M2C (ranked first by J-B and second by J-A, V4 7/7) has a "What would change my recommendation" section, separates notice from consent on Pellworth, and gives signs that tell commitment from compliance.
  - K0B gives a per-group *agreed / agreed if X / not yet asked* status for the CEO.
  - In brief 3, J-A ranked A5V first: "distinguishes 'live with' from 'argue for'", with a named tie-breaker.
  - These map to the skill's commitment machinery: the Commitment Template's conditions, review point and dispute resolution, the commitment levels, BATNA (the fallback), and interest archaeology.

What weakens it:
- **The size comes mostly from the extension batch.** Under the final scores, the value margin is +0.08 on r1/r2 and +0.92 on r3/r4. The skill arm was stable (5.75 → 6.04). The no-skill arm dropped (5.67 → 5.12) because its r3/r4 replies were weak: N3E and L6A have arithmetic errors, and C1A and H0C are thin. Pre-extension, the margin was +0.17 and rankings were 1–2.
- **Judge re-scoring noise is about ±1 per cell.** In the extension the judges re-scored all eight replies per brief, and 21 of the 24 r1/r2 cells changed on at least one dimension.
- **Worse in the skill arm:**
  - Length on briefs 1 and 3 (see G1).
  - Faint method vocabulary (see G2).
  - A few unsupported assertions that come from the BATNA/power prompts. H7A says "Their alternatives are other hills" (J-B: "asserted, not given"), and Z0Y says "The deal is probably worth doing", unsupported.
  - Odds stated without grounding. H7A writes "roughly even if you do only the process work", and both judges flagged it as "loosely/thinly grounded".

Best estimate of the true value effect: about +0.3, carried by V4 and V2. That is real but small, and not reliably above the +0.5 claim bar.

## 2. Blockers

### guard_audit_ceremony: FAIL (3 hits vs 2 of 12; margin −0.083 equals the band, and the rule's "less than one hit" is strict)

Skill arm hits (quoted by the auditor):
- **N0D** (brief-1 r3), from the closing of "Assumptions I made": "the core approach holds: get the legal facts straight, get the three [outside parties and the dissenting directors to shape the terms...]"
- **K0B** (brief-2 r1), the closing paragraph: "A plan that says 'here are the five conditions, here is who has agreed to what, and here is the one decision I need from you' is much easier for a CEO to back..."
- **L9V** (brief-2 r2), the closing paragraph: "You will have a costed, staffed plan, with each group's commitment recorded and the open items named."

No-skill hits:
- **L6A** (brief-2 r4), heading: "Where the plan breaks (the pathway view)"
- **C1A** (brief-3 r4), closing: "The one-line pitch for the offsite: We capture the savings and the bundle..."

**Classification: mainly an instrument artifact plus small-sample noise. The skill's contribution is weak.**
- **K0B and L9V were audited in the pre-extension run with zero ceremony** (`audit-pre-ext/audit.json` covers both). The re-audit of the same text flagged them. Two of the skill's three hits are auditor variance on identical replies.
- Four of the five hits in both arms are closing wrap-ups, a base-model habit. The auditor passed similar closings: V5F's "My honest read" restates the four risks, J8F's "If you can only do three things", and H7T's "What to say".
- K0B's line is arguably advice about how to pitch the CEO, not a recap. A reader would not mind it.
- The skill link is indirect. The Output Template ends with "Implementation Notes" and "Confidence: [X]%", which invites a closing wrap paragraph. It costs one sentence to forbid, so the fix below includes it.
- Under one-hit tolerance this would PASS. The G1/G2 NOISE would still finalise NOT VALIDATED, as the research note says.

### guard_judge_G1 (proportionality): NOISE (per brief −0.62, +0.75, −0.75)

**Classification: skill defect, moderate.**
- **G1 is length.** Across all 48 judge cells, the correlation between word count and G1 is −0.81. The skill replies' median was 1.27× the no-skill median on brief 1, 0.82× on brief 2 and 1.30× on brief 3. The longest replies scored G1 4 from both judges: V5F (2041 words), N0D (1886) and A5V (1843).
- **Mechanism: the skill organises the answer as a roster of parties, often twice.** The no-skill replies are organised by blocker: "Fix these before anything else", "Four issues that could sink the deal", "Why the facts point this way". The skill replies add a per-party section on top of the issues:
  - V5F: "Who really matters" (386 words), then a separate lease section (260), then asks grouped by party.
  - N0D: "What each party really needs" (674 words) covers the same four blockers the asks then repeat.
  - A5V: "What each person needs" (198) and later "What to offer, and to whom" (236), the same four people twice.
  - M2C: "What each party needs" and later "Protecting the earnout and the people".
  - Rosters include parties that cannot block: Alderline, the nine employees, "Your platform team" as a needs entry.
  - G8J merged needs and get/give into one section ("What each party needs, and what they get"). It was the shortest skill reply on brief 3 (1291 words) and scored G1 5/5 and V 6/6.
- **Causing lines:**
  - Output Template **L362–365** (Key Stakeholders table) **plus L379–383** (Value Distribution table): one roster of parties, then a second.
  - **L367–369** (Zones of Agreement section).
  - **L55–81** (a nine-field profile per stakeholder).
  - **L50** "Identify all stakeholders (not just vocal ones)". This is good for analysis (it found the Vantongerens, SPD and physio), but nothing tells the reply to report only the parties who matter.
  - Nothing in the skill addresses size.
- **Why brief 2 was fine.** In the hospital case the stakeholders *are* the blockers: anaesthesia, SPD, physio and the ward are each a capacity constraint. A roster by department is therefore the issue list, with no duplication. Three of the four skill replies (L9V, T0A, T7C) put it in one compact table (1209–1328 words). The no-skill replies were the long ones on that brief: L6A (1746 words) with "pathway view" plus numbered sections, and T5P (1594). On briefs 1 and 3 the blockers are contract facts (the lease, the debentures, the earnout, Pellworth's clause, the cloud commit). Those attach to parties but are not the same as them, so roster plus facts plus asks repeats itself.

### guard_judge_G2 (machinery leakage): NOISE (per brief −1.0, +0.38, −0.25)

**Classification: skill defect, mild. The backstage rule cannot catch it.**
- **Brief 1 (−1.0). The no-skill arm scored 7 on every cell.**
  - **H7A** (G2 5/5). Its section "What you all already agree on" is "negotiation scaffolding" to J-B and reads "a little like scaffolding" to J-A. It also has the odds paragraph, and "Their alternatives are other hills" (the BATNA prompt). The causes are Zones of Agreement **L91–123** (the Foundation Statement) and Output Template **L367–369**, Confidence **L392–393**, and BATNA **L221–223**.
  - **V5F** (6/7) and **N0D** (6/6) have a "light position/interest trace" (J-A, both). V5F writes "Their stated position is 'keep my lifetime pass.' Underneath..."; N0D writes "His position is 'approve the deal.' His interest is..." The causes are **L53, L72–73, L83–87, L153–157 and L322** (stated position vs underlying interest).
  - **Z0Y** (6/7) has "Everyone wants the hill to survive... The disagreement is mostly about...", which is the agreement zone again, plus "the underlying worry".
- **Brief 3 (−0.25).** J-A gave 6 to A5V, G8J and M2C (and to no-skill J8F); J-B gave all of them 7. The traces are commitment-level and value-distribution vocabulary: "'Can you live with this' and 'will you argue for this'", "whether you have commitment or only compliance", and per-party "They give up...". The causes are **L225–229** (comply/accept/endorse/champion) and **L379–383**. These are incidental, and the judges also praised them as content.
- **Brief 2 (+0.38).** Only K0B carried a trace ("Where people really agree", which J-A called "negotiation-method scaffolding", 6/6). The no-skill arm had its own: S4P "Positions vs interests" phrasing (6/6), and L6A "(the pathway view)" with numbered sections (6/5). The base model emits this vocabulary unprompted, and on brief 2 it happened to do so more in the no-skill arm.
- **Why the backstage rule (L410) misses it.** Its literal search list bans method names, "pattern", "branch" and similar, but not the method's *stage vocabulary* (stated position / underlying interest, zones of agreement, BATNA, commitment levels). "What you all already agree on" passes the literal search.
- **The skill also contradicts itself.** The Output Template asks for "## Confidence: [X]%" (L392) and is headed "# NDF Decision Record" (L357). The backstage rule forbids both ("no confidence-aggregation", no "NDF").

### Other conditions
- G3, leaks, length cap (1.13×), value, ranking, negative, framing and agreement all PASS.
- The value PASS rests on the extension batch (see §1).

## 3. Proposed minimal edit (15 changed lines, Output Template plus the backstage rule)

This keeps everything that produced the gain: interest archaeology, "identify all stakeholders" during analysis, BATNA, the Commitment Template (conditions, review point, dispute resolution) and the get/give per party. It removes the agreement section, the second roster, the odds line and the stage vocabulary in output.

**Edit A: one roster with get/give folded in** (L363, L365 changed):

Old:
```
| Stakeholder | Interest | Power | Support Level |
|-------------|----------|-------|---------------|
| [Name] | [What they want] | [H/M/L] | [Champion/Endorse/Accept/Oppose] |
```
New:
```
| Stakeholder (only those who can block or must act) | What they need | How they could block | What they get / give |
|-------------|----------|-------|---------------|
| [Name] | [Their real need, in plain words] | [Vote, veto, walk-out, quiet non-compliance] | [Gain] / [Concession] |
```

**Edit B: delete the agreement section** (L367–370 removed):
```
## Zones of Agreement
- [Shared goal 1]
- [Shared goal 2]

```
→ (nothing)

**Edit C: delete the second roster** (L379–384 removed):
```
### Value Distribution
| Stakeholder | What They Get | What They Give |
|-------------|---------------|----------------|
| [A] | [Gain] | [Concession] |
| [B] | [Gain] | [Concession] |

```
→ (nothing)

**Edit D: replace the odds line with the V4-7 anchor** (L392–393):

Old:
```
## Confidence: [X]%
[Based on commitment strength and alignment quality]
```
New:
```
## What would change this recommendation
[The fact that would flip it, and the cheapest way to check it first]
```

**Edit E: extend the backstage rule** (L410). Append to the end of the paragraph:
```
The method's stage vocabulary is machinery too: never write "stated position" versus "underlying interest", "zones of agreement", "BATNA" or commitment-level labels; name the specific need instead. Lead with the recommendation and the blockers, describe each party once and only if it can block or must act, add no separate "what everyone agrees on" section, and stop at the last new point with no closing recap.
```

Line count: A 2, B 4, C 6, D 2, E 1, for 15 lines. The method sections (A through N) are untouched.

Expected effect:
- Removes the H7A, K0B and Z0Y agreement-section traces and the V5F/N0D position/interest phrasing (G2).
- Removes the duplicated party roster seen in A5V and M2C, plus non-blocking parties (G1). The rough target is 200–400 fewer words on briefs like 1 and 3.
- Removes the closing-recap pattern behind all three skill ceremony hits.
- Keeps the M2C-style "what would change my recommendation", which is the gain's best V4 driver.

Process notes (repo rules):
- This is a content change, so it needs a pre-registered gauntlet round, or an owner decision disclosed in the README and CHANGELOG.
- It also needs bumps to `metadata.version` (to 2.3.0) and to the plugin version.
- Edit B also removes the only template home for "shared goals". The L91–129 method step still exists for analysis, which is intended.

## 4. Prediction for a fresh pre-registered round (edited vs current vs none, fresh briefs)

- **Rewrite gate, edited vs current: KEEP about 55–60%.** The edit should improve G1, G2 and ceremony against the current skill. KEEP also needs the edited skill to stay ≥ current on *every* guard on both instruments, a key rate ≥ current's, and value ≥ current − 0.25. The trimming could cost a few V2 points (word count and value correlate at +0.49 across cells), but −0.25 is a forgiving bar.
- **Validation gate, edited vs none: VALIDATED about 25%.** The gate needs four things together:
  - G1 and G2 ≥ the no-skill arm on brief-paired means. Any small negative is NOISE, and NOISE becomes NOT VALIDATED after the extension.
  - Ceremony ≤ the no-skill arm. Here auditor variance alone flipped two replies.
  - A value margin ≥ +0.5 that clears its band.
  - Rankings not lost.
  With a true value effect near +0.3 and guards that must be non-negative on every brief, the joint pass rate is low even if the edit works as intended.
- **Main risk.** The value claim, not the guards. The first-batch margin was +0.08, and +0.50 needed a weak no-skill extension batch. A leaner skill that matches the no-skill arm on length may also give up part of its V2/V4 edge. If so, the guards pass and value lands at NOISE, and the round ends NOT VALIDATED again. A secondary risk is auditor instability on closing paragraphs. The same text was scored 0 and then 1 across two audit runs, so a one-hit ceremony difference is close to a coin flip.
