# Follow-up forensic review: adversarial-reasoning (round 9, extended)

Written 2026-10-13, after the round closed. This review does not re-score anything. The verdict (NOT VALIDATED) is final under the pre-registered text. Everything below comes from the files in `evolution/gauntlet-2026-10/adversarial-reasoning/` (scores, scores-pre-ext, keys, audit, raw, SEALED.json) and from `harness/gates.py`. The tested arm `arms/i5/SKILL.md` is byte-identical to the shipped `skills/adversarial-reasoning/SKILL.md` (v2.2.1).

## Bottom line

- **Realness: real, but modest.** The skill makes replies better argued and better calibrated. It does not make them more complete: keys are level.
- **Blockers:** value NOISE is an **instrument artifact**. The band rule penalises positive gains that differ in size from brief to brief, and it is non-monotone: a larger gain on one brief turned PASS into NOISE. G2 NOISE is a **one-point, skill-caused cosmetic trace** (a "Confidence" heading that the template asks for), and the zero-tolerance guard at the score ceiling turned it into a blocker.
- **Skill fix:** fold the template's `## Confidence: [X]%` into the Residual Risk section as plain words (4 lines). An optional second edit addresses the brief-1 length.
- **Gate fix:** a per-brief sign rule for the value claim, plus a small non-inferiority margin on the judge guards.
- **Likelihood that a fresh round validates:** about 15% under the current gate and about 45% with the gate change.

## 1. Is the improvement real?

### Per-brief paired differences (new − none, both judges, 4 runs per arm)

| brief | V1 | V2 | V3 | V4 | G1 | G2 | G3 | value | keys (new / none) |
|---|---|---|---|---|---|---|---|---|---|
| 1 Co-op election | +0.62 | +0.38 | +0.38 | +0.75 | **−0.62** | −0.12 | +0.25 | +0.53 | 0.72 / 0.66 |
| 2 Smart locks | +1.38 | +0.88 | +1.75 | +1.38 | +0.25 | 0.00 | +1.25 | **+1.34** | 1.00 / 0.94 |
| 3 Donation match | +0.25 | +0.25 | +0.50 | +0.12 | +0.62 | 0.00 | +0.62 | +0.28 | 0.84 / 0.91 |

### Evidence that the effect is real

- **Rankings.** The skill won all 6 rankings in the final panel (sign p = 0.031). It also won all 6 in the pre-extension panel, which judged a different 4-reply set per brief. That makes 12 of 12.
- **Permutation test.** Shuffling arm labels within each brief over reply-level value gives a one-sided p of about 0.0002. The observed +0.72 is far outside label noise.
- **Stability across runs.** Every brief is positive in both halves of the data. Runs 1–2 give +0.63, +1.25 and +0.38. Runs 3–4 give +0.44, +1.44 and +0.19.
- **A higher floor.** The lowest-scoring skill reply on any brief has a value of 5.5. The no-skill arm has replies at 4.0 and 4.38. Within-cell SD of reply value is 0.22–0.31 for the skill on every brief, against 0.78 for no-skill on brief 2.

### What the skill replies did better (from judge rationale)

**Brief 2.** All four skill replies got the gate-PIN maths right: about 1 in 900, about 15 hours to a hit. Three of them ranked the gate first or second. Two of the four no-skill replies made reasoning errors:
- L1S (no-skill) scored V3 = 2/2 and G3 = 3/2. J-A wrote: "the gate maths is wrong: it says about 1 hit per 600 days when its own figures (1 in 900, 1,440 guesses a day) give about 1.6 a day. That error leads it to put the gate last."
- O8B (no-skill) scored V3 = 3/3. J-A wrote: "Says airplane mode 'doesn't matter', which misses that the revoked person's phone can be the courier. Its 'about 10 hours' contradicts the 1-per-minute rate."
- The skill replies were credited with the subtle k1 form, that the revoked person can stop their own revocation. N5P: "its headline is the key point: revocation needs the help of the person being revoked." E8H: "the revoked person blocking their own revocation… reinstatement also lags."

**Brief 3.** Skill replies flagged the brief's ambiguous volunteer cap instead of assuming an answer. G2T and V4R scored G3 = 6/6. J-B on G2T: "flags the volunteer-cap ambiguity instead of assuming." The no-skill L7F instead "asserts that the volunteer cap is per charity and then builds on that reading" (G3 4/4).

**Brief 1.**
- C6O was ranked first by J-A, and J-B called it "the most insightful reply". It was the only reply credited with tying the non-voter list to targeted takeovers (k2).
- Z9S was ranked first by J-B as "the tightest reply… honest about the risk that remains".

**Calibration across briefs.** 7 of the 12 skill replies state their confidence in words. None of the 12 no-skill replies do. 7 of 12 skill replies have a residual-risk or "what remains" section, against 0 of 12 no-skill replies. Judges explicitly reward these:
- "stated confidence and named unknowns" (E8H)
- "honest residual risk" (N5P)
- "explicit residual-risk statement and assumptions" (E5F)
- "its confidence breakdown by finding is well calibrated" (F1L)

### What the skill replies did worse

- **Length on brief 1.** The median ratio is 1.34× on brief 1, against 1.15× on brief 2 and 1.00× on brief 3. G1 on brief 1 is −0.62. A3Z (2,261 words) and C6O (2,437 words) scored G1 = 4/3 and 4/3. J-B on A3Z: "too long, with a long tail of extra bullets." Both replies use a "five worst problems" layout with long subsections, which mirrors the template's `## Top 5 Attack Paths [Detailed attack scenarios]`.
- **Invented claims still occur.** C6O scored G3 = 3 from J-B, which called "presumably has an interest in the roof project" an unflagged guess and "usually a few hundred dollars" an invented figure. M3L said "nothing checks the date" although the brief says OCR checks it. E5F said "the charity keeps both" after a refund.
- **Brief-3 k2 (token gifts against the five-donor threshold).** The skill arm scored 0.375 on this key and no-skill scored 0.75. Skill replies framed the threshold as a coordination or collusion prize: V4R scored ✗ for "Five people can agree in a chat…". No-skill replies more often named the zero-minimum-gift trick, for example L7F: "Tiny donations ($5 each) count the same as $500 ones." This is one key with n = 4 per arm, so it is weak evidence. It does suggest that the attack-narrative framing pulls attention away from boundary checks on business rules.

### Verdict on realness

The improvement is real: consistent direction, 12 of 12 rankings, a tight skill-arm floor. It is modest in substance. Keys are level, so the skill does not find more of the planted holes. What it does is:
1. avoid gross reasoning errors,
2. flag ambiguity and assumptions,
3. close with residual risk and a fallback, which drives V4.

Note that brief 2's large figure rests partly on two no-skill blunders. With the lowest reply trimmed from each arm, the gain is still +1.17, so it is not only outliers.

## 2. Blockers

### value: NOISE (margin +0.72, band 1.06). Instrument artifact.

Evidence: the per-brief value gains are +0.53, +1.34 and +0.28. All are positive, and the mean clears the +0.5 bar. The rule in `gates.compare(..., claim=True)` also requires the margin to exceed the band, which is defined as max − min of the per-brief gains.

**(a) Is the spread real?** Yes, it is genuine heterogeneity, not sampling noise.
- The pooled within-cell SD of reply value is 0.40, which gives an SE per brief difference of about 0.28.
- If the true effect were the same on every brief, the expected band from three briefs would be about 0.45 (median). The chance of a band ≥ 1.06 would be about 2% (simulated; Cochran's Q = 7.7 on 2 df).
- The same ordering appears in both run halves.

**Why is brief 2 large?** Its no-skill baseline is fragile.
- The brief carries a quantitative trap (dense valid PINs) and a reasoning trap (sync needs the cooperation of the person being revoked). Both invite confident errors.
- Two of the four no-skill replies made such errors. Every skill reply got them right, and the skill replies ranked feasibility explicitly. The skill tells the model to assess Feasibility for each attack, which plausibly pushes it to actually do the arithmetic.
- The skill's benefit is floor-raising, and brief 2 had the most floor to raise.

**Why is brief 3 small?** The baseline was already strong and steady: no-skill SD 0.20, with W1L scoring 6.0/5.75. The prompt itself ("Where would someone smart attack this…?") already elicits adversarial analysis. The skill arm also had slips (M3L) and lost ground on k2.

**Why the verdict is still an artifact.** The question the gate asks is whether the skill helps on average and is not explained by chance. Heterogeneity in the size of a uniformly positive effect is not evidence against that. The rule is also non-monotone. Holding briefs 1 and 3 fixed:

| brief-2 gain | margin | band | result |
|---|---|---|---|
| +0.80 | 0.54 | 0.52 | PASS |
| +1.00 | 0.60 | 0.72 | NOISE |
| +1.34 (actual) | 0.72 | 1.06 | NOISE |

The pre-extension panel also passed value (diffs +0.69, +0.75, +0.25: margin 0.56 > band 0.50). The extension raised the margin to 0.72 and flipped value to NOISE. Part of that flip is judge-panel context: the same r1–r2 replies, re-judged among 8 instead of 4, moved brief 2's difference from +0.75 to +1.25. For example, J-B rated M3L "strongest calibration" (G3 6) in the 4-reply panel and G3 5 with "errors" in the 8-reply panel. So the band partly measures judge-context shifts, not just effect noise.

A reader would not penalise a skill for helping a lot on one task and somewhat on another.

### guard_judge_G2: NOISE (6.96 vs 7.00). Skill-caused trace, amplified by the instrument.

Evidence: the only G2 deduction in 48 scores is J-B on A3Z (brief-1, skill, r2), scored G2 = 6: "The 'Confidence' heading is a small trace of structure." A3Z ends with `## Confidence` followed by a plain-prose paragraph ("I'm confident on points 1 to 4… verify those two things first"). The auditor found no leaks or ceremony in A3Z.

- **Cause in the skill.** `skills/adversarial-reasoning/SKILL.md` lines 337–338 contain `## Confidence: [X]%` and `- [Justification - coverage, depth, expertise]`. The output template asks for exactly this heading. So the trace is a genuine (tiny) skill defect.
- **Why it blocked.** `compare(margin=-0.042, band=0.125, need=0)` returns NOISE for any deficit that is smaller than the band. With no-skill at the 7.0 ceiling, the skill can only tie or lose. One point of 48 decided it.
- **The rubric contradicts the deduction.** It says "A plain statement of how confident the reply is belongs to G3 and is not leakage". The deduction punishes a heading, not machinery.
- **Pre-extension G2 was the other way round.** The skill led by +0.17. E8H, O8B, P5Z and L7F each took a 6 there, from both arms. G2 here is ceiling noise.

### Non-blocking conditions worth noting

- **Length 1.16× (PASS, cap 2.0).** The ratio comes almost entirely from brief 1 (1.34×). Its cause is the template's "Top 5 Attack Paths [Detailed attack scenarios]" combined with the extra sections the template carries:
  - Edge Cases appears in 3 of 12 skill replies and 0 of 12 no-skill replies.
  - Residual Risk / "what remains" appears in 7 of 12 skill replies and 0 of 12 no-skill replies.
  - Confidence appears in 7 of 12 skill replies and 0 of 12 no-skill replies.

  The residual-risk and confidence material is part of what earns the G3 and V4 gain, so it should stay. The "detailed top 5" layout is what lengthens rich briefs. This is not a blocker now, but G1 was NOISE before the extension (diffs −0.75, −0.25, 0) and is the next guard most likely to trip.
- **G1 PASS (+0.08)** only because briefs 2 and 3 offset brief 1's −0.62.
- **Keys +0.02 (band 0.12).** The key instrument had little headroom. Brief 2 scored 1.00 vs 0.94, and k1, k3 and k4 on brief 3 were hit by nearly every reply. The skill does not raise completeness. Since value is the claim route, this did not block.
- **(c) Is the gain mostly V3 and G3?** Partly confirmed. V3 (+0.87) is the largest single gain, but V1 (+0.75) and V4 (+0.75) are nearly as large, and V2 is +0.50. G3 is +0.71.
  - **V3** is driven by the no-skill arithmetic and logic errors quoted above: L1S, O8B, and F6O's "a third… should be two-thirds".
  - **G3** is driven by flagged ambiguity and stated confidence in the skill arm (G2T, V4R, E8H, F1L), against invented generalisations in the no-skill arm on brief 1 ("many require two-thirds", "often a supermajority") and L7F's unflagged reading on brief 3.
  - **V4** comes from the residual-risk sections and fallbacks: Z9S's "If you can't fix the first three", N5P's timed plan, F1L's interim step.

## 3. Proposed fix

### Skill edit A (recommended): fixes the G2 trace and keeps the calibration gain

This is a 4-line change in `skills/adversarial-reasoning/SKILL.md`, Output Template, lines 334–338.

Old:
```
## Residual Risk
[What risks remain after mitigations]

## Confidence: [X]%
- [Justification - coverage, depth, expertise]
```
New:
```
## Residual Risk
[What risks remain after mitigations, then in plain words (no percentage, no "Confidence" heading): what you took from the brief, what you assumed, and what to check first]
```

The judges rewarded the content (separating known from assumed, and what to verify) and docked the heading. This edit keeps the content and removes the heading and the `[X]%` figure.

### Skill edit B (optional, lower confidence): addresses brief-1 length and G1

This is a 2-line change, lines 325–326.

Old:
```
## Top 5 Attack Paths
[Detailed attack scenarios]
```
New:
```
## Attack Paths, worst first
[As many as change the decision, usually 3 to 5: a short paragraph each on how it works here and the fix; lesser findings one line each]
```

Risk: C6O's top V1 (7/7) came with its length. Cutting depth could cost V1 on rich briefs. Edit A carries no comparable risk. In total, A + B change 6 lines.

Per repo rules, either edit needs a pre-registered gauntlet round (or a disclosed owner decision), a bump to v2.2.2 or v2.3.0, a plugin version bump, and a CHANGELOG entry.

### Gate change (fair and pre-registrable, for the next program or round, not this one)

**Value claim.** Replace "margin > max−min band" with a one-sided per-brief sign rule:
- PASS iff the value margin is ≥ +0.5 and every brief's difference is > 0.
- NOISE iff the margin is ≥ +0.5 but some brief is ≤ 0.
- An alternative is a band built from within-brief run variability (2 × SE of the mean paired difference). That band would have been about 0.33 here, so the margin would PASS.

Risk of passing a skill that doesn't help, from simulation with per-brief SE 0.28:
- Under a true null with brief heterogeneity τ = 0.3, the sign rule passes about 1.5% of the time, against about 0.7% for the band rule.
- Under a small true effect of +0.2, it passes about 9%, against about 5%.

Almost all the protection comes from the +0.5 bar, not from the band. The real residual risk is not chance. It is judge-pleasing surface features: confidence statements and residual-risk sections lift G3 and V4 without more keys found. The rankings condition and an unchanged key instrument do not guard against that. Keep the key-rate report, and consider requiring "keys not worse" alongside a value claim.

**Judge guards.** Replace "any deficit within band = NOISE" with a non-inferiority margin: FAIL if the deficit is beyond −0.25, PASS otherwise. This tolerates a single ceiling-level point like the G2 here. The risk is admitting real but small leakage. The auditor's ceremony and leak counts, which stay zero-tolerance, still cover that.

## 4. Prediction for a fresh pre-registered round (fresh briefs)

**Assumptions.** I shrink the observed true gain to about +0.55–0.65 to allow for the winner's curse, with between-brief τ ≈ 0.3–0.5. The pre-extension panel's +0.56 is consistent with this.

- **Current gate, current skill: about 12%.**
  - The value band rule passes only about 25–38%.
  - G1 is about 60% (it was NOISE before the extension here).
  - G2 at ceiling is about 60%.
- **Current gate, with edit A (+B): about 15–18%.** G2 rises to about 70%, and G1 to about 65% with B. The value band rule remains the binding constraint.
- **Gate change (sign rule plus guard non-inferiority), with edit A: about 45%, range 35–55%.** The value condition passes about 50–65% and the guards about 85–90%.
- **Main risk: brief mix.** The skill's benefit is floor-raising: it prevents confident blunders and adds calibration. Fresh briefs whose baseline is already strong (like brief 3, or prompts that already ask "where would someone smart attack") could push one brief to ≤ 0 or the mean below +0.5. A secondary risk is G1 on long, multi-surface briefs (like brief 1).
