# Multifactor authentication: count categories, not screens

Multifactor authentication (MFA) combines factors from different categories. A password and a personal identification number (PIN) are both knowledge factors; two prompts do not automatically mean two factors.

| Category | Example |
|---|---|
| Knowledge: something you know | Password |
| Possession: something you have | A registered security key |
| Inherence: something you are | A biometric characteristic |

A company asks for a password and a code from a registered authenticator. The design combines knowledge with possession when implemented correctly. Enrollment, recovery, and factor replacement must preserve that assurance.

An unexpected approval prompt is not evidence that you should approve it. Use a trusted reporting path. Recovery that removes the second factor after weak identity checks can undermine the original design.

Check yourself: explain why adding a second password is different from adding a security key. Then describe what the help desk must verify before replacing a lost factor.

## Exam connection and review

Partial SY0-701 4.6 alignment. This short page does not complete the objective. [Review questions](../practice-tests/concept-review-10.md) · [Study index](../study/README.md).

## Source

[Primary documentation](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html). Examples are original and fictional.
