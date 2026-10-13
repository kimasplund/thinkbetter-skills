I run operations for Corrabay Storage, nine self-storage sites. In November we replace padlocks with app-controlled smart locks at every site, and I'd like you to attack the design before we do.

- Tenants unlock their unit over Bluetooth with our app. The locks have no network connection of their own; they sync with our server through any Corrabay app that connects to them while the phone has signal. Many units are in basements with no signal, so each lock caches up to 50 credentials and accepts them offline.
- Tenants can add helpers by phone number. Helpers get the same unlock rights until the tenant removes them.
- When a unit changes hands, a helper is removed, or a tenant is overlocked for being 30 days late on rent, the change is pushed to the lock at its next sync.
- Every unlock is recorded by the app and uploaded at the next sync, which gives us a full access history for theft disputes and insurance claims.
- Site managers can generate a 24-hour maintenance code for any unit from the admin panel; it goes to their own phone.
- At 60 days delinquent, the site manager opens the unit and photographs the contents. Those photos become the auction listing and our record of what was inside.
- The front gate keypad takes a 6-digit PIN unique to each tenant. After 5 wrong entries it locks for 5 minutes. Our largest site has about 1,100 active tenants.

Our insurer wants a written security review by the end of the month. What breaks first, and what should we change?
