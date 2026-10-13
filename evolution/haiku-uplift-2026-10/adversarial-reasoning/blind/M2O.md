Short version: as described, this system can't give you a secret ballot, and the lost-link phone process lets anyone take over a unit's vote. Fix those two before links go out. I'm working only from your description, so treat these as questions to put to Varrow in writing, not as confirmed facts about their system.

**1. The vote is not secret.** Each submission is logged with timestamp, token ID and choices. Anyone who can read that log (the office manager, Varrow staff, anyone with portal admin, which includes Dorota) can match a unit to how it voted. Ask Varrow: can the logs be split so the token/unit record and the choices are never stored together? If not, you can't honestly call this a secret ballot under your bylaws.

**2. The link in the email is the password, and email is not private.** Whoever receives or can open the email can vote as that unit. That includes a tenant, a housemate, an ex-partner, someone with access to a shared inbox, or anyone who was sent to an old address. Ask: are tokens long and random, single-use, and do they expire or stop working once a vote is cast? (A link that keeps working after voting lets someone change a vote they never saw.)

**3. The lost-link phone process is the biggest hole.** Staff confirm unit number and full name, then send a new link to any address the caller gives. Unit numbers and names are easy to find (mailboxes, the building directory, social media, previous notices). An attacker calls, gives a victim's name and unit, asks for a new link sent to their own email, and votes. The old link is deactivated, so the real owner may not notice. Fixes to demand: new links only go to the address already on file; a new link triggers an email to the old address saying "your link was replaced, if this wasn't you call X"; or require a signed form or ID shown in person. Also ask for a log of every replacement, and have the board see the list before close.

**4. Proxies are the easiest way to cast a fake vote.** One person (the office manager) approves a scanned PDF. Nobody checks the signature against the owner's record, and the approved ballot then shows up on the proxy holder's page. Questions: how is each proxy checked against the owner's signature on file? Who else sees the approval? Can the owner revoke a proxy, and what happens if they vote directly too? Require two people to approve proxies, and send the owner a notice when a proxy is accepted for their unit.

**5. Live running totals are a problem.** Showing totals for each question while voting is open lets people (including whoever sees the dashboard) change their vote or push turnout based on the count, and it undermines a fair vote on a $1.9M assessment. Turnout by floor is also a privacy issue: on a small floor, turnout plus a known unit can reveal how a person voted. Ask Varrow to hide question totals until close, and to show turnout only as a building-wide number.

**6. Dorota's access is a conflict.** She is a candidate, has full portal admin rights, and is the liaison to Varrow. She could deactivate links, approve proxies, see logs and dashboards, or change things in the portal, all while running in the same election. Recommend: she recuses from admin actions during the vote, every admin action is logged, and a non-candidate board member (or an outside person) reviews the admin log before certification.

**7. Quorum and counting can be faked or unverifiable.** Quorum is 206 units (50% of 412). Fake links, fake proxies and lost-link replacements all count toward it. The CSV export is emailed as a plain attachment, so nothing shows it wasn't changed. Ask for: the export file's SHA-256 hash published to the board before and after the email, a count done from the raw records (not a summary), and a rule for what happens if the numbers don't match.

**8. Phishing will come.** A contentious vote with an emailed link is an easy target. Expect fake "your ballot link" emails. Tell members now: the official email comes from [exact address], the link goes only to the Varrow portal domain, and nobody will ask for a password or payment. Ask Varrow for a short written notice you can post in the building before links go out.

**9. Things to ask Varrow in writing (they should be able to answer all of these):**
- Are tokens random, long, single-use, and deactivated after a vote is cast?
- Is the token-to-choice log separable, and who can read it?
- What does the lost-link process require, and can a new link go to a new address without notice to the old one?
- Who approves proxies, how is the signature checked, and can approval be done by two people?
- Are question totals hidden until close?
- Who has portal admin rights, and is every admin action logged?
- Is the portal served over HTTPS, is there rate limiting on login and token attempts, and when was it last tested by someone outside Varrow?
- Can you give us a paper or in-person backup for members who can't vote online?

**What to do before Monday:** send the questions above to Varrow in writing. If they can't give clear answers to items 1, 3 and 5, push the board to either postpone or move the roof vote to a neutral platform or a paper ballot with independent counters. A contentious $1.9M vote needs more protection than a link in an email.

This is based only on your description, not on testing the system.
