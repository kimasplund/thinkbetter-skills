## VX-41 end-of-life: options for the board

The full 14-month last-time buy (about €1.9M) is probably not the right answer. The strongest option to test is to move courier bikes to the Corwen M7 first and buy only enough VX-41 for retail, which fits inside the €700k you can free up. Several other levers are worth checking before the board meets.

### Key numbers (my assumptions, please verify)

- Production: 4,000 bikes/yr, about 333/month. Retail (40%) is about 133/month; courier (60%) is about 200/month.
- Board stock covers 7 months, about 2,330 controllers.
- Full 14-month need is about 4,670 controllers, so the gap without any buy is about 7 months (about 2,330 controllers).
- Implied price: €1.9M / 4,670 is about €400 per controller. That is high for a microcontroller, so confirm whether the quote is for the VX-41 chip alone. Every figure below scales with this number.
- Assumed: the 14-month plan starts now, the 7-month stock figure is measured from now, and the M7 port includes any PCB changes.

### Options

**A. Full last-time buy (€1.9M).** Closes the gap entirely, but you cannot fund it without new financing. Ruled out unless financing appears.

**B. Partial buy at the €700k cap.** About 1,750 controllers, roughly 5 months. Stock plus buy covers about 12 months, leaving about a 2-month gap. Needs one of the levers below to close.

**C. Retail-only tail (recommended to test).** Courier bikes move to the M7 board when VX-41 stock runs out (month 7). Retail stays on VX-41 until the hill-hold sensor is certified (month 14).
- Retail need after stock: about 133/month x 7 months, about 930 controllers.
- Add a 2-month buffer for courier slippage (about 400): about 1,350 controllers, about €550k at the implied price.
- Saves roughly €1.3M against the full buy.
- Risk: the M7 port plus EMC must finish in about 7 months, which is the same as the plan with no slack. The buffer and the used-bike option (E) cover slippage.
- Needs a two-SKU plan (VX-41 retail variant and M7 courier variant), or hill-hold disabled by configuration on courier bikes. Check what the variant does to certification and production cost.

**D. Ship the M7 board without hill-hold first.** The sensor is the long pole: 4 + 7 + 3 months in series. Shipping the M7 without hill-hold, or with it disabled, could reach certification in about 7 months, matching the stock runway, and could avoid the last-time buy entirely. Hill-hold returns later as an upgrade. Costs: retail loses a feature used on 6% of rides, and feature removal may need a review of type approval, product claims, and customer notice. This is the biggest lever and needs a yes or no from the electronics team and a regulatory check.

**E. Recover controllers from the 1,900 used bikes.** Every model since 2019 uses the same board, so these bikes likely hold VX-41 controllers. Pulling boards before stripping or scrap could yield up to about 1,900 controllers, roughly 5–6 months of production, but yield after testing is unknown.
- Test a sample of 20–50 boards now: function, age, firmware version, and confirm the part is actually VX-41.
- Check whether the bikes are worth more whole or refurbished than as scrap. That could also raise some of the cash you need.

**F. Brisk Motion parts auction (next month).** Brisk's stock may include finished controllers or VX-41 boards from Tarrow.
- Set a maximum bid in advance and inspect lots before buying.
- Auction lots carry provenance and counterfeit risk and usually no warranty. Treat it as upside, not a plan.

**G. Tarrow Electronics.** Ask whether they hold VX-41 stock or can pool a last-time buy with other customers. Ask whether they can do the M7 port or act as a second source. Your existing relationship and Brisk's history with them are leverage.

**H. Velan negotiation.** Ask for:
- A blanket last-time order with scheduled call-offs over 14 months, paid as drawn. This cuts the up-front cash.
- A delivery window that runs past the 10-week order close.
- Supplier credit or staged payment terms.
- Any extension or bridge quantity, at a premium if needed.

Check authorized distributors for stock too. Avoid unauthorized brokers because of counterfeit risk.

**I. Financing other than the bank.**
- Supplier credit, as in H.
- Customer prepayment or co-funding from lease fleet partners, who care about uptime.
- Invoice finance on receivables.
- Sale and leaseback of board stock.
- Regional or government green-manufacturing support, where available.
- Sale of used-bike stock (see E).

**J. Demand-side moves.**
- Allocate remaining VX-41 stock to contracted courier orders first.
- Tell retail customers about the hill-hold change.
- Review retail volume and pricing for the bridge period.

**K. Cheaper hill-hold path.** Ask the electronics team whether an external timer IC, or software hill-hold on the M7's own timer, could replace the 7-month sensor design. This could shorten the long pole.

### Suggested sequence

1. Start the M7 port now. Every path that avoids the full buy needs it.
2. Put the questions in D and K to the electronics team, with a date for answers.
3. Ask Velan for call-off terms and a delivery window (H).
4. Test used-bike board yield (E) and check Tarrow stock (G) before the board meets.
5. Size the order to the retail tail plus buffer (about 1,350 controllers, about €550k), within the €700k cap, unless D removes the need.
6. Set a maximum bid for the Brisk auction (F).

### Timing

The board meets in 3 weeks and the last-time order closes in 10 weeks, which leaves about 7 weeks to place the order after the board decides. Board yield tests and Velan terms need to start now to inform the decision.

### Compliance check

Any controller change needs EMC work and probably type-approval re-testing. Removing hill-hold may also need review. Confirm this with your certification body before committing to D.
