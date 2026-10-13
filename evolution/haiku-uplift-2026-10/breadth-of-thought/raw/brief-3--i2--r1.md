You have more options than "how much last-time buy can we afford". Several of them attack the gap itself rather than the cheque size, and two use things you already own.

## The numbers that frame the menu

- You build about 330 bikes a month, so about 330 boards a month.
- 7 months of stock is roughly 2,300 boards. A redesign at 14 months leaves a gap of about 7 months, or roughly 2,300 more boards.
- €700k against a €1.9M full buy covers roughly 5 months of that gap, assuming the €1.9M prices the full 14 months. If it prices only the 7-month gap, €700k covers about 2.5 months. Please check which it is, because it changes the picture.
- Last-time-buy orders close in 10 weeks, and the board meets in 3. That leaves about 7 weeks after the meeting to commit. Anything that needs Velan's agreement should be started now, before the meeting.

## The menu

**A. Shrink the gap (change the redesign)**

1. **Ship the new controller without hill-hold, and add hill-hold later.** The firmware port (4 months) plus EMC (3 months) is about 7 months, which is almost exactly your stock cover. The 7-month sensor design is only needed for a feature used on about 6% of rides, almost all on retail bikes. Fleet bikes move to a hill-hold-free Corwen M7 board at about month 7, and hill-hold returns as a later revision. Risks: lease contracts or fleet specs that name hill-hold, retail marketing claims, and loaded-cargo rollback on slopes. Also check with engineering whether the board can be certified once and the sensor added later without a second full EMC round.
2. **Run the sensor design in parallel with the port.** The 14 months looks sequential (4 + 7 + 3). If sensor design and port can overlap, the total drops to about 10 months. Ask the team directly whether it is sequential by necessity or by habit.
3. **Replace the VX-41 timer function some other way.** Options are an external timer or small companion chip, a different M7 peripheral with a firmware rework, or a sensor-less approach using motor feedback. Any of these could be faster than a new sensor. The team may already have rejected them, so ask why.
4. **Add capacity.** Brisk Motion is in administration, so its electronics engineers are probably available as contractors or hires. An outside design house, or Tarrow's own engineers, could shorten the port or the EMC prep.

**B. Stretch the supply you have or can find**

5. **Pull the controller boards out of the 1,900 trade-in bikes.** Every model since 2019 uses the same board, so those are about 1,900 boards, equal to roughly 5-6 months of production. You are currently stripping the batteries and scrapping the rest. Stop that now, or at least stop discarding the boards. Used boards will need testing, a firmware check and probably refurbishment, and some will fail. A realistic yield of 60-80% still gives you 3-4 months. The safest use is service and warranty replacements, plus refurbished-bike sales, which frees new boards for production. Using them in bikes sold as new is a warranty and disclosure question for you and your lawyer. Refurbishing and selling the bikes instead of scrapping them is also worth a look.
6. **Bid at the Brisk auction next month.** Brisk bought controllers from Tarrow, so find out what Brisk's stock includes: VX-41 chips, bare or assembled boards, or Tarrow-built stock on the same chip. Ask Tarrow before the auction which items are compatible with your board. Also ask the administrator about finished controllers and test fixtures. This is cheap to pursue, but compatibility is unknown, so don't count on it in the base plan.
7. **Ask Tarrow what it holds and what it can source.** As the contract manufacturer for two brands, Tarrow may have VX-41 inventory, an allocation of its own, or a broker channel. It could also place the last-time buy on your behalf and hold the stock.
8. **Buy through distributors or brokers after the deadline.** This is a fallback only. Broker-sourced parts carry real counterfeit and quality risk and need incoming testing.
9. **Ask Velan for flexibility.** Examples are staged deliveries against a single order, a later delivery window, or a die or wafer bank. Many suppliers will do this to secure a large last-time buy. Ask whether a pin-compatible or successor part exists.

**C. Cut how much you need to buy before month 14**

10. **Use two controller versions in the interim.** Reserve the remaining VX-41 stock and any last-time buy for the retail bikes that use hill-hold. From about month 7, the fleet bikes (60% of volume) move to the M7 board. The VX-41 need for months 7 to 14 drops from about 2,300 boards to about 900 (retail only), which is roughly 40% of the full amount. At the per-board cost implied by €1.9M, that is about €0.4M if the figure covers 14 months. If it covers only the gap, it is about €0.75M. Either way it is close to or inside what you can free up. This combines well with option 1, and is a lot more affordable than the full buy.
11. **Slow or prioritise production.** Allocate boards to contracted lease deliveries first, trim retail volume or push out retail dates, and raise retail prices. Each month of stretch buys time, but it costs revenue, so treat it as a lever for the last few months of the gap rather than a plan.

**D. Pay for it differently**

12. **Find money that isn't the bank.** Examples are inventory finance or a supplier facility secured on the parts, customer or lessor prepayments (fleet customers have an interest in continuity of supply), Tarrow supplying on deferred terms, an investor bridge, or selling and leasing back the trade-in stock. The bank refusal rules out the existing facility, not every source of funds.
13. **Do nothing and accept a stock-out.** Include this on the board slide so the board sees what it costs. When the boards run out at month 7, production stops. You face lease delivery penalties and lost retail season, and a possible loss of fleet customers. It is the baseline the other options are compared with.

## How the options combine

| Plan | What it needs | Rough coverage | Main risk |
|---|---|---|---|
| Partial buy only (€700k) | Cash | Gap closed for 2.5-5 of 7 months, depending on how the €1.9M is built | Shortfall of 2-4 months |
| Partial buy plus harvested boards | Cash plus test and refurb capacity | Probably most or all of the gap | Board quality and warranty handling |
| No hill-hold at launch plus two versions plus a smaller buy (options 1, 10, with 5 as cover) | Product decision, engineering, about €0.4-0.8M | Closes the gap on current numbers and keeps hill-hold for retail | Fleet contract terms, retail reaction, EMC approach |
| Faster redesign (options 2, 3, 4) plus a partial buy | Engineering confirmation | Could cut the gap to 3-4 months | Team may say it cannot be done |
| Stock-out | Nothing | None | Revenue and customer loss |

My suggested core plan to bring to the board is the third row, with the harvest of old boards as a cushion and the Brisk and Tarrow enquiries as upside. It spends the cash on the part of the gap you can't cover any other way.

## Before the board meets

1. **This week:** stop scrapping trade-in bikes. Count them by model year and test a sample of boards.
2. **This week:** ask Velan for staged deliveries and a longer order window. Ask Tarrow what VX-41 and Brisk-related stock it knows about, and whether it can hold a last-time buy for you.
3. **Engineering:** ask for the sensor and port timeline as overlapped, and the cost and time to certify a no-hill-hold board first.
4. **Commercial:** check which lease contracts mention hill-hold, and what fraction of retail buyers use it.
5. **Finance:** confirm what the €1.9M covers, and line up one or two non-bank funding conversations.

## What I'm assuming

- Boards and VX-41 chips are interchangeable for planning, and the €1.9M scales evenly with quantity.
- The 4/7/3-month sequence is as your team described it. The hill-hold usage data (6% of rides) holds across the fleet.
- Old boards from 2020-2023 bikes are electrically and mechanically compatible, which is likely given the shared design but needs testing.
