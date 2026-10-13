Yes. Here is how I would attack it, most dangerous first. I am working only from your description, so I have not seen Varrow's system. Where I assume something, I say so.

## The phone helpdesk can steal any unit's vote (fix before Monday)

Staff confirm only a unit number and a full name, then deactivate the old link and email a new one to any address the caller gives. Both facts are easy to get: unit numbers are known to neighbours and delivery drivers, and names are on mailboxes, doorbells, and old meeting minutes. An attacker calls, gives a name and unit, and sends the new link to their own inbox. The real owner's link stops working and they may not notice. Across 412 units, one person could take over many votes in a day.

Fix: never send a new link to an address that was not already on file. Send it to the address on file, and tell the old address that a new link was issued. Better still, require a verified photo ID in person or a callback to a phone number already on file.

## Anyone holding a link can vote, and nobody can tell who it was

A token in an emailed URL is the only login. If the link is forwarded, sits in a shared inbox, or is seen on a shared screen, whoever has it can vote. Tokens in URLs also end up in browser history and mail server logs. Ask Varrow how long the tokens are, how they are generated, and whether they are stored hashed or in plain text. Short or guessable tokens are a serious problem.

## The log breaks the secret ballot

You said each submission is logged with timestamp, token ID and choices. If token IDs map to units (they almost certainly do), then anyone with access to that log can see how every unit voted. The CSV export also puts this in an email. Your bylaws require a secret ballot, so this may break them outright, not just weaken them.

Fix: after a vote is cast, store the choices in a table with no unit or token link. Give each voter a random receipt code they can check. Ask Varrow who can open the raw log, and make that a short list.

## Dorota Weiss is a conflict of interest, and she has the keys

She is a candidate with full admin rights and is the liaison to Varrow. As admin she could probably reissue links, approve proxies, see the log, or change a result. Whether or not she would, a losing candidate will say she could. Take her admin rights away from the vote, or make her read-only and recused. Require two people for any admin action, and make one of them someone who is not on the ballot.

## The live dashboard can influence and expose votes

Running totals per question during voting let people react to early numbers, and campaigns will use them. Turnout by floor can also reveal votes on small floors. Show turnout only until close, and hide any floor with fewer than about 10 units. Ask whether the board and office manager really need the running totals.

## Proxies are a single point of failure

One office manager approves a scanned PDF with no check on the signature. A forged proxy gives someone else's unit to a proxy holder, and that person may be on the board. Things to check:
- Can the member also vote with their own link? If so, which vote counts? If both are cast, the last one may win, which is confusing and open to abuse.
- Can the member see that a proxy was filed for their unit, and cancel it?
- Does one proxy holder get capped? How many units can one person hold?

Fix: have a second person check each proxy against the member's details on file. Notify the member by their own contact method when a proxy is approved. Set a clear rule that a member's own vote overrides the proxy.

## "Last submission counts" plus the export means the result can be altered

Anyone who gets a fresh link can change a vote. The CSV is an ordinary file that can be edited before it is emailed, and the certifying board members have no independent way to check it. Ask Varrow for the raw log as well as the CSV. Have a volunteer who is not on the board check that the count from the log matches the totals. Publish a file hash, so the numbers can be checked later.

## Phishing and fake reminders

Members are used to getting voting links by email, so a fake "your link has changed, click here" is easy to send. Post the official site address in the building, in the newsletter, and on every notice. Tell members that Varrow will never ask for their link by email or phone.

## Quorum and eligibility

Check who is on the list. A tenant may have the email address on file, not the leaseholder. Old or wrong addresses mean members never get their link. Eligibility of voters needs a clear rule, and the list of eligible units should be frozen and shared before voting opens.

## The legal side

A $1.9M assessment is a big decision, so check two things with a lawyer or your state or provincial co-op authority: whether your bylaws allow electronic voting at all, and whether this process meets the secret-ballot rule. If a result is contested, a weak process is the main thing that gets a vote thrown out.

## What to do before Monday

1. Stop the phone helpdesk from sending links to new addresses.
2. Remove Dorota's admin access from the vote, or make it read-only and recused.
3. Ask Varrow in writing: token length and storage, who can see the log, whether ballots are separable from unit IDs, how proxies are checked, and whether the raw log can be exported to an observer.
4. Turn off running totals until close.
5. Get a volunteer with IT security experience, or a local university computing department, to spend an afternoon trying to break it. Give them the same list as this one.
6. If Varrow cannot answer items 3 and 5 clearly, consider delaying the links. A bad online vote on a $1.9M assessment is worse than a delayed one.

If you want, I can draft the written questions for Varrow or a short test plan for your volunteers.
