# Security review: Corrabay smart locks

**Bottom line:** The design breaks first wherever it depends on a phone happening to pass a lock. Basements with no signal are where the failures concentrate. I would not roll this out to all nine sites until the first four changes below are in place, or until you have accepted the remaining risks in writing for the insurer.

## What breaks first

1. **Removed access survives in basements.** A removed helper, a sold unit's former tenant, and an overlocked tenant all keep working until some Corrabay app syncs with that lock. In a basement unit with no signal, the lock keeps accepting every cached credential, possibly for weeks. Worse, the phone that carries the revocation is usually the tenant's own. A tenant who wants to keep access can run a modified app that drops the revocation, or simply stops letting the app sync. The 30-day overlock is therefore not enforced in exactly the units where enforcement matters most.

2. **The gate keypad can be guessed.** With 1,100 live PINs out of 1,000,000 possible, a random guess matches a real tenant about 0.11% of the time. If the lockout is per keypad (5 wrong entries, then 5 minutes), an attacker gets about 1,440 guesses a day, which means roughly one to two valid PINs a day. A month of that is a steady stream of gate entries, each one borrowing a real tenant's identity in the logs. The fix is a lockout that counts per PIN and escalates, plus a longer PIN.

3. **The access history will not hold up in a theft dispute or insurance claim.** Unlocks are recorded by the tenant's phone and uploaded later. A tenant can avoid the upload by not syncing, or a modified app can drop or edit entries. The record is complete only for honest users, and the people with a reason to hide an entry are exactly the ones who control the phone that writes it. An adjuster will ask who controls the record, and the answer is the party it might incriminate.

4. **The maintenance code is an unsupervised master key.** Any site manager can generate a 24-hour code for any unit, with no second approval and no recorded reason. It works offline and goes to the manager's own phone. The same manager who opens a unit also photographs its contents for the auction listing. One person therefore controls entry, the inventory record, and the sale. A dishonest manager can remove items, then photograph whatever list suits them. The only corroboration is the app log from item 3.

5. **Photos are not evidence on their own.** The photos are taken by the party who benefits from the auction, with no independent timestamp and no second witness, and they can be staged or retaken. Treat them as the start of a record, not the record.

6. **Bluetooth relay.** Unlocking is a radio command from a phone within range. An accomplice standing at a unit door with a relay device can open it while the tenant's phone sits in a pocket nearby. Nothing in the description requires the tenant to confirm an unlock.

7. **Helpers added by phone number.** If the app does not verify the helper, whoever holds a reassigned or ported number gets full unit access. If helpers can add other helpers, one compromised tenant account spreads access across many units. I could not tell from the description whether helpers can add helpers; please check.

8. **The 50-credential cache can be pushed out.** When a lock is full, adding a credential may evict a legitimate tenant or helper, who is then locked out offline. A tenant with many helpers, or an attacker who adds many, can displace real users. The eviction order is not described.

9. **The admin panel and the vendor are shared trust.** One stolen manager login can open units at all nine sites. Lock firmware and the app's third-party SDKs are also part of the chain that decides who gets in.

## What to change, in priority order

1. **Give every site a network path to its locks.** A gateway or bridge in each building, reachable from the basements, lets revocations reach locks in minutes rather than whenever a phone passes by. This is the largest single fix, and item 1 depends on it.
2. **Make offline credentials expire.** Each credential carries a validity window (for example 72 hours) that the lock enforces with its own clock. Renewal requires a fresh sync. A revocation then costs at most one window. For units that cannot sync, shorten the window.
3. **Record unlocks on the lock and sign them.** The lock stores each event and signs it with a key the phone cannot forge, and events are collected through the gateway. The record then exists even when the phone is hostile.
4. **Fix the keypad.** Count failures per PIN as well as per keypad, escalate the lockout (for example, 10 wrong entries gives one hour, then longer), alert management on repeated failures, and move to an 8-digit PIN. Confirm whether the gate keypad receives revocations at all.
5. **Tighten maintenance codes.** Require a second manager's approval and a work order reference, limit validity to a few hours, make the code single-use, and send the tenant an automatic text whenever a code is used on their unit.
6. **Make the delinquency inventory independent.** Two people attend, each photo is timestamped and hashed at capture by the app, and the entry is written to the sealed log from item 3. For auctions, consider a third-party inventory service.
7. **Verify helpers.** Send the helper a one-time code, require the tenant to confirm, block helpers from adding helpers, and notify the tenant whenever a helper is added.
8. **Protect the cache.** Alert when a lock reaches 45 of 50 credentials. Evict the credential that expires soonest, and never evict a tenant's own credential to make room for a helper.
9. **Harden admin access.** Require multi-factor sign-in for every manager, scope managers to their own sites, and log every code they generate.
10. **Stop relay unlocks.** Require the app to be open and the phone unlocked, or a deliberate tap, before a Bluetooth unlock. Consider a short distance limit at the lock.

## Edge cases to test

- **Change of ownership mid-sync.** The old owner's phone still holds valid credentials, and the new owner's phone issues new ones. Both can open the unit until the next sync.
- **Dead battery.** A lock with no battery has no fallback unless there is a mechanical key or an emergency override. Battery replacement needs a visit and a recorded event.
- **Clock drift.** Time-limited credentials fail or fail open if a lock clock drifts or resets, such as after a power cut. Test a long outage.
- **Full cache.** A tenant with the maximum number of helpers, plus one more, should get a clear message and a defined eviction result.
- **Physical attack on the lock body.** A smart lock may be weaker than a hardened padlock and its hasp, so cutting or drilling could be easier than any electronic attack. Test the body and hasp against the same tools a thief would bring.

## Residual risk after these changes

- A physical attack on the lock body, unless hardened, still bypasses everything electronic.
- Managers keep some reach by design. Logging and second approval reduce misuse but do not remove it.
- If photos stay in manager hands, the auction record is still weaker than it looks.
- An 8-digit gate PIN is still guessable with sustained effort, so the escalating lockout and alerts carry the load.
- Vendor firmware and SDKs remain a supply chain you must review and monitor.

## How sure we are

I am fairly sure about the basement revocation problem and the keypad arithmetic, since both follow directly from the description. I am less sure about four things that would change the advice: whether the lock stores its own event log, whether credentials already carry an expiry, whether helpers can add helpers, and whether the gate keypad is networked. I have assumed the locks have a working clock and that the phone is the only sync path. Please confirm those four facts with the vendor before the insurer review.
