# Where the Password Reset Design Can Break

## Summary
- **Target**: Email-based reset with a 6-digit code valid for 30 minutes, a 10-attempts-per-IP-per-minute limit, and sessions left alive after the password changes.
- **Critical Findings**:
  1. The 6-digit code can be brute-forced. The per-IP limit is the only throttle, and it is easy to get around with rotating IPs.
  2. Surviving sessions mean a reset does not evict an attacker who already has a session. For an account-takeover flow, that is the wrong default.
  3. Real-time phishing can relay the 6-digit code to the attacker within its 30-minute window.
- **Recommendation**: Fix before shipping. The core design needs changes to the throttling, the code lifecycle and session handling. The overall flow can stay.

## Threat Model
- **Spoofing**: Phished codes let an attacker impersonate the account owner at the reset step. Codes are not bound to the requesting session or device.
- **Tampering**: Attempts are not counted per code, so the same code can be guessed repeatedly across IPs. There is no evidence the code is invalidated after a wrong guess or after a successful reset.
- **Repudiation**: No mention of notifying the user that the password changed, so a silent takeover goes unnoticed.
- **Information Disclosure**: Unknown whether the "email not found" and "code sent" responses differ, which would enable account enumeration. Timing differences would too.
- **Denial of Service**: No per-account limit on code requests. An attacker can flood a victim's inbox with codes, and a per-IP limit does not stop a distributed flood.
- **Elevation of Privilege**: Anyone who completes the reset gets full account access, including the ability to change the recovery email, which then locks the owner out.
- **Supply Chain / Social Engineering**: Email provider access or a compromised mail account bypasses the whole flow. Support staff who reset accounts by hand are another route.

## Top 5 Attack Paths

### 1. Distributed brute force of the 6-digit code
- **Attacker profile**: Opportunistic attacker with a botnet or residential proxy pool. Low cost, low risk of detection.
- **Sequence**: Request a reset for the target email. Submit guesses from many IPs at 10 per minute each. Repeat with new codes as needed.
- **Arithmetic**: One IP gets 300 guesses in a 30-minute code window. The code space is 1,000,000, so one IP has about a 0.03% chance per code. With 1,000 IPs the attacker makes 300,000 guesses in that window, which gives about a 26% chance per reset. Repeated resets raise the odds further.
- **Detection**: Many failed attempts on one account from many IPs. Current per-IP limits will not catch this.
- **Current mitigations**: Per-IP rate limit only. The gap is the missing per-account and per-code limit.

### 2. Real-time phishing relay
- **Attacker profile**: Targeted or mass phishing. Medium effort.
- **Sequence**: The attacker sends a lookalike "verify your account" page. The victim enters their email, then the code the real service just emailed. The attacker submits the code and a new password within the window.
- **Detection**: Hard to detect server-side because the code is valid. Only a login-time signal, such as a new device or geography, would flag it.
- **Current mitigations**: None in the design. A 30-minute window gives plenty of time to relay the code.

### 3. Takeover that survives the reset
- **Attacker profile**: Anyone who already has a stolen session cookie, for example from malware or a session leak.
- **Sequence**: The attacker has a session, or the victim's reset was triggered by an attacker. The owner resets the password, but the attacker's sessions stay alive "for convenience". The attacker keeps access after the owner believes the problem is fixed.
- **Detection**: Sessions with a changed password but an old creation date. Little else.
- **Current mitigations**: None. Keeping sessions alive is the opposite of what a reset should do.

### 4. Recovery email hijack after the reset
- **Attacker profile**: Attacker who completes any reset, by brute force or phishing.
- **Sequence**: After the reset, the attacker changes the account's recovery email or 2FA settings. The owner can no longer reset again, and the attacker holds the account.
- **Detection**: Notification to the old address on any change to recovery settings. The design does not mention one.
- **Current mitigations**: None mentioned.

### 5. Inbox flood and reset-loop abuse
- **Attacker profile**: Harassment or sabotage. Low skill.
- **Sequence**: The attacker requests codes for a victim's email repeatedly. The victim gets dozens of codes, some from a valid session, and may enter one by mistake or give up.
- **Detection**: Request volume per account.
- **Current mitigations**: The per-IP limit applies only to attempts, not to code sends.

## Countermeasure Recommendations

Listed in the order the work should be done.

1. **Throttle per account and per code, not only per IP.** Lock the code after 5 wrong guesses, and invalidate it. Rate-limit code requests per account, for example 3 per hour, with a backoff. Keep the per-IP limit as a second layer.
2. **Shorten the code lifetime to 10 minutes and make it single-use.** Store only a hash of the code. Invalidate all outstanding codes when a new one is issued or the reset completes. Compare with a constant-time function.
3. **Revoke all sessions on password reset.** This is the single most important change. Keep only the session that just completed the reset, if any. Require a fresh login everywhere else.
4. **Notify the old and new contacts** whenever the password, recovery email or 2FA changes, with a clear "not you?" link. Require re-verification for recovery-email changes, and hold them for a cooling-off period (for example 24 hours) with a notice to the old address.
5. **Bind the code to the request.** Tie the code to the session or a device token created when the reset starts, and show the device or location in the email. A phished code then fails on a different device, and the victim sees a warning.
6. **Make enumeration uniform.** Return the same response and similar timing whether or not the email exists.
7. **Check the new password** against a breached-password list and the account's history at reset time.
8. **Use a CSPRNG for codes**, and never log codes or put them in URLs or referrers.
9. **Move rate-limit state to a shared store.** An in-memory counter per instance multiplies the effective limit by the number of instances. A shared store such as Redis fixes this.
10. **Handle IPs carefully.** Do not trust a client-supplied `X-Forwarded-For` header for the limit. Carrier NAT can lock out many legitimate users behind one IP, so the per-account limit is needed anyway.

**Detection and response**: Alert on several failed codes against one account from several IPs, on more than three reset requests per account per hour, and on a reset followed quickly by a recovery-setting change. Response: lock the account, notify the owner on all channels, and revoke all sessions.

## Edge Cases Identified
- **Multiple outstanding codes**: The user requests a second code, and the first still works. Expected: only the latest code is valid.
- **Clock and expiry**: A code submitted at 30:00 exactly, or after a server clock skew. Expected: a clear expiry rule with a tolerance, applied the same way on every instance.
- **Retry after lockout**: The user is locked out and tries again. Expected: a clear "try again in N minutes" message that does not reveal whether the account exists.
- **Shared-IP users**: An office or mobile carrier behind one IP. Expected: the per-account limit protects the account without blocking the whole IP.
- **Concurrent resets**: Two reset requests from the same user at once. Expected: one code survives, and the second request does not reset the first's attempt counter.
- **Password reused from before**: The new password matches the old one. Expected: rejected or flagged.
- **Email change during reset**: The recovery address changes mid-flow. Expected: the reset is cancelled or re-verified.

**Test cases**: Automated tests for lockout after 5 wrong codes, single-use codes, session revocation on reset, uniform response for unknown emails, and a concurrency test on two simultaneous requests.

## Residual Risk
- **Real-time phishing**: Even with device binding, a victim who approves a fake prompt can still be tricked. The residual risk is reduced, not eliminated. Phishing-resistant second factors (passkeys or hardware keys) remove most of it, and the reset flow should not become the weakest path around them.
- **Compromised email account**: If the mail account is taken over, the reset flow cannot tell the owner from the attacker. Recovery should not depend on email alone for high-value accounts.
- **Support-assisted resets**: Any human reset path is a social engineering target. It needs its own verification steps.

## What This Review Did Not Cover
- The actual implementation code, storage schema and where the rate-limit counters live. The multi-instance risk assumes an in-memory limiter, which is not confirmed.
- The email provider's delivery and logging behavior, and whether codes appear in logs or previews.
- Whether 2FA is enforced for the account, which would change the impact of a password takeover.
- Business rules for account recovery, such as who can unlock an account and how support handles requests.
- Expertise that would sharpen the findings: a review of the actual session store, and a penetration test with an authorized test account in a non-production environment.
