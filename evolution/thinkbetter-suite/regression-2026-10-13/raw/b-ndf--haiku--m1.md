# Recommended Agreement: Q3 Roadmap (Tech Debt, Sales Features, Cloud Spend)

**Assumptions:** I don't know the size of the debt backlog, the effort for each of the three features, or how much of the cloud bill can be cut without re-architecture. I've assumed Engineering has roughly one quarter of its capacity to allocate and that the 15% cloud target is a finance number that can be met partly without feature-level engineering time. Check these before you take the plan to the VPs.

## Stakeholder Landscape

| Stakeholder | Interest | Power | Support level needed |
|-------------|----------|-------|----------------------|
| Engineering VP | Debt stops slowing every future release; fewer reliability incidents | High (controls capacity) | Endorse |
| Sales VP | Three customer-requested features that protect or win named deals | High (revenue, customer relationships) | Accept at minimum |
| Finance VP | 15% cloud cut, predictable spend trend | High (budget, can block) | Accept at minimum |

Underlying interests:
- Engineering needs the debt not to make next quarter's work slower. Debt that makes cloud costs high is the same debt that makes features slow.
- Sales needs specific accounts kept or won. It probably doesn't need all three features in Q3.
- Finance needs the spend trend to bend by a date. It doesn't need the savings to come from Q3 feature time.

## Zones of Agreement

- All three want the company to hit its annual targets without a reliability or cost surprise.
- All three will accept a plan that is funded and dated, rather than one that gets re-argued every month.
- Cloud cost and tech debt overlap. Old instance types, unused services and inefficient queries are both debt and cost. This is the most useful finding here: part of the finance target is the debt work.

## Conflicts Addressed

| Conflict | Type | Resolution |
|----------|------|------------|
| Engineering debt vs. sales features for the same engineers | Resource | Split capacity and sequence debt that unblocks the committed features first |
| Finance 15% target vs. engineering time | Interest (partly false) | Treat the cheapest savings (rightsizing, commitment purchases, deleting unused resources) as a small, separate cost effort that needs little feature time |
| Sales wants all three features now | Resource | Commit two features for Q3; put the third on a conditional Q4 slot with a named trigger |

## Proposed Agreement

**Q3 split (about 75% of Engineering's capacity for the plan):**
1. **Cloud cost sprint, weeks 1 to 6:** two engineers plus a finance partner. Rightsize the top cost drivers, buy commitments, remove unused resources, and fix the five most expensive inefficiencies. Target: a committed run-rate reduction of 15% by end of Q3, with the full effect visible on the bill by end of Q4 if it lands late.
2. **Debt work scoped to the committed features and the costliest services:** only the parts that either unblock feature 1 or 2 or are among the top cost drivers. The rest waits.
3. **Sales features 1 and 2:** committed for Q3.
4. **Sales feature 3:** conditional Q4 slot. It moves in automatically if features 1 and 2 are on time, or earlier if the named account signs.
5. **Remaining capacity (about 25%):** standing allocation to debt in Q4, so the debt problem has a funded owner after this quarter.

### Value Distribution

| Stakeholder | What they get | What they give |
|-------------|---------------|----------------|
| Engineering | Debt work funded and scoped; cost sprint counted as debt work; Q4 allocation | Full debt backlog waits; some debt stays unfixed in Q3 |
| Sales | Two of three features committed for Q3; third date fixed, not open-ended | Third feature moves to Q4 by default |
| Finance | A dated 15% run-rate target with a named owner and monthly visibility | Accepts that part of the saving lands in Q4 and that feature time is shared |

## Commitments and Conditions

- **Finance milestone:** if the cost sprint has cut at least 8% by mid-quarter, Finance accepts the full-year 15% target as on track, even if the last points land in Q4.
- **Feature slip rule:** if feature 1 or 2 slips more than two weeks, feature 3 moves out of the Q4 slot automatically. No re-argument needed.
- **Review point:** 30 minutes monthly, with the three VPs and one named owner from each team. Decisions are made against the written agreement.
- **Disputes:** any VP can escalate once, in writing, to the COO or CEO with a one-page case. Until a decision comes back, the agreed split stands.

## Implementation Notes

- Get each VP to sign a one-page version of the agreement. The signature matters more than the wording.
- Name one owner for the cost sprint who reports to the Finance VP, not to Engineering. This keeps the savings from being quietly reabsorbed into feature work.
- Publish the cost numbers from the first week. Visible progress is what keeps Finance from pushing for more Engineering time.
- Ask each VP, before the meeting, what would make them say no. Address those points in the document, not in the room.

## Risks to the Agreement

- **Sales reopens feature 3** when a deal stalls. Mitigation: the trigger is written down, and the named account has a documented path.
- **Finance counts Q3 spend** before savings land and asks for more cuts. Mitigation: report the run-rate, not the monthly bill, and show the Q4 trajectory.
- **Engineering under-delivers the debt part** because the cost sprint absorbs more time than planned. Mitigation: cap the cost sprint at two engineers and require the review point to report both tracks.
