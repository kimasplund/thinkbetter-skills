Notes

- O4M: Covers the review gate, the PWA and Driftwell blockers, stock events, the token issue and stale jobs, all tied to the brief. It says to freeze scope because any later feature costs another review. Its "where this could be wrong" section is precise and names the cheapest checks: ask IT and security this week. No invented facts.
- R4T: Correct and compact, but thinner than the others. It has no conflict handling for jobs reassigned while offline. Its uncertainty handling is a short assumptions list, and "submit by week 3, aim for week 2" leaves the slack loosely defined.
- S0O: Thorough and sound. It has all four design points, a phase-2 path and clear remaining uncertainties. It is longer than needed and restates the deadline logic in a few places.
- G9R: Solid coverage. One slip: it says that if the event work "adds more than a week, it is still the only option that fits", but 3+ weeks of build plus 8 weeks of review reaches or passes 11 weeks. It also points testing toward a week-3 submission, which uses up the slack.
- D9Z: Makes the sharpest point against CRDTs: merge semantics can't enforce a bounded stock count. Good concrete test (a two-day airplane-mode run with two handsets on one van), and it correctly computes a week-15 landing for phase 2. Some claims are stated as certain ("can't go in the managed catalogue", "won't finish in the weeks you have"), and it has no explicit handling of stale or reassigned jobs.
- O0W: Concise and well reasoned. It notes that every option except the PWA is a new app version, that the team's 2-week estimate may not include the token and stock work, and that a review-free server-side path would change the answer. "Lose a week and you miss the season" slightly overstates the risk given about one week of slack.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,O4M,6,6,6,7,5,7,6,43
J-B,R4T,5,5,5,5,6,7,5,38
J-B,S0O,6,6,6,6,4,7,6,41
J-B,G9R,6,6,5,6,5,7,5,40
J-B,D9Z,6,6,6,6,5,7,5,41
J-B,O0W,6,6,6,6,6,7,6,43
```

```ranking
judge,brief,order
J-B,brief-1,O4M O0W S0O D9Z G9R R4T
```
