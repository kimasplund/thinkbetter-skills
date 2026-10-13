You can just push it. A full side-by-side comparison with judges is meant to catch changes in behavior, such as different wording that shifts tone, instructions, or how the model responds. Fixing "recieved" to "received" doesn't change the meaning, and any model reads both spellings the same way. A rerun would cost you time and tell you nothing.

A few quick habits so the fix stays low-risk:

1. Make sure the diff is exactly the one word. Check that nothing else in the prompt changed, including whitespace, quotes, or template placeholders.
2. Send one test order through the assistant after deploying. Confirm the confirmation message reads normally.
3. Keep the change in version history with a note like "typo fix, no behavior change". That way the last compared version stays your baseline.

If you later edit instructions, examples, or tone in the prompt, that is when the full comparison is worth rerunning.
