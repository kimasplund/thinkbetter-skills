Just push it. A one-word spelling fix doesn't need the side-by-side comparison with judges.

That kind of testing is for changes that could alter how the assistant behaves, such as new instructions, a different tone, or reworded rules. Changing "recieved" to "received" doesn't change what the prompt tells the model to do. If anything, it removes a small risk, because the assistant might copy the typo into customer messages.

Before you push:

1. Check that the diff is exactly that one word and nothing else. Copy-paste or editor autocorrect can sneak in other changes.
2. Search the prompt for other copies of "recieved" and for other likely typos, so you fix them all in one go.
3. Send one test order confirmation after the push and check that the wording reads correctly.
4. Keep the old version handy so you can roll back if something looks off.

If you later make a real change to the prompt's wording or instructions, that's when the full comparison is worth rerunning.
