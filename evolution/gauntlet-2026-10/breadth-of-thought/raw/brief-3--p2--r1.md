The bank's refusal and the 14-month redesign look like a choice between a big last-time buy and a shortage. They aren't. Your facts point to at least ten options. Several of them cost almost no cash, and some stack. The main one is that you may not need hill-hold on the first Corwen board.

## Assumptions
- The €1.9M last-time buy covers the whole 14-month window, about €135k per month of supply. €700k therefore buys roughly 5 months on top of your 7 months of stock, about 12 months in total. If the €1.9M only covers the 7-month gap, €700k buys about 2.5 months, and the other options matter even more.
- Your 4 + 7 + 3 month estimate is sequential. I suspect that is because one team does everything, not because of a hard dependency.
- You build roughly 330 bikes a month, and one board goes into each bike.

## The full menu

**1. Partial last-time buy with the €700k (the baseline)**
- Cash cost is €700k, which uses up everything you can free.
- It gets you to about month 12, or later if the cost per month is lower than I assumed. That leaves a gap of at least 2 months, and zero cash for anything else.
- On its own it is not enough. It is a component of the other options.

**2. Staged or consigned last-time buy**
- Ask Velan, its distributor or Tarrow for staged delivery: you commit to the full quantity, pay per shipment, and the supplier holds the stock.
- Other variants are extended payment terms, or Tarrow carrying the chips on its balance sheet and charging a holding fee.
- This is the only option that attacks the €1.9M cash problem directly. EOL programmes often allow it, and Tarrow has a strong interest in keeping its board orders from you.
- Risk: Velan may require non-cancellable orders, or Tarrow may want a premium or a guarantee. Ask in the first week, before the ten-week deadline.

**3. Ship a Corwen M7 board without hill-hold first (the biggest lever)**
- The 4-month firmware port and the 3 months of EMC certification make about 7 months. That is the same as your existing stock, instead of 14 months.
- The 7-month sensor design only blocks hill-hold. It doesn't block the controller.
- Hill-hold is used on about 6% of rides, almost all on retail bikes, so lease fleets would barely notice. Courier fleets are 60% of your volume.
- The hill-hold sensor can follow later as a second board revision or a retrofit for retail customers.
- Risks:
  - Retail marketing or spec sheets may promise hill-hold.
  - Lease contracts may specify it. Check this first.
  - Any EMC failure puts the 7 months at risk, so build in margin.
  - Certification would have to run again for the board revision that adds the sensor.

**4. Parallelise and accelerate the redesign**
- If the port (4 months) and sensor design (7 months) can run at the same time with separate people, the critical path becomes about 7 + 3 = 10 months, not 14.
- A contract design house or extra engineers cost money but far less than the €1.9M.
- Pre-compliance EMC testing during the design shortens the formal certification.
- Combined with option 3, the full hill-hold board could arrive in about 10 months, after a no-hill-hold board at about 7.
- Risk: more people on a critical path add coordination cost, and some tasks genuinely depend on each other.

**5. Rework a different hill-hold method on the M7**
- Ask the team whether the missing timer peripheral can be emulated with M7 timers, DMA or an interrupt scheme.
- Another route is to detect slope from existing signals (motor current, wheel speed, an inertial sensor already on the board).
- If it works, hill-hold ships in the first release with no new sensor.
- Risk: it may not meet the feel or safety expectations of a brake-hold feature, and the team likely already considered it. Still, it is worth a one-week, cheap check.

**6. Harvest boards from the 1,900 trade-in bikes**
- Every model since 2019 uses the same controller board, so those bikes hold up to roughly 1,900 boards. At about 330 builds a month, that is around 5 to 6 months of supply.
- You are currently stripping the batteries and scrapping the rest. Stop the scrapping now.
- Cost is labour, testing and refurbishment, plus the lost scrap value. It needs almost no cash.
- Risks:
  - Used boards have wear, and 2020–2023 boards may be older revisions.
  - You would need a bench-test and burn-in process.
  - Putting refurbished boards into new bikes may raise warranty and labelling questions.
  - You may also want to keep some boards as service spares for the leased fleets.
- This is probably the cheapest option in cash, and combined with stock it covers about 12 to 13 months.

**7. Buy the Brisk Motion parts stock at the administrator's auction**
- Brisk bought controllers from Tarrow, the same contract manufacturer you use, so the stock may include VX-41 chips, bare boards or finished controllers.
- Get the lot list from the administrator this week and have your engineers and Tarrow inspect it.
- Insolvency auctions are often priced low, but sales are as-is, so check authenticity, date codes and storage conditions. A broker-sourced chip bought at a distress price can also be counterfeit.
- It costs cash from the same €700k, so decide the maximum bid after the inspection.
- Ask Tarrow for help: it knows what Brisk's boards contained and what Tarrow itself holds or can source.

**8. Ask Tarrow and Velan's channel for stock you haven't been offered**
- Tarrow may hold VX-41 stock for other customers, including Brisk's old orders, or know where allocation remains.
- This costs little to try. Other VX-41 users, including Brisk's administrator, are also trying to sell or buy.
- Grey-market brokers are a last resort because of counterfeit risk.

**9. Buy a ready-made controller or motor system instead**
- A third-party drive-system supplier could replace the in-house board.
- Cash cost can be low if they hold the stock, but it means a mechanical and electrical integration project plus new certification, probably 6 to 9 months.
- You also lose control of the controller and the hill-hold behaviour.
- It is a fallback if the Corwen port stalls, not a lead option.

**10. Manage demand while the supply is short**
- Allocate boards to the highest-margin or contract-committed bikes first: the lease fleets with contractual delivery.
- Move retail to made-to-order or slow it down for a couple of months.
- Seek pre-payments or deposits from fleet customers to fund part of a last-time buy.
- Raise cash against the used-bike inventory or other stock, or sell it to a lessor.
- This protects revenue but doesn't solve supply. It buys time for the others.

## Which combinations work

| Package | What it contains | Supply covered | Cash needed |
|---|---|---|---|
| A. Cheapest cover | 6 + 3 | Stock + harvested boards + a no-hill-hold Corwen board at about month 7 | Mostly engineering and refurbishment labour |
| B. Safe-minimum | 1 or 2 + 6 + 7 | About 12 months of boards plus Brisk lots | Within €700k |
| C. Lowest customer impact | 4 + 5 + staged buy (2) | Hill-hold kept in the first release | Highest, and most schedule risk |
| D. Fallback | 9 + 10 | Only if the Corwen port stalls | Needs lead time |

## What I would recommend taking to the board
1. **Lead with option 3 plus option 6.** The Corwen board without hill-hold arrives at about month 7, and harvested boards bridge any slip. They make the case with the lowest cash risk.
2. **Run options 2, 7 and 8 in parallel** over the next two to three weeks. They are cheap to ask about and they extend the safety margin.
3. **Keep the €700k as a reserve** rather than spending it all on a partial buy. Commit part of it only after the Brisk inspection and Velan's answer on staging.
4. **Start options 4 and 5 now** so hill-hold follows as quickly as possible.

## Questions to settle before the board meeting
- Do any lease contracts or retail marketing promise hill-hold?
- How many of the 1,900 bikes still have intact boards, and what are their revision levels?
- Can the firmware port and the sensor work run in parallel?
- Will Velan or Tarrow allow staged payment?
- What is the cost per month of a last-time buy, and what does the €1.9M actually cover?
- What exactly is in the Brisk lots, and what is the inspection window?

## Not covered
I haven't looked at buying a competitor's controller design under licence, or at exiting retail models that depend on hill-hold. Both are possible but slower or more drastic than the options above.
