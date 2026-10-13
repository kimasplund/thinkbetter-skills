**Short answer:** the first thing to break is revocation. The lock only learns about a removal, an overlock or a unit transfer at its next sync, and sync depends on a phone with signal. Everything else matters less than that, though the gate PIN and the evidence trail are close behind. Assumptions: the lock has a real-time clock but no network, and credentials are validated on the lock against a stored list or signed tokens.

## Revocation lag (breaks first)

Overlock, helper removal and unit handover all wait for the "next sync". For a basement unit that might be days or weeks. Consequences:
- A removed helper, an ex-tenant or an overlocked delinquent tenant can keep opening the unit. The overlock for non-payment may not enforce at all, which also undermines the 60-day auction process legally.
- An ex-partner or ex-employee who was a helper can keep access after the tenant removes them. This is the most likely real-world incident, and it is a safety issue, not only a theft one.
- Cached credentials (up to 50) have no stated expiry, so a stale credential is valid indefinitely.

Changes:
- Give every credential a short expiry (for example 24 to 72 hours) that the lock enforces with its own clock, refreshed on each successful sync. Revocation then has a hard upper bound even if the lock never hears about it.
- Add a signed revocation list that rides along with any phone that syncs. Because any Corrabay app can relay to any lock, push revocations to nearby phones, not only to the affected tenant's phone. Staff phones on their rounds should sync every lock they pass.
- Put a sync point (a signal-bearing relay or a staff routine) near basement clusters.
- For overlocks, have staff do a physical step, since you cannot rely on the lock hearing it: a staff overlock, or a visible tag and a site-manager check.
- Tell tenants plainly that removing a helper is not instant in low-signal areas.

## Offline trust and the sync channel

- The phone is a courier between lock and server. A malicious or modified app can drop, delay, replay or alter updates, for example by never forwarding a revocation or by uploading falsified logs. Sign everything server-side and verify on the lock. The lock should reject unsigned or stale-versioned updates, and use monotonic version numbers so old state cannot be replayed.
- Bluetooth relay and replay: capture the unlock exchange and replay it. Use challenge-response with a fresh nonce per attempt, and per-lock keys, never one key shared across locks or sites. One extracted key must not open nine sites.
- Lock clock drift or tampering matters once you rely on expiry. Have the server sync time on each connection, and limit how far a lock accepts a time jump.
- Physical attack: the shackle and body matter as much as the crypto. Check the lock's cut resistance, and whether the battery cover or reset path is reachable from outside. Define what happens when the battery dies (an external power contact or a mechanical override, plus staff access).
- Firmware update path: signed firmware only, and rollback protection.

## Helpers by phone number

A phone number is a weak identity. Recycled numbers, SIM swaps and typos hand access to the wrong person. Changes: confirm the helper with an SMS or in-app code before activating, notify the tenant on first use, show tenants a list of active helpers with last-use time, cap helper numbers, and allow time-limited helpers. Decide whether helpers can add other helpers (they should not).

## Maintenance codes

A 24-hour code sent to the manager's own phone is a master key to any unit, so it is the highest-privilege item in the design.
- Require a reason and a ticket reference, and notify the tenant when a code is issued.
- Single use or short window, tied to one unit, logged with the manager's identity, and visible in a monthly review.
- Admin panel: mandatory MFA, per-site scope (a manager at site A cannot issue codes for site B), and separation of duty for high-risk cases such as units in delinquency.
- Phone forwarding or screenshots mean the code can travel. Time-boxing and logging limit that.

## Logs as evidence

You rely on the access history for theft disputes and insurance claims, but the logs are weaker than they look:
- Logs only arrive at the next sync, so a lock that is never reached has no record for the period in question, and an absence of entries is not proof of no entry.
- Logs come from the phone, so they can be omitted or forged, and denied-attempt events and entries by maintenance codes may not be captured at all.
- Have the lock write its own signed, hash-chained, sequence-numbered log with timestamps. Gaps in sequence numbers are then detectable. Record failed attempts, revocation events, and which credential (tenant, helper, maintenance) was used.
- Be honest in the insurer review: for any unit not synced since the incident, the log is incomplete. Consider adding door or camera coverage at the site level as corroboration.
- Retention and privacy: define how long logs are kept and who can see them. Helper phone numbers and access times are personal data.

## Delinquency access and photos

At 60 days a manager opens the unit and photographs the contents. This is both a legal and a security problem:
- One person alone with a unit, with a maintenance code, is a theft and accusation risk in both directions. Require two people (or a witness plus video), a logged entry, and a written inventory.
- Photos may reveal personal documents, ID, medical items and the like. Restrict who can view them, store them encrypted, strip location data, redact before listing, and delete on a schedule. Public auction listings must not show anything sensitive.
- Check the legal notice requirements in each jurisdiction before the lock lets anyone in, and make sure an overlocked tenant can still be given supervised access to retrieve necessary items if the law requires it.
- Property that is auctioned may be claimed later, so the photos are evidence. Keep them tamper-evident (hash and timestamp at capture).

## Gate keypad

A 6-digit PIN has 1,000,000 possibilities. With about 1,100 tenants at the largest site, roughly 1 in 900 random guesses hits a valid PIN. Five tries then a 5-minute lockout allows about 60 guesses per hour, around 1,440 a day, per keypad. That gives an attacker about 1 expected hit per 600 days of continuous guessing at random, which is slow, but:
- PINs people choose are not random (1234, birthdays, repeated digits), so a targeted attempt does far better. If the system lets tenants pick PINs, the effective space is much smaller. Assign random PINs and block weak ones.
- The lockout is probably per keypad, so it is also a denial-of-service lever: anyone can lock out real tenants every 5 minutes. Consider an escalating lockout (5 minutes, then 30, then 4 hours) and an alert after repeated lockouts.
- Because the PIN is unique per tenant, a valid hit identifies a person, and shoulder surfing yields a reusable credential. Tenants share PINs with friends. Prefer per-visit or app-based gate entry, add cameras at the gate, and rotate PINs on unit changes.
- A PIN also needs revocation when a tenant leaves or goes into overlock (see section 1).
- Tailgating through an open gate bypasses everything, so add gate cameras and an anti-tailgate cycle.

## What to do before November, in priority order

1. Credential expiry on the lock plus a signed revocation list pushed through any phone (section 1). This single change turns "unbounded" into "bounded".
2. Per-lock keys, nonce challenge-response, and signed server updates (section 2).
3. Lock-generated signed, hash-chained logs, including failed attempts and maintenance-code use (section 5).
4. Maintenance code controls: MFA, per-site scope, tenant notice, audit (section 4).
5. Two-person rule and photo handling for delinquency entry (section 6).
6. Helper verification and visibility (section 3).
7. Gate PIN assignment, escalating lockout and cameras (section 7).
8. Pilot at one site first, run a red-team day (attempt replay, a modified app, a removed helper in a basement unit), and record the measured worst-case revocation time. Put that number in the insurer review.

## For the insurer document

Describe the controls as bounds ("a revoked credential works for at most N hours") rather than as promises of instant revocation, list residual risks (offline lag, physical attack, phone-based identity), and state your incident response: how a lost tenant phone, a lost staff phone, or a suspected stolen master code is handled, and how you would lock a unit down by hand. I can draft the review document in the insurer's format if you tell me what they require.
