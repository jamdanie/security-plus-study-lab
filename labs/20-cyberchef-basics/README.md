# Exercise 20: encoding and hashing side by side

[Learning missions](../../resources/hands-on-missions.md) · [Cryptography guide](../../study-guides/cryptography-choices.md)

Browser activity using [GCHQ CyberChef](https://gchq.github.io/CyberChef/). Use only the supplied practice text. Ready to try; this project does not claim a completed browser run. Partial SY0-701 1.4.

## Make a prediction

Type exactly `hello` into Input, without a newline. Find and add the **To Base64** operation. Predict whether the output can be reversed without a secret key.

The expected output is `aGVsbG8=`. In a fresh recipe, paste that output into Input and add **From Base64**. It should return `hello`.

## Compare a digest

Clear the recipe and use `hello` as Input again. Add **SHA2** and select a 256-bit output if needed in your version. Record the digest. Compare it with the digest for `Hello`.

A case change changes the input bytes. With these two inputs, the SHA-256 digests differ. Keep the exact text and any newline behavior in your notes.

<details>
<summary>Explain the difference</summary>

Base64 changes representation and can be decoded without a secret. It does not provide confidentiality.

SHA-256 produces a digest. It has no corresponding decrypt operation that recovers arbitrary original input. You can still hash guesses and compare them; a digest does not make a predictable password safe.

Neither operation alone authenticates who created a message. A trustworthy reference matters when using a digest for integrity comparison.

</details>

## Bring it back to a question

A fictional team must send a confidential document. Someone proposes Base64 because the result looks unreadable. Explain why that fails and which requirement an encryption scheme would address.

Then try [Visual tools 15](../../practice-tests/visual-tools-15.md) and [the cards](../../anki/visual-tools.txt).

[Official CyberChef source and documentation](https://github.com/gchq/CyberChef). Operation labels may change. Do not place real passwords, tokens, or private files into this exercise.
