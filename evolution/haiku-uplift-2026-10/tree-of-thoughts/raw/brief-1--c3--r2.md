My recommendation is the 2-week option: cache the day's jobs read-only and let technicians fill in completion forms offline, uploaded later. It is the only one of the five that fits the calendar and the constraints you described. But it is not enough on its own, and you should not commit the team on Monday without resolving three blockers first.

**Why the timeline decides it**

Harrowgate's IT review of each new app version takes about 8 weeks, and you have 11 weeks. That means the build you submit has to be final by about week 3. Working backwards:

- **CRDT rebuild (9 weeks):** Submitting at week 9 leaves about 2 weeks of review time, not 8. It cannot be reviewed and deployed before storm season. It also does not fit well with the stock counts (see below), because a CRDT merges concurrent edits but does not enforce a count that bills cost centres.
- **Driftwell (3 weeks):** Fast to build, but it adds a new sub-processor. Their contract only permits you and your hosting provider. Adding Driftwell needs a contract amendment with Harrowgate, which may take longer than the engineering. It also costs about $24,000 a year. Check the contract before you consider this seriously.
- **Queue and replay (5 weeks):** Submitting at week 5 leaves about 6 weeks of review. That is tight but possibly survivable. However, replaying stock decrements against the API after reconnect means the server must handle conflicts between two crew members drawing from the same van while offline. That work is not in the 5-week estimate as far as I can tell.
- **Progressive web app (6 weeks):** Their handsets have the browser disabled and only install from the managed catalogue, so a PWA cannot run on the devices at all. Drop it.

**The stock count problem**

Two crew members on separate handsets draw from the same van. If each decrements the count offline, the counts diverge, and Harrowgate bills cost centres from those counts. The 2-week option avoids this only if offline completion forms do not change the stock count at all. Instead, record each part as a pending line item on the form. The server applies the decrement when the form uploads, and flags a conflict for the dispatcher if the van's stock has changed in the meantime. Confirm with your mobile team that this fits the 2 weeks, and confirm with product that dispatchers can accept a delay in stock counts until upload.

**The 12-hour sign-in token**

This is the one I would worry about most. The offline window can be up to two days, and tokens expire after 12 hours. Any offline design will have uploads arriving with expired credentials. You need to agree with Harrowgate's security team on how queued uploads are authenticated: for example, a device-bound credential that the server accepts for uploads made during the offline window, with the form's signing time checked. Do not implement a workaround that quietly extends the token lifetime without their agreement. Ask them this week, since the answer may change the design.

**What I would do on Monday**

1. Commit to the cache-and-forms option, with stock recorded as pending line items rather than decremented offline.
2. This week, get written answers on two questions: whether Harrowgate's security team will accept a token scheme for offline uploads, and whether they will accept an IT review submission at roughly week 3 (or whether they can expedite it).
3. Ask legal whether Driftwell would need a contract amendment, in case you need a fallback.
4. Start the Harrowgate IT review as soon as the build is feature-complete, not after it is fully tested.
5. Keep the CRDT rebuild as a post-storm roadmap item. It is a sound long-term direction for conflict handling, but it does not fit this deadline.

**Assumptions**

- The estimates are the mobile team's, and I have not validated them.
- The 8-week review applies to every new version, and an already-approved version cannot be extended to cover offline use without a new review.
- I do not know whether the server side needs changes for stock reconciliation. If it does, the 2-week figure is optimistic.
