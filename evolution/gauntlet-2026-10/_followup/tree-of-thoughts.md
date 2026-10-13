# Follow-up forensic review: tree-of-thoughts (gauntlet 2026-10, round 4)

Written 2026-10-13. This is a post-hoc review and nothing in it is binding. The round's verdicts (validation NOT VALIDATED, rewrite REVERT) stand as recorded. No round file was changed.

Arm codes (SEALED.json): `i1` = new (1.1.0), `i3` = old (v1.0.0 body, which is what ships now as 2.3.1), `j3` = none. The shipped `skills/tree-of-thoughts/SKILL.md` body and `references/` are byte-identical to `arms/i3/`. Only the frontmatter differs.

## Headline

1. **The only ceremony hit the old arm was charged with is not in an old-arm reply.** The auditor credited the quote "Hollis is the only option on the list with a fixed deadline" to R7C (brief-3, old, r1). That sentence does not appear in R7C. It appears verbatim only in **S9M** (brief-3, *new*, r1), line 37. The auditor's brief-3 output is shifted by one slot. Its S9M entry ("Don't sign the 18 t Alto Merida deal.") is in fact **Q7L** (brief-3, *none*, r1), line 55. The S0O quote (brief-1, new) is attributed correctly.
2. Once each quote is credited to the file it comes from, the counts are **old 0/6, new 2/6, none 1/6**. For old vs none, the ceremony guard goes from FAIL to **PASS**. The recorded verdicts for the new arm do not change: new vs none is 2 vs 1, still exactly one hit and so still FAIL under the strict rule, and the negative fixture FAILs anyway. New vs old is 2 vs 0, still FAIL.
3. **The improvement is real.** Each of the 6 old-arm replies outscored each of the 6 no-skill replies on value. The gain is not in planted keys, which are at ceiling for both arms. It is in reasoning soundness, decision usefulness and calibration.
4. **G1 is the real long-run obstacle.** The deficit is explained entirely by length: old replies are about 21% longer. With length held constant, the old arm is no less proportional. Part of that extra length, though, is restatement that comes from the skill's synthesis template. A small edit targeted at that is proposed below.

## 1. Is the improvement real? Yes.

### Numbers (old vs none, brief-paired, recomputed from scores/*.md)

| dim | brief-1 | brief-2 | brief-3 | margin | band |
|---|---|---|---|---|---|
| V1 insight | +1.00 | +1.00 | +1.25 | +1.08 | 0.25 |
| V2 specificity | +1.00 | +1.00 | +0.50 | +0.83 | 0.50 |
| V3 soundness | +1.00 | +1.50 | +1.25 | **+1.25** | 0.50 |
| V4 decision use | +1.25 | +1.00 | +1.00 | +1.08 | 0.25 |
| value (V1–V4) | +1.06 | +1.12 | +1.00 | **+1.06** | 0.12 |
| G1 proportionality | +0.25 | −1.00 | −0.25 | −0.33 | 1.25 |
| G2 leakage | 0 | 0 | 0 | 0 | 0 |
| G3 calibration | +1.00 | +1.25 | +0.50 | +0.92 | 0.75 |

Per-reply value (mean of both judges):

- old: O4M 6.50, F4Z 6.38, Y1Z 6.25, R7C 6.25, O0W 6.13, G5X 6.00
- none: Q7L 5.88, G9R 5.50, R4T 5.00, W9C 5.00, R5H 5.00, R0F 4.75

The two arms separate completely: the weakest old reply (6.00) beats the strongest no-skill reply (5.88). An exact Mann-Whitney test gives p ≈ 0.002, treating replies as independent. Both judges put both old replies above both no-skill replies in all 6 rankings, so rankings are 6–0.

**Keys do not discriminate.** Old caught 24/24 keys. None caught 23.5/24; the half point lost is R4T's k4, the token conflict, marked "~". Every planted key was found by nearly every reply, so this pack cannot show a key-detection gain. The whole measured gain is in judge-scored quality.

**Length confound.** Across all 18 main replies, value correlates with word count at r = +0.72, and G1 with word count at r = −0.69. I fitted an OLS on the 12 old and no-skill replies: value = 4.02 + **0.82**·old + 0.13·(words/100). So about +0.82 of the +1.06 survives a length control. At matched length the skill still wins, for example:

| reply | arm | words | value |
|---|---|---|---|
| F4Z | old | 1,056 | 6.38 |
| Q7L | none | 1,056 | 5.88 |
| O4M | old | 1,005 | 6.50 |
| G9R | none | 1,032 | 5.50 |
| Y1Z | old | 952 | 6.25 |
| W9C | none | 848 | 5.00 |
| R5H | none | 863 | 5.00 |

### What the skill replies did better (judge rationale)

- **Brief 1 (offline mode).**
  - O4M ranked first with both judges. It says to freeze scope because any later fix costs another 8-week review. It names the security team's answer on offline use after token expiry as the first check, because a "no" there breaks every option. Its next steps are ordered with dates.
  - O0W flags that rework after review feedback can wipe out the slack. It notes that the team's 2-week estimate may leave out the token and stock work, and it asks whether a review-free server-side path exists, which would change the answer.
  - On the no-skill side, G9R has a slip that J-B caught: "3+ weeks build plus 8 weeks review reaches or passes 11". R4T is thin, with no handling of conflicts or reassigned jobs and only partial k4.
- **Brief 2 (ski area).**
  - Y1Z ranked first with both judges. It gives a fallback tree keyed to the Trust's answer, notes that a buyer would inherit the same lease limits, and flags its assumption about the beginner guns.
  - G5X reads the 2025 renewal on unchanged terms as a sign the Trust may resist. It asks whether the 15 years is measured at application or at award, gives the 2041 target and splits its confidence.
  - On the no-skill side, R5H gets the lease term wrong ("about 8 years remain", V3 = 4) and makes an unsupported call for a "larger water source". J-B says W9C is weak on what would change the advice and misses that snowmaking on owned land is grant-eligible.
- **Brief 3 (roaster).**
  - F4Z: growth under the cap has to come from margin per kilo. A 4–6 t second blend fits the current machine without spending £68k. Alto Merida can grow only about 5% until 2028, and Varnland is not caught by the café clause. It has an explicit "what would change this" section.
  - R7C: the cap is the real ceiling. It notes that Hollis may prefer its own blend, lists ways to get a café waiver, flags the 40% concentration risk, says to rerun the "double profit" claim and plans the 2028 renegotiation.
  - On the no-skill side, R0F gets V3 = 4: "6–8 t could fit under the cap", the 15 kg roaster "doesn't remove the lease-hours limit", and it ranks the café clause above the cap. J-A notes that Q7L says little on what would change the advice and that its bottom line repeats earlier points.

**Where the gain comes from.** The skill's Step-5 synthesis template asks for alternatives considered with a reason for each prune, a confidence with its justification, and remaining uncertainties. The backstage rule turns these into content sections: "Where this could be wrong", "What would change this advice", "Fallbacks", "What I'm unsure about", "Confidence: high that… moderate that…". These map directly onto the rubric's top anchors for V4 ("what would change it, cheapest way to reduce uncertainty") and V3/G3 ("strongest counter-case", "flags where it could be wrong"). Step 4's push to deepen the winning option shows up as more design detail on the chosen option: event fields, the stale-job rule, the second-blend tonnage.

### What was worse

- **Length.** Old is 1.21× the no-skill median (brief medians 979 vs 841, 1,051 vs 856, 1,138 vs 927 words).
- **Restatement.** J-B on G5X: "long and somewhat repetitive". J-A on G5X and R7C: "a little long". J-B on R7C: "slightly long". In G5X, all five options are analysed one by one and then walked through again under "Recommended direction". In R7C, Hollis and the contract roaster are covered under "Why the deal doesn't work", again under "What I'd do", and a third time in the growth table, and "The three-year shape" re-lists the December steps.
- **Small unflagged leaps in skill replies too.** G5X's 71,500 m³ assumes the beginner area is separate from the 9 ha. R7C says "retail earns far more per kilo" without support. F4Z uses the muddled phrase "Saturday-free scheduling". O0W's "lose a week and you miss the season" overstates the risk.

**Verdict on realness: real.** The direction is robust: complete separation and 6–0 rankings. The size is probably about +0.8 rather than +1.06 once length is accounted for.

Caveats:
- n = 6 vs 6.
- The two Opus judges agree at 0.99, so in practice they act as one instrument.
- Judges scored all six replies side by side.
- All executors were Sonnet.
- The keys were at ceiling, so key detection gives no independent confirmation.

## 2. Blockers (old vs none, post-hoc application of the validation gate)

| condition | as recorded | evidence | classification |
|---|---|---|---|
| guard_audit_ceremony | FAIL (old 1/6 vs none 0/6; exactly one hit is not "less than one hit") | `audit.json` R7C: "Hollis is the only option on the list with a fixed deadline". The text is in **S9M** line 37 (new arm): "Hollis is the only option on the list with a fixed deadline and a large sum of money behind it, so it deserves the effort." `grep` finds it in no other file. R7C (`raw/brief-3--i3--r1.md`, identical to `blind/R7C.md`) contains no such sentence. | **Instrument error (mis-attribution), not a skill defect.** Corrected: old 0, none 1 (Q7L's "Bottom line"). **PASS.** |
| guard_judge_G1 | NOISE (margin −0.33, band 1.25) | Paired diffs +0.25 / −1.00 / −0.25. Brief 2 drives it: G5X G1 = 5/4 at 1,150 words vs W9C and R5H at 6/6 with about 850 words. OLS: G1 = 8.50 + **0.26**·old − 0.32·(words/100), so with length held constant old is slightly *more* proportional. | **Mostly small-sample noise plus the rubric's length penalty**, with a **minor real component**: about 100–200 words of restatement in the longer old replies, traceable to the synthesis template (below). |

All other conditions PASS for old vs none:
- G2: 7.00 vs 7.00.
- G3: +0.92.
- Leaks: 0 vs 0.
- Length: 1.21 against the 2.0 cap.
- Value: +1.06 against a band of 0.12.
- Rankings: 6–0.
- Negative fixture: 42 words vs 43, no ceremony.
- Framing: invariant.
- Agreement: 0.99.

**Corrected post-hoc reading for old vs none:** every condition PASSes except G1, which is NOISE. That makes the reading INCONCLUSIVE, where the recorded one was NOT VALIDATED.

### Other findings from the same check

- I checked every key-verifier quote against the blinded file it was credited to. All match: the only differences are paraphrase or capitalisation (O4M k2, Q7L k1) and one quote that appears in two files (G9R k2). The mis-keying affects the auditor only.
- `research-note.md` is wrong on two points. It says old had "1 ceremony hit"; it had 0. It also cites "Don't sign the 18 t Alto Merida deal." as a 1.1.0 quote, but that sentence is from the no-skill reply Q7L.
- Did the three genuine hits come from the skill? The correctly attributed hits are S0O's closing confidence recap, S9M's "Why this order" recap and Q7L's "Bottom line" recap. All three are **closing recaps**, and one is from the no-skill arm. This auditor's ceremony trigger, in practice, is a closing paragraph that repeats the reasons already given. One old reply carries the same pattern: G5X's final "Confidence:" paragraph restates the snowmaking and lease findings. It was not flagged this time, but it is the most likely source of an old-arm hit in the next round.

## 3. Fix

**The evidence shows no ceremony defect.** The old body produced no correctly attributed ceremony hit, no leaks and a clean negative fixture.

**There is one minor real defect: restatement that inflates length.** It is the only thing standing between the shipped skill and the binding G1 guard (S ≥ N). The cause is in `skills/tree-of-thoughts/SKILL.md`:

- **Lines 203–234, the Synthesis Template.** Separate "Key Insights" (one per level), "Alternatives Considered", "Final Confidence + Justification", "Recommendation" and "Remaining Uncertainties" blocks each revisit the same facts. Under the backstage rule the executor turns each block into a user-facing section, so the options get covered twice (G5X, R7C) and the confidence paragraph repeats the findings (G5X).
- **Line 236**, "Comprehensive synthesis…", and **line 387**, "The goal is high-confidence optimal solutions, not quick answers.", push toward length in the user-facing answer.

**Minimal edit** (2 lines changed, 1 paragraph of 3 lines added; method untouched).

Line 236, old:
```
**Deliverable**: Comprehensive synthesis with traced path and confidence score
```
Line 236, new:
```
**Deliverable**: Synthesis with traced path and confidence score. This template is your working record; the user-facing answer follows the answer-shape rule at the end.
```

Line 387, old:
```
**Remember**: Quality over speed. ToT trades time for rigor. The goal is high-confidence optimal solutions, not quick answers.
```
Line 387, new:
```
**Remember**: Quality over speed in the thinking, not in the answer. ToT trades time for rigor; the reply itself stays as short as the decision allows.
```

Append after line 391, as a new paragraph that ends the Backstage rule section:
```

**Answer shape.** Lead with the recommendation. Give each rejected option its deciding reason once, and don't walk through the rejected options again in the plan. Then give the steps for the chosen option. End with the assumptions that matter, what would change the recommendation, and the cheapest check for each. Say each fact once: no closing summary or bottom line that repeats earlier sections. If you state confidence, use one sentence that names the deciding unknown rather than restating the reasons.
```

**Why it keeps the gain:**
- It keeps, and makes explicit, the sections that drove V4, V3 and G3: assumptions, what would change it, cheapest check, and a deciding reason for each pruned option.
- It removes only the second and third passes over the same facts, and the recap-style confidence paragraph that matches this auditor's trigger.
- The internal method (5+ branches, scoring, recursion) is unchanged.

**Expected effect:**
- Roughly 10–15% shorter replies.
- G1 up about 0.3–0.5 at the measured slope of −0.32 per 100 words.
- Value down perhaps 0.1–0.2 at the measured slope of +0.13 per 100 words. That leaves the margin around +0.8, well above the +0.5 bar.

**Process:**
- Under the repo rules this is a content change. It needs a pre-registered round, a `metadata.version` bump, a `plugin.json` bump and a CHANGELOG entry.
- The 2-arm round below would serve as that round.

## 4. Prediction for a fresh pre-registered 2-arm round (shipped skill vs none, fresh briefs, same gate)

I ran a rough Monte Carlo with per-reply noise taken from this round, the one permitted extension, and the auditor's hit rate of about 0.1 per reply. The estimates:

- **Shipped as-is: about 10–15% VALIDATED.**
- **With the edit, if it closes most of the length gap: about 25–35%.**

The edit roughly doubles the odds, but the round is unlikely to pass even then.

Condition by condition:

- **Value and rankings:** above 90% PASS in either case.
- **G1 (main risk).** The guard is "S ≥ N" with no tolerance, and NOISE resolves to NOT VALIDATED after one extension. With the skill about 0.3 behind on G1, it ends NOT VALIDATED about 55% of the time. Even with no true difference, a near-zero margin falls on the wrong side often enough that about 20–25% of runs still end there. The edit attacks the only lever the skill controls here: length.
- **Auditor ceremony (second risk).** One extra hit is a decisive mechanical FAIL with no extension. This round showed the auditor both mis-attributes quotes and flags ordinary bottom-line sentences. Even at equal true rates, about 15–20% of rounds fail on this alone.
- **Negative fixture (about 10% risk).** It is hair-trigger (1.5× of a ~40-word reply), though the old body passed this time with 42 words vs 43.
- **Framing (about 5–8% risk).**

These are recommendations for the program owner. They do not change any closed round. To count for a future round, they must be pre-registered and frozen before it runs.

- Add a mechanical check that every auditor quote is a substring of the reply it is credited to, and re-run the auditor on any mismatch. This round's ceremony result for the old arm is wrong because no such check exists.
- Consider whether "S ≥ N" guards with NOISE → NOT VALIDATED are intended to fail skills that tie on a guard. As written, an exact tie on G1 has roughly even odds of blocking validation.
