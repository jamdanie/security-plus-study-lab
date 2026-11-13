# Mapped scenario drill 3

Six original questions. This is targeted practice, not a domain-weighted mock exam or actual exam content. Select one answer and state the requirement that led you there before opening the explanation.

## 1. Access after a role change

Morgan moves from tutor to learner. Learners only need practice-file read access. What best implements that change?

A. Keep tutor access until someone complains.
B. Remove tutor-only permissions and verify effective learner access.
C. Give Morgan a shared administrator account.
D. Disable the practice files for the entire group.

<details>
<summary>Answer and objective connection</summary>

B. This item's primary alignment is 4.6. The requested action concerns permissions after a role change. A retains unnecessary access; C grants excessive shared access; D disrupts unrelated users.

[Review access](../study-guides/identity-and-access.md). Explain what inherited permissions you would check, not just the displayed role name.

</details>

## 2. Patch before closure

An exposed service has a confirmed vulnerability. A patch reports successful installation. What best supports closing the finding?

A. Delete the ticket immediately.
B. Change its severity to zero.
C. Check remediation and required service functions.
D. Stop collecting logs.

<details>
<summary>Answer and objective connection</summary>

C. Primary alignment: 4.3. The requirement is evidence of successful remediation. A and B change records without verification; D reduces visibility. Installation success alone does not establish closure.

[Review validation](../study-guides/vulnerability-management.md). Describe both a security check and an operational check.

</details>

## 3. Suspicious sign-ins

Four accounts fail login from one recorded source. One then succeeds. The records contain no attempted passwords or device assurance. Which statement is supported?

A. All four accounts are compromised.
B. Password spraying is proven.
C. The successful user is certainly legitimate.
D. The sequence merits investigation, but the cause is not established.

<details>
<summary>Answer and objective connection</summary>

D. Primary alignment: 4.9. The task is interpreting evidence. A and C assign control of accounts without evidence. B requires information about password attempts that is absent.

[Review logs](../labs/05-sign-in-log-review/README.md). Name additional evidence that could change your conclusion.

</details>

## 4. Match the containment goal

An affected workstation is communicating with other internal devices. The authorized response lead wants to limit spread while preserving useful evidence. Which action best matches that immediate goal?

A. Isolate the workstation using the approved response process and document the action.
B. Publish its files online.
C. Declare recovery complete.
D. Rebuild it immediately without evidence review.

<details>
<summary>Answer and objective connection</summary>

A. Primary alignment: 4.8. Isolation supports containment; documentation supports the response record. B discloses data; C declares an unsupported outcome; D can destroy evidence and skips the stated preservation constraint.

[Review response](../study-guides/incident-response.md). Isolation does not itself prove eradication.

</details>

## 5. The backup requirement

An outage occurs at 14:00. The latest usable data point is 13:00, and the recovery point objective is 30 minutes. What is the result?

A. The objective is met because the restore is fast.
B. The objective is missed by 30 minutes.
C. The objective concerns only downtime.
D. The schedule overrides the usable data point.

<details>
<summary>Answer and objective connection</summary>

B. Primary alignment: 5.2. RPO means recovery point objective. The data point is 60 minutes old, exceeding 30 minutes by 30 minutes. A and C confuse recovery point with time; D ignores actual usable data.

[Review recovery](../study-guides/backup-and-recovery.md). State separately what evidence you need to assess recovery duration.

</details>

## 6. Risk left after a control

A control reduces the likelihood of a loss, but does not eliminate the scenario. What best describes the remaining exposure?

A. A false negative.
B. Automatic avoidance.
C. Residual risk.
D. Guaranteed loss.

<details>
<summary>Answer and objective connection</summary>

C. Primary alignment: 5.2. Residual risk remains after controls. A concerns a missed finding; B implies avoiding the activity rather than reducing likelihood; D turns uncertainty into certainty.

[Review risk](../study-guides/risk-management.md). Identify who should review whether the remaining risk is acceptable.

</details>

## Use the result

Award one point per item for a raw total out of six. Also mark any correct guesses. Each objective has too few items to establish mastery; revisit the related exercise and explain a changed scenario.

Four items focus on operations and two on risk-related decisions. This distribution is intentional targeted practice, not a reproduction of the 28% and 20% exam-domain weights.

[Exam weights and mapping](../study/exam-alignment.md).
