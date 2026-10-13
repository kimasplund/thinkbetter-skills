**Decision now: revert the config push first. Do not hotfix.** Every minute the webhook runs, more customers get double-charged, so stop the bleeding before you investigate.

**Next 5 minutes**

1. **Revert the config push** to the last known-good version. Config reverts are usually the fastest rollback you have. If the revert is slow or unclear, **pause the payment webhook handler or its retry/consumer** so it stops processing events.
2. **Confirm the double charges stop.** Watch the charge-creation rate and the webhook's duplicate-event count. If they don't drop within a few minutes, pause the webhook entirely and accept delayed payment confirmations over more duplicates.
3. **Tell support now.** Send a short holding message: "We've identified a payment issue affecting some customers, we've stopped it, and duplicate charges will be refunded." Don't promise specifics you haven't verified.

**Next 30 minutes**

4. **Scope the damage.** Pull every charge created since the config push that has a duplicate for the same order, invoice or idempotency key. This is your refund list.
5. **Decide on refunds.** Refund the duplicates through your payment provider, then reconcile against your ledger. Don't refund anything until you've confirmed the duplicate is real and not a legitimate second purchase.
6. **Find the root cause after the bleeding stops.** Compare the config diff against the change that enabled duplicate processing, usually a retry setting, a missing idempotency check, or a timeout that now triggers resends. Fix it properly before re-enabling the webhook.

**Assumptions:** the config push is the only change since the problem began, and a revert is available. If a revert isn't available, pause the webhook first and fix forward.
