Here is my read of the design, ranked by what I expect to fail first. I've assumed the gate keypad checks PINs against a list that is stored on the keypad, and that the locks use a fixed credential per tenant or helper. If either assumption is wrong, the related findings change, so please confirm them.

## 1. The gate keypad will be brute-forced (fails first)

A 6-digit PIN has 1,000,000 possibilities. With 5 wrong tries followed by a 5-minute lockout, an attacker can make 5 tries every 5 minutes, which is about 1,440 guesses a day. At your largest site with about 1,100 active tenants, roughly 1,100 of the million PINs are valid, so each guess has about a 0.11% chance of hitting one. That works out to about 1.6 successful entries per day, or close to certain entry within a week of patient guessing. The lockout is also a denial-of-service lever: if it is per keypad rather than per PIN, anyone can lock out the whole gate for 5 minutes at a time.

Changes:
- Use escalating lockouts (for example 1 minute, then 10, then 1 hour) and alert the site manager after repeated failures.
- Count failures per PIN and per source, and do not let one bad actor lock out the whole gate.
- Use longer codes (8 or more digits) or add a second factor such as a phone prompt for gate entry.
- Confirm that PINs are never reused across tenants and that the keypad logs every attempt.

## 2. Removals and overlocks don't take effect where you need them most

Changes reach a lock only at its next sync, and the locks are in basements with no signal. A helper who is removed, or a tenant who is overlocked at 30 days late, keeps working on that lock until a Corrabay app happens to sync with it. Worse, the 50-credential cache is evicted by count, not by time. In a quiet unit that is never synced, a revoked credential can survive indefinitely because nothing newer pushes it out.

Changes:
- Give every cached credential an expiry (for example 24 to 72 hours) and make the lock refuse expired credentials. Renewal then happens at the next sync, and a revoked person's access ends at the expiry even if the sync never comes.
- Treat a revocation as a delete on the lock, not an eviction candidate. Check that the lock actually confirms the deletion at the next sync.
- For overlocks specifically, check whether you can physically shut the unit or change the lock when the revocation can't be delivered. The overlock is also the moment a tenant is most likely to be in a dispute.
- Make sure the unlock credential is not a static value that could be captured over Bluetooth and replayed. It should be encrypted per session or challenge-response based.

## 3. Helpers are added by phone number with no verification

Anyone a tenant names gets the same rights as the tenant. Phone numbers are recycled, so a helper's number can be reassigned to a stranger who then gets unlock rights to the unit. Nothing in the design says who approved the helper, and the tenant may be able to add helpers without your staff knowing.

Changes:
- Require site-manager approval for each helper, or at minimum notify the manager and the tenant on every addition.
- Give helpers an expiry date and a re-verification step, and tie access to a verified account rather than a bare phone number.
- Decide whether a helper can add other helpers. If yes, the rights multiply, so it probably should not be allowed.

## 4. The access log is weaker evidence than you think

The log is written by the app and uploaded at sync. Three problems follow:
- A gap in the log does not prove no entry happened. A lock that was used offline and never synced leaves no record.
- The log is not signed. A phone or app that is modified, or simply a user who edits the upload, can change what the record says. Insurers and courts will ask whether it is tamper-evident.
- Log entries are created by the phone, so they show that a phone was used, not who held it.

Changes:
- Have the lock sign each event with a counter that increases with each event, so gaps and replays are detectable.
- Describe the log to the insurer as "the lock's record as of the last sync", and state the blind spots in the review.
- Keep the log retention policy and the chain of custody documented.

## 5. Maintenance codes give managers silent access to any unit

A manager can open any unit at any time, and the tenant is not told. The design does not say what the manager must record, whether a second person approves, or whether the event shows up in the tenant's own history.

Changes:
- Require a work-order reference for each code, cap the duration, and make the code single-use.
- Notify the tenant (or the tenant's record) of every maintenance entry, and log it in a way the managers cannot edit.
- Review the manager accounts' access rights and separate duties where possible (one person issues the code, another reviews the log).

## 6. Opening a unit at 60 days is a legal question first

Photographing contents and listing them for auction only holds up if the entry and the sale followed your state's lien and notice rules, which vary a lot. A manager who opens the unit with a code, or who photographs things without an inventory process, can create a dispute you lose. The photos are also only as good as their timestamps and their chain of custody.

Changes:
- Have a lawyer confirm the notice periods and the sale procedure in each state where you operate.
- Use a written inventory form, two-person entry where possible, and time-stamped photos stored outside the manager's account.
- Keep the 60-day entry separate from the maintenance code path, so the two records can't be confused.

## Suggested order for November

1. Fix the gate PIN lockout and add alerts (quick, and it is the most immediate exposure).
2. Add expiry to offline credentials and confirm that revocations are enforced on the lock.
3. Put helper approval, expiry, and notification in place.
4. Add signed events to the lock log and document the gaps.
5. Tighten maintenance codes and the 60-day entry procedure, with legal review before any auction.

I would not go live at the nine sites until items 1 and 2 are done. Please have a qualified security reviewer and a lawyer check this before it goes to the insurer, since I have only reviewed the description you gave me.
