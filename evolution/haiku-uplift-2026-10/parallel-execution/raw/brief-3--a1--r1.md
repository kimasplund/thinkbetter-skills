Here is a plan for splitting the work across the four analysts, with some problems in the current setup that I'd fix before Wednesday. I've made the assumptions stated below where your message was unclear.

**Problems to resolve first**

1. **Transect overlap.** Site A covers transects 1-7 and Site B covers 7-12, so transect 7 appears in both. Please confirm which site owns transect 7. Until then, the analysts may double count it. I've assumed it belongs to A.

2. **Observer confounding.** Mara and Tobiah swapped sites in 2022. Any difference between sites that changes over time is partly an observer effect. For example, Sites A and B changed observers in 2022, which means their 2022-2025 trends include an observer change. Mara also records more of the quiet, high-pitched species, so for those species the observer change alone can produce a spurious trend. Each analyst's model should include an observer term (or the data should be split by observer period), and the species most affected are the quiet, high-pitched ones. Without this, averaging four site trends will not give a clean regional trend.

3. **Tit-wren code split.** Site D logs reed and sedge tit-wrens from 2023 onward. Sites A, B and C still log "marsh tit-wren". You cannot split the old records into reed and sedge, so the cleanest fix is to combine reed, sedge and marsh tit-wren into one "marsh tit-wren complex" for all years. Use that combined group for every site and year. Otherwise, Site D's trend will show an artificial drop in marsh tit-wren from 2023 that is really a relabelling.

4. **Missing Site B data in 2021.** The protocol fills it with the ratio to Site C in the same year. That is fine as a rule, but it makes Site B's 2021 value depend on Site C's 2021 counts, and Site C in 2021 was also surveyed by Tobiah while Mara covered A and B. Please have the analyst for Site B record that the 2021 value is imputed, and check whether the imputation should be excluded from the trend fit. A more conservative choice is to treat 2021 as missing for Site B and let the model handle the gap.

**What each analyst does**

Each analyst takes one site, using the site's own spreadsheet:

- Standardise the species names, applying the tit-wren complex rule above.
- Add an observer column and a season column, then check the observer assignment against the rules in your message.
- For Site B only, apply the 2021 rule and flag the imputed rows.
- Fit one trend model per species at the site. Use a consistent model across all four analysts, including the observer term.
- Hand back: a table with one row per species giving the trend estimate, its standard error or confidence interval, the number of seasons with data, the number of count points, and any species the model could not fit (too few detections). Also hand back a short note on any data problems found, and the list of flagged or imputed rows.

**How you combine them**

- Average the four site trends. Consider weighting by the number of transects, since Site A has 7 transects, Site B has 6, Site C has 5 and Site D has 5. An unweighted mean gives each site equal say. Either choice is defensible, but state which one you used.
- Report species that were not fitted at one or more sites as missing from the regional figure, not as zero.
- Include the uncertainty. Combine the site standard errors rather than reporting only the mean of the point estimates.
- Show a sensitivity check that excludes the imputed Site B 2021 value and, separately, drops the observer term, so the board can see how much the conclusions depend on these choices.

**Before Wednesday**

Please confirm the transect 7 ownership and the tit-wren complex rule, since the analysts will need both to start. Once those are set, the four site tasks are independent and can run in parallel.
