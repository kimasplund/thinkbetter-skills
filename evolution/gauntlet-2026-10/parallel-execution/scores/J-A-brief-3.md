Notes (J-A, practitioner persona)

- Q5J: Catches all four data traps and the weighting issue. It keeps the site split with a per-site observer covariate, though it has just said observer can only be estimated across sites. The pooled model is only a check. The plan is internally inconsistent.
- S1U: Species-split with a pooled model is the right structure, with a good hand-back spec. It wrongly says the switch happens "at different times at different sites", and its 2021 observer sentence is garbled (Tobiah did C in 2021).
- K0T: Species split with a joint model. Every trap is handled correctly, including the observer bias in the B/C ratio. It alone flags that the observer estimate rests on the A/B vs C/D contrast, and it suggests a cross-calibration check. Strongest.
- N8O: Keeps the site split, with a pooled model as the preferred cross-check. Thorough but long. The point counts are slightly off, and it never states the observer bias in the 2021 ratio itself.
- J2U: Keeps the per-site fits and claims observer becomes identifiable if all analysts "use the same model", which is wrong for separate fits. It says the switch happens in different years at different sites, and it suggests ratio years "where B and C had the same observer" (none exist). The test species and leave-one-out ideas are good.
- O4R: Correct species-split plan, solid and clean. The sensitivity run with "split vs combined tit-wrens" makes little sense. Thinner on what would change the plan.
- L7C: Species split. It picks up the 3-vs-4-year asymmetry, gives a sanity check (loud species should show roughly zero observer effect) and asks about overlap calibration. Analysts start Thursday instead of Wednesday.
- J3I: Smart use of the site split for prep, then a joint fit split by species. Concise. Its point-count arithmetic is wrong (B 60 if transect 7 goes to A).
- T9W: Site split for cleaning, then a central pooled fit, with an honest fallback and disclosure. It misses that the B/C ratio carries the observer difference. Timeline is concrete.
- L6T: Site-split prep plus diagnostic per-site fits, then a pooled model. All traps are covered, including the ratio's observer bias. Practical checks.
- E0N: Covers everything but hedges with several options. The "with and without D's split codes" sensitivity is muddled. Long.
- Q9R: Clean, concise species-split plan. It misses the observer bias inside the B 2021 ratio fill. Good spot-check step.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-A,Q5J,5,6,4,5,5,7,5,37
J-A,S1U,6,6,4,6,5,7,4,38
J-A,K0T,7,6,6,6,5,7,6,43
J-A,N8O,5,6,5,5,4,7,5,37
J-A,J2U,5,6,3,4,4,7,4,33
J-A,O4R,6,5,5,5,5,7,5,38
J-A,L7C,6,6,6,6,5,7,6,42
J-A,J3I,6,5,5,6,6,7,5,40
J-A,T9W,5,6,6,6,5,7,6,41
J-A,L6T,6,6,6,6,5,7,5,41
J-A,E0N,6,5,5,4,4,7,5,36
J-A,Q9R,5,6,5,5,6,7,5,39
```

```ranking
judge,brief,order
J-A,brief-3,K0T L7C L6T T9W J3I Q9R S1U O4R Q5J N8O E0N J2U
```
