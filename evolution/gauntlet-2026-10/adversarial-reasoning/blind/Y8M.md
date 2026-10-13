# Corrabay smart-lock rollout: security review

I've assumed the locks check credentials on their own with no network, that your server signs what it sends them, and that the maintenance code is checked by the lock offline. If any of that is wrong, the affected findings change. I flag where.

## What breaks first

**1. The gate PIN falls within about a day.** Your 1,100 tenants hold 1,100 valid PINs out of 1,000,000 possible, so a random guess is right about 1 time in 900. The lockout allows 5 tries every 5 minutes, which is about 1,440 guesses a day on one keypad. That works out to roughly 1.5 valid PINs found per day, with no need to target anyone. Two further problems:
- If the lockout applies to the whole keypad, one person standing there can lock out every tenant at the site indefinitely.
- A found PIN gets the attacker onto the site and into the corridors, where they can attack locks physically.

**2. Revocation is only as fast as the slowest sync, and the courier can be the person being revoked.** An overlock, a removed helper or a changed tenant reaches the lock only when some phone running the app is near it and has signal. In a basement that could be days or never. Until then the old credential keeps working, which matters in three cases:
- A tenant 30 days late can empty the unit before overlock takes effect. Your auction and recovery process depends on that not happening.
- A removed helper, or an ex-partner of a tenant, keeps access.
- The phone that carries the revocation to the lock may be the removed person's own, and a modified app can quietly drop it. Be clear about this: nothing in the design stops a courier from withholding or replaying an older, still-valid lock state.

**3. The access history won't hold up as evidence.** Entries are recorded by the phone and uploaded later. That means:
- A tenant or helper can delay, drop or alter entries.
- A thief using a stolen phone or a valid credential produces entries only if their app uploads them.
- An unlock that was never uploaded looks like no unlock.
- Lock clocks drift without a network, so timestamps in a dispute can be challenged.
- An insurer or a tenant's lawyer will ask how you know the log is complete. Today the answer is that you don't.

## Other significant findings

**Maintenance codes are a master key with weak accountability.**
- A 24-hour code that goes to the manager's phone can be forwarded, screenshotted, or taken with the phone.
- Nothing ties it to a reason, a second person, or a tenant notification.
- It is also your best insider-theft tool: a manager can enter an occupied unit for a day, and the only record is whatever that manager's app uploads.
- Whoever takes over an admin panel account can generate codes for every unit at every site. That makes the panel your most valuable target. Check whether manager accounts are scoped to their own site and have MFA.

**Helpers added by phone number.**
- A typo in the number gives a stranger the same unlock rights as the tenant.
- Recycled numbers and SIM swaps give the same result later, with the person who now holds the number never having been vetted.
- If helpers can add other helpers, or remove the tenant, access spreads and the tenant loses control. Check this.
- Credentials are capped at 50 per lock. If a helper can add many others, or a malicious tenant adds many, the cache fills and a legitimate credential may be refused or silently evicted. Find out which.

**The 60-day photos create a privacy and theft problem.**
- Photos of the full contents of a unit, with no review, become a public listing. They will show ID documents, medication, correspondence and children's items, and photo metadata can reveal the site and the unit.
- A listing that shows high-value contents and the site tells thieves where to go before the auction.
- A single manager opening the unit alone and photographing it is also a weak record in a dispute. A tenant can say items went missing, and your only evidence is that manager's photos.

**Smaller items to check with the lock vendor.**
- Whether a Bluetooth unlock can be relayed from a distance by an attacker who captures the tenant's phone signal.
- Whether keys are per-lock. If one key serves all locks, a single lock taken apart on a bench compromises every site.
- Whether old lock state can be replayed to a lock after a revocation. Locks should reject any state older than the one they hold.

## What to change

**Before November, in this order:**

1. **Gate PIN.**
   - Lengthen it to 8 digits or more, or move the gate to the app, a fob, or PIN plus app.
   - Replace the flat lockout with a backoff per source that does not shut out everyone else.
   - Alert on repeated failures.
   - Add a camera on the keypad.

2. **Make credentials expire, so a missed sync can't leave access open.**
   - Give every credential, helper credentials included, a short life, for example 7 to 14 days, and have the lock refuse expired credentials.
   - Tenants who visit often renew automatically on any sync. A tenant who stops showing up simply loses access, which is the right default for overlocked and departed tenants.
   - Add a revocation version number so a lock rejects any state older than the one it holds.
   - Sign every server message to the lock end to end, so the phone is only a courier. Where basements allow, put a small Bluetooth hub at each site so locks sync without relying on tenants.

3. **Make the access history tamper-evident.**
   - Have the lock keep its own log, signed and chained so gaps are visible, and upload it at the next sync.
   - Treat any unit whose log goes unuploaded for more than a set number of days as an open item for the site manager.
   - Say in the insurer review that the log proves what it recorded, and describe how gaps are detected.

4. **Maintenance codes.**
   - Make each one single-use, tied to one unit, valid for about 2 hours.
   - Require a logged reason, and a second approver for any occupied unit.
   - Notify the tenant of each entry.
   - Scope manager accounts to their own site, require MFA, and review the issuance log weekly.

5. **Helpers.**
   - Require the helper to confirm by SMS code before they get access.
   - Cap the number of helpers and re-confirm periodically.
   - Make clear that helpers can't add helpers or remove the tenant.
   - Show the tenant a list of who has access.

6. **Auction process.**
   - Require two staff for the 60-day opening, with a timestamped, scoped entry through the process above.
   - Review and redact photos before they are published.
   - Strip metadata and keep the originals privately as your record.
   - Don't name the site in the public listing before the auction.

**Choices for you:**
- If you can't have expiring credentials on day one, an interim step is to push overlocks to the hub or have the site manager physically check the lock at the 30-day mark.
- Be ready to tell the insurer that revocation has a window, state how long it is under the new design, and say what covers it.

## What remains after these changes
- A tenant could still pass on their own credentials or phone on purpose. This is also true of keys.
- Bluetooth relay attacks and physical attacks on a lock depend on the vendor's hardware. Get their written answers before you sign off.
- During a server outage, locks keep honoring cached credentials until they expire. That is why the expiry window should be short.

My confidence is high on the PIN, revocation and log findings, which follow from the design as you described it. It is moderate on the maintenance-code and helper findings, which depend on details I assumed.
