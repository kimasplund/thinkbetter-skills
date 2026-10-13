Do not pay tonight, and do not let the server be wiped tonight. You have two clean copies of your data that are both about to be damaged, and one of them has a hard deadline of 19:00. Protecting those copies is the most important thing you can do in the next half hour.

**Why the clock matters**

- **The NAS at 19:00.** It replaces last night's copy with whatever is on S: at that moment. If S: is still encrypted, you lose your best clean copy.
- **Kelpie Drive.** It is syncing the encrypted files up as new versions. You are at about 1.84 TB of 2 TB, and S: is about 380 GB, so a full re-upload of encrypted files would push you over the limit. Kelpie then starts trimming older versions, and those are the clean ones. Every minute it stays connected makes this worse.

**Next 30 minutes, in this order**

1. **Cut the server off from the network (now, 2 minutes).** Unplug its network cable and turn off any Wi-Fi. Do not shut it down or power it off. Dean wants it left running so he can examine it, and powering off can destroy evidence. Cutting the network stops the Kelpie sync and stops the encryption spreading. If the server is not already unplugged from the NAS, do that as well.
2. **Protect the NAS (before 16:40).** Check whether the NAS copy has been touched. Look for .qrx files on it, and check the time of its last copy (it should be 19:00 last night). If it looks clean, unplug its network cable and power it off, or at minimum disable its schedule. Do not let the 19:00 job run. Do not open or "test" files on it from a networked PC.
3. **Secure the Kelpie account (from a phone or a PC you trust, 5 minutes).**
   - Log in to the Kelpie web account and confirm the server is no longer syncing.
   - Change the password, sign out all other sessions and devices, and turn on two-factor authentication if it is not on.
   - Do not delete anything. Do not "free up space".
   - Contact Kelpie support and ask them to place a hold on version trimming for your account, or to temporarily raise your storage. Note the time of the call.
4. **Call the insurer's incident line (by about 16:45).** Your policy says to do this before any recovery step or payment, and they usually bring in specialists who can help with exactly this. Tell them:
   - What happened and when (about 15:40).
   - That you have a NAS copy from 19:00 last night and Kelpie versions going back 30 days.
   - That your IT contractor proposes to wipe the server tonight.
   - That a partner wants to pay.

   Ask them directly whether wiping the server tonight is allowed, who they want to examine it, and whether they have a recommended recovery provider. Write down the claim number, the name of the person you spoke to, and the time.
5. **Speak to Dean again (by about 16:50).** Ask him not to wipe or reinstall anything until the insurer has approved it. Reinstalling destroys the evidence needed for the claim and for working out how they got in. It may also put you back online with the same weakness. He can still do useful work tonight: take an image of the disk if the insurer agrees, and prepare a clean machine or a rebuilt server that is not connected to anything yet.
6. **Brief Ruth (by about 16:55).** Be concrete about why paying tonight is the wrong call:
   - You have 72 hours, so there is no need to decide tonight.
   - You probably do not need to pay. If last night's NAS copy or the Kelpie versions are clean, you can restore without the criminals.
   - Payment is not guaranteed to produce a working decryption tool, and decryption can be slow and incomplete.
   - Paying can breach your policy terms or sanctions rules, and the insurer will want to be involved in that decision.
   - If both copies turn out to be unusable, payment becomes a decision for the partners and the insurer together, later.
7. **Keep everything else quiet.** Keep the PCs off, as Dean said. Do not let anyone log in to the server or plug in a USB drive. Do not delete the ransom note. Photograph it with a phone and photograph any screens that show the problem. Do not contact the attackers.

**The VAT deadline**

You probably can still get the 46 returns done. The data is likely recoverable from last night's NAS copy (everything up to Tuesday evening) or from the Kelpie versions from before 15:40. Work from a clean laptop that has never been connected to the server. Any of Wednesday's changes may need to be redone from paper or email. I do not know what your practice software needs in order to run, so ask Dean and the software vendor tonight whether it can be installed on a clean machine, and where its data lives. Also check whether HMRC gives you any flexibility on late filing, and note that you may be able to submit returns directly through HMRC's online services if the practice software cannot be restored in time.

**Assumptions I made**

- The NAS and Kelpie copies are unaffected so far. I could not check this, and step 2 is how you confirm it.
- You are in the UK, given the VAT and HMRC context.

**Things to do after tonight**

- Restore from the cleanest copy once the insurer has agreed, onto a clean machine.
- Change every password that was used on the server, since the attackers may have captured them.
- Keep a copy of your data that is offline, or one that cannot be overwritten, so a single bad night cannot replace every copy.
- Find out how they got in before the server goes back on the network.
- Check whether you have to notify anyone about client data, and ask the insurer about it on the call.
