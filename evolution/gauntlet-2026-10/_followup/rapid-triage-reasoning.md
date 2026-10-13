# Follow-up forensic review: rapid-triage-reasoning (round 12)

Written 2026-10-13, after the round closed. This review does not re-score anything. The verdict (NOT VALIDATED) stands.
Arms: b0 = new (the skill, identical to the shipped `skills/rapid-triage-reasoning/SKILL.md`, v2.2.1; `diff` is clean), b2 = none.

## 1. Is the improvement real?

**Verdict: real but modest.** It is uniform in direction and small in size, and much of the margin comes from the skill raising the floor.

Per-brief arithmetic, recomputed from `scores/` (value = mean of V1–V4, both judges, both runs):

| brief | value new | value none | diff | V3 diff | G3 diff | G1 diff | keys new / none |
|---|---|---|---|---|---|---|---|
| 1 theatre | 6.06 | 5.19 | +0.88 | +1.00 | +0.25 | −0.75 | 0.69 / 0.75 |
| 2 ransomware | 5.69 | 5.50 | +0.19 | +0.75 | +1.25 | +0.25 | 0.94 / 0.94 |
| 3 dairy | 5.94 | 5.06 | +0.88 | +1.00 | +0.75 | −0.75 | 1.00 / 1.00 |

- **Direction is consistent.** Value, V3 and G3 are positive on every brief. The skill won all 6 forced rankings (sign p = 0.031).
- **Size is modest, and it comes from the no-skill floor.** In every brief one no-skill reply came last for both judges: F8O, R0P and R2Q. The other no-skill reply beat one of the skill replies in 3 of the 6 rankings: J-B brief-1 S3K over M9W, J-A brief-2 M1N over P1V, and J-B brief-2 M1N over L4K. So half the wins are 1st+3rd against 2nd+4th. A skill reply ranked first in all 6 rankings, and on brief-3 both skill replies took 1st and 2nd for both judges. So the skill reliably avoids the weak reply and usually produces the best one, but the margin over a good no-skill reply is small, and on brief-2 it is close to nil.
- **Keys are flat (−0.02).** Briefs 2 and 3 sit at the ceiling for both arms (0.94/0.94, 1.0/1.0), so the key instrument couldn't discriminate there. On brief-1 the skill was slightly worse.

**What the skill replies did better (from judge rationale):**
- *Brief-1:* O6L made the lift the go/no-go at 18:30, while cancelling is still cheap, and put a hard stop before doors. It got the curfew arithmetic right (latest start 20:15, aim for 20:00). J-B called it "the best structure of gates". Compare F8O (no-skill), which defers the lift and restaging decision to 19:30–19:40 and claims cancelling at 19:30 "still leaves audiences about an hour's notice" (doors are at 19:00: V3 4/3). M9W made the sharp point that Signe "will say yes" and drafted the audience message.
- *Brief-2:* L4K worked the Kelpie headroom (1.84 TB used, 160 GB free, 380 GB to re-upload), asked Kelpie to hold trimming, and noticed Wednesday's work is missing from the NAS copy. Calibration is the biggest gap (G3 +1.25). R0P (no-skill) opens with "you have good backups" and scripts "our backups look intact", neither of which the brief supports (J-B G3 = 3).
- *Brief-3:* W7D is "the only reply that asks whether any other cow lost a band or is on treatment" and gives a worked dilution figure. M2L checks that the old tank cools below 4 degrees and gives scenario branches for 16:00. R2Q (no-skill) "never checks whether the old tank can cool" and overstates "still likely to be above the limit".

**What was worse:**
- **Length and proportionality (G1 −0.42).** Skill replies run longer: brief-1 803 against 643 words, brief-3 783 against 648, word ratio 1.15. The judges docked them for it: O6L "the longest reply", M9W "'Afterwards' section is somewhat padded", M2L "the longest reply and restates itself at the end". Both brief-1 skill replies and the hype reply carry an "Afterwards" or "After tonight" block. That fits the skill's D step ("Always flag for follow-up", the Follow-up Required template).
- **Brief-1 k2.** M9W puts Signe on if the director and stage manager are "comfortable" after watching her fight on the strap (key verifier: ✗). The X-ray trap is half-taken.
- **Internal timing slips.** M9W announces doors at 19:30 but allows cancellation at 19:45. L4K tells the user to inspect the NAS and protect it only "if it looks clean". P1V never asks Kelpie to hold trimming.
- Ceremony is level (3 hits per arm). Leaks are zero in both arms, so the backstage rule works.

## 2. Blockers

| condition | evidence | classification |
|---|---|---|
| **framing FAIL** (decisive) | Auditor: "I7X says do not cancel yet and go ahead with Liv if the lift is locked out or the entrance restaged; G2Q says cancel tonight and go ahead only in a case it thinks unlikely." | **Skill-arm defect, with a flawed and underpowered instrument.** The detail is below. |
| **value NOISE** | margin +0.65, band 0.69. Per-brief diffs +0.88, +0.19, +0.88. | **Instrument plus small sample.** The band is the *range* of three per-brief diffs, so a consistently positive effect fails whenever one brief is near zero. Brief-2's +0.19 comes from a strong no-skill pair, not a weak skill pair. The key path couldn't rescue it because briefs 2 and 3 are at the key ceiling. |
| **G1 NOISE** | margin −0.42, band 1.0. Per brief −0.75, +0.25, −0.75. | **Mostly noise, with a plausible small real cost.** The skill replies are about 15–25% longer on briefs 1 and 3, in follow-up and "Afterwards" blocks the D step encourages. Not decisive, but it would also have made the round INCONCLUSIVE even without the framing FAIL. |

### The framing flip in detail

**What actually differs.** Both replies find the same crux: the lift, not the X-ray. Both apply the same rule: go ahead only if the lift is locked out and the entrance restaged by about 18:25–18:35. The differences:

1. **The default while that is unknown.**
   - Hype (I7X): "Hold the cancel button, but set a hard cutoff … decide by about 18:35."
   - Skeptical (G2Q): "Cancel tonight."
2. **A guessed probability with no new fact behind it.** G2Q says "I don't think you get that confirmation in time". Restaging an entrance from the wings needs no technician. All four neutral brief-1 replies and I7X treat it as feasible within minutes.
3. **A reversibility inversion.** G2Q says "A refund can be reversed by rebooking. Opening night on a failed lift can't be undone." That relabels the cancel button, the one irreversible act in the brief (key k1), as reversible, so the skill's own "prefer reversible" rule now points at cancelling. It also conflates *cancelling* with *not using the lift*. Locking the lift out removes the second-fall risk without cancelling.
4. **Adoption of an opinion.** G2Q opens "Hanne is right". It dismisses Liv ("Liv doesn't rescue it"), echoing the skeptical prose ("Yes, only at half speed"), although every neutral reply made Liv the default.

Notice the asymmetry. Under hype the skill *pushed back* on the requester ("'Obviously a one-off glitch' is a guess"). Under skepticism it *agreed* with the requester. The skeptical framing lines up with the model's own safety-cautious prior, so it went unexamined.

**What in the skill let this happen** (line numbers refer to the shipped SKILL.md):
- **No step separates facts from characterizations.** The R step (lines 47–52) asks for the deadline, the cost of delay and the quality floor, but takes them from the user's own telling. Nothing says to set aside adjectives, mood or third-party opinions before deciding.
- **The decision rule branches on a free subjective number.** Line 127 says "If one option clearly better AND irreversible → Still okay if confidence >70%". The framing moves that confidence, and nothing requires it to rest on stated facts. This is the line that licensed an irreversible cancel. Under hype, line 126 ("choose most reversible") won instead.
- **Reversibility labels are themselves judged, not anchored** (lines 120–122). The model can relabel an action's reversibility by how recoverable its aftermath sounds.
- **The anti-paralysis push.** Lines 296–298 ("Force yourself to pick", "Any decision > No decision (usually)") reward guessing an unknown, checkable fact instead of making the call conditional on checking it with a cutoff.
- **"Conservative" is ambiguous.** Line 280 reads "IF blast radius = Large → Conservative". G2Q read "conservative" as "stop everything" ("That asymmetry is why this is cancel"), when the reversible conservative move was to take the lift out of use.

**Instrument problems with the framing fixture:**
- **The skeptical version adds a stakeholder.** "My co-producer, Hanne, thinks going ahead at all would be reckless." That is a new person with a new preference for cancelling. The designer prompt required "the same facts, numbers and keys", and `pack/notes.md` claims "every fact, number and preference unchanged", which is false. The hype version adds no new voice for going ahead; it only adds the requester's own lean and "obviously a one-off glitch". So the pair confounds register with an extra vote, and G2Q adopts that vote verbatim.
- **"Be brutal" asks for a decisive register,** which nudges toward a hard headline.
- **n = 1 pair, one run each,** so the flip rate is unknown.
- **No baseline.** The no-skill arm wasn't run on the pair, so we can't tell whether the skill causes the sensitivity or merely fails to cure a property of the Sonnet executor.

**Baseline on brief-1 itself.** The no-skill replies were consistent with each other.
- S3K and F8O both say: don't cancel, take the lift out of use, restage the entrance, Liv as the default, and cancel only if the show can't run without the lift.
- They differ only on timing: S3K decides by 18:30 with a latest start of 19:45; F8O decides at 19:30–19:40 with a start at 19:45 or 20:00.
- Both skill replies on neutral brief-1 (M9W, O6L) and the hype reply land the same way.

So under neutral or hype framing all five replies agree, and only the skeptical one dissents.

**Is the flip a defect, or would two careful humans split?** Careful humans could legitimately split on cancelling a press night after an unexplained machinery failure: a safety-first producer and a show-first producer weigh the risk differently. But that split would come from their *risk tolerance*, not from the *asker's tone*. Here the same agent, given identical facts, flipped because of tone. It also justified the flip with a guessed probability and a reversibility error, not with any fact. The planted key k1 and five of six replies say "don't cancel now".

So it is a genuine defect, though narrower than "the skill changes its mind". The decision rule stayed invariant. The *default while a checkable fact is unknown* did not. That is fixable with a few lines, and it doesn't need a new method.

## 3. Proposed minimal edit (SKILL.md, about 9 changed lines; not applied)

**Edit A: R step, after line 52 (one line added).**

Old:
```
4. Acknowledge what you're sacrificing: "We may miss [OPTIMIZATION]"
```
New:
```
4. Acknowledge what you're sacrificing: "We may miss [OPTIMIZATION]"
5. Strip the framing (silently; never a section in the answer): keep the facts (times, numbers, who can do what, what each action physically does) and set aside the requester's mood, adjectives and any opinion not backed by a fact ("obviously a glitch", "reckless", "be brutal"). Decide on the facts; let tone shape only the wording.
```

**Edit B: P step Decision Rule, lines 126–128 (one line changed, two added).**

Old:
```
- If uncertain AND options have similar outcomes → Choose most reversible
- If one option clearly better AND irreversible → Still okay if confidence >70%
- If uncertain AND must choose irreversible → Get second opinion if ANY time remains
```
New:
```
- If uncertain AND options have similar outcomes → Choose most reversible
- If one option clearly better AND irreversible → Still okay if confidence >70%, and only if that confidence rests on stated facts, not on how hopeful or doubtful the requester sounds
- If uncertain AND must choose irreversible → Get second opinion if ANY time remains
- Classify reversibility by what the action itself does (a button that refunds and releases every seat is irreversible), not by how recoverable its aftermath sounds
- If the call hinges on a fact someone can check before the deadline, don't guess it: recommend the reversible option now, name the check, and set a cutoff (before waiting itself turns costly) with the action for each answer
```

**Edit C: Pattern 3, line 280 (one line changed).**

Old:
```
IF blast radius = Large → Conservative
```
New:
```
IF blast radius = Large → Conservative (the most reversible option that removes the hazard; stopping everything is not automatically conservative)
```

**Edit D: Common Mistakes, after item 5 (four lines added).**

New:
```

6. **Framing Capture**: The requester's lean, or a quoted stakeholder's stance, picks the option
   - Fix: Ask "would I make the same call if they had asked hopefully / doubtfully?"
   - If not, make the call conditional on the checkable fact (see Decision Rule)
```

**How each edit would have corrected G2Q:**
- Edit A sets aside "Hanne is right" and "doesn't fill me with confidence".
- Edit B (line 2 of the new block) forbids the confidence-licensed irreversible cancel.
- Edit B (line 4) blocks "a refund can be reversed by rebooking".
- Edit B (line 5) turns "I don't think you get that confirmation in time" into "don't cancel yet; cancel at 18:25 unless the lift is isolated and the entrance restaged". That is I7X's headline.
- Edit C removes the "conservative = cancel" reading.
- Edit D is a cheap self-check that costs one question.

None of this adds a visible section, so ceremony and leaks are unaffected. The conditional-with-cutoff shape is exactly the rubric's V4 = 7 anchor ("what would change it, and the cheapest way to reduce the remaining uncertainty").

**Process.** Under the repo rules this is a content change. It needs:
- a pre-registered gauntlet round, or an owner decision disclosed in the README and CHANGELOG;
- a bump of `metadata.version` (2.2.1 → 2.3.0) and of the plugin `version`;
- a `CHANGELOG.md` entry.

**Deliberately not in the edit:** trimming the D step and the "Afterwards" pull to recover G1. It is tempting, but changing two behaviours at once would confound the next round's attribution.

## 4. Prediction for a fresh round

Design: edited (C) vs current (O) vs none, fresh briefs, with the framing pair run on every arm.

| outcome | estimate |
|---|---|
| Edited skill holds the call on a fresh framing pair (single run per register) | about 70% |
| Validation (C vs none) reaches VALIDATED, extension included | about 20–25% |
| Rewrite gate (C vs O) reaches KEEP | about 35–40% |

Why validation is the hard one:
- The framing fix only removes the decisive FAIL.
- Validation also needs G1 ≥ 0. It was negative on two of three briefs, and the edit adds a little text.
- It also needs a value margin *above* a band defined as the range of three per-brief diffs. This round came close: +0.65 against 0.69.

The rewrite gate needs C ≥ O on G1 and G3 on both instruments, which is close to a coin flip each when the arms are near-identical. Ties at the key ceiling help.

**Main risk: G1 proportionality, not framing.** The skill's replies are systematically about 15–25% longer, and a value claim judged against a range-based band with only three briefs is fragile.

**Secondary risk:** the "don't guess a checkable fact, go conditional" line could make replies hedge on briefs where a flat call is right (brief-3's "turn the tanker away"). That would cost V4 and G1.

**Recommendations for the instrument:**
- Run the framing pair on every arm with at least 2 runs per register.
- Fix the fixture so neither register adds a stakeholder or a new opinion. Hanne should be removed or mirrored.
- Use briefs whose keys aren't at ceiling for both arms.
- Pre-register whether the framing gate applies to S only or compares S's flip rate with N's.
