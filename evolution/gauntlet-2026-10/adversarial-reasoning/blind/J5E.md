# Ostwick online vote: where it breaks

**Bottom line: do not send links Monday as designed.** The setup cannot deliver a secret ballot, and it lets one or two people at Varrow, or one candidate, change or take votes without anyone noticing. On a contentious $1.9M assessment, either problem could get the result challenged or overturned. Most fixes are procedural and can be done this week. A few need Varrow to change the portal, and if they can't, delay the launch.

Assumptions: the portal is a vendor product you can't inspect, and "token in the URL" means the link alone is the credential.

## The serious problems, worst first

**1. The ballot is not secret.**
Every submission is logged with token ID and choices, and Varrow knows which unit each token went to. Anyone with the log can see how each unit voted. The proxy design is worse: a proxy holder's page shows the grantor's ballot, and the dashboard shows running totals per question, so a vote can be traced by watching totals move.
- Your bylaws require a secret ballot. A court or a unit owner who loses can say the process breached them.
- Fix: log timestamp and token ID, but not choices, or store choices separately with no token link. Confirm with Varrow in writing exactly what is stored and who can read it. If the system can't separate identity from choice, you don't have a secret ballot. Consider a vendor that is built for this.

**2. Anyone with an email address and a phone can take over a unit's vote.**
The lost-link process needs only the unit number and the leaseholder's full name, both of which are semi-public (door lists, notices, neighbours). The new link goes to whatever address the caller gives. A person who wants to swing the roof vote can call, claim to be a leaseholder, and receive a live link. The old link is deactivated, so the real member is locked out until they notice. Because members can change their vote until close, an attacker can also overwrite a vote the member already cast.
- Fix: send replacement links only to the address on file. If the member's address has changed, require in-person ID at the office, or a call back to the number on file, and have a second person approve. Keep a log of every reissue and give the committee a daily list of reissued units. Notify the original address whenever a link is reissued.
- Also tell members that anyone who has their link can vote for them, so they shouldn't forward it.

**3. Varrow staff can vote for people, and no one could prove it.**
The office manager approves proxies, reissues links, sees live totals and exports and emails the final results. One person can issue a link to an address they control, vote it, or approve a fake proxy, then report the result they like. Nothing in your design lets the committee check the count independently. That's a concern even if Varrow is honest, because the contentious vote means someone will claim they aren't.
- Fix: have someone not at Varrow, such as two committee members or a neutral scrutineer, verify the outcome. Require two people for proxy approval and link reissue. Get Varrow to confirm in writing that its staff are barred from voting for units and from reading individual choices.

**4. Dorota Weiss is a candidate and holds full admin rights.**
She is running for re-election and can see live results while votes are still being cast, and probably can change settings, approve proxies, reissue links or alter data. Even if she never does, the conflict makes any close result for her or for the roof vote easy to attack.
- Fix: for the length of the election, take her admin rights down to read-only without results, or give the liaison role to someone not on the ballot. Review who else has admin rights, including Varrow staff and the vendor, and remove anyone who doesn't need them. Do it before Monday, and record that you did.

**5. Live running totals bias the vote and leak information.**
Board members and the office manager see turnout by floor and running totals per question. Seeing the roof vote trending lets insiders pressure floors, target reminder calls at people likely to vote their way, or decide to push proxies. Turnout by floor is also very small data: if a floor has a few units and two vote, people can infer how they voted.
- Fix: show turnout only (voted or not, by unit) and no per-question totals until close. Reminder calls then go to everyone who hasn't voted, with the same script. Drop per-floor breakdowns for small groups.

**6. Proxies are the easiest way to rig the quorum and the result.**
A scanned PDF signature is easy to forge, and the only check is one approver. A proxy holder can collect many proxies. Your design puts the grantor's ballot on the holder's page, so the holder controls it and can see what they were given. Nothing says whether a member who gave a proxy can still vote themselves, or whether a proxy is revocable.
- Fix: cap proxies per holder (check your bylaws and local law for a limit), require a second approver, check each against the signature on file, and send the grantor a confirmation at their address on file. State that a member's own vote overrides a proxy. Consider letting the proxy grantor mark the vote in the portal, not the holder.

**7. The results path is manual and unprotected.**
The office manager exports a CSV and emails it. Email is not secure, and a CSV can be edited before it's sent. You then certify what you were sent.
- Fix: the committee exports the file itself, or two committee members are present when the export is made. Record a checksum of the file at export and keep the raw log. Compare the CSV against the submission log and the member list: the count of votes should match the count of units that voted, with no duplicates and no unknown tokens.

## Smaller problems you should still handle

- **Links in email.** Anyone with access to a mailbox (shared inbox, family member, forwarded mail, a compromised account) can vote. Tokens in URLs also end up in browser history and some logs. Make sure links expire at close and can't be guessed (long random strings, not numbers). Ask Varrow.
- **Phishing.** A fake "Ostwick voting" email with a link to a lookalike site is easy to send. Tell members which sender address and web address are real, and that no one will ask for a password or payment.
- **Email addresses on file may be stale.** Some units will never get a link. Before Monday, check the list for bounced, blank or obviously wrong addresses, and have a paper or phone option for people without email, with the same identity checks.
- **Changing votes until close** is fine, but it means a last-minute takeover (see point 2) can't be recovered. Include a confirmation email to the address on file after every submission, so a member who didn't vote sees it.
- **Quorum and turnout.** Decide now how you count a proxy toward quorum, and what happens with a unit with several owners or a leaseholder who has changed. Write the answer down before voting starts, not after.
- **Outage or attack.** If the site goes down on the last day, what happens? Decide who can extend voting, by how long and how that is announced. A rule of "the committee may extend by up to 24 hours by unanimous decision, announced to all members" is better than improvising.
- **Disputes.** The roof vote is contentious, so expect a challenge. Keep the full log, the reissue list, proxy forms and the committee's decisions for as long as your counsel advises.
- **Your own bylaws and law.** Check that your bylaws and local co-operative rules allow electronic voting and online proxies. If they don't, the vote could be invalid regardless of how well it is run. Have your lawyer confirm before Monday.

## What to do before Monday

1. Ask Varrow in writing: what does the system store, who can read it, can choices be separated from identity, who has admin access, and what is audited.
2. Remove Dorota's admin rights for the election, or move the role to someone not on the ballot.
3. Change the lost-link rule: send only to the address on file, with a second approver and a log.
4. Hide per-question totals from everyone until close.
5. Put two approvers on proxies, with a cap per holder and a confirmation to the grantor.
6. Plan the count: two committee members or a neutral person run the export and check it against the log.
7. Check the email list and set up an alternative for members without email.
8. Have your lawyer confirm electronic voting and proxies are valid under your bylaws.

## If you can't fix the first three

If Varrow can't separate votes from voters, can't stop its staff from reading or changing votes, or won't give you an independent check on the count, delay the roof vote or run it by paper or a specialist election service. A delayed vote is annoying. A $1.9M assessment overturned in court after the roof work has started is far worse.

## What remains after these fixes

Some risk will remain. Anyone with a member's email access can still vote as them, and a determined insider at Varrow is hard to rule out completely. The aim is to make cheating need several people, leave a trail, and be caught by a check you control.
