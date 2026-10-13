Blunt answer: as described, this setup would not survive a contested $1.9M vote. Several flaws break the secret ballot or let one person swing the result unnoticed. Below are the problems in order of severity, then what to do before Monday. I'm assuming the portal is a vendor product run by Varrow and that you can't change the software, only the rules, permissions and procedures around it.

## Critical: fix before links go out

**1. The ballot is not secret.**
Every submission is logged with token ID and choices, and each token belongs to one unit. Anyone who can see the log can see how each unit voted. That includes Varrow staff, anyone with admin rights, and anyone who gets the CSV. Your bylaws require a secret ballot, so a challenger could argue the whole vote is invalid.
- The log must not link a person or unit to their choices. Log only "unit X voted at time T" in one place. Store the choices in a separate, unlinked ballot box.
- If the software can't do that, you can't call this a secret ballot. Tell the board now and consider a different method for the roof question: paper ballots, or a vendor built for member elections.
- "Last submission counts" makes this harder, since the system has to know which earlier ballot to replace. Ask the vendor how it does that without keeping the link.

**2. The lost-link process is an account-takeover process.**
Anyone who knows a unit number and the leaseholder's full name can phone Varrow and have a new link sent to any email address they give. Names and unit numbers are easy to find (notice boards, mailboxes, past minutes, neighbours). An attacker, or a keen campaigner, could request links for units they know won't vote, or for a neighbour they dislike. Deactivating the old link also means the real member is locked out until they notice.
- Send replacement links only to the address on file, or hand-deliver them to the unit.
- If the address has to change, require a written request in person or with ID, approved by two people, and logged.
- Notify the unit by its original address and by post whenever a link is reissued.
- Because ballots can be changed until close, a stolen link also lets someone overwrite a legitimate vote. The member would see nothing unless they check.

**3. Proxy approval is a single point of control and it breaks secrecy.**
- One person, the Varrow office manager, approves proxies from scanned PDFs. A forged signature is trivial to produce. Nobody on your side checks them.
- The proxy holder sees the granting unit's ballot on their page, so they see and control it. If the granting member had voted already, the holder may see how. A proxy holder can also overwrite the vote at any time, with no record of whether the grantor intended that.
- Proxy hoarding: nothing limits how many proxies one member can hold. In a contested vote, a campaigner could collect dozens.
- Fixes: check your bylaws for whether proxies are allowed at all for assessments and for elections. Cap proxies per holder. Have two people, including one committee member, verify each proxy against the signature on file. Publish the list of approved proxies (unit and holder only) to the committee. Let the grantor revoke it, and lock the ballot once the grantor votes. Consider requiring proxies to name the choice for each question, so the holder only transmits it.

**4. Dashboard with running totals lets people steer the vote and leaks secrets.**
Board members and the office manager see live totals per question, and turnout by floor. On a contested question, anyone who sees the roof vote trending can target reminder calls, delay or push proxies, or lean on holdouts. In a small floor, turnout and totals can reveal individuals ("floor 7 has two voters and both voted yes"). Board members who are candidates, or who have a stake in the roof vote, shouldn't see this.
- Show turnout only (who has voted, in aggregate by building), never running results, until close.
- Hide any breakdown with fewer than about 10 units.
- Reminder calls should work from a "has not voted" list of units, not from totals by question.

**5. Dorota Weiss has full admin rights and is a candidate.**
This is a conflict of interest regardless of her intentions. Full admin may let her see logs, edit proxies, reissue links, change results or export data. Even if she never does anything, a loser can claim she could have, and you couldn't prove otherwise.
- Remove her admin rights for the election period or reduce them to a read-only liaison role with no access to ballots, proxies or links.
- Turn on audit logging of all admin actions and have someone other than her review it.
- Apply the same to any other candidate or interested board member.
- Ask Varrow which of their own staff have admin access, and apply the same logic. Varrow also has an interest if the roof contract involves the management company or a contractor they use.

**6. The results path has no integrity check.**
The office manager exports a CSV and emails it to you, and you certify. Email can be altered, and there's no independent count. The person who approves proxies and can see running totals is also the person who produces the final numbers.
- Have two people, one from the committee, run the export together, or have the committee export directly.
- Compare the export against independent counts: number of units that voted, number of proxies, number of reissued links. Totals should reconcile exactly.
- Get a hash (checksum) of the file recorded at export, transmit it by a separate channel, and keep the raw log.
- Keep the data for the period your bylaws or local law require, in case of a challenge.

## Serious but secondary

**7. Email as the only delivery channel.** Emails go to the address on file. Stale addresses, shared accounts and spam filters will lock out members, which in a 412-unit co-op is a real risk to quorum. Anyone with access to a member's inbox, including a family member or a former tenant, can vote. Links forwarded to others work for whoever clicks first. Check the address list now, correct it, and offer paper or in-person voting for those without email. Note that a token in a URL can also leak via email forwarding, browser history and shared computers. Ask whether tokens expire, are single-session, and whether the link can be used from two devices at once.

**8. Eligibility and "one vote per unit."** Who is allowed to vote for a unit with multiple owners, a deceased member, or arrears? The lost-link check relies on the "leaseholder's full name", so joint leaseholders and sublets are ambiguous. Decide the rule in advance, in writing, and apply it equally. Check that bylaws on special assessments don't require a higher threshold than a simple majority (many require two-thirds or a quorum of members present, not of units).

**9. Quorum and the ten-day window with edits.** Quorum is 50% of units, so 206 votes. Because votes can change until close, a late flood can flip the result and leave no time for objections. Decide in advance how you will handle: a tie, a result within a handful of votes, and a quorum missed by a few. A $1.9M assessment passing by a few votes with questionable proxies will be litigated.

**10. Software and vendor security you can't see.** Ask Varrow in writing:
- Who built the portal, where is data stored, and is it backed up?
- Is the connection encrypted, are tokens long and random (not sequential or guessable, like unit number plus date), do they expire?
- Is there rate limiting so someone can't guess tokens?
- Has anyone tested it? Can they run a mock election before Monday?
- Who can see the database, and how is access logged?
If the answers are vague, treat that as a "no".

**11. Disputes and recovery.** Nothing in your description says what happens if someone claims they didn't vote, or that their vote changed. Members should get a confirmation email after each submission (without revealing the choice) so they can spot tampering. You also need a written process for complaints, a named neutral person to hear them, and a way to void and rerun if the system fails.

## What I'd do this week, in order

1. Decide whether the software can deliver a secret ballot. If not, move the roof question to paper or a proper election vendor. This is the biggest risk to the legitimacy of the vote.
2. Remove or restrict Dorota's admin rights and anyone else with a stake. Turn on audit logging.
3. Close the lost-link hole: reissue only to the address on file or in person.
4. Change the dashboard to turnout only, no running results.
5. Tighten proxies: cap, double verification, publish list, lock on vote.
6. Run a short test election with committee members and Varrow staff, including a lost-link request, a proxy, an edit, and an export.
7. Write down the rules (eligibility, proxy limits, tie handling, complaints) and send them to members with the links.
8. If you can't do all this by Monday, delay the launch. A one-week delay is cheap compared with a $1.9M vote that gets overturned.

Also consider having a lawyer or your bylaws' interpretation source confirm that online voting, proxies and the assessment threshold comply with your bylaws and local co-op law. I can't confirm that from here.

I can draft the written rules, the questions for Varrow, or a one-page notice for members if that would help.
