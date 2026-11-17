# Certificates: a trusted issuer is only one check

Transport Layer Security (TLS) uses certificates in typical web-server authentication. A client needs to validate the presented identity and trust configuration, not merely notice that a certificate exists.

Checks include the requested hostname, validity period, trust chain, and applicable revocation or status handling. A certificate for a different hostname does not become suitable because its issuer is trusted.

Worked example: you request payroll.example and the server presents a certificate for files.example. Investigate the mismatch through a trusted support route. A configuration mistake is possible; the warning alone does not prove an attack.

A certificate carries a public key and identity-related information. Protecting the corresponding private key remains essential. A successful TLS connection does not prove the application's content or business practices are trustworthy.

Check yourself: explain why the padlock does not grant permission to every file, and why a valid date does not resolve a hostname mismatch.

## Exam connection and review

Partial SY0-701 1.4 alignment. This short page does not complete the objective. [Review questions](../practice-tests/concept-review-10.md) · [Study index](../study/README.md).

## Source

[Primary documentation](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html). Examples are original and fictional.
