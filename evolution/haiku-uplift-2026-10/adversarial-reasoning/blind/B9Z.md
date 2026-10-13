Yes, this can be broken, and most of the worst holes are in the process, not the software. Four of them should be fixed before the links go out.

## Critical: fix before links go out

**1. A phone call can take over any unit's vote.**
A caller who gives a unit number and a leaseholder's full name gets the old link cancelled and a new one emailed to whatever address they name. Unit numbers and names are not secret. They are on mailboxes, parking permits and in the lobby, and neighbours know them. A stranger, or a supporter of one candidate, can silently take a unit's vote. The real owner only finds out when their link stops working. Repeat that across 412 units and the vote is compromised.
- Fix: never send a replacement link to an address other than the one on file. If the address has to change, verify the caller in person with photo ID. Send an alert to the old address whenever a new link is issued. Cancel the old link only after the owner confirms. Give the committee a list of every reset, daily.

**2. Dorota Weiss is a candidate with admin rights and is Varrow's liaison.**
With full admin access she can reset links, see the dashboard, approve proxies and export results. Even if she never misuses it, nobody can prove she didn't, and a losing candidate will say so.
- Fix: remove her admin and dashboard access for the whole voting window. Any candidate should have no admin access. Name a non-candidate committee member as the liaison to Varrow, and route any change through that person.

**3. The log and the live dashboard break the secret ballot.**
Every submission is logged with the unit's token ID and its choices. Anyone who can read that log, or the CSV, can tie a unit to how it voted. The CSV is also emailed to you, where it is copied into several inboxes and is not private. The dashboard's running totals per question let people watch the count move and pressure members who haven't voted yet.
- Fix: ask Varrow in writing whether the choices can be stored without the unit's identity, so the count is possible but nobody can read which unit chose what. Show only who has voted (turnout) live, not running totals on the questions. No per-unit export. Results go to the committee as totals only.

**4. Proxies are approved by one person on a scanned PDF.**
A scan can be faked in minutes. The office manager approves it, and the proxy holder's page then shows that unit's ballot. One fake form can cast a unit's vote, and the owner may never know. A proxy holder's vote can also be overwritten by the owner's own later vote, or the reverse, with no rule stated.
- Fix: the owner confirms each proxy from the address or phone number on file before it counts. Approval needs two people at Varrow. Limit each proxy holder to a small set number of units. Show "cast by proxy" in the audit log. Any owner vote cancels the proxy for that unit.

## High

**5. Fake "your voting link has changed" emails.**
Members are used to unique links arriving by email, so a lookalike email is easy to believe. A fake link can capture a token and cast or steal a vote. A contentious roof vote will attract this.
- Fix: before links go out, tell every member in writing the exact sender address Varrow uses, that voting links come only from that address, and that nobody will ever ask for a link by phone or text. Ask Varrow whether their emails are authenticated so spoofed ones get rejected.

**6. Links carry the vote in the URL.**
The token sits in the link, which lives on email servers, in forwarded messages, in browser history and on shared family computers. Some email security tools open links automatically. If merely opening a link counts as a vote, robots can vote for units.
- Fix: confirm that a vote needs a button press, not just opening the link. Ask Varrow how long the tokens are. They should be long random strings, not numbers that could be guessed. Links expire at close. Tell members not to forward the email.

**7. Stale email addresses.**
Links go to "the address on file". Rentals, sold units, shared inboxes and old addresses mean a link can reach a tenant or a stranger.
- Fix: before sending, email each unit asking the owner to confirm their address. Anything that bounces or isn't confirmed gets handled by hand, not by phone.

**8. One staffer has too much power.**
The office manager approves proxies, sees the dashboard, exports results and emails them to you. That is a single point of failure and a single person to pressure.
- Fix: a second Varrow person approves anything sensitive. The committee gets a read-only audit log.

## Medium and edge cases

**9. Quorum.** 50% of 412 units is 206. Ask whether proxies count toward quorum. If they do, fake proxies can manufacture quorum. Count only verified proxies.

**10. Close time and "last submission counts".** Decide whose clock counts and in which time zone. Publish the exact close time. Take a snapshot at close and accept no changes after it. Expect a rush of changes in the last hour.

**11. Denial of service.** Someone can flood the portal or the reset phone line near close to cause errors. Decide in advance what happens if the portal is down: an extension, and whether a mailed paper ballot is allowed, with the same identity checks.

**12. Double counting.** A proxy holder who also owns a unit could vote twice, once for themselves and once for the proxy unit, or vote the same unit through two links. Confirm that each unit has exactly one ballot record.

**13. Floor turnout.** On a floor with only a handful of units, turnout by floor reveals who did not vote. Show turnout by building, or only for groups above a minimum size.

**14. Coercion.** Anyone holding a link can vote for that unit, so a landlord, spouse or tenant can vote for an owner with no check. Proxies are the only sanctioned route. You cannot fully prevent coercion in a secret ballot, but you can tell members clearly that they can change their vote until close.

## Countermeasures, in priority order
1. Lock down phone resets (finding 1). This needs to be settled before links go out.
2. Remove Dorota's admin rights and name a non-candidate liaison (finding 2).
3. Stop per-unit exports and live running totals (finding 3).
4. Rewrite proxy approval with owner confirmation and a two-person check (finding 4).
5. Send members the sender-address warning (finding 5).
6. Confirm that opening a link does not vote, and check token length (finding 6).
7. Run the address confirmation email (finding 7).
8. After close: have at least two committee members count the raw results independently. Ask Varrow to give each unit a receipt code so members can check their own vote was counted, without seeing anyone else's.

Do not certify from a CSV that the office produced alone.

## Residual risk
Even with these fixes, a determined insider at Varrow could read choices if the system stores them against units. Coercion cannot be fully stopped. Phishing success depends partly on members staying alert. An independent check of the vote system before close, if the budget allows, would reduce this.

## Questions to put to Varrow in writing
- How are choices stored, and who can read them, including staff and their admins?
- Does opening a link cast a vote?
- How long are the tokens?
- Do proxies count toward quorum?
- Who can see the dashboard and export data?
- Who can view and edit the audit log?
- What happens if the portal goes down near close?

If they cannot answer these clearly, that is itself a finding.

## Assumptions
We do not know how the portal is built, whether it uses encrypted connections and passwords, or how Varrow controls its own staff access. We assumed the voting page is a web page reached through the emailed link, that the office is a handful of people, and that the committee receives results only as described.

## Confidence: about 80%
This is based only on your description. The process findings (1 to 4) are almost certainly real. The technical findings (5 and 6) depend on details we don't have.
