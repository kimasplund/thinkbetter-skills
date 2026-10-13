Short version: as described, this setup cannot honestly be called a secret ballot, and on a contentious $1.9M vote it has several ways to be manipulated or challenged that need no hacking skill at all. I would not send links Monday unless the first four items below are fixed. Most fixes are process changes, not software.

I am working only from your description. I have not seen the portal itself, so some items are things to demand answers on from Varrow.

## Fix before Monday

**1. The ballot is not secret, and your own log proves it.**
Each submission is logged with the timestamp, token ID and choices. Varrow issues the tokens, so Varrow can map token to unit to person. Anyone with log access (Varrow staff, the portal admin, a contractor) can see how every unit voted. Bylaws require secrecy, so this alone gives a losing side grounds to challenge the result, and it exposes members to pressure from neighbors or the board.
- Ask Varrow whether the vote record can be stored without the link between voter and choice. The usual design is that the system records "unit 14B has voted" in one place and drops the choices into a separate pool with no unit or token attached.
- If the portal cannot do this, it is the wrong tool for a secret ballot. Consider a specialist election provider or paper mail-in ballots.
- Also note "change your vote until close, last counts" forces the system to know which earlier vote to replace. That is exactly what makes the link between person and choice persist. Allowing re-votes is a feature to give up, or to implement very carefully.

**2. The lost-link phone call is the easiest way to steal a vote.**
Staff check the unit number and the leaseholder's full name, then email a new link to whatever address the caller gives. Both facts are easy to find: names and units are on mailboxes, in the building, and often in minutes or notices. A neighbor, a landlord's agent or an organized faction could call, get a fresh link sent to their own email, and vote someone else's unit. The old link is deactivated, so the real owner then finds their link dead. Worse, if the real owner already voted, the thief's submission replaces it (last submission wins).
- Only send replacement links to the address already on file. If the member needs to change address, they must do it in person or with ID, before voting opens.
- Send an automatic notice to the address on file whenever a link is reissued.
- Keep a written log of every reissue: who called, who handled it, when. Review it daily.
- Make clear to Varrow staff that a pressured or tricked employee is the realistic threat here, not a hacker.

**3. The proxy process hands too much power to one person, and it breaks secrecy.**
- A scanned PDF "signature" is trivial to forge. The office manager approves it alone, with nothing to compare against.
- Once approved, the unit's ballot appears on the proxy holder's page. That holder can now see and cast that unit's vote, and a bad actor can collect many. Check your bylaws for any cap on proxies per person; if there is none, set one.
- Require proxies to be signed and dated, name the holder, and ideally say whether they cover one or both questions. Have two people compare the signature against the member's file. Notify the grantor at the address on file when a proxy is approved, and let them revoke it.
- Decide in advance what happens when the grantor also votes themselves, or if a proxy and a direct vote both arrive. The rule should be written down now, not improvised in a dispute.
- Proxy holders voting differently from the instructions given is a separate risk. A holder should not be able to see the grantor's token or prior choices.

**4. The live dashboard with running totals is dangerous on a contentious vote.**
Running totals by question for 10 days let anyone with access, including board members and Varrow staff, know whether the roof assessment is passing before it closes. That enables:
- Targeted pressure: "Floor 6 is against, let's visit them."
- Late tactics: holding back proxies or reissued links until the margin is known.
- Accusations of tampering whichever way it goes.
Turnout by floor is also a privacy problem in a small building: on a floor with few units, turnout plus a known neighbor's behavior reveals things.
- Show only the count of units that have voted overall, or the list of units that have not voted yet (that is what reminder calls need). Do not show running totals for any question. No one sees results until close.
- If you must show per-floor turnout, suppress any floor with fewer than about 10 units.

**5. Dorota Weiss has full admin rights and is a candidate.**
This is the problem you are most likely to get blamed for, whatever her intentions. She could (or will be accused of being able to) see live results, read the log, reissue links, approve proxies or edit records, while standing in the election. Even if she never touches anything, a candidate holding the keys makes the result challengeable.
- Remove her admin rights for the election period. Give her a read-only role limited to non-sensitive information, or nothing.
- The same applies to any other candidate or board member who is on the ballot.
- Admin access should belong to a person at Varrow who is not a candidate and not a member, and every admin action should be logged.

## High priority, can be fixed in the first days

**6. The office manager is a single point of failure for the whole election.** One person approves proxies, sees the dashboard, exports the results and emails them to you. Whoever that is (or whoever compromises that person's email) can change a CSV before you see it, and you would have no way of knowing. Fix: results should come from the system directly to two committee members, with the totals checked against the raw record by someone who did not produce the export. Do not certify from an emailed spreadsheet alone. At minimum, have a second person at Varrow plus two committee members present when results are pulled, and keep a copy of the file with a checksum recorded at that moment.

**7. Tokens in URLs leak.** A link containing the token can be forwarded, sits in email forever, shows up in browser history, and may be passed to other websites in the referrer. Questions to ask Varrow: does a link work only once? Does it expire at close? Does the vote page ask for anything else, such as unit number plus a code mailed on paper? Also, shared emails are a real problem: a household email account, or a landlord who manages email for several units, means one person can see and vote several links. Check how many units share an address. If an address appears on more than one unit, treat it as a flag.

**8. Email is a weak delivery channel.** Expect: links going to spam, wrong or stale addresses on file, and phishing. Once people know that the link arrives by email, a fake "Your Ostwick ballot link" email from outside is very likely, especially in a contentious vote. Tell members in advance exactly what the real email looks like, what sender address it comes from, and that neither the board nor Varrow will ever ask for a password or phone code. Offer a paper alternative to anyone who requests it. Many co-ops are legally required to anyway; check your bylaws and local law on whether electronic voting is permitted and whether members must opt in.

**9. Quorum and the vote itself.** 50% of 412 is 206 units. Decide now, in writing:
- Does a proxy count towards quorum? Does a reissued-link vote count the same?
- What happens if a unit is co-owned or has two leaseholders? Who may vote?
- What if someone votes both online and (if offered) on paper?
- Does a roof assessment need a simple majority of votes cast or a higher threshold of all units? Check bylaws and corporate law. A $1.9M special assessment is exactly what gets litigated, so a procedural defect is a ready-made reason to overturn it.

## Things that will go wrong without anyone attacking

- **Outage or slow service at the deadline.** If the portal goes down in the last hours, you will have unhappy members and a dispute. Decide in advance who can extend voting, and by how long, and write it down. Also ask who hosts the portal and whether there are backups.
- **Time zone and close time.** State the exact closing time, with time zone, in the notice and check that the server uses it.
- **Members without email or comfort with computers.** Older residents and non-English speakers will be less likely to vote or will ask others to do it for them. Plan help (an in-person session, phone assistance, paper) that does not break secrecy: a helper must not be someone who has an interest in the outcome.
- **Double clicks and re-submissions.** If a member submits twice, the log should show which counted. Test this.
- **Votes changed late by someone with the link.** Because the last submission wins, a forwarded or stolen link used in the final minutes is nearly impossible to undo or even detect.
- **Records retention.** Decide how long the log and the raw data are kept, who can see them, and when they are destroyed. Keep enough that you can answer a challenge.

## What I would do this week, in order

1. Call Varrow today and get written answers on: where the choices are stored relative to token and unit, who has database and log access, whether links are single-use, where replacement emails go, and how the CSV is produced.
2. Remove Dorota Weiss's admin rights, and any other candidate's, until results are certified.
3. Replace the dashboard with a "has voted / has not voted" list only.
4. Change the lost-link rule: reissue only to the address on file, with a notice and a written log.
5. Tighten proxies: second reviewer, notice to the grantor, a cap per holder, and a rule when both exist.
6. Agree the written rules in item 9, and brief the board on them before links go out.
7. Have two people who are not candidates observe the results export and certify against the system's own totals.
8. Run a dry test with five or six volunteers on dummy data before Monday: lost-link, proxy, re-vote, and check what the log and dashboard reveal.

If Varrow cannot deliver items 1 and 4 in time, I would postpone the launch by a week or two rather than run a flawed vote on a $1.9M assessment. A delay costs you an awkward email; a successfully challenged vote costs you the roof decision and a lot of trust.

I would also have a lawyer who knows co-op law spend an hour on your bylaws and the proxy and quorum rules before you start. That is cheap compared with what is at stake.

How sure am I: confident about the structural problems (items 1 to 5), because they follow directly from what you described. Less sure about what the portal actually does under the hood, so items 6 and 7 depend on Varrow's answers.
