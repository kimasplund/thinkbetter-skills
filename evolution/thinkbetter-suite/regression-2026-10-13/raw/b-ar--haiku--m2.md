# Password reset: how it breaks

**Verdict: Fix before shipping.** Two design choices are serious. The 6-digit code protected only by a per-IP limit can be brute-forced through distributed IPs, and keeping all sessions alive after a reset means an attacker who already has access keeps it.

**Assumptions:** the attacker can reach the public endpoints, has no access to the victim's mailbox at the start, and may use a botnet or residential proxies. I assumed codes are sent by email and that the reset endpoint accepts email, code and password in one request.

## Critical

**1. Brute-forcing the 6-digit code across many IPs**
- The code space is only 1,000,000 values. The limit is 10 attempts per IP per minute, and nothing limits attempts per account.
- A single IP would need roughly 35 days to hit the right code, but a botnet or proxy pool multiplies throughput. With 1,000 IPs the attacker gets about 10,000 guesses per minute, so the full space falls in roughly 100 minutes. Within one 30-minute validity window, a 100-IP pool gets about 30,000 guesses, roughly a 3% chance per code.
- IPv6 makes per-IP limits weaker still, since one host can hold a large prefix.
- *Fix:* cap failed attempts per account (about 5 per code), then invalidate that code and require a new request. Limit by account and by IP separately, and add a global or CAPTCHA step after repeated failures. Use a longer code (8+ alphanumeric characters) or a high-entropy token in a link, not a 6-digit number.

**2. Sessions survive the reset**
- If an attacker already has a session (stolen cookie, earlier breach, malware), a password reset does not remove it. The user believes the reset fixed things, but the attacker is still in.
- *Fix:* on successful reset, revoke all existing sessions and refresh tokens, then require a fresh login. Keep only the session that is created by the reset itself, if any. "Keep alive for convenience" should be dropped. Offer a "stay signed in" option only after normal login.

## High

**3. Codes stay valid for 30 minutes and may not be single-use**
- Several codes may be valid at once if each request issues a new one without invalidating the older ones. An attacker who triggers many requests gets several targets.
- Concurrent submissions of the same code can race and both succeed if the check and the consumption are not atomic.
- *Fix:* invalidate any earlier code when a new one is issued. Consume the code atomically in the same transaction as the password change. Shorten validity to 10 minutes.

**4. The flow is not bound to one request sequence**
- The endpoint takes email, code and password in one body. Nothing ties the code to the session that requested it, so the code can be replayed against a different email or in a different order.
- *Fix:* create a server-side reset record keyed to the account and a signed, random flow ID. The code check must match both.

**5. Email enumeration**
- Different responses or timing for registered and unregistered emails reveal which accounts exist.
- *Fix:* return the same message and similar timing for both cases.

**6. Attacker-triggered reset spam and lockout**
- Anyone can request resets for a victim's email, flooding their inbox and training them to ignore real resets.
- *Fix:* rate-limit reset requests per account (for example, 3 per hour), and show a neutral message.

## Medium

**7. No notification of the change**
- Users don't learn their password changed unless they see an email, so a hijacked account is hard to notice.
- *Fix:* email the old address (and any recovery address) when a password changes, with a "this wasn't me" link that locks the account.

**8. Trusting spoofable client IPs**
- If the rate limit reads `X-Forwarded-For` or similar headers without a trusted proxy list, the attacker sets a fresh IP on every request and the limit disappears.
- *Fix:* only trust forwarding headers from known proxies. Rate-limit on the connection IP or on an authenticated identity.

**9. Weak new-password checks**
- The new password is not stated to be checked against breached-password lists or against the previous password.
- *Fix:* check against a breached-password list (k-anonymity API or local list), reject reuse, and apply the same policy as signup.

**10. Code delivery channel**
- Codes sent in email are exposed to anyone who reads the mailbox, including shared devices and notification previews. Codes must never be written to logs or analytics.
- *Fix:* keep codes out of logs and error messages. Hash codes at rest. Use a constant-time comparison.

## Edge cases to test

- Request a code, request a second one, then try the first. The first should fail.
- Submit the same code from two parallel requests. Exactly one should succeed.
- Submit a valid code with a different email. It should fail.
- Submit a valid code but skip the new-password step, or send only the code. Nothing should change.
- Reset while holding a valid session from before the reset. That session should be dead afterwards.
- Trigger 11 failed attempts from one IP across 11 accounts, then try a real account from a new IP. The account-level limit should still hold.
- Send the same request with and without a spoofed `X-Forwarded-For`. The result should be identical.
- Use a password that is in a breach corpus, or the current password. Both should be rejected.
- Time the response for a registered and an unregistered email, and compare.

## Residual risk after fixes

- Anyone who controls the email account can still reset the password. Email security (2FA on the mailbox, recovery codes, or a passkey) is the real limit.
- Session revocation does not stop an attacker who still holds the victim's email. The notification email is the only early warning.

## Recommendation

Ship only after items 1 and 2 are fixed and the edge-case tests pass. Items 3 to 6 should go in the same release. Items 7 to 10 can follow in the next cycle, but are cheap to include now.

**Confidence: moderate.** I have only the description, not the code or the rate-limit implementation. Items 1 and 2 are clear from the description alone. Items 3 to 10 depend on details the design doesn't state.
