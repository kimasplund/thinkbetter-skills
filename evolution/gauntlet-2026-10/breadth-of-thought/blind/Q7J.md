The full buy is not the only way to cover 14 months. Several of your other facts (the 1,900 trade-ins, Brisk's stock, hill-hold being a 6% feature, and Tarrow being a shared supplier) are also sources of supply or ways to need fewer chips. Below is the menu, then how I'd combine the options.

## Working numbers and assumptions

- You build about 333 bikes a month, so 7 months of stock is roughly 2,300 boards.
- I'm assuming the €1.9M quote covers the whole 14 months of production, about 4,700 boards or roughly €400 each. You already hold 7 months of that, so the real shortfall is about 7 months, or roughly €950k. That is not far above your €700k. Please confirm this reading with Velan or Tarrow, because it changes the whole conversation. If the €1.9M is only the shortfall, the picture is much tighter.
- I'm assuming the 14 months starts now and has no slack. Redesigns of this kind slip, so any plan should survive a 3 to 4 month slip.
- Your installed base is roughly 25,000 bikes built since 2019, all on this one board. Replacement boards for repairs and warranty are a separate demand that the 14-month figure probably doesn't include. Whichever route you take, decide how many boards to ring-fence for service.

## The options

**1. Don't wait for hill-hold: ship the new controller without it, and keep old boards for bikes that need it**
Hill-hold is the only reason the redesign takes 14 months instead of about 7. The firmware port to the Corwen M7 takes 4 months and EMC takes 3. The 7-month sensor design is what stretches the schedule, and the feature is used on about 6% of rides, almost all on retail bikes.
- Build the M7 board without hill-hold, aiming at the 60% of volume that goes to fleets, in about 7 to 8 months.
- Keep VX-41 boards for retail bikes only (about 40% of volume) until the sensor is ready.
- Effect on supply: 8 months at full consumption, then 6 months at 40%, comes to about 10.4 months of boards. You hold 7, so the gap is about 3.4 months, or roughly 1,100 boards. At about €400 each that is about €450k, which fits inside your €700k.
- The cost: fleet customers lose a feature, and hill-hold bikes would run a mixed fleet for a while. Check three things:
  - whether any lease contracts or tenders specify hill-hold;
  - whether the 7-month sensor design can run alongside the M7 launch and reach retail later;
  - whether EMC can start on a board that is not final.
- Risk: the 7-to-8 month date is now the critical path. A slip eats the margin quickly.

**2. Replace the missing timer instead of designing a new sensor**
The 7 months comes from needing a sensor for a feature that relies on a timer only the VX-41 has. Ask the electronics team three questions:
- Can a small companion chip (a cheap timer or logic device) on the M7 board provide the missing function?
- Can hill-hold be done in software from the motor position signals you already have?
- Is a degraded version, such as a brake-assisted hold, good enough?

I can't tell you from here whether any of these work. Each one could cut months from the schedule and would shrink every other number in this memo. Ask for a one-week answer before the board meets.

**3. Harvest the 1,900 trade-in bikes**
Every model since 2019 uses the same board, so each trade-in is a potential VX-41 board. 1,900 boards is about 5.7 months of production, worth roughly €750k at your implied unit cost, and you're currently selling them for scrap.
- Realistically a share will fail testing or have a firmware-incompatible revision. At 70% usable you get about 1,300 boards, or 4 months.
- You'd need a bench test and refurbishment step, some labour, and a decision on whether refurbished boards go into new bikes, into service stock, or both. Your own quality and warranty policy decides this, and the safer starting use is service spares.
- The trade-in scheme keeps adding bikes, so supply continues.
- Trade-off: resale of whole refurbished bikes would bring in cash, but each bike can only be one or the other.
- Do this now: strip and test 30 boards this week.

**4. Buy Brisk Motion's stock at the administrator's auction**
Brisk bought its controllers from Tarrow, the same contract manufacturer as you. If those boards used the VX-41, or a board you could rework or reflash, the auction could supply boards or loose chips quickly and cheaply, and administrators sell fast.
- Ask the administrator for the lot list now, and ask Tarrow what was in Brisk's boards and whether they match yours. Tarrow may also hold Brisk-related stock or orders.
- Get the board to approve a bid ceiling in advance, because the auction is next month and your meeting is in three weeks.
- Check:
  - authenticity and storage condition of any chips;
  - whether firmware or board revision differs from yours;
  - whether buying from an administrator carries restrictions.
- Treat it as upside only until you know what the lots are.

**5. Partial last-time buy with the €700k**
At about €400 a board, €700k buys roughly 1,750 boards, or about 5 months. That takes you to roughly 12 months of cover, 2 months short of the plan and without slack on its own.
- It works well as the base layer for options 1, 3 and 4 and is the one decision with a hard deadline (ten weeks).
- The risk is committing the whole sum before you know what options 2 to 4 deliver. Consider ordering in tranches if Velan allows, or placing the first order at the deadline once the facts are in.

**6. Change how you pay for the last-time buy, not only how much you buy**
You can't borrow from the bank, but cash is not the only lever.
- Ask Velan or Tarrow for staged deliveries with payment on shipment, or for Tarrow to buy and hold the chips and invoice you on call-off. Chip makers often prefer a smaller up-front commitment to losing the order.
- Ask your fleet customers whether they would prepay or co-fund a part of the supply, since it protects their deliveries.
- Look at non-bank finance secured on your lease book or your stock, such as receivables financing, sale and leaseback of leased bikes, or inventory finance.
- Existing shareholders, or an investor who wants to bridge 14 months, are another route. A grant for the redesign is a long shot but worth a call.

**7. Allocate boards deliberately between customers and models**
If supply is going to be tight under any plan, decide in advance who gets the boards: lease contracts with penalties first, or the higher-margin models first. A wrong allocation costs more than any one purchase. I'd want your margin by channel to advise on this.

**8. Look for other sources and a second life for the part**
- Ask Velan whether a recommended replacement part exists with a compatible timer. End-of-life notices often name one, and the team may not have been told.
- Ask independent distributors about VX-41 stock. Buy only from traceable sources, because counterfeit chips are a real risk after an end-of-life notice.
- Ask Tarrow whether other customers hold unused last-time-buy allocations.

**9. Add engineering capacity to shorten the redesign**
Hire contractors or have Tarrow take on part of the board work. If the 4-month port or the 3-month EMC shortens by even a month or two, you need correspondingly less stock. Partial effect only, as certification times don't compress easily.

**10. Reduce demand for boards**
Slow retail builds, or build to order only, for a few months. This protects cash and stock but costs revenue, and it only makes sense for the lowest-margin lines. I'd keep it as a last resort.

## How I'd combine them

The options differ in cost, speed and risk, so I'd present the board with a plan rather than one pick.

| Plan | What it does | Boards covered | Cash needed | Main risk |
|---|---|---|---|---|
| A. Minimum | Option 5 only (partial LTB) | about 12 months | €700k | 2 months short, and no spare margin if the schedule slips |
| B. Recommended | Option 1 + a reduced LTB (about €450k to €550k) + option 3 for service stock | about 10.4 months needed vs about 12 to 14 months available | €450k to €700k | Fleet customers lose hill-hold for a time; 8-month date on the critical path |
| C. B plus upside | B + option 4 (if Brisk's lots fit) + option 2 | more cover and possibly an earlier full launch | B plus bid budget | Depends on what the auction contains and on the electronics team's answer |

## What I'd do before the board meets (three weeks)

1. Confirm what the €1.9M covers, and ask Velan for call-off or staged terms.
2. Ask the electronics team: can hill-hold be dropped from the first release, can it be replaced by a companion chip or software, and can EMC start earlier?
3. Test 30 boards from the trade-in stock for yield and compatibility.
4. Get Brisk's lot list and Tarrow's view on compatibility.
5. Check the lease contracts for any hill-hold commitment.
6. Get a number for service-spare demand over the next 3 years.

I'd put the choice to the board as "which plan, and what bid ceiling for the auction" rather than "how much can we afford". With the hill-hold decoupling, your €700k probably covers the gap, and the harvest and the auction act as insurance if the redesign slips.
