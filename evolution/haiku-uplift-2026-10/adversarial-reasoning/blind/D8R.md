Blunt answer first: as described, this system would let a motivated person swing the roof vote without anyone noticing, and it would let people see how each unit voted, which breaks your bylaws. Several of the problems are not technical at all. They come from who has power over the links, the proxies and the data. Fix the first group before the links go out next Monday.

I'm working from your description only. I haven't seen the portal, the emails, or Varrow's contract, so treat the items below as the questions to put to Varrow in writing, not as proven facts.

## Assumptions

- The attacker is a determined member or outsider who can find out a neighbour's name and unit number, or who gets into someone's email. They don't need to be a hacker.
- Dorota Weiss, or anyone with office access at Varrow, is someone who could act on purpose or by mistake.

## The biggest problems

**1. Anyone who can get a unit's name and number can take over that unit's vote.**
Unit numbers and names are easy to find (mailboxes, buzzers, neighbours, old newsletters). A caller who gives those two facts gets the old link switched off and a new link sent to any email address they name. That is the whole attack, and it takes one phone call per unit. An attacker could do it to dozens of units in an afternoon, and the owners would find out only when they tried to vote. Varrow staff, or anyone with the admin rights below, could do this silently.
- Fix: a new link should go only to the email address already on file, or be sent by post to the unit. Require a second check, such as a code sent to the old address. Log every replacement and tell the owner by email when it happens.

**2. The voting links themselves are fragile.**
A link is a secret key in the web address. Anyone who receives it, sees it in a forwarded email, or finds it in browser history or a shared computer can vote with it. Nothing ties the link to the person who should be voting, so a spouse, a tenant or a relative can vote for them, and someone can buy or pressure votes by asking for the link.
- Fix: ask Varrow whether the link can be used only once a person has also confirmed something only they know, and whether links expire when voting closes.

**3. Phishing emails can harvest links.**
Members are trained to expect emails from Varrow with links. A fake "your voting link has changed, vote again here" email from a look-alike address would collect links from people who think they're doing the right thing. Warn members now: the committee will never ask anyone to re-vote by email, and the only real link comes from one specific sender.

**4. Your secret ballot is at risk from the data you're collecting.**
- Each submission is logged with a token ID and the choices. Anyone who can read the log can match a unit to its vote. That is a direct breach of your bylaws.
- The live dashboard shows turnout by floor and running totals. On a floor of 20 to 40 units, a floor breakdown can reveal how a small group voted, and running totals let people watch the vote move and target pressure.
- The CSV export is emailed to the committee. Email is not a secure channel, and the file contains unit-by-unit choices.
- Fix: keep the per-unit log out of anyone's reach except one independent auditor. Show turnout only, not choices, until close. Remove the per-floor choice breakdown. Replace the emailed CSV with a count that the committee and an outside person can each verify on their own, with the unit-level file held by the auditor.

**5. Proxy forms can be forged, and the proxy holder sees the ballot.**
Varrow's office manager approves proxies from a scanned PDF. Nobody checks the signature against the owner's records, and a forged form could hand a unit's vote to someone else. The proxy holder's page showing the unit's ballot also means the proxy holder can see how that unit voted, which is a secret-ballot problem.
- Fix: verify each proxy by calling the owner on a number already on file, and keep a log of who approved it. Say in the bylaws what happens if the owner then votes too. Don't show the unit's ballot to the proxy holder, only confirm that the vote was cast.

**6. Dorota has admin rights while running for re-election.**
As vice-chair she can switch off links, issue new ones, approve proxies and see the dashboard, and she's a candidate. Even with good intentions, that is a conflict you can't defend. Someone with no stake in the election should hold admin rights, and every admin action should be logged and visible to the committee.

## Other risks

- **Last vote counts, and votes can be changed until close.** This lets someone who obtained a link after the real owner voted change the result late, and the owner may never notice. Ask Varrow to email owners a confirmation each time their vote changes.
- **Quorum can be pushed either way.** Fake votes can help reach 50% (206 units). Switching links off can stop it. Monitor both.
- **Portal under load near close.** A rush at the deadline, or someone flooding the site, could lock people out with no way to recover in time. Ask for a stated fallback, such as an extended deadline with notice.
- **The management company is a single point of trust.** Varrow has the data, the phone desk, the proxy approvals and the export. Ask whether they have a written security policy and who else at their firm can access your portal.

## Edge cases to test

- A unit with two leaseholders, one of whom has a different email. Who can vote, and does the second person's vote replace the first?
- A unit sold or rented during the 10 days. The old owner's link goes to an address the new owner doesn't control.
- Owners whose email on file is out of date, shared with a spouse or a tenant, or missing. These units may never get a link.
- A proxy holder who also owns a unit, or who holds several proxies. Is there a limit?
- Someone who votes on two devices or double-clicks submit. Does a duplicate count?
- A deadline in a different time zone, or one that falls on the last moment of the 10 days.
- An email sent to spam, so a member thinks they can't vote and calls in for a replacement link.

## Countermeasures in priority order

1. Replacement links: verify the caller against the address on file, not the address they give. Notify the owner. (Stops the phone takeover.)
2. Remove the choices from the log, the dashboard and the emailed CSV until close. Give the auditor the only full record. (Restores the secret ballot.)
3. Move Dorota's admin rights to someone neutral and log all admin actions. (Removes the conflict.)
4. Verify every proxy with the owner before approving, and stop showing the unit's ballot to the proxy holder. (Stops forged proxies.)
5. Send owners a confirmation email for every vote, including changes. (Lets owners catch a takeover.)
6. Send a clear warning to members about phishing, and publish the one real sender address. (Blocks fake emails.)
7. Ask Varrow in writing about their security policy, hosting, and staff access. (Covers the vendor risk.)

## Residual risk

Even with all of this, a person can still buy or coerce votes by asking a neighbour to vote on their behalf, and a link forwarded to someone else still works until it is used or closed. Secret-ballot protections depend on Varrow doing what they say, and you have no independent way to check that during voting. The fix is to make the result checkable after close: an independent count, the unit-level list held by a neutral auditor, and a published turnout figure.

## How sure I am

Moderately sure on the main findings, because they follow directly from your description. Low on the specifics of Varrow's system, since I can't see it or test it. I'd suggest a short written question list to Varrow, and if you can get a test link and a test proxy, a volunteer should try the phone replacement and the proxy approval on a dummy unit before Monday.
