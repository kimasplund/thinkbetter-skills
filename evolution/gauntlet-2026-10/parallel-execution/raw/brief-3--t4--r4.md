**Short answer:** the split by site works, but not as you've described it. Four things in the setup would make the four-site average wrong or hard to interpret, and I'd settle them before Wednesday. Each one is quick to fix and has to be the same for all four analysts. The fan-out itself is fine once these are fixed.

## Fix before the split (Tuesday, one person, about half a day)

1. **Transect 7 is in both Site A (1-7) and Site B (7-12).** That makes 23 listings for 22 transects, so one is probably a typo. If it's real, transect 7 is counted twice in the regional figure. Decide which site owns it, and have both analysts drop it from the other.

2. **The tit-wren split.** Only Site D uses the new reed and sedge codes, so D's 2023-25 data can't be compared with the others. The fix is to collapse reed and sedge back into "marsh tit-wren" at Site D, for 2023 onward, before anything is fitted. Seasons 2023-25 are too short for a separate reed or sedge trend, so report the combined species only. Check that nobody else has quietly adopted the new codes. Also confirm that every site's species list uses one naming standard. I'd have one person write a single species crosswalk and give it to all four analysts.

3. **Observer is confounded with period at every site.** Mara and Tobiah swapped site pairs in 2022. So at A and B, "Mara then Tobiah" is perfectly aligned with "early then late". Mara records more quiet, high-pitched species, so A and B will show an artificial decline for those species and C and D an artificial rise. A model fitted to a single site cannot separate the observer effect from the real trend. The swap works in your favour once the sites are pooled: it is balanced, so a pooled model can estimate the observer effect. That means:
   - Analysts should not each fit a trend and hand back a number. An observer-adjusted trend can only come from a model fitted across all four sites.
   - A plain unweighted average of four site trends only roughly cancels the bias, and only if the sites are similar in size and the effect is the same everywhere. It won't be exactly so, because the sites cover 7, 6, 5 and 5 transects.

4. **Site B 2021 imputation.** The protocol fills it with the ratio to Site C in the same year. That is a problem for three reasons:
   - It makes Analyst B depend on Analyst C's data, so the two can't run independently.
   - In 2021 B was counted by Mara and C by Tobiah, so the ratio carries the observer difference. It is worst for the quiet species.
   - Filled values then look like real data and shrink the uncertainty.

   My recommendation is to leave 2021 missing at B. Trend models handle a missing year without trouble. If the board requires the protocol, do the fill once, centrally, flag the rows as imputed, and report the trend with and without them. Your protocol, so your call, but make it one decision for all analysts.

## What each analyst does (Wednesday onward, in parallel)

Every analyst gets the same instructions, with their own site's spreadsheet.

1. Apply the species crosswalk, with Site D's tit-wren merge, and the transect ownership rule.
2. Run data checks:
   - 10 points per transect per year.
   - No duplicate or missing point-years, other than B 2021 if applicable.
   - Observer recorded on every row.
   - Species with zero detections in some years listed.
3. Produce a clean long-format table for the site: site, transect, point, year, observer, species, count. Use identical column names for all four.
4. Fit per-site trend models as a diagnostic: a log-linear trend per species (for example a Poisson or negative binomial GLMM with a transect random effect). These are for comparison and are not the regional figure, because of the observer problem above.
5. Flag species with too few detections to fit (say, fewer than 20 total, or absent in more than 3 years). Don't force a fit.

## What they hand back

- The clean table (item 3), as CSV with a fixed column spec.
- The diagnostic trend table: species, estimated annual log-change, standard error, n detections, model type, and any fit warnings.
- A short note listing anything unusual: recodes, dropped rows, species flagged as unfittable.

## How you combine it (after hand-back)

1. Stack the four clean tables and check that they reconcile (row counts per site-year, species list identical).
2. Fit one pooled model per species across all sites, with an observer fixed effect, site as a fixed effect or random intercept, a transect random effect, and a shared year trend. Optionally allow a site-by-year-trend term, which shows how much the sites differ. This is the regional figure.
3. As a check, compare the pooled trend with the average of the four site trends. A large gap tells you the observer effect matters for that species.
4. If you still want an average of site trends for the report, weight by transect count (or by area) and combine standard errors properly. A simple mean throws away the uncertainty.
5. Report the quiet, high-pitched species with a caveat. They are the ones most sensitive to the observer effect.
6. Run a sensitivity check with B 2021 imputed versus missing, if the protocol fill is used.

## Timeline

Tuesday is for the four fixes above and for writing one shared analysis spec. The analysts then run in parallel from Wednesday. Pooling takes you a day or two once the four tables are in. That fits comfortably before the end of the month, and it avoids a regional trend that is partly an artefact of who counted where.

If you can tell me how transect 7 should be assigned, and whether the board will accept leaving 2021 missing, I can turn this into a one-page analyst brief and a column spec.
