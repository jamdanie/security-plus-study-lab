# Password storage: salt and work factor solve different problems

A service usually needs to verify a password, not recover its original text. Use a purpose-built password-hashing design rather than storing plaintext or relying on a fast file hash.

A salt is a unique value used with a password before deriving the stored result. It prevents identical passwords from necessarily having identical stored results and limits reuse of precomputed tables. The salt is not normally a secret.

A work factor makes each guess more costly. It must be chosen and updated with performance and security requirements in mind. Salting does not make a weak password unguessable; increasing work does not fix plaintext storage.

A pepper is an additional secret kept separately from the password database. It has its own key-management and recovery requirements.

Worked example: two people choose the same password. Different salts can produce different stored results, but an attacker can still test guesses against each record.

Check yourself: identify which requirement concerns uniqueness and which concerns cost per guess. Do not use the repository's file-hash checker as a production password-storage system.

## Exam connection and review

Partial SY0-701 1.4, 4.6 alignment. This short page does not complete the objective. [Review questions](../practice-tests/concept-review-10.md) · [Study index](../study/README.md).

## Source

[Primary documentation](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html). Examples are original and fictional.
