**Short answer:** Don't roll back the price or kill the onboarding flow yet. The data you've given argues against both as the main cause. The strongest lead is the Android 5.2 billing library upgrade. You can confirm or rule it out with a few cuts of data you already have, well before the board meets.

**What the evidence says**

1. **Onboarding is effectively cleared.** Control converts at 29.4% and the new flow at 28.7%. Both arms dropped together, so whatever happened hit everyone. The lower day-3 practice rate (52% vs 58%) is a real retention concern, but it isn't what moved trial-to-paid. Judge the flow on its own merits, such as retention and day-30 outcomes. Don't kill it as a conversion fix.

2. **Price can't be the whole story.** Brazil, India and Mexico had no price change, yet they fell from 33% to 20%. That is a drop of about 40% in relative terms. US/UK/EU fell from 41% to 31%, about 24% in relative terms. If price were the driver, the unchanged markets should be flat. Something else is hitting them, and hitting them harder.

3. **The refund pattern points at Android, not price.** Play refunds went from about 20 to about 300 a week, while App Store refunds are flat. A price increase applies to iOS users in the same regions, so it should show up there too. A problem that only appears on the Play side suggests something specific to Android. That fits the Aug 31 release, which included the billing library upgrade. Android is 60% of trials, which is enough to drag the blended number down a lot.

4. **A billing problem could look like a price complaint.** Billing tickets rose from about 12 to about 50 a week. Your support lead reads them as price complaints, but that is an interpretation. The same tickets could be double charges, charges after cancelling, failed purchases, or "I was charged and have no access". Those lead to refunds and abandoned conversions. The PM's reading of the refunds ("they tried the paid plan and wanted their money back") is also unproven. Refunds can just as easily be people charged unexpectedly or incorrectly.

5. **The regional pattern fits a billing library issue.** Brazil, India and Mexico rely heavily on local payment methods such as Pix, UPI, carrier billing and boleto, and a billing library upgrade can break those. I'm assuming those markets are Android-heavy, which you should check.

**My ranking of the causes**

- **Most likely:** a billing or purchase-flow regression in Android 5.2, with the price increase as a smaller, real contributor in US/UK/EU.
- **Plausible but partial:** the price increase. It probably explains some of the US/UK/EU decline, especially on iOS.
- **Unlikely:** the onboarding test, given the equal arms.
- **Unlikely:** the iOS 7.4 release. App Store refunds are flat, and I haven't seen anything iOS-specific. Confirm with the split below.
- **Check:** a measurement artifact. Trials that started Sept 1-21 may not have finished their trial window when you pulled the number. If late-September starts are still pending, conversion looks lower than it will end up. The previous six months may have been measured on fully matured cohorts. Compare like for like. Also check whether the 5.2 billing change altered how trial conversions are recorded or attributed.

**How to confirm in the next few days**

1. **Break conversion out by platform x region group (about 6 cells), and by app version on Android (5.1 vs 5.2).** This is the most decisive cut.
   - If iOS US/UK/EU fell only slightly while Android fell sharply, the cause is Android.
   - If Android users still on 5.1 convert normally and 5.2 users don't, the billing upgrade is the cause.
   - iOS in US/UK/EU is your cleanest read on the pure price effect.
2. **Check Play Console and billing logs for 5.2.** Look at purchase error rates, failed or pending transactions, double charges, and the success rate by payment method and country.
3. **Read 30-50 billing tickets and the Play refund reason codes yourself.** Tag them as price, charged-in-error, can't-access, or cancel-failed. This replaces opinion with counts.
4. **Compare refunds by app version and by days since the charge.** A spike concentrated in 5.2 and in the first day or two after purchase suggests a billing defect.
5. **Re-run conversion on matured cohorts only**, so the comparison is fair.

**What to do before the board**

- If Android 5.2 is the culprit, fix or hotfix the billing flow, or roll back the billing library change if the store allows it. Proactively refund and message affected users. This is likely to recover the most conversion.
- Hold the price decision until you have the iOS US/UK/EU read. If that cut shows a clear drop, consider a proper price test rather than a blanket rollback. A rollback also loses revenue per paying user. If conversion falls 25% and price rises 22%, the gross effect on revenue is close to neutral, so the price change is not obviously a loss.
- Let the onboarding test run to its planned end and decide it on retention and downstream metrics.

**What to tell the CEO now:** "Conversion fell about 10 points. The data we have doesn't support price or onboarding as the main cause. The unchanged-price markets fell the most, the two onboarding arms are equal, and the refund spike is Android-only. Our leading hypothesis is a billing regression in Android 5.2, with the price increase contributing a smaller share. We'll confirm with a platform and version split by [date], then decide on the price and the fix."

**Assumptions I made:** I don't have the platform-by-region numbers, trial length, or ticket text. The reasoning above is a diagnosis from the pattern, not proof. The splits in step 1 will tell you quickly if I'm wrong. If iOS conversion fell as much as Android's, the price increase moves up the list and my ranking would change.
