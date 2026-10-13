The options are wider than "how much last-time buy (LTB) can we afford", because several of them shrink the gap before you spend any money. Your constraint is a 14-month redesign against 7 months of stock, so the gap is about 7 months, or roughly 2,300 boards at about 333 a month.

**Assumptions.** I'm reading the €1.9M as the cost to cover the full 14 months. If it only covers the 7-month gap, the quote is roughly twice as expensive per board, which is worth checking. I'm also assuming the "3 months EMC" can't start until the hardware is final, and that hill-hold is a comfort feature rather than a regulatory or safety requirement. Please verify that last one.

## A. Find more VX-41 boards without buying new ones

1. **Stop scrapping the trade-in bikes' controller boards today.** Every model since 2019 uses the same board, so the 1,900 used bikes hold up to about 1,900 working boards. That is roughly 5.7 months of production, and it costs only test and refurb labour. Assume 60-80% usable after testing, which gives about 3.5-4.5 months. Check warranty terms, board revision differences and ESD handling. Keep trading bikes in, because each one is now a board supply. This is probably your biggest single lever.
2. **Bid at the Brisk Motion auction next month.** Brisk's controllers came from Tarrow, so their parts stock may hold VX-41 chips, bare or populated boards, or Tarrow-specific parts. Ask the administrator for the lot list now. Beware of boards that aren't our design (chips could be pulled and reused, but that means rework and traceability risk) and of anything without a provenance trail.
3. **Ask Tarrow directly.** Do they hold VX-41 stock or open orders, including any placed for Brisk and now cancelled? Can they place the LTB under their volume, or hold it on consignment?
4. **Check franchised and independent distributors for remaining VX-41 stock.** Be careful about counterfeits. Buy only through franchised channels or with test and authentication.
5. **Ask Velan about alternatives.** Is there a form-fit-function successor, a staged-delivery LTB, a licensed continuation source, or a longer extended-life programme?

## B. Make the LTB cheaper or later

6. **Negotiate the LTB shape.** Orders close in 10 weeks, but delivery can often be scheduled over 12-18 months with payment on delivery. That could turn a €1.9M upfront cost into a payment profile your €700k can service. Also ask for tolerance to cancel or defer part of it.
7. **Size the LTB to the residual gap, not 14 months.** If the other options below fill most of it, the LTB only needs to cover the remainder.

## C. Shrink the problem

8. **Split the product: ship a no-hill-hold controller first.** Hill-hold is engaged on about 6% of rides, almost all on retail, and it is the part that needs a 7-month sensor design. The firmware port to the Corwen M7 takes about 4 months, so a courier-fleet variant without hill-hold could be certified and shipping in about 7-8 months (4 months port plus 3 months EMC), not 14. Courier bikes are 60% of volume, so the VX-41 then goes only to retail. That stretches your VX-41 stock considerably. Retail hill-hold follows once the sensor is ready, possibly as a retrofit. Check this with your courier customers' contracts and use cases first, since hills matter more in some cities.
9. **Run the firmware port and the sensor design in parallel.** If the team's 4 + 7 + 3 months is sequential, parallel running gives about 10 months (the longest of the two, then EMC). That is 4 months saved, and the cost is extra headcount or a contractor.
10. **Avoid the new sensor.** Can the timer function be provided by a small companion MCU or an external timer or CPLD, or by a different M7 peripheral with a software workaround? Could an off-the-shelf IMU module or motor-current/Hall-based estimation give hill-hold without a custom sensor? Any of these could cut the 7-month item sharply. Test it with a short spike of 2-3 weeks.
11. **Pre-compliance EMC early** on the M7 board, so the final 3 months become confirmation and not discovery.

## D. Money

12. **Customer prepayments or deposits** from the larger fleet customers, in return for guaranteed delivery slots or price locks.
13. **Supplier terms and non-bank finance:** Tarrow credit terms, inventory or asset-backed finance against the stock, or invoice finance on leases. These are different from the facility the bank has refused.
14. **Sell instead of scrap.** Refurbish the best of the 1,900 trade-ins and sell them as certified refurbished retail bikes, which brings in cash and uses the stripped batteries. The boards you need for A1 come from the bikes you don't refurbish, so decide the split early.
15. **Release other cash:** slower-moving inventory, sale-and-leaseback on the lease book, shareholder or equity bridge.

## E. Demand and commercial levers (last resorts)

16. **Prioritise allocation** of scarce boards to higher-margin or contractually committed orders.
17. **Reserve a service-spares quantity.** Bikes built since 2019 will keep needing boards for repair, so that demand competes with production. Size it explicitly.
18. **Slow, pause or de-spec the line** for a few months, or push price and lead-time changes to retail. This costs revenue, so it is the fallback if the others fail.
19. **Tell lease customers early** and agree any change to the hill-hold spec or delivery profile.

## Rough picture (before any LTB)

| Source | Months of production |
|---|---|
| Existing board stock | 7 |
| Trade-in boards (60-80% yield) | about 3.5-4.5 |
| Brisk auction and Tarrow stock | unknown, to be sized |
| Total | about 10.5-11.5+ |

Needed: 14 months for the full redesign, about 10 if the port and sensor run in parallel, and about 7-8 for the courier variant. Combining 1, 8 and 9 appears to cover the gap with little or no LTB. The residual LTB could then fit within the €700k, ideally with staged payments from option 6.

## Suggested package for the board

- **Do now, no decision needed:** stop scrapping boards (1), list the Brisk lots (2), open conversations with Tarrow and Velan (3, 5, 6), and start a 2-3 week spike on sensor alternatives (10).
- **Board decision:** approve the split plan (8) and parallel development (9), including the budget for extra engineering, plus a capped LTB in staged form (6, 7).
- **Contingency:** prepayments or alternative finance (12, 13) and an agreed trigger for slowing the line (18).

The key dates are the LTB close in 10 weeks and the Brisk auction next month. Both fall after the board meeting, so ask the board for authority to move quickly on both. If you tell me the real LTB unit economics, the trade-in yield test and the courier contracts' hill-hold requirements, I can turn this into a month-by-month board supply model.
