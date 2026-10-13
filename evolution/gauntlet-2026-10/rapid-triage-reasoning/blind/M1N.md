You have two things that will destroy your recovery options if they happen before 19:00, so do those first. Then call the insurer. Nothing else needs a decision tonight.

**Minutes 0-10: stop the two things that overwrite your good copies**

1. **The NAS.** At 19:00 it replaces last night's copy of S: with whatever is on the server then, which is encrypted files. That would destroy your only offline-style backup. Unplug the NAS's network cable now. Pulling its power is also fine. Don't log in to it or "check" it. Just disconnect it, and leave it as it is until Dean or the insurer's responders look at it.
2. **Kelpie Drive.** The server is still syncing, so encrypted files are being uploaded as new versions. You're at 92% of 2 TB, and S: is about 380 GB, so a full re-upload could push you over the limit. Kelpie says it trims older versions once you're full, and those older versions are your clean copies. Pause or stop sync, or better, take the server off the internet. If you can't do that cleanly, unplug the server's network cable. Then phone Kelpie support and ask them to:
   - hold or freeze version trimming on your account
   - confirm you can restore to a point before about 15:40 today

   Don't delete anything in Kelpie, and don't "clean up" space.

**Minutes 10-20: contain the server, but don't wipe it**

- Unplug the server's network cable (and Wi-Fi, if it has any). **Leave it powered on.** Dean was right about that, because a running machine may hold evidence in memory that responders can use. Don't reboot it and don't try to decrypt anything.
- Keep the PCs shut down and off the network. Don't switch them back on until someone has checked them. The ransomware may be on some of them too.
- Take photos of the ransom note and a few of the encrypted files with a phone. Write down the times: first noticed around 15:40, and when you disconnected things.
- Don't reply to the attackers, don't click anything in the note, and don't pay anything.

**Minutes 20-30: call the insurer's incident line**

Do this before any recovery or payment, as your policy says. Call as soon as the NAS and Kelpie are protected, or sooner if someone else can do those two jobs while you phone. Tell them:
- what happened and when
- that the NAS and cloud sync are now isolated
- that the server is still on but off the network
- that the contractor wants to wipe and reinstall it tonight
- that you have a deadline tomorrow

Ask them directly:
1. Can you restore from Kelpie or the NAS, and do they want the server preserved first?
2. Do they supply or approve a forensic and recovery firm tonight?
3. What do they require before any payment? Make it clear that paying is not being decided tonight.
4. What are the breach-notification steps? You hold client financial data, so there may be regulatory reporting deadlines, which the insurer can advise on. Write down the claim number and the name of the person you spoke to.

**Dean and the wipe**

Phone or text Dean now: **do not wipe or reinstall anything tonight until the insurer has agreed.** Wiping destroys the evidence they need to find out how the attackers got in. If you restore onto a machine that is still compromised, you can be hit again. It may also put your claim at risk. He can still come at 19:30 and help, and the insurer may want him to work with their responders.

**Ruth and paying**

You don't have to settle this tonight, and it is not your call alone. Paying doesn't guarantee that the decryption key works or that your data hasn't already been copied. It can also break the policy terms if done before the insurer has agreed. Tell Ruth that the insurer has to be involved first. There is also a good chance you won't need to pay, because you probably have clean copies:
- the Kelpie versions from before 15:40 (30 days of history, assuming nothing has been trimmed)
- last night's NAS copy, if you act before 19:00

**The VAT deadline**

The practical route is to restore from Kelpie, or the NAS, onto a clean machine rather than the old server. That machine can be a new or temporary one, and the insurer or Dean can help you set it up. Prioritise the 46 VAT clients' files and the practice software data first. If recovery slips past tomorrow, ask the insurer and your clients about late-filing options. A short, documented delay caused by a cyber attack is much better than a rushed restore onto a compromised system.

**Also, tonight**

- Tell staff not to open the shared drive, not to plug in USB sticks, and not to use work email from the office PCs.
- Later, from a clean device, change passwords for email, Kelpie and the admin accounts, and turn on multi-factor authentication. Don't change them from the infected network now.
- Tell the partners that what you've done so far (isolating the NAS and cloud, not paying, calling the insurer) is the right order.

**Summary of what to do**

1. Unplug the NAS.
2. Stop Kelpie sync and ask them to freeze trimming.
3. Unplug the server's network cable but leave it running.
4. Call the insurer.
5. Tell Dean not to wipe anything.
6. Hold off on any payment.

I've assumed that Kelpie sync can be paused from the server, or that you can cut its internet access, and that the server's network cable can be pulled. If either assumption is wrong, tell the insurer and Dean as soon as possible.
