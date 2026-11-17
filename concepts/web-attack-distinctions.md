# Web attacks: identify the interpreter and boundary

Structured Query Language injection (SQL injection) happens when untrusted input can alter a database query's intended meaning. Parameterized queries separate values from query structure.

Cross-site scripting (XSS) involves untrusted content executing in a browser in an application's context. Context-appropriate output encoding, safe framework features, and appropriate sanitization help address it.

| Scenario | First distinction |
|---|---|
| Search input changes database query logic | Investigate SQL injection |
| A stored comment executes script in another user's browser | Investigate stored XSS |

Both involve untrusted input, but the affected interpreter and defenses differ. Output encoding for a browser is not a substitute for query parameterization. A firewall can add protection without fixing unsafe application code.

Worked decision: a developer proposes adding input length limits to fix unsafe string-built database queries. Limits may be useful validation, but do not replace parameterized queries.

Check yourself: explain why a single rule to remove one punctuation character is not a complete defense. These are conceptual scenarios, not instructions to test a live service.

## Exam connection and review

Partial SY0-701 2.3, 2.4 alignment. This short page does not complete the objective. [Review questions](../practice-tests/concept-review-10.md) · [Study index](../study/README.md).

## Source

[Primary documentation](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html). Examples are original and fictional.

[OWASP XSS prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) supports the browser-side discussion.
