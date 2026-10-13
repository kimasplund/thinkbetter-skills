**Recommendation: take the Tarnwell standby site (€360k a year, about €1.8M over five years), and keep the existing tape routine.** It is the only option that is far enough away to survive the same event as your data centre and can plausibly meet the 8-hour target.

**Why the others fail**

- **Nimbara Cloud:** Replication is easy. 150 GB a day is only about 14 Mbps, so the 2 Gbps line is plenty for that, which is what Nimbara's claim covers. Getting data back is the problem. 2 Gbps is roughly 20 TB a day at best, so pulling 420 TB home takes about three weeks. Even restoring only the last two years of studies (about 110 TB) takes around 5 hours of pure transfer, before anything is running. Brisewood won't support its software on anything except its own certified appliances, so after a loss you would also have to buy and install matched servers to restore onto. The €110k a year is cheap because it doesn't buy a working service within 8 hours.
- **St Brennan's plant room:** It is the best-controlled option, but it shares the river and the Wharf Road substation with you. In 2024 both hospitals ran on generators for four days. A flood that takes out your basement is the scenario most likely to affect them too, so you would pay €1.1M up front plus €70k a year (about €1.45M over five years) for a site that may fail at the same moment. A fire in your building would be covered, but the flood case would not. You would also still have to buy and certify a matched Brisewood appliance set, and I can't tell from your figures whether the €1.1M includes that.
- **Weekly offsite tapes:** Up to a week of studies could be lost. Rebuilding on new certified hardware and reading back 420 TB from tape takes days to weeks, not 8 hours. Keep tapes only as the last-resort copy.

**Why Tarnwell works:** 200 km puts it in a different flood and power zone, and a standby kept in sync means radiologists reach prior scans without a restore step. Sync traffic is about 14 Mbps, so your line is not the constraint. The cost leaves about €200k of headroom in the €2M budget.

**Steps before the January recommendation**

1. Get written confirmation from Brisewood that the standby hardware Tarnwell will run is certified and supported, and ask who owns that licence and support cost.
2. Get Tarnwell to price capacity growth. The archive will pass 650 TB by year five (420 TB plus roughly 275 TB of new studies). If €360k a year only covers today's size, the total could exceed the €2M budget.
3. Get Tarnwell's contract commitments in writing for failover time, the sync lag it guarantees, and the penalty if it is missed.
4. Plan how radiologists reach the standby when you fail over. Find out whether your hospital's network will still be up if only the basement is lost, and whether you need a second internet link. A flooded basement could also take the line with it.
5. Rehearse a full failover, with radiologists actually opening prior studies, before signing off. Repeat it every year.

**Assumptions that matter, and the cheapest check for each**

- Tarnwell can host Brisewood-certified appliances. If Brisewood refuses, this option fails, and the fallback is a sister-site build with a certified set. Check by asking Brisewood this week.
- €360k a year includes growth. If it doesn't, the budget breaks. Check with a written quote at 700 TB.
- Your own network and power would remain up after a basement loss. If they wouldn't, add a second link at the clinical end. Check with your network team and a look at where the line enters the building.
- The 8 hours is measured from loss of the site to radiologists reading with priors. If the board means full restoration of everything, the target changes, but the ranking doesn't.

I'm fairly confident in this ranking. The deciding unknown is whether Brisewood will certify Tarnwell's hosting.
