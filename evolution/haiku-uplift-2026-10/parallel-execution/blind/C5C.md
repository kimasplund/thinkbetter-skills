Splitting the trend work by site is workable, but I would not start the four analysts on Wednesday until a few data problems are settled. Each one would otherwise produce a trend that looks clean and is biased in a way the average cannot fix.

**Problems to resolve first (these affect every site)**

1. **Transect 7 is listed in both Site A (1–7) and Site B (7–12).** Confirm which site owns transect 7 in each season, and whether its records are duplicated across the two spreadsheets. If they are, counting it twice will inflate those sites.

2. **Observer changed at the same time as the site assignment.** Mara and Tobiah swapped Sites A/B against C/D in 2022. Any A-versus-C or B-versus-D comparison is therefore confounded with observer. Mara records more quiet, high-pitched species, so a site-level trend can shift in 2022 just because the observer changed. Before fitting, include observer as a covariate (or use observer-year effects), or at least check whether a 2022 step appears at each site.

3. **Marsh tit-wren split in 2023.** Site D logs reed or sedge tit-wren from 2023, while A, B and C still log "marsh tit-wren". Fitted separately, Site D's reed and sedge series will look like new species starting in 2023, and A–C's marsh tit-wren will look like a decline. Agree on one mapping before anyone fits: either combine marsh + reed + sedge into a single "tit-wren complex" for all sites and years, or use the new codes everywhere with the old code treated as unknown for 2023 onward. Do not let each analyst decide.

4. **Site B 2021 is imputed from Site C.** The protocol fills B's 2021 count from C's ratio in that year. That value is not an independent observation, so it should not enter a trend as if it were. Either exclude B 2021 from the fit or flag it, and in both cases state the choice in the report. Note that the imputed value also ties B's trend to C's.

**Proposed split**

- **Before Wednesday:** you (or one analyst) write one shared specification and one shared script. The spec covers the species list and codes, the mapping above, the observer covariate, the treatment of B 2021, the count model (for example a Poisson or negative binomial GLM or GLMM with year as a trend term and a site offset), and the output format. Each analyst should run the same script on their own site, changing only the input file and site ID.
- **Each analyst (one site):** run the shared script, check the per-species fit diagnostics (convergence, overdispersion, zero counts), and hand back a fixed-format table: species, site, year-count, trend estimate, standard error or interval, the number of transect-years used, and any flags (imputed years, observer change, species with too few detections). They should also return a short note listing any species they could not fit and why.
- **You:** stack the four tables, check that every site reports the same species list, and combine the site trends. Plan the regional figure so the method is decided in advance. A simple unweighted mean of the four site trends ignores differences in effort and precision between sites, so consider weighting by inverse variance or fitting one model across all sites with a site-by-year interaction. Report the choice and show the site-level trends next to the regional one, so the board can see whether one site is driving the result.

**Assumptions I made**

- You have counts per point per season, so the model has one row per transect-point-season.
- All four sites have the same species list after the mapping is applied.
- Analysts work from the raw spreadsheets, not a merged file.

If you can confirm the transect 7 assignment, the observer change year, and the tit-wren mapping, I can draft the shared specification and the hand-back template.
