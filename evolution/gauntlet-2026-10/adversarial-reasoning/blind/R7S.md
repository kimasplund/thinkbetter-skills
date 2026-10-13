Give the vendor 30 minutes. That is a sensible default for a member portal, and anything from 15 to 60 minutes is defensible.

Add these requirements so the number actually protects you:

- **Single use.** The link stops working once it has been used, and also when a newer reset is requested.
- **Random token.** It should be long and unguessable, at least 128 bits from a secure random generator. The vendor should store only a hash of it.
- **Short is fine.** Email can be slow, but members can just request a new link. Avoid anything over a few hours, because the link sits in an inbox that someone else might read.
- **Neutral wording.** The "request reset" page should respond the same way whether or not the email address exists.
- **After the reset.** Existing sessions should end, and the member should get a confirmation email.

I'm assuming a standard email-link reset with no extra verification step. If the portal holds sensitive data such as financial or personal records, use 15 minutes. If many of your members are not comfortable with email, 60 minutes is reasonable.
