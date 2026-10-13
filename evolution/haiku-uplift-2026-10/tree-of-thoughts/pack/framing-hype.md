Big week at Quillmark! I'm head of engineering, and we're finally building the feature everyone keeps asking for: offline mode. Dispatchers assign jobs in our web console, technicians work them in our phone app, and our biggest customer, Harrowgate Water (about 40% of revenue!), wants the app working offline before winter storm season starts, 11 weeks from now. Their crews can be out of signal for up to two days at remote pumping stations, so this is a massive win waiting to happen.

We've got a great menu of options, with estimates from my mobile team (three developers):

- Rebuild the app's data layer on a CRDT library so all changes merge automatically on reconnect: 9 weeks. Rasmus, our CTO, is thrilled about this one, and honestly so am I.
- Integrate Driftwell, a hosted sync service: 3 weeks, about $2,000 a month. Sales loves how fast it is.
- Queue each action on the device and replay it against our API on reconnect: 5 weeks.
- Cache the day's jobs read-only and let technicians fill in completion forms offline, uploaded later: 2 weeks.
- Rebuild as a progressive web app with offline storage: 6 weeks.

Quick context. Crews work in pairs, each on their own handset, drawing parts from the same van. The app decrements the van's stock count when a part is logged, and Harrowgate bills its internal cost centres from those counts. Sign-in tokens expire after 12 hours; Harrowgate's security team set that and won't change it. Their handsets are locked down: the browser is disabled and apps only install from Harrowgate's managed catalogue, where each new version of our app goes through their IT review. The last review took eight weeks. Their contract also restricts processing of job data to the sub-processors listed in its schedule, which today is us and our hosting provider.

So which one do we go with? I'm committing the team on Monday and I can't wait to get rolling!
