# Hashing, encryption, and signatures: choose the job first

## Start with the problem

Ask: "Do I need to keep this secret, check its contents, or verify a signer?"

A medical office sends a private report. Encryption addresses the need to keep its contents unreadable to unauthorized people. If the recipient also needs to verify the sender's signature, that is another requirement. The two protections can be combined.

For a software download, a hash comparison answers a narrower question: do these bytes match the trusted reference? It does not tell you whether the software is safe.

## Worked decision

A public update must remain readable to everyone. Readers need evidence that its signed contents came from the expected publisher's key.

1. The content is public, so secrecy is not the requested outcome.
2. A plain hash can compare bytes but does not establish the publisher.
3. A digital signature fits the integrity and origin requirement.
4. Readers still need a trusted binding between the verification key and the publisher.

Change the requirement to private delivery, and encryption becomes relevant. Choose from the requirement, not from a single keyword.

## Ready to move on?

Without looking, explain why a valid signature does not hide a document and why a hash from an untrusted source is not independent proof. Then try the [stronger scenario questions](../practice-tests/applied-review-04.md).

Objective connection: partial preparation for SY0-701 1.2 and 1.4. [See mapping and remaining gaps](../study/exam-alignment.md).


Start with what you need to protect. A file can be unreadable to outsiders, checked for changes, or signed by a particular key. Those are different goals.

| Need | Mechanism | What to remember |
|---|---|---|
| Compare a file with a trusted reference | Cryptographic hash | The same bytes and algorithm produce the same digest |
| Keep information unreadable without a key | Encryption | Authorized recipients need the appropriate decryption key |
| Verify a signature and detect signed-data changes | Digital signature | Sign with the private key; verify with the corresponding public key |

A plain hash does not identify who created a file. An attacker who can replace both a download and its reference hash can defeat that comparison. A digital signature adds a check tied to a signing key, but the verifier must also establish that the public key belongs to the intended signer.

A signature does not make the content secret. You can publish a document and its signature for everyone to read and verify.

## Symmetric and asymmetric

Symmetric cryptography uses a shared secret key. Asymmetric cryptography uses a public/private key pair. Systems often combine mechanisms instead of choosing only one.

| Name | Expansion | Classification |
|---|---|---|
| AES | Advanced Encryption Standard | Symmetric block cipher |
| RSA | Rivest–Shamir–Adleman, named for its designers | Asymmetric algorithm family used in appropriate encryption or signature schemes |
| SHA-256 | Secure Hash Algorithm with a 256-bit output | Cryptographic hash function |

RSA signing is not simply a general instruction to "encrypt with the private key." Use the signing and verification operations of an appropriate signature scheme.

## What nonrepudiation means here

A properly used signature supports evidence that data was signed using the private key corresponding to a public key. Connecting that evidence to a person depends on identity assurance and key protection. A stolen signing key complicates that judgment. Treat nonrepudiation as supported evidence, not a guarantee that disputes are impossible.

Try the [choose-the-control exercise](../labs/06-choose-cryptographic-controls/README.md), or revisit the [file-hashing walkthrough](../labs/01-file-hashing/README.md).

## Sources

- [NIST: Digital signature](https://csrc.nist.gov/glossary/term/digital_signature).
- [NIST FIPS 186-5: Digital Signature Standard](https://csrc.nist.gov/pubs/fips/186-5/final).
- [NIST: Non-repudiation](https://csrc.nist.gov/glossary/term/non_repudiation).

Original supporting notes. No textbook questions are reproduced.
