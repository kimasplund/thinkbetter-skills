**Short answer:** the first thing to break is revocation. Everything else (audit trail, gate PIN, maintenance codes, auction photos) is weaker than it looks, but revocation is the one that fails in ordinary use, with no attacker involved.

Assumptions: the lock verifies credentials locally (signed tokens or stored IDs), its clock is a simple RTC, and the app/server are otherwise sound.

## Revocation is only as fast as the next sync (breaks first)

Your locks learn about changes only when some Corrabay app, on a phone with signal, connects to them. Basement units may go weeks without that. The failure cases:

- **Overlocked tenant:** the lock is the enforcement point for the 30-day overlock, but it keeps accepting the tenant's cached credential until it syncs. The tenant keeps access, and you may have a legal problem if they remove goods after the overlock.
- **Unit changes hands:** the previous tenant, and every helper they added, can still open the unit until sync. A new tenant's goods are exposed to the old tenant's circle.
- **Removed helper (the ex-partner or ex-employee case):** the removal is often made because of a falling-out, which is when the risk is highest. The helper can keep opening the lock offline.
- **Attacker-controlled delay:** a removed person can keep their phone in airplane mode or avoid the app so the lock never receives the update. The lock never learns it has been out of touch.

**Changes**
- Give every credential a short expiry enforced by the lock (for example 24 to 72 hours), refreshed whenever the tenant's app syncs. A tenant who goes underground for a week and returns simply re-syncs at the entrance, where there is signal. Revocation delay is then bounded by the expiry, not by the sync luck.
- Use a revocation list or monotonically increasing version counter pushed to the lock. Make every app that connects to any lock, including the manager's and staff apps, carry the latest revocation data for that site. Opportunistic sync becomes a strength.
- Put a gateway or a BLE hub with a data connection in the basement areas of each site. That removes the "no signal" assumption altogether and is probably cheaper than the incident it prevents.
- Treat the 50-credential cache as a threat surface. Does a tenant plus helpers ever need 50? Cap it lower and confirm what happens at overflow (does the lock evict the oldest? Could an attacker flood it by adding phone numbers?).
- Be explicit with tenants and in your terms about the worst-case revocation delay. The insurer will ask for that number.

## Offline credentials and the lock itself

- **Replay and cloning:** confirm the Bluetooth exchange uses a challenge-response with a fresh nonce, not a static token an eavesdropper can record and replay. Test it with a sniffer.
- **Clock:** offline expiry depends on the lock's clock. Check whether it can be set or rolled back through the app, and how it drifts. Maintenance codes (below) depend on the same clock.
- **Firmware and keys:** are keys per-lock, or shared across the fleet? A shared secret means one extracted lock compromises all nine sites. Is firmware signed, and can it be updated over the air? Is there a physical override (key or battery access) and who holds it?
- **Physical:** cheap smart locks are often defeated mechanically (shackle, cutting, shimming). Ask the vendor for independent test results, and note a smart lock is no stronger than a padlock against bolt cutters.

## Helpers added by phone number

- A phone number is a weak identity. Number recycling, SIM swap, or a typo grants access to a stranger. Require the helper to verify the number by SMS code and install the app, and notify the tenant whenever a helper is added or first uses the lock.
- Helpers have the same rights as tenants. Can a helper add other helpers? Remove the tenant? Check that helpers cannot escalate and cannot alter the tenant's PIN or payment details.
- Consider limiting helper rights (for example, no gate PIN, optional time windows).
- Account takeover of the tenant's account (weak password, SMS reset) gives an attacker the unit and the ability to add themselves. Require MFA or at least re-authentication to add a helper, and alert the tenant.

## The access history is weaker than you believe

You describe it as "a full access history for theft disputes and insurance claims". It is not full:

- Logs are recorded by the app and uploaded at the next sync. A tenant or thief who wants no trace can use a phone that never uploads, or delete app data. Offline unlocks in basements are exactly the ones that lag.
- If the app is the recorder, a modified app can lie. The lock should write signed, append-only entries (with a counter so gaps are visible) and the server should verify them. Then a missing entry shows up as a gap, not silence.
- Gaps themselves are evidence. Record "last sync time" per lock, and tell insurers that "no log entry" means "no known entry" until the lock has synced after the incident date.
- In a theft dispute, you cannot prove who was holding the phone. Logs show a credential, not a person. Do not promise more than that.
- Privacy: logs tied to phone numbers are personal data. Set retention and access rules.

## Maintenance codes

- They go to the site manager's own phone. That makes the manager's phone and account a master key for the unit: if the account is compromised, an attacker can generate codes for any unit at any site. Scope them: per site, per manager, with MFA on the admin panel.
- A 24-hour code is long. Offer codes valid for one entry or one hour, tied to a ticket or reason.
- Make every generation and use appear in the access history, and tell the tenant (a notification) when one is created for their unit. Without that, insider abuse is invisible.
- Codes are validated offline, so they cannot be revoked within the 24 hours. Consider that when a manager leaves the company: disable the account immediately and ensure the lock-side expiry limits damage.
- Separate duties where practical: whoever generates a code should not be the only person who can delete the log.

## Delinquency access and the auction photos

- At 60 days the manager opens the unit and photographs everything. That is a one-person, unwitnessed entry into a tenant's goods. It creates a dispute risk ("there was a watch in there") and an insider-theft opportunity. Require two people, or a person plus a recorded camera, and log it. Check state law on lien notices and entry rules.
- The photos are your record of contents, but also a sensitive data set: documents, IDs, medical items, and photos of people may appear in the frame and the public listing. Redact before publishing, restrict internal access, and set a retention period. Store them where the manager cannot quietly delete or replace them (server-side, timestamped).
- Consider sealing the unit and having the inventory done in a documented process, not an ad hoc phone camera.

## Gate keypad

- A 6-digit PIN has 1,000,000 values. At the largest site, about 1,100 active tenants means roughly 1 in 900 random guesses is a valid PIN. The lockout is 5 attempts per 5 minutes, so one keypad allows about 1,440 guesses per day; the expected time to hit a valid PIN is roughly 15 hours of continuous guessing. That is practical for someone parked there overnight, and the lockout does nothing to stop a slower, patient attacker who guesses in the shadow of ordinary traffic. Tenants also choose birthdays, 123456, and repeating digits, which sharply reduces the real search space.
- A PIN that is unique to each tenant must be assigned by you, not chosen (otherwise uniqueness leaks information: "that PIN is taken" tells an attacker a valid one). If tenants choose, make the "taken" message the same as any other rejection.
- The PIN is shared with helpers and relatives, so it is not an identity. A PIN reveals nothing about who entered unless you tie each helper to a separate PIN.
- Changes: raise the length to 8 digits, use escalating lockouts (5 min, then 30 min, then 24 h, with an alert to the manager), add cameras and ANPR at the gate, and consider moving gate access to the app/Bluetooth credential, with the same short-expiry revocation as the locks. Remove a tenant's PIN promptly on move-out or overlock.
- Gate keypads are typically online, so revocation is immediate there. That is a good argument for the gate to do the check the lock cannot.

## Operational and fleet risks

- **Single points of failure:** if the server or admin panel is down, can tenants still unlock (cached credentials work), and can staff still help someone locked out? A server outage during a mass sync or a bad push could lock out nine sites, or open them. Stage rollouts and keep a documented emergency procedure (physical override, who holds it).
- **Migration in November:** during cutover, old padlocks and new locks coexist. Avoid a window where a unit has no lock or two valid access methods.
- **Battery:** what happens when the battery dies? A dead lock must fail closed to the outside and have an external power or key override that is not itself an easy bypass. Alert on low battery through sync data.
- **Admin panel:** audit roles, MFA, session timeouts and who can see all units.

## What I would put in the insurer review

1. Stated worst-case revocation delay and the mechanism that bounds it (expiry and refresh).
2. Lock-signed audit logs with gap detection, and an honest statement of what the logs can and cannot prove.
3. Scoped, short-lived, logged, tenant-notified maintenance codes with MFA on managers.
4. Two-person, recorded process for delinquency entry and photos, with data retention and redaction rules.
5. Gate hardening (longer or app-based credentials, escalating lockout, cameras).
6. Fleet key management, signed firmware, and an incident and lockout runbook.

## Priority order

1. Credential expiry and revocation (fix before November).
2. Gate PIN (cheap, quick).
3. Maintenance code scoping and notifications.
4. Signed lock-side logs.
5. Delinquency entry procedure.
6. Helper verification and escalation limits.

Things I could not check from your description and would verify with the vendor: the cryptographic design of the Bluetooth exchange, key sharing across locks, the lock clock, firmware signing, and what the 50-credential cache does when full.
