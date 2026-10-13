## The core problem

You need roughly 14 months of controllers. You have about 7 months in stock, and a last-time buy (LTB) that covers the full 14 months costs about €1.9M, or roughly €136k per month of production. With €700k you can buy about 5 months, which gets you to about 12 months. That leaves a gap of about 2 months, and the bank will not help. Every option below is a way to close that gap, cheaper, or both.

## Options

**1. Harvest controllers from the 1,900 used bikes in the warehouse (strongest option).**
Every model since 2019 uses the same controller board, so these bikes are a parts source. At 4,000 bikes a year (about 333 a month), 1,900 boards is roughly 5.7 months of production. Stripping them costs labour and some testing, not much cash. Stock plus harvest gives about 12.7 months, which is nearly the full 14. Caveats: yield after testing is unknown (assume 80 to 90 percent usable until you test a sample), boards from older bikes may need reflashing or rework, and you should check whether any harvested units are a different board revision.

**2. Small top-up LTB, sized to the gap.**
If harvest and stock give about 12.7 months, you need only about 1.3 months more, roughly €180k. That is well within the €700k. Order it in the first LTB window, before the 10-week deadline, and ask Velan or the distributor for a split shipment or a tiered price so you are not paying for all of it up front.

**3. Buy the Brisk Motion parts stock at the auction.**
Brisk bought controllers from Tarrow Electronics, the same contract manufacturer you use. The stock may include finished controller boards or VX-41 devices. Ask Tarrow to confirm what Brisk ordered and whether any of it is VX-41 based. Before bidding, check authenticity, date codes and whether the lot includes boards or only parts. Buying Brisk's installed base may also bring warranty or support obligations, so price those in.

**4. Ask Tarrow for their own VX-41 inventory and a quote.**
Tarrow may hold VX-41 stock or have buffer buys from other customers. Get their quote and lead time now, and ask whether they can run the Corwen M7 port.

**5. Ask Velan for a successor or form-fit-function replacement.**
Many end-of-life notices name a replacement part or a bridge (pin-compatible) device. Even if the successor needs a firmware change, it may be far faster than the Corwen port or the hill-hold redesign. Confirm this in writing before the board.

**6. Shorten the redesign.**
The 14 months looks sequential (4 + 7 + 3). Ask the electronics team whether the firmware port and the sensor design can run in parallel, and whether EMC testing can start on the ported firmware before the sensor is done. Also ask whether hill-hold can be rebuilt without the VX-41 timer, for example with an external timer chip, a timer on the Corwen M7 used differently, or a software method using motor current or back-EMF. A "minimum viable" hill-hold that does not need the old timer might save months.

**7. Decide the hill-hold scope.**
Hill-hold is on about 6 percent of rides, almost all retail. One option is to ship the Corwen port without hill-hold on retail bikes, which takes the 7-month sensor work off the critical path and reduces the period you need controllers to about 4 months. The cost is consumer-law and marketing risk for retail buyers who expect the feature, plus a possible customer communication and warranty plan. Get legal advice before choosing this. A middle option is to ship hill-hold only on leased fleet bikes where the fleet operator has agreed.

**8. Find cash other than the bank.**
Options include supplier-financed LTB terms (pay on shipment or in tranches), inventory or purchase-order financing from a specialist lender, customer deposits or prepayments from leasing fleets that want supply certainty, and a shareholder loan or sale-leaseback of equipment. Note that the bank refusal may limit what other lenders will offer, so start these now.

**9. Protect the fleet customers.**
Sixty percent of volume goes to leasing fleets. Tell them early and offer a supply plan, which is worth more to them than the hill-hold feature. This also builds the case for option 7.

## Suggested plan for the board

1. Harvest the 1,900 warehouse bikes now, starting with a test sample to measure yield.
2. Size a top-up LTB (about €180k to €300k, with margin) and place it with Velan or the distributor before the 10-week deadline.
3. Start the Corwen port now, and ask electronics for a parallel schedule and a no-timer hill-hold option.
4. Get written quotes from Tarrow and Velan's successor-part answer, and check the Brisk auction lot.
5. Ask the board to approve the plan and a budget ceiling, and to decide the hill-hold scope (option 7) once legal and customer-impact advice is in.

## Assumptions

- The €1.9M LTB price is for 14 months of production at current volumes, so each month costs about €136k.
- Production runs evenly at about 333 bikes a month.
- The 7 months of stock is measured in finished-production months, not boards.
- The 14-month redesign clock starts roughly now.

If any of these are wrong, the arithmetic changes, but the shape of the options does not.
