# K3 security review: where an attacker starts and what to fix first

## Bottom line

Do not put this in front of the insurer as it stands. Two problems would fail the review on their own, and each is trivial to demonstrate:

1. The Bluetooth PIN can be read off the radio. The controller advertises "K3-<serial>", and the PIN is the last six digits of that serial. Anyone in range has the PIN before they connect.
2. The cloud credential is public. The shared API key is built into firmware, and you publish firmware images on your website. Anyone can download an image, extract the key, and then needs only a serial number to speak as any of your 5,200 controllers.

The worst outcome is not data theft. It is a silent frost-protection failure on the one night it matters. Most of the attack paths below end there, so I've ranked them by that outcome.

## Where an attacker starts (most likely first)

### 1. Drive-by Bluetooth: turn frost protection off (critical, trivial)

- **How.** Scan for "K3-*" advertisements. Read the serial from the name, take the last six digits as the PIN, enter setup mode, and disable frost protection or raise the threshold so it never triggers. A directional antenna extends range well past the vineyard fence. The attacker needs no account and no prior knowledge, and the tools are off-the-shelf.
- **Why it's nasty.** It can be done in autumn and nobody notices until the first frost. Your texts only fire when frost protection *starts* or the unit goes offline for 30 minutes. A controller that was quietly disabled stays online and sends neither. The grower's first sign is dead buds.
- **Other things the same access does.** Run valves (flood a block, drain a reservoir, waste water), or change thresholds so sprinklers fire in the wrong conditions.
- **Fix before review:**
  - Replace the derived PIN with a random per-device pairing secret that is not computable from the serial. Use LE Secure Connections or an equivalent authenticated, encrypted pairing.
  - Gate setup mode behind a physical action (a button or a magnet on the enclosure) and time-limit it. Rate-limit PIN attempts and lock out after a few failures.
  - Stop advertising the full serial. Use a short random ID, and let the Field app resolve it from the dealer's assigned list.
  - Alert the grower on any configuration change, and especially on "frost protection disabled".
  - Add a "frost protection armed" heartbeat to the dashboard, with a distinct alert when it isn't.
- **Fleet note.** Units in the field need these changes by OTA. Until then, consider disabling remote-reachable setup mode by default and requiring the physical gate.

### 2. Impersonate controllers to the cloud (critical, trivial)

- **How.** Download any firmware image, pull the key out, and enumerate serials. Serials that are sequential or guessable make this a loop. Then:
  - Post fake "all is well" telemetry for a controller whose real unit is dead, offline or tampered with. This hides the 30-minute offline alert, so it defeats the one monitor you have.
  - Flood the backend with traffic from thousands of fake units.
  - Read whatever the cloud returns to a controller: its configuration, its owner's details, and any queued commands.
  - If the cloud can push commands or settings to a unit, an attacker who can speak as the unit may be able to influence what the cloud believes. I'd check that the reverse direction can't be abused.
- **Fix:**
  - Give each unit its own credential: a client certificate or key provisioned at manufacture, ideally in a secure element, with mutual TLS. Remove the shared key from firmware.
  - Rotating the shared key is not enough, because the next firmware image would leak the new one.
  - Fleet migration is the hard part, and the insurer will ask about it. Enroll each unit once, authorized by something other than the shared key (for example, tied to the claim record and owner approval), then cut off the shared key on a published date. Flag the units that never migrated.
  - Make serials non-sequential or unguessable for lookup purposes, and rate-limit auth failures per source.

### 3. Hijack ownership through the claim flow (high)

- **How.** The claim needs only serial numbers. An attacker with a list (from Bluetooth sweeps, from a dealer's photo of the labels, or just a guess within the serial range) enters them in the dashboard. The only barrier is an email to the previous owner, who has seven days to object. People miss emails, use dead addresses, or have had the account phished. After day seven the attacker owns the controllers, and probably the alert phone numbers too, so the grower stops getting texts altogether.
- **Fix:**
  - Require proof of possession: a code printed inside the enclosure or shown on the unit, an installer-issued transfer code, or an invoice reference checked by your support team.
  - Notify the current owner by every channel on file (email, SMS and a dashboard banner), and make the default fail-safe: an unconfirmed claim does not go through silently.
  - Keep the existing owner's alert recipients active during the pending period, and send a "claim approved" notice afterwards with a way to dispute it.
  - Rate-limit claims per account and flag one account claiming many unrelated serials.

### 4. Poison the nightly update (high impact, harder to execute)

The signature check is the right idea. What matters is everything around it.

- **Signing key custody and build pipeline.** If someone compromises your CI or your signing key, they can ship a signed release to the whole fleet at 02:00 and it installs on every unit, reboots it, and runs. That is one event taking out frost protection across 5,200 sites. Hold the key in an HSM or offline, require two-person release approval, and make the build reproducible and logged.
- **Downgrade.** You publish old images on the website. If controllers accept any validly signed image, an attacker who can intercept or redirect the update check can serve an old signed release with a known bug. Add a monotonic version counter or rollback protection enforced on the device.
- **Fail-open handling.** Confirm the device rejects a missing or malformed signature rather than skipping the check. Also confirm the USB update path performs the same verification. Dealer USB is often the weaker door.
- **Transport.** Use TLS with certificate validation or pinning for the update check, so a rogue cell-network or DNS trick can't redirect it.

### 5. A bad or interrupted update on a frost night (edge case, but a safety risk)

Even a legitimate release is a risk with this schedule.

- 02:00 is close to the coldest, most frost-prone hour. Every unit checks, downloads, installs and reboots at about the same moment. A buggy release, a failed flash, or a cellular drop mid-download turns into a fleet-wide outage in exactly the window you protect.
- **Fix:**
  - Use A/B partitions with a boot watchdog that automatically rolls back.
  - Roll out in stages (1%, then 10%, then everyone) with a halt switch.
  - During frost season, block updates whenever the temperature is near the threshold or sprinklers are running, and install at a safe time of day.
  - Define what state the valves and sprinklers take on boot. They should not stay stuck open or stay off after a restart.
  - Randomize the check time so the fleet doesn't hit your server in one spike.

### 6. Local and physical (medium)

- **Sensor tampering and failure.** A single temperature reading drives a safety action. Someone with a can of cold spray or a heat source can trigger sprinklers in the wrong conditions or suppress them. A failed sensor (open circuit, stuck reading) could run the water indefinitely or never start. Add plausibility checks, a maximum run time, a fallback behaviour on sensor fault, and an alert for it.
- **SMS alerting.** Alerts depend on one phone number and one carrier path. SIM swaps, jamming, or simply a controller without signal all lose the warning. The 30-minute offline rule is a reasonable start, but consider a second channel and a push notification in the app.
- **Dealer and SIM material.** Check that the SIMs can't be removed and used elsewhere (private APN or IP allow-listing), and that dealer accounts and the Field app have per-person credentials, not shared ones.

## What to fix before the review, in order

1. **Bluetooth pairing and setup mode:** random per-device secret, physical gate, no serial in the advertisement, lockout. This is the cheapest high-value fix and the most visible failure.
2. **Per-device cloud credentials:** remove the shared key, with a migration plan and a cut-off date you can state to the reviewer.
3. **Alerts on tampering:** config changes, frost protection disabled, and an armed-state heartbeat. This is quick to build and closes the silent-failure gap for the units you can't patch yet.
4. **Claim flow:** proof of possession, no silent approval, multi-channel notice.
5. **Update safety:** key custody, anti-rollback, USB path verification, A/B with automatic rollback, staged rollout, and no updates during frost-risk windows.

Items 1 to 3 are what I would want finished and demonstrable. For the rest, a written plan with dates is usually acceptable to a reviewer, provided the critical gaps are closed.

## Residual risk

Even after these fixes, someone with physical access to a unit can still tamper with the sensor or valves, and a very determined attacker can still jam cellular or Bluetooth. Frost protection will remain a safety-critical system on a fleet that is hard to patch, so migration completeness will matter more than any single control.

What I took from your brief: the controllers act autonomously on their own sensor and don't need the cloud to start sprinklers, the dashboard can configure but I don't know what it can command, and the update server is a plain HTTPS service you control. I assumed that setup mode over Bluetooth is available at any time, not only after a physical action, that serials are sequential or close to it, and that old firmware images stay on the site. I also assumed that the USB update path uses the same signature check, which is the first thing to verify. If any of those is wrong, the ranking above changes, so check them before anything else, starting with whether the setup mode really is reachable without touching the unit.
