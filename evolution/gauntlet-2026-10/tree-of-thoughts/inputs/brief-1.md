I'm head of engineering at Quillmark. We make field-service software: dispatchers assign jobs in a web console, and technicians work them in our phone app. Our biggest customer, Harrowgate Water (about 40% of revenue), wants the app to work offline before winter storm season starts, 11 weeks from now. Their crews can be out of signal for up to two days at remote pumping stations.

Options, with estimates from my mobile team (three developers):

- Rebuild the app's data layer on a CRDT library so all changes merge automatically on reconnect: 9 weeks. Rasmus, our CTO, is keen.
- Integrate Driftwell, a hosted sync service: 3 weeks, about $2,000 a month. Sales likes the speed.
- Queue each action on the device and replay it against our API on reconnect: 5 weeks.
- Cache the day's jobs read-only and let technicians fill in completion forms offline, uploaded later: 2 weeks.
- Rebuild as a progressive web app with offline storage: 6 weeks.

Some context. Crews work in pairs, each on their own handset, drawing parts from the same van. The app decrements the van's stock count when a part is logged, and Harrowgate bills its internal cost centres from those counts. Sign-in tokens expire after 12 hours; Harrowgate's security team set that and won't change it. Their handsets are locked down: the browser is disabled and apps only install from Harrowgate's managed catalogue, where each new version of our app goes through their IT review. The last review took eight weeks. Their contract also restricts processing of job data to the sub-processors listed in its schedule, which today is us and our hosting provider.

Which approach should we go with? I need to commit the team on Monday.
