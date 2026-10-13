## Short answer

What breaks first is revocation. Every control that takes access away (overlock, helper removal, change of tenant) only takes effect at the lock's next sync, and the lock keeps accepting cached credentials in the meantime. Because many units are in basements with no signal, that gap can last days or weeks. Close it first. The audit trail, the maintenance code, the auction photos and the gate PIN come next.

Assumptions: I don't know the lock vendor, the credential format, or how the app authenticates. Check each point below against the real design.

## 1. Revocation lags, and the lock trusts its cache (highest priority)

- **Overlock does not work as an enforcement tool.** A tenant who is 30+ days late keeps working credentials until a phone with signal syncs that lock. A tenant who knows this can avoid syncing, for example by staying out of signal or switching off mobile data. Even a normal tenant in a basement unit may not sync for a long time.
- **Removed helpers and ex-tenants keep access.** A helper a tenant has removed (an ex-partner, a dispute) can still open the unit. A previous tenant whose unit was re-let can too, while the new tenant is inside. This is a theft and liability problem, and it undermines the insurance story.
- **Credentials need an expiry the lock can check on its own.** Locks can't see the network, but they can have a clock. Issue credentials with a short validity (for example 24 to 72 hours, or 7 days), signed by the server. The app refreshes them whenever it has signal. The lock rejects an expired credential even if it has heard nothing. Choose the window by weighing the lockout risk in basements against the exposure.
- **Unit turnover is the worst case, so handle it separately.** When a unit changes hands, do a physical or in-person reset: the manager re-keys the lock with a fresh key or a manager-side Bluetooth session, rather than waiting for a sync.
- **Make overlock a physical state.** A manager-applied overlock or a lock-side "denied" flag, pushed with priority to any phone that is near, is better than a server flag. If the lock supports it, a manager's handheld or the site's own gateway device should sync locks directly instead of depending on tenant phones.
- **Add a site gateway or manager sync tour.** A fixed Bluetooth gateway near each basement, or a daily manager walk with the app, removes the dependence on tenant phones.
- **Sync is an attack surface too.** Check that a lock accepts updates only from signed server messages. A phone is a relay and must not be able to forge or replay them. Check that it can't be rolled back to an older credential list. Check that a phone cannot suppress an update by dropping it while the lock still believes it is current.

## 2. The 50-credential cache and phone-number helpers

- Helpers are added by phone number. Phone numbers get recycled, and they can be SIM-swapped or mistyped. Require the helper to verify the number with a code, and show the tenant who has access. Alert the tenant when a helper is added or first uses the lock.
- Confirm what happens at 50 credentials. Does the oldest get evicted, or does the lock refuse new ones? Either could lock out a legitimate user or let an old one linger. Cache only the credentials for that unit, and say so in the design.
- Set a cap on helpers per unit, and let the tenant see and remove them in the app.
- Consider whether a helper's right should expire on its own (for example 30 days unless renewed).

## 3. The audit trail is not reliable evidence

You describe the access history as "full". It isn't, for these reasons:

- Logs are written by the app and uploaded at the next sync. A thief or dishonest tenant can stop the app from uploading, or can use a modified app. Logs can also be lost if the phone is wiped or the app is uninstalled before a sync.
- Offline unlocks are recorded only on the phone, so the record for the period that matters most for a theft claim (the time the unit was unreachable) may arrive late or never.
- Time stamps come from the phone's clock, which the user controls.
- The lock should keep its own signed, append-only log (who, when, per its own clock) and hand it over at sync. The server should merge the lock's log with the app's log and flag gaps.
- The lock's capacity is finite, so decide what happens when its log is full.
- For insurance and disputes, say plainly what the history can and cannot prove, rather than calling it complete. Add the gate and door camera footage as an independent source.

## 4. Maintenance codes

- A 24-hour code that goes to the manager's own phone is a bearer secret: it can be forwarded, screenshotted or shared, and it works for a whole day. Anyone with a manager account can generate one for any unit, at any site.
- Scope each code to one unit, one site and a short window (one hour is usually enough for a service call), single use if the lock supports it.
- Require a reason code and log who generated it. Tell the tenant when the code is used (a notification), except where law or the lease says otherwise.
- Limit who can generate them. Review the admin panel itself: use MFA, role-based access per site, and alerts on unusual volume of codes. If a manager's phone is lost or an employee leaves, revoke their access straight away.
- Also check whether a manager code can be used on a unit where the tenant has an overlock or is otherwise in a dispute, and who approves that.

## 5. The 60-day delinquency process and auction photos

- One manager opens the unit alone and photographs the contents. This is a classic insider risk (theft, or a dispute that the contents were different). Use two people, or a recorded body-camera or timestamped photo process, and make the unlock event show up in the log.
- The photos are the auction listing and your only record of the contents. They may show personal data (documents, medical items, photos of people, ID). Store them with access control and set a retention period. Blur or exclude documents and personal papers before publishing, and have a rule for items that must not be sold (for example firearms, ID, medical records), which depend on your jurisdiction. Check the legal notice requirements before the lock change makes access easier.
- Take the photos so they can't be altered later: store them with a hash and a server-side timestamp.
- Because the overlock may not have reached the lock (see point 1), a tenant may enter the unit between the photos and the sale. Confirm that the lock really is in the denied state before you rely on the photo record.

## 6. The front gate PIN

- A 6-digit PIN has 1,000,000 values. With about 1,100 active tenants at your largest site, an attacker who guesses any valid PIN gets in, so the chance that one random guess succeeds is roughly 1,100 in 1,000,000, about 0.11%. An attacker is not trying to hit one tenant, any tenant will do.
- The lockout (5 tries, then 5 minutes) allows about 60 guesses an hour, or about 1,440 a day. Over a day, the expected number of hits is around 1.6, and over a week it is very likely that someone gets in. That assumes the guesses are uniform; people choose PINs like 123456, 000000 or birthdays, so it is faster in practice.
- The lockout is probably global per keypad, which means that anyone can also lock out every tenant with five wrong entries every five minutes. This is a denial-of-service problem, and a real one at closing time.
- Fixes: tie the gate to the app (Bluetooth or a QR code) instead of, or in addition to, the PIN; lengthen the PIN to 8 digits; use an escalating lockout (5 minutes, then 30, then an alert to a manager); do not allow weak or sequential PINs; and alert on repeated failures. Tailgating through the gate is a separate risk, so add cameras.
- If PINs are unique per tenant and stored, also check how they are stored and who can see them.

## 7. Other things worth checking before the review

- **App and account security.** The unlock right sits on the phone. Check login strength (MFA or at least device binding), what happens with a lost or stolen phone, and whether the tenant can revoke their own device.
- **Lock firmware.** Can it be updated securely? What is the physical tamper story (a lock that can be reset by removing a battery cover, or opened by a cut shackle)? Is the Bluetooth link encrypted and protected against relay attacks (a phone near the door being relayed from far away)?
- **Rollout in November.** Run the old padlocks and the new locks side by side for a trial site first. Plan for a dead battery, a dead phone and a tenant with no smartphone: you need a manager override path that is itself audited.
- **Incident response.** Decide now what you do if a credential or the signing key leaks: how you revoke everything at once, given that locks only learn about it at sync.

## Suggested order of work

1. Add signed credential expiry in the lock and a revocation path that does not rely on tenant phones (gateway or manager sync). This answers "what breaks first".
2. Make the lock the source of the audit log, and restate honestly what the record proves.
3. Narrow the maintenance codes and secure the admin panel.
4. Fix the gate PIN (longer, app-based, escalating lockout, alerts).
5. Put two-person control and a privacy and retention policy around the 60-day entry and photos.
6. Tighten helper verification and notifications.

For the insurer, the review should say what each control actually guarantees and its worst-case delay, for example "an overlock takes effect within X hours at most", and not just that the change is pushed at the next sync. If you tell me the lock vendor and how credentials are signed, I can make the points in sections 1 and 3 more specific.
