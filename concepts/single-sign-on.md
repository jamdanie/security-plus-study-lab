# Single sign-on and federation: follow the trust relationship

Single sign-on (SSO) lets a user access multiple services using an established sign-in session. Federation allows systems to rely on identity information across an agreed trust relationship.

| Term | Role |
|---|---|
| Identity provider | Authenticates the user and issues identity information |
| Relying application | Validates the relevant information and enforces local permissions |
| SAML | Security Assertion Markup Language, used for federation messages |
| OIDC | OpenID Connect, an authentication layer built on OAuth 2.0 |

OAuth 2.0 concerns delegated authorization; it is not by itself a complete user-authentication protocol. OpenID Connect adds identity information for sign-in.

Worked example: a business user signs in through a trusted identity provider but cannot open payroll. The federation exchange can succeed while payroll's authorization denies access.

SSO reduces repeated sign-ins; it does not mean every application grants the same permissions. Protect the central identity and validate the trust configuration.

Check yourself: explain what the application must still decide after receiving trusted identity information.

## Exam connection and review

Partial SY0-701 4.6 alignment. This short page does not complete the objective. [Review questions](../practice-tests/concept-review-10.md) · [Study index](../study/README.md).

## Source

[Primary documentation](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc). Examples are original and fictional.
