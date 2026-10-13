**Short answer: don't roll back the price or kill the onboarding flow yet. Your own numbers point at the Android 5.2 billing change, not at either of those. A day or two of data cuts will confirm or kill that before the board meets.**

## What your data rules out

**Onboarding is not the cause.** The test is a clean 50/50 split running over the same weeks, and the arms convert almost identically (29.4% vs 28.7%). Both arms fell to about 29%, so whatever hit conversion hit both. The lower day-3 practice rate (52% vs 58%) is a real concern about engagement, but it hasn't cost you conversion so far. Decide the flow on retention and longer-term revenue, separately from this question.

**Price alone doesn't explain it.** The decisive fact is Brazil/India/Mexico. Their prices did not change, yet conversion fell from 33% to 20%, a relative drop of about 40%. US/UK/EU, where prices did rise, fell from 41% to 31%, a relative drop of about 24%. If price were the driver, the unchanged markets should have held steady. Something else hit all regions, and it hit the unchanged ones harder.

The refund split points the same way. Both stores got the same price increase, but only Play refunds moved (about 20 to about 300 a week), and App Store refunds are flat. A price reaction would show up on both. Your PM's reading (people tried the paid plan and asked for their money back) doesn't fit that. Support's view that billing tickets are mostly about price may well be true of the tickets they read, but a rise from 12 to 50 a week is also what a billing malfunction would produce. Tagging tickets by platform and reading a sample will settle it.

## The leading explanation: the Android 5.2 billing library upgrade

- Android is about 60% of trials, so a problem there pulls the blended number down a lot. If iOS and web stayed near 41%, Android would have to be at about 22% to produce a blended 29%. That is a large but plausible Android-specific drop.
- Timing fits: 5.2 shipped Aug 31, and the September cohort is where conversion falls and Play refunds start.
- The mechanism fits. A billing library migration commonly breaks things like trial-to-paid transitions, purchase acknowledgement (Google auto-refunds purchases that aren't acknowledged within three days), duplicate or unexpected charges, or regional pricing and currency handling. Any of those would lower conversion and produce refunds in Play only. Brazil/India/Mexico could be hit harder if the new library handles regional price tiers or local payment methods differently.
- About 300 Play refunds a week is large against roughly 1,300 Android trial starts a week. That points to a systematic failure, not to a few people changing their minds.

The price increase probably does cost you something in US/UK/EU. It is likely a smaller part of the 10-point drop there than the blended numbers suggest, and it can't be measured until the Android problem is separated out.

## What to pull before the board meeting (about a day of work)

1. **Conversion by platform, by region, for Sept 1 to 21 vs. the prior baseline.** This is the key table. Prediction if I'm right: iOS and web are only modestly down (a price effect in US/UK/EU, little or none in BR/IN/MX), while Android is down sharply in every region. If iOS US/UK/EU is down just as much as Android there, the price matters more than I'm saying here.
2. **Android conversion by app version.** Compare users on 5.2 and on the older version, since not everyone updates at once. A gap between versions in the same period and region is close to proof, because the price is identical for both.
3. **Play refunds and the failed or abandoned billing events**, by reason code, app version and region. Look for duplicate charges, unacknowledged purchases and failed renewals. Ask engineering to check the billing logs for 5.2 errors at the trial-to-paid transition.
4. **iOS 7.4 (Sept 3).** Compare iOS conversion before and after that date. It's a lower-probability suspect, but it's cheap to rule out.
5. **Cohort maturity.** Check that the Sept 1 to 21 cohorts have had time to finish their trials. If trials last 7 or 14 days, the latest starts are still incomplete and are dragging the 29% down. Compare cohorts at the same trial age.

## What to tell the CEO

- Rolling back the price now is a guess that could cost real revenue. The price rise applies to the markets where you earn the most per user, and the data doesn't show it is the main problem. If the Android bug is the cause, a rollback would leave conversion down and give up about $2 a month per subscriber.
- Killing the onboarding flow would remove an experiment that shows no conversion effect.
- The faster and safer action is to ask engineering today to investigate the 5.2 billing path, and to check whether a hotfix is possible. If the cut by version confirms it, fixing it should recover much of the gap, and you can then read the true price effect from the iOS and web numbers. If the data says the price is a major factor after all, you will have clean evidence for a targeted decision, such as a smaller increase or a price test in one market.

**Confidence:** fairly high (roughly 75%) that Android billing is the main driver, based on the unchanged-price regions and the Play-only refunds. The size of the price effect is still unmeasured, and the platform-by-region table above is what will settle it.
