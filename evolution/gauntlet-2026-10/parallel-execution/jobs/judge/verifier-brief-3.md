You are a strict key verifier.

Read the user's request at ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/inputs/brief-3.md, then these reply files, and nothing else under ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution:
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/Q5J.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/S1U.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/K0T.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/N8O.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/J2U.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/O4R.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/L7C.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/J3I.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/T9W.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/L6T.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/E0N.md
- ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/blind/Q9R.md

Each code is a file name without ".md". Below are the sealed keys: things a strong reply must catch. Never reproduce them anywhere except in your output file.

- k1: Transect 7 belongs to both Site A (1-7) and Site B (7-12). If each analyst models their own site and the results are combined, transect 7's birds are counted twice and both sites share non-independent data. A strong reply assigns transect 7 to one site, or removes the duplicate, before the split.
- k2: The observer is confounded with a 2022 step change at every site. A and B switch from Mara to Tobiah in 2022, and C and D switch from Tobiah to Mara. Within one site, the observer effect cannot be separated from a real change in 2022, so per-site models will show spurious declines at A and B and spurious increases at C and D for quiet species. Averaging these partly cancels them and hides the problem. Only a pooled model across all sites with a shared year effect can estimate the observer effect. A strong reply pools the observer adjustment, or the whole model, instead of fanning it out by site.
- k3: Taxonomy must be harmonized before any site analysis. Site D splits marsh tit-wren into reed and sedge tit-wren from 2023 while A-C do not, so D shows an artificial crash in marsh tit-wren and two new species appear at one site only. A strong reply requires a central step that lumps the two species back into the old code (or otherwise reconciles them) before the analysts start, rather than leaving it to each analyst.
- k4: Site B's analysis depends on Site C's output. The missing 2021 B season is imputed from Site C's same-year counts, so the B analyst needs C's cleaned (and observer-consistent) data first. Note that C's 2021 observer differs from the one B would have had. A strong reply sequences B after C for that step, or centralizes the imputation, instead of treating B as independent.

For every reply and every key, grade:
- ✓ if the reply clearly identifies the key in substance, with the right implication;
- ~ if it does so only partially or vaguely;
- ✗ if the key is missing or wrong.

When you are torn between two grades, give the lower one. Add a quote of 15 words or fewer as evidence for each grade.

Write JSON to ~/projects/thinkbetter-skills/evolution/gauntlet-2026-10/parallel-execution/keys/brief-3.json in exactly this shape:
{"<CODE>": {"<key_id>": "✓", "evidence": {"<key_id>": "quote"}}}

Then return only: done
