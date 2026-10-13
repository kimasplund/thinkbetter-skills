You have about 2.5 hours before the NAS runs at 19:00, and the first few minutes matter most. Your clean copies are your way out of this, so the first job is to stop the attack from overwriting them. Don't pay anything tonight, and don't let the server be wiped tonight.

**Next 10 minutes: protect the clean copies**

1. **Cut the NAS off from the network now.** Unplug its network cable, or at least switch it off. At 19:00 it will replace last night's good copy with whatever is on S: today, which is encrypted. If the ransomware has already reached the NAS, leave it unplugged and untouched. Don't power it back on or connect it to anything until Dean or the insurer's team says so.
2. **Stop the Kelpie sync, and do it from two directions.**
   - Unplug the server's network cable. Leave the server powered on, as Dean asked. This stops the encrypted files syncing up and also stops the ransomware spreading.
   - On a phone or a personal device, log in to the Kelpie web account. Pause or unlink the server's sync if you can find the option, and change the account password. Turn on two-factor authentication if it isn't on already.
   - The reason for the urgency is that every encrypted file uploads as a new version. You're at 92% of 2 TB, so older versions will start being trimmed, and your good versions are the ones that get trimmed. Don't delete anything in Kelpie.
3. **Confirm all 14 PCs are shut down and stay off.** Tell people not to log in to anything that touches S: or Kelpie. Anyone on Wi-Fi with a laptop should switch it off, not just close the lid.

**Minutes 10 to 20: call the insurer**

Call the incident line before anything else is done. Your policy requires it before any recovery step or payment, and a wrong move could put your cover at risk. Have these ready:

- The timeline: first signs at about 15:40, ransom note, 72-hour demand.
- What you've done so far: network cables pulled, NAS offline, PCs off, server left running.
- The backup situation: a NAS copy that may be clean, plus Kelpie with 30 days of versions.
- Dean's plan to wipe the server tonight.

Ask them directly:

- Whether they have a forensics or response team, and who authorises Dean's work.
- Whether the server should be wiped at all. Wiping destroys the evidence of how they got in. If you wipe without finding that out, the attacker may still have access.
- What their obligations are about notifying clients, your regulator and the data protection authority. The server holds client financial records, so a data breach notification clock may already be running.

**Call Dean back (a 2-minute call)**

- Don't wipe or reinstall the server tonight. Ask him to wait for the insurer's instructions.
- If it's possible, ask him to take a disk image or make sure nothing is overwritten before anything is rebuilt.
- Tell him about the NAS and Kelpie steps so he doesn't reconnect either one when he arrives.

**Ruth and the payment**

Tell Ruth you understand the deadline pressure, and then make these points:

- The insurer has to be involved before any payment. If you pay without them, you risk your cover.
- The demand runs for 72 hours, so nothing is lost by waiting until tomorrow to decide. Paying is also not a safe route to the deadline. Decryption can be slow and incomplete, and there is no guarantee you get the files back or that the attackers leave.
- You probably don't need to pay. You have two backup sources, and the first job tonight is to find out whether either is clean.
- If the money is ever paid, it should go through the insurer's negotiators and legal advisers, who check sanctions rules and often get the amount reduced.

**The VAT returns tomorrow**

- Once the insurer has spoken, ask Dean or their team to restore the 46 clients' files from Kelpie's version history (from before 15:40 today) onto a clean machine that is not on the infected network. That is the quickest realistic way to get working. It means a restore of the folders you need first, not all 380 GB.
- Practice software might be a problem if it lives on the server and its database is encrypted. Ask Dean tonight whether it can be run elsewhere from backup, and whether the vendor can help.
- If the returns still can't be done in time, VAT returns can be filed on the client's own HMRC login with their figures, or the late filing can be explained. Late submissions generally mean penalty points or interest rather than anything catastrophic. Check HMRC's current guidance tomorrow morning, and send clients a short, honest note. If you tell people it's an IT incident, and nothing more, you'll avoid putting out claims you can't back up.

**Write down as you go**

Note the time of each action and who did it, plus the ransom note text and its wallet address. Take photos of the screen with a phone. Don't try to open the .qrx files, and don't delete the ransom note.

**Assumptions**

I've assumed you're in the UK, given VAT and HMRC. I've also assumed the server wasn't already switched off, and that Kelpie versions older than the ransomware start are still within the 30-day window. If the NAS did run at some point after 15:40 today, its copy is probably bad. Kelpie is then your main source, which is why the sync has to stop first.

**Order of play from here**

1. NAS offline. (Now)
2. Server network cable out, Kelpie sync paused, password changed. (Now)
3. Call the insurer. (By about 16:45)
4. Call Dean and ask him to hold the wipe. (Straight after)
5. Talk to Ruth, with the insurer's answers in hand. (By 17:00)
6. Plan the restore from Kelpie for the VAT returns. (Evening, with Dean and the insurer)
