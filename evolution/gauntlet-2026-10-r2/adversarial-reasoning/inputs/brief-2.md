I'm CTO at Kellsby Agritech. Our K3 controller runs irrigation valves and frost-protection sprinklers in vineyards and orchards, and about 5,200 are in the field. In spring, when a controller's temperature sensor reads below 1°C, it starts the overhead sprinklers by itself, and one missed frost night can cost a grower the season's crop. A large farm insurer will recommend us to its clients if we pass its security review, so please attack the design first.

- Controllers reach our cloud over cellular. Each authenticates with its serial number plus an API key that is the same on every unit and built into the firmware. We publish firmware images on our website so dealers can update units by USB.
- Every night at 02:00, each controller checks our update server, downloads any new release, verifies its signature against our public key, installs it and reboots.
- Dealers set controllers up over Bluetooth with our Field app. Controllers advertise as "K3-" followed by their serial number, so you can pick the right one out of a row. Setup mode needs a six-digit PIN: the last six digits of the serial, printed on a label inside the enclosure lid. In setup mode you can change thresholds, run valves and turn frost protection off.
- Growers manage their controllers in our web dashboard, which texts them when frost protection starts or when a controller has been offline for more than 30 minutes.
- When a farm changes hands, the new owner claims its controllers by entering their serial numbers in the dashboard. The previous owner gets an email, and the claim goes through after seven days unless they object.

Where would an attacker start, and what should we fix before the review?
