Notes (J-B, brief-3)

Q9R: Clean species-group split with all the main issues: observer confound, transect 7, tit-wren lump, B 2021, weighting. It misses that the B/C 2021 ratio itself carries the Mara/Tobiah difference. Concise and actionable.
E0N: Catches everything, including the observer bias in the 2021 B/C ratio, and states its assumptions. It is padded with the Option A/B site alternatives and a long limits list.
L6T: Keeps site split for prep plus diagnostic fits, with a central pooled model. Sound, and it catches the ratio observer bias. Analysts' site fits are mostly busywork. "Fan-out" phrasing.
T9W: Same shape as L6T, with a good explicit fallback and an honest note that two observers make a weak observer estimate. Misses the ratio observer bias. "About an hour" is optimistic.
J3I: Prep by site, then fitting by species group. Strong, and it asks about any overlap data for direct calibration. Arithmetic slip: if transect 7 goes to A, B has 50 points, not 60.
L7C: Species split, catches all issues, and has a good sanity check (loud species should show near-zero observer effect). The "3 vs 4 years asymmetry" reasoning is muddled, and prep through Thursday morning contradicts "from Wednesday".
O4R: Species split, all key issues including the ratio observer bias, the seven-season caveat and a clean hand-back. Well sized.
J2U: Recommends per-site fits with an observer covariate, which is aliased with the 2022 step inside a site. It wrongly says the swap year differs by site. It suggests using years where B and C had the same observer, but no such years exist. Long.
N8O: Per-site fits with an observer term, then a pooled model as preferred. Inconsistent. It misses the specific 2021 Mara-B/Tobiah-C ratio bias and only vaguely gestures at it.
K0T: Species split with a joint model. Catches the ratio observer bias. It honestly caveats that the observer estimate rests only on the A/B vs C/D contrast and asks about cross-calibration. Small slip in the alternative site-size list.
S1U: Good structure, with a species split and a QA-owner idea. It wrongly says the switch happens "at different times at different sites" (it is the same year, opposite directions), and its 2021 ratio explanation is garbled.
Q5J: Keeps per-site fits with an observer covariate and asks for the four within-site observer coefficients to be compared, but those are not identifiable within a site. That contradicts its own point 1. The pooled model appears only as a check.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,Q9R,5,6,6,6,6,7,5,41
J-B,E0N,7,6,6,6,4,7,6,42
J-B,L6T,6,6,6,6,5,6,5,40
J-B,T9W,5,6,5,6,5,7,6,40
J-B,J3I,7,6,5,6,6,7,5,42
J-B,L7C,7,6,5,6,5,7,6,42
J-B,O4R,6,6,6,6,6,7,5,42
J-B,J2U,5,5,2,4,3,7,4,30
J-B,N8O,5,5,4,5,4,7,5,35
J-B,K0T,7,6,6,6,6,7,6,44
J-B,S1U,6,6,4,6,5,7,5,39
J-B,Q5J,5,5,3,4,5,6,4,32
```

```ranking
judge,brief,order
J-B,brief-3,K0T O4R J3I L7C E0N Q9R L6T T9W S1U N8O Q5J J2U
```
