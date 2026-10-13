Assumptions: the API key is one shared secret across all ~5,200 units; the signing private key lives somewhere in your build/release infrastructure; the update server and cloud API are reachable over TLS, but I can't confirm certificate validation on the device.

## Where an attacker starts (ranked by ease times impact)

**1. The shared API key (cheapest, widest blast radius).**
Anyone who buys one controller, or downloads one of your public firmware images, can extract the key. Serial numbers are short, sequential or guessable, and are broadcast over Bluetooth. So "serial + global key" means an attacker can impersonate any controller to your cloud.
- Impact: forge temperature and online status, suppress or fabricate the "offline" and "frost started" texts, and probe whatever the cloud sends back (config, commands, other units' data, depending on your API's authorization).
- A fleet-wide key can't be revoked without a firmware push to 5,200 units, so any leak is permanent until then.

**2. Bluetooth setup: the PIN is not a secret.**
The PIN is the last six digits of a serial that the device advertises in its own name ("K3-<serial>"). Anyone in radio range reads the PIN directly from the advertisement, with no brute force at all. In setup mode an attacker can turn frost protection off, change thresholds, or run valves.
- Impact: this is the frost-night attack. Disable protection on a target vineyard in the afternoon and the crop is lost that night, with no cloud access needed. Running valves can also flood or drain a system. Range is tens of metres, extendable with a directional antenna, and a single drive-along covers many farms.
- Also check: whether setup mode is always available or needs a physical action, whether there is rate limiting or lockout, whether pairing uses encrypted and authenticated BLE (LE Secure Connections), and whether a dealer's phone or app retains access afterward.
- Printed labels inside the lid are fine as a factory secret only if the value is random and independent of the serial.

**3. Update pipeline.**
Signature verification is the right control, but check the rest:
- Is there rollback or downgrade protection (version monotonic counter)? Without it, an attacker with a validly signed old image, which you publish on your website, can reinstall a vulnerable version.
- Is the image encrypted or just signed? Public images hand attackers the firmware for offline analysis (which is how they get the key in #1).
- Where is the signing key stored (HSM or CI secret)? Compromise there means a fleet-wide, signed, automatic 02:00 push. All units update at the same time, so a bad release, malicious or just buggy, takes out the whole fleet before anyone wakes up, in frost season.
- Is the update server's TLS certificate validated and pinned? Is the USB path held to the same signature check? Is the 02:00 reboot safe, given that 02:00 to dawn is exactly when frost sprinklers must run? Does a failed update roll back to the previous image automatically?
- Is the signature check covering the full image and metadata, and is it done before writing to the boot partition?

**4. Ownership claim process.**
Claiming only needs serial numbers, which are guessable and advertised over Bluetooth. The only defense is a seven-day email to the previous owner.
- An attacker claims a target's controllers and waits. If the old owner's email is dead, ignored, goes to spam, or belongs to a dealer or ex-employee, the claim completes silently.
- After that the attacker owns the dashboard view, can change settings, and receives the alerts, while the grower is locked out and, worse, no longer gets frost texts.
- Also a griefing path: anyone can spam objection-requiring claims against any farm.
- Fix: require proof of possession (the lid-label code, physical button press, or a dealer or sales-order attestation), notify through multiple channels (SMS, dashboard banner, email to all account users), make the claim not take effect on live frost-protection settings until confirmed, and require an affirmative approval by the old owner for units that are recently active.

**5. Dashboard and alerting.**
- Alerting depends on the cloud and cellular. An attacker who jams cellular or spoofs status (#1) could keep "offline" alerts from firing, or flood them.
- Check account security: MFA, password reset, session handling, and per-tenant authorization (IDOR on serial numbers is likely given everything is keyed on serial).
- Frost alerts should come from independent paths, not only the unit reporting its own status.

**6. Safety design (the insurer will care most about this).**
The controller acts on a single sensor reading below 1°C. A shorted, failed, or tampered sensor produces false triggers (water waste, ice load, flooding) or, if it reads high, a missed frost night. Consider sensor plausibility checks, a second sensor, and a failsafe default. Disabling frost protection should require stronger authorization than other settings and should generate an alert to the grower.

## What to fix before the review (priority order)

1. **Per-device credentials.** Provision a unique key or client certificate per unit at manufacture (ideally in a secure element), use mutual TLS, and enable server-side revocation. Remove the global key from firmware. For the fielded fleet, ship a signed firmware that enrolls each unit with a fresh credential, then disable the global key on a schedule.
2. **Bluetooth.** Stop broadcasting the serial (use a random or rotating identifier). Replace the derived PIN with a random per-device secret not derivable from the serial. Require a physical action (button held on the unit) to enter setup mode, time-limit it, add attempt lockout, and use authenticated, encrypted BLE pairing. Log setup-mode changes to the cloud and alert the grower when frost protection is disabled or thresholds change. This is the most dangerous issue to leave open.
3. **Claim process.** Add proof of possession and multi-channel notification, as above. Don't let a claim cut off an existing owner's alerts without affirmative confirmation.
4. **Update pipeline.** Add anti-rollback, staged rollout (canary, then 1%, 10%, 100%), automatic rollback on failed boot, signing key in an HSM with restricted access, and a kill-switch or hold flag. Avoid 02:00 reboots during frost season, or make them conditional on temperature (no update if forecast or current temp is near freezing).
5. **Fail-safe local behavior.** Frost protection should keep running autonomously if the cloud, cellular, or an update fails. Confirm that nothing remote can switch it off without local authentication.
6. **Evidence for the reviewer.** Prepare a threat model, a key-management description, an incident-response and revocation plan, and a penetration-test report. An independent test of the BLE and cloud interfaces before the review is worth it.

## Suggested sequence
Do the BLE and per-device-identity work first, since those are exploitable today by anyone with a phone or a downloaded firmware image. Do the claim flow and the update-pipeline hardening next, then document everything. Tell the reviewer honestly what is already fixed, what is in rollout, and what the plan is for the units still in the field.
