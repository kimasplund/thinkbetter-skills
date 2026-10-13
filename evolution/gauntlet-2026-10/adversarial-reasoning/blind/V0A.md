Give the vendor 30 minutes. Anything from 15 to 60 minutes is defensible, and 30 is a common middle choice.

Settings to ask for along with it:

- **Single use.** The link stops working as soon as it is used. Requesting a new link should also invalidate any earlier ones.
- **Random token, stored hashed.** The token should be long and unguessable (at least 128 bits), and the vendor should store only a hash of it.
- **Confirmation email.** Send members a notice after a successful reset, so they find out if someone else did it.
- **Sessions ended.** A reset should sign out any existing sessions.
- **Rate limiting.** Limit how many reset requests can be made per account and per IP address.
- **Same message every time.** The "we've sent a link if that account exists" message should read the same whether or not the email is registered.

Why 30 minutes: people usually click within a few minutes, and a link that sits in an inbox is a risk because mailboxes get shared, forwarded and compromised. If many of your members are older or not comfortable with technology, going up to 60 minutes is reasonable. I would not go past a few hours, and 24 hours or more is too long.
