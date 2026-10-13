# Where a determined cheat gets through, and what to change

**Short answer: don't sign as designed.** The proctoring itself is reasonable. The weaknesses are in what surrounds it: the register is updated before anyone has looked at the evidence, the question bank is too small to survive a 3-day window, and the identity check can't tell a real candidate from a stand-in. All three can be fixed without changing vendor.

## The attacks, worst first

**1. The register publishes passes before the review that could stop them (critical)**
A pass is confirmed automatically after 2 working days. Flagged sessions are reviewed within 10. So a cheat who is flagged gets a certificate and a public register entry, and can hand over signed fire-door reports for up to 8 working days before an officer looks at the recording. Building owners and insurers rely on those reports, so a revocation after the fact means reports that need re-inspection, and a possible liability claim against you. Cheats don't need to avoid being flagged. They only need the review to be slow or inconclusive.
*Change:* Make a pass provisional until the session is cleared. A flagged session never auto-confirms. Unflagged sessions can auto-confirm, but add a random sample (say 10%) for human review before release. Also write down a revocation process: what the register shows, who notifies employers and insurers, and how an appeal works. Without one, you will hesitate to revoke when it matters.

**2. A stand-in sits the exam (critical)**
Your identity evidence is a name, membership number and email typed into a web form, plus one snapshot of ID held up to a webcam. Nothing in the design says anyone compares that snapshot with the membership record, checks the ID is genuine, or confirms the person at minute 60 is the person at minute 0.
- A qualified colleague or paid impersonator can book using the real candidate's details and show the candidate's ID, which is easy to obtain when the candidate hands it over. A photocopy, a screen image, or a lightly edited ID photo may pass the webcam test.
- The person can be swapped after the ID check.
- Membership numbers are often printed on certificates and sometimes appear in public directories. Anyone could book in someone else's name.
*Change:* Have a human (yours or Tallyward's) compare face to ID and to the photo on the membership record before the paper unlocks. Reject an ID that is held up but not tilted or moved to show it is a physical card. Require the payment cardholder name to match the booking. Run continuous face matching against the opening snapshot and treat a mismatch as an automatic hold, not just a flag. Consider a short live video check for first-time candidates.

**3. The 90-question bank leaks within a few sittings (critical)**
Each paper has 60 of 90 questions, so any two candidates share about two-thirds of their questions. Shuffling stops side-by-side copying but doesn't affect leaking. With about 117 candidates a month, each of whom memorises what they can, a group of cheats can rebuild most of the bank within a few cycles. Failed candidates can resit next month, which means a deliberate "scout" can sit up to twelve times a year, paid for by whoever buys the answers. A phone photograph of the screen is also enough to capture a question, since the app locks the computer but not a second device.
The 3-day window makes this worse. A Friday-morning candidate can pass questions to a Sunday candidate in the same cycle.
*Change:* Grow the bank to at least 300 and tag questions by topic so papers stay balanced. Track how often each question is shown, and retire or rewrite questions that become known (look for suspiciously high accuracy on hard items). Run fixed sittings (for example, three start times, each with its own paper) instead of a 3-day open window, or at minimum release a different subset of questions on each day. Limit resits: a cool-off of at least 3 months after two failures, and show no question-level feedback after the exam. Add a few "canary" questions seeded in different forms and watch for them in online forums.

**4. Unlimited pauses make the exam open-book (high)**
The timer stops whenever the connection drops and there is no cap on reconnections. A cheat can pull the cable (or just block the app), look up the answer, ask a friend, then reconnect. "Rural broadband" gives them an excuse every time. Total time at the desk is unbounded, so one candidate could spend hours on a 90-minute exam. During the disconnected period, nothing is streaming, so Tallyward has no evidence of what happened.
*Change:* Count every disconnect as a flagged event with timestamp and duration. Allow a small number (say 3), each with a maximum pause (say 5 minutes), and a cumulative cap (say 15 minutes). The app should keep recording locally during an outage and upload on reconnect, so there is a record of the gap. Give genuinely affected candidates a free rebook with a different paper, and offer a supervised test centre for those with poor connections, which also serves anyone who cannot meet the technical requirements.

**5. Second devices and a hidden helper (high)**
The app can see what the webcam shows. It cannot see a phone just outside the frame, a second monitor, an earpiece, notes beyond the camera's angle, or a person in the next room who doesn't speak. Software flags for "looking away" are easy to defeat once the cheat learns what triggers them: put the helper's screen directly behind the webcam. A virtual webcam or a capture card can feed a pre-recorded or edited video. A virtual machine or remote-control tool can run the exam while someone else drives the computer.
*Change:* Ask for a 360-degree room scan at the start, including the desk and surroundings, and a second view (phone as side camera) if budget allows. Have the app detect virtual cameras, VMs, remote-access tools and extra displays, and refuse to start. Ask Tallyward to describe, in writing, how it detects each of these. Run a trial where your staff try to cheat before you sign.

**6. Review capacity and insider risk (medium-high)**
Two officers reviewing every flagged session means a single point of failure, and also a pair of people whose decisions nobody else sees. If the flag rate is 15%, that is about 210 sessions a year, and more if the software is over-sensitive, which makes backlog likely. Backlog shortens each review. One officer being bribed or pressured is enough to clear a flagged session, and because the same two people also own the outcome, there's no check on them.
*Change:* Have a second reviewer on a random sample of cleared flags, with a written rule for what counts as a pass. Log every reviewer decision. Agree with Tallyward how many flags per hundred sessions you will tolerate, since a high flag rate is a risk too. Make "who reviews" independent of who is on the committee that handles appeals.

**7. The vendor's copy of your exam (medium)**
Tallyward streams every screen to its own servers. That means a recording of your questions and answers sits with a third party. A breach or a rogue employee there exposes the bank, and the webcam snapshots of ID cards are personal data you are responsible for.
*Change:* Put retention limits, access logging, breach notice terms and sub-processor lists in the contract, and delete session video after the appeal period. Check the data-protection terms for ID images.

## Edge cases to settle before February

- **The Monday cut-off:** What happens to someone who starts at 07:40 on Monday? Does the exam end at 08:00 or at 90 minutes? Pick one and test it, including how it interacts with paused time.
- **Time zones and UK clock changes:** A candidate working abroad or on the day clocks change could get the wrong window.
- **Vendor outage:** If Tallyward is down for part of the window, who decides who sits, and are the papers reissued?
- **Refund and chargeback abuse:** Candidates who fail and dispute the £340 payment.
- **Duplicate or multiple bookings:** The same membership number booking twice in a window, or booking for a friend and sitting both.
- **Accessibility:** Candidates who need extra time or screen readers, which interacts with the timer and with the app's lock-down.
- **Question quality:** With random draws of 60 from 90, some papers will be harder than others. A 75% pass mark will then pass and fail people unevenly. Check difficulty balance by topic.

## What to do before signing

1. Make a pass provisional until the session is cleared, and write the revocation process.
2. Add a real identity check against your membership record, and continuous face matching.
3. Grow the bank to 300 or more, shrink the exam window to fixed sittings, and limit resits.
4. Cap pauses and keep recording during outages.
5. Ask Tallyward for a written answer on virtual cameras, VMs, remote access and extra displays, and for a live test attack by your staff.
6. Add independent second review and tighten the contract on data.

## What remains afterwards

A person with an accomplice in the room, a good second camera, and the discipline to avoid the flagged behaviours can still get through a remote exam. So can a candidate who memorised a leaked bank. The goal is to make that expensive and detectable after the fact, not impossible. If a pass is a licence-like credential that insurers rely on, consider keeping a small supervised in-person option, plus a re-check of a sample of registered assessors' work in their first year.

**What I took from your message and assumed:** I took your numbers (about 1,400 candidates a year, 60 of 90 questions, 75% pass mark) as given, and assumed a flag rate of 10 to 15% because you didn't give one. I assumed Tallyward doesn't already match ID against your membership data, since you didn't mention it, and that membership numbers aren't secret. I assumed the register is public and live from the moment a pass is confirmed. **Check first:** how the register and certificates are triggered (can you hold them back for flagged sessions?), and Tallyward's real flag rate and virtual-camera detection in a trial run.
