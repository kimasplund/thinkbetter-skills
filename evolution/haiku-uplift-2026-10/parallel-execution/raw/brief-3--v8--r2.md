The split can work, but as described it has three dependencies and confounds that would bias the regional figure, so I would fix them before Wednesday. I have assumed the four spreadsheets have the same layout and that the trend model is the same at every site.

**1. Site B's 2021 gap depends on Site C.**
The protocol fills B-2021 using the B-to-C ratio for that year. The B analyst therefore cannot finish 2021 until Site C's 2021 counts are in.
- Site C's analyst hands over the 2021 totals first, or you compute the fill ratio centrally and give it to the B analyst.
- Record the fill in the output as imputed, so it is visible in the trend.

**2. Observer is confounded with site and period.**
Mara covered A and B in 2019–2021 and C and D in 2022–2025. Tobiah did the reverse. Each site therefore has one observer change, in 2022, and the direction is opposite at A/B and C/D. Mara also records more of the quiet, high-pitched species.
- A separate site fit will read the 2022 observer change as a trend step, especially for those quiet species.
- Fit one pooled model across all four sites with site-by-year effects and an observer term. The opposite switch directions let the pooled model separate observer from trend. A single-site model cannot.
- If the team must fit per site, every site model needs the same observer term, and the analysts should flag quiet-species results for review.

**3. The marsh tit-wren split is not comparable across sites.**
From 2023, Site D logs reed and sedge tit-wren. Sites A, B and C still log marsh tit-wren. A, B and C cannot be split after 2023, so their series and D's series do not measure the same thing.
- Decide the mapping before the split. The simplest option is to analyse a combined "tit-wren complex" (reed + sedge + marsh) at all four sites for all years.
- If you need the separate species, report them only for Site D from 2023 onward and say so.

**Combining the results.**
- Averaging four site trends gives each site equal weight. Site transect counts differ (A has 7, B has 6, C has 5, D has 5), so the weighting is a choice you should make and state.
- Average slopes on the log scale, not abundances. The regional confidence interval should come from the pooled model or from the between-site variance, not from a simple mean of the site intervals.

**What each analyst hands back.**
A single table per species and site with: year, count total, transect-point count, fitted slope, standard error, 95% interval, model formula, observer term used, and any imputed or remapped values. Add a short list of data issues they found.

**Before Wednesday (about one hour of your time):**
- Agree the tit-wren mapping.
- Agree the model formula, including the observer term.
- Send Site C's 2021 totals to the Site B analyst.
- Give everyone the same output template.

Then analysts can start Wednesday on their site, and the pooled model can run as a check on the averaged figure.
