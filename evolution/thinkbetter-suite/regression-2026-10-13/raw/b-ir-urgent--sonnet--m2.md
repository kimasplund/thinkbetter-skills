Stop the bleeding first, diagnose second. Roll back the config push now.

**Next 5 minutes**

1. **Revert the config push.** The double-charging began right after it, so this is the most likely cause (I'd put it at ~85-90%). Reverting is fast, reversible and cheap. Don't spend time proving the cause before you do it. If a revert will take more than a few minutes, go to step 2 at the same time.
2. **If the revert is slow or doesn't stop it, pause charge processing.** Do one of these, whichever your system supports:
   - Disable the webhook endpoint or consumer.
   - Flip the feature flag that gates charge creation.
   - Pause the queue worker that handles payment events.

   Letting payment events pile up in a queue for a while is much better than charging customers twice. Most providers retry undelivered webhooks, so you shouldn't lose events.
3. **Name one incident lead.** One person decides and communicates. Everyone else executes.
4. **Confirm the fix worked.** Watch new charges for 5-10 minutes. The duplicate-charge rate should drop to zero. Check by looking at charges per payment or order ID, not just overall volume.

**While that happens, in parallel**

- **Support:** Post a short holding message and give agents a macro: "We've identified a billing issue affecting some payments. We are fixing it and will refund any duplicate charges automatically. You don't need to take any action." Don't promise timelines you can't keep. Don't tell customers to dispute charges with their bank. That creates chargeback fees and more work for you.
- **Stakeholders:** Send finance and leadership a one-line heads-up. They will get questions soon.

**Likely causes (for after you've stopped it)**

What did the config change touch? These are the usual suspects:
- **Retries/timeouts:** A shorter timeout or more retries means your handler is slow, the provider retries, and both attempts get processed.
- **Idempotency:** The idempotency key or dedupe check was disabled, changed or pointed at a different store.
- **Duplicate consumers:** The config registered the webhook twice, or the same queue now has two consumers, or the event is handled by two environments.
- **Wrong environment values:** A flag or URL pointing at the wrong place, so both old and new paths run.

Diff the config push against the previous version. In most cases that finds the cause in minutes.

**Once it's stopped (the next hour)**

1. **Size the damage.** Query for payments with two or more successful charges for the same order or payment intent since the push time. Export the list: customer, amount, charge IDs, timestamps.
2. **Refund the duplicates.** Do it in bulk and programmatically, keeping the first charge. Do a small batch first and check it before running the rest. Make sure the refund job is itself idempotent. Don't let it double-refund.
3. **Tell affected customers.** Send an email saying what happened, that a refund is issued, and how long it takes to show up (usually 5-10 business days on their statement). Fee reversals and overdraft effects may need extra goodwill handling.
4. **Check downstream side effects.** Duplicate receipts, duplicate fulfillment, duplicate credits, subscription state and accounting entries may all have been triggered twice.

**Afterwards (this week)**

- A blameless post-mortem. The questions: why did a config push reach production without catching this, and why did alerts not fire before support tickets did?
- Add an alert on duplicate charges per payment ID.
- Make charge creation idempotent at the payment level, so a bad config can't cause double-charging again.
- Stage and canary config changes to the payment path, with automatic rollback.

**Assumptions:** I don't know your stack or payment provider, so I've kept the steps generic. If you tell me what the config change contained, I can narrow down the cause. For now, revert first.
