Your doubt is justified for four of the five. One is defensible: the 2-week option (cache jobs, fill in completion forms offline, upload later). It needs some added scope, and the biggest risk to the date has nothing to do with engineering.

**The constraint that decides this is Harrowgate's app review.** The last review took eight weeks, and every new version goes through it. You have 11 weeks. So the build has to be submitted by about week 3, which leaves no margin if the review runs as long as last time. Anything that takes more than about 2 to 3 weeks to build misses the date, however good it is. That rules out the 5-week queue, the 6-week PWA and the 9-week CRDT rebuild on timing alone.

**Why each option stands or falls**

| Option | Verdict | Reason |
|---|---|---|
| PWA (6 weeks) | Dead | Harrowgate's handsets have the browser disabled and only install from the managed catalogue. It cannot run there. |
| Driftwell (3 weeks, $2k/month) | Blocked | It would process job data through a third party that isn't in the contract's sub-processor schedule. Using it needs a contract amendment and Harrowgate's sign-off. You'd be adding that approval cycle on top of the app review, and Harrowgate would be the one deciding. |
| CRDT rebuild (9 weeks) | Wrong tool and too slow | It misses the review window by itself. It also solves the wrong problem. Automatic merging doesn't enforce "stock can't go below zero", and Harrowgate bills from those counts. Your suspicion about Rasmus's motive may be right, but the timing argument is enough without it. |
| Action queue and replay (5 weeks) | Right idea, wrong moment | Submitting at week 5 plus an 8-week review lands in week 13. It is a sound phase two, but not the storm-season answer. |
| Read-only cache plus offline forms (2 weeks) | Defensible, with additions | It's the only one that fits the review window, and it covers what crews need at a pumping station: see today's jobs, record the work, and upload when signal returns. |

**What the 2-week version has to cover.** The estimate probably assumes the simple case. These facts from your context change the scope:

1. **Offline for two days, but tokens last 12 hours.** The app must let a technician keep working with an expired token by unlocking with the device's own screen lock or a local PIN. Uploads then wait until they sign in again on reconnect. The offline data store must be encrypted. Don't extend the token lifetime, because Harrowgate's security team won't allow it.
2. **Cache more than "the day's jobs".** A crew leaving for a two-day stretch needs at least three days of assigned jobs, refreshed on every sync. Dispatchers can't reassign jobs while a crew is out of signal. Agree that limitation with Harrowgate up front.
3. **Record parts as events, not stock counts.** Two technicians draw from the same van on separate handsets. If each handset writes "stock is now 14", one write overwrites the other. Instead, each handset records "used 2 of part X" with a unique ID. The server applies these on upload, so the van count comes out right whatever order they arrive in, and a retried upload can't be counted twice. If the total goes negative, flag it for reconciliation. Don't silently clamp it, because the counts feed billing. This is the one piece of real design work, and it's probably another week.
4. **Two people on the same job.** Decide the rule now, for example the first completion upload wins and the second is held for review. Don't leave it undefined.

Realistically that is 3 weeks, not 2. Even so, the review leaves essentially no slack.

**What to do before Monday**

- **Today:** ask Harrowgate's IT contact for a firm review slot, ideally expedited. Offer a deliberately small release and ask whether review time scales with the size of the change. If they can't commit to less than 8 weeks, no option on your list makes the date. You'd rather learn that now and tell Harrowgate plainly than find out in week 10.
- **Commit the team to** the cache-plus-forms release, with parts as events, offline unlock and the multi-day cache. Target submission by end of week 3, with the first two weeks held to the minimum scope.
- **Plan the queue-and-replay work as the follow-up** for after storm season. It extends the same local store and the same unique-ID upload approach, so nothing from the first release is thrown away. That also gives Rasmus a real next step. If you still want a CRDT, revisit it then, once you've seen how often offline conflicts actually happen.
- **Park Driftwell** unless Harrowgate volunteers to amend the sub-processor schedule. Sales shouldn't raise it with them as a solution.

**What I'm assuming.** I'm taking "11 weeks" as the date by which the build must be live on handsets, not just in review. I'm assuming the 8-week review is typical for any new version. And I'm assuming your team's estimates are sound. If Harrowgate can review in under four weeks, the 5-week queue becomes viable and is the better long-term choice, so ask that question first.

My confidence is high that the read-only cache plus offline forms is the only workable choice from this list. It is moderate that it ships in time, because that depends on a review process you don't control.
