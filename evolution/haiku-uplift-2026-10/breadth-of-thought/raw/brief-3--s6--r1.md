The full menu comes down to one question: how much VX-41 supply do you need to bridge to a working replacement controller, and where can that supply come from? Here are the options I see, with the trade-offs for each. Figures are rough and use the numbers you gave me.

**Working assumptions:** the €1.9M last-time buy is for the full 14-month window, so it costs roughly €136k per month of production. Your board stock covers about 7 months, so the real gap is about 7 months. Lead times, supplier qualification and EMC retest risk are not in the brief and would need checking.

## 1. Full last-time buy for 14 months (€1.9M)
- **Why it is on the list:** it is the simplest path to keeping the current product unchanged.
- **Why it fails:** you can fund about €700k and the bank has refused to extend the facility. Only about 5 months of the buy would be affordable.
- **Verdict:** not fundable as stated. It is useful only as the reference point for the other options.

## 2. Last-time buy sized to the gap, on the current 14-month plan
- Covering the remaining ~7 months beyond stock costs roughly €0.95M, which is still above €700k.
- It can only work if you find another €250k or so, or if you combine it with option 4 or 5 below.
- The order window closes in ten weeks, which leaves about seven weeks after the board meets to place the order.

## 3. Run the redesign work in parallel
- The firmware port (4 months) and the hill-hold sensor (7 months) look like they could run side by side, with EMC certification after both. That would make the redesign about 10 months, not 14. The brief describes them as sequential, so you would need to confirm that with the electronics team.
- A 10-month redesign needs only about 3 months of last-time buy beyond stock, roughly €0.4M. That fits the €700k you can free up, with room to spare.
- The cost is engineering capacity. Running both workstreams at once needs people and possibly outside help.

## 4. Drop hill-hold from the new controller at first
- The Corwen M7 port alone plus EMC is about 7 months, which is inside your stock coverage. That means no last-time buy is needed.
- The cost is the feature itself. Hill-hold is used on about 6% of rides, mostly on retail bikes. Retail is about 40% of your volume, so losing it there could hurt sales. You could offer it later as a retail-only upgrade, or as a paid option once the sensor is ready.
- Check first that the production controller can be validated without the sensor, and that the port alone clears EMC on time.

## 5. Use the 1,900 trade-in bikes as a parts source
- Every model since 2019 uses the same controller board, so the trade-in fleet, mostly 2020–2023 models, should contain VX-41 boards. Your current practice is to strip batteries and scrap the rest, which throws those boards away.
- At 4,000 bikes a year, roughly 330 a month, 1,900 boards would cover about 5–6 months of production if they are usable. That is a large share of the gap, at almost no purchase cost.
- The catch is labour and quality. Boards need to be removed, tested and sometimes reworked, and older boards may have aged components. Start with a sample of 50–100 bikes to measure yield before you count on the full number.
- Scrap value may be low, so the labour may still be worth it.

## 6. Buy Brisk Motion's parts stock at the auction
- Brisk used the same contract manufacturer (Tarrow Electronics) for its controllers. Its stock could include VX-41 boards, or boards built to the same spec.
- Costs are uncertain and the auction is next month, so you need to know quickly what is in the lots. Ask Tarrow to confirm the board revision and whether the parts are original, not rework or counterfeit.
- Brisk's customer base and service records could also be worth a look, but that is a separate decision.

## 7. Buy VX-41 stock from brokers or the open market
- After end-of-life, remaining stock is often sold through brokers at a premium. Price and availability are uncertain.
- The risk is counterfeit or re-marked parts. Use only authorised or well-documented sources, with traceability and test certificates.
- This is a bridge option, not a long-term fix.

## 8. Reduce build rate to stretch the stock
- Halving production would stretch 7 months of stock to about 14 months, with no outlay.
- The cost is lost revenue and possibly breach of lease commitments, since 60% of volume goes to courier and delivery fleets on lease. Check contracts before choosing this.
- It works best combined with option 4 or 5, or as a short-term measure while the others are arranged.

## Combinations worth putting to the board
- **Lowest cash:** parallel redesign (3) with trade-in board harvesting (5). Stock plus harvested boards may cover most of the 10-month window, and the cash need drops well below €0.4M.
- **Lowest risk to the product:** parallel redesign (3) with a small last-time buy (about €0.4M) and a trade-in harvest as backup. Keeps hill-hold and fits the funds.
- **Fastest and cheapest:** drop hill-hold for the first release (4), harvest boards (5), and keep the Brisk auction (6) as an option.

## Before the board meets
1. Ask electronics whether the firmware port and sensor work can run in parallel, and what the real EMC lead time is.
2. Audit the trade-in fleet: sample 50–100 bikes, count usable VX-41 boards, and note the cost of removal.
3. Get Tarrow to tell you what Brisk's auction lots contain and what they can supply directly.
4. Confirm the last-time buy deadline and the minimum quantity Velan will accept.
5. Check lease contracts for supply and delivery obligations before any build-rate cut.

If the parallel redesign and the board harvest both check out, you can likely fund the controller change without new borrowing.
