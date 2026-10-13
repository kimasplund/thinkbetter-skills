# Blunt verdict: do not send links Monday as designed

As described, this setup does not deliver a secret ballot, and it has several cheap ways to steal or swing votes. Given that the roof vote is contentious ($1.9M, about $4,600 per unit) and an admin is on the ballot, someone has a motive. Some of the fixes below are policy changes you can make this week with no IT skills. A few need Varrow to change the software, and if they can't, delay the vote by a week or two rather than run it as is.

I'm assuming Varrow runs the portal and holds the data, and that the 10-day window and the quorum rule are in your bylaws. Check the proxy and secret-ballot points against the bylaws and your province's or state's co-op act, because they may be legal requirements and not just good practice.

## The five worst problems, in order

### 1. The ballot is not secret (critical)

Every submission is logged with the token ID and the choices. Each token maps to a unit, and Varrow emailed it. So Varrow staff, anyone with admin rights (including Dorota), and anyone who gets the log or the CSV can see how unit 7C voted. The live dashboard adds to this. Running totals by floor, refreshed all through the vote, let anyone watching see exactly who just voted and which way the total moved. On a small floor with a handful of units, that identifies individual votes. Because members can change their vote, a log of revisions also shows who flipped and when.

Fixes:
- Stop recording choices next to identity. Record only "unit X voted at time T" in one list, and keep the ballots in a separate list with no token ID and no unit. Ask Varrow in writing whether the system can do this. If it can't, it can't give you a secret ballot, and you need a different system or paper.
- Remove the running totals for each question from the dashboard. Show only the number of units that have voted, in total. Drop the floor breakdown, or show it only where a floor has more than about 20 units. Results are released only at close.
- Written confirmation that nobody, including admins, can view individual choices.

### 2. "Lost your link" is the easiest way to steal a vote (critical)

The phone check is a unit number plus the leaseholder's full name. Both are on notice boards, in minutes, in AGM packages and on mailboxes. A neighbour, a relative, an ex-partner or a campaigner can call, say they are the leaseholder, and ask for the new link to go to any address they give. The old link is deactivated, so the real member then finds their link dead. They either don't notice (lost vote) or call, and now there is a dispute about which submission is real. Doing this against 20 or 30 units known to oppose the roof assessment could swing a close vote. Staff can also be pressured or bribed, and nobody sees the calls.

Fixes:
- Send replacement links only to the address on file. If the member has a new address, they change it in person or in writing with ID, before voting opens.
- Keep a written log of every replacement: date, who called, who approved. The election committee reviews it daily.
- Email the address on file whenever a link is replaced ("Your voting link was replaced. If this wasn't you, call this number"), and send a notice to the unit's mailbox as well.
- Offer an in-person replacement at the office with photo ID.
- Set a cap, e.g. one replacement per unit without committee sign-off.

### 3. Proxies are the biggest quiet hole (critical)

A scanned PDF of a signed form uploaded in the portal, approved by one person at Varrow. Problems:
- Anyone can forge a signature on a PDF, and the office manager can't verify it.
- The person uploading may not be the unit owner. Who checks?
- Once approved, the unit's ballot moves to the holder's page. Does the unit lose its own link? Can the unit still vote itself? Can both vote? Which wins?
- A holder can collect many proxies. A canvasser could gather 30, 50 or 80 proxies and control a large part of the vote, with no cap. For the roof vote, that is the whole election.
- The proxy holder sees the unit's ballot on their page, so there is no secrecy between the member and the holder.
- Nothing says the proxy is for this vote, or whether it says how to vote.
- One person, the office manager, approves everything, and nobody checks the approver.

Fixes:
- Check the bylaws: the form, the cap per holder (many co-ops allow 1 to 3), whether the proxy must be specific to this meeting, and the deadline.
- Proxy forms are due before voting opens, not during it. Set a deadline, e.g. 3 days before.
- Two people check each proxy against the signature on file: the office manager plus a committee member who is not a candidate.
- Publish (to the committee, not to members) the list of proxies per holder, and flag any holder with more than your cap.
- A proxy ends if the member votes in person or online themselves, or you rule that it does not. Pick one rule and tell everyone.
- Tell the unit by mail when its proxy is approved.

### 4. A candidate has full admin rights (critical)

Dorota is running for re-election and has full portal admin. This is a conflict of interest whatever her intentions, and it looks bad even if she is honest. Admin rights could let her see live results and who hasn't voted (she can target reminders to supporters), approve proxies, reset links, view the log, or change the settings. If the result is close, her opponent will say the election was rigged, and you won't be able to prove otherwise unless the logs show it.

Fixes:
- Remove her admin rights for the election period, or reduce them to read-only turnout (see point 1). Give the liaison role to a board member who isn't on the ballot.
- If nobody else is available, have Varrow run the admin side and give the committee the audit trail.
- The same applies to every other candidate, and to anyone who is a Varrow employee and a member, or related to a candidate.
- Ask Varrow for a list of everyone with admin access today, and what each person can do. Remove everyone who doesn't need it.
- Whoever certifies the result should not be a candidate.

### 5. Results come out by CSV email, and the office manager controls everything (high)

The office manager approves proxies, sees the dashboard, holds the results, exports the CSV, and emails it. One person can alter a spreadsheet before sending it, and the committee can't tell. Email is not a secure channel, and CSV files get forwarded. You then certify what you were sent, with no independent check.

Fixes:
- The committee should get the counts straight from the system at close, with two committee members present, not forwarded by email. Take the totals yourselves.
- Reconcile: number of units that voted, plus proxies, equals number of ballots in the count. Any mismatch is investigated before certifying.
- Keep the raw export and a hash of it (Varrow can generate one), and store it for the period your bylaws require.
- Ask Varrow for an independent audit log of admin actions (who changed what, when), and request a copy at close.

## Other serious problems

- **Link in a URL is a bearer token.** Whoever has the email has the vote. Forwarded emails, shared family mailboxes, compromised email accounts, and emails on a shared computer all give access. URLs also land in browser history, and in the logs of email services. Fix: send the link by email and also a short code by post or to the unit mailbox that the voter must enter; links expire after the vote closes; links work only once per session start.
- **Stale or wrong addresses.** "The address on file" for 412 units will have errors, former tenants and dead addresses. Someone receives a stranger's link. Fix: before Monday, send a notice to every unit to confirm or correct their address, and check bounced emails. Reach members with no email by paper or in person.
- **Members who can't use the portal.** Older residents, no email, language barriers. If they are shut out, a roof vote can be challenged as unfair. Offer a paper ballot or a supervised terminal at the office, counted into the same total, with the unit marked as voted so they can't vote twice.
- **Change-your-vote.** This is a good feature but it allows coercion and vote-buying (a campaigner stands over you until the end), and it lets a last-minute stolen link overwrite a legitimate vote on day 10. Fix: send an email to the unit's address each time a ballot is submitted or changed, so the real member can see and complain. Freeze lost-link replacements in the last 24 hours except in person.
- **Quorum.** 50% of 412 is 206 units. If turnout is low, the vote fails, or you are tempted to chase proxies to reach it. Decide now: do proxies count towards quorum? What happens if quorum isn't met by day 10 (extend, or re-run)? Also watch for people asking the office to "vote on behalf" of units that haven't voted.
- **Double-voting.** A unit with joint leaseholders, or a unit with a proxy and its own link, or a replaced link plus an old email. Test that one unit gives exactly one counted ballot in every one of those cases.
- **Joint owners and sublets.** Who may vote for unit 5B if two leaseholders disagree? The bylaws should say. Decide before opening.
- **Timing.** Opening a vote at midnight, closing at an unclear time, time zones in the export, and a server that's down at close. State the closing time and the time zone in the notice, and have a plan if the portal is down in the last hours (extend by a set time, announced by mail).
- **Phishing.** Sending links by email trains people to click links. A scammer sends a fake "Ostwick voting" email with a look-alike address to collect real links. Tell members in advance what the sender and domain will be, and that nobody will ever ask for their link by phone or reply.
- **Vendor risk.** Varrow is the single point of failure: they hold the data, they run the portal, and their staff can see everything. Ask for their written security answers: where the data is hosted, who has access, how long they keep logs, whether anyone has tested it, and what happens to the data after certification.
- **Accessibility and disputes.** Keep the logs and records until the challenge period under your bylaws has expired. If the roof vote is challenged, those logs are your defence, but only if they don't reveal how people voted (see point 1).
- **Dashboard misuse.** Reminder calls are useful, but calls aimed at "units that haven't voted yet" are a campaign tool for whoever has the list. Limit who can see the list of non-voters, and have the committee, not candidates, make the reminder calls, with a script that is the same for everyone.

## What to do before Monday

Must do, or don't open:
1. Take away candidate admin rights (Dorota, and any other candidate).
2. Change lost-link replacement to: send to address on file only, written log, notification to the unit.
3. Close the proxy rules: deadline before opening, cap per holder, two-person check, notification to the unit.
4. Get Varrow to confirm in writing that choices are not stored with identity, and that admins can't see them. If they can't, move to a delay or a paper ballot.
5. Strip the dashboard down to total turnout only.

Should do this week:
6. Address check and a paper/office voting option.
7. A written plan for the count: who is in the room, how totals are taken, the reconciliation, and how long records are kept.
8. Confirm quorum, joint owner, and proxy rules against the bylaws and your co-op act, and put the answers in writing in the notice to members.
9. Tell members how the vote works, who to call, and what the real emails will look like.

## What can't be fixed quickly

If Varrow's system genuinely can't separate identity from choices, the vote is not secret, and a contentious $1.9M assessment passed on that basis is open to a legal challenge. Your options are then a paper or in-person vote, or a different vendor, and a delay of one to three weeks is a much smaller cost than redoing a challenged vote. I would put that choice to the board in writing now.

## Confidence

I'm confident on points 1 to 4, because they follow directly from how you described the process. I'm less sure of the specifics of what Varrow's software can do and what your bylaws and local law say, since I haven't seen either, so verify those two things first. Even with every fix applied, you'll still rely on trusting Varrow to run the system honestly, so the audit trail and the in-room count are what let you show members the result is sound.
