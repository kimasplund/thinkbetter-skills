**Short answer:** the first thing to break is revocation. Almost everything you rely on (removal, overlock, unit transfer, audit history) depends on a lock syncing, and a lock only syncs when someone's phone with signal happens to connect to it. The second is the gate PIN, which can be guessed.

Assumptions: I haven't seen the app or lock firmware. I'm assuming the lock can't verify credentials against a server, has a clock that may drift, and that credentials are signed tokens or stored IDs. Check each point against the real design.

## 1. Revocation lag (breaks first)

Removals, overlocks and transfers only reach a lock at its next sync. Locks in no-signal basements may go days or weeks without one, and they only sync when some Corrabay app connects to them. The cached credentials stay valid offline in the meantime.

Consequences:
- A former tenant, a removed helper (e.g. an ex-partner or ex-employee) or an overlocked tenant keeps access until the lock syncs. Overlock is your main rent-enforcement tool, so it can silently fail.
- An attacker who knows they are being removed can simply stay out of sync. Switching the phone to airplane mode doesn't matter, because the lock is what needs the update.
- A new tenant of a transferred unit can find the previous tenant's cached credentials still working.

Changes:
- Give every credential an expiry (for example 24 to 72 hours), refreshed whenever the phone syncs. A stale credential then fails closed. Pick the window by weighing it against how long tenants go without signal.
- Use a short expiry for helpers, and a short one for any unit flagged for transfer or overlock.
- On a transfer or overlock, push the change from the gate and office too. A phone or tablet that physically visits the lock can force the sync. The overlock procedure should include a staff step that confirms the lock acknowledged the change, rather than assuming it did.
- Report lock sync age per unit in the admin panel, and alert on locks that haven't synced within a threshold. Treat those units as exposed.
- Say in the insurer review that offline acceptance has a bounded window, and state the number.

## 2. Gate PIN brute force

A 6-digit PIN has 1,000,000 values. At 5 tries per 5 minutes that is about 1 try per minute, or roughly 1,440 per day per keypad. If the PINs are unique per tenant and the largest site has 1,100 tenants, about 1 in 900 random guesses hits a valid PIN. So an attacker expects a valid PIN in about 900 guesses, roughly 10 hours of guessing at the lockout rate, or less than a day even if lockouts are spread out. Attackers who know that tenants pick weak PINs (birthdays, 123456, 000000) will do far better.

Uniqueness also leaks information. A rejected PIN means that PIN belongs to nobody, and it tells the attacker which codes are taken once any one is observed.

Changes:
- Don't rely on a global per-keypad lockout alone. Use escalating lockouts (5 minutes, then 30, then 24 hours) that reset only after a valid entry, and alert staff on repeated lockouts.
- Move to longer PINs (8+ digits) or PIN plus a second factor such as the app, a fob or a plate/QR check.
- Block trivial PINs (repeated or sequential digits, common patterns). Don't assign sequentially.
- Camera coverage of the keypad, and an alert on a burst of failures.
- Check that tenant-chosen and unit-derived PINs aren't predictable (e.g. last digits of phone number or unit number).

## 3. Audit log is weak evidence

You plan to use the access history for theft disputes and insurance claims. But unlock events are recorded by the app and uploaded later.

Problems:
- The record comes from the phone, which the tenant controls. A modified or offline app can drop or alter entries, and events from a phone that is never opened again may never arrive.
- Events arrive late, so for the period of a dispute the history can be incomplete. A missing event is not evidence that nobody entered.
- Without the lock signing entries, timestamps can't be trusted. Lock clocks drift, and phone clocks can be set by the user.
- Offline unlocks by revoked users (see section 1) look legitimate.

Changes:
- Have the lock itself keep a tamper-evident log: each entry has a sequence number, the lock's own timestamp, the credential ID, and a signature or hash chain. The app only carries it to the server. Gaps in sequence numbers then show up as missing data.
- Record sync time and clock offset so you can state how reliable a timestamp is.
- Stop describing it as a "full" history in the insurance review. Describe it as complete up to the last sync of each lock, and report which locks have gaps.
- Add independent evidence for high-value claims: cameras at the aisle and gate.

## 4. Maintenance codes

The 24-hour code goes to the manager's own phone. That means:
- Any manager can generate a code for any unit, on any site, with no reason recorded. That is an insider-theft path, and with 9 sites you have many people with that power.
- The code lives on a personal phone, where it can be shared, screenshotted or kept in messages, and it works for 24 hours.
- It is not clear whether the code survives a lock sync, whether it is single-use, or whether it appears in the audit log tied to a named person.

Changes:
- Restrict a manager to units at their own site, require a ticket or reason (work order, overlock, auction), and log who generated it and for which unit.
- Make codes single-use or short (for example 1 to 4 hours), tied to a named person, and revocable.
- Notify the tenant when their unit is opened by staff (with reason) and make it visible in their app history.
- Review code generation counts per manager monthly.

## 5. Delinquency photos at 60 days

Opening the unit at 60 days and photographing the contents creates two problems.
- Privacy and sensitive data: the photos may capture documents, ID, medical items, firearms, family photos. The auction listing could expose personal information publicly. Check your lease terms and the law of the jurisdictions where you operate on entry, notice and sale. I can't advise on that, so get legal review.
- Evidence and liability: the photos are your record of what was inside, so a tenant who later claims items were missing will point at who had access. Controls over who can open, who holds the photos and how long you keep them matter.

Changes:
- Two staff present, or a witness, and a logged entry with a reason; photos taken with a company device, uploaded to restricted storage, with timestamps.
- Redact documents and personal items before public listing, and use only a limited set of listing photos. Keep the full set private and delete it after the retention period.
- Notice requirements before entry should be documented in the review.

## 6. Helper handling by phone number

Helpers are added by phone number. Phone numbers get recycled, can be spoofed, and can be SIM-swapped.
- If a helper's number is reassigned, a stranger could inherit access, if enrolment is tied to the number alone.
- Tenants can't see what a helper actually did unless the history shows it.

Changes: verify the number with a one-time code at enrolment and at each new device, bind credentials to the device, give helpers an expiry by default (e.g. 30 or 90 days) with a renewal step, and notify the tenant on each helper's first use.

## 7. Smaller items

- 50 cached credentials per lock: define what happens past 50, and what is evicted. A full cache must not cause silent failure or let old entries persist.
- Bluetooth: ask the vendor about replay protection, relay attacks (an unlock request relayed from a tenant's phone to the lock), pairing, and firmware updates. Relay is a known weakness of phone-proximity entry, so consider requiring an explicit tap on the phone.
- Lock firmware updates also depend on the same sync path, so a firmware flaw may stay unpatched for a long time.
- Battery death: define a manual override and who holds it, since it is also an attack path.
- Admin panel accounts: require MFA, per-site roles, and log every action.
- Rollout in November: don't switch all nine sites at once. Pilot one site, and keep a rollback plan.

## Priorities for the insurer review

1. Credential expiry and sync-age monitoring (closes the biggest gap).
2. Gate PIN hardening.
3. Lock-signed, tamper-evident audit log, and honest wording about its limits.
4. Maintenance code controls and staff-entry logging.
5. Photo handling and privacy rules.
6. Helper verification and expiry.

For the written review, I'd present each as: threat, current control, residual risk, change, owner and date. If you share the app's credential format and the lock vendor's documentation, I can tighten the offline expiry numbers and the Bluetooth items.
