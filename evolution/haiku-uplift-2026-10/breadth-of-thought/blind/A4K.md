The real constraint is timing, not just money. The VX-41 last-time-buy window closes in ten weeks, the board meets in three, which leaves about seven weeks to place any order. Your redesign path is 14 months, your board stock is 7 months, and the bank will not extend. Every option below is judged against those three numbers.

One assumption shapes everything: I am reading the €1.9 million as the cost of 14 months of boards. If your current stock counts toward those 14 months, the order you actually need to place is for roughly the remaining 7 months, about €950,000. That is much closer to the €700,000 you can free up. Please confirm this with the electronics team before the board meeting, because it changes which options are affordable.

**Options**

1. **Full last-time buy covering 14 months.** This gives the cleanest bridge to the redesign. It costs €1.9 million in the worst reading, and the €700,000 you can free up does not cover it. It is only viable if the stock assumption above holds and you can find the remaining cash.

2. **Partial last-time buy sized to available cash, plus a second source for the gap.** At roughly €136,000 a month, €700,000 buys about five months. Combined with stock, that could cover most of the 14-month path, leaving a gap of a few months. The gap has to be closed by one of the options below.

3. **Drop hill-hold from the first redesign.** Porting to the Corwen M7 and certifying the EMC takes about 7 months, which roughly matches your existing board stock. The sensor work, which is the 7-month piece that depends on the VX-41 timer, moves to a second release. Hill-hold is used on about 6% of rides, almost all retail. The cost is that retail customers lose a feature they use, and you would need a clear answer for them: a later software update, a retrofit kit, or a sales message. This option removes most of the need for a large last-time buy, so it is probably the strongest option on paper. Electronics should confirm that the M7 port can be done without the sensor work.

4. **Hill-hold without the VX-41 timer.** Engineering may be able to implement hill-hold on the M7 using a different timer, a software approach using existing sensors, or an external timer chip. This would remove the 7-month sensor item. It is uncertain until electronics has looked at it, but it is worth a short technical check before the board meeting because it could keep the feature and shorten the timeline.

5. **Buy parts from the Brisk Motion administration auction.** Brisk bought its controllers from Tarrow Electronics, the same contract manufacturer you use. Their parts stock may include VX-41 boards or compatible controllers. The auction is next month, which is inside your ten-week window. Risks: the stock may be small, may not be VX-41 specifically, may be used or of unknown provenance, and you would need to test it before relying on it. The auction timing means you should ask now whether someone can attend and inspect.

6. **Recover controllers from the 1,900 used bikes in the warehouse.** Every model since 2019 uses the same controller board, and the 2020–2023 bikes in the warehouse should contain it. Stripping boards from these bikes instead of selling them for scrap could yield a meaningful stock of controllers at low cost. The yield, the condition, and whether the boards still work after storage are unknown, so this needs a sample teardown and test. It also has a second benefit: it avoids scrapping units you could otherwise sell or refurbish.

7. **Ask Velan for an extended or lifetime buy, or go to authorized brokers.** Velan may offer a larger final order at a different price, or may allow a longer window for a customer with a substantial commitment. Independent brokers may hold VX-41 stock. The main risk with brokers is counterfeit or re-marked parts, so any purchase from them needs incoming inspection and an authorized-distributor check.

8. **Fix the financing gap before the purchase.** The bank has refused an extension, but other sources may exist: deposits or prepayments from courier and delivery fleets on lease, a supplier or contract manufacturer willing to hold or finance inventory, invoice financing against lease receivables, or a sale-leaseback of the warehouse stock. Any of these could make a larger last-time buy affordable. None is certain, and each takes time that is short.

9. **Reduce or reshape production during the transition.** Since 60% of your output goes to lease fleets, you could protect fleet supply and slow retail builds, or keep building retail models without hill-hold. This lowers how many boards you need to bridge the gap, at the cost of retail volume and revenue.

**Options I would not put forward as a main path**

- Switching to a different microcontroller family for a new design, instead of the M7, would likely take longer than the 14 months you already have, since it restarts firmware and certification work.
- Doing nothing and reacting when the stock runs out would leave you with no board supply for several months, with no bridge and no bank facility to lean on.

**What I would take to the board**

The most useful package is a combination rather than a single choice. Based on the facts you gave, a credible plan would be:

- Primary: drop hill-hold from the first redesign, which brings the timeline close to the stock on hand, and place a smaller last-time buy sized to close the remaining gap. Ask electronics whether hill-hold can be delivered later or on the M7 without the VX-41 timer.
- Parallel: send someone to the Brisk auction and run a teardown of the warehouse bikes. Both could add controllers at low cost and reduce how much you need to buy from Velan.
- Financing: approach fleet customers for prepayment or deposits, and talk to a supplier or invoice-finance provider now, since the bank route is closed.
- Fallback: if none of these closes the gap, reduce retail production for a few months and protect lease-fleet supply.

**Before the board meeting, confirm**

- Whether the €1.9 million covers the full 14 months, or whether current stock counts toward it.
- Whether the M7 port is achievable without the sensor work, and whether hill-hold can be done another way.
- What Velan will offer in a final order, and whether the price or quantity changes.
- What is in Brisk's parts stock, and whether someone can inspect it before the auction.
- How many usable controllers the 1,900 warehouse bikes would yield, based on a small teardown sample.
