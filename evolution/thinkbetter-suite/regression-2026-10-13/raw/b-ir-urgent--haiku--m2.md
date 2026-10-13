Roll back the config push now. Don't debug first. Customers are being double-charged every minute this stays live, and reverting the config is the fastest way to stop new double charges.

Do these in order:

1. **Revert the config to the last known-good version.** If your config system supports instant rollback, use it. If not, redeploy the previous config. Confirm in logs that new webhook events stop producing duplicate charges.

2. **Pause payment capture on the webhook path if the rollback is not immediate.** Turning off the webhook consumer or switching the handler to "record only, don't charge" stops the bleeding while the rollback propagates. Stripe or your processor will retry webhooks, so pausing is safe as long as you process the backlog afterward.

3. **Stop the duplicates already in flight.** Pull the last 10 to 15 minutes of charges and group them by order or payment-intent ID. Any ID with more than one successful charge is a double charge. Refund the extra charges, not the originals, and keep a list of affected IDs.

4. **Check idempotency.** Confirm the webhook handler is deduplicating on the event ID. If the config change disabled or changed that check, the rollback restores it. If not, it is the next thing to fix.

5. **Tell support now.** Send a short holding message: a billing issue from a config change, duplicate charges are being refunded, and no action is needed from customers. Give support the list of affected IDs once step 3 is done so they can answer tickets with specifics.

After the bleeding stops, find out what in the config push caused the duplicate processing, and add a test or a check that catches that kind of change before it ships.

Assumptions: the config push is the cause (you said it started right after), and you can roll back config without a full code deploy. If a full code deploy is needed to roll back, the pause in step 2 matters more.
