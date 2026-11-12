# Exercise 6: choose a control and explain its limits

Status: ready to try. No learner completion results have been recorded.

These are fictional scenarios. No software installation or real keys are needed.

## Decide before opening the answers

For each scenario, choose hashing, encryption, a digital signature, or a combination. Explain what the choice does and what it does not establish.

1. You downloaded a practice file and have a trusted SHA-256 reference. You want to check whether its bytes match the reference.
2. You need to send a private document so that an unauthorized reader cannot read its contents.
3. A group publishes a public study guide. Readers should be able to check its signature using the group's trusted public key.
4. A document must remain private in transit, and its recipient must also be able to verify the sender's signature.

SHA-256 means Secure Hash Algorithm with a 256-bit output.

<details>
<summary>Suggested answers</summary>

1. Calculate the hash using the same algorithm and compare it with the trusted reference. This checks content consistency; it does not independently identify the author or prove that the file is harmless.
2. Use appropriate encryption and key management. Confidentiality does not by itself establish who wrote the document.
3. Use a digital signature. The signer protects the private key; readers verify with the trusted corresponding public key. The guide remains readable.
4. Use a properly designed system that combines encryption and digital signatures. Each serves a different requirement. Do not invent a custom cryptographic protocol for a real deployment.

</details>

## Challenge the conclusion

A signature verifies correctly, but the public key came from the same untrusted message as the file. What is missing?

<details>
<summary>Explanation</summary>

You have not established that the key belongs to the intended sender. An attacker can create a key pair and sign a file. Verification shows consistency with that key; a separate trusted identity binding is needed.

</details>

## Record your reasoning

After completing the exercise, choose the scenario that was hardest to classify. Explain the required property, your choice, and one limit of that choice.

[Read the guide and its sources](../../study-guides/cryptography-choices.md).
