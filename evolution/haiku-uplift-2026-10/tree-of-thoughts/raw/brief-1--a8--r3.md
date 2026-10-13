**Recommendation: commit Monday to the read-only job cache with offline completion forms (2 weeks), built so it can grow into queued actions later. Start talking to Harrowgate's IT team on Monday as well, because their review time is the real deadline.**

## Why the calendar decides this

Your last Harrowgate IT review took eight weeks. Any option that changes the app has to clear that review before storm season, so the usable build time is about 3 weeks, not 11. This is the estimate plus review against your 11 weeks:

| Option | Build | + 8-week review | Fits in 11 weeks? |
|---|---|---|---|
| Read-only cache + offline completion forms | 2 wks | 10 wks | Yes, with about 1 week spare |
| Hosted sync (Driftwell) | 3 wks | 11 wks | No margin, and blocked on contract (below) |
| Queue and replay actions | 5 wks | 13 wks | No |
| Progressive web app | 6 wks | n/a | No (below) |
| CRDT data layer | 9 wks | 17 wks | No |

Two of the options fail for reasons beyond time:

- **Progressive web app:** Harrowgate has disabled the browser on its handsets and only allows installs from its managed catalogue. A PWA can't run there at all.
- **Driftwell:** Your contract limits processing of job data to the sub-processors in its schedule, which today is you and your hosting provider. Driftwell would be a new one, so you would need Harrowgate's agreement and a contract change first. That is a legal and procurement process, probably with their security team, and it can't be assumed to finish in 3 weeks. Even if it did, 3 + 8 weeks leaves no slack.

The CRDT rebuild is the best long-term engineering story and Rasmus's preference is understandable. But it can't ship this winter, and it would put the team's whole capacity into a data-layer rewrite that Harrowgate's reviewers then have to approve.

## What the winning option has to get right

The simple version is nearly enough. Four things in your context would break it if you build it naively.

1. **Parts and van stock.** Two technicians draw from one van on separate handsets, and Harrowgate bills its cost centres from the stock counts. Offline, each handset sees a stale count.
   - Don't upload "the count is now 14". Record each use as its own event (part, quantity, job, technician, device timestamp, a unique ID) and let the server apply the decrements when it receives them. Decrements add up in any order, so two partners' uploads can't overwrite each other.
   - The server should deduplicate by event ID, so a retried upload doesn't double-count.
   - Stock can go negative after two days of unsynced use. Allow it, flag it for the van's owner, and bill from the event log rather than from the running count.
   - Don't let a handset hand out the "same" last part twice without a warning. A local on-screen caution when a part is logged that the cached count says is gone will catch most of it.
2. **12-hour sign-in tokens.** Crews can be offline for 2 days, so the token will expire mid-trip, and Harrowgate won't change the lifetime.
   - Let the app keep working locally after expiry, behind the device lock or a local PIN. Don't require a valid token to open cached jobs or to add forms.
   - Keep completed forms in the local queue until the technician signs in again on reconnect, then upload them under the fresh session. Check with Harrowgate's security team that a local-only unlock is acceptable. This is a short conversation, but it needs to happen early.
   - Store the cached jobs and queued forms encrypted on the device.
3. **Read-only means read-only.** Technicians can't reassign or edit jobs offline, and dispatchers can change jobs while a crew is out of signal. On upload, the server should accept the completion but flag any case where the job was cancelled, reassigned or changed in the meantime, for a dispatcher to review. Decide that rule now; it is cheap to build and expensive to discover in the field.
4. **Which jobs get cached.** Pull the next day or two of assigned jobs, including the details crews need at a remote pumping station (site notes, asset history, parts lists). Show a clear "synced at" time and a "waiting to upload" count on screen, so crews know what has and hasn't gone through.

## Making the review window work

- **Ask Harrowgate IT on Monday** what their review process needs, how many cycles it usually takes, and whether a smaller, offline-only change can go through a faster track. Ask for a named contact and a slot booked for week 3. The difference between an 8-week and a 5-week review is the difference between making winter and missing it.
- **Submit as early as you can.** Aim to hand over a release candidate at the end of week 2 or early in week 3, and use the spare time for fixes if review sends it back once.
- **Keep the release narrow.** Fewer changed permissions, no new network destinations and no new third parties should make the reviewers' job easier. This is another reason to avoid Driftwell.

## Beyond this winter

After this ships, the next release can add technician edits and queued actions, replayed against your API on reconnect. That is the 5-week option, built on the same local store and event queue you are about to create. If the stock and conflict handling above prove awkward, that is the point to reconsider a CRDT layer, with real field data to justify it. Plan that release for after the winter freeze, and put it in front of Harrowgate IT early so the next review doesn't take another 8 weeks.

## What to tell people

- **Harrowgate:** You will have offline access to the day's jobs and the ability to complete them with parts, notes and photos, ahead of winter. Editing jobs offline comes later.
- **Rasmus:** The CRDT idea isn't wrong, only too late. The queue-and-replay work you do next gets you most of the way there without a rewrite.
- **Sales:** Driftwell's speed is real, but it needs a contract change with Harrowgate first and leaves no margin in the review window.

## Assumptions and risks

- The 8-week review figure holds for a smaller release. If it is firmer than that, even the 2-week option is at risk, and the conversation with Harrowgate's IT team should happen first. If they say a review can't finish by week 11, tell Harrowgate now rather than in week 10.
- Crews mostly need to read their jobs and record completions, rather than edit job details, while out of signal. Confirm with two or three Harrowgate technicians before Monday if you can. If offline editing turns out to be essential, nothing on the list fits in 11 weeks, and you will have to agree a narrower scope with Harrowgate.
- The 2-week estimate comes from your team. The stock event log and the token handling above are probably where it grows, so ask them to re-estimate with those included before you commit.
