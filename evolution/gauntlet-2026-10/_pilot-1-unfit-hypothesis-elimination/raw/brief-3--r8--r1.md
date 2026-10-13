**Short answer:** I wouldn't do either rollback yet. Your own numbers point away from both changes as the main cause. The best-supported explanation is the Android 5.2 billing change. Price may be a smaller, real second effect. You can confirm or kill this in a day or two with data you already have.

## What your data rules out

**The onboarding flow.** Control converts at 29.4% and the new flow at 28.7%. Both arms dropped by about 11 points from the 39-42% baseline, and they dropped together. A change that causes a drop can't show up equally in the arm that doesn't have it. The lower day-3 practice rate (52% vs 58%) is worth watching for retention, but it isn't what hit conversion. Killing the flow won't bring conversion back. If you want to stop the test, do it on the retention evidence, not as a conversion fix.

**Price as the whole story.** Brazil, India and Mexico had no price change, yet they fell from 33% to 20%. That is a 13-point drop, larger than the 10-point drop in the markets that did get the increase. Something other than price is hitting conversion everywhere.

**Price-driven refunds.** If people were trying the $10.99 plan and then asking for refunds, you'd see it on both stores, because the price went up on both. App Store refunds are flat. Play refunds went from about 20 to about 300 a week, and they started in the first week of September, right after the Aug 31 Android release. Your PM's reading doesn't fit the iOS side. A refund spike confined to one store points to something that changed on that store.

**iOS 7.4.** It shipped Sept 3 with a tuner feature, and App Store refunds are flat. Nothing so far implicates it.

## What fits best

The Android 5.2 billing library upgrade is the one change that matches every observation:

- It is Android-only, and Android is about 60% of trials, so it can move the blended number by a lot.
- It lines up in time with the Play refund spike.
- It would hit Brazil, India and Mexico as well as the priced-up markets.
- It would explain a jump in billing tickets, which are not all price complaints.

One concrete mechanism to check first: Google Play automatically refunds a subscription purchase that the app doesn't acknowledge within 3 days. A billing library upgrade that breaks or delays acknowledgment would produce exactly this pattern. Users get charged, the purchase isn't acknowledged, Play refunds it, and entitlement is lost or revoked. These look like failed conversions, high refund counts and confused billing tickets. Other Android billing failures could look similar, such as double charges, charges at the wrong time, or purchases not restoring.

For scale, 9,000 trials a month is roughly 2,100 a week. At 60% Android, that's about 1,300 Android trials a week. A rise of around 280 refunds a week is a large share of Android paid conversions, which is too big to be a few unhappy customers.

I'm assuming your trial is short enough that trials started through Sept 21 had mostly resolved. If the trial is 14 days or longer, the later September cohorts are not mature yet, and the 29% will rise a bit on its own.

## Where price probably still matters

I don't think price did nothing. US/UK/EU fell 10 points, and some of that is likely a genuine price effect. But the Android problem is confounded with it, and you can't read the price effect off the regional totals. The cleanest read is **iOS only, US/UK/EU, before and after Aug 28**. That group got the price increase but not the Android change. If iOS in those markets is down only a couple of points, price is a minor factor. If it's down 8-10, price is a major one and you have two problems.

## What to pull before the board meeting

1. **Conversion by platform, by region group, by week**, for trials started in July through September. This is the single most important cut. I'd expect Android to fall off a cliff starting with the first 5.2 cohort, and iOS to show a smaller drop.
2. **Android conversion split by app version** (5.2 vs earlier versions). Users who haven't updated are a natural control group. If conversion on old versions held at about 40% and 5.2 users convert far lower, that settles it.
3. **Play Console refund and order data**: refund reason, time between purchase and refund, and whether refunds cluster at about 3 days. Also check Play Console's Android vitals and subscription reports for unacknowledged purchases, and look at your server-side receipt or RTDN logs for acknowledgment errors.
4. **A sample of 30-50 billing tickets, read individually.** Your support lead's read of "price" may be right for some, but sort them into price complaints, charged-but-no-access, double charges and refund requests. Tagged "billing" lumps them together.
5. **The 5.2 diff in billing code**, specifically the purchase flow, acknowledge calls, and subscription status checks.

## What to tell the CEO

- **Don't kill the onboarding flow for conversion reasons.** It didn't cause the drop.
- **Hold the price rollback** until the iOS US/UK/EU cut is in. If Android billing is the main cause, rolling back the price would cost you revenue and not fix conversion.
- **Treat the Android billing issue as urgent now.** It is likely losing paying customers every day, and a fix doesn't have to wait for the board. If the data confirms an acknowledgment or entitlement bug, a hotfix release is the first action.
- **The cause statement for the board** should come from the platform-by-version cut. I'm reasonably confident the Android release is the main driver, but that is an inference from the pattern. The version split would turn it into a finding.

If the cuts come back and don't show an Android effect, then my explanation is wrong and I'd look again at the other possibilities, including a regional payment-method or tax change. But I'd run these checks before touching price or onboarding.
