# Pre-registration: tree-of-thoughts (Haiku uplift)

Written 2026-10-13, before any new cell ran. The question: does Haiku with this skill reach Sonnet without it? Design: `docs/superpowers/specs/2026-10-13-haiku-uplift-design.md`.

- **Arms:** hs = haiku with the skill; hn = haiku alone; ss = sonnet with the skill; sn = sonnet alone (replies reused from arm 'none' of `evolution/gauntlet-2026-10/tree-of-thoughts`). Arm codes are sealed in `SEALED.json`.
- **Pack:** the sealed pack of `evolution/gauntlet-2026-10/tree-of-thoughts`, unchanged. Reused replies came from the same pack and the same executor prompts; their provenance is in `reuse.json`, and they are frozen with the pack.
- **Cells:** 24 main cells (3 briefs × 4 arms × 2 runs). This program runs no framing or negative fixtures.
- **Instruments:** as in the 2026-10 programs. Two Opus judges (J-A practitioner, J-B skeptic) score every reply of a brief in one blind panel against `harness/rubric.md` and rank them; a Sonnet auditor applies the rule text below; Sonnet key verifiers grade the held-out keys.

## Gate text (binding)

**Reaches Sonnet (H = Haiku with the skill, S = Sonnet alone).** REACHES iff all hold:
1. Value (mean of V1–V4, brief-paired): H − S ≥ −0.25.
2. Keys: H − S ≥ −0.10.
3. Judge guards G1, G2, G3: H − S ≥ −0.25 on each.
4. Auditor: H carries at most one more ceremony hit and at most one more leak hit than S in total; H's replies are at most 2.0× S's median length.
5. Rankings: FAIL only if H loses more rankings than it wins with a two-sided sign test p ≤ 0.2.
6. Inter-judge agreement at least 0.80; `freeze.py verify` clean.

**Uplift (reported with a verdict, no action follows).** Haiku with the skill vs Haiku alone, and Sonnet with the skill vs Sonnet alone, each under the validation gate of the follow-up program (Amendment 3), without the framing and negative conditions.

**Conditions and noise:** each condition is PASS, FAIL or NOISE. Margins are brief-paired, and the band is the max − min of the per-brief differences; a margin below its bar but within the band is NOISE. Any FAIL decides the negative verdict; otherwise any NOISE gives INCONCLUSIVE. INCONCLUSIVE on any comparison gets one extension (runs 3 and 4 of every arm; reused arms take runs 3–4 from the source round where they exist and run fresh otherwise). After it, INCONCLUSIVE reads DOES NOT REACH or NOT VALIDATED.

**What follows:** no skill text and no README row changes because of this program. The result is reported in the README and `docs/VALIDATION.md`.

**Auditor rule text (quoted verbatim to the auditor):**
- **Ceremony:** a ceremony hit is any of the following, in a reply's user-facing text:
  - a section that restates the question;
  - a heading or label that describes the method rather than the content;
  - a summary that repeats earlier sections without adding information;
  - a template field left in place with nothing new in it;
  - a decision-record or report scaffold on a task that needed a direct answer.
- **Leak:** a leak hit is any of the following:
  - the name of a reasoning method, framework or skill (for example "tree of thoughts", "breadth-of-thought", "dialectical", "premortem", "hypothesis elimination");
  - an acronym for one;
  - internal scoring schemes, rating tables or confidence arithmetic shown to the user (a plain statement of how confident the reply is, in words or a single figure, is calibration and is not a leak);
  - numbering of the method's own stages or phases.

  Headings about the user's content are not leaks.

No goalpost movement after results. A bar that turns out to be mis-set is reported under both readings, and this text decides.

## Freeze record

Recorded in FREEZE.md (written right after registration).
