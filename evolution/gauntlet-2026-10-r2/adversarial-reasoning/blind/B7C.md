I'd start the attack at the shared API key. After that, the order is the Bluetooth PIN, the ownership claim, then the update path. Your design has a physical safety consequence (frost protection), so a reviewer will weigh anything that can silently disable or falsely trigger it most heavily. I only have your description, so where I assume something, I say so.

## Where an attacker starts

**1. The shared, firmware-embedded API key (fleet-wide compromise, most likely first move)**
- Your firmware images are public, so the key is public. Anyone can download an image and extract the key with strings or a firmware unpack. No hardware attack is needed.
- Authentication is "serial plus key". Serials are probably sequential or guessable, and the last six digits are also the BLE PIN. So an attacker with the key can enumerate serials and impersonate any controller, or act as any controller toward the cloud.
- Impact depends on what the key authorizes. Likely outcomes are:
  - reading telemetry and location for the whole fleet
  - sending fake "I'm fine, temp 15°C" readings
  - suppressing or forging offline and frost alerts
  - pulling per-device config
  - possibly pushing commands if the channel is bidirectional
- The key cannot be rotated without a firmware release, and it is in every image already published. Treat it as burned.

**2. The Bluetooth PIN (per-site compromise, easy to scale)**
- The PIN is the last six digits of a serial the device broadcasts. "K3-" plus the serial is advertised in the clear, so the attacker doesn't need to guess anything. They read the PIN off the advertisement. It is effectively no authentication.
- Setup mode lets them change thresholds, run valves and turn frost protection off. An attacker within Bluetooth range (tens of metres, much more with a directional antenna) can disable frost protection on a vineyard the night before a frost. It may also be possible to flood a block or run pumps.
- Nobody sees this attack happen. The device may not alert, and the cloud may not know. The grower finds out when the crop is lost.
- It also needs no skill. A phone app, or a scripted scan of the row, is enough.
- Questions to check: Is setup mode always available, or only after a button press or power cycle? Is there any rate limit, lockout or pairing bond? Does a settings change get logged and reported to the cloud?

**3. The ownership claim (account takeover without touching the device)**
- A claim needs only serial numbers, which are guessable or enumerable and printed on the label.
- The only defense is an email to the previous owner with a seven-day objection window. Several attacks follow:
  - If the previous owner's email is stale, unmonitored or a shared mailbox, the claim succeeds quietly.
  - The objection email may be missed, filtered or lost in the spring season, especially during busy periods.
  - An attacker can claim a competitor's or victim's controllers directly. Once the claim goes through, they own the dashboard view: they can change thresholds, turn off frost protection through the cloud, and read the SMS alert contacts. The real owner loses control.
  - The old owner might lose alert texts. The attacker might also redirect them.
- This is a non-technical attack that scales. It needs no physical presence and no key.
- Missing safeguards: proof of possession (for example a code printed inside the enclosure or a physical button press on the device), identity verification of the new owner, a dealer or sales-order link, and notification through more than one channel (SMS to the existing owner too).

**4. The nightly update path (highest consequence, harder to reach)**
- Signature verification against your public key is the right control. Questions a reviewer will ask:
  - Where is the signing key stored? Is it in an HSM, or on a build server or laptop? Who can use it? Is signing done in CI with approvals?
  - Is there rollback or downgrade protection? If not, an attacker who can serve an older, signed, vulnerable image (for example one with a known bug) can downgrade devices. Check a monotonic version or counter.
  - How is the update server reached, and does the device validate TLS? With the shared API key as the only authentication, can an attacker redirect or man-in-the-middle the channel? A signature protects integrity, but not freshness or downgrade.
  - What happens on a failed or partial install? Is there an A/B slot with automatic rollback? An update at 02:00 in spring, exactly when frost is most likely, followed by a reboot, is a real risk. A bad release or an interrupted update could leave the sprinklers off during the coldest hours of the night.
  - A fleet-wide simultaneous update at 02:00 is a single point of failure. A bug in one release hits 5,200 sites at the same moment.
- The USB firmware path: public images are good for transparency, but confirm that USB updates go through the same signature check and downgrade rule.

## Further issues a reviewer is likely to raise

- **Alert integrity.** The "offline for more than 30 minutes" text is the only safety net when the controller is down. If an attacker can spoof heartbeats using the shared key, they can hide an offline controller. Conversely, a flood of fake alerts can cause alert fatigue.
- **Spoofed or tampered temperature.** The frost trigger depends on one sensor reading below 1°C. A failed or disconnected sensor, a sensor reading too high, or a single point of failure all cause missed frost nights. Consider redundancy, sanity checks and a fail-safe (for example, treat an implausible or missing reading as a reason to alert).
- **Cloud-side dashboard.** Check password policy, MFA, session handling and per-controller authorization, especially after claim transfer.
- **Cellular and privacy.** Location data per controller, and where fleet data is stored.
- **Physical access.** Labels inside the lid mean anyone who can open the enclosure reads the PIN. That is acceptable only if the PIN is not also derivable from the broadcast name.
- **Logging and detection.** Do you log settings changes, claims, and updates? You can't tell the reviewer you'd detect an attack if you can't see one.

## What to fix before the review (priority order)

1. **Replace the shared API key with per-device credentials.**
   - Give each unit a unique secret or certificate (mutual TLS, provisioned at manufacture, ideally in a secure element), tied to its serial.
   - Add server-side revocation.
   - Ship a transition release: new devices use per-device credentials, old ones migrate over the signed update channel, and the old key is then disabled. Until then, restrict what the shared key can do (read-only, rate-limited) and monitor for abuse.
2. **Fix the Bluetooth setup authentication.**
   - Use a random per-device PIN or passkey, not derived from the serial and not broadcast.
   - Require physical presence to enter setup mode (a button press with a time window or a magnet switch), with a timeout.
   - Add attempt limits, lockout and bonding.
   - Stop advertising the serial, using a rotating identifier or a short ID instead. Dealers can still identify units through a button-triggered mode or an LED.
   - Make "frost protection off" require a stronger confirmation, and report every setup change to the cloud and notify the grower by SMS.
3. **Rework the ownership transfer.**
   - Require proof of possession (an on-label claim code that is not the serial, or a button press on the device) plus verified identity, and ideally a dealer-confirmed transfer.
   - Notify the current owner through every channel (email and SMS) and make the objection simple.
   - Don't let a claim silently take over alerting. Freeze remote safety-critical changes (turning frost protection off) during the pending period.
   - Add an audit trail.
4. **Harden the update pipeline.**
   - Document signing-key custody (HSM or equivalent, access control, offline root, key rotation).
   - Add anti-rollback counters, A/B slots with automatic rollback, and a health check after boot.
   - Stagger rollouts (canary, then waves) and avoid updating during frost-risk windows, or at least confirm frost protection is active after reboot.
   - Make sure the device pins the server certificate and validates TLS.
5. **Fail-safe behavior for frost protection.** Define what the unit does when the sensor fails, the cloud is unreachable, or config is tampered with. A sensible default is to keep protecting and to alert. Add independent bounds on thresholds so that "off" cannot be set casually.
6. **Monitoring and incident response.** Fleet anomaly detection (the same key used from many IPs, mass enumeration, many claims), a security contact, and a disclosure process. Reviewers like to see that you can revoke and respond.

## Suggested framing for the insurer

Be upfront. Tell them what you found, what you are fixing, and the dates. A credible remediation plan, with the per-device identity and Bluetooth/claim changes done first, will do more than an assurance that everything is secure. If an item can't ship before the review (the key migration across 5,200 field units, for example), present the interim mitigations and a firm schedule.

## Assumptions

I assumed the API key authorizes more than read-only telemetry, that serials are guessable, and that Bluetooth setup mode is always available rather than gated by a button. If any of these is wrong, the ranking above shifts, but the shared key and PIN-from-serial problems stand on their own. If you tell me what the key can do and whether setup mode needs a physical action, I can refine the ordering.
