I read your design as an attacker would. The most serious problems are that identity is never verified, the bank is too small to stay secret, and registration happens before anyone has reviewed the session. Assumptions: the 1,400 candidates a year are spread over 12 windows, so about 115 per window, and the "two working days" auto-confirm is a fixed rule with no hold.

## Where a determined cheat gets through

**1. Impersonation (the biggest hole).**
- Booking needs only a name, a membership number and an email. Membership numbers are not secret, and the register is public.
- The ID check is the candidate holding ID up to the webcam, with a snapshot saved. Nobody compares it to anything at the time. The snapshot is only useful if a human looks at it later, and nothing in your flow makes them.
- A hired expert can book as the candidate, hold up a card (a photo of a real ID, a forgery, or the candidate's own ID passed over in person), and sit the exam. The paying candidate can sit next to them off-camera.
- Remote-control software on the locked-down machine, or a second machine driving the first, defeats the "looking away" flags entirely.

**2. Question-bank exposure.**
- 60 from 90 means any two papers share at least 30 questions, and the average overlap is about 40. Two candidates comparing notes can reconstruct most of the bank.
- Over 12 windows, with about 115 candidates each, the bank is effectively public within a few months. Every candidate has a full 3-day window plus a screen stream to photograph with a phone. Shuffling options and order doesn't help, because the question stems are the same.
- Early starters on Friday can pass the content to Saturday and Sunday starters. The 3-day window makes this simple, because the exam stays open until Monday 08:00.
- A resitter sees another random 60 the next month, so failing is also a way to harvest the bank.

**3. Weak proctoring, which you can't see into.**
- Automated flags are easy to defeat. A phone, a second screen out of the camera's view, an earpiece, notes below the lens, and a helper who stays silent and uses text messages all produce no flag. Tallyward's flags need tuning, and you have no measured false-negative rate.
- Review happens within ten working days, but passes are confirmed in two. So a cheat is already certified, on the public register and issuing reports to insurers before anyone looks. The register is the thing people rely on, and you are using the slowest and weakest control on the fastest-moving step.
- Two officers reviewing every flagged session: at about 115 sessions a window, if the flag rate is even 30 to 50%, that is 35 to 60 sessions of 90 minutes of video each, so the review will either be skimmed or fall behind. Reviewers also become a single point to bribe or pressure.

**4. Reconnection abuse.**
- The timer pauses for as long as the candidate is disconnected, with no cap. A deliberate "drop" gives unlimited time to look up an answer, ask someone, or switch to another machine. With 60 questions in 90 minutes, a 20-minute "outage" repeated three times is a free hour of research.
- The pause also hides what happens while the stream is down. You will see a gap, not behaviour.
- A pause that costs nothing is also a way to carry on a conversation with a helper.

**5. Account and payment gaps.**
- Anyone can book using someone else's membership number and email, so you also have no assurance the person who paid is the person who sits. Chargebacks, stolen cards and resale of a slot are open.
- The app is installed by the candidate on their own computer. A virtual machine, a modified OS, or a screen-capture device (HDMI splitter) defeats lockdown. A second person can read the questions from the splitter output and send answers back.

**6. Operational and fairness risks.**
- The 3-day window means unsupervised conditions persist for 72 hours, with no one on hand to handle disputes or outages in real time.
- The fixed 75% pass mark on random subsets of different difficulty means papers aren't equivalent. A candidate who gets an easy draw has an advantage, and a challenge to a fail is hard to defend.
- Streaming webcam, microphone and screen to a third party is a data-protection issue (UK GDPR): you need a DPIA, retention limits, and a lawful basis. A breach would also expose ID images.
- Candidates on rural broadband are the legitimate users most hurt by tighter controls, so changes need to avoid punishing them.

## What to change, in priority order

**A. Stop certifying before review (cheap, do first).**
- Replace automatic confirmation with provisional results. Certificate and register entry follow only after the session has passed a check. For clean sessions with no flags and a verified identity, release in two days. For flagged sessions, hold until reviewed.
- Add a short appeals and revocation rule to the terms: you can withdraw a registration if misconduct is later found. This matters because insurers rely on the register.

**B. Verify identity properly.**
- Verify ID at booking, not only at the exam. Use a document check with liveness (a selfie matched to the ID by the vendor or a separate identity provider), and tie the booking to the membership record by something stronger than a number, for example a one-time link sent to the email held on the membership file.
- At the start, have a person (or vendor staff) compare the live face with the ID, and make a failed match stop the exam. Do a second face check mid-session and at the end, to catch a swap.
- Require a 360-degree room scan and a view of the desk and of the second-screen area. Ask for a side-on camera (phone as a second camera) if you want to catch the helper and the phone. This helps most for the impersonation and the notes problems.
- Compare the stored snapshot with the face on the register photo, and with the person who attends any later practical or CPD events.

**C. Fix the bank and the windows.**
- Grow the bank to several hundred questions, or generate parametrised variants, and draw so overlap between any two papers is small. Retire and rotate questions after a fixed number of uses. Add a few scenario questions that depend on a photo or document, which are harder to share by text.
- Shorten the window. Use fixed sessions (or a 24-hour window at most) with staggered start times, and accept a few more slots rather than a three-day open window. Forbid early starters from overlapping with late ones, so that nobody gets the same paper after someone else has finished it.
- Add a non-disclosure agreement to the terms, with the sanction of removal from the register. Run web and forum monitoring for leaked questions, and seed a few marked "canary" questions so a leak can be traced to a session.

**D. Limit reconnections.**
- Cap disconnections (for example 3 per session, 5 minutes each, 10 minutes in total), log each with a timestamp, and review every session that exceeds the cap before the pass is released.
- Add a "break the pause" rule: while the stream is down, the question on screen is hidden, and on reconnection the candidate gets a different question order position for unanswered items, so a drop cannot be used for lookup.
- For genuine rural-broadband cases, offer a documented alternative: a supervised test centre or a partner-venue sitting, so honest candidates with poor connections are not forced to choose between the cap and failing.
- Have the app record locally and upload afterwards, so a poor connection doesn't leave a blank in the evidence.

**E. Make proctoring evidence stronger and cheaper to review.**
- Ask Tallyward for measured detection rates against a red-team. Before you sign, run a pilot in which your own staff try the attacks above (phone, splitter, remote desktop, helper, VM) and see which are caught. Make this a contractual acceptance test, with termination rights if the vendor does not meet an agreed detection rate.
- Triage the flags by severity rather than reviewing all of them equally. Add a risk score (flags plus long disconnections plus unusual answer timing plus a pass from a first attempt with a very fast finish), and randomly audit a share of unflagged passes, so that a cheat who stays under the flag threshold still runs a risk.
- Add a third reviewer or a vendor-side first-line review so two officers are not the bottleneck, and rotate who reviews what.
- Use statistical analysis of answer timing and identical wrong answers between candidates to spot collusion.

**F. Booking, payments and data.**
- Require booking from a logged-in membership account, bind the slot to the verified person, make it non-transferable, and match the paying cardholder name to the candidate where practicable.
- Restrict the app to a managed configuration: detect VMs, remote-access tools and extra displays, and refuse to start if found. Be honest that this raises the cost of cheating rather than eliminating it.
- Complete a DPIA, publish the retention period (delete video once the appeal period ends), and make sure the vendor contract covers security, sub-processors and breach notice.

**G. Think about the stakes.**
- A pass here has real-world safety consequences, because registered assessors sign off on fire doors. Remote, unattended multiple-choice exams alone are a weak basis for that. Consider a layered model: the online knowledge test, plus a short live oral or video scenario interview with an examiner, or a supervised practical, before the register entry. That is the strongest single defence against an impersonator, since the person who passes the quiz also has to show the competence.
- Consider periodic re-verification or spot-check inspections of registered assessors' work.

## Suggested sequence before you sign

1. Change the terms: provisional results, revocation, NDA, reconnection cap.
2. Make Tallyward's contract conditional on a red-team pilot with agreed detection results.
3. Add identity verification at booking and a live face match at the start.
4. Shorten the windows and expand the bank before February. If the bank can't grow in time, run a smaller number of candidates through supervised sittings first.
5. Add the live oral or practical component for the register entry, at least for first-time candidates.

If you tell me the vendor's actual detection claims and how many questions you can write before February, I can help turn this into acceptance-test criteria for the pilot.
