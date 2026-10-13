# Breaking the online Level 4 exam: what a determined cheat does and what to change

## Bottom line

I would not sign the vendor contract on this design as it stands. The proctoring tool is not the main weakness. The weaknesses are in the rules around it. Four of them let someone get onto your public register and into circulation as a signing assessor before anyone has looked at the evidence. Fix those four first. Most of the fixes are policy changes that cost little and need no new technology.

The stakes justify the effort. A registered assessor's signature is accepted by building owners and insurers, so a fraudulent pass can become a fire door that was never properly inspected.

## The ways through, worst first

### 1. The pass is issued before the review happens

The certificate and register entry go out automatically two working days after the exam. Your officers have ten working days to review flagged sessions. So for up to eight working days, a person whose session was flagged for a second voice, or a second face, is already on the public register and already signing reports. Nothing in the design reverses that if the review later finds cheating. A cheat who has just passed has also had days to do paid work on the strength of it.

**Change:**
- Hold the certificate and register entry until any flag on that session has been reviewed. Unflagged sessions can still release automatically at two working days.
- Add a written process for revoking a pass and removing a register entry, and for notifying the people who relied on that person's reports. Decide now who gets told.
- Make the review window shorter than ten days, or make release depend on it.

### 2. Nobody checks that the person on camera is the person who booked

Booking takes a name, a membership number and an email, and nothing verifies that the person booking is that member. At the exam, the candidate holds ID up to the webcam and the app saves a snapshot. That is a record, not a check. Nothing in the design compares the face to the ID, and the ID itself is not checked for forgery. A cheat does not need to defeat the software. The easiest attack is to hire a competent assessor to sit the exam as them. The paying candidate lends their real ID and the hired expert holds it up, or the candidate sits the first minutes and hands over. A photo of a photo, or a lightly edited ID, would also pass if no human ever looks at it.

**Change:**
- Have a trained person compare face and ID live before the exam unlocks. This is the single most useful use of the vendor's staff, if they offer it.
- Re-check the face at random points during the session, not only at the start. A mid-exam swap is otherwise invisible.
- Check that the booking name, the membership record and the ID agree, and that the membership is current, before taking £340.
- Keep the ID photo and a face from the session on file, and compare them in the review for every pass, not just flagged ones. A sample of a few percent of unflagged passes is a cheap way to find out how often the unflagged ones are wrong.
- Consider requiring in-person ID verification once, for example at the first attempt or at a partner site, so the register holds one verified face per assessor. That also helps later, when someone is signing reports in the field.

### 3. The timer pauses on any disconnection, with no limit

This is a gift to a determined cheat. Pulling the network cable, or killing the Wi-Fi, stops the clock and may stop the stream. During the gap the candidate can look up answers, ask someone, or let a helper take over, then reconnect with the clock still stopped. Because reconnections are unlimited, they can do this once per hard question. Your rural-broadband reason is real and a hard cap would punish honest people, but the current rule is open-ended.

**Change:**
- Pause the timer only while the connection is down, record every drop and its length, and put the total paused time on the session record.
- Cap the total pause allowance, for example at 10 to 15 minutes in all, with a reasonable number of reconnections. Past the cap, the clock keeps running. Candidates on poor connections can be offered a supervised sitting or a test centre instead.
- Treat several drops, or drops that cluster near difficult items, as flags that always get human review.
- Once a question has been shown, lock it so that a candidate who reconnects cannot return and change a previously viewed answer after a long break. Better still, stop the questions from showing at all during a reconnect.
- Make sure the app does not reveal the screen contents during the reconnect handshake, and test what actually happens on the candidate's screen when the stream drops.

### 4. The question bank is small and the exam window is three days long

Sixty from ninety means each candidate sees two thirds of the bank. With about 117 candidates a month on average, and a window that lasts from Friday 08:00 to Monday 08:00, the first sitters can pass the content to the rest over the weekend. A small group who each photograph or write down the questions they see will reconstruct nearly the whole bank within a few sittings. Shuffling question and answer order does not help much. Answers are remembered by content, not position, and a memorised answer text is easy to match. Failed candidates can also resit next month with more knowledge of the bank, and the first failure is itself a way to scout.

**Change:**
- Grow the bank substantially. Several hundred items is a more realistic target for an exam with real consequences, with the draw built from blueprint areas so the difficulty stays comparable.
- Shorten the window, or use fixed sittings so no one sees the paper long before others. If the weekend window stays, treat leakage during it as the main risk and plan for it.
- Track how often each question has been shown and retire or rotate the most exposed. Watch for questions that candidates answer unusually fast or all correct, and for answer text turning up online.
- Search the web and the usual forums and chat groups for your question wording after each sitting.
- Cap the number of attempts per person across all names, and watch for the same person booking under a second name or email.

### 5. The proctoring software sees only what the candidate lets it see

Looking away, a second voice, a second face are the easy cases. A determined cheat can:
- keep a second device or screen just outside the camera's view, or a phone behind the laptop
- run the app in a virtual machine, or share the screen to an accomplice who answers elsewhere
- use remote control software from another computer, or a hardware capture device so the locked machine shows only the exam while a second machine runs a search
- use an earpiece or smart glasses, which look like normal behaviour and make no sound the microphone picks up
- read a partner's whispered answers from a person sitting off-camera, with the candidate looking naturally at the screen

Flag-based detection also trains cheats to stay below the thresholds. It will miss quiet, practised cheating.

**Change:**
- Ask Tallyward directly how the app detects virtual machines, remote-control tools, second displays and capture hardware, and have your own people try each on a test account before signing. Make this a condition of the contract, with the results in writing.
- Require a room scan at the start and a second view of the desk, for example a phone camera placed at the side.
- Ask for the false-negative rate, not just what it flags. A vendor that cannot say how often it misses cheating has not measured it.
- Add a proper live proctor option for first attempts or for any candidate who wants to take the exam with fewer restrictions, as an alternative to a test centre.

### 6. The review stage is thin, and relies on trusting everyone involved

Two exam officers review every flagged session within ten working days. Rural broadband will produce many flags that are not cheating, and officers will gradually start to wave them through as the queue grows. Both officers and the vendor's staff can also see the ID, video and answers, so an insider is a possibility, and an insider can make a flag disappear or sell exam content. The vendor holds a large store of faces, voices and identity documents, which is both a data-protection obligation for you as the controller and a target for theft.

**Change:**
- Estimate the flag volume now. Run a pilot with, say, 100 sessions and see how many flags per session you really get, then check whether two people can keep up. Add a second reviewer for the high-severity categories so that no single person can clear a serious flag.
- Log every review decision, and have a sample of cleared flags re-checked by someone else.
- Require the contract to cover who at Tallyward can see recordings, how long they are kept, where they are held, breach notification, and deletion. Check your lawful basis for processing ID and biometric-type data.

### 7. Smaller points

- **Booking and payment.** Anyone can book with another person's membership number and email. A stolen card or a refund dispute is a lesser issue. Verify membership against your own records before the booking is accepted.
- **Automatic pass.** Because pass is decided by the system alone, a technical fault or a scoring error flows straight to the register. Keep a person in the release step, even a brief one.
- **Resit rule.** Failing candidates get one more try next month, with everything they remembered from the first. Consider a longer gap or fresh forms for resits.
- **Outage.** If Tallyward is down on the Friday or Saturday, you need a plan for the people locked out, since your policy is about connection drops, not vendor failure. Decide who can authorise a rebooking, so that a fraud attempt cannot disguise itself as an outage.

## Other ways it can go wrong without anyone cheating

- Honest candidates on weak connections are flagged or lose time, and complain or appeal. Have a clear appeals route before February.
- The app fails on some computers (older machines, corporate laptops that cannot be locked down, assistive technology). Decide what you offer disabled candidates and those who cannot install it.
- Differences in difficulty between the random papers make some candidates' 75% harder than others'. Check by analysing results after the first few sittings.
- A candidate loses power or the stream fails in the last minutes. Decide in advance how you treat a finished or half-finished paper.
- The window is in UK time and the app clocks may differ on a candidate's machine. Test the cut-off at 08:00 on Monday.

## What to do before signing, in order

1. Release passes only after review, and write the revocation process. (Policy change, days.)
2. Add human face-to-ID matching before the exam starts and at least one random re-check during it. (Contract term.)
3. Cap total pause time and treat repeated drops as flags. (Configuration, ask the vendor.)
4. Grow the bank, shorten the window or use fixed sittings, and watch for leakage after every sitting. (Content work, start now, because writing items takes the longest.)
5. Test the app yourselves against the list in section 5 and make the results part of the contract.
6. Pilot a hundred sessions to size the review workload and the false flags before the full intake.
7. Settle the data-protection terms with Tallyward.

If you want to keep the open weekend window and the remote format for convenience, the cost is that you accept more leakage and need more review. If you want the register to be trusted, give the highest-risk steps, identity and the first attempt, to a person who can see the candidate.

## What remains after these changes

Even with all of the above, a candidate with a skilled accomplice off-camera and a well-hidden second device can still get through a remote exam. You can make it expensive and likely to be caught, but not impossible. The residual defence is afterwards: random re-verification of registered assessors, a way for insurers and building owners to report doubts about a report, and statistical checks that look for strange score and timing patterns. Plan to use them.

## What I took from your message, and what to check first

I took it that you are the buyer with room to change the rules and contract terms, not only the technology, and that the register's standing is what matters most to you. I assumed the vendor's app does not already include live human ID matching, mid-session face re-checks or virtual machine detection, since you described only snapshots and flags. I also assumed that the booking site does not check membership against your own records and that nothing reverses a pass once issued. I did not know how many flags a session typically produces, how large the question bank could become, or whether the officers have time to review more. If any of those assumptions is wrong, the order above shifts a little, but not the top two items.

The first thing to check is what Tallyward actually does about identity and about virtual machines or second devices, because that decides how much of the cheating risk the contract can cover. The second is how many flags a realistic pilot produces, since that decides whether your two officers can do the review work.
