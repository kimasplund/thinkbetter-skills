Blunt version: as designed, this system cannot deliver a secret ballot, and several paths let one person (or a Varrow employee) change the outcome of a contentious $1.9M vote without detection. I'd fix the top items before Monday or delay the launch. Assumptions: I only know what you wrote, and I haven't seen the software. Ask Varrow to confirm the points below.

## Critical (fix before launch)

**1. The ballot is not secret.**
- Each submission is logged with token ID plus choices. Token ID maps to a unit, so the log is a list of who voted how.
- The live dashboard shows running totals during voting. With 412 units, a floor with few votes, or a single new vote, reveals individual choices. It also lets people see how the vote is trending and pressure or target holdouts.
- Proxy holders see the proxied unit's ballot on their page, so they see how that unit voted.
- Fix: separate the "who voted" record (turnout) from the "what was chosen" record. Store ballots with no token or unit link. Otherwise your bylaws' secret-ballot requirement is not met, and a challenger can use that to void the result.

**2. Lost-link process is an account-takeover channel.**
- The unit number and the leaseholder's full name are public or easy to learn (directories, mailboxes, neighbors, ex-partners). The link then goes to any address the caller gives.
- Someone who wants to swing the roof vote can phone in for units that haven't voted, such as absent owners or elderly members, and vote for them.
- Because the last submission counts, an attacker can also overwrite a vote that was already cast. The real member may never notice.
- Fix: send replacement links only to the address on file, or require an in-person or ID-verified check for address changes. Notify the original address and any phone number on file whenever a link is reissued. Log who requested it and from what number. Limit when reissuing is allowed (for example, not in the last 24 hours without a second approver).

**3. Proxy approval is a single point of fraud.**
- One office manager approves proxies, and the proxy then moves that unit's ballot to the holder's page. A forged scanned PDF is trivial to make. Nobody checks signatures against anything.
- A holder can collect many proxies. You have no stated cap, no stated rule on whether the grantor can still vote, and no revocation process.
- Open questions: does the grantor's own link stay active? If the grantor votes after the proxy, who wins? Does the proxy cover both the election and the roof vote, or can it be limited?
- Fix: check your bylaws and state law for proxy limits and formalities. Require a second reviewer, a signature match against the lease file, and confirmation to the grantor by a separate channel. Cap proxies per holder, and publish the proxy list to the committee before the close.

**4. Concentrated insider power with no oversight.**
- Varrow staff can reissue links and approve proxies. They can probably see the data and export the CSV. The dashboard gives the office manager live totals.
- Dorota Weiss has full admin rights and is a candidate. She could view results live, edit settings or proxies, or alter data, and no one could show she didn't. Even if she never does anything, the appearance alone invites a challenge. She should not hold admin rights while on the ballot. Move her to read-only, or remove the access until certification, and let someone not on the ballot act as liaison.
- Varrow is also a party with an interest: the roof assessment may matter to its contract or fees. Don't let them be the only custodian of the evidence.
- Fix: no admin who is a candidate; a second person approves every admin action; an audit log that admins can't edit, ideally sent to someone independent.

**5. Results are exported and emailed as a CSV by the office manager, then you certify it.**
- You have no independent check that the CSV matches the database. An edit in a spreadsheet is undetectable. Email is not tamper-evident.
- Fix: have the committee, not Varrow, pull the final results with at least two people present. Compare the totals with the logged submission count and the turnout list. Keep a hash (checksum) of the export and a read-only copy of the full log. If you can, get an independent person to check.

## High

**6. Dashboard visibility during voting.** Live totals for a contentious vote let people campaign on the trend, and let any insider with access time a push. Show turnout only (counts, not choices) until close. Turnout by floor is also risky for small floors; use building-wide numbers.

**7. Tokens in URLs leak.** Links in email can be forwarded, sit in mail archives, get picked up by shared family or work inboxes, and may appear in browser history, server logs and referrer headers. Anyone with the link can vote or change the vote. Use single-use or short-lived links where possible, and add a second factor (for example, a unit-specific code mailed or handed out separately). Also confirm what happens to units with no email on file, stale addresses, or shared addresses between units.

**8. Change-your-vote plus last-submission-wins, with no receipt.** Members get no confirmation that their final ballot was recorded as they chose. Attackers (item 2) can overwrite quietly. Fix: send a confirmation email on every submission to the address on file, with a note that says to call the committee if you didn't do this. Don't put the choices in the email, since that weakens secrecy.

**9. Quorum and eligibility.** Who counts as a unit that can vote: leaseholders only? One vote per unit even with joint holders? Does a proxy count toward quorum? Is quorum on turnout of units or on completed ballots? Decide these before launch and write them down. Contentious votes get contested on exactly these points. Also check that your bylaws actually permit electronic voting and the notice period (the links go out Monday; check the notice rules for a special assessment).

**10. Access and fairness.** Some members have no email, poor internet, or limited English or disability access. Offer a paper or in-person alternative and a plan for counting those votes without breaking secrecy or double-voting. Failing to do so is a common basis for a challenge.

## Medium

- **Availability.** What if the portal goes down on the last day? Say now whether the deadline is extended and who decides.
- **Backups and retention.** Keep the data until the challenge window passes. Decide who holds it.
- **Data protection.** The logs hold names, addresses and votes. Check how Varrow stores and secures them, who can access them, and what their contract says.
- **Phishing.** Attackers can copy your voting email. Tell members the exact sender address and that you will never ask for a password or payment.
- **Reminder calls.** Calling nonvoters is fine, but use the "has not voted" list only, not choices.

## What I'd do this week

1. Ask Varrow in writing: How is the vote stored? Is the ballot unlinked from the token? Who can see or edit data? Is there an immutable audit log? Can the dashboard show turnout only?
2. Change the lost-link rule and proxy approval as described above.
3. Take admin rights away from Dorota until after certification, and say so openly, so no one can claim favoritism.
4. Name two committee members not on the ballot as observers for the close and the export.
5. Write a one-page procedure covering eligibility, proxy rules, quorum and what happens if something fails. Send it to members with the link.
6. If Varrow can't make the ballot truly secret, consider a different tool built for secret-ballot elections, or delay the roof vote. A tainted result on a $1.9M assessment is expensive to defend. Consider a short consult with a co-op lawyer on the bylaws and proxy rules.

I can draft the questions for Varrow or the one-page procedure if that helps.
