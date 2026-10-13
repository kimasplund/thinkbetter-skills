I'd change the split before Wednesday. As written, "one site per analyst, then average the four trends" would give you numbers that look fine but are partly artifacts of how the data were collected. Below are the problems, then a plan that still lets four people work in parallel and still starts Wednesday.

## Problems with one site per analyst

1. **Observer is confounded with time within every site.** Mara counted A and B in 2019-21 and C and D in 2022-25. Tobiah did the reverse. So at each site the observer changes exactly once, and Mara records more quiet, high-pitched species.
   - Sites A and B will show spurious declines for those species (Mara, then Tobiah).
   - Sites C and D will show spurious increases (Tobiah, then Mara).
   - A single-site model cannot separate observer from trend, because they are the same variable.
   - Averaging the four sites may partly cancel the bias, but only by luck, and the weights are not equal. Don't rely on it.
   - A pooled model across sites can estimate the observer effect, because the switch happens at different times at different sites. It needs observer as a covariate and a shared year trend.
2. **Transect 7 is in both Site A (1-7) and Site B (7-12).** Either that is a typo or two analysts will model the same 10 points. Please confirm which site owns transect 7 before anyone starts. If it is double-counted, the regional average is no longer independent across sites.
3. **The tit-wren split is only applied at Site D.** From 2023, D reports reed and sedge tit-wren, while A, B and C still report "marsh tit-wren". D's marsh tit-wren series therefore appears to collapse in 2023, and the new species starts from zero. Four analysts would each handle this differently.
4. **The Site B 2021 fill uses Site C, but the ratio is not neutral.**
   - It creates a data point that was never observed. It also couples B's trend to C's, so the sites are no longer independent in the average.
   - Mara did B in 2021, and she was Tobiah's replacement at C in that period, so the ratio mixes observer effects.
   - Follow the written protocol if you must, but I'd fit the model with 2021 simply missing, which a count model handles fine. Run the protocol fill as a sensitivity check and report both.
5. **Averaging four site trends treats them as equally reliable.** Sites differ in size (A, B, C, D have 7, 6, 5 and 5 transects, or similar) and in how many species occur there. A species seen at only one or two sites needs different handling from a species seen at all four.

## Suggested structure

**Step 0 (you or one designated person, Monday and Tuesday): harmonise the data once.** Do this before anyone fits a model.
- Resolve transect 7.
- Build one combined table with the same columns plus `site`, `year`, `observer`, and a flag for imputed or missing site-years.
- Create a species crosswalk. For all sites and years, collapse reed tit-wren and sedge tit-wren into "marsh tit-wren (sensu lato)" so the 2019-2025 series is consistent. Optionally keep a separate reed versus sedge look at Site D 2023-25, labelled exploratory.
- Decide the missing-B-2021 treatment (see above).
- Write one model specification, for example a count model (negative binomial or Poisson with overdispersion) with `count ~ year + observer + site (random or fixed) + offset(points surveyed)`, and one script every analyst uses. Fix this before they start.

**Step 1 (Wednesday onward): split by species group, not by site.** Give each analyst a quarter of the species list (grouped by, say, habitat or detectability so each analyst has a mix of loud and quiet species). Each fits the shared pooled model, with all four sites, for their species.
- This uses the same effort as the site split, and it is the only version where observer and trend can be separated.
- If you prefer to keep a site structure for ownership, give each analyst one site as a **QA owner** (check data, transect coverage, outliers, year-by-year plots) and also a species group for fitting.

**What each analyst hands back, in one standard format (one row per species):**
- Species, number of site-years with data, number of sites where it occurs.
- Trend estimate (log scale per year and percent per year) with standard error and 95% CI.
- Observer effect estimate with its CI.
- Site-specific trend estimates (as a check, not as the headline).
- Convergence and overdispersion diagnostics, plus a note on any problems.
- Sensitivity: trend with and without the B-2021 fill, and with and without the observer term.
- Script and package versions, and the random seed.

**How you combine it:**
- Because every analyst fitted the same pooled model, the regional trend is already in their output. You only need to stack the tables, not average site trends.
- Check that each analyst's results can be reproduced by one other person for two species.
- Flag species where the trend changes sign or the CI shifts a lot between the with-observer and without-observer fits, or between the two B-2021 treatments. Report these as "not robust" in the regional report rather than giving a single number.
- If the board needs site-level figures, take them from the model's site-specific terms. If you do still average site trends, use inverse-variance weights (or a random-effects meta-analysis), not a plain mean, and only for species with at least three sites.

## What I'd say to the board

Seven seasons of single-visit point counts is a short, noisy series. Report trends with intervals and a robustness flag, and say explicitly that observer rotation was a design confound that the model corrects for. That is easier to defend than a plain average.

## Assumptions I made

- Transect 7 is a typo, or at least needs checking. I didn't assume which way it resolves.
- The analysts have similar skills and can all use the same software (R or Python).
- Site sizes are roughly as the transect ranges imply; I haven't seen the data.

If you can confirm the transect 7 question and agree to the shared crosswalk, I can draft the model specification and the hand-back template for Wednesday.
