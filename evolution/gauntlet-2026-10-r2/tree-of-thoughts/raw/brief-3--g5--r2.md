**Recommendation: take the Tarnwell option, with conditions. Keep your current tapes as a second layer. Don't pick any of the other three as the main answer.**

The requirement that decides this is the 8-hour return to work with prior scans available. Three of your four options can't meet it, and the reasons are mostly in your own background notes.

**Nimbara Cloud (€110k/yr): fails on restore time and on software support**
- Nimbara's "plenty" is true for keeping the replica in step. 150 GB/day is only about 12 Mbps on average. It is not true for restoring.
- 2 Gbps is roughly 250 MB/s, or about 21 TB/day at best. Pulling 420 TB back takes around 20 days, against an 8-hour target. Real-world throughput would be worse.
- The obvious workaround is to run the archive in the cloud. Brisewood supports its software only on its own certified appliances, so you can't do that.
- Even then, you'd have no servers to restore onto until you had bought and certified matched hardware.
- It is the cheapest and the most appealing to the CIO, but it is a backup, not a recovery plan.

**St Brennan's (€1.1M + €70k/yr, about €1.45M over five years): right idea, wrong place**
- It is 3 km away on the same stretch of river, so a flood that takes your basement can plausibly take the sister site too.
- In 2024 both hospitals ran on generators for four days when the Wharf Road substation flooded. A shared power failure is a known event, not a theoretical one.
- The scenario the board is worried about, losing the site to flood, is the one where both sites are most likely to fail together.
- The plant room also needs a matched set of Brisewood appliances. I'm assuming the €1.1M covers that. Please confirm, because it is a large hidden cost if it doesn't.
- Control is a real advantage. It doesn't outweigh the shared risk.

**Weekly offsite tapes (€30k/yr): fails on every measure**
- Restoring 420 TB from tape takes days to weeks, and you'd still need servers to restore onto.
- You'd lose up to a week of studies, which is a patient-safety problem in itself.
- It is useful as a last-resort copy, not as the disaster recovery plan.

**Tarnwell (€360k/yr, about €1.8M over five years): the only option that can meet the target**
- At 200 km it is outside any flood plain or power event that would hit you.
- Standby servers already running and in sync means failover takes hours, not weeks.
- Because Tarnwell hosts the servers, the Brisewood-certified matched set can be satisfied.
- The 2 Gbps line is enough to keep the standby in sync at 150 GB/day.

**Conditions to settle before you sign (all can be done before January)**
1. **Brisewood.** Get written confirmation that Brisewood will certify and support its appliances in Tarnwell's facility, and ask what they charge. Ask whether Brisewood offers its own hosted DR service. If Brisewood won't support it, this option fails too.
2. **Budget.** Five years of Tarnwell is €1.8M of your €2M. That leaves about €200k for the initial seeding, any network upgrade, testing, and appliance purchase or refresh if it is not in the fee. Ask Tarnwell exactly what the €360k includes, and negotiate a multi-year rate.
3. **Initial seeding.** Copying 420 TB over the line takes around 20 days and would saturate it. Ask Tarnwell about shipping disks or seeding from the tapes.
4. **The 8-hour clock, end to end.** The standby site is only part of it. Check that:
   - the modalities, PACS viewers and radiologist workstations can be redirected to Tarnwell;
   - the hospital's network link doesn't depend on the basement data centre;
   - the 2 Gbps line, or a second link, can carry image viewing for all radiologists at once;
   - the DNS and identity systems the archive depends on also exist offsite.
5. **A contractual RTO and a test.** Write the 8-hour recovery time into the contract, and run a full failover test in the first months, then at least annually.
6. **Data protection.** Confirm the data-processing agreement, the country Tarnwell is in, and encryption in transit and at rest. This is patient data.

**Why keep the tapes:** continuous replication copies mistakes and ransomware to the standby as well. You already own the tape library, so the marginal cost is low, and an offline copy protects you from a failure that Tarnwell can't. I would send a set offsite regularly, and I wouldn't call that the DR plan.

**Assumptions:** the figures you gave are all-in, the 2 Gbps line is available for this use, and Tarnwell's facility can host Brisewood's appliances. If Brisewood or Tarnwell can't commit to the 8-hour target in writing, come back to the board with that finding. At that point the most defensible fallback is probably a second site at a greater distance than St Brennan's, not a cheaper option that misses the requirement.
