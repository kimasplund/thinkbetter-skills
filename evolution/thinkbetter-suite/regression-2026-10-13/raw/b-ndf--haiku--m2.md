The trick is that the three asks are less opposed than they look. All three compete for one pool of Q3 engineering time, but each VP's real goal is different, and some of the work serves more than one of them. Here is how I'd get to a plan all three will sign.

**Assumptions:** one shared engineering team covers all three asks, the three features have a known revenue or account value, and cloud spend is roughly $X/month. Replace these with real numbers before you talk to anyone.

**1. Find what each VP actually needs**

- **Engineering (tech debt):** the underlying need is probably fewer incidents and faster shipping. Ask which debt items cause outages, slow releases, or block feature work.
- **Sales (three features):** the underlying need is keeping and winning specific accounts. Ask which customers are waiting, how much ARR is tied to each feature, and whether any deal has a hard date.
- **Finance (15% cloud cut):** the underlying need is margin and predictable spend. Ask whether the target is a run-rate or a fixed-dollar number, and by when.

**2. Where they overlap**

- Some debt work is also cost work. Unused services, over-provisioned instances, and inefficient data paths drive both incidents and the cloud bill.
- Some features depend on debt being paid first. If a requested feature touches a messy module, cleaning that module up is part of building the feature.
- All three want a platform that is cheaper to run and quicker to change.

**3. The real conflict**

It is a capacity conflict: Q3 has a fixed number of engineering weeks. That can be solved by sequencing and bundling, not by one side winning outright.

**4. Options to put on the table**

| Option | Engineering | Sales | Finance | Main risk |
|---|---|---|---|---|
| A. Debt first, features in Q4 | Strong | Weak; one or more deals may slip | Strong if the debt is cost-focused | Sales escalates |
| B. Features first, debt in Q4 | Weak | Strong | Weak; the cut is delayed | Engineering blocks |
| C. Split capacity by ratio | Medium | Medium | Medium | Each side gets less than it needs |
| D. Bundle: cost-focused debt first, then the features that depend on it | Strong | Medium to strong | Strong | Scope needs careful definition |

Option D is most likely to get all three to sign, because it converts the debt into cost savings and makes the features cheaper to build.

**5. Draft plan to test**

- **Q3, about half of engineering capacity:** debt work, starting with items that both cut cloud cost and reduce incidents. Target the infrastructure cleanup first.
- **Q3, the feature tied to the largest account:** built on the cleaned-up modules, so it costs less than it would have otherwise.
- **Q4:** the other two features, each with a committed date that sales can share with customers.
- **Cloud target:** 15% reduction measured on the bill. Infrastructure work in Q3 should deliver part of it. Set a checkpoint at the end of Q3 and assign the rest to Q4 if needed.
- **Tie-breaker:** name one person (CEO or COO) who decides disputes within a set time, so the plan does not get reopened every month.
- **Review:** a 30-minute check each month against the cloud bill, incident count, and feature dates. If the cost target is hit early, capacity shifts to features.

**6. Getting the signatures**

1. Meet each VP one-to-one before any group meeting. Show the draft and ask, "What would make you block this?" Fix those points first.
2. Share each VP's underlying need with the others, with their permission. Most people accept a plan more readily when they see that their concern was actually weighed.
3. Hold one 60-minute joint session to agree on the draft, not to start negotiating from scratch.
4. Put the final plan on one page, with the owner, dates, and review date. Each VP signs it. Aim for at least "accept" from all three, and "endorse" from the owner of each piece of work.

**Next steps this week**

1. Pull the list of debt items with their cloud cost and incident history.
2. Pull the three features with the accounts and ARR attached.
3. Get the cloud bill broken down by service so the 15% target has a clear baseline.
4. Book the three one-to-ones and send each VP the draft beforehand.
