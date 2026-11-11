# Exercise 5: what do these sign-in logs actually show?

Status: ready to try. No learner completion results have been recorded.

The [sample log](events.log) is fictional training data in a custom format, not output from a real system. All eight event timestamps use Coordinated Universal Time (UTC). The source labels stand in for recorded device identifiers and do not prove who operated a device.

## Review the evidence

Read the log and answer these questions before opening the suggested analysis:

1. Which source has failures involving four distinct accounts within 30 seconds?
2. Which account then has a successful login from that source?
3. Does the next event show a failed login or a denied resource action?
4. Can these records prove password spraying or an account compromise?
5. Which additional evidence would help you decide what happened?

## Suggested analysis

<details>
<summary>Open after reviewing the events</summary>

guest-device-1 has four failed logins: avery, morgan, riley, and casey. The next event records a successful login for morgan from that source.

The answer-guide event is an authorization denial. The successful login and denied action describe different decisions: identity verification succeeded, but the resource action was denied.

Failures across several accounts can justify investigating password spraying. However, these records do not show which passwords were attempted. They cannot establish whether the same password was used across accounts, whether a person mistyped credentials, or whether the successful session belonged to an attacker.

Check identity-provider records, multifactor authentication results, known device information, approved activity, and subsequent session actions. Multifactor authentication (MFA) uses factors from different categories. These sample records do not say whether it was required or completed.

avery's later failure followed by a success could be an ordinary correction, but that explanation is still a hypothesis. The log alone does not confirm it.

</details>

## Write a short finding

Separate your response into observed facts, possible explanations, and the next evidence you would request. A supported finding could say:

"One source recorded failed logins for four accounts in 30 seconds, followed by a successful login for morgan. A later request to read the answer guide was denied. I would investigate the source and successful session before deciding whether this was an account compromise."

This is an example answer, not a record of your completed investigation.

## What should stay out of logs?

Record useful event context, such as time, account identifier, action, and outcome. Do not record plaintext passwords, access tokens, or session secrets just to make an investigation easier. Restrict access to logs and remove private information before sharing real examples.

## Source and related study

- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html): security events, event context, and sensitive data exclusions.
- [Identity and access guide](../../study-guides/identity-and-access.md).
- [Original Anki cards](../../anki/sign-in-log-review.txt).
