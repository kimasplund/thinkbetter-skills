# Where the Password Reset Flow Can Break

## Summary
- **Target**: Email -> 6-digit code (30 min validity) -> code + new password -> existing sessions kept alive. Rate limit: 10 attempts per IP per minute.
- **Critical findings**:
  1. The 6-digit code is brute-forceable because the limit is per IP, not per account or per code. A botnet or rotating proxies gets effectively unlimited guesses.
  2. Keeping all sessions alive after a reset means an attacker who already has a session (stolen cookie, shared device) survives the reset. The reset is the moment the user is saying "someone else may have access", and the design ignores that.
  3. Nothing is said about code lifecycle (single-use, one active code per account, invalidation on new request), so the 30-minute window can be abused repeatedly.
- **Recommendation**: Fix before shipping. The structure is fine, but the rate limiting and the session policy need to change.

## Threat Model
- **Spoofing**: Guess the code and take over any account whose email is known. This is the main attack on this design.
- **Tampering**: Changing the email parameter between the request and verify steps, if the code is not bound to the account it was issued for.
- **Repudiation**: No mention of logging reset requests, successes and failures, so a takeover cannot be reconstructed or the owner notified.
- **Information disclosure**: Differing responses for known vs unknown emails reveal who has an account. Codes in URLs or logs leak.
- **Denial of service**: An attacker can lock out or spam a victim by repeatedly triggering reset emails, or by burning the per-IP budget of a shared NAT.
- **Elevation of privilege**: Resetting an admin or support account gives the attacker everything it can do.
- **Supply chain**: The email provider and its logs are part of the trust chain. Anyone who can read the victim's mailbox owns the account.
- **Social engineering**: Phone or chat pretexting to get a user to read out a code.

## Top 5 Attack Paths

**1. Distributed brute force of the code (Impact 5, Feasibility 5, risk 25)**
The code space is 1,000,000 values. The attacker requests a reset for the victim's email, then submits guesses from many IPs, each staying under 10 per minute. With 1,000 proxy IPs that is 10,000 guesses a minute, so the whole space falls in about 100 minutes, and roughly 30% of it in the 30-minute window. Even from a single IP, 10 per minute gives 300 guesses per window, a 0.03% chance per request. Requesting a new code repeatedly (if each request issues a fresh valid code, or the old one stays valid) multiplies the odds. The attacker sets their own password and owns the account. Cheap residential proxy pools make this routine.

**2. Surviving attacker sessions (Impact 4, Feasibility 4, risk 16)**
The user suspects compromise (strange activity, lost laptop, a stolen cookie from malware) and resets the password. Because all sessions stay alive, the attacker keeps full access, including the ability to change the email, add recovery methods, or reset again. The user believes they are safe and are not.

**3. Mailbox or email-channel compromise (Impact 5, Feasibility 3, risk 15)**
Anyone with access to the victim's inbox (a compromised email account, a forwarding rule, a shared mailbox, a leaky mail provider) can complete the reset. A 6-digit code is also easy to shoulder-surf or read off a lock-screen notification.

**4. Account enumeration and reset spam (Impact 3, Feasibility 5, risk 15)**
If the response differs for unknown emails, an attacker can harvest the list of registered users. If there is no per-account limit on code requests, they can flood a victim with reset emails (harassment, or hiding a real alert in the noise) and cost money in email sends.

**5. Code reuse and replay (Impact 4, Feasibility 3, risk 12)**
If a code is not invalidated after use, or after a newer code is issued, anyone who sees it later (email archive, logs, a proxy) can reuse it within the window to reset again.

## Countermeasure Recommendations
Prioritized:

1. **Limit by account, not just IP.** Allow around 5 verification attempts per issued code, then invalidate it and require a new request. Also cap code requests per account (for example 3 per hour). Keep the per-IP limit as a secondary layer, not the main defense. This alone kills attack 1.
2. **Make the secret stronger.** Use a long random token in a link (128 bits), or at least a higher-entropy code. If you keep 6 digits for UX, shorten validity to 10 to 15 minutes and enforce the 5-attempt cap strictly. Store only a hash of the code, and compare in constant time.
3. **Revoke other sessions on reset.** Invalidate all existing sessions and refresh tokens when the password changes, and issue a fresh session for the device that did the reset. If you want convenience, offer "keep me signed in on this device" as an explicit choice, never the default for all sessions.
4. **Make codes single-use and singular.** A new request invalidates earlier codes. A successful reset invalidates the code immediately. Bind the code to the account and to the reset request, not just to the email string.
5. **Uniform responses.** Return the same message and similar timing whether or not the email exists ("If that account exists, we sent a code").
6. **Notify and log.** Email the account owner when a reset is requested and when the password changes, with a "this wasn't me" path. Log requests, failures and successes with IP and device.
7. **Higher-risk accounts.** Require a second factor (TOTP or passkey) for reset on admin accounts and any account with MFA enabled, so email access alone is not enough.
8. **Detection.** Alert on many failed code attempts across IPs against one account, and on spikes in reset requests.

## Edge Cases Identified
- **Timing**: A code expires at the 30-minute mark while the user is typing the new password. Define whether expiry is checked at submit, and let the user restart gracefully. Clock skew between app servers can cause early or late expiry.
- **Concurrency**: Two tabs submit the same code at once. Without an atomic "consume" step both may succeed, or one fails confusingly. Use a single atomic update.
- **State**: A user requests a code, then logs in successfully with the old password. The pending code should be invalidated. Likewise, a password change elsewhere should kill outstanding codes.
- **Shared IPs**: Offices, universities and mobile carriers (CGNAT) share one IP. A per-IP limit of 10 a minute can block legitimate users, and an attacker can deliberately exhaust it for a whole network.
- **Boundary conditions**: Leading zeros in the code (a code stored as an integer loses them), whitespace or pasted formatting, and a new password equal to the old one.
- **Email delays**: The email arrives after 30 minutes, or the user requests a second one and uses the first. Make the "latest code wins" rule clear in the UI.
- **Case and normalization**: Email case or Unicode variants resolving to different accounts or bypassing per-account limits.
- **Integration**: Email provider outage, so users cannot recover at all. Have a support-assisted fallback with strong identity checks, which itself needs hardening against social engineering.

## Residual Risk
- A compromised mailbox still means a compromised account unless a second factor is required.
- A 6-digit code, even capped at 5 attempts, still has about a 1 in 200,000 chance per issued code of being guessed. Attackers with unlimited reset requests could exploit that, so per-account request caps matter.
- Phishing pages that capture the code in real time remain possible.
- Revoking sessions inconveniences legitimate multi-device users. That is the intended trade-off.

## What This Review Did Not Cover
- The login flow, MFA design, session token storage and cookie settings, and how the reset link or code is delivered in the email template.
- Infrastructure details (how the rate limiter is implemented, whether IP detection behind proxies can be spoofed via headers like X-Forwarded-For, which is worth checking since it would defeat the per-IP limit outright).
- Whether the email is the only recovery path, and the support-desk recovery process.
- Assumed: a skilled attacker with access to commodity proxy services, no insider access. A review with your actual stack and logs would sharpen the likelihood estimates.
