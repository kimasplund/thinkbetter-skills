# Smart lock rollout: security review for Corrabay Storage

## Bottom line

Fix the gate keypad and the revocation design before November. Do not roll out as specified.

- **The gate PIN breaks first.** It is guessable within about a day at your largest site.
- **Revocation is the biggest structural problem.** Removed helpers, former tenants and overlocked tenants keep working credentials until their lock happens to sync, and the design gives them no reason to help it sync.
- **The access history your insurer will rely on can be erased by the people it is meant to catch.** The same applies to the 60-day photo record.

The details are below, in the order I would fix them.

## Gate PIN: guessable in roughly a day

At your largest site, 1,100 of the 1,000,000 possible 6-digit PINs are valid. Any random guess has about a 0.11% chance of being someone's PIN.

The lockout allows 5 tries every 5 minutes, which is 1 guess a minute or about 1,440 a day. That gives roughly 1.6 expected hits per day. The expected time to the first working PIN is around 15 hours. Someone with a folding chair and a phone timer, or a cheap keypad-bypass device, gets in within a day or two. A script on a wired keypad does it faster.

Other problems with the gate:

- **The lockout is a denial-of-service switch.** Five wrong entries every 5 minutes keeps the gate unusable for every tenant, and all it takes is someone standing there. Check whether there is a fallback, such as the app, a fob or a staff override. If not, a gate-down night becomes a flood of manager call-outs.
- **Wrong attribution.** A successful guess logs as an innocent tenant entering. That is a bad basis for a theft dispute.
- **PINs get shared and watched.** They are 6 digits typed in the open, so shoulder-surfing and sharing with friends are easy. It is also unclear whether PINs are revoked at overlock or move-out. If they are not, delinquent tenants and ex-tenants keep site access.

**Changes:**
- Use longer PINs (8 digits or more), or better, make the gate open from the app with a per-tenant credential and keep the PIN as a fallback only.
- Escalate lockouts (5 min, then 30 min, then 24 hours) instead of repeating a flat 5 minutes.
- Alert the manager on repeated failures.
- Put a camera on the keypad.
- Revoke the PIN automatically at overlock and move-out.

## Revocation depends on a sync that nobody is obliged to do

The locks have no connection of their own. A change reaches a lock only when some Corrabay app with phone signal connects to it. The attacker is often the one holding the app.

- **Overlock does not work reliably.** A tenant 30 days late whose phone never syncs, or who is in a basement with no signal, keeps opening the unit indefinitely. A tenant who understands this can stay in airplane mode. You then bear the cost of an unpaid unit while the tenant keeps using it, and the lien process you start at 60 days rests on a lock state you cannot prove.
- **Removed helpers and former tenants keep access.** The most damaging case is a previous tenant, or a helper the tenant fell out with, going back to a unit that now belongs to someone else. The old credential stays valid on the lock until the new tenant's phone, or a lucky staff phone, pushes the change. The new tenant's goods are at risk from day one of the new rental.
- **You will not know how bad it is.** The server has no view of which locks are stale unless you build one.
- **The 50-credential cache** is a quiet limit. Check what happens when a unit has accumulated more than 50 current and historical credentials, and whether removed entries free space.

**Changes:**
- **Make credentials expire on the lock itself.** Each credential carries a validity window of, say, 24 to 72 hours, and every successful online refresh extends it. A lock that has not heard from the server stops honoring the credential by itself. This bounds the revocation delay to the length of the window instead of leaving it unbounded. Basement tenants can refresh whenever they next have signal, so size the window to how often they actually do.
- **Push revocations first.** Order the sync queue so revocations and overlocks go before everything else, and have the app carry them to any lock it meets.
- **Use staff phones as sync couriers.** Managers or a rotating staff member walk each site on a schedule and sync every lock they pass. This also catches stale locks.
- **Alert on stale locks.** Report any lock not synced in X days, and treat any overlocked or moved-out unit not confirmed synced within a day as an open ticket.
- **Consider a small Bluetooth hub** in each basement bank if the staleness report shows real dead zones.
- **For overlock, keep a physical fallback.** A manual overlock disc over the lock, or a lock mode that the staff app can set directly on site, covers the case where sync does not arrive.

## The access history can be starved or forged

The app records each unlock and uploads it at the next sync. The history is therefore produced and delivered by the person being logged.

- A tenant who wants an entry to vanish can force-quit the app, uninstall it before it uploads, or stay offline. The unlock still happened. Nothing records it.
- The ex-tenant or removed helper in section 2 has no incentive to sync, so exactly the unlocks you need for a dispute are missing.
- Your insurer is relying on "a full access history". What you actually have is a history of entries by cooperative users.
- Phone clocks can be wrong, and an app log is easy to edit if someone is determined.

**Changes:**
- **Have the lock record every event** (unlock, failed attempt, credential used, time) in its own memory, signed with a key held in the lock. The app is only a courier for that log. The log fills in whenever any app syncs the lock, including staff phones on rounds.
- **Record failed attempts and unknown devices as well** as successes.
- **Keep a lock-side clock** and record drift when it syncs.
- **Say plainly in the review** that the history is complete only up to the last sync of each lock, and report the staleness figure.

## Maintenance codes: strong access, weak controls

A 24-hour code for any unit, sent to a manager's own phone, is effectively a master key.

- It works offline, so you cannot revoke it. A lost or compromised phone is a 24-hour hole in any unit that code covers.
- It can be forwarded, screenshotted or kept after the job, and it is not tied to a person or a reason.
- Managers could use it to enter a unit without any record the tenant can see, and whether the lock logs it depends on section 3.
- Anyone who gets into the admin panel (a phished manager password, for example) can mint codes for any unit at any site.

**Changes:**
- Make codes single-use or valid for a couple of hours, and tied to a named manager and a ticket.
- Scope codes to one unit at one site.
- Have the lock log every use with the issuer's identity.
- Notify the tenant, or at least record that a code was issued for their unit.
- Require MFA on the admin panel, and alert on unusual volume of codes.

## The 60-day photos: one person alone with the contents

At 60 days the site manager opens the unit and photographs the contents. Those photos are the auction listing and your record of what was inside.

- **One person with sole access** can remove items before taking the photos. The tenant later says things were taken, and your only record was made by the person they accuse.
- **Photos on a personal phone** are easy to delete, edit or lose, and they usually leave the company's control.
- **Contents are personal data.** Photos of paperwork, IDs, medication or family items end up in a public auction listing or on staff phones.
- **Lien rules vary by state.** The notices and timing required before entry and sale, and what you must inventory, need confirming with counsel. This sits outside the lock design but is the part an insurer is most likely to ask about.

**Changes:**
- Require two people (or one person plus a live video call with another manager) at the opening.
- Take photos or video through the company app so they upload at once to your server with a timestamp, rather than staying on a phone.
- Log the opening through the lock log and a ticket.
- Apply a sensible retention period, and redact personal documents before listings go public.

## Helpers by phone number

- Phone numbers get reassigned, and SIM-swap attacks are common. If a helper's number changes hands, the new owner could claim helper access.
- Helpers have "the same unlock rights" as the tenant. It is unclear whether that includes adding other helpers, which would let one helper's credential spread without the tenant knowing.
- A tenant can add helpers without limit, which interacts with the 50-credential cache and your ability to attribute unlocks.

**Changes:**
- Confirm the helper's number by a one-time code when they accept.
- Give helpers an expiry date by default, with renewal.
- Do not let helpers add further helpers.
- Tell the tenant when a helper unlocks for the first time.

## Other points to cover in the review

- **Phone theft.** Does the app require a passcode or biometric before it will unlock? A stolen unlocked phone with the app open should not be enough.
- **Bluetooth relay.** Check with the lock vendor whether a relay attack, where a tenant's nearby phone is relayed to the lock, is mitigated, for example by requiring a challenge response and a short range limit.
- **Vendor and update risk.** Ask who signs the lock firmware, how updates reach locks given they are offline, and what happens to your locks if the vendor's service goes down or is breached.
- **Day-one cutover.** Replacing padlocks site by site in November means a window where some units are on old and some on new access. Make sure old keys and codes are retired as each site moves over.
- **Server outage.** Confirm that locks keep working for current tenants and staff if your server is down, and that you can still grant emergency access.

## Order of work before the insurer deadline

1. Gate: longer or app-based credentials, escalating lockout, alerts, camera. Quick to do, and it is the most visible hole.
2. Credential expiry on the locks, revocations first in the sync queue, a stale-lock report, and a physical fallback for overlocks.
3. Lock-recorded signed logs, with the app as courier only.
4. Maintenance code limits and MFA on the admin panel.
5. Two-person opening and company-controlled photo capture for the 60-day step.
6. Helper verification, expiry and limits.

For the insurer, I would state the revocation window and the log completeness explicitly as numbers (for example "revocations take effect within 48 hours at worst, and each lock's log is complete up to its last sync, reported daily"). A review that gives honest bounds is more credible than one that claims real-time control the architecture cannot provide.

I made a few assumptions you should check: that the gate PIN lockout applies to the keypad as a whole rather than per user, that gate PINs are not currently revoked at overlock, and that the lock vendor's firmware supports on-lock credential expiry and its own event log. If the vendor cannot support the last of these, that is the question to put to them first.
