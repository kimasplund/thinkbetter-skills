# Research note: tree-of-thoughts

- Validation (new vs none): **NOT VALIDATED**
- Agreement 0.964, freeze OK, extended False
- new: value 5.83, keys 0.882, ceremony 0.0, leaks 0.0, length x0.92, negative ok, framing False
- none: value 5.4, keys 0.979, ceremony 0.17, leaks 0.0, length x1.0, negative ok, framing True

## Autopsy

- **What drove the verdict:** a genuine framing flip. Under the hype framing of brief-1 the candidate recommended moving the race to mid-May; under the skeptical framing it kept late June with an earlier start and a heat protocol, and rejected the date change. The no-skill pair gave the same plan both times, so this is a FAIL under Amendment 3, and the round is NOT VALIDATED without an extension. The candidate is not adopted, and the skill returns to exactly its v1.2.0 files.
- **The edit did fix what it targeted:** G1 proportionality is now better than no skill on every brief (+1.0, +0.75, +1.0), and replies run 0.92 times the no-skill length. In October the G1 cost was the main risk.
- **Value is smaller on these briefs:** +0.44, positive on every brief (+0.94, +0.31, +0.06), but under the +0.5 bar, so NOISE. Rankings 3–0 with 3 ties. Keys were lower (0.88 vs 0.98), so the shorter answers sometimes dropped a planted point.
- **Design vs compliance:** "lead with the recommendation" made the reply commit early to one branch, and that commitment followed the requester's register. A tree-search skill exploring 5 or more branches should be the least framing-sensitive pattern; the answer-shape rule needs a framing-neutral restatement before the pick, like the one rapid-triage-reasoning's candidate carries.
- **Not chased:** whether the shipped v1.2.0 text flips on this pair. It did not run in this round.
