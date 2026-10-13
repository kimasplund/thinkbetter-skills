# Breaking the online Level 4 Fire Door Assessor exam

A determined cheat has several easy routes through this design, and the first one needs no technical skill. A pass puts someone on a public register that insurers rely on, so a fraudulent pass is worth far more than the £340 fee. I'd fix the items below before you sign with Tallyward, roughly in this order.

## Verdict

Don't sign yet. The proctoring tool is reasonable. The weaknesses are in how the rest of the process is built around it: the timing of results, identity checks, the size of the question bank and the unlimited pause. Most fixes are rule changes rather than new technology.

## The ways through, worst first

**1. The pass is published before the cheating review happens.**
Passes are confirmed automatically after two working days. Flagged sessions are reviewed within ten working days. So a cheat who is flagged still gets a certificate and a register entry, and may hold them for up to eight working days before anyone looks at the recording. The certificate can be used to sign inspection reports in that time. Even if the officers later catch them, you are then revoking a credential that insurers and building owners may already have relied on.
*Change:* never auto-confirm a pass for a flagged session. Hold it until an officer has cleared it. Better still, make the review deadline shorter than the confirmation delay, or confirm every pass only after the review queue for that sitting is clear. Add a clause to the candidate terms that lets you revoke a pass for integrity reasons after the fact, and decide now how you would notify employers and insurers if that happens.

**2. A paid stand-in can sit the exam.**
Booking needs only a name, a membership number and an email address, and none of those is checked against anything the candidate can't simply supply. At the start, the candidate holds ID up to the webcam and the app saves a snapshot. Nobody compares that snapshot to the ID or to a photo you already hold, and nothing checks that the same person is at the keyboard at minute 80. A qualified assessor who sits for someone else, or a stand-in coached for one sitting, would pass the ID step easily. Photo ID can also be a good forgery or someone else's real ID held up for a few seconds.
*Change:*
- Collect a photo and ID at booking and have a person verify it against the membership record before the candidate is allowed to book a slot.
- At the start, have a live human or a trained reviewer match the face to the ID before the paper unlocks, not after.
- Re-check the face at random points and at submission, and make the reviewers look at those frames first.
- Confirm that the membership number belongs to the person booking, for example by sending a confirmation to the contact details already on your member record rather than the email typed in at booking.

**3. The unlimited pause on disconnection is an open door.**
The timer stops whenever the connection drops and there is no limit on how many times it can. A candidate can pull a cable, or switch off the Wi-Fi, at the point where a question is stuck, then look it up, ask a colleague or message a helper, and reconnect later with the clock still where it was. "Rural broadband" gives a ready excuse, and the vendor's flags won't fire while the stream is down. Over a 60-question paper, ten short drops could add up to a lot of unobserved time.
*Change:*
- Cap the number of drops and the total paused time (for example three drops and 15 minutes in total), and flag any session that gets near the cap.
- While disconnected, hide the question or blank the screen, and let the app keep recording locally and upload the recording on reconnection, so the gap isn't a blind spot.
- Log every drop and look at the timing: drops that always land just after a question appears are a signal.
- Offer genuinely poor-connection candidates a supervised alternative, such as a test centre or a library with a proctor, so you can stay strict on the home route without being unfair.

**4. The question bank will leak within a few sittings.**
Each candidate sees 60 of 90 questions, which is two thirds of the whole bank. Two papers share about 40 questions on average. If three candidates pool what they remember, around 96 in 100 questions are covered. With five, almost the whole bank is covered. At about 117 candidates a month, and with failed candidates allowed to resit the next month and see the bank again, the bank will end up on a forum or in a WhatsApp group quickly. The shuffling of order and options makes two papers look different, but it doesn't stop memorised answers from working.
The three-day window makes it worse: someone who sits on Friday morning can pass the questions to someone who sits on Sunday night.
*Change:*
- Grow the bank substantially (several hundred items is a more realistic target for 1,400 candidates a year) and keep a rule for retiring and replacing items every cycle.
- Don't give item-level feedback to people who fail, only an overall result and broad topic areas.
- Run several equivalent forms and rotate which items are live in each window.
- Look at the answer data: the same unusual wrong answers, unusually fast times on hard items, and clusters of near-identical papers are the usual signs of a leaked bank.
- Consider one sitting day (or a few fixed sessions) rather than a Friday-to-Monday window, so there's no time for answers to travel within the same sitting.

**5. The lockdown and webcam can be sidestepped with a second device.**
The app watches one webcam, one microphone and one screen. It can't see a phone propped outside the camera frame, a second monitor, an earpiece, notes on the wall behind the screen, or a person sitting out of shot. A virtual machine, a remote-desktop session to a helper, or a capture card feeding a second computer are further options. A candidate can also photograph the screen with a phone to harvest questions for sale. Tallyward's flags (looking away, a second voice, a second face) catch the clumsy cases, not a prepared one.
*Change:*
- Ask the vendor how they detect virtual machines, remote access, virtual cameras and extra displays, and ask for a test result rather than a promise. Try to bypass it yourselves during the pilot.
- Require a room scan before the start and a second camera angle (a phone on a stand showing the desk and hands), and keep the recording of both.
- Prefer a quiet room with the door closed and set rules for who may be present.
- Keep a supervised test-centre route for the highest-risk cases.

**6. Human review is a single point of failure.**
Two exam officers review every flagged session in ten working days. You haven't said how many flags to expect. If the software is jumpy (rural lighting, a noisy household, a child walking past), the officers can be swamped and start to wave sessions through. Alternatively, an officer could be bribed, pressured or simply careless, and nothing in the design lets anyone check their decisions. A recording is not very useful if it is only watched by the person with something to lose.
*Change:* sample-check cleared sessions with a second reviewer, require two people for any decision to clear a high-severity flag, keep a log of who reviewed what, and agree a flag rate with the vendor so you can staff for it. Run the pilot first and count flags before you set the review deadline.

**7. The vendor and the recordings are a target of their own.**
Tallyward will hold video, audio, screen captures, ID images and your question content for every sitting. A breach exposes candidates' IDs and your exam. Check where the data is held, how long it is kept, who at the vendor can see it, whether there is an independent security assessment, and what the contract says about breach notification. Face and ID images processed to identify a person may need extra care under UK data protection rules, so run a data protection impact assessment before launch.

## Smaller gaps worth closing

- A candidate who finishes at 07:59 on Monday plus any pauses will run past the stated closing time. Say whether the paper must finish or only start by then.
- Passes are confirmed by an automatic process, so anyone who can alter results data, or who gets access to the register admin, bypasses all of this. Limit and log who can change results or add register entries.
- Test what happens with duplicate bookings, someone booking under another member's number, a payment refund after a start, and a candidate who starts on two computers at once.
- Make sure the app handles a power cut or a crash by resuming with the same questions, not drawing a new random set (which would give a free look at a second paper).
- A resit the next month gives a cheat repeated attempts. If you can, limit the number of resits within a year and treat repeated near-misses as a flag.

## What I'd change before signing, in order

1. Hold any flagged pass until it's been reviewed, and add revocation to the terms.
2. Put a real identity check before the paper unlocks, and verify the candidate against your member record.
3. Cap and log the disconnection pauses, and record locally during drops.
4. Enlarge the bank, rotate forms, and start analysing answer patterns.
5. Add a second camera view and ask the vendor to prove their lockdown against VMs and remote access.
6. Agree flag volumes and staffing, add second-person review, and run a pilot with deliberate cheating attempts (your own staff) before the first real February sitting.

## Residual risk

Even with all of this, a home-sat exam can't fully stop a determined, well-resourced cheat, such as a paid stand-in with a good fake ID and a prepared room. What you can do is make cheating costly, detectable afterwards and reversible. That last part matters most here, because the register is relied on by people outside your organisation.

What I took from your description: the exam is entirely remote with no test-centre option, the vendor's software only flags and doesn't block, and the register entry is created automatically. I assumed the 117-a-month figure is spread evenly and that your question bank is currently exactly 90 items. I also don't know how many flags you expect or what the contract says about data or breach handling. Check first how long a flagged candidate would hold a live certificate under the current timetable, because that's the quickest gap to close and the most damaging if left open.
