**Recommendation: take the Tarnwell option, subject to one written confirmation from Brisewood (below).** It is the only option that survives a flood and can plausibly meet the 8-hour target. Over five years it costs about €1.8M, inside the €2M ceiling.

**Why the others fail**

- **Nimbara (€110k a year):** The problem is the restore, not the replication. Keeping the copy in step needs only about 15 Mbps (150 GB a day). Pulling 420 TB back over a 2 Gbps line takes roughly 19 days at full line rate, and longer on a shared line. It also leaves you with nothing to run the archive on, because Brisewood won't support its software on anything except its own certified appliances. Cloud could only work if Brisewood certifies running the archive inside Nimbara, and you have not said it does.
- **St Brennan's (€1.1M plus €70k a year, about €1.45M over five years):** It is cheaper than Tarnwell and you'd control it, but it shares your failure modes. It is 3 km away on the same river, and the 2024 Wharf Road substation flood put both hospitals on generators for four days. A flood that takes the basement could take the plant room, or leave both sites without grid power or road access. It would fix a fire in the building but not the flood the board is worried about.
- **Weekly offsite tapes (€30k a year):** Restoring 420 TB from tape needs replacement certified hardware first, then days of reading. Up to a week of new studies is also lost. This is a backup, not a way to get back to work in 8 hours.

**Steps**

1. Get Brisewood to confirm in writing that its certified appliances can be hosted at Tarnwell as a live standby, and what licence and support terms apply. Brisewood sells the matched appliances and won't support anything else, so this decides whether Tarnwell is possible.
2. Get Tarnwell to commit in the contract to an 8-hour recovery target, with a failover test each year. Also ask who owns the failover decision and the hardware refresh.
3. Plan the initial copy. Sending 420 TB over a shared 2 Gbps line takes about three weeks at best, so seed it with shipped disks or tapes and let the line carry only the daily 150 GB.
4. Design the network for the day the basement is gone. Radiologists, modalities and the PACS viewers need a route to Tarnwell that doesn't depend on the lost building. That means a second carrier path, ideally entering the hospital at a different point, and a plan for where staff work from.
5. Keep the nightly tapes, and consider sending a monthly set offsite for about €5k a year. Replication copies deletions and corruption as faithfully as good data, so the tapes protect against those. That fits in the €200k left under the ceiling.
6. Run a full failover rehearsal before the first winter, and time it against the 8-hour target.

**Assumptions and what would change the answer**

- **Brisewood supports hosting its appliances at Tarnwell.** If it refuses, no outsourced option works, and the fallback is a second certified site you own, away from the river valley, at a cost above Tarnwell's. The check is one email to Brisewood this week.
- **The 8-hour target means usable studies in the viewers, not a complete restore of everything.** If it means everything, confirm that Tarnwell's standby is a full running copy and not a build-on-demand arrangement. The check is to ask Tarnwell for its last failover test time.
- **€360k a year is the all-in price.** Ask whether it includes hardware, bandwidth and support, and whether the price rises with 150 GB a day of growth (about 55 TB a year). If it climbs past roughly €400k a year, you lose the margin for the tape set and extra network path.
- **A second network route into the hospital can be obtained.** If the one line enters through the basement and no alternative exists, Tarnwell holds the data but staff can't reach it. The check is to ask your carrier for the physical route of the line.

The main unknown is Brisewood's answer. If it is yes, I'm confident in Tarnwell, because the alternatives fail on arithmetic or geography.
