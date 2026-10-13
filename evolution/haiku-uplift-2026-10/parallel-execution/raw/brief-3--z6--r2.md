I'd advise against the site-per-analyst split as described, because it would produce a regional trend that looks fine but is biased. Your data has four problems that a per-site split can't fix. Each one is easy to deal with if you change the plan slightly, and you can still start Wednesday.

## Why the site split doesn't work

1. **Observer is confounded with time within every site.** Each site has exactly one observer switch (A and B go from Mara to Tobiah after 2021, C and D go from Tobiah to Mara). Mara records more quiet, high-pitched species. So within a single site, "observer effect" and "real trend" can't be separated. Site A will show a spurious decline in high-pitched species after 2021, and Site C will show a spurious increase. Averaging the four sites would partly cancel these, but only by luck, and the leftover is unquantified. The observer effect can only be estimated across sites, because the switches go in opposite directions in the same year. That needs one joint model, not four separate ones.

2. **Transect 7 is in both Site A (1–7) and Site B (7–12).** Those 10 points would be counted twice in the regional figure. Please confirm whether this is a typo, for example B should be 8–12 or A should be 1–6, or whether two sets of counts really exist for transect 7. Decide this before anyone starts. It also changes the site sizes (7, 6, 5 and 5 transects, or 6, 6, 5 and 5 if the overlap is a typo).

3. **The tit-wren split affects only Site D.** From 2023, D has reed and sedge tit-wren, while A, B and C still say "marsh tit-wren". A per-site model would give D two new species with 3 seasons of data and no trend for the old species. The analysts would also have no way to line D up with the others. The fix is to merge D's two new codes back into "marsh tit-wren" for 2023 on, for the regional trend. Do this once, centrally, and keep the split codes as a separate dataset. If you want separate reed and sedge trends, that has to be a Site D-only supplementary analysis.

4. **The missing Site B 2021 value is filled using Site C, and the observers differ.** In 2021 Mara would have counted B and Tobiah counted C. So the B/C ratio carries the observer difference, especially for the quiet species. Also, a filled-in number treated as real data makes the model overconfident. I'd treat 2021 at B as missing in the model and let it estimate through the year and site structure. If the board needs the written protocol, run the protocol version as a sensitivity check and compare. Note the protocol has this flaw, and consider amending it.

## Revised plan

**Step 0, before Wednesday (you or one person, about a day).**
- Settle the transect 7 question.
- Stack the four spreadsheets into one long file with columns for site, transect, point, year, observer, species and count. Add observer from your roster, which is determined by site and year.
- Recode D's 2023+ reed and sedge tit-wren to marsh tit-wren (keep the originals in another column).
- Leave 2021 at B missing. Do not impute.
- Run basic checks (duplicates, transect numbering, 10 points per transect-year).

**Step 1, on Wednesday, split by species, not by site.** Give each of the four analysts about a quarter of the species, for example grouped by detectability (quiet, high-pitched species should be shared out or reviewed together, because the observer effect matters most there). Each analyst fits one model per species using **all four sites**:

- count ~ year trend + observer effect + site effect (+ point or transect random effect for repeat visits)
- Use a Poisson or negative binomial family, or occupancy or presence if counts are very sparse.
- Use the same model template, code and software for everyone, which you supply. Without this, the four sets of results won't be comparable.
- The observer term is identified because Mara and Tobiah swapped sites in opposite directions. Please check that the analyst reports its size and uncertainty.

**What each analyst hands back, per species:**
- Trend estimate (per-year % change) with standard error and 95% interval, for all sites combined.
- The same for each site (as a derived output from the same model, optionally with a site-by-year-trend term).
- Observer effect estimate with interval.
- Number of detections, and a flag if the species was too sparse to fit.
- Model diagnostics (convergence, dispersion, residual check) and the code and version used.
- A sensitivity result: trend with and without the 2021 Site B protocol fill.

**Step 2, how you combine.**
- No need to average site trends. The joint model already gives a regional trend and its uncertainty. If you do want site-level numbers, combine them with weights by site size (number of points), not a simple mean of four, and combine standard errors properly instead of averaging them.
- Collect the four outputs into one table. Check for species where results look odd: wide intervals, a large observer effect, or a big difference from the sensitivity run.
- Report results for D's tit-wren as the merged "marsh tit-wren", with the split species as a short note.

## Caveat for the report

Even with this, observer and period are tied to site pairs (A and B versus C and D), so the observer estimate rests on that contrast. Say that in the methods. It is also worth asking Mara and Tobiah whether either has a cross-calibration (any years or points where both counted) that would let you check the observer effect directly.

## Assumptions

I've assumed "transect 7" in both Sites A and B is an error (or at least needs checking), that the data are counts per point per year, and that your four analysts can all work in the same software. If it's a different setup, the plan adapts, but the key points hold: fit one joint model, put observer in it, clean up the codes once, and don't fill in the 2021 B value from C.

If it would help, I can draft the model template and the exact column layout for the stacked file so that the analysts can start straight away on Wednesday.
