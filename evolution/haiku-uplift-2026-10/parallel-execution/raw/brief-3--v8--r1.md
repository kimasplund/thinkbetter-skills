Splitting by site works for the bulk of the job, since each site is its own spreadsheet with identical columns and the four fits don't depend on each other. But three things in the data would bias the regional figure if the analysts start on Wednesday as planned. I'd settle them first, in a short shared step, and then fan out.

**1. Fix the three data problems before anyone fits a model (one person, about a day)**

- **Observer change in 2022.** Mara and Tobiah swapped sites in 2022, so every site has an observer change in the same year. Within one site, a trend line can't separate "the population changed" from "a different person counted." Mara records more of the quiet, high-pitched species, so those species will show a 2022 step at A and B in one direction and at C and D in the other. Averaging the four site trends won't cancel that cleanly, because the effect differs by species and by how many transects each site has. The fix is to fit one regional model per species with an observer term (Mara or Tobiah, per count), using all four sites together. If you want per-site figures for the report, make the observer term part of each site model as well. Per-site fits without an observer term are not safe for the quiet species.
- **Marsh tit-wren split.** Site D logs reed or sedge tit-wren from 2023 onward. A, B and C still log "marsh tit-wren." If you fit each site separately, D will show a break that is really a relabelling. Decide now how the old code is handled. The cleanest option is to combine reed, sedge and marsh tit-wren into one "tit-wren complex" for the whole series, and report the split only where the data supports it. Don't let each analyst choose.
- **Site B in 2021.** The protocol fills B's 2021 count from Site C's ratio. That makes B's 2021 value partly a copy of C, so B and C are no longer independent, and the fill sits inside the trend. Either (a) fit B with 2021 treated as missing, which a count model handles without any fill, or (b) use the fill but flag the B-2021 row and run a sensitivity check without it. I'd do (a) for the main figure. The protocol may need a note either way.

**2. Analyst briefs (after step 1)**

Each analyst gets the same spec:
- Input: their site's spreadsheet, plus the harmonised species list and the observer column from step 1.
- Fit one trend model per species, using the same model form for all four sites (state the form in the brief, e.g. a Poisson or negative-binomial count model with a season term, and count points or transects as the offset).
- Species with too few detections to fit: report "insufficient data" with the count, not an estimate.
- Hand back, per species: the trend estimate, its standard error or 95% interval, the number of seasons with detections, and any species they had to drop. Also hand back the fitted model code and the exact input file version used.
- Don't change the codes or the observer handling locally. If they think a rule is wrong, they flag it to you.

**3. How you combine it**

- Don't average the four site trends with equal weight. Site A has 7 transects, B 6, C 5 and D 5. Weight each site by its transect count, or better, fit the single regional model in step 1 and use the site fits only as checks.
- Use the regional model as the headline figure. The average of site trends is a useful cross-check; if the two disagree for a species, look at that species before publishing.
- Check the pooled result against the raw counts per season for each species, since a trend can look smooth in a model and still come from a few lucky seasons.

**Assumptions I made**

- The point counts are on the same 10-point transects each year and the offset is the number of points surveyed.
- Mara's and Tobiah's records are identifiable per count row. If they aren't, the observer fix in step 1 has to be done from the field sheets.
- You can afford about a day of setup before the analysts start, so the Wednesday start is still realistic if step 1 is done Monday or Tuesday.
