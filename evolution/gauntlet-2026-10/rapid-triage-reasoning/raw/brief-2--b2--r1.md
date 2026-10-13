This is recoverable, and you have good backups. Your priority in the next 30 minutes is to protect those backups and make two phone calls. Don't pay, and don't let anything be wiped yet.

**Do these now, in this order**

1. **Protect the NAS (most urgent, do it before 19:00).** The NAS replaces last night's copy with a fresh one at 19:00. If the server is still encrypting files, the NAS will overwrite your last clean copy with encrypted files.
   - Unplug the NAS's network cable now, or power it off. Don't log into it from any infected machine.
   - Ask Dean to confirm the NAS's backup schedule can't run, and don't re-enable it until he's checked it.

2. **Isolate the server, but don't power it off.**
   - Unplug the server's network cable (and Wi-Fi, if it has any). That stops the encryption spreading and stops the Kelpie sync, without losing evidence held in memory.
   - This differs slightly from Dean's instruction. He said to leave it running, and he's right that it shouldn't be shut down. But leaving it connected means the damage keeps spreading and encrypted files keep syncing to the cloud. Tell him you've disconnected the network cable only and the server is still on. He'll almost certainly agree.

3. **Stop the cloud sync and protect the Kelpie versions.**
   - Pause or disconnect Kelpie sync on the server. If you can't reach it there, log into your Kelpie account from a clean device (a phone or a personal laptop that isn't on the office network) and pause it from there.
   - Change your Kelpie password and turn on two-factor authentication from that clean device.
   - You hold 30 days of versions, but you're at 92% of 2 TB. Encrypted copies of 380 GB of files will count as new versions and could trigger trimming of the older, clean versions. This is why stopping the sync matters. If you can, ask Kelpie support to pause version trimming on your account.
   - Don't delete anything from Kelpie.

4. **Call the insurer's incident line now.** Your policy says to call before taking any recovery steps or making any payment, so do it before Dean wipes anything. The steps above are containment, which is normally encouraged, but tell them exactly what you've done. Ask them:
   - whether they'll assign a response firm, and whether Dean can still do the rebuild;
   - what they need preserved (the server's disk, the ransom note, logs);
   - whether wiping the server tonight would affect your cover.
   Write down the claim or reference number and the name of everyone you speak to.

5. **Call Dean back.** Tell him what you've done and ask him to hold off on the wipe until the insurer has been spoken to. He should plan for a rebuild, but it shouldn't happen until:
   - the insurer has signed off, and ideally the disk has been imaged or kept, because wiping destroys the evidence they may need;
   - you know how the attacker got in, so the rebuilt server isn't hit again.
   Ask whether he could bring a spare drive or a replacement machine so the original can be kept untouched.

6. **Keep the PCs off the network.** Dean's instruction to shut them down is fine. Don't turn them back on or plug them in until he has checked them. Any one of them could be where this started, or could be carrying the infection. Photograph the ransom note on a phone, and note the time the first file changed (about 15:40).

**On Ruth's wish to pay tonight**

Please hold off, for these reasons:
- Your policy requires you to call the insurer first, and paying without that could put your claim at risk.
- You probably don't need to. You have two independent backups that may be clean: the Kelpie versions (from before 15:40) and the NAS copy (from 19:00 last night, if it's protected). Restoring from those is likely to be faster and safer than trusting the attacker's decryption tool.
- Paying doesn't guarantee that files come back, that the tool works, or that they won't come back for more. It may also raise legal questions, and the insurer or an adviser will want to look at that before anything is paid.
- There's also no deadline pressure on the ransom. You have 72 hours, so there's no reason to decide tonight.

Suggested line for Ruth: "Our backups look intact, so payment isn't our only route, and paying before the insurer approves it could void our cover. Let's hear from them first. We can still decide later."

**The VAT deadline**

- Note that the VAT filing portal and clients' records are a separate matter from the server. You may be able to file from clean laptops using data restored from Kelpie, even if the server isn't back.
- Restoring from Kelpie versions can be done file by file or folder by folder. Start with the 46 VAT clients' folders, so the deadline work comes first and everything else follows.
- If you can't make the deadline for some clients, contact the tax authority. A genuine IT incident is generally a recognised reason to ask for leniency, but check the rules for your country. Keep the incident records, since you'll need them. Your insurer or Dean may be able to help with this.
- Tell the 14 staff what to do tomorrow: not to log in to anything, and to wait for your message.

**Also worth doing tonight or tomorrow**

- Your practice software lives on the same server, so find out when it was last backed up and whether that's covered by the NAS or Kelpie copy. This is a question for Dean.
- Because it's client financial data, you may have to report the incident to the data protection regulator, and possibly to clients, within a fixed time (72 hours in many places). Ask the insurer, who will usually guide you on this.
- Change the passwords for email, the cloud, banking and any admin accounts, from a clean device, in case the attacker took credentials.
- Don't tell the attackers anything or reply to the ransom note.

**Assumptions I've made.** I've assumed that you're in the UK or a similar jurisdiction and that the NAS and Kelpie copies were healthy before 15:40. I haven't been able to check either, so Dean or the insurer should confirm. If the NAS is encrypted already, Kelpie is your main route, which is why the sync pause is so important.

If you tell me which of these steps you can't do or don't understand, I'll help you work out the next move.
