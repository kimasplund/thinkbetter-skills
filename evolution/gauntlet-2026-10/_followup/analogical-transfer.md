# Follow-up: analogical-transfer, post-hoc forensic review

Written 2026-10-13, after the round closed. This is not a re-score: the verdict (NOT VALIDATED) is final under the pre-registered gate. This note asks three things. Is the gain real? What exactly blocked validation? What is the smallest edit that removes a genuine defect?

Sources: `evolution/gauntlet-2026-10/analogical-transfer/` (PRE-REGISTRATION.md, scorecard.md, verdict.json, SEALED.json, scores/, audit/audit.json, keys/, raw/, pack/), `harness/rubric.md` and `harness/gates.py`. The tested text `arms/u1/SKILL.md` is byte-identical to the shipped `skills/analogical-transfer/SKILL.md` (v2.2.1), so the line numbers below apply to both.

Arms: u1 = new (skill), b8 = none. Blind codes:

| brief | skill r1 / r2 | none r1 / r2 |
|---|---|---|
| 1 (theatre membership vs gym) | D9X / N7Z | B6S / K8K |
| 2 (ochre wilt vs firebreak) | E3H / H4J | L7J / Y1U |
| 3 (hardship fund vs sick club) | G2G / T0U | K9A / F2O |

## 1. Is the improvement real?

**Verdict: real in direction. The size is soft.**

I recomputed the brief-paired differences (skill minus none) from the judges' score blocks:

| brief | V1 | V2 | V3 | V4 | value | G1 | G2 | G3 |
|---|---|---|---|---|---|---|---|---|
| 1 | +0.50 | +0.25 | +1.00 | +1.00 | **+0.69** | −0.25 | −1.00 | +0.75 |
| 2 | +0.75 | +0.25 | +0.50 | +0.75 | **+0.56** | −0.25 | −1.00 | +1.25 |
| 3 | +1.00 | +0.50 | +1.00 | +0.50 | **+0.75** | −0.25 | 0.00 | −0.25 |

The evidence for a real gain:
- **Value is positive on every brief and every value dimension.** No per-brief value difference is below +0.25.
- **Rankings went 6–0.** A skill reply ranked first in all six judge × brief rankings (N7Z twice, H4J once, E3H once, T0U twice), and the sign test gives p = 0.031. In 5 of the 6 rankings both skill replies sit in the top two; the exception is J-B on brief 1, where D9X placed third behind K8K.
- **Judge agreement was 0.99.** Both Opus judges saw only blinded copies.
- **Keys reached the ceiling** (1.00 vs 0.94). The whole key margin comes from one key, brief-1 k3: free bookings no-show at 14%, so members will book speculatively. Both skill replies caught it and proposed a control. D9X wrote "Add a late-cancellation rule, because your no-show rate on free tickets is 14%", and N7Z wrote "Release unclaimed member seats a couple of hours before curtain, and give a strike or fee". B6S only noted the 14% (~), and K8K missed it ("paid member seats will behave far better", ✗). Briefs 2 and 3 were at the ceiling in both arms, so keys add little evidence.

Concrete things the skill replies did better, as named in the judges' rationales:
- **Brief 1, N7Z** (ranked first by both judges). It computes the break-even visit count (5.3), the revenue at risk (about €540k, 18% of box office) and the roughly 3,000 new members needed to offset it. It states its reading of "issued at" as an assumption that decides the design, notes that a negotiated per-performance allocation could remove the comp cap, keeps the pilot inside the cap, and ends with a pre-agreed decision rule. D9X points out that midweek face values may sit below the €34 average.
- **Brief 2, H4J.** It sets graded sampling distances (100 m to 3 km), notes that routine felling in the surrounding woods also creates breeding material, explains why a short delay costs little, and assigns roles to Ruairi and the lab. **E3H** reframes the problem as a spot fire, which judge J-B called "the strongest framing". That gives the manager a way to talk to Ruairi, and it makes approval on 1 December conditional on a wood-handling plan.
- **Brief 3, T0U.** It uses the hiring hall as a better structural analogue than the sick club, which ties eligibility to the desk's own records. It shows that Halcyra needs a drop of more than 40% before the trigger fires at all, says payouts must be excluded from the trailing average, and flags the conflict of desk members judging claims. **G2G** makes "the sharpest insight": members who left probably had months at 65 to 80%, so a 60% cliff would never have paid them.
- **Calibration (G3 +0.58).** The skill replies end with honest limits sections: "I haven't verified the details of individual cinema or museum schemes, so treat them as pointers" (N7Z), and "I am recalling these from general knowledge, so ask the plant-health lab" (H4J). The no-skill replies made more unflagged claims: Y1U lumps ash dieback in with the beetle-borne diseases and states analogue outcomes without hedging, and L7J asserts "a poor record" without support.

Where the gain plausibly comes from in the skill text: the disanalogy check (lines 234–238), "Unmapped Elements" (line 159), "the unmapped elements are the important ones" (line 281), and the instruction to seek deep structural rather than surface parallels (lines 266–276). These match the kind of wins above: better structural analogues (hiring hall, spot fire, airline buckets) and the points where the user's analogy breaks. The closing confidence slot (lines 392–393) plausibly drives the G3 gain.

What was worse or no better:
- **Length.** Skill replies were 16% longer (median word ratio 1.18, 1.23 and 1.06 by brief).
- **Padding.** H4J scored G1 4/4, and both judges named the cholera and malaria analogies and the "thousand kilometres" line as padding.
- **Visible method.** N7Z has a "stripped of theatre" abstraction section, which cost G2 5/5. E3H has a "What carries over" mapping column, scored G2 5 by J-B.
- **Errors in the skill arm.** D9X contradicts itself: it caps seats below the comp cap while pricing credits to avoid comp status, then projects about 13,000 admissions (V3 4/4). This is the same class of error as B6S and K8K in the no-skill arm. G2G makes two unflagged leaps (G3 4 from J-B), and E3H has small inventions ("valley", a date slip).

**Why "soft" on size:** there are 2 runs × 3 briefs per arm. Much of the V3 margin (+0.83) comes from the no-skill arm's arithmetic or pricing slips (B6S, K8K and K9A each scored V3 4/4). D9X shows the skill arm is not immune. On fresh briefs I expect the value margin to shrink towards +0.4 to +0.6, which is near the +0.5 bar. Also, the no-skill baseline is strong (value 5.33), because every brief explicitly asks "what else is this like". The skill's gain is incremental depth, not a different kind of answer.

## 2. Blockers

### guard_audit_ceremony: FAIL (skill 0.67 hits per reply vs 0.00; band 1/6)

Evidence (audit/audit.json):

| reply | quoted hit | rule clause | traced to SKILL.md | classification |
|---|---|---|---|---|
| N7Z | heading "What the problem is, stripped of theatre" | "a section that restates the question"; "a heading … that describes the method" | The B step (lines 44–70: "Describe the problem in abstract, domain-neutral terms", with a `## Base Problem` template) and the output-template slot `## Problem Abstraction` / `[Domain-neutral core challenge]` (lines 369–370) | **Skill defect, clear.** It is the method's first step shown as a reply section. |
| N7Z | "You have a perishable inventory of 130,000 seats a year" | the body of the same section | same | **Instrument inflation.** One section is counted twice (its heading and its first sentence). |
| H4J | H1 title "# Is a fire-style firebreak right for ochre wilt?" | restates the question | The output template opens with `# Analogical Analysis: [Problem]` (line 367) | **Skill defect, low reader cost.** The template asks for a problem title, and the executor obliged. A reader would barely mind, but it is within the rule's letter. |
| T0U | "The sick-club comparison is sound in spirit (…), but it breaks on verification, participation and correlation" | "a summary that repeats earlier sections without adding information" | The closing template slot `## Confidence: [X]%` / `[Based on analogy strength and mapping completeness]` (lines 392–393) invites a final re-judgement of the analogy | **Mild skill defect, partly rule-application noise.** It repeats the opening section's three conditions. But the no-skill reply B6S ends with a similar recap ("Overall, Maren's instinct … A capped Tuesday to Thursday membership delivers it …") that was not flagged. |

The FAIL is robust to every reading. Under `gates.py` `_audit`, the margin must be within strictly less than one hit, so a difference of exactly one hit already fails. N7Z's section alone would fail the gate. Counting it once gives 3 hits (0.50 per reply), which still fails.

**Why the Backstage rule (line 398) did not stop it:** that rule bans method names, narration, scores and checkpoint talk. It says nothing about the method's *steps* turning into content-like sections: abstracting the problem, a title that restates it, re-judging the analogy at the end. Meanwhile the "Output Template" block (lines 364–394), which an executor told to apply "the skill exactly" reads as the reply's shape, explicitly asks for a title, a problem abstraction and a confidence section judged on analogy strength. The two instructions conflict, and the template wins on some runs (2 of the 6 main replies had a step-section; 3 of 6 had any hit).

### guard_judge_G1 (proportionality): FAIL (margin −0.25, band 0.00)

Evidence: the per-brief differences are −0.25, −0.25 and −0.25. Each brief has 4 G1 scores per arm (2 replies × 2 judges), so −0.25 is a one-point difference in total, the smallest non-zero difference possible. Three identical differences give a band of max − min = 0, so `compare()` turns any negative margin into FAIL.

Where the single points came from:
- **Brief 1:** every skill score was 5. The no-skill reply K8K got a 6 from J-B, a reward for compactness.
- **Brief 2:** H4J got 4/4 ("It is long, with some padding (cholera, malaria)"), and E3H got 6/5. The no-skill L7J got 5/4 ("somewhat long") and Y1U 6/5.
- **Brief 3:** every skill score was 5. The no-skill F2O got 6/6 ("compact"), and K9A 5/4 ("the longest reply").

Classification: **mostly an instrument artifact, with a small real component.**
- The artifact: a band of zero from identical integer-step differences means the gate cannot tell a one-point wobble from a real deficit. Under a one-point tolerance (the logic the auditor guard uses), G1 would read NOISE.
- The real part: skill replies are 16% longer, and H4J's padding is a skill effect. The method generates 5–10 candidates and investigates 3–5 (lines 110–113, 130, 338–339). The template's `## Analogies Investigated` list (lines 372–375) and nothing in the skill tells the writer to drop analogies that did not change the recommendation. In briefs 1 and 3 the skill replies were not marked down; the no-skill arm simply drew a 6.

### guard_judge_G2 (machinery leakage): NOISE (skill 6.17 vs 6.83; margin −0.67, band 1.0)

Evidence:
- **N7Z, 5/5.** J-A called the "stripped of theatre" framing section "a faint trace of method", and J-B "a trace of method".
- **E3H, 5 from J-B.** "The table's 'What carries over' column shows a little of the analogy-mapping machinery." N7Z also uses "What carries over:" as a repeated bullet label.
- **D9X and H4J, 6/6.** No explicit reason was given.

Classification: **a mild skill defect, with the size inside small-sample noise.**
- The source is the same as the ceremony hits: the abstraction step, plus the mapping vocabulary from the structural-mapping template (lines 134–144) and "Require structural mapping table" (line 336), leaking into reply labels.
- Brief 3 shows no difference at all (all 7s).

### Not blockers

- **Leaks: 0 vs 0.** The Backstage rule works for names and scores.
- **Length ratio 1.16, under the 2.0 cap.**
- **Negative fixture.** The skill reply was 24 words against 29 for no skill, with no ceremony.
- **Framing invariance holds.** Both framing replies recommend a Tuesday-to-Thursday pass priced at or above half of face value, plus a pilot.

## 3. Proposed fix (minimal; the method is unchanged)

Diagnosis: the BRIDGE method (lines 42–262) and the quality heuristics (264–282) are what produce the gain. The defects come from two places:
1. The **Output Template** (lines 364–394) asks for a problem title, a "Problem Abstraction" section and an analogy-strength confidence close.
2. The **Backstage rule** (line 398) covers names and scores but not displayed steps.

The fix leaves the method untouched. It changes the template's opening and closing slots and adds one sentence to the Backstage rule. That is about 11 changed lines.

**Edit 1: template opening (lines 364–370).**

Old:
````
## Output Template

```markdown
# Analogical Analysis: [Problem]

## Problem Abstraction
[Domain-neutral core challenge]

## Analogies Investigated
````

New:
````
## Output Template

Work the steps above in your notes. The reply delivers only their results, under headings in the user's own terms, and opens with the answer, not with a title or a restatement of the problem.

```markdown
**Short answer:** [Verdict on the user's analogy or plan, and what to do instead]

## Analogies Investigated
````

**Edit 2: template close (lines 392–393).**

Old:
```
## Confidence: [X]%
[Based on analogy strength and mapping completeness]
```

New:
```
## Where I could be wrong
[Only what is new: assumptions that decide the design, analogue facts recalled rather than checked, and what would change the answer. No recap of earlier sections.]
```

**Edit 3: Backstage rule (insert a new paragraph after line 398).**

New:
```

The method's own steps stay backstage too: no section restating the problem in abstract or domain-neutral terms, no title that repeats the user's question, no closing recap of points already made, no mapping labels such as "what carries over" (say what the user should do instead), and only the analogies that change the recommendation.
```

What each edit targets, and what it keeps:

| defect | evidence | edit |
|---|---|---|
| Abstraction step shown as a section | N7Z (ceremony ×2, G2 5/5) | 1 (removes the `Problem Abstraction` slot) and 3 |
| Title restating the question | H4J (ceremony) | 1 (removes the `# Analogical Analysis` title, opens with the answer) and 3 |
| Closing recap that re-judges the analogy | T0U (ceremony) | 2 (no recap) and 3 |
| Mapping vocabulary in reply labels | E3H, N7Z (G2) | 3 |
| Padding from surplus analogies | H4J (G1 4/4) | 3 ("only the analogies that change the recommendation") |

What is kept:
- The method body (B step, mapping tables, disanalogy check, heuristics) is untouched, so the analysis that found the hiring hall, the spot fire and the comp-cap logic still runs.
- The calibration content that drove G3 stays. Edit 2 keeps a "Where I could be wrong" section and narrows it to new information: unverified analogues and the assumptions that decide the design. Those are exactly the lines judges praised in N7Z and H4J.
- The **Short answer** opening matches what the best replies in both arms already did, so it should not cost V4.

Process, per the repo rules (not done here):
- Ship this only through a pre-registered `skill-gauntlet` round.
- Bump `metadata.version` (2.2.1 → 2.3.0), bump the plugin `version` in `.claude-plugin/plugin.json`, and add a CHANGELOG entry.

## 4. Prediction for a fresh pre-registered round

Setup: edited (E) vs current v2.2.1 (C) vs none (N), on fresh briefs.

- **E vs C (rewrite-style KEEP): about 65%.**
  - E should beat C on ceremony and G2, because the ceremony came from template slots that no longer exist.
  - G1 should be equal or slightly better.
  - The value tolerance (≥ C − 0.25) is lenient.
- **E vs N (validation): about 30% VALIDATED in the first round.** Roughly another 15% would come out INCONCLUSIVE and need the extension. Every one of the following has to hold at once:
  - **Zero ceremony hits across 6 replies.** One hit fails, because the no-skill arm sat at 0. Even a clean skill keeps some risk here from auditor variance: compare the T0U flag with the unflagged B6S recap.
  - **G1 paired margin ≥ 0 with a likely zero-width band.** E may still be about 10% longer, since a "Where I could be wrong" section remains.
  - **G2 near 7.** The no-skill arm scored 6.83, so any single 6 makes the margin negative. It would most likely read NOISE, which means INCONCLUSIVE and the extension.
  - **Value ≥ +0.5 beyond its band on fresh briefs.** I estimate about 60%, given the soft size noted in §1.

**Main risk:** two strict gates. The ceremony guard fails on a single hit, and a zero-band integer G1 fails on any one-point wobble. Neither depends on whether the edit works, so a clean edit can still fail by chance. The secondary risk is that hiding the machinery also trims what produced the gain: the abstraction step written out may have helped N7Z, the best reply, reason. If the value margin falls below +0.5, the round fails on value even with clean guards.

**Suggestions for the next pre-registration** (they apply only to future rounds; this round's verdict stands):
- Count one ceremony hit per section rather than per quote.
- Give G1 and G2 a minimum band of one score point per brief, the same tolerance the auditor guard already has.
- Pre-register both readings so neither can be chosen after the results.
