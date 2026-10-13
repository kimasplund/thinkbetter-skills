**Recommendation: option 4, cache the day's jobs read-only and let technicians fill in completion forms offline, uploaded later.** Make the server the only writer of stock counts, and start the Harrowgate IT review this week, because that review is the real deadline.

**The constraint that decides this is the 8-week IT review, not the build.** Every option ships a new app version through Harrowgate's managed catalogue. With 11 weeks left and an 8-week review, you have to submit by about week 3. That rules out anything longer than roughly 2 to 3 weeks of build and test.

**Why each option lands where it does:**

- **CRDT rebuild (9 weeks).** It misses the window: 9 weeks of build plus 8 weeks of review is 17 weeks against 11. It also doesn't solve the hard problem. CRDTs merge concurrent edits, but a van's stock count is a shared quantity that must not go negative, and Harrowgate bills cost centres from it. Two handsets decrementing the same van offline need a business rule for oversell and billing, and a CRDT library won't supply that. I'd keep CRDTs in reserve for fields that merge naturally, such as notes, not for stock.
- **Driftwell (3 weeks, $2k/month).** It looks fastest, but a hosted sync service is a new sub-processor. Harrowgate's contract only allows you and your hosting provider, so this needs a contract schedule amendment, which is likely slower than 3 weeks and may need Harrowgate's consent. It also still requires the app review, and it still has the stock-count conflict problem.
- **Queue and replay (5 weeks).** It misses the window once review is counted: submit at week 5, approved around week 13. Its design also has the stock problem described below.
- **Progressive web app (6 weeks).** Harrowgate's handsets have the browser disabled and only install apps from their catalogue, so a PWA can't reach the crews at all. Drop it.
- **Cache and offline forms (2 weeks).** This is the only option that fits. It adds no new sub-processor and no new data-handling party. It also solves the stock problem by design: technicians record parts used on the form, and the server applies the decrement when the form uploads. Upload-time decrements are the single source of truth, so the device never decides a count. If the van would go negative, the server accepts the form and flags it for a dispatcher to reconcile.

**Things to settle this week, whichever option you pick:**

1. **Review timing.** Ask Harrowgate's IT team whether they can start review on a feature-complete build now, or accept a staged or early submission. Your slack depends on it. Any later feature needs another 8-week review, so the first submission should cover what the crews need in storm season.
2. **Sign-in tokens.** The 12-hour expiry means the app can't rely on a live token during a two-day outage. You'll need offline read of the cached jobs without a valid token, with local encryption, and queued uploads that wait until re-authentication on reconnect. Harrowgate's security team set the 12-hour limit, so they should approve the offline data-at-rest design before you build it, not after.
3. **Billing timing.** Confirm with Harrowgate that cost centres are fine being billed when forms upload rather than when the part was logged. Totals should match; only the timing shifts.
4. **Scope risk.** If crews truly need live stock visibility offline, option 4 won't deliver that. Say so to Harrowgate now, because the alternative is a second review later.

**For Monday:** commit the team to option 4. Start the IT review and the security conversation this week, and ask Rasmus to keep the CRDT idea for a later, non-stock feature. Happy to draft the Harrowgate security questions or the review timeline if that helps.

**Assumptions I made:** the 8-week review applies to each new app version; the team can have a review-ready build by about week 3; and Harrowgate would accept a version whose offline scope is forms and a read-only cache.
