Blunt version: as described, this setup would not survive a contested $1.9M vote. Several flaws are serious enough that I would delay the launch, or at least fix the top five items below before Monday. I'm assuming the portal is a Varrow-operated system you can't inspect, and that your bylaws say nothing specific about electronic voting. Check both.

## The biggest problems (fix before launch)

**1. The ballot is not secret, and the bylaws require it.**
Every submission is logged with token ID and choices. Varrow knows which token went to which unit, because it emailed them. So anyone with log access can see how each unit voted. The same is true of the CSV export. The live dashboard also shows running totals for each question while voting is open. On a 412-unit building, with turnout by floor, small groups can be identified. If a floor has 6 votes in so far and the totals move by one, you know how that person voted.
- Fix: separate the identity from the choice. Record that unit X voted (a participation list) in one place, and store the choices with no token or unit link. Use a vendor built for secret-ballot elections if Varrow's tool can't do this. Ask Varrow in writing exactly what is stored and who can see it.
- Note that "change your vote until close, last counts" makes secrecy harder, because the system has to match the later vote to the earlier one. A properly designed system can do this without revealing the choice. A logged token ID plus choices cannot.

**2. Live results and the dashboard can distort and contaminate a contested vote.**
Running totals visible to board members and Varrow staff mean insiders can see how the roof vote is going and target reminder calls at the side they favour. That is a real fairness problem in a contentious election. It also leaks information that can be used for pressure.
- Fix: show only turnout (number voted, and ideally who hasn't voted) and no per-question totals until close. Do not show turnout by floor unless floors are large. Better still, limit reminders to a single building-wide message plus a list of non-voters.

**3. The "lost link" phone process is an account takeover with a phone call.**
Anyone who knows a unit number and the leaseholder's full name, both of which are easy to find (mailboxes, a directory, a neighbour, a landlord, a family member, an angry ex), can call and have a fresh link sent to any address they give. The old link is deactivated, so the real member is locked out, and may not notice. A bad actor could also vote for a unit that they know won't vote. Staff are also under no obligation to log these calls.
- Fix: only reissue to the address on file. If the address has to change, require the member to come in person or verify by something the real member has, and notify the old address and the unit by mail when any link is reissued. Keep a written log of every reissue (who, when, what verification), reviewed by the committee, and not just by Varrow.

**4. The proxy process gives one person at Varrow control over votes.**
Proxies are PDFs uploaded to the portal and approved by the office manager. A scan of a signature is easy to forge, and the person approving it is a Varrow employee with no independent check. When approved, the ballot appears on the proxy holder's page. Problems:
- Nobody checks the signature against a record.
- One person can quietly approve (or reject) proxies. In a contested vote, that is a lot of power.
- One holder could accumulate many proxies. Your bylaws probably limit this. Check, and enforce a limit in the system.
- A proxy holder who sees the ballot can see how the grantor's unit has voted if the grantor already voted, and the grantor can still vote themselves after granting a proxy. The rules for who wins in that case have to be written down.
- Fix: the committee, and not Varrow, approves proxies, with two people reviewing. Publish the proxy count and holders' names. Match signatures to leases. Set a proxy deadline earlier than the voting close. Decide and publish the rule: a direct vote overrides a proxy, or the proxy locks the unit out. Confirm that your bylaws allow proxies in this format at all.

**5. Dorota Weiss has full admin rights and is on the ballot.**
This is a conflict of interest, however honest she is. Full admin could allow her to see logs, approve proxies, reissue links, edit unit records and export results. She does not have to do any of that for the appearance to destroy the result's credibility, and in a contested election the losing side will say so. Nobody could prove otherwise, because the logs are controlled by the same people.
- Fix: before the election, remove her admin rights, or reduce them to read-only access that doesn't include any voter data, and she shouldn't see per-unit voting records. Have her recuse from all election-administration matters. Tell members that you did this. Ideally, no candidate and no one with a stake in the roof vote holds any admin power.

## Other serious problems

**6. Results go by CSV email, from one person, with no independent check.**
The office manager exports and emails the results, and you certify. Nothing proves the file matches what members actually submitted. Email can be altered, and the exporter can edit a CSV before sending. There is no neutral person who can verify the count.
- Fix: have two people from the committee present for the export (a screen share is fine), record the total number of ballots and a checksum of the file, and cross-check the number of ballots against the participation list. Keep an untouched copy of the raw export and logs. Do the count with at least two committee members who are neither candidates nor have a stake. Keep every record for at least as long as the challenge period in your bylaws or law.

**7. Link emails are weak, and nobody verifies the address list.**
The links go to "the address on file." Out-of-date addresses, shared emails, units with several owners, units that are sublet, and email accounts that other people can read mean that some links go to the wrong person. A forwarded email is a forwarded vote. Anyone with the link can vote, and the token in the URL can leak through browser history, forwarded mails, mail-scanning tools, and logs.
- Fix: audit the address list now against your membership register. Send a printed notice to every unit saying that links are being sent and to whom, so members notice if they didn't get one. Make links single-use for logging in, expire them, and add a second factor, such as a code mailed or texted to the member separately. Offer a paper or phone alternative for members who have no email, because excluding them can invalidate the election.

**8. Quorum and the "unit" definition.**
Quorum is 50% of units, i.e. 206. Decide what counts toward it: do proxy ballots count? Do partial submissions (voted on the board but not the roof) count? If Varrow reissues a link, is there a risk of two votes for one unit? State it. A $1.9M special assessment may also need a supermajority or a separate threshold under your bylaws or state or provincial law. Check that. If the threshold is not met, the result will be challenged.

**9. Audit logs: weak and mutable.**
The logs should show who changed what, when, including reissues, proxy approvals, admin actions, and exports. You've only described submissions. Ask whether logs can be edited by Varrow or by admins, and whether they're backed up. Ask what happens if the portal goes down on day 9, and what the plan is if there is a dispute, a bug, or a breach.

**10. Basic security you can't see.**
You don't know whether the portal uses HTTPS, how tokens are generated (long and random, not guessable or sequential), whether there's rate limiting, whether admin accounts have strong passwords and two-factor authentication, or whether there's been any independent test. Ask Varrow for these answers in writing. If you get vague answers, assume the worst.

## What I'd do this week, in order

1. Postpone the launch by a week or two if Varrow can't answer the secret-ballot question (item 1) in writing. A late start costs less than a voided $1.9M vote.
2. Remove Dorota's admin rights and have her recuse from the process (item 5).
3. Turn off per-question live totals (item 2).
4. Change the lost-link process and the proxy approval process (items 3 and 4).
5. Audit email addresses and send a paper notice to every unit (item 7).
6. Set up the two-person export and verification routine, and keep records (item 6).
7. Check the bylaws and local law on electronic voting, proxy format, thresholds and challenge periods. Consider asking a lawyer for an hour of review, given the size of the assessment. This is the one place I'd spend money.
8. Send members a clear plain-language description of the process before voting opens, including how to report a problem. Transparent rules lower the chance of a challenge more than anything else here.

If you tell me what the portal vendor is and what your bylaws say about proxies and special assessments, I can tighten this list.
