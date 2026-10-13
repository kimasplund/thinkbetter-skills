Blunt answer: as described, this design can be broken easily, and several of the breaks are by insiders. For a contentious $1.9M vote, I would not send links Monday unless you fix the first five items below. Assumptions: I have not seen the portal or Varrow's contract, so some of this needs confirming with them.

## The big problems, worst first

**1. The secret ballot does not exist.**
Every submission is logged with timestamp, token ID and choices. Varrow maps token to unit (they email the links), so anyone with log access can see how each unit voted. The dashboard and the "proxy holder's page" also tie ballots to units. Your bylaws require a secret ballot, so this is a bylaw violation, and it also invites coercion and retaliation in a contentious vote. Anyone who can see the log, the CSV or the admin screens can see how your neighbors voted.
Fix: store ballots without the unit or token link. Keep a separate "has voted" record (unit, timestamp) and a separate ballot box (choices only, no identity). Ask the vendor in writing whether the system can do this. If it cannot, you need a different tool or a different process.

**2. The "lost link" phone process is an account-takeover hole.**
Anyone who knows a unit number and the leaseholder's full name (both easy to find: mailing lists, notices, neighbors, a hostile relative or ex-partner) can call, and Varrow emails a fresh link to any address the caller gives. The old link is deactivated, so the real member may also be locked out and not notice. Worse, if the real member already voted, the impersonator can vote again, because the last submission counts.
Fix: send replacement links only to the address on file, or hand them over in person with ID. Log every reissue and notify the original address and the committee. Cap reissues per unit. Reissues should be reported to you daily.

**3. Varrow staff and Dorota can vote for people or change results, undetected.**
The office manager approves proxies, reissues links, sees the live running totals and exports the final CSV. Dorota has full admin rights and is on the ballot. Nobody independent watches any of it. Specific abuses:
- Reissue a link for a non-voting unit to an address they control, then vote.
- Approve a fake or altered proxy.
- Edit the CSV before emailing it. You certify a file you cannot check.
- Use live totals to decide which units to chase or discourage.
A candidate with full admin rights is a conflict of interest even if Dorota is entirely honest, because the result will not be trusted. Contentious roof vote plus a candidate with admin power equals a challenge to the result.
Fix: Dorota loses admin rights (or has read-only access) until the election is certified, and this is recorded. No candidate, and nobody with a stake in the roof outcome, gets admin access. Two people, neither a candidate, review reissues and proxies. An independent person (an election inspector, or a neutral third party) gets read access to the raw data.

**4. Live running totals are a manipulation and fairness problem.**
Turnout by floor is a mild concern (it can pinpoint pressure and canvassing). Running totals for each question are worse: they let people see whether the roof assessment is winning and target reminders at likely supporters or opponents, and they discourage voters who think it is decided. Totals can also expose individual votes on a small floor or late in the process (if you know 11 of 12 units on a floor voted and the total moved by one, you know that vote).
Fix: show turnout only, and only the overall number against quorum. No per-question totals until close. If you want floor-level data, suppress counts below a threshold (for example, fewer than 10 units).

**5. Proxies are the weakest link.**
A scanned PDF is trivially forged, and one office manager decides on approval. Then "that unit's ballot appears on the proxy holder's page", which means the holder sees and controls it, and the holder's access is separate from the owner's. Open questions:
- Can the owner still vote, and who wins, the owner or the holder?
- Can one person collect many proxies? (Check your bylaws for a cap.)
- Does a proxy for the roof assessment carry the same rules as a board vote?
- Can a proxy be revoked? When?
- Are proxy holders also seeing the owner's choices?
Fix: check what your bylaws and state or provincial law say about proxies for assessments. Define a cap and revocation rule. Verify the signature against the file. Have two non-candidate people approve. Publish a list of approved proxies (unit and holder, no vote) to the committee before close. Better: require a proxy to be directed (the owner tells the holder how to vote) or let the owner vote directly and override the proxy.

**6. Bearer links mean anyone with the email has the vote.**
The token in the URL is the only credential. Forwarded emails, shared family inboxes, email scanners, browser history, referrer headers and shared computers can all leak it. Members who do not use email, or whose address on file is outdated, are silently disenfranchised, or their link goes to a former tenant or an ex.
Fix: confirm addresses before Monday. Offer a paper or in-person alternative. Add a second factor (for example, a unit code mailed on paper or a PIN). Tokens should be long and random, single-account, and not shown in reminders.

**7. "Change until close, last submission counts" combined with the issues above.**
It is good for voter freedom (it helps against coercion), but combined with reissue fraud it lets an attacker overwrite a real vote on the final day. Also, a late change near close leaves no time to detect and correct anything.
Fix: send every voter a confirmation email on each submission to the address on file ("your vote was recorded or changed at X"). That is the best cheap detector you have. Consider closing at a time when staff and committee are reachable, and freeze reissues and proxies a day or two before close.

**8. Results and audit trail are not independently verifiable.**
The CSV is exported and emailed by the office manager. Emailed files can be altered, and you have no hash, signature or second source. The log mixes identities and choices (see item 1). You also have no plan for disputes.
Fix: the export is produced at close with two people present (one from the committee, not a candidate). Record a hash of the file. Have the system keep an immutable record of ballots and reissues. Keep the raw data until the challenge period ends. Check your bylaws for a recount and dispute procedure and write it down now.

**9. Quorum and the 50% threshold.**
Quorum is 50% of 412 = 206 units. Check whether bylaws or law require more for a special assessment (often a supermajority of all units, not of votes cast) and whether abstentions count. Confirm what happens if a unit has joint owners, sublets or is vacant, and who is eligible (leaseholder only?). A proxy may count toward quorum. Decide in advance, and write it down.

**10. Availability and process.**
Test the system with a dry run this week. What if the portal goes down on day 9? What if the email is blocked or goes to spam (send a test to all units)? Who can extend the vote and under what rule? Do accessibility needs (no internet, older members, language) need paper options? Privacy: unit and name data lives with Varrow, so check their data handling and retention.

## What to do before Monday

Must do:
1. Remove admin rights from Dorota and any other candidate until certification.
2. Ask Varrow in writing: is the vote record separated from voter identity? Who can see the log, token mapping and CSV? If they cannot answer, delay.
3. Change the lost-link process: send only to the address on file, or in person with ID, and report every reissue to two non-candidate committee members.
4. Turn off per-question live totals. Show turnout only.
5. Turn on confirmation emails per submission.
6. Settle proxy rules (cap, revocation, approval by two people, who wins when both vote).
7. Do a test send to confirm that addresses work, and run a dry run with a test ballot.

Should do:
- Appoint an independent election inspector or a neutral third party to observe the close and export.
- Offer a paper or in-person option.
- Get a legal opinion on whether the assessment vote and bylaws allow electronic voting at all. Many bylaws and statutes require specific notice or methods, and a $1.9M assessment is exactly what a dissatisfied owner will challenge.

If Varrow cannot do items 1 to 5, I would postpone the online vote rather than run a flawed one. A delayed vote is annoying; a result that gets overturned, or a bylaw breach on a contentious $1.9M assessment, is far worse.

Tell me what the portal can actually do (who sees what, whether it can separate identity from ballot), and I can help turn this into a short checklist or a message to Varrow.
