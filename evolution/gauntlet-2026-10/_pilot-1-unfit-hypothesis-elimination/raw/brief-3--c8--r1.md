Don't make either change yet. The data you've given points away from both the price and the onboarding flow as the main cause. The strongest suspect is the Android 5.2 billing library upgrade.

**What the data rules out**

- **Onboarding flow:** Both arms are at about 29% (29.4% vs 28.7%). Both arms fell from 39-42%, so the test can't explain the drop. The lower day-3 practice rate is a separate engagement question to follow up. It didn't cause this conversion drop, and killing the flow won't recover it.
- **Price as the whole story:** Brazil, India and Mexico had no price change, yet they fell from 33% to 20%. That's a larger relative drop (about 39%) than US/UK/EU (about 24%). Something that isn't price hit all regions. The 8.99 to 10.99 increase is 22%. A 10-point drop on a 22% increase would be an unusually steep response, but it's possible.

**What fits the evidence**

The Play Console refunds went from about 20 a week to about 300 a week, while App Store refunds are flat. That points at the platform, not the price. Price-driven regret would show up on iOS too, and it doesn't. The Android 5.2 release on Aug 31 included the billing library upgrade, and the timing matches the first week of September.

Some candidate mechanisms:
1. Purchases aren't being acknowledged. Google automatically refunds subscriptions that aren't acknowledged within 3 days. This would give refunds, "billing" tickets, and users losing access.
2. Trial-to-paid conversion events aren't recorded correctly. Conversion could be undercounted rather than lost.
3. Users are charged but don't get entitlement. They would file billing tickets and refund requests.
4. Users are double-charged or charged at the wrong price.

Your support lead's read ("unhappy about the price") and your PM's read ("tried it, then wanted their money back after the price rise") are interpretations of the tickets and refunds. Neither has been checked against ticket text or refund reason codes.

**Likely picture:** an Android billing defect is the main driver, and the price increase probably contributes some in US/UK/EU. I'm inferring that from the evidence. I haven't confirmed it, and the checks below should settle it.

**Checks that take a day or two**

1. **Split conversion by platform and region.** Compare iOS, Android and web in each region, before and after. If iOS US/UK/EU fell only modestly while Android fell sharply everywhere, it's the platform. If iOS in US/UK/EU fell about as much as Android, price matters a lot there. Brazil/India/Mexico iOS is the cleanest control, since neither price nor Android changed.
2. **Split by app version.** Compare Android 5.2 users against users still on 5.1. This is the most direct test of the billing change.
3. **Read Play refund reason codes and sample 50 to 100 billing tickets.** Check how many mention a charge without access, a double charge, a failed purchase, or an error, and how many mention price.
4. **Check Play Console data** for unacknowledged purchases, subscription-cancellation reasons, and billing-related errors in Android vitals and logs.
5. **Look at timing.** Plot daily Android conversion against the 5.2 rollout percentage. A price effect would start Aug 28 on all platforms. A billing bug would start with 5.2 adoption.

**Recommendation for the board**

- **Don't roll back the price now.** If the cause is the billing bug, a rollback costs margin and doesn't fix the problem. Revisit it once the platform split shows how much the price contributes. If a price effect is real, a controlled test is better than a rollback, for example 8.99 vs 10.99 on iOS in the US.
- **Don't kill the onboarding flow because of conversion.** The data doesn't support it. Decide on it separately, based on the day-3 practice gap and retention.
- **If the Android billing defect is confirmed:** hotfix and roll out quickly, check that affected users have access, proactively refund or credit anyone wrongly charged, and tell support what to say.
- **Tell the CEO plainly:** "Our best current hypothesis is an Android billing issue, and we'll confirm it within a few days. The price likely explains part of the US/UK/EU drop, and we'll quantify how much."

**Assumptions**

I'm assuming the Brazil/India/Mexico trials are mostly on Android. I'm also assuming the 29% figure is the overall rate for trials that have had time to convert. Trials started late in the window may not have finished, which would lower the number slightly. Check that every cohort has had the full trial length plus the billing delay. It doesn't explain a drop this large.
