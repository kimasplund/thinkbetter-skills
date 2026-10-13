Your doubts are justified. As described, the design has several gaps that a determined cheat could use, and two of them need no skill at all. I've ranked them by how badly they hurt the register. I haven't seen Tallyward's product, so where I say "the app" I'm working from your description, and you should test those claims rather than trust them.

## The worst problems

**1. A cheat is on the register before anyone looks at the evidence.**
Passes are confirmed automatically after 2 working days. Flagged sessions are reviewed within 10 working days. So a flagged cheat gets a certificate and a public listing, and insurers and building owners can rely on their reports for up to 8 working days before an officer sees the flag. Even if you catch them later, reports they signed in the meantime are already in circulation. The review is also only a clean-up step, because nothing in the process stops a pass.
- Change: don't issue the certificate or register entry until review is complete. Unflagged sessions can clear fast, and flagged ones wait.
- Also: add a written revocation policy, a candidate agreement that allows revocation for later-discovered malpractice, and a plan for notifying clients of a revoked assessor's reports.

**2. Nothing proves the person sitting the exam is the person who booked.**
Booking needs a name, a membership number and an email. None of these is secret, and anyone with a card can pay. At the exam, the candidate holds up ID and the app saves a snapshot. Nobody compares it to anything unless the session is flagged. A friend or paid expert can sit the exam with their own face and a forged or borrowed ID. The saved snapshot is useful for an investigation after the fact, but it doesn't stop the impersonation.
- Change: have a human or a reliable automated check compare the ID photo, the live face and the membership record before the exam starts, with no start until it passes. Check the ID's security features, not just the photo.
- Also: run a periodic face-match of the start-of-session face against the face at the end and at random points, so a swap mid-exam is detected.
- Also: confirm that the membership number belongs to the named person with a check that isn't just something they typed in.

**3. The question bank will leak, and the 72-hour window speeds it up.**
Each paper uses 60 of 90 questions, so any two papers share about two-thirds of their questions on average, and a handful of candidates can reconstruct nearly the whole bank. Shuffling order and options hides nothing, because the content of the questions is what gets shared. The window makes it worse. Someone who sits at 08:05 on Friday can pass questions to everyone sitting on Saturday or Sunday, with 48 or more hours to look up answers. Failed candidates are an extra source: they see 60 questions, resit a month later, and in the meantime can write up what they saw. With 1,400 candidates a year, the whole bank would be public in a few months. The claim that "no two papers are the same" is true of the order of questions and not of the content, and I wouldn't rely on it as a security property.
- Change: cut the window to fixed slots, or a window of a few hours. If you need flexibility for site work, offer several short sessions on one day with a fresh paper for each, and don't release any candidate's questions until everyone in that window has finished.
- Change: grow the bank substantially and retire items on a rotation, with a plan to write new questions continuously. As a rough guide, you want a bank several times the size of a single paper, and a way to track how often each item has been exposed.
- Change: limit the resits and reduce what failures reveal. Don't show failed candidates which questions they got wrong. Consider a longer wait or a fresh set of items on resits.
- Also: monitor the web and the usual exam-dump forums for your questions.

**4. Unlimited reconnections with a paused timer is a built-in way to cheat.**
A candidate can drop the connection on purpose when they reach a question they don't know, look the answer up, and reconnect, with the clock paused the whole time. The pause also hides what happens during the gap: the stream isn't recording, so a helper can walk in. The 90-minute limit then means very little. You're right that rural broadband is a real problem, and I'd keep the accommodation but tighten it.
- Change: cap reconnections (say 2 or 3) and total paused time (say 5 to 10 minutes), and treat the limits as automatic flags for review. Make the cap exceptions go through a documented route with evidence.
- Better: have the app record locally and upload when the connection returns, so a drop doesn't leave a gap in the evidence. Questions seen before the drop shouldn't be changeable afterwards, and the app should not show a question again after a disconnection with different options.
- Also: give candidates a way to run a connection check beforehand, and an offer of a test centre as a fallback for those who can't get a stable link.

## Other ways in

**5. The lockdown app and webcam leave a lot of room.**
Common routes include a virtual machine or remote-desktop session where the real screen is controlled by someone else, a second device or an HDMI splitter feeding the questions to a helper, a phone out of the camera's view, an earpiece, and notes just outside the frame. A webcam sees a face and a bit of a room, and "looking away" is a weak signal because honest candidates look away too. I can't tell you how well Tallyward handles these. Ask them.
- Before signing: ask for the detection rates for each of these methods, ask how the app detects virtual machines and remote access, and get a trial where your own staff or a hired tester try to cheat. Make this a condition of the contract.
- Consider requiring a room scan at the start and a second camera view (for example a phone placed to show the desk and hands) for higher-risk sessions.
- Be clear internally that remote proctoring reduces cheating and doesn't eliminate it. The design should assume some cheating will get through and have a second line of defence (see below).

**6. Reviewing only the flagged sessions means unflagged cheats are never checked.**
If the software misses it, nobody looks. A good cheat is designed to avoid triggering the flags.
- Change: have officers review a random sample of unflagged sessions each month, and use the miss rate to check the vendor's flagging.
- Check capacity: 1,400 a year is about 115 sessions a month. If, say, a fifth are flagged, that's about 25 sessions of 90 minutes each to review, plus a sample, for two officers. That seems feasible, but check against the real flag rate in the pilot, because a noisy tool can swamp you.

**7. Statistics catch what cameras miss, and you aren't using any.**
Look at the results as data: unusually fast completion on hard items, identical wrong answers across candidates, clusters of candidates from the same employer or training provider, pass rates that jump when the bank leaks, and candidates who score high on the exam but have a history of failing similar things. These checks are cheap and run after the fact, and they catch collusion and proxy-taking that video won't.

**8. Insiders and the vendor.**
Tallyward streams and stores the screen, which means they hold the entire bank and recordings of every candidate. Your exam officers have access too. Check the contract for who can see the questions, how long recordings are kept, and what happens at the end of the contract.

## Fairness and legal points

The same system that catches cheats will wrongly flag honest people: those with poor lighting, disabilities, neurodivergent candidates who look away to think, and people in shared homes where a second voice is unavoidable. If an automatic flag can lead to a failed or revoked result, you need a clear appeals route, human review of the evidence and a published reasoning standard. Webcam, microphone, screen and ID images are personal data, and probably sensitive data in places, so you will need a data protection impact assessment, a retention limit and a clear lawful basis before launch. Check these with your data protection lead and counsel, because I can't settle them from here.

## What I'd change first

1. Hold certificates and register entries until review is done (cheap and the most important fix).
2. Verify identity properly before the exam starts.
3. Shorten the window and fix the bank problem: bigger bank, item rotation, resit limits.
4. Cap reconnections and paused time, and record locally so there are no evidence gaps.
5. Make the vendor contract depend on a live attack test, and sample unflagged sessions.
6. Add post-exam statistics and a revocation policy.

## A broader point

The credential is trusted because it points to a competent physical assessor, and a multiple-choice exam of recalled facts is a weak proxy. If the register matters to insurers, consider whether to add a practical or observed component, even a short one, so that a leaked bank can't be enough to get listed. That's a design choice for you, but it would remove much of the reward for cheating.

## Assumptions

I've assumed the exam is the only route onto the register, that flags come from Tallyward's software with no live human proctor, and that the 8:00 Friday to 8:00 Monday window applies to the whole cohort. If any of these is wrong, tell me and I'll adjust.
