# Attacking the K3 design: where an attacker starts and what to fix first

## Bottom line

I would not put this in front of the insurer's reviewers as it stands. Three weaknesses can be exploited with no special skill, and each one can switch off frost protection on a target night. Two more could hit the whole fleet at once. Most of the fixes are small. The firmware and cloud-identity fixes take longer.

## Where an attacker starts

Cheapest first. All of these use information you publish or broadcast.

**1. Download your firmware and extract the shared API key (fleet-wide, no hardware needed).**
The key is identical on every unit and built into images that sit on your website. Extracting it is an afternoon's work with `strings` or a disassembler. The attacker then has what every controller has, plus a serial number, and serials are short and probably sequential. With that they can:
- Impersonate any controller to your cloud. They can send fake "all fine, 4°C" telemetry, or report a controller offline.
- Pull a unit's configuration, and send commands if your cloud can push them.
- Flood the API with 5,200 identities' worth of traffic and degrade the service for everyone.

Rotating the key doesn't help, because the next release carries the new shared key in the same public file. Every unit needs its own credential.

**2. Walk up to a vineyard and turn frost protection off (local, one site at a time).**
The Bluetooth name is "K3-" plus the serial, and the setup PIN is the last six digits of that serial. The PIN is therefore broadcast to anyone in radio range, so it is not a secret at all. Anyone with a phone and a Bluetooth scanner can:
- Read the PIN from the advertised name.
- Enter setup mode, lower the threshold below any realistic temperature or disable frost protection, and leave.
- Run valves on demand, for example to flood a block or drain a water supply.

Nothing you described stops this: no lockout, no logging, no alert to the grower. Setting it up before a cold night and watching the result from the road is practical. Walking a row of controllers with a script would take a few minutes. The same attacker can sit at the edge of a property and do it to every unit in range.

**3. Take over the account, not the device (silent, scalable, and it gets the dashboard and the texts).**
Ownership transfers on the strength of serial numbers, which the attacker already has from point 2 (or from guessing). The only protection is one email to the previous owner and a seven-day silence window. In practice:
- Growers ignore or miss emails, use an old address, or are away during the off-season. Silence counts as consent.
- Once the claim lands, the attacker owns the dashboard. The frost and offline texts go to them, not the grower. The grower loses visibility on the controller, and nobody gets warned of the failure.
- The attacker can then change settings remotely, or simply watch where and when each site is vulnerable.

A claim timed for early spring means the real owner finds out when the crop is gone. Also check what a new owner can see: the previous owner's history would be a data leak.

**4. Fleet-wide failure through the nightly update (hits everyone at once, with or without an attacker).**
Signature verification is the right design, but several things around it can go wrong:
- **Rollback.** Old signed images are public. If the controller doesn't refuse older versions, an attacker who can redirect a unit (rogue cell tower, DNS or TLS problem, a hostile network at a dealer) can serve an old, legitimately signed release that has a known hole. Check that the version only ever goes up and that it is covered by the signature.
- **Signing key.** Everything rests on one private key. If it is on a build server or a laptop, compromising it is a fleet takeover, and the signed update is the delivery vehicle. It should live in an HSM or equivalent, with signing as a separate, reviewed step.
- **No staging.** All 5,200 units check at 02:00 and reboot. A bad release, signed and legitimate, takes out the whole fleet at the coldest part of a frost night, with sprinklers dead during the reboot or after a boot loop. This is the one most likely to happen by accident.
- **Frost-night interaction.** Check whether an update can install while the temperature is near the trigger, or while sprinklers are running. It shouldn't.

**5. Make a controller blind, or make it wrong.**
- **Sensor.** A single temperature sensor is the trigger for everything. A failed, disconnected or shielded sensor reads high or reports nothing. Decide what the controller does with an implausible or missing reading. The safe choice for a frost device is to run protection, within limits, and alert.
- **Cell jamming.** A cheap jammer makes the controller "offline". You alert at 30 minutes, but the controller keeps running locally, which is good. Be clear in the review that frost protection must work with no network at all, and test it.
- **False activations.** Spoofed readings or a lowered threshold can run sprinklers on warm nights. That means flooded blocks, wasted water and sometimes disease or regulatory trouble. It is less dramatic than missed frost but easy to cause.

**6. Social engineering and the people around it.** Dealers hold the PIN labels and set up many sites. An attacker who calls support pretending to be a new owner, or who phishes a dealer, gets the same result as point 3. Support staff need a verification process for ownership changes that does not rely on facts from the label or the BLE name.

## What to fix before the review, in order

1. **Per-device credentials.** Give each controller its own key or certificate, provisioned at manufacture, kept in secure storage if the hardware has any, and revocable per serial. Remove the shared key from firmware. This breaks attack 1 completely. If new hardware is out of reach, at minimum bind a per-device secret generated at factory and held in the cloud, and rate-limit and monitor per serial.
2. **Stop broadcasting the PIN.** Generate a random PIN per unit at manufacture (not derived from the serial) and print it on the label. Add attempt lockout with growing delays. Better still, require pairing with a physical action, such as a button press on the enclosure within a short window, before setup mode will accept changes. Don't advertise the serial: use a random or rotating identifier, and let the dealer confirm the unit with a blink or LED.
3. **Make transfer require proof of possession.** Require something only the holder of the physical unit has, for example a claim code printed inside the lid (random, separate from the PIN), or confirmation from the controller itself. Keep the notice to the old owner, but send it by SMS as well as email, make it shout, and keep the old owner able to veto during the window. Do not give the new owner the old owner's history.
4. **Alert on changes, not just on frost.** Text the grower on any change to frost protection, threshold or valve commands made by Bluetooth or the dashboard, and whenever a transfer is requested. That turns attacks 2 and 3 from silent into noticed, and it gives you an audit trail.
5. **Harden the update path.** Add monotonic version checks (anti-rollback). Move the signing key to an HSM. Roll out in stages, for example 1%, then 10%, then the rest, over days, with automatic halt on failures. Randomize check times within a window and don't install when the temperature is near the trigger or sprinklers are active. Keep a known-good fallback image so a bad release recovers without a truck roll. Confirm USB updates are verified exactly like network ones.
6. **Fail-safe sensor behaviour.** Define and test what happens on a missing, stuck or out-of-range reading, and consider a second sensor or a plausibility check against the cloud's weather data.
7. **Cloud-side basics the reviewers will ask for.** Per-serial rate limits, alerting for one credential appearing from two places, an audit log of every configuration change with who or what made it, and a way to revoke a single controller.

## Edge cases that are not attacks but will bite

- A unit that never gets its 02:00 check because of coverage gaps could fall many versions behind, so the staged rollout and rollback policy need to handle big version jumps.
- Clock drift or a missing clock could break any time-based rule (the 02:00 check, the seven-day claim window, signature validity).
- Two people in setup mode at once, or a Bluetooth session dropping halfway through a threshold change, could leave a half-applied configuration. Make changes atomic and confirm them back to the user.
- A reboot loop after a power brown-out on a cold night. Confirm the sprinkler logic restarts into the right state, not "off".
- A grower who changes email or phone leaves alerts going nowhere. Verify contact details periodically.
- Devices resold or moved between farms without a transfer, which leaves two parties believing they own one unit.

## Residual risk

Even after these fixes, someone physically at the site can still pull the power, cut the sensor cable or break the valves. The enclosure and the cabling are the limit of what software can do, so be upfront about that with the reviewer. A compromised signing key or insider at Kellsby would still be a fleet-wide event, which is why staging and the fallback image matter.

What I took from your brief: the shared key and the firmware images are public in the way you describe, the PIN really is a suffix of the advertised serial, there is no attempt lockout or logging on setup mode, and the controller keeps running frost logic locally when the network is down. I assumed serials are sequential or otherwise guessable, that the cloud can push settings to a controller, that USB updates use the same signature check, and that the hardware has no secure element. Check first: whether a controller can really be switched into setup mode with no physical action, whether an unsigned or older image is refused on both the network and USB paths, and what the controller does if its sensor reads nothing.
