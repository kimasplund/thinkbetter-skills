Short version: split the data preparation by site, but do not split the trend modelling by site. Four independent site fits would build two of your data problems straight into the regional numbers. Here is a plan that still gives each analyst a site and still lets you start Wednesday.

## Why a pure one-site-per-analyst split is risky

1. **Observer and period are confounded within every site.** At each site one observer covers 2019-2021 and the other covers 2022-2025. Inside a single site, "Mara vs Tobiah" is the same thing as "before vs after 2022", so no site-level model can separate an observer effect from a real change. Mara records more quiet, high-pitched species, so a step at 2022 will show up as a fake trend. It will point down at A and B (Mara to Tobiah) and up at C and D (Tobiah to Mara). Averaging the four trends may hide this for some species, but not reliably. The observer effect can only be estimated across sites, because the two site groups swap observers in opposite directions. That needs one model that sees all four sites.
2. **The missing Site B 2021 fill depends on Site C.** The protocol ratio uses C in the same year, so B's analyst cannot do it alone. Filling also makes the data look more complete than it is, which understates uncertainty in B's trends.
3. **The marsh tit-wren split affects D differently from the rest.** From 2023 D has reed and sedge tit-wren, while A, B and C still log "marsh tit-wren". If D is analysed as-is, those two species have short series and no pre-2023 data. The other sites would produce a marsh tit-wren trend that D can't contribute to.
4. **Transect 7 appears in both A and B** (A is 1-7, B is 7-12). Either it is a typo, for example B should be 8-12, or transect 7 is genuinely counted twice. This is a double-count if it is real.
5. **Simple averaging of four site trends** gives each site equal weight even though they have different numbers of transects (A 7, B 6 with the overlap, C 5, D 5, or 70, 60, 50 and 50 points). It also ignores each site's uncertainty.

## Resolve these before Wednesday (you, about an hour)

- **Transect 7:** decide which site owns it. If both really surveyed it, say so and keep one copy. Check the spreadsheets for duplicated rows.
- **Observer:** confirm each spreadsheet has an observer column. If it doesn't, add one now from your 2019-2025 assignment (Mara A/B 2019-21, C/D 2022-25; Tobiah the reverse).
- **Tit-wren rule:** choose one of these. (a) Fold reed and sedge tit-wren back into "marsh tit-wren" for 2023-2025 at Site D, so all four sites and all years share one code. This is the usual choice for a 2019-2025 trend. (b) Keep the new species for 2023 onwards as a short separate series. I'd do (a) for the headline trend and (b) as a note. Don't reassign old marsh tit-wren records to the new species.
- **Site B 2021:** decide whether you follow the written protocol or treat 2021 as missing. Treating B 2021 as a gap in the model is statistically cleaner, and the protocol fill can be reported as a sensitivity check. If the board requires the protocol, the fill is done once, centrally, by you or one analyst, after C is cleaned (see step 2).
- **Common format:** give everyone the same column names, species code list, the year coding, and a fixed trend definition (for example, a log-linear trend per year in counts per point, with a set model family).

## What each analyst does (Wednesday to Friday)

Each analyst takes one site (A, B, C or D) and:

1. Cleans their site's spreadsheet to the common format. They check for duplicates, impossible values, missing points and species codes against the agreed list.
2. Applies the tit-wren rule (analyst D only).
3. Produces a **count table**: site, transect, point, year, observer, species, count, with a zero for every point-year where the species was not recorded. Zeros matter for trends.
4. Fits a **site-only trend as a check** (not the regional figure): per-species slope, standard error and number of non-zero point-years. The analyst notes that observer and the 2022 step can't be separated here.
5. Writes a short **data note**: species with too few detections to model, odd records, and anything that didn't match the plan.

What they hand back: the cleaned count table (one file in the common format), the per-species site check table, and the data note. Analyst B also reports 2021 as missing and does not fill it. Analyst C hands over final C counts first, since a protocol fill for B needs them.

## How you combine it (Monday onward)

1. **Stack the four count tables** and check row counts per site-year against what you expect (B 2021 absent).
2. **Fit one regional model per species** on all the data, with a year trend, a site effect (and site-by-year or random effects), and an observer effect. The observer effect is identifiable because the site groups swap in opposite directions. Use point or transect as a random effect for repeat counts. The regional trend is the year effect from this model, weighted by sites' sizes.
3. **Handle B 2021:** the model simply has no data there. If the protocol fill is mandatory, run a second version with the filled values and report the difference.
4. **Compare** the regional trend with the simple average of the four site-only slopes. Where they differ a lot, the observer step is probably the cause, and the pooled model is the one to report.
5. **Species flagged as observer-sensitive** (quiet, high-pitched ones) should get a caveat in the report, and their observer-adjusted trends deserve a second look. The observer effect is identified from only two observers, so treat it as an estimate with real uncertainty.
6. **Report** regional trends with confidence intervals, not point values alone. State the observer adjustment, the tit-wren handling and the B 2021 gap in the methods.

If you can't get a pooled model fitted in time, the fallback is to average the site slopes weighted by inverse variance (or at least by number of points), say clearly in the report that the figures are not corrected for the 2022 observer swap, and avoid reporting quiet-species trends as firm.

## Rough timeline

- Tuesday: you settle transect 7, observer column, tit-wren rule and B 2021 treatment, and send the common format to the analysts.
- Wednesday to Friday: analysts clean and return their files, C first.
- Following Monday to Wednesday: you or one analyst stacks and fits the pooled models.
- Remainder of the month: checks, write-up and board review.

A few assumptions I made: the spreadsheets have identical columns, but I don't know whether they include an observer field, so I've asked for it. I've also assumed "transects 7-12" for B is correct as written until you confirm.
