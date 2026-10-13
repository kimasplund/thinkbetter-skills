# Ostwick online vote: where it breaks

**Blunt verdict: do not send links Monday as designed.** Several problems are not technical bugs. They are design choices that make the vote impossible to certify as secret or as clean, on a contentious $1.9M question. Most fixes are procedural and cheap, and you can do them this week. If a few can't be done by Monday, delay the launch. A short delay costs far less than a challenged result.

I'm assuming the portal is a Varrow-run or third-party product you can't modify yourselves, and that "token ID" in the logs can be traced back to a unit. Check both assumptions with Varrow in writing.

## The five things most likely to hurt you

### 1. The ballot is not secret (bylaw breach, likely invalidates the result)

Each submission is logged with timestamp, token ID and choices. Each token belongs to a unit. So anyone with log access can see how every unit voted. Add the dashboard (running totals per question) and the proxy page, which shows one member another unit's ballot, and secrecy is gone in several places.

Who can see it: the office manager, Varrow IT staff, the portal vendor, and Dorota as admin. In a 412-unit building where the roof assessment divides people, "management can find out how I voted" is a coercion and retaliation risk. It is also a straightforward bylaw violation that any losing side can use to challenge the result.

Fixes:
- Ask Varrow whether the vote record can be separated from the voter record. The usual design is to keep a list of who has voted, with no choices, and a separate anonymous ballot box with no unit or token link. If the portal can't do that, it is the wrong tool for a secret-ballot vote.
- Failing that, get written confirmation of exactly who can read choice-level logs, have those people's access removed or sealed, and have the committee, not Varrow, hold the only copy.
- Ask for the answer in writing before Monday. If the answer is "the system can't separate them," postpone and use a vendor built for association elections.

### 2. The "lost link" phone process lets anyone take over a unit's vote

Staff verify two facts: unit number and the leaseholder's full name. Both are easy to learn. Names are on mailboxes, in directories and in past meeting minutes. Then staff email the new link to whatever address the caller gives. So the attack is one phone call: "I'm Maria Costa in 7B, I lost my link, send it to maria.costa.7b@example.com." The old link is deactivated, so the real owner is also locked out and may not notice until they try to vote, or may find that "their" vote has already been cast.

Who would do this: a neighbour who wants the roof assessment to fail, or pass; a relative or ex-partner; a canvasser working through the list of units that haven't voted. The dashboard even tells them which units haven't voted. Because members can change their vote until close, an attacker can also overwrite a vote that was cast legitimately, simply by getting a fresh link to a voted unit.

Fixes:
- Re-issue only to the address already on file. No exceptions on the phone. If the address is wrong, the member comes in person with ID, or the committee handles it.
- Send a notice to the address on file, and a letter or door notice, every time a link is replaced ("a replacement link was issued for your unit; if this wasn't you, call X").
- Keep a log of all replacements and have the committee review it daily. A spike in replacements is an alarm.
- Do not let replacement happen after a vote has been cast without a committee member's sign-off.

### 3. Proxies are a way to stuff or buy ballots, and the office manager is the only check

A scanned PDF of a signed form is easy to forge: copy a signature from any document the neighbour has seen, or make one up. The only gate is the Varrow office manager, who probably can't tell. Once approved, the proxy holder sees that unit's ballot on their page and can vote it, and can change it freely until close. Other problems:
- Nothing says how many proxies one person can hold. One person collecting 40 proxies is a bloc, and on a contentious vote that is how it would be done.
- The proxy holder sees the grantor's ballot, which breaks secrecy again (and shows whether the grantor had already voted, and how).
- A member can sign a proxy, then vote themselves, and nobody has defined which wins.
- Proxies can be pressured out of older or vulnerable residents ("just sign this for me").
- Check your bylaws and your provincial or state co-op legislation: many restrict proxies, require specific wording, or require them to be filed before the meeting or a set time before voting opens. Some require a vote-by-vote instruction.

Fixes:
- Set a cap (for example 2 or 3 per holder, or whatever your bylaws say) and enforce it.
- Verify each proxy by contacting the grantor directly at the contact on file, by phone or in person, and record that you did.
- Publish the list of approved proxies (holder and grantor unit, not the instruction) to the committee.
- Decide that a member's own vote always overrides a proxy, and tell the portal vendor.
- Proxy holders should vote the grantor's ballot without seeing any earlier vote. Better still, have the grantor's instruction recorded on the form.

### 4. The people running the vote can see live results, and one of them is a candidate

The dashboard shows running totals for each question to board members and the office manager, during the vote. That is a problem on its own: the people reminding members to vote can target reminder calls to the people who are likely to vote their way, and drop the others. On a 10-day contentious vote that is influence over the outcome, and it looks like it even if nobody does it. It also lets someone time a push, such as late proxy collection or link takeovers (see 2), for the margin they need.

Dorota Weiss has full admin rights and is on the ballot. Whether or not she would ever misuse them, she is in a position to read choices, issue links, approve things, and see totals while a candidate. If she loses by a few votes, she will have to defend that she never touched anything, and she can't. If she wins narrowly, the other side will say she could have.

Fixes:
- Turn off per-question running totals for everyone until close. Show turnout only (number of units voted, by floor if you must, never per question). Turnout by floor is itself a mild privacy leak if a floor has few units. Group to wings or the whole building if small.
- Remove Dorota's admin rights for the whole election period, or have a non-candidate committee member act as liaison. Do this before Monday and announce it. It protects her as much as anyone.
- Give each admin a separate named login, not shared, and turn on logging of admin actions (who issued links, approved proxies, viewed logs).
- No candidate and no person with a side on the roof vote should have any tool that issues, resets or views links.

### 5. Results come out of Varrow's hands, unverified, as a CSV in an email

At close, the office manager exports a CSV and emails it to you, and you certify. Email is not secure or tamper-proof. The office manager (an employee of the firm that manages the building and presumably has an interest in the roof project) can edit the file between export and sending, and you have no way to compare. Your certification would then be signing off on a number you can't check. Quorum is another weak spot: if "50% of units" is calculated from submissions, then duplicates, replaced links and proxy-held ballots all affect it.

Fixes:
- Have two committee members present when results are exported, on screen, or run it on a call. Screenshot totals before the export and compare them to the file.
- Get the final tallies from the portal's own screen, not only the file, and have the file hashed or sent to more than one committee member at the same moment.
- Publish the counts: total units, units voted, votes for each choice, proxies used, links reissued. Agree beforehand how quorum is calculated, including whether a proxy counts as attendance.
- Keep the raw log for the dispute period, in a place Varrow can't alter.

## Other holes worth fixing before Monday

**Phishing and link theft.** The token in the URL is the whole credential. Anyone who gets the email can vote. Risks: shared family or roommate email accounts; forwarded emails; links that sit in an inbox visible to a landlord or subtenant; the link staying in browser history on a shared computer; the URL leaking to the portal's analytics or to anything linked from the page. Mitigation: tell members to treat the email like a ballot paper, not to forward it, and to be wary of any look-alike emails. A fake "your voting link has changed, click here" email is an easy scam in this setup, so tell everyone exactly what the real email looks like and that the committee will never send a replacement by anything other than the process above.

**No check that the email address on file is right.** Check it now. Out-of-date addresses (a former tenant, a deceased member, a unit sublet) mean links go to the wrong person. Pull the list, compare it to the member register, and call or door-knock where it bounces.

**"One vote per unit" with several owners or leaseholders.** If a unit has two names on the lease, who votes? Both getting links is a risk, and a dispute inside a household can end with two people trying to overwrite each other's votes. Decide in advance who the voting member is for joint units, and check that against your bylaws.

**Members who can't use the portal.** Older members, people without email, and people with accessibility needs. If they can't vote, or someone "helps" them, you get disenfranchisement complaints on one side and undue influence on the other. Offer a paper or in-person alternative with a committee member, and put the count of paper ballots into the same tally.

**Eligibility.** Are units in arrears, or sublet units, allowed to vote under your bylaws? Check the list before links go out; it's hard to fix afterwards.

**The "last submission counts" rule.** It is friendly, but it also gives an attacker or a coercive person a second chance: someone can stand over a neighbour while they vote, and then re-vote after. The reverse also holds, an attacker who has taken over a link (see 2) can overwrite on day 10, after the real owner has stopped checking. Mitigation: send a confirmation email to the address on file for every submission and every change, with no choices in it, and have a lock on changes in the last hours, or at least a flag for committee review of any unit that changed its vote in the last 24 hours.

**Day-10 timing and outages.** What happens if the portal goes down on the last day, or is slow? Define in advance whether the vote can be extended, who decides, and how members are told. Check the time zone of the close time and say it in the notice, in writing, with the date and hour.

**Vote buying and pressure.** Unavoidable online, but the roof assessment is $1.9M across 412 units (about $4,600 per unit on average). That is enough for neighbours to pressure each other and for someone to offer money for links. Say in the notice that links are personal and selling or sharing them is grounds for a disqualified ballot, if your bylaws support this.

**Audit trail goes both ways.** Logs with token ID and choices are useful for investigating fraud, but they are exactly what creates the secrecy problem in 1. Keep an audit log of actions (link issued, vote received, proxy approved, who did it) without choices attached.

## What I'd do this week, in order

1. Ask Varrow in writing: can ballot choices be separated from voter identity, who can read the logs, and can per-question live totals be turned off? (Today)
2. Change the lost-link rule: re-issue only to the address on file, notify the member, log every replacement. (Today)
3. Remove Dorota's admin rights, or give the liaison job to someone who is not a candidate. Turn off running totals for everyone. (Before Monday)
4. Fix the proxy rules: cap, verification by calling the grantor, own vote overrides proxy, no holder sees the grantor's earlier ballot. Check the bylaws and local law on proxies. (Before Monday)
5. Settle the results process: two committee members present at export, tallies compared, counts published, quorum defined. (Before Monday)
6. Clean the email list against the member register, and send a plain-language notice explaining how to spot the real email and what to do if it doesn't arrive. (Before Monday)
7. Offer a paper or in-person option. (Before Monday)

If items 1 and 3 can't be settled by Monday, move the launch back. A one-week delay, announced calmly, is far better than a result that gets challenged on a $1.9M assessment.

## What remains risky even after all this

Online voting through a management company can never be fully secret or fully verifiable. Someone with enough access (Varrow staff, the vendor) could still change records, and you can't prove they didn't. You can reduce the chance and make it detectable, but if the roof vote is likely to end up in a dispute or in court, consider hiring an independent election service for this vote, or having an independent person (a lawyer, an accountant, or a neutral scrutineer) oversee the count. It's usually a few hundred dollars and is cheap next to a re-run.

My confidence is high on items 1 to 4, which follow directly from what you described. It is lower on how Varrow's portal is actually built, because I've only your description. The answers to question 1 will change how serious some of these are.

I'm not a lawyer. Have your co-op's lawyer check the bylaws and local co-op law on secret ballots, proxies and electronic voting before you certify.
