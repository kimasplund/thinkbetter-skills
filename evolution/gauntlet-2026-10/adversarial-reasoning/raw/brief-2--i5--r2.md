# Security review: Corrabay smart-lock rollout

## Short answer

The first thing to break is revocation. Every control that takes access away (unit handover, helper removal, 30-day overlock, a lost phone) only reaches a lock at its next sync. The locks sync only when some Corrabay phone with signal happens to connect, and basement units may go weeks without that. Until then the lock keeps accepting the old credential. On launch day this means every ex-tenant, removed helper and overlocked tenant can still get in.

The second weak point is the gate PIN. The third is that your access history and your delinquency photos are less trustworthy as evidence than the design assumes.

I'm assuming the locks have a clock but no way to correct it, that the credentials are signed by your server, and that the gate keypad works independently of the unit locks. Please correct me if any of these is wrong, because some findings depend on them.

## What breaks, in order

### 1. Revoked people keep working credentials (Critical)

- **Stale access.** A former tenant, an ex-partner who was a helper, or an overlocked tenant keeps unlocking for as long as the lock hasn't synced. Nothing in the design bounds that time.
- **Overlock fails.** A tenant 30 days late who knows the overlock is coming can empty the unit before it lands. Nothing makes the push arrive on a particular day.
- **Handover.** The new tenant's unit may still open for the previous tenant. If something goes missing, you have an access dispute that the old tenant can truthfully say they were allowed to have.
- **The revoked person can block their own revocation.** The removed person's phone is the one most likely to be near the lock. If it connects first and drops or refuses the update, the revocation is delayed again. This only works if the phone is trusted to carry data it can't verify, so the answer is below.
- **Lost or stolen phone.** The tenant reports it, you revoke it on the server, and the lock doesn't know.

**Change:** make credentials expire on their own. Each credential in a lock should carry an expiry (for example 48 to 72 hours, shorter for helpers) and the lock should refuse it after that, whatever its sync state. A phone that syncs refreshes it. That turns "revoked eventually" into "revoked within N hours at worst", and you can state N to your insurer. Use a longer window only for basement units with a documented reason. Check that the lock's clock is accurate enough to enforce this, and what happens after a battery change. Also let a sync push revocations with priority, signed by the server, so any phone that passes the lock delivers them.

The cost is that a tenant who hasn't synced for 72 hours can't get in. You need a fallback that doesn't weaken the rule: a signal-free spot at each site with a refresh point, a manager-issued time-limited code, and a clear message in the app about when the credential expires.

### 2. Gate PIN: guessable and easy to lock out (High)

- **Guessing.** There are 1,000,000 possible 6-digit PINs and about 1,100 are live at the biggest site, so roughly 1 guess in 900 hits a real tenant. At 5 tries per 5 minutes that's about 1,440 guesses a day, so an attacker should find a valid PIN in roughly 15 hours of patient attempts. That's easy over a weekend, or from a car outside the gate. Tenants choose predictable PINs (1234, birth years, repeated digits), so it's faster in practice.
- **Framing.** The attacker gets in as that tenant, so your log blames the tenant. Your history will say a real customer entered the site at 2 a.m.
- **Lockout as denial of service.** If the five-failure lockout applies to the whole keypad, anyone can stop every tenant using the gate by typing five wrong numbers every five minutes. At a site with no staff on duty this becomes a real outage.
- **Uniqueness leak.** If tenants choose their own PIN and the system says "already taken", it tells an attacker which PINs are live. If the system assigns PINs, they are probably fine but should be random.
- **Stale PINs.** Check that a departed tenant's gate PIN is deactivated, and how quickly.

**Change:** use at least 8 digits, or better, let the app open the gate so the PIN is only a fallback. Escalate lockouts (5 minutes, then 30, then an alert to the manager) and make the lockout per source where you can. Assign random PINs. Put a camera on the keypad and alert on repeated failures. Treat the gate as a deterrent, since a determined person can follow a car in.

### 3. The access history is weaker than you think (High, because of the insurer)

You rely on the log for theft disputes and insurance claims. Today it has these weaknesses:

- **The log is held and delivered by the phone.** The unlock record is created by the app and uploaded later. A modified app, or a user who deletes it or turns off data, produces no record. Someone who wants no trace can simply never upload.
- **Lag and gaps.** Entries arrive at the next sync, the same gap as above. A claim filed this week may be missing yesterday's unlocks.
- **Forged or misattributed entries.** The server cannot tell a genuine unlock record from a made-up one if only the phone vouches for it.
- **Entries by helpers, managers and the gate PIN** may be attributed to the wrong person or not recorded at all.

**Change:** have the lock write its own log entry on every unlock, with a counter and a hash chaining each entry to the previous one, signed with a per-lock key, and have phones merely carry it. A gap or edit then shows up when the log is uploaded. Record the gate, the maintenance codes and the manager entries in the same way. Tell the insurer plainly that the log is eventually complete rather than live, and give them the maximum delay.

### 4. Maintenance codes and managers (High)

- A code that works for any unit goes to the manager's own phone. If the phone is lost, shared, forwarded in a chat or shoulder-surfed, that is a 24-hour key to any unit it was issued for. Check that a code opens only the one unit and that the lock enforces the 24 hours with its own clock.
- A manager can open any unit for any reason. The log is uploaded by that manager's phone, so the accountability is weakest where the power is greatest.
- A manager can issue a code at one site for a unit at another, if the panel doesn't prevent it.
- A departed employee's admin account and phone may still produce codes.

**Change:** tie each code to one unit, one manager and a reason field; email the tenant when it is used; send the manager's use of it into the same lock-signed log; require a second approval for codes outside business hours; give admin accounts per-site scope and strong sign-in; and remove access the day someone leaves.

### 5. Helpers by phone number (Medium to High)

- **Recycled or hijacked numbers.** A phone number a helper no longer has can be reissued by the carrier, or taken over by SIM-swap, and then it holds a live unlock right.
- **Helpers are never re-confirmed.** They have the same rights "until the tenant removes them", and tenants forget. Combine that with slow revocation and you have people with access that nobody remembers granting.
- **Abusive relationships.** A tenant who adds a partner and later breaks up can't instantly cut them off.
- **The 50-credential cache.** What happens at number 51? If an old entry is evicted, a legitimate tenant could lose access. If new additions are refused, a tenant can add helpers to crowd out other units' credentials. Check whether the cap is per lock or shared with other things, and what a lock does when the cache is full.
- Can a helper add other helpers? They should not be able to.

**Change:** verify the helper's phone with a one-time code when they accept; expire helpers every 90 days unless the tenant renews; notify the tenant on each helper's first use; make the cap clear and fail safely; limit helpers to unlock rights only.

### 6. Delinquency entry and the auction photos (High, for legal and privacy reasons)

- **One person, no witness.** A single manager opens a tenant's unit and photographs it. If the tenant later says items are missing, your only record is the manager's. That is a weak position for you and a risk of internal theft.
- **The photos are private data.** Contents often include ID, medical papers, family photos and bank statements. They go into a public auction listing, which also tells burglars what is stored and where.
- **Opening on a stale record.** If a payment arrived or an overlock was reversed, the lock may not know yet. Equally, a tenant who has paid is locked out in a basement until the lock syncs, which is both a customer problem and a legal exposure.
- **Timing and notice.** Check that the 60-day entry follows your notice requirements, because the log will be read by lawyers.

**Change:** two people for every delinquency entry; photos taken in the app and uploaded straight to your server, with a timestamp and the unit ID, never to a personal phone; review the photos and blur documents, faces and identifiers before any listing; keep the raw set private with a retention limit; confirm the account status on the server immediately before opening.

### 7. Phones as couriers (Medium)

Any app can connect to any lock and carry data for other locks. That is clever, but every message needs to be signed by the server and checked by the lock, not just encrypted in transit, and the phone should not be able to read or alter it. Check that:

- each lock has its own key, so one extracted key doesn't open every lock at nine sites;
- unlock requests can't be replayed or relayed from a distance;
- a rooted phone or a cloned app doesn't give extra rights;
- the lock ignores older revocation lists than the one it holds.

## Edge cases to test before November

- Dead phone, lost phone or no signal in a basement: how does a legitimate tenant get in, and how long does it take?
- Lock battery dies or the clock resets: does it fail open, fail closed or lose its cache?
- A lock sees two updates out of order.
- A tenant moves to another unit and the first unit's helpers are not cleared.
- Two phones sync the same lock simultaneously.
- A phone number is reused (new tenant gets an old helper's number).
- Physical attack on the shackle or lock body, and any mechanical override key. If there is one, who has it?
- The server is down: what do locks and the gate do?

## What to do, in priority order

1. Credential expiry on every lock, with a documented maximum revocation delay.
2. Replace the 6-digit gate PIN with 8+ random digits or an app-based entry, with escalating lockouts and a camera.
3. Lock-signed, hash-chained access logs that include maintenance codes and the gate.
4. Tighten the maintenance codes: one unit, logged, tenant notified, second approval after hours.
5. Two-person delinquency entries; photos uploaded directly and redacted before they reach any listing.
6. Verify and expire helpers.
7. Pilot at one site for a few weeks before nine, and measure the real gap between a revocation and a lock obeying it.

## Residual risk

After these changes, someone with a valid credential can still use it for up to the expiry window, and an authorised insider can still misuse access, although both would now be logged and attributable. Tailgating at the gate and physical attacks on the locks remain. Tell the insurer these numbers (maximum revocation delay, maximum log delay, expiry window) rather than describing the system as real-time, because the design cannot honestly promise that.

My confidence is about 75%. The main unknowns are how the lock verifies codes and keeps time, whether the gate keypad lockout is global, and what your tenant agreement says about entry at 60 days.
