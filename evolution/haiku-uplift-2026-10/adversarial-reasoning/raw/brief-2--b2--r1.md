Here is my attack on the design, ranked by what breaks first. I've listed the assumptions I had to make at the end, since several of these findings depend on them.

## 1. Revocation does not reach basement locks (breaks first)

Removals only take effect when the lock next syncs. A lock in a basement with no signal may not sync for weeks, and it keeps accepting up to 50 cached credentials the whole time. That means:

- A removed helper keeps working until someone with signal walks past that unit.
- A tenant overlocked at 30 days late keeps access to the unit. You are still paying for the lock, and the tenant still has a key.
- A sold unit's previous tenant keeps access to the new owner's contents.

The lock has no notion of time, so nothing expires on its own. A thief who once held a helper credential can use it indefinitely.

Changes to make:
- Give every credential a hard expiry. A reasonable starting point is a rolling 7 to 14 days, renewed at each sync, so a lock that has been offline for longer than the window stops working on its own. Accept the operational cost: a tenant in a basement must sync before the window closes.
- Issue server-signed, time-limited tokens rather than static credentials, and have the lock verify the signature and the expiry itself. Revocation then becomes "do not renew" instead of "push a delete".
- Make overlock and vacate actions a hard state on the server that is enforced at the next sync, and tell the tenant and the site manager that the lock may still work until then.
- Look at a cellular or LoRaWAN gateway for the basement sites, or at least for the highest-risk units.

## 2. The gate PIN is brute-forceable at this scale

Do the arithmetic. With a 6-digit PIN there are 1,000,000 possible values, and about 1,100 are active at your largest site. The lockout allows 5 wrong entries, then 5 minutes. That gives roughly 1,440 guesses per day, and each guess hits an active PIN with probability about 1,100 / 1,000,000 = 0.11%. Expected successful entries per day are about 1.6. An outsider with patience gets in within days, and does not need to know anything about the tenants.

The lockout also has a second failure mode. If it is keyed to the keypad rather than to the PIN or the source, anyone can lock the gate for everyone for 5 minutes at a time, indefinitely.

Changes to make:
- Replace the fixed 5-minute lockout with escalating backoff: for example 1 minute, then 15, then 1 hour, then manual reset. Track failures per keypad and per PIN, and alert staff when the thresholds are crossed.
- Move to longer codes, at least 8 digits, or to a phone-based credential at the gate. Alternatively, pair the PIN with the app, so a PIN alone does not open the gate.
- Check whether the gate validates PINs against the server or locally. If locally, the revocation problem in item 1 applies here too, and a delinquent tenant's PIN may still work.
- Log every gate entry with the PIN identity, so that a PIN in use from a second location is visible.

## 3. The access log is weaker than you think

"Full access history" holds only for unlocks that are later synced from a phone that is operating normally. Several gaps follow:

- Unlocks in basements are not recorded until the phone syncs, and the phone may be one the tenant has since reset or replaced.
- The app records the unlock, which means a tenant with a modified phone, or with a credential used by a non-Corrabay client, can produce an unlock with no record. The locks have no network connection of their own, so they cannot independently confirm what happened.
- Log entries are created and uploaded by the same device whose behavior you are investigating. In a theft dispute, the tenant's own phone is the witness.

Changes to make:
- Have the lock keep its own event log with a monotonic counter, and sign entries with the lock key. Upload that log at each sync and check for gaps in the counter. A gap is evidence in itself.
- State in the tenant terms that the record is kept, what it covers, and that the lock may hold unsynced events.
- Make sure the insurer understands what the log proves. It cannot establish that a specific person was present.

## 4. Maintenance codes give site managers access to every unit

A 24-hour code for any unit, usable offline, is effectively a master key held by each site manager. There is no tenant notice, no per-unit scoping, no reason code, and no second approver. Several things follow:

- A manager can open any unit at any time and the tenant has no way of knowing.
- A code forwarded or screenshotted from the phone can be used by someone else for the full 24 hours.
- The admin panel logs that a code was created, but not necessarily that it was used. Check whether the lock records use of the maintenance code and whether that record reaches the server.

Changes to make:
- Scope each code to one unit, one window, and one stated reason, such as a work order number.
- Notify the tenant when a code is generated, and show the tenant in the app which managers opened the unit and when.
- Require a second person to approve codes, or at least log the approver, for any unit that is delinquent or in a sale or auction process.
- Review manager access by role, and remove the ability to generate codes for all units from one account.

## 5. Delinquency and auction photos need a legal review

The 60-day step puts a manager inside a unit to photograph its contents, and those photos become the auction record. Points to check with counsel before November:

- Whether your state's lien-sale or self-storage statute requires specific notices, timing, or methods before entry or sale. Many do, and they vary considerably.
- Whether entry under a maintenance code, rather than a documented lien process, creates exposure for tampering or conversion claims.
- The chain of custody for the photos: timestamps, who took them, the device, and whether they are stored unaltered. Use a write-once or hash-based store where you can.
- Whether the photos are complete enough to serve as an inventory. Photographing only some items invites disputes.

I am not giving legal advice here. Treat these as questions for counsel.

## 6. Smaller items to close

- Phone-number helpers: the design does not state how the helper is verified. Require the helper to accept an invitation in the app and confirm it. Otherwise a mistyped number, or a number later reassigned to someone else, becomes a stranger's access. Scope helper rights and give them an expiry.
- Bluetooth relay: a phone-as-key unlock can be relayed from outside the building by a device near the tenant's phone. Use challenge-response with a timing bound, or require a deliberate button press in the app.
- Lock and app firmware: confirm that the lock can be updated securely, that keys are unique per lock, and that a lock can be factory-reset or re-keyed when a unit changes hands.
- Lost or replaced phones: define how a tenant's credentials are revoked when a phone is lost, and how fast.

## Priority order before November

1. Hard expiry on all offline credentials, plus a server-enforced vacate and overlock state (item 1).
2. Fix the gate PIN lockout and lengthen codes (item 2).
3. Lock-side signed event log (item 3).
4. Scope and notify maintenance codes (item 4).
5. Counsel review of the delinquency process (item 5).

## Assumptions

I could not check any of these, so please confirm them. If any is wrong, the affected finding changes.

- The locks store credentials and do not log events internally, and the app is the only place unlocks are recorded.
- The gate keypad may or may not be connected to your server. I assumed it may validate PINs locally.
- Maintenance codes are usable offline by the lock without a further server check.
- The 50-credential cache is a cap that the server fills, and the server does not currently set an expiry on those credentials.
- The tenant's phone is the only path by which unlock events reach your server.
