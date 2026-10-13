# Security review: Corrabay smart-lock rollout

## Short answer

Revocation is what breaks first, and it breaks in the exact cases the system exists to handle: overlocks, move-outs and removed helpers. The access history your insurer will rely on is the next weakest part. The gate PIN is weaker than it looks. The maintenance codes and the 60-day photo process are insider-risk gaps rather than outside-attack gaps.

Assumptions: the lock enforces expiry with its own clock, the server pushes changes unsigned or signed in a way I can't see, and the gate keypad is separate from the lock system. Correct me if any of these is wrong, because they change the severity of items 1 to 3.

## Revocation only happens if the person being revoked helps (breaks first)

A change reaches a lock only when some Corrabay app connects to that lock while its phone has signal. The people you most want to cut off are the ones least likely to cause that sync.

- **Overlock.** A tenant 30 days late has every reason not to open the app near their unit. Their cached credential stays valid on the lock, and the overlock never lands. In a basement with no signal, no one else may connect for weeks. The overlock exists to stop access, and it may do nothing.
- **Deliberate staleness.** Any tenant or helper can put the phone in airplane mode, never update the app, or keep an old phone. The cached credential keeps working. Nothing on the lock expires it, as far as your description goes.
- **Removed helpers and ex-partners.** A removed helper keeps access until the lock syncs. A tenant removing an ex-partner believes the removal is done when it is not.
- **Unit turnover.** The old tenant's credential stays live on the lock after the new tenant is assigned. The first person to hit this will be a new tenant whose belongings are gone.
- **Fixed cache size.** At 50 credentials, it is unclear what happens when helpers, maintenance codes and turnover fill the cache. Dropping the newest or the oldest entry are both bad outcomes.

What to change:
1. Make every credential expire on the lock, for example 24 to 72 hours, and renew it at sync. A tenant who never syncs gets locked out by the clock, so staying quiet no longer works. Choose the window against how often tenants really visit. Weekly visitors would need a longer window.
2. Put a Bluetooth gateway on each site's corridor or ceiling, powered and online, so locks sync on a schedule without depending on a tenant's phone. This is the real fix. It also gives you lock health and battery alerts.
3. Treat overlock as a hard state. A signed "deny" record pushed through the gateway should override any cached credential immediately. Until gateways are in, fit a physical overlock hasp on delinquent units.
4. Sign every server-to-lock message and add a version counter, so a rogue app cannot replay old state or push a forged one. Today the phone is a trusted courier for data it could alter.
5. Define the cache-full behaviour and test it. A full cache should reject new helpers visibly, not silently evict someone.

## The access history is not evidence yet

The app records each unlock and uploads it later. That makes the record the tenant's phone's claim, not the lock's.

- A tenant who wants to hide a visit can kill the app, go offline or delete it, and the event may never upload.
- Events can be delayed for weeks, which matters in a theft dispute about who was in the unit on a given day.
- Helpers' and maintenance unlocks share the same weakness.
- If the lock's clock drifts while offline, timestamps in a claim may be challenged. A clever tenant's lawyer will make this point.

What to change: the lock should write the event itself, with its own timestamp, a running counter and a signature from a key that never leaves the lock. Any app that syncs just carries the log. A gap in the counter shows a missing event. Store the last few hundred events on the lock. Sync the lock clock at every connection and record the drift. With this, "full access history" becomes defensible, and your insurer can be told so in writing.

## Gate PIN: unique PINs make guessing much easier

One million possible PINs and about 1,100 live ones at your largest site means a random guess hits a valid PIN about 0.11% of the time. The lockout is five tries per five minutes, so about 60 guesses an hour per keypad. That is roughly one success every 15 hours of guessing. A person who comes back for two nights will very likely get in, with no tools at all.

Real PINs are worse than random. Expect many 123456, birthdays and repeated digits. The keypad is also a shoulder-surfing target. Because the lockout is per keypad, not per PIN, an attacker can also hold the gate in lockout and block legitimate tenants every five minutes. That is cheap, annoying and a good way to start a bad review.

What to change: use a longer PIN (8 digits) and require unit number plus PIN, so a guess has to match both. Make the lockout escalate (5 min, then 30, then alert the manager). Reject trivial PINs at issue. Add a camera on the keypad, and an app unlock at the gate as the main path. Get the gate-access log into the same signed-record scheme as the locks.

Note the gate only gets someone onto the site. The impact is theft from vehicles, tailgating and surveillance of units, not direct entry to units, so it ranks below items 1 and 2.

## Maintenance codes are an unchecked insider tool

A 24-hour code for any unit, sent to the manager's own phone, is a skeleton key with a very light trail.

- One manager can generate a code for any unit at any site, with no stated reason and no second person.
- The code sits on a personal phone: screenshots, forwarded messages, a lost or borrowed phone, or a former employee's account.
- A full day of validity is long for a job that takes ten minutes.
- If the code unlocks a unit while the tenant has an active credential, the tenant may never know.

What to change: make each code single-use, valid for the one unit and no more than 2 to 4 hours, with a required reason. Require a second approver for any unit that is occupied by a tenant who is not delinquent. Alert the tenant when it is used. Log it in the signed log. Remove codes from personal phones where you can, and tie generation to the manager's account with strong sign-in. Review monthly who generated how many codes.

## Helpers by phone number

Phone numbers are recycled and can be typed wrong. A helper added with a typo, or a number that later passes to a stranger, gets the same unlock rights as the tenant. SIM-swap or an account takeover on a tenant's number also hands over every unit they hold.

What to change: confirm the helper by a code sent to the number before they gain access. Notify the tenant on each helper action. Give helpers a time limit (say 30 days) that the tenant renews. Stop helpers from adding other helpers. Treat tenant sign-in as the front door and require a one-time code or biometrics on new devices.

## The 60-day photo process

Photographs are both your auction listing and your record of what was in the unit. One manager alone in the unit, with their own phone, is a weak setup for both purposes.

- Nothing proves the manager did not take items before photographing. A former tenant who says "there was a watch in there" has a good claim against you.
- Photos may show IDs, medical papers, children's items, other people's names and addresses. Putting those in a public listing is a privacy problem. Bidders can also use the listing to plan a burglary of the unit.
- Photos on a personal phone are not a tamper-evident record. Timestamps and file edits can be disputed.

What to change: two staff present for every opening, or one staff member and a body camera. Use a company device with timestamps and uploads straight to your server. Blur or remove paper documents and personal items before the listing goes live. Keep the full unredacted set privately for disputes. Make the opening a logged event in the same record as everything else.

## Edge cases to test before November

- Lock battery dies or the lock fails: does it fail shut or open? Who has a physical override, and is use of it recorded?
- A phone with a stale app syncing a lock: does older data ever overwrite newer?
- Two phones syncing the same lock at once.
- A tenant's phone is stolen. How quickly can you revoke it, given the sync delay in item 1?
- Relay attacks: someone near the tenant's phone forwarding Bluetooth signals to a lock far away. Test whether the lock needs proximity or a distance check.
- Moving a unit to a new tenant the same day.
- A lock cache that holds 50 entries when a unit has a tenant, several helpers and a maintenance code.
- Time zones and daylight-saving changes against expiry rules.

## Priorities for the insurer's report

1. Before November: credential expiry on the lock and signed server messages (item 1, steps 1 and 4). Signed on-lock event logs (item 2). Gate PIN length and lockout changes (item 3). Maintenance code limits (item 4).
2. By the first quarter: corridor gateways at the nine sites (item 1, step 2). These make the other fixes work much better.
3. Process changes you can make now at almost no cost: the two-person rule and photo redaction (item 6), helper confirmation (item 5), physical hasps on delinquent units.

Residual risk after these changes: a stolen but unlocked phone can still open units until the credential expires, and a determined insider with two colluding managers can still get around the rules. Both are far smaller risks than today's. Write them in the report as known and accepted. Insurers tend to respond better to honest limits than to a claim of none.
