**Short answer:** Mirela is right about what has to go, and Anders is right about what has to survive. The finding says *standing write access*. It doesn't say engineers can never touch the database. Your logs show those are two different things, so you can close the finding by 31 January without taking away the incident-response path.

## What your numbers say

- **Standing write access is almost never used.** 310 of 14,200 sessions wrote anything (about 2%), and 270 of those were the on-call engineer during an incident. Taking standing write away removes a permanent exposure that is used about once a day on average, mostly in an emergency.
- **Reads are the bulk of the traffic, and nobody needs write to do them.** At least 91% of sessions were SELECT-only, mostly support checking transaction status. Those people don't need production credentials on the ledger. They need a way to see the data.
- **The incident writes are narrow and repetitive.** In 29 of 38 Sev-1 fixes (76%), the write was one of three statements: re-queue a stuck payout batch, release a settlement lock, or correct an FX rounding row. That's a short, known list, which means it can be packaged and reviewed in advance.
- **The remaining exposure is small.** About 9 Sev-1 fixes needed something outside those three. About 40 write sessions weren't on-call incident work, and I'd want to know what those were before Monday.
- **You already have a working model.** The proxy gives time-limited, logged grants for the card vault. Anders's objection is that those grants are slow at 3 am. That's a fixable design problem with the grant flow, not an argument against grants.

## Where each of them is right

**Mirela:** an auditor reading "any engineer can write to the ledger at any time" will not accept "we trust them." A payments processor needs to show that write access is granted for a reason, for a limited time, and is reviewable afterward. Her 31 January date is reasonable for the *standing write* part.

**Anders:** 38 of 41 Sev-1s fixed with direct database access, at a median of 22 minutes, is real operational value. If the replacement adds an approval queue at 3 am, the median goes up, and he's right that you risk both customer harm and losing senior engineers. Blanket removal, which is what Mirela's position says on its face, would do that.

The disagreement is partly about scope. Mirela is arguing against standing access and Anders is arguing against all access. Neither has said so, and a month of arguing suggests they're answering each other's headline instead of each other's actual position. Put both versions on one page on Monday and the gap gets much smaller.

## What I'd propose

**1. Remove standing write by 31 January, for everyone, including seniors and platform.** This is the part that closes the finding. Keep it simple and absolute so the auditors can verify it from the grant system.

**2. Give read access a different route.** Support and engineers read through a read replica or a masked, read-only view, and the proxy logs it. This covers the 91% of sessions that were SELECT-only and removes the need for any write credential in daily work. Check first whether the ledger has columns (customer identifiers, account data) that need masking. Reads of sensitive data may draw their own audit question.

**3. Turn the three common fixes into reviewed, pre-approved operations.** Re-queue payout batch, release settlement lock, and the FX rounding correction become parameterised runbook commands or stored procedures. Security and platform review them once, and the on-call engineer runs them with no grant request. Each run is logged with the incident ID, who ran it, and the before and after values. That covers 76% of the Sev-1 writes with almost no added time, and you can show the auditors exactly what can be done and that nothing else can.

**4. Make break-glass writes fast, but not free.** For the remaining ~24% (ad hoc fixes), use the grant mechanism the card vault already has, with changes to fix the 3 am problem:
- The grant is requested automatically when the engineer accepts the page or the incident is declared. It's ready before they open a terminal.
- It's auto-approved for the on-call engineer while a Sev-1 or Sev-2 incident is open, with the incident ID required.
- It expires in about 60 to 120 minutes, and every statement is logged.
- Optionally, a second engineer joins the session in the incident channel, or approves in one click. Don't make this a gate on the first minutes.
- A named person reviews every break-glass session within 1 business day. Unreviewed sessions are the thing auditors will look for.

**5. Measure it.** Track time to first write in incidents before and after, with Anders's 22-minute median as the baseline. Agree an acceptable ceiling now (for example, median under 30 minutes). If a step adds friction, you have data to fix it rather than another argument.

## What to tell them on Monday

To both: "The audit finding is about *standing write access to the ledger*. We're removing that by 31 January. We are not removing the ability to fix an incident. We're replacing standing access with three things: read-only access through a replica, pre-approved operations for the three fixes that make up most of our Sev-1 writes, and automatic, logged, time-limited access for everything else."

To Mirela: you get standing write gone on your date, and every remaining write tied to an incident, a person and a time window, with review. Ask her to agree to auto-approval during live incidents, since that's the one place the design gives up a pre-approval step, and to own the weekly review report.

To Anders: you keep the ability to fix anything in an incident, and the common fixes get faster because they need no grant. Ask him to own the grant flow and the runbook commands, and to commit to a measured response-time ceiling. If the numbers go the wrong way, you'll change the design.

## Things to check before Monday

- **What were the ~40 write sessions that weren't incident on-call work?** Migrations, data fixes and support one-offs need their own route (change ticket and scheduled grant), and they may be the easiest thing for an auditor to question.
- **What were the roughly 7% of sessions that were neither SELECT-only nor writes?** The numbers leave a gap, and it may just be sessions that ran other statement types. It's worth a quick look.
- **Will the auditors accept this design?** I'd send them the outline now, in December, rather than discover in April that "auto-approved during incidents" isn't enough for them. If they want a second approver, add it and measure the cost.
- **Dry-run it.** Run the new flow at 3 am with an on-call engineer in a game-day exercise, before the cutover, and use the result to settle the speed argument.

## What this doesn't solve

- Auto-approved break-glass is still a control based on review after the fact. It's weaker than approval before the action, and its strength depends on the follow-up review actually happening.
- The three pre-approved operations need maintenance. If a new class of incident fix appears, someone has to add it, or people will drift back to ad hoc grants.
- Attrition risk is real and a policy won't remove it. Anders's seniors will judge this by what 3 am feels like, so the game-day exercise and fast iteration matter as much as the design.

I'm fairly confident in the structure (roughly 80%). The usage numbers support it well. What I can't see is how the auditors will react and what's in the unexplained 40 write sessions, which is why I'd check both this week.
