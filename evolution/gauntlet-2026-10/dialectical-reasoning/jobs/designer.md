You are designing a sealed evaluation pack for the skill "dialectical-reasoning". Read ~/projects/thinkbetter-skills/skills/dialectical-reasoning/SKILL.md and any references it links, so you understand what the skill claims to do.

Write these files into ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/dialectical-reasoning/pack:

- **brief-1.md, brief-2.md, brief-3.md:** three realistic user requests, each in a different fictional domain. Each should be hard enough that the skill ought to matter, meaning something a strong professional would find genuinely tricky. Write each in 120–300 words, as the user would write it, with the facts needed and no hints at the answer.
- **Keys:** plant keys of this type in every brief: a false dichotomy that hides a workable third option. Plant 3–4 per brief. Every key must be checkable: a strong reply either catches it or doesn't.
- **Difficulty:** in every brief, at least two keys must be things a capable assistant answering quickly and without a careful method would plausibly miss. For example, the decisive evidence is easy to overlook, the most salient clue points the wrong way, or the key only becomes visible after something else is ruled out. A key that can be found by restating the most obvious clue is too easy. If every key is caught by every reasonable reply, the evaluation measures nothing.
- **framing-hype.md and framing-skeptical.md:** the same facts as brief-1, rewritten once in an excited, hype register and once in a doubtful, skeptical register. Keep the same facts, numbers and keys.
- **negative.md:** a task too small for this skill, such as a quick factual or one-step request in the same general area, where the right answer is short and direct.
- **keys.json:** in this shape:
  {"brief-1": [{"id": "k1", "text": "what a strong reply must catch, and why", "split": "held-out"}], "brief-2": [...], "brief-3": [...]}
- **notes.md:** one short paragraph per brief explaining its planted keys.

Rules:
- Use fictional domains, companies and people only. No real companies, people, products or private projects.
- Never reuse or paraphrase any brief or fixture from these earlier rounds: 
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/_pilot-1-unfit-hypothesis-elimination/pack/brief-1.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/_pilot-1-unfit-hypothesis-elimination/pack/brief-2.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/_pilot-1-unfit-hypothesis-elimination/pack/brief-3.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/_pilot-1-unfit-hypothesis-elimination/pack/framing-hype.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/_pilot-1-unfit-hypothesis-elimination/pack/framing-skeptical.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/_pilot-1-unfit-hypothesis-elimination/pack/negative.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/adversarial-reasoning/pack/brief-1.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/adversarial-reasoning/pack/brief-2.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/adversarial-reasoning/pack/brief-3.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/adversarial-reasoning/pack/framing-hype.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/adversarial-reasoning/pack/framing-skeptical.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/adversarial-reasoning/pack/negative.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/breadth-of-thought/pack/brief-1.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/breadth-of-thought/pack/brief-2.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/breadth-of-thought/pack/brief-3.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/breadth-of-thought/pack/framing-hype.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/breadth-of-thought/pack/framing-skeptical.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/breadth-of-thought/pack/negative.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/pack/brief-1.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/pack/brief-2.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/pack/brief-3.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/pack/framing-hype.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/pack/framing-skeptical.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/hypothesis-elimination/pack/negative.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/pack/brief-1.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/pack/brief-2.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/pack/brief-3.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/pack/framing-hype.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/pack/framing-skeptical.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/integrated-reasoning/pack/negative.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/pack/brief-1.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/pack/brief-2.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/pack/brief-3.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/pack/framing-hype.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/pack/framing-skeptical.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/pack/negative.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/premortem-evolved/pack/brief-1.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/premortem-evolved/pack/brief-2.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/premortem-evolved/pack/brief-3.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/premortem-evolved/pack/framing-hype.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/premortem-evolved/pack/framing-skeptical.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/premortem-evolved/pack/negative.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/pack/brief-1.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/pack/brief-2.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/pack/brief-3.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/pack/framing-hype.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/pack/framing-skeptical.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/reasoning-handover-protocol/pack/negative.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/pack/brief-1.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/pack/brief-2.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/pack/brief-3.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/pack/framing-hype.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/pack/framing-skeptical.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/self-reflecting-chain/pack/negative.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/tree-of-thoughts/pack/brief-1.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/tree-of-thoughts/pack/brief-2.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/tree-of-thoughts/pack/brief-3.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/tree-of-thoughts/pack/framing-hype.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/tree-of-thoughts/pack/framing-skeptical.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/tree-of-thoughts/pack/negative.md
- ~/projects/thinkbetter-skills/evolution/thinkbetter-suite/regression-2026-10-13/fixtures/fixtures.json
- ~/projects/thinkbetter-skills/examples/premortem-evolved/deployboard-premortem.md
- ~/projects/thinkbetter-skills/examples/premortem-evolved/premortem-newsletter-example.md
- ~/projects/thinkbetter-skills/skills/skill-gauntlet/references/fixtures.md
- Never hint at a key in a brief, and never quote expected answers.
- Briefs must not mention skills, reasoning methods, evaluation, or that this is a test.

When done, return at most 10 lines: one line per brief naming its domain, and one line naming the fixture types. Say nothing about the keys.
