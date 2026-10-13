**Verdict: don't ship as designed. Two parts are broken outright (the rate limit and keeping sessions alive). Both are cheap to fix.**

I assumed a skilled attacker who can rent proxies or botnet IPs, and who may already hold a stolen session or know the victim's email address. I also assumed the code is the only proof of identity at the reset step.

## The serious problems

**1. Keeping all sessions alive after a reset (Critical)**
People usually reset a password because they think the account is compromised. If an attacker already has a session, whether from a stolen cookie, malware, or a borrowed laptop, the reset changes the password and the attacker stays logged in. The attacker never needs the new password. They also keep access to anything that doesn't re-check it, such as API tokens, "remember me" cookies, and email-change flows.
- Fix: on a successful reset, revoke every session and refresh token, and invalidate API tokens tied to the old credentials. Then sign the user in on the current device only, and email them that "your password was changed and all other devices were signed out".
- If convenience matters, keep only the session that completed the reset. Never keep the others.

**2. The rate limit protects the wrong thing (Critical)**
A 6-digit code has 1,000,000 possible values. The limit is 10 attempts per IP per minute, and it is tied to the IP, not the account being attacked.
- From one IP, an attacker gets about 300 guesses in the 30-minute window, roughly a 0.03% chance. That alone looks fine.
- Attackers don't use one IP. With a few thousand proxy IPs, or a single IPv6 /64 if you key on the full address, the per-IP limit never triggers. About 3,000 IPs at 10 guesses each cover 30,000 guesses in a single minute, a 3% chance against one victim. Across the 30-minute window the odds approach certainty. Cost is a few dollars of proxy time.
- The attacker only needs the victim's email address, and then owns the account. With the sessions issue above, they also stay in.
- Fix: limit by **account/reset request**, not only by IP. Allow 5 wrong guesses, then permanently invalidate that code and require a new one. Keep the per-IP limit as a secondary control.
- Make the counter atomic (a single increment-and-check in the database or Redis). A read-then-write counter lets parallel requests slip extra guesses past the limit.

**3. Code lifetime and lifecycle (High)**
Thirty minutes is long for a 6-digit secret. Nothing in the design says what happens in these cases:
- Is the code single-use? If not, a code seen over a shoulder or in a mail preview can be replayed.
- Does requesting a second code invalidate the first? If not, an attacker can request many codes and multiply their chances, since each new code is another valid target.
- Is the code stored hashed, and compared in constant time? A plain-text code in the database turns any read-only DB leak into an account takeover.
- Fix: single-use, newest code replaces older ones, store a hash, drop the lifetime to 10-15 minutes. Better still, bind the code to the reset attempt: issue a random reset token in a cookie or in the link at request time, and require code and token together. A guesser then also has to hit the right in-flight request.

## Medium-priority issues

**4. Account enumeration.** If "email not found" looks different from "code sent" (different message, status, or response time), attackers can check which emails have accounts. Always return the same message and similar timing, and send the email asynchronously. Apply the same rule to the code-entry step, so a wrong email and a wrong code can't be told apart.

**5. Email bombing and abuse of your sender reputation.** There's nothing about limiting how many reset emails go to one address. An attacker can flood a victim's inbox, harass them, or burn your sending reputation and get your domain blocklisted. Limit sends per email address (for example 3 per hour) and per IP, and add CAPTCHA or a proof-of-work step after a few requests.

**6. The email account is the weakest link.** Anyone who controls the victim's mailbox controls the account. For high-value accounts, require MFA at the reset step, or add a delay and notification before the change takes effect. Send "password changed" notices to the old email, and add a recovery/undo link for a short window.

**7. Weak new-password handling.** The reset form accepts a password, so it needs the same checks as signup: minimum length, a breached-password check, and no reuse of the last few passwords. Otherwise the reset flow is a back door around your password policy.

**8. The code can leak.** Do not log codes. Do not put them in URLs that end up in referrer headers or analytics. Keep them out of the email subject line, where lock-screen previews and notification mirrors can expose them.

## Edge cases to test

- **Leading zeros**: code `004217` must not be stored or compared as the number 4217.
- **Email normalization**: `Bob@x.example` vs `bob@x.example`, Unicode look-alikes, and plus-addressing should all map to the same account, or you'll send codes to the wrong place or create duplicates.
- **Parallel guesses**: fire 50 simultaneous requests at the same account and confirm only 5 get evaluated.
- **Double submit**: two submissions of the correct code at once should result in one password change, not two.
- **Expiry boundaries**: a code submitted at exactly 30:00, clock skew between servers, and a retry after a timeout.
- **User signed in elsewhere while resetting**: confirm that device is actually logged out.
- **Mail delay**: a user requests three codes because email is slow, and then uses the first. Decide on purpose whether that works.

## Recommended order of work

1. Revoke all other sessions on reset, with a notification email. Small change, closes the worst gap.
2. Per-account attempt cap (5 tries, then the code dies), atomic counter. This is what actually stops guessing.
3. Single-use hashed codes, newest request invalidates older ones, shorter lifetime, and tie the code to a per-request token.
4. Uniform responses and per-address email send limits.
5. MFA or delay for sensitive accounts, plus password policy checks on the new password.
6. Alerting: spikes of failed code attempts across many IPs for the same account, or many resets across many accounts from one ASN, are both clear signs of an attack.

## What's left after these fixes

The residual risk is mainly a compromised mailbox and phishing (a fake page that asks the victim for their code). Short expiry, MFA on sensitive accounts, and the "password changed" notification reduce both, but you can't remove them while email is the recovery channel.

I'd call the redesign low-risk once items 1 to 3 are in. Items 4 to 6 can follow in the next cycle. This is based on the description you gave. I haven't seen how the code is stored, how the counters are implemented, or whether MFA exists, so check those directly.
