Splitting by site can work for the model fitting, but four things in your description would make the four trends quietly wrong or not comparable. Fix them in a short shared step before Wednesday, then fan out.

## Problems to fix first

1. **Observer is confounded with time inside every site.** At each site, Mara and Tobiah swap in a fixed year. Site A has Mara in 2019–2021 and Tobiah in 2022–2025. Site C has the reverse. An analyst who sees only one site cannot tell an observer effect from a real trend. For quiet, high-pitched species the observer effect is large, and it will appear as a trend of the opposite sign at A/B versus C/D. Averaging the four sites might cancel it partly, but not reliably. The design does let you separate the two across sites, because the swap runs in opposite directions. That means observer has to be a covariate in every model, and its effect has to be estimated from all sites together (see "Combine").

2. **Transect 7 is in both Site A and Site B.** Site A is transects 1–7 and Site B is 7–12. That is 23 listed transects for 22 real ones. Please check whether this is a typo (for example, A should be 1–6, or B should be 8–12). If transect 7 really is shared, its data would be counted twice, and two analysts would model the same counts. Assign it to one site only.

3. **The tit-wren split is only in Site D.** Sites A–C log "marsh tit-wren" for all years. Site D logs reed and sedge tit-wren from 2023. Fitting these separately would give D two short, different series. Before anyone fits anything, collapse reed and sedge at Site D to "marsh tit-wren" for 2023–2025, so all four sites share one species list. If you want separate reed and sedge trends later, treat that as a small separate analysis for 2023 onward, and only where the observers can tell them apart.

4. **The Site B 2021 fill needs Site C, and a ratio fill is not a good idea anyway.** Site B's analyst would depend on Site C's data, which breaks the independence the split relies on. The fill also treats an imputed value as if it were a real count, so the uncertainty comes out too small. Your protocol says to do it, so decide with the board whether you can deviate. My recommendation is to leave B 2021 as missing and let the model handle it, which gives B six seasons and honest uncertainty. A site-year random effect or a smooth trend handles a gap without any fill. If the protocol must be followed, run the fill once in the shared prep step. Flag those values, and also fit without them as a sensitivity check. 2021 was also a Mara-at-A/B year, so the gap is not neutral for the observer effect.

## Step 0: shared preparation (one person, before Wednesday)

- Settle the transect 7 assignment.
- Harmonise species codes across all four spreadsheets, using one lookup table.
- Add columns for `observer` and `site` to each file, filled from your records. Also add `year`, and a flag for any filled value.
- Decide the B 2021 approach and carry it out here if you use the fill.
- Write a one-page model specification all four analysts will use: same count family (for example Poisson or negative binomial), same trend definition (log-linear slope per year, 2019–2025), same observer covariate, same random effects (transect and point within transect), same species list, and the same handling of species with too few detections (for example fewer than 3 detections at a site: do not fit, report as "insufficient data").
- Fix the random seed and the software version.

## What each analyst does (in parallel, one site each)

1. Fit the specified model for every species at their site.
2. Check fit: dispersion, convergence, residuals by year.
3. Write the results to the shared template, in their own file (never edit another analyst's file).

## What each analyst hands back

One table per site, same columns for everyone:

- species, site, number of detections, number of points
- trend estimate (log scale slope per year) and its standard error
- observer coefficient (Mara versus Tobiah) and its standard error
- annual index for each season, with its standard error
- convergence and dispersion flags, and a notes column

Also the fitted model object and the script. Return the estimates and standard errors, not just percentages, because you need the standard errors to combine them.

## How you combine it

1. **Do not simply average the four trends.** Use an inverse-variance weighted average of the site slopes, or weight by the number of points or transects in each site (A 6–7, B 5–6, C 5, D 5 transects). Say which weighting you chose and why in the report. An unweighted average gives a 5-transect site the same say as a 7-transect one.
2. **Handle the observer effect.** The best option is one pooled model across all four sites (a site-by-species random effect, observer as a fixed effect), run once by you or one analyst as a check. The pooled model separates observer from time because the swap runs in opposite directions at A/B and C/D. Compare its regional slope with the weighted site average. If they differ meaningfully for the quiet, high-pitched species, report the pooled one. If you keep the four-site approach, check that the four observer coefficients agree in sign and size. They should be about the same, since the same two people made the counts.
3. **Uncertainty.** The standard error of the regional slope comes from the weights and the site standard errors, not from averaging standard errors. Report confidence intervals for the regional trend, and show the four site trends next to it.
4. **Checks before the board sees it.** Compare site trends for each species and look at any where the sites disagree in sign. Rerun with and without the B 2021 fill. For tit-wren, report the combined marsh tit-wren trend only.

## Timeline suggestion

Step 0 on Monday and Tuesday so the four analysts can start on Wednesday with identical inputs. Have them return results by the end of next week, which leaves the following week for the pooled-model check and the report before the end of the month.

If you can tell me the answer on transect 7 and whether the B 2021 protocol is negotiable, I can turn the specification into an exact template for the analysts.
