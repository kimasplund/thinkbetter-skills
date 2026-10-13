The "how much last-time buy can we afford" framing is too narrow. Your situation has at least eight levers, and several of them are cheaper than the LTB. Combined, they may close the gap without the full €1.9M.

**Assumptions (please correct me)**
- You build about 333 bikes a month, so your 7 months of stock is roughly 2,300 boards.
- The redesign finishes at month 14, so you are short about 7 months of supply, about 2,300 boards. I'm reading the €1.9M as the cost of covering that shortfall. If it covers all 14 months, the €700k buys proportionally more (roughly 5 months).
- On that reading, €700k buys roughly 2.5 months of supply, about 37% of the €1.9M.

## The options

**1. Stop scrapping the trade-in bikes and harvest their controller boards (do this first)**
- You hold 1,900 used bikes, and every model since 2019 uses the same board. That is about 5.7 months of production sitting in your warehouse.
- Assume 60-80% of the boards test as good. That gives roughly 1,100-1,500 boards, or 3-4.5 months of supply, for the cost of testing, refurbishment and handling.
- Risks to check:
  - Board revision differences across 2019-2023.
  - Wear and reliability on a safety-relevant part.
  - Warranty and lease terms if refurbished boards go into customer bikes.
  - Whether you can reflow-harvest VX-41 chips for rework.
- Start a pilot batch of 50 bikes now. Pull all scrap shipments until you have the results.
- Keep feeding this channel. Trade-ins and lease returns will keep adding boards.

**2. Split the redesign: ship the new controller without hill-hold first**
- Port the firmware to the Corwen M7 (4 months), then run EMC certification (3 months). That is about 7 months, which is exactly when your current stock runs out.
- Treat the 7-month sensor as a separate, later release.
- Only about 6% of rides use hill-hold, almost all on retail bikes, and fleet bikes (60% of volume) barely use it. Fleet bikes could move to the new board without hill-hold.
- Ask the electronics team three questions:
  - Can hill-hold be done without the VX-41 timer, using motor current, Hall signals or a software timer on the M7 (a lower-spec version)?
  - Can the sensor be an off-the-shelf part instead of a custom 7-month design?
  - If the sensor comes later, can the board carry a footprint or connector for it? Then it could ship as a retrofit or an add-on with a firmware update, and might not need full recertification.
- Check the legal and safety position before dropping hill-hold. If it counts as a safety feature, or is advertised, removing it affects marketing, consumer-law claims and lease specifications.

**3. Allocate scarce VX-41 boards by who needs them**
- Reserve the old-design boards (and any LTB) for retail models that rely on hill-hold.
- Put fleet bikes on the new board as soon as it is certified.
- This stretches the old stock further because the new board needs no hill-hold. It also protects the customers most affected by the feature loss.

**4. Partial last-time buy with the €700k**
- Buy about 2.5 months of supply (more under the other reading).
- Combined with options 1 and 2, it is a buffer against slippage rather than the whole answer.
- Ask Velan to schedule deliveries after the order closes, so cash goes out in tranches rather than all up front. LTB programmes often allow deferred shipment.
- Ask Velan about:
  - Splitting the order into tranches, with a deposit now and the balance on delivery.
  - Extending the order close date.
  - Extended availability or a longer-life version of the part.
  - Cancellation terms.
- Buy only through authorised distributors. Gray-market brokers carry counterfeit risk.

**5. Brisk Motion's auction next month**
- Brisk bought controllers from Tarrow, which also builds yours. Their parts stock may contain VX-41 chips, finished boards, or boards close enough to adapt.
- Contact the administrator now to get the lot list and register as a bidder. Plan the budget and decide your maximum bid.
- Before bidding, check:
  - Whether the part or board is the same variant, and what condition and age it is in.
  - Whether the packaging is sealed.
  - Whether there are authenticity risks and what the title and warranty position is, since administrators sell "as is".
- Have Tarrow inspect the lot and help verify it.

**6. Tarrow Electronics as a partner**
- Ask Tarrow:
  - Do they hold VX-41 stock, or have an allocation from Velan?
  - Have they got Brisk's order backlog or cancelled-order stock, which may now be unclaimed?
  - Can they place the LTB on their own account, buy on their balance sheet, and sell to you over time, with consignment or deferred payment?
- Tarrow also serves other VX-41 customers, so they may already be planning an LTB. Join it to pool volume.
- Ask Tarrow how quickly they could port or build the M7 board, and whether they can compress the schedule or share EMC resources.

**7. Fund the shortfall differently**
- The bank has refused, but you can still look at:
  - Asset-based lending or inventory finance secured on boards and finished stock.
  - Factoring or financing against the lease receivables, since 60% of your sales are leased to fleets.
  - Prepayment or deposit from fleet customers who want guaranteed delivery. Offer a price lock or priority slot in return.
  - Supplier credit from Tarrow or Velan.
  - Shareholder or owner funding, or a short bridge loan.
  - Regional or industrial development funding.
- An LTB is inventory with a resale value. That makes it easier to finance than operating losses.
- The more precise the plan, the easier it is to raise: "€1.2M for six months of boards, secured on stock" is a different ask from a general facility.

**8. Manage demand and mix**
- Prioritise fleet orders (contracted, recurring) over retail if boards run short.
- Delay or slow retail volume in months 8-14 if a gap remains, or limit retail to the models that use the boards most efficiently.
- Raise retail prices on hill-hold models to ration demand.
- Last resort: a planned short production pause. It would be costly but controlled, and it is better than a surprise stop.

## How they combine (illustrative)

| Source | Approx. months of supply |
|---|---|
| Current board stock | 7 |
| Harvested boards (60-80% yield) | 3-4.5 |
| Partial LTB (€700k) | 2.5 |
| Brisk or Tarrow stock | 0-3, uncertain |
| **Total** | **12.5-17+** |

- Against that, the new non-hill-hold board arrives around month 7-8 if you split the redesign, and the full redesign at month 14.
- On these numbers, options 1, 2 and 4 together may close the gap without the full LTB. That needs verifying.
- The main risks are schedule slippage on the port and EMC certification, and the harvest yield.

## What to do before the board meeting (3 weeks)

1. **This week:** halt scrapping of trade-ins. Test 50 boards from the 2020-2023 bikes and measure the yield and the variant mix.
2. **This week:** ask the electronics team for a re-plan with a hill-hold-free first release, and a view on the alternative sensing approaches. Ask for a schedule with confidence ranges.
3. **This week:** call Velan about deferred delivery, tranches and extended dates. Call Tarrow about their stock, their LTB plans and financing support.
4. **Within 1-2 weeks:** contact the Brisk administrator for the lot list. Get Tarrow to inspect it.
5. **Within 2-3 weeks:** sound out two or three financing routes, and ask your top fleet customers whether they would prepay for supply certainty.
6. **For the board:** present the scenarios as a decision tree, with the trigger points. The LTB closes in 10 weeks, so the board has to decide the size of the partial buy no later than about week 7-8, ideally with the harvest and auction results in hand.

## Decisions I'd ask the board for
- Approve the split release (new board without hill-hold first), subject to the legal check.
- Approve up to €700k for a partial LTB, tranched where Velan allows, with the balance of the decision held until the harvest and auction results are known.
- Authorise a bidding budget for the Brisk auction.
- Authorise exploring the alternative financing routes.
- Set a stock-level trigger (for example, below 4 months of cover with no certified board) at which retail volume is cut.

I'd be happy to turn this into a one-page board paper or a scenario table once you have the harvest test results and Velan's response.
