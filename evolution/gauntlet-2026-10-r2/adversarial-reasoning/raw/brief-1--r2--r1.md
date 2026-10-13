Short version: the design has several holes a determined cheat can walk through, and the biggest are structural (the exam format and the timing of confirmation), not proctoring-software problems. I've assumed Tallyward's flagging is roughly as good as the industry norm, so I focus on what the design lets through even when the tool works.

## How a determined cheat gets through

**1. Question-bank harvesting (most serious).**
- 60 of 90 questions means any candidate sees two thirds of the bank. Three or four candidates who pool recall cover the whole bank within a sitting window.
- The exam is open for about 72 hours every month, so early sitters can pass questions to later ones. A leaked bank is also valuable because the register is public and carries commercial weight.
- Shuffled order and options only defeat naive answer-sharing. They do nothing against sharing question text and correct answers.
- Screen capture is the obvious route: a second device pointing at the screen, an HDMI splitter or capture card feeding another machine, or a phone photographing the screen just off-camera. Lockdown software only controls the machine it runs on.
- Fix: a bank of 90 is far too small for 1,400 candidates a year. Aim for several hundred items with variants, and retire and rotate exposed items. Track item statistics for items whose pass rate suddenly rises. Add a confidentiality agreement with real consequences.

**2. Impersonation and proxy sitting.**
- Booking needs only a name, membership number and email. Membership numbers are probably not secret, and nothing ties the booker to the person who sits the exam.
- The ID check is the candidate holding ID to the webcam and the app saving a snapshot. Nobody verifies it in real time. A stolen, borrowed, photo-edited or fake ID passes, and the snapshot is only looked at later, if the session is flagged.
- A proxy (an expert sitting for the candidate, with the candidate present as a face) is not caught by "looking away" or "second face" flags if the expert is the one on camera. Face-to-ID matching is the only control, and it is not live.
- Fix: live or near-live ID verification by a human or a certified automated check before the exam content is released, with face match against the ID and, ideally, against a photo captured at booking. Verify identity again at random points during the session. Bind the booking to a verified account, not just an email. Consider a requirement for employer or sponsor attestation.

**3. Remote access and virtual machines.**
- Another person can control the candidate's machine remotely, or the candidate can run the exam in a VM while an assistant works on the host. Remote tools and VMs are a known gap for lockdown apps. Streaming of the "screen" can also be a virtual display.
- Fix: require that the vendor detects VMs, remote desktop software and virtual cameras and microphones, and ask them for evidence on this, not a feature list. Require a room scan and a second-camera view (phone as side camera) so you can see the desk and the screen.

**4. Off-camera help.**
- A webcam cannot see most of a room. Earpieces, a person behind the monitor, notes beside the screen and a second monitor are all feasible. The software flags "looking away" and "second voice", but a quiet helper, a text channel, or a candidate who learns to keep their eyes forward will not trigger them.
- Fix: room scan at the start, 360 degree view, a second camera, and sensible rules on environment. Accept that remote proctoring is deterrence plus detection, not prevention.

**5. Timer pause on disconnect (exploit as a feature).**
- The pause with unlimited reconnections is a gift to a cheat. They can disconnect at will, look up an answer, or consult someone during a pause, and the clock stops. A flaky connection also makes the behaviour look legitimate. Nothing says what happens to the question on screen when the connection drops.
- Fix: cap reconnections (for example three) and cap total pause time (for example 10 to 15 minutes). Log every disconnect with reason, and flag sessions with more than a threshold. Allow candidates with documented connectivity problems to sit at a supervised test centre. Lock answered questions once the candidate moves on, and, on reconnect, show the same question rather than a fresh one.
- Rural broadband is a real access concern, so offer an offline-tolerant mode or a centre option rather than leaving the loophole open.

**6. Review comes too late and the pass is released automatically.**
- Passes are confirmed automatically after two working days, but flagged sessions are reviewed within ten working days. So a cheat can be on the public register, with a certificate in hand and reports signed, for up to eight working days before anyone looks at the footage. With ~1,400 candidates a year, a cheat who passes can sign inspection reports that insurers and building owners rely on.
- Capacity is a problem too. About 117 candidates a month, spread over three days, flagged sessions that average one hour each, and two officers reviewing within ten working days is possible, but AI flagging tends to produce many false positives, and a looser threshold means a backlog. Review quality will drop under volume. Reviewers should also not be the only control.
- Fix: do not publish a pass until any flagged session has been reviewed. Make the rule "no register entry until review cleared" and shorten the window to match, or hold all passes for the review period. Risk-rank sessions, and sample a random percentage of unflagged sessions to measure what the flags miss. Add a third reviewer or an escalation route.

**7. Predictable, exploitable booking and scheduling.**
- A single weekend window every month concentrates the load. Support issues, vendor outages and capacity pressure all land together, and the window is long enough for answer sharing.
- Fix: shorter fixed sessions, multiple sittings with different question sets (which also limits harvesting), and live proctoring slots for higher-risk candidates.

**8. Resits.**
- Failing and resitting next month gives a cheat unlimited probes at your bank, since each attempt shows 60 of the 90 questions. A failed candidate can record or memorise what they saw and return.
- Fix: limit the number of attempts per period, draw resit papers to minimise overlap with the previous paper, and treat repeat candidates as a risk factor.

**9. Process and data risks around the vendor.**
- You are sending video, audio and ID of 1,400 people a year to a third party. Check UK GDPR basis, retention, where data is stored, who at Tallyward can view it, and what happens in a breach. Also check accessibility and reasonable adjustments for disabled candidates, since lockdown software often causes problems here. Candidates can complain that false flags are unfair, so you need an appeals process and a documented evidence standard.
- Fix: a data processing agreement, retention limits, and a written appeals and misconduct policy before launch.

## What I'd change first, in order

1. Stop automatic registration while flagged sessions are unreviewed. This is cheap and removes the worst consequence (a cheat on the public register and signing reports).
2. Cap disconnects and total pause time.
3. Add real identity verification before the exam starts, and bind bookings to verified identities.
4. Enlarge the question bank, rotate it, and monitor item statistics.
5. Require VM, remote access and virtual device detection, plus a second camera or room scan.
6. Limit resits and make resit papers differ.
7. Sample unflagged sessions to see what the tool misses.

## Questions to put to Tallyward before signing

- Do you detect virtual machines, remote desktop and virtual cameras? Show test results.
- What are your false positive and false negative rates, and on what test data?
- Is identity verification live, and who does it?
- Can we pilot with deliberate cheating attempts (a red-team session) before going live?
- Where is the data stored, and for how long?

## Bigger point

Because the register is public and third parties rely on it for safety-related inspections, the consequences of a wrongly passed candidate are higher than for a typical exam. If you cannot get the controls above to a level you're comfortable with, consider a hybrid: online for the knowledge test with tighter controls, plus a short supervised practical or viva (in person or live video) before registration. That addresses the proxy and bank-leak risks together, because someone who did not do the work struggles in a live conversation about fire doors.

Assumptions: I don't know Tallyward's actual feature set, your current pass rate, or whether there is a practical assessment elsewhere in the route to registration. If there is one, the stakes of the online exam are lower than I've assumed.
