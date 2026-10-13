Assumptions: neighbours in a shared area (a few streets to a small town), tools worth roughly $20 to $1,000, and an app that handles payments and messaging.

Several fields have already solved versions of this problem. Four of them map well.

| Field | What it does | What carries over |
|---|---|---|
| Tool libraries and public libraries | Lend physical items on trust, with few deposits | Reciprocity and social visibility keep most people honest |
| Car rental and pawn shops | Hold value against a loan | A deposit should scale with the replacement value of the item |
| Credit bureaus | Build a portable record from repeated completed transactions | Reputation should come from finished exchanges, not from ratings alone |
| Two-sided marketplaces (eBay, Airbnb) | Let both parties rate each other | Ratings get distorted by retaliation unless they are hidden until both sides have reviewed |
| Community-managed commons (Elinor Ostrom's work) | Small groups govern shared resources | Works through repeated contact, local monitoring and graduated sanctions |

**Design principles drawn from these**

1. **Scale the deposit to the tool, not to the person.** A cordless drill and a pressure washer carry different risks. Holding a deposit equal to replacement cost, or a fraction of it for trusted users, mirrors how rental cars work.
2. **Record condition at handoff and return.** Photos taken at both ends, with a timestamp, settle most damage disputes before they start. Rental companies rely on this for the same reason.
3. **Build reputation from completed loans only.** Count returns on time and in good condition, not stars. A new user should be able to unlock larger loans by completing smaller ones.
4. **Publish reviews only after both sides submit, or after a fixed window (say 14 days).** Without this, people hold back negative reviews to avoid retaliation, or write them in anger.
5. **Use graduated responses.** A late return triggers a reminder. Repeated lateness pauses borrowing privileges. Damage or non-return escalates to removal. This follows the commons approach rather than an instant ban.
6. **Show reputation locally first.** Display a user's history to people in their area or to mutual contacts. This recreates the social pressure that works in a neighbourhood, where people will see each other again.

**Where the analogies break down**

- Libraries and tool libraries rely on an institution to enforce norms. A peer app has to create that enforcement through deposits and sanctions.
- Ostrom's commons work because neighbours meet repeatedly. If your user base is spread across a city, local visibility will be thin, so the deposit and condition-recording rules will matter more.
- Tools are physical and expensive, unlike books. Losses are larger, so insurance or a small pooled damage fee is worth considering, similar to rental insurance.
- Credit-style scoring of people raises legal questions about data use and fair treatment, depending on where you operate. Check this before building a score that affects access to services.

**Suggested starting point**

Start with a trust tier. New users borrow low-value tools with a full deposit and photo check. Reputation from completed loans unlocks higher-value tools and smaller deposits. Use double-blind reviews, and make the sanctions graduated. Test the deposit amounts with a small group of neighbours before scaling up, since the right numbers depend on how often tools get damaged in practice.
