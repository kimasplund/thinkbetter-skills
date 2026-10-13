**Short version:** the last-time buy is only one of about ten levers, and the problem is smaller than "€1.9M vs €700k" suggests. The real gap is about 7 months of boards (14 months to redesign, 7 months of stock), roughly 2,300 boards at your current run rate of about 330 bikes a month. Several of the options below can close that gap, alone or combined, for much less than €1.9M.

**Assumptions (please check these first, because they change the numbers):**
- The €1.9M covers a full 14 months of production, which is about 4,700 units, or roughly €400 per unit. I've assumed it doesn't net off your existing 7 months of stock. If it does, the cash problem is far smaller than it looks. Ask finance and procurement to confirm this before the board meeting.
- The 4 + 7 + 3 month plan is sequential as your team described it. Sequential isn't strictly necessary, and that's option 2.
- Retail is about 1,600 bikes a year (about 133 a month), and fleets are about 2,400.

## The options

**1. Buy part of the last-time buy with the €700k.**
- If the €1.9M is a gross figure, €700k buys about 37% of the need, roughly 5 months of production. Add your 7 months of stock and you reach about 12 months of cover against a 14-month redesign.
- Ask Velan and your distributor whether you can pay in tranches rather than all up front, or whether payment falls due at delivery rather than at order. Orders close in ten weeks, but cash may not have to leave until later. That could change the picture a lot.
- Weakness: on its own it leaves you about 2 months short, with no margin if the redesign slips.

**2. Shorten the redesign by running the work in parallel.**
- Start the hill-hold sensor design now, alongside the 4-month firmware port, instead of after it. The schedule becomes about 7 months of design plus 3 months of EMC, so roughly 10 months rather than 14.
- Cost: more engineering effort at the same time, and possibly a contract design house for the sensor.
- Risk: the 7-month sensor estimate is the long pole, and EMC can't finish before the sensor design is frozen.
- This is nearly free in cash terms and cuts the gap from 7 months to about 3.

**3. Split the product by customer: fleets get the new controller first, without hill-hold.**
- Hill-hold is used on about 6% of rides, almost all on retail bikes. The M7 port and EMC take about 7 months and don't depend on the sensor. That matches your stock, though with zero margin.
- Fleet bikes (60% of volume) would move to the M7 controller without hill-hold at about month 7. Retail bikes would keep the VX-41 until the sensor is ready.
- After month 7 you'd only need VX-41 boards for retail, about 133 a month. For roughly 7 months that's about 900 boards, or about €0.4M at your implied unit cost. That is within the €700k.
- Risks: two variants to certify and support, and a feature gap on fleet bikes. Check whether any lease contracts or fleet specifications mention hill-hold. A fleet customer who contractually expects it would be a problem.

**4. Use the 1,900 trade-in bikes as a parts source instead of scrap.**
- Every model since 2019 uses the same controller board, so those bikes hold up to about 1,900 boards, or about 5.7 months of full-rate production. That is currently going to scrap.
- Test and refurbish the boards, and replace any weak components. Pull the VX-41 chips for reuse as well.
- Risks: the age and wear of the boards, the cost of testing and rework, warranty exposure on bikes built with reclaimed boards, and whether the 2020–2023 board revisions are electrically identical to current ones. A sample teardown of 20 to 30 boards would answer most of this in a week or two.
- This is probably the best value per euro on the list. It is cheap and quick, and you already own the stock.

**5. Buy from the Brisk Motion administration auction next month.**
- Brisk bought its controllers from Tarrow, your own contract manufacturer. There may be finished controller boards, loose VX-41 chips, or the same board design in the lot.
- Get the lot list from the administrator now. Check whether the boards match yours or only use a similar part, and whether there is VX-41 stock.
- Administrators often sell at steep discounts, but you may be bidding blind. Cap your bid and test a sample if they allow viewing.
- Weakness: it's an opportunity, not a plan. The contents and the price are unknown.

**6. Ask Tarrow (and Velan) to help directly.**
- Tarrow may hold VX-41 stock or have its own last-time-buy allocation. It may also be able to buy on your behalf, hold the stock on consignment, or extend payment terms.
- Velan might accept a staged or partly cancellable schedule, since it also wants the end-of-life sell-through.
- Cost: only the time to ask. But this depends on goodwill and on what Tarrow is allowed to do.

**7. Reduce what hill-hold needs from the VX-41.**
- Ask the electronics team whether the timer function can be done on the M7 using a different peripheral, DMA, or software. Or use an off-the-shelf IMU or tilt sensor with a small separate microcontroller. Another route is detecting a hill-hold condition from motor current and brake input, which needs no special hardware.
- If any of these works, the 7-month sensor design shrinks and the redesign could approach the 4 + 3 month minimum.
- Risk: a performance or safety compromise on a braking-related feature. It needs proper testing, and it is uncertain whether it works at all.

**8. Find more cash.**
- Ask fleet customers for deposits or prepayments in return for priority delivery or price protection.
- Use the 1,900-bike warehouse stock as asset-finance collateral, or sell refurbished bikes as certified used instead of scrapping them.
- Look at factoring or selling your lease receivables.
- Look at supplier financing, or a deposit from Tarrow.
- Weakness: the bank has already declined to extend, so these will cost more and take longer. They are worth running in parallel with the options above.

**9. Manage demand instead of supply.**
- If stock is going to be short, decide who gets the boards: fleet contracts under penalty clauses first, then retail.
- You could slow retail, take pre-orders, or raise prices to ration units.
- This is the fallback. It costs revenue, but it is fully in your control.

**10. Last resort: gray-market VX-41 chips from brokers.**
- Possible, but counterfeit and quality risk is high on an end-of-life part. Only consider it with testing, and only for a small top-up.

## Combinations worth taking to the board

| Package | What it combines | Rough cover | Cash need | Main risk |
|---|---|---|---|---|
| **A. Parallel redesign + partial last-time buy** | 1 + 2 | 7 months stock + about 5 months bought = about 12 months against a roughly 10-month redesign | About €0.7M | Redesign slips past month 12 |
| **B. Two-track launch** | 3 + 1 (retail only) | Fleets on the M7 at about month 7; retail on VX-41 until the sensor is ready | About €0.4M | Two variants, fleet contract terms |
| **C. Cheap stock first** | 4 + 5 + 6 | Up to about 5.7 months from reclaimed boards, plus an unknown amount from the auction | Test and rework cost plus a capped bid | Quality of reclaimed boards, auction outcome |
| **D. Cash-raising** | 8 + 6 | Lets you buy more of the last-time buy | Lowers the up-front cash | Cost and time of finance |

## What I'd recommend

I'd present **Package B with Package A's parallel schedule** as the base plan. Start the M7 port and the sensor work now, and aim for fleets on the M7 at about month 7. Cover retail's VX-41 needs with part of the €700k. Layer **Package C** on top as cheap insurance, since the reclaimed boards and the auction are your largest sources of extra boards at the lowest cost. Keep the cash-raising and demand-management options as contingencies if the redesign slips.

If the €1.9M turns out to be net of existing stock, or the lease contracts require hill-hold on fleet bikes, the answer shifts. In the first case buying the full last-time buy gets much more affordable. In the second, Package A gets more attractive than B.

## To check before the board meets (three weeks)

1. Whether the €1.9M is gross or net of existing stock, and when the cash is actually due.
2. The Brisk lot list, and whether the boards or chips match yours.
3. A sample teardown and test of 20 to 30 boards from the trade-in bikes.
4. Whether Tarrow holds VX-41 stock or can buy for you, and whether Velan will accept staged delivery.
5. Whether the sensor work and the M7 port can really overlap, and whether EMC can start before the sensor is final.
6. Whether any fleet lease contracts or specifications depend on hill-hold.
7. Whether hill-hold can be reworked on the M7 (option 7), which would shorten everything else.

One more point on timing: orders close in ten weeks, so the decisions about how much to buy have to be made within about seven weeks of the board meeting. The cheap checks above should be finished before then.
