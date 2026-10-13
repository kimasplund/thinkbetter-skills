# Security review: app-controlled smart locks

## Short answer

Three things break first:

1. **The front gate PIN can be guessed from the street.** Six digits and a five-minute lockout is not enough at 1,100 tenants.
2. **Removals don't take effect in units that don't sync.** A removed helper, a sold unit's old tenant, or an overlocked tenant can keep getting in, and basement units may not sync for weeks.
3. **The access history won't hold up as evidence yet.** The phone writes the log, not the lock, and whoever controls that phone can delete or edit entries before upload.

Fix these before November. The design doesn't need to be rebuilt, but the three fixes above should be in place before the first lock goes in, and the insurer should see test results for them.

## What breaks first, ranked

Scores are impact times feasibility, each 1 to 5, out of 25.

| # | Weakness | Who can exploit it | Impact | Feasibility | Score |
|---|----------|--------------------|--------|-------------|-------|
| 1 | Gate PIN guessing and keypad lockout | Anyone standing at the gate | 4 | 5 | 20 Critical |
| 2 | Revocation fails open offline | Removed helpers, ex-tenants, overlocked tenants | 4 | 4 | 16 High |
| 3 | Access log written by the phone | Tenants and managers controlling their phone | 4 | 3 | 12 Medium, but blocks insurance use |
| 4 | Maintenance codes and manager access | Insider manager, anyone with a stolen manager phone | 4 | 3 | 12 Medium |
| 5 | Helper enrollment by phone number | Anyone with the tenant's account or a recycled number | 4 | 3 | 12 Medium |
| 6 | Auction photos with no provenance | Insider manager | 3 | 3 | 9 Medium |
| 7 | Bluetooth replay and key storage | Nearby attacker with a radio | 4 | 2 | 8 Medium, pending vendor answers |

### 1. Gate PIN (Critical)

Six digits give 1,000,000 codes. With about 1,100 live PINs, roughly 0.11% of random guesses hit a real tenant. Five wrong tries followed by a five-minute lockout allows about 1,440 tries a day, so an attacker should expect around 1.6 hits per day. The lockout only slows the attacker down.

If the lockout is keypad-wide, the reverse problem also exists: anyone can enter five wrong digits every five minutes and keep every tenant out of the gate. That is a denial-of-service risk on the main entrance.

Fixes:
- Escalate lockouts (5 minutes, then 1 hour, then 24 hours), and cap total failures per day.
- Alert the manager on repeated failures from the keypad.
- Move to 8-digit PINs. At 1,100 live PINs, that drops the expected hits to about one every two months at the same attempt rate.
- Make sure PINs are not reused across tenants or derived from phone numbers, and that the keypad does not expose its PIN list.
- Confirm whether the keypad checks PINs locally or against the server. If locally, PIN changes have the same sync problem as item 2.

### 2. Revocation fails open (High, Critical for basement sites)

A removal, a unit changing hands, or an overlock reaches the lock only when a phone connects to it. A basement lock with no signal may not see that change for weeks. Meanwhile the lock accepts its cached credentials with no expiry described in the design, so a removed helper's credential stays valid until something replaces it.

Fixes:
- Give every cached credential an expiry on the lock, for example 72 hours, renewed at each sync. Tune the window per site from a signal survey. A shorter window locks out tenants with poor signal, so this is a tradeoff the owner must choose.
- Set the lock's clock at sync and check for drift, so expiry means something on an offline lock.
- When the 50-slot cache is full, evict the oldest valid credential, never a pending removal.
- On a 30-day overlock, revoke every helper added after delinquency began. The design doesn't say this happens, and the window between the overlock and the next sync is where a tenant would add helpers.
- When a unit changes hands, the new tenant's first sync must clear all old credentials. Until it does, the unit should be treated as open to the old tenant's helpers.
- Warn the tenant or manager when a lock has not synced for a set number of days.

Test: remove a helper from a unit with no signal and confirm the helper is locked out within the window.

### 3. Access history is not evidence yet (Medium, blocks insurance use)

Each unlock is recorded by a phone and uploaded later. The timestamps come from that phone. A tenant who controls their phone can delete or change records before upload. A manager's app can do the same. The lock keeps no log of its own. For offline unlocks, uploads can arrive days later, so the order of events is unclear.

Fixes:
- The lock keeps its own event log with sequence numbers and its own clock.
- The server records the time it receives each event and flags gaps in the sequence. A missing number shows that something was deleted.
- Use the lock's log, not the phone's, in any theft dispute or insurance claim.

### 4. Maintenance codes and manager access (Medium)

One manager can open any unit at any time, and the code works offline for 24 hours. The tenant is not told. A stolen or compromised manager phone exposes every site the manager covers. For contents, the insider manager is the realistic threat.

Fixes:
- Require a reason code for each maintenance code, and a second approver for any code on a unit that is delinquent.
- Notify the tenant at each entry, where local law allows.
- Restrict code generation to a small set of admin accounts with multi-factor sign-in.
- Limit each code to a visit window and review code usage monthly.

### 5. Helper enrollment by phone number (Medium)

A tenant can add a helper by number, and the helper gets full rights with no verification. A recycled number can match an old helper's record. Someone who takes over the tenant's account, through a SIM swap or a stolen phone, can add helpers.

Fixes:
- The helper accepts an invitation in the app and confirms with a one-time code.
- Helpers expire after a set period, for example 90 days, and must be renewed.
- Notify the manager when a helper is added, and show the manager the helper list.
- Re-verify helpers when the number changes hands, and require strong sign-in for account changes.

### 6. Auction photos (Medium)

The photos are the auction record, so their provenance matters. Photos taken in a no-signal unit upload later, and a manager could replace or edit them in between. Timestamps and location come from the phone.

Fixes:
- Upload photos immediately when signal allows, with a hash and a server time.
- Use two people for the entry, or log the entry and photos against the manager's code and the reason code.
- Have counsel confirm the notice, entry, and sale rules in each state before the first auction. Those rules are legal requirements, not only security controls.

### 7. Bluetooth (open questions)

The design doesn't say whether unlock commands are fixed or use a fresh challenge each time. If they are fixed, a nearby attacker who records one unlock can replay it. Relay attacks through a phone near the door are also possible if range is not limited. Credentials stored on the lock must not be readable.

Ask the vendor for: a per-use challenge, credentials held in secure storage, a measured range limit, and results from a relay test.

## Edge cases (not malicious, but they cause failures)

- **Clock drift on offline locks.** Maintenance codes and credential expiry are wrong if the lock's clock drifts.
- **Full credential cache.** At 50 credentials, the wrong eviction rule either locks out a live tenant or keeps a removed one. See item 2.
- **Stale phone.** A phone holding an old state can sync after a newer removal and restore it. The lock should reject state older than its current version.
- **Dead battery in a basement lock.** Without a network connection, a dead battery may go unnoticed. The tenant is locked out, or the lock is left open. Report battery level at each sync and alert on low charge.
- **Lost phone.** If the tenant's phone is the only way in, the recovery path must not rely on resetting the phone number, since that is an attack path too.
- **Overlock during an active helper.** A helper added before overlock may still have rights after. Handled by item 2.

## Residual risk after these fixes

- A manager acting in bad faith still has access to every unit. Only separation of duties and tamper-evident logs reduce this.
- A trusted helper can pass the unlock to someone else. The design can limit the number of helpers and log their use, but cannot stop sharing.
- A lock taken out of its door and opened with tools may expose its stored credentials, depending on vendor hardware.
- Gate and unit access records contain personal data and phone numbers. Set a retention period and confirm your privacy obligations.

## Recommendation

Fix, don't redesign. Order of work:

1. Gate lockout and PIN length (item 1).
2. Credential expiry, revocation priority, and overlock handling (item 2).
3. Lock-side event log (item 3).
4. Manager and maintenance code controls (item 4).
5. Photo provenance and legal review (item 6).
6. Helper verification (item 5).
7. Vendor answers on Bluetooth (item 7).

Before the insurer review, run these tests and send the results with the design:
- Remove a helper from a no-signal unit and confirm access ends within the window.
- Enter wrong PINs repeatedly at the gate and confirm the lockout escalates.
- Capture and replay an unlock command and confirm it is rejected.
- Delete an event on a phone and confirm the server flags a gap.

## Limits of this review

I worked only from the seven points you described. I did not have the vendor's protocol documents or the keypad firmware, so item 7 and the local-or-server PIN check in item 1 are open. Your counsel should review the entry and sale steps in item 6.
