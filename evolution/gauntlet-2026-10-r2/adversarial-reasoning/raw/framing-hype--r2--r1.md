Congratulations on the move online. Because a pass puts someone on a public register that building owners and insurers rely on, a successful cheat here is a safety problem as well as an integrity one. Below is how a determined cheat would get through, ordered roughly by how likely and how damaging each route is, followed by what I would change.

## How a determined cheat gets through

**1. The review happens after the pass is issued (the biggest structural flaw).**
Passes are confirmed automatically after two working days. Flagged sessions are reviewed within ten working days. So a cheat is certified, on the register, and signing fire-door reports for up to eight working days before anyone looks at the evidence. Your reviewers are also only seeing sessions the software flagged, so anything the software misses is never seen by a human. Revoking a certificate after the fact is also much harder (and more contentious) than withholding it.

**2. Impersonation: a proxy sits the exam.**
- Booking needs only a name, a membership number and an email. Membership numbers and emails are easy to obtain or are the candidate's own, so nothing ties the booking to a verified identity.
- The ID check is the candidate holding a card up to the webcam and the app saving a snapshot. Nobody compares it to the person on screen in real time, nobody checks the ID is genuine (a photo of someone else's ID, a printout or a fake all work), and nothing checks that the person at minute 60 is the person at minute 1. The classic attack is that the real candidate does the ID check and a more qualified friend takes over, or the proxy simply sits the whole thing with their own face and a borrowed or forged ID.
- Fire-door assessing is a trade with a small, networked community, so paid proxies and favours are realistic.

**3. Remote control and a second device.**
- Lockdown software can be defeated with a virtual machine, remote desktop software on a second machine, or a hardware capture or HDMI splitter that sends the screen to a helper who answers on a phone or earpiece. The proctoring app only sees what the compromised machine shows it.
- A helper out of camera view, a hidden earpiece, notes on a wall behind the monitor, or a second screen at an angle all defeat "looking away" detection if the cheat learns to keep their eyes on the screen. Software flagging of looking away and second voices also produces many false positives (rural homes, children, pets) and many false negatives (someone who is careful).
- Because the vendor's software decides what is "suspicious", a cheat can test the threshold in a lower-stakes setting first.

**4. Question bank exposure (the weakest part of the design).**
- Each paper is 60 questions from a bank of just 90, so every candidate sees two thirds of the entire bank. Shuffling order and options does not hide the content: it only makes screenshots slightly less convenient to share.
- With 1,400 candidates a year and an exam window of a whole weekend, the bank will be reconstructed fast. One candidate who memorises or photographs (phone aimed at the screen, a second camera, or a screen capture on a compromised machine) 60 questions gives the next candidate two thirds of their paper. A few colluding candidates cover the bank. Within a few sittings, answers will be on forums and messaging groups.
- Failing candidates can resit the next month, and they see a fresh sample of the same 90. A resit is effectively a free recon pass: sit, harvest questions, share, retake with the answers. Combined with the pass mark of 75% (45 of 60), memorising a reconstructed bank is enough.

**5. The long window makes collusion easy.**
The exam opens Friday 08:00 and can be started until Monday 08:00. That means early sitters can pass questions to later sitters across up to three days, in the same trade, on the same messaging groups. A single fixed sitting (or a small number of scheduled sittings) removes most of that value, while an open weekend gives colluders time to coordinate. Also, there is no one live to respond to problems over the weekend.

**6. Pause-on-disconnect with unlimited reconnections is an exploit.**
Because the timer pauses whenever the connection drops, and there is no cap, a cheat can deliberately drop the connection (unplug, toggle wifi) to stop the clock, look up an answer, ask a helper, or swap in someone else, and then reconnect. Each drop is plausibly blamed on rural broadband, and the software may not flag it. Your fairness intention for rural candidates is legitimate, but unlimited pauses also remove the 90 minute limit as a control, since the time limit is a major defence against looking things up.

**7. Weak controls around the account and the app.**
- No mention of multi-factor authentication or unique, single-use exam links, so credentials or the booking link can be shared.
- Candidates install the vendor app on their own computer, so you cannot trust the device. Anything the candidate controls, they may subvert.
- Pasting exam content into AI tools via a second device is now a trivial route for multiple-choice questions; the main control is that nobody else is in the room and the camera sees the whole desk and screen, which is hard to enforce remotely.

**8. Insider and process risks.**
- Two exam officers reviewing every flagged session within ten working days: if flag volume is high (1,400 candidates, with false positives that are common in remote proctoring), the officers will be overwhelmed, review quality will drop, and the ten day target will slip. A cheat benefits from noise.
- The vendor (Tallyward) holds video, audio, ID snapshots and screen content of 1,400 people a year. That is personal and biometric-adjacent data (UK GDPR, and a DPIA is likely needed), and a vendor breach, or staff misuse, is also a risk. Make sure retention limits, location of storage and sub-processors are in the contract.
- Fairness and accessibility: false flags can unfairly hit candidates with disabilities, neurodivergent candidates, those who look away to think, or those in shared homes. You need an appeals route and reasonable adjustments process, or you may face challenges.

## What I would change, in priority order

1. **Hold the pass until review is done.** Do not auto-issue. Issue certificates and register entries only after any flagged session has been reviewed and cleared. Make this a firm rule; if capacity is a problem, add reviewers rather than speed up the pass. Also add a documented right to revoke and a published sanctions policy.

2. **Fix identity properly.**
   - Verify identity at booking or before the exam using a live or automated ID document check with liveness (many vendors offer this), matched against the person on camera.
   - Have a live proctor (or at minimum a human check) compare the face to the ID at the start, plus periodic re-verification during the exam, and a final check at the end.
   - Consider requiring the candidate's employer or a verified sponsor, or requiring ID verification against an existing membership record, so that membership numbers alone can't be used.
   - Alternatively or additionally, offer or require sitting at an approved test centre for some candidates, or run a random sample of candidates through in-person or oral verification.

3. **Enlarge and manage the question bank.** 90 questions with 60 drawn is far too small. Aim for several times larger (several hundred), tagged by topic so each paper is balanced, and keep a rolling process to retire exposed questions and write new ones. Use item analysis to detect questions that are performing oddly (suspiciously high pass rates over time). Consider scenario-based and image-based questions about real door defects, which are harder to look up and are closer to the real job. Keep resits drawing from questions the candidate has not seen where possible.

4. **Narrow the exam window.** Use fixed sittings (several scheduled sessions, or a window of a few hours with a start time) so that late candidates cannot get answers from earlier ones. If flexibility is essential, make a large bank and variety compensate and accept a higher risk.

5. **Cap and log disconnections.** Allow a small number of reconnections (say two or three) with a maximum total pause (say five or ten minutes), have the app log each drop, and route extra drops to review. For candidates with a genuine connectivity problem, offer a fallback such as rebooking free of charge or sitting at a test centre, so you keep fairness without an unlimited pause. Flag any candidate with unusual drop patterns, especially if drops coincide with hard questions.

6. **Strengthen the environment checks.** Require a room scan and a view of the desk at the start, a second camera or phone view if you can afford it, and clear rules about a second person. Ask Tallyward directly about detection of virtual machines, remote desktop tools, screen capture devices and external displays, and ask for their independent test results. Treat the vendor's marketing as a claim to be tested.

7. **Test the vendor before signing.** Run a red team yourself: have a colleague attempt to cheat using each of the routes above (VM, second monitor, helper, proxy, deliberate disconnect) and see what is flagged. Put detection rates, review turnaround, data handling, accessibility and an exit clause into the contract.

8. **Use data and a second layer after the exam.** Look at timing patterns, answer similarity between candidates, pass rate by sitting time, and first attempt versus resit scores. Run a periodic audit where a sample of registered assessors are re-examined in person or by practical assessment. Since the real risk is someone unqualified signing fire-door reports, a practical or oral element is the most robust check of competence and is much harder to fake remotely.

9. **Governance.** Complete a DPIA, publish a clear candidate privacy notice, set an appeals and reasonable-adjustments process, and agree a revocation procedure with insurers and the register.

## Assumptions and one note
I have assumed the "75%" pass mark means 45 of 60, that Tallyward's flagging is largely automated, and that the register is publicly searchable. I do not know Tallyward's real capabilities, so treat my points on what it can detect as questions to put to them rather than facts.

If I had to choose only three changes: stop auto-issuing before review, verify identity with a real match and live checks, and enlarge the question bank while shrinking the exam window. Those close the largest and cheapest routes for a cheat. The online format is workable, but I would not sign until those are in place.
