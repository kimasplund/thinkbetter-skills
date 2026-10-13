# Decision Record: Double-charging after config push

## Do this now (next 5 minutes)

1. **Roll back the config push.** It's the only recent change, the timing matches, and a revert is fully reversible. Do it first and investigate afterward.
2. **If the rollback can't be done in a couple of minutes, stop the charging another way.** Pause the webhook handler: disable the endpoint in the payment provider's dashboard, or flip a feature flag so the handler returns 200 without charging. Most providers retry failed or undelivered webhooks, so you can replay them later.
3. **Tell support now.** Post one line in their channel: "Known issue, double charges since about [time], fix in progress, do not issue manual refunds yet, we'll refund in bulk." This stops duplicate refunds and gives them something to tell customers.

## Constraints
- **Deadline:** Now. Each minute adds more duplicate charges, and each one is money taken from a customer.
- **Cost of delay:** More affected customers, more refunds and chargebacks, and more damage to trust.
- **Quality floor:** No new duplicate charges. Finding the root cause can wait.

## Options considered
1. Roll back the config. About 2 to 5 minutes, fully reversible. **Chosen.**
2. Pause the webhook endpoint or handler. About 1 to 2 minutes, reversible if events are queued or retried. This is the fallback, or you can do it alongside the rollback if the rollback is slow.
3. Hotfix forward by finding the bad setting and patching it. Slow and risky under pressure, and it isn't reversible if the guess is wrong. Rejected.
4. Do nothing and wait for more information. Rejected, because the harm grows every minute.

## How sure
I'm fairly confident, around 85%, that the config push is the cause, since the timing lines up exactly. What could make this wrong is a coincident change, such as a provider-side retry storm, a deploy by another team, or a delayed queue. So confirm the rollback worked instead of assuming it did.

## Verify within 5 to 10 minutes
- Check that new charges stop duplicating, using a query like "same customer, same amount, same order or event ID, charged more than once in the last N minutes".
- Watch the webhook error and retry rate and the queue depth.
- If duplicates continue after the rollback, the config isn't the whole story. Switch to option 2, pause the handler, and start diagnosing.

## Likely mechanisms to check afterward
- The config changed webhook retry or timeout settings, or the handler now responds slowly, so the provider retries and the handler processes each event twice.
- Idempotency is missing or broken: the idempotency key setting, event-ID dedupe, or a dedupe cache or TTL was altered.
- Two handlers or workers now consume the same events, for example a duplicated endpoint URL, an extra subscription, or a doubled queue consumer.

## Cleanup after the bleeding stops
- [ ] Pull the list of affected customers, meaning every duplicate charge since the push, and refund them in bulk. Don't make customers ask.
- [ ] Send a short proactive customer notice: what happened, that refunds are coming, and the expected timeline.
- [ ] Watch for chargebacks and disputes over the next few days, and flag the affected accounts to your payment provider if needed.
- [ ] Do a root cause analysis. Diff the config, reproduce in staging, and confirm which setting broke deduplication.
- [ ] Add durable protections: idempotency keys on charge creation, a dedupe check on event ID, an alert on duplicate charges per customer, and a staged rollout or canary for config pushes that touch payments.
- [ ] Write a short postmortem.

## Need a human?
If the rollback fails or you can't tell whether charges are still duplicating, escalate to whoever owns payments and call your payment provider's support line. Many providers can pause webhook delivery or help identify duplicate events.
