Yes. Disabling the button as soon as it's tapped (and showing a spinner or "Submitting...") stops the second tap at its source, and it's a one-line change. Re-enable it only if the upload fails so the technician can retry.

If duplicates still matter after that, add an idempotency key to the completion request, because flaky field connections can also cause retries that a disabled button won't catch.
