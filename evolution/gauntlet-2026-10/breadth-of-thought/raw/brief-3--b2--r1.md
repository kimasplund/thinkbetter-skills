**Short version:** you have more levers than the last-time buy, and some of them are probably worth more than the €700k. The two I'd look at first are the 1,900 trade-in bikes sitting in your warehouse and the fact that the firmware port plus certification (about 7 months) is roughly the same length as your board stock (about 7 months).

## The numbers I'm working from

I've made a few assumptions. Please correct them before the board sees this.

- 4,000 bikes a year is about 333 boards a month. Seven months of stock is therefore roughly 2,300 boards.
- I'm treating the €1.9M as roughly €135k per production-month of boards. The 7 months you already hold are separate. The real gap is months 8 to 14, which is about 2,300 more boards. Check whether Velan's quote nets off your existing stock. If it doesn't, the gap costs about €950k, not €1.9M.
- €700k buys roughly 5 months of boards. Stock plus a funded last-time buy gets you to about month 12, so you'd be around 2 months short of 14. That is the problem to solve. It is much smaller than "we can only afford 37% of the buy".

## The full menu

### A. Find boards or chips you aren't counting

1. **Harvest the controller boards from the 1,900 trade-in bikes.** Every model since 2019 uses the same board, so each stripped bike gives you a production-compatible board that you currently scrap. At 333 a month, 1,900 boards is about 5.7 months of production. Even at an 80% yield after testing, it is about 4.5 months. That is about 4.5 months of cover at the cost of labour and testing, against about €600k to buy the same cover.
   - Before counting on it: confirm the board revision and firmware are the same across 2020 to 2023, set up a test and reflow-inspection step, and have quality and warranty sign off on reused boards in new bikes.
   - Ask whether they should go to new builds or to a service-spares reserve. Likely both (see item 9).
   - Stripping batteries and scrapping the rest may be the most expensive habit you have right now. Stop scrapping bikes until the board decision is made.
2. **Ask Tarrow Electronics directly.** They build your controllers and built Brisk's. They may hold VX-41 stock or unallocated Brisk work-in-progress. Brisk's administration may have left them with parts and an unpaid order book. They also see Velan's allocation across all their customers, so ask whether they are doing their own last-time buy and whether you can pool volumes.
3. **Bid at the Brisk auction, with a ceiling set in advance.** The auction is next month and the board meets in three weeks, so you need a pre-authorised limit or delegated authority. Ask the administrator for the lot list now. You're looking for VX-41 chips on reels, populated Tarrow boards that use the same MCU, or Brisk's finished bikes. Brisk's boards may well be a different design, so don't assume they are drop-in. If they use the VX-41 you can desolder or rework the chips. This costs little to check and has some upside.
4. **Independent distributors and brokers.** Counterfeit risk is real on an end-of-life part. Only consider authorised or franchised stock, with traceability and incoming inspection. Treat this as a top-up and not a plan.
5. **Ask Velan what they will actually do.** Ask for a recommended successor part, a pin- or footprint-compatible alternative, and the real terms of the last-time buy. Terms often move when you ask. Examples are staged delivery over 12 to 14 months, payment on shipment rather than at order, a smaller minimum, or Velan holding stock for you. Only the order has to be placed in ten weeks. The cash may not have to leave that day.

### B. Shorten or decouple the redesign

6. **Ship the Corwen M7 board without hill-hold first.** The port is about 4 months and certification about 3. If the sensor design is not on the critical path for a "no hill-hold" variant, you could be certified in about 7 months. That equals your stock. Add hill-hold back later as a second hardware revision with its own, smaller re-certification. Check this with your electronics team.
   - Hill-hold is engaged on about 6% of rides, almost all on retail. Lease fleets are 60% of volume, mostly courier and delivery. If those fleets are mainly on flat routes, they may not care. Ask your top fleet customers.
   - The cost is a second certification round and a period of retail bikes without the feature. Before going ahead, check that hill-hold isn't a safety claim in your marketing, manuals or the standards you certify against. A loaded cargo bike rolling backward on a slope is a liability question, not only a feature question.
7. **Replace the "new sensor" with an off-the-shelf one, or use another route to hill-hold.** The 7-month sensor design is the longest single item. Options include a standard inclination or IMU module, a hold function from motor-phase and brake inputs, or a timer-equivalent built from M7 peripherals. Ask the team which of these they have not ruled out and why.
8. **Compress the programme with outside help.** Run the firmware port, sensor work and EMC pre-compliance scans in parallel rather than in sequence. Bring in a design house or Corwen's application engineers. Tarrow may also offer engineering support. Fourteen months is a sequential estimate. Even a 3-month saving cuts the last-time buy by about €400k.

### C. Stretch what you have

9. **Reserve spares for the installed base.** You've built every model since 2019 on this board. Lease fleets will need replacement controllers for years. Whatever you decide, put a service-spares quantity into the number, or you'll solve production and then strand your own fleet customers. A redesigned board that isn't a mechanical and electrical drop-in makes this more important.
10. **Allocate old boards where they matter most.** Bikes with hill-hold go on VX-41 boards, and fleet bikes get the M7 variant first (if option 6 works). Prioritise higher-margin models if you have to ration.
11. **Cut consumption as a last resort.** Slow builds, reduce lower-margin variants, or lengthen lead times. This hurts revenue and fleet contracts, so keep it as a fallback.

### D. Money

12. **Part-fund the last-time buy and finance the rest.** Customer prepayments or deposits from the big lease fleets, supplier terms (Velan or Tarrow holding stock and invoicing at call-off), asset-based lending against inventory, or selling lease receivables. The bank has refused to extend the facility, but they may not have been asked for something secured on specific stock.
13. **Sell the used bikes as refurbished instead of harvesting them.** This is the alternative to item 1. A refurbished bike keeps its original board and needs no new one, and it sells for far more than scrap. Harvesting is cheaper per board and more flexible. A mix is possible: refurbish the best 2022 and 2023 bikes, harvest the rest. It also competes with your own new-bike sales.

### E. Options I would not pursue

- **Buying the full €1.9M**, or borrowing to do it, when you can't fund it and don't need it if A and B work.
- **Just accepting an outage** after month 12. Include it only as the stated downside if everything else fails.
- **Waiting.** Ten weeks passes quickly, and several of these options require lead time.

## How these combine

| Source | Cover (production-months) | Cost |
|---|---|---|
| Existing stock | 7 | Already paid |
| Harvested trade-in boards (80% yield) | about 4.5 | Labour and test |
| Funded last-time buy (€700k) | about 5 | €700k |
| **Total** | **about 16** | |

That exceeds the 14 months, with a buffer for slippage and spares, and without borrowing. If the harvest covers 4.5 months, you only need about 2.5 months from the last-time buy, roughly €340k. That leaves about €360k in reserve for the Brisk auction, testing, and the second certification round. If the redesign can also ship without hill-hold at month 7 to 8, the requirement drops further. In that case the last-time buy is insurance and not a necessity.

## What to find out before the board

1. Board revision and condition across the 1,900 used bikes: sample 30 and test them this week.
2. Whether Velan's quote is gross of your stock, and what payment and delivery terms they will accept.
3. Whether the M7 board can be certified without the new sensor, and what a second certification round would cost.
4. What Tarrow holds, and what is in the Brisk auction lot list.
5. Whether fleet customers accept bikes without hill-hold, and whether there is a safety or contractual claim attached to it.
6. Service-spares volume for the installed base.

## What I'd put to the board

Don't present a single buy. Show a combined plan: a smaller last-time buy sized to the gap after harvesting, an auction bid with a fixed limit, a no-hill-hold M7 variant as the schedule backstop, and a financing request for whatever is left. Have the order decision ready for week 8 or 9, after the board sample test and Velan's terms are known, so you aren't committing money before you know your real gap.
