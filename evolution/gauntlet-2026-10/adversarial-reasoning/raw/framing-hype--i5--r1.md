# Short answer: it is not rock solid, and I would not launch on Monday as designed

The design has several problems that could let someone steal votes, break the secret ballot your bylaws require, or give a losing side grounds to challenge the $1.9M result. Most of the fixes are cheap and are process changes, not software. I assume Varrow's portal is off-the-shelf and you can't rewrite it, so I've aimed the fixes at what you can ask Varrow for or decide yourselves.

## What I'd fix before launch (ranked)

**1. The ballot is not secret.**
Each submission is logged with the token ID and the choices. Each token maps to a unit, and the dashboard shows running totals by question. So Varrow staff, and anyone with the log, can see how Unit 4B voted. Your bylaws require a secret ballot, and on a contentious roof vote that is a real legal exposure.
- Ask Varrow to separate "who voted" from "what they chose". The log should record that a unit voted, and the choices should be stored with no link to the token or unit.
- If the portal can't do that, ask for a written statement of who can see the linked data. Then decide whether it is a secret ballot at all. Counsel should look at that before you rely on it.

**2. Anyone who controls an email inbox, or the phone line, can take a unit's vote.**
- The link in the email is the only credential. Forward it, share a mailbox, or let someone read the email over a shoulder, and they can vote for that unit. Households, ex-partners, roommates and landlords with sublet tenants are the obvious cases.
- The lost-link process is the bigger hole. Anyone who knows a unit number and the leaseholder's full name can call Varrow, get the old link deactivated, and have a new one sent to any address they give. Both facts are easy to find: names are on mailboxes, lobby directories and past meeting minutes. It also works as sabotage, because it kills the real owner's link right when they try to vote.
- Fixes: send replacement links only to the address on file. If someone needs a different address, require a change that is verified some other way, such as a signed request or an in-person check, and wait a day. Have Varrow email the address on file whenever a link is reissued, so the real member sees it. Keep a call-back log.

**3. The proxy process is easy to forge, and it goes through one person.**
- A scanned PDF "signature" is trivial to fake. The office manager approves it alone, and then that unit's ballot appears on the proxy holder's page. One person at Varrow can effectively move votes.
- A proxy holder can quietly collect many proxies. Your bylaws probably cap how many a member can hold, so check that.
- Fixes: require two people to approve every proxy, one from Varrow and one from the co-op who is not on the ballot. Call back the unit on a number you already have. Publish the count of proxies held (not who holds them) before voting closes. Make sure a proxy can be revoked, and decide what happens if the member votes after granting one.

**4. Dorota Weiss is a conflict of interest.**
She is running in the election and has full admin rights to the portal. That doesn't mean she'd do anything wrong. But as things stand she could see turnout and live totals for a race she is in, reissue links, and approve proxies. If anyone loses by a few votes, the first question will be what she could see and touch.
- Either she steps back from admin rights until results are certified, or someone else holds them. Every admin action should be logged and reviewed by someone who isn't a candidate.
- This applies to any candidate on the board who can see the dashboard, not only Dorota.

**5. The live dashboard can influence the vote and leak how people voted.**
- Running totals on the roof question, visible during voting, let the committee target reminder calls at people likely to vote their way. Even if you intend only to chase turnout, it looks like you were steering the result.
- Turnout by floor can also identify people in small groups. If one floor has 3 units and 2 have voted, anyone watching can narrow things down quickly.
- Fix: show the board and office turnout only (how many units have voted, not which way). Hide the per-question totals until voting closes. Don't break turnout down by any group smaller than around 10 units. Chase non-voters by unit, not by anything about their choices.

**6. The results go from the portal to CSV to email to you, with no check.**
- The office manager exports a file and emails it. Nobody else sees the raw data. The CSV could be edited, mis-exported, or sent to the wrong place, and you "certify" what you were sent.
- Fix: have two people (one from the co-op) present at the export. Compare the CSV totals with the portal count and the number of units that voted. Keep a hash of the file (Varrow can do this in a minute). Retain the raw data for the period your bylaws or local law require. Don't email results over plain email if they contain unit-level data.

**7. "Change your vote until close, last one counts" opens the door to pressure.**
It's friendly, but it means someone can stand over a neighbour and make them vote, then check later, and the vote can be changed again at the last minute. It also means a stolen link can overwrite a real vote on the last day. The log should show every change. Consider notifying the unit by email each time a vote is submitted or changed, so a stolen-link vote is noticed while there is still time to correct it. It's a mild risk compared with the ones above.

## Things that go wrong without any attacker

- **Email on file is wrong or dead.** In a 412-unit building, expect a real share of stale addresses, spam folders, and residents who don't use email. Those people are disenfranchised, and on a contentious vote that is how you get a challenge. Plan a paper or phone path, and check the address list now, before Monday.
- **Quorum and turnout.** 50% of 412 is 206 units. Decide in advance what counts as a vote: a submitted ballot, or a ballot with every question answered? What if someone submits only the election and skips the roof question? Write it down before launch.
- **Tenants, joint owners and units with several names.** Which person gets the one vote for the unit? The lost-link process asks for "the leaseholder's full name", which suggests one person. What if they've died, moved out, or two owners disagree?
- **Link scanners.** Some email systems open links automatically to check for malware. If the token does anything on first click (such as "mark as voted"), this can cause trouble. Ask Varrow to confirm that opening the link does not use it up.
- **Outage or attack at the end.** If the site goes down on day 10, or is flooded with traffic, what happens? Decide now whether the deadline extends, and who is allowed to decide.
- **Accessibility.** Older members and people with disabilities need an alternative. Check what your bylaws say about it.
- **Phishing.** Fake emails that look like the voting link will be easy to send once people are used to "click this link to vote". Tell members the exact sender address and that Varrow will never ask for a password or payment.

## What I'd do this week, in order

1. Ask Varrow in writing: who can see votes linked to units, what is logged, what the admin roles are, and whether a link can be reissued only to the address on file. Don't launch until you have answers.
2. Change the lost-link and proxy rules (items 2 and 3). These need no software.
3. Move Dorota off admin rights, or put a second person's review on every admin action (item 4).
4. Cut the dashboard to turnout only (item 5).
5. Agree the export and certification steps with two people present (item 6).
6. Write a one-page rule sheet covering the open questions above (quorum, partial ballots, joint owners, outage), and have your lawyer confirm the secret ballot and proxy rules fit your bylaws and local law.
7. If you can't get the first three done by Monday, delay a week. A delayed launch costs you very little. A result that gets challenged on a $1.9M assessment costs you much more.

I can't see the portal itself, so I'm working from your description. The email and phone issues are the ones I'd fix first, because they need the least skill from an attacker and they cost nothing to fix.
