Here is a menu for the board. The options group naturally by what they do: get more boards, make the boards you have last longer, shorten the redesign, and pay for it. The strongest answer is a combination, which I set out at the end.

## The gap you are solving

- Board stock covers about 7 months. The redesign takes 14 months as scoped. The uncovered stretch is about 7 months of production.
- I'm assuming the €1.9M quote is for roughly 14 months of boards, about €135k a month. On that reading, €700k buys about 5 months. Add the 7 months in stock and you reach about 12 months of cover against 14 needed, with no margin for schedule slip. Please check with purchasing what the €1.9M actually covers (chips only or finished boards, and from which date). Everything below scales with that answer.
- The last-time-buy deadline is 10 weeks away and the board meets in 3. You have about 7 weeks after the meeting to commit money.

## A. Get more boards or chips

1. **Last-time buy sized to your cash.** Commit the €700k, which is about 5 months of boards. On its own this leaves you roughly 2 months short, so it needs help from the options below. Ask Velan or its distributors whether the order can be placed now with staged deliveries or staged payment. Many last-time-buy programs allow this, and it would stretch the €700k.
2. **Strip boards from the 1,900 trade-in bikes.** Every model since 2019 uses the same board, so each used bike holds a usable controller. At about 330 bikes a month, 1,900 boards is roughly 5 to 6 months of production, and it costs you almost nothing because you are currently selling these bikes for scrap. Stop scrapping them now. The caveats are that the boards need testing and refurbishment, older 2020 builds may have a different firmware or hardware revision, and your own warranty and service spares also need boards. Even so, this is probably the largest single source of cover you have.
3. **Brisk Motion's stock at the administrator's auction next month.** Brisk bought its controllers from Tarrow, the same manufacturer you use. There may be finished boards, VX-41 chips, or both in that stock. Ask Tarrow this week whether Brisk's boards are compatible or carry the VX-41, and ask the administrator for the lot list. A bid has to be sized before you know what is in the lots, so set a ceiling in advance.
4. **Tarrow's own inventory.** Ask whether Tarrow holds VX-41 chips or partly built boards for Brisk or for you. Ask whether they would carry the inventory on their books and be paid as you build, since that moves the cash problem onto their balance sheet. They have an interest in keeping you as a customer.
5. **Independent brokers and the grey market.** This is a fallback only. The counterfeit and relabeled-chip risk is real on a safety-relevant motor controller, so any purchase should come with traceability and incoming testing.

## B. Make the boards you hold last longer

6. **Ration boards by customer segment.** Lease fleets are 60% of volume and sit on recurring contracts, so fulfilling them has priority. Retail can be sequenced behind them or taken from the oldest orders first. This does not create boards, but it protects your most important revenue if stock runs thin.
7. **Reserve boards for service.** Every bike you have sold since 2019 may need a replacement controller. Decide how many boards to hold back for warranty and repairs, so the answer to "how long does stock last" is a deliberate choice and not a surprise.
8. **Slow production deliberately.** If the redesign slips, a controlled cut in output is better than a sudden stop. This is a last resort, but the board should know it exists and roughly what it would cost.

## C. Shorten or reshape the redesign

9. **Run the firmware port and the sensor design in parallel.** The 14 months assumes the work is sequential (4 + 7 + 3). If two teams, or the in-house team plus a contractor, run the port and the sensor design side by side, the total becomes about 10 months (7 + 3). The cost is extra engineering spend, which is far smaller than the cost of buying chips.
10. **Release in two stages.** Port the firmware to the Corwen M7 without hill-hold and certify that board, which is about 4 + 3 = 7 months. Hill-hold is used on about 6% of rides, almost all on retail bikes, so the lease fleets would not notice its absence. Retail bikes keep using VX-41 boards until the hill-hold sensor board is certified. Under this plan, VX-41 boards after month 7 are needed only for retail, about 40% of output, which cuts the quantity you must buy now by more than half. The costs are two board variants to support, a second EMC round, and a commercial question about whether retail buyers accept a bike that eventually changes hardware.
11. **Replace the missing timer peripheral instead of designing a new sensor.** Hill-hold depends on a timer that only the VX-41 has. Ask the electronics team whether an external timer IC, a small programmable logic part, or a different measurement method on the M7 could deliver hill-hold sooner than a 7-month sensor design. I don't know if this is feasible. It's cheap to ask and could remove the longest item in the schedule.
12. **Drop or defer hill-hold.** If the answer to the previous point is no, consider launching the new board without hill-hold for all bikes and adding it later. This is the fastest path and carries the highest commercial risk with retail customers. Check whether hill-hold has a safety role on loaded cargo bikes before putting this to the board.
13. **Buy a ready-made controller.** A third-party motor controller or a drive-system supplier could replace your board for some or all models. It is expensive and means redesigning around someone else's hardware, but it is a real exit if the schedule collapses.
14. **Ask Velan about a successor part.** Check whether Velan has a pin-compatible or software-compatible replacement. That would turn a redesign into a requalification.

## D. Pay for it

15. **Customer prepayments or deposits from fleet customers.** Lease and delivery fleets want guaranteed supply. A deposit tied to a delivery schedule can fund part of the purchase.
16. **Supplier-side financing.** Tarrow, Velan's distributors, or a trade-credit insurer may accept a payment schedule on the last-time buy. This is worth a call now.
17. **Different lenders.** Your bank has declined, but inventory-backed finance, asset-based lending, or finance against the lease receivables are separate products from the bank facility.
18. **Raise cash from what you hold.** Sell the used bikes that don't have to be stripped for boards, to the extent they have value beyond scrap, and consider selling or leasing back assets.

## What I would take to the board

**Plan 1, the safe default.** Commit the €700k last-time buy, use the 1,900 trade-in boards, and run the redesign in parallel (about 10 months). Cover is roughly 12 months of purchased and stocked boards, plus the harvested boards, against a 10 to 14 month need. This works without new money, but it depends on the boards from the used bikes testing well.

**Plan 2, the lowest cash and lowest risk.** Do everything in Plan 1, and also release the M7 board without hill-hold at month 7, as in option 10. A last-time buy sized only for retail's needs after month 7 costs around €380k, well inside what you can fund, and leaves the rest of the €700k as a reserve against slippage. I think this is the plan that deserves the most attention.

**Plan 3, if the timer question has a good answer.** If option 11 works, the sensor design disappears from the critical path, and the program could finish in 7 to 8 months with very little last-time-buy exposure.

**Contingency.** Bid on Brisk's stock within a pre-set ceiling, and keep production slowdown (option 8) and a bought-in controller (option 13) as stated fallbacks.

## Things to settle before the meeting

1. What exactly does the €1.9M buy, and can Velan or its distributors stage payment or delivery?
2. Does Tarrow hold VX-41 stock or Brisk-related boards, and what is in the auction lots?
3. How many of the 1,900 used boards pass a functional test, and which hardware revisions are they?
4. Can the electronics team staff parallel work, and is an external timer feasible?
5. How many boards should be held for service and warranty?

The first four can be answered in two weeks and they decide which plan to put to the board.
