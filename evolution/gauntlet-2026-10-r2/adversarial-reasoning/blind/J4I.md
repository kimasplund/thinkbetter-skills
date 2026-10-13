# Attacking the online Level 4 exam design

## Verdict

Your doubts are justified. As described, I would not sign with Tallyward yet. The weakest points are in your own process, not in the proctoring software. The top three:

1. **Nothing proves the person on camera is the registered candidate.** Booking needs only a name, membership number and email, and the ID snapshot is saved but never checked against anything.
2. **A pass reaches the public register two working days after the exam, but flagged sessions are reviewed up to ten working days after.** Anyone who cheats and isn't caught inside two days is already registered, with certificate in hand and reports being signed.
3. **The question bank is too small and too exposed.** Ninety questions, a 65-hour window and unlimited resits mean the whole bank will leak within a few months.

None of these needs a sophisticated attacker. Each is open to someone with a friend, a phone and a few hundred pounds of motivation. A register that insurers rely on makes a pass worth far more than the £340 fee, so expect people to pay for help.

## The attacks, most serious first

### 1. Someone else sits the exam
- **How:** A cheat books with their own details (or a colleague's membership number, which is hardly secret) and a qualified assessor sits in their place. At the start the proxy holds up a photo ID: a good copy, someone else's genuine ID or a lookalike. The app saves a snapshot, and nobody looks at it unless the session is flagged. A proxy who sits still and looks at the screen won't trigger "looking away" or "second face" flags.
- **Why it works:** The check is recorded, not performed. Nothing compares the ID to the person, the person to the booking, or the booking to your membership records.
- **Change:**
  - Verify booking identity against your membership records (name matches member, email on file, not a free-text claim).
  - Have a human proctor, or an ID-verification service that checks document authenticity and face match, approve the ID before the exam unlocks. A snapshot filed for later is not enough.
  - Compare the face to the verified ID throughout the session. A different person halfway through is a standard handover trick.
  - Put a photo on the register entry that matches the verified ID.

### 2. Pass first, review later
- **How:** The pass is confirmed automatically at two working days. Your two officers review flagged sessions within ten. A cheat flagged on day five is already on the register and holding a certificate. Insurers and building owners may by then have accepted inspection reports signed by them.
- **Why it matters:** Revoking a registration after the event leaves a trail of fire-door reports that were signed by someone who is not competent. That is your reputational and legal exposure, and arguably a safety exposure.
- **Change:**
  - Don't publish a pass until its session has been cleared. Either shorten review to fit inside the confirmation window, or lengthen the confirmation window to cover review. At roughly 117 sittings a month, clearing every flagged session before release is realistic for two officers if the vendor's flagging is tuned sensibly.
  - Release unflagged passes quickly if you like, but never flagged ones.
  - Write down now how you revoke a registration, how you notify insurers and what happens to reports already signed. You will need it.

### 3. The bank leaks, and the resit rule helps the leaker
- **How:** The pass mark is 45 correct out of 60. Each paper is 60 of 90 questions, so any two candidates share about 40 questions on average. Shuffling the order and answer options hides nothing: a questions-and-answers sheet still works. A candidate points a phone at the screen, or reads questions aloud to a recorder, and the next group has the lot. One sitting exposes two-thirds of the bank, and two sittings expose nearly all of it.
- **The resit makes it cheaper:** A candidate who deliberately fails can resit next month and harvest again. £340 buys a look at 60 of your 90 questions.
- **The 65-hour window makes it worse:** Friday 08:00 sitters can pass questions on to Sunday and Monday sitters through a group chat. Your "fit it around site work" feature doubles as a leak channel.
- **Change:**
  - Grow the bank substantially (several hundred items) and retire and rotate items on a schedule. Track how often each question appears and how it performs, and replace any that behave oddly, such as everyone suddenly getting a hard question right.
  - Use scenario and image-based questions with varied parameters (door type, gap measurements, certification details) so memorised answers don't transfer.
  - Give resitters a paper built from questions they haven't seen, and cap attempts per year.
  - Shorten the window or run fixed sessions in several slots. If site work forces flexibility, accept a bigger bank as the price.

### 4. The pause on reconnection is a lookup tool
- **How:** Any time the connection drops, the timer stops, and there's no limit on reconnections. A candidate can see a hard question, "lose" the connection, look up or ask for the answer in the gap, reconnect and answer. While disconnected there's no stream, so nobody sees it. Repeating this ten times costs nothing. Also, if Tallyward only records while connected, the gaps are blind spots, and an unlimited number of them makes the "whole session" recording a fiction.
- **Change:**
  - Cap reconnections (for example three) and cumulative paused time (for example ten minutes). Beyond that the session ends and goes to a human.
  - Lock the current question on disconnection so it can't be viewed or changed until the stream is back, and don't let candidates return to earlier answers afterwards.
  - Log every drop and flag unusual patterns, such as drops that coincide with question views or happen repeatedly on hard questions.
  - Deal with rural broadband fairly through a pre-booked accommodation route: a tested connection check before the exam, a mobile hotspot backup, or an assisted sitting at a partner centre. Don't make the weakest control in the design the default for everyone.

### 5. The lockdown and the camera see less than you hope
- **How:** Your brief says the app "is meant to" lock down the computer and Tallyward's software "supposedly" flags behaviour. I'd treat those words as the real risk. Common ways round it:
  - A virtual machine or remote-access tool lets a helper see and control the exam from elsewhere.
  - A second screen, or a phone propped out of the webcam's view, displays notes or a live helper.
  - A hidden earpiece or a person off-camera whispering. A webcam shows a face, not the room.
  - A screen mirrored through a capture device to someone else who types answers back.
- **Change:**
  - Before signing, make Tallyward demonstrate against these attacks. Ask for independent penetration-test results, and run your own test with a staff member trying to cheat in each way listed above. If they won't allow it, that tells you something.
  - Require a room sweep at the start (a slow 360 degree pan with the camera, desk and floor visible) and consider a second camera, such as a phone on a stand showing the candidate's hands and side view.
  - Check the contract for what it guarantees: detection rates, false-positive rates, and who is liable if it fails.
  - Treat flags as a means of triage, not proof. A determined cheat produces few of them.

### 6. The reviewers are a bottleneck and a single point of trust
- **How:** Two officers must clear every flagged session. If the software flags a large proportion (they usually do, because looking away is normal for people thinking), they will skim. Skimming plus pressure from candidates, employers and each other is how things get waved through. Two people with the power to clear a session are also an obvious target for bribery or pressure, and a cheat who knows the process may approach them.
- **Change:**
  - Sample unflagged sessions too, so cheats can't rely on staying under the radar and you can measure what the flags miss.
  - Require a second reviewer for any decision to clear a flagged session where the first reviewer was uncertain, and log all review decisions.
  - Agree a standard for what the vendor flags and set a target for how many flagged sessions per month are manageable. If it's more than your two officers can properly review, adjust the vendor settings or add capacity before launch.

### 7. The data you will be holding
- You will store IDs, faces, voices and video of 1,400 people a year, across your systems and Tallyward's. That is sensitive personal data under UK GDPR, possibly biometric. A leak at the vendor also supplies identity-theft material and forged IDs for the next attack. Confirm retention periods, where the data is stored, who at Tallyward can see it and what the breach terms are. Also check that your certificate email can't be intercepted or reused to claim someone else's pass.

## Smaller gaps worth closing
- **Deadline edge:** What happens to someone mid-exam at 08:00 on Monday, or whose paused session runs past it? Decide the rule and stick to it.
- **Failed-login and device failure:** Define who decides whether a crashed session counts as an attempt, and make sure a cheat can't claim "technical fault" to get a free sitting.
- **Certificate and register:** Ensure certificates carry a verifiable register link so a forged PDF can't pass as real. Insurers should be able to check the register, not just the paper.
- **Appeals:** If you start voiding passes, expect challenges. A written appeals route protects you.

## What I'd do before February
1. Add real identity verification at booking and before the exam starts.
2. Move register publication to after review, and write the revocation procedure.
3. Cap and lock reconnections.
4. Make Tallyward prove its lockdown and flagging against a live attack by your own staff, and amend the contract accordingly.
5. Expand the bank and rotate it, fix the resit rule and narrow the window.

If you can do only two before launch, do the first two. They close the cheapest routes to your register and limit the damage from everything else.

## Residual risk

Even with all of these changes, a remote, unsupervised exam taken at home cannot be made cheat-proof. A well-resourced cheat with a proxy who passes identity checks and a clever second-camera setup may still get through occasionally. The aim is to make cheating costly and likely to be caught, and to be able to withdraw a registration quickly when it is. If the consequences of one unqualified registered assessor are severe, consider keeping a supervised in-person route, or a short supervised practical check, for the highest-stakes level.

I worked only from your description, so I took the vendor's claims as unverified, assumed roughly 117 sittings a month, and assumed that membership numbers can be obtained by other people. I did not see the contract, the question bank or Tallyward's actual settings. Check first who is verifying identity, what the register publishes automatically and when, and whether the vendor will let you test it with a live attempt.
