**Recommendation: Tarnwell Continuity (the 200 km standby), subject to three checks before January.** Two of the other options fail the 8-hour target on the numbers you gave, and a third fails the flood scenario.

**Why the others don't work**

- **Nimbara (cloud replica) fails on restore time.** Keeping the replica in step is easy. 150 GB/day averages about 14 Mbps, so the 2 Gbps line is plenty for that. The restore is the problem. Pulling 420 TB back over 2 Gbps takes about 19 days at full line rate, and the line moves only about 14 TB in 8 hours. A cloud copy is also only storage. Brisewood supports its software only on its own certified appliances, so you can't run the archive in Nimbara's cloud. After a disaster you would still need to buy and install matching appliances and then reload the data. The cost is attractive, but this option doesn't meet the requirement. It would also take 3 to 5 weeks just to seed the first copy.
- **St Brennan's (3 km) fails on correlated risk.** It is on the same river, and both sites ran on generators for four days after the Wharf Road substation flooded in 2024. A flood or a regional power loss would very likely take out both sites together, which is the scenario the board is worried about. It also costs the most up front and adds a building and a team to run. It would protect you against a fire in your own data centre, but not against the flood. The facilities team's wish to control it is understandable, but it isn't a reason to choose it.
- **Weekly offsite tapes fail on recovery time and data loss.** You could lose up to a week of studies, and restoring 420 TB from tape takes days to weeks, not hours. It does give you a cheap last-resort copy.

**Why Tarnwell fits**

- 200 km is far enough to be outside the river, the substation and probably the regional weather event.
- The standby servers are already running and synchronised, so failover can be measured in hours. This is the only option that can realistically meet the 8-hour target.
- Cost is €360k x 5 = €1.8M, inside the €2M ceiling.

**Check these before committing (I've had to assume some of them)**

1. **Brisewood support.** Get written confirmation that Brisewood certifies and supports the Tarnwell standby set-up. That means either Brisewood-certified appliances at Tarnwell, or an arrangement Brisewood signs off on. Without this, the standby could be unsupported at the moment you need it.
2. **How radiologists actually reach it.** Your 2 Gbps line is in the building that has flooded. Ask for a second route, such as a different carrier or a link from a clinical site that is still working, so radiologists can connect to Tarnwell. Include PACS access from workstations, modality routing and the RIS and EHR integrations in the plan.
3. **Failover scope and an actual test.** Write the 8 hours into the contract as a recovery-time commitment, and agree on what "working" means. Test a full failover at least once a year, and once before go-live. Also confirm that new studies from modalities can be received at Tarnwell during an outage, and that you can fail back afterwards.

**Budget and extras**

- The first sync of 420 TB will take roughly 3 to 5 weeks over the line, so ask Tarnwell about a shipped-disk seed. Throttle the sync so it doesn't hurt clinical traffic.
- Tarnwell's €1.8M leaves about €200k for the second network route, testing and contingency. That is tight. Check whether the €360k is fixed, or whether it rises as the archive grows (150 GB a day adds roughly 55 TB a year, or about 275 TB over five years).
- Replication copies mistakes and ransomware as faithfully as good data. Keep your nightly tapes. If you can afford the €30k a year for weekly offsite tapes, add them as a cheap protection against ransomware. That would bring the total to about €1.95M, so negotiate the Tarnwell price first.

**What to tell the board:** Tarnwell is the only option that meets the 8-hour target and survives a flood that takes out the local area. The cloud option's restore time is measured in weeks, and St Brennan's shares the same flood and power risk. The recommendation depends on Brisewood's written support, a working second network route and a tested failover.
