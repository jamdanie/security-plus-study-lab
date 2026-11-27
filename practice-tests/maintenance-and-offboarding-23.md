# Maintenance and offboarding 23

Four original questions. Partial SY0-701 4.3 (1–2) and 4.6 (3–4). This targeted set is not a weighted mock exam.

[Visual session](../resources/maintenance-session.md) · [Contents](../study/contents.md)

## 1. The exercise prioritizes applicable, internet-exposed findings with confirmed exploitation. LAB-A meets both; isolated LAB-B has a higher severity label. Which follows the rule?

- A. Investigate LAB-A first.
- B. Ignore LAB-A because B has a higher label.
- C. Close both without checking.
- D. Treat all assets as equally exposed.

## 2. No exploitation evidence is supplied for a finding. What is supported?

- A. It cannot be exploited.
- B. It requires no follow-up.
- C. The evidence is missing; assess remaining risk.
- D. It is definitely a false positive.

## 3. The main account is disabled, but an explicitly independent local account is active. What follows?

- A. All access must already be revoked.
- B. Review and revoke the remaining path under policy.
- C. The worker is definitely malicious.
- D. A badge automatically disables it.

## 4. A shared service account supports a running application after a worker leaves. What is the best approach?

- A. Delete it without review.
- B. Keep the departing person's access forever.
- C. Assume disabling the main account rotates every secret.
- D. Review dependencies and ownership, remove the person's access, and transition through the approved process.

<details>
<summary>Answers and explanations</summary>

1. **A.** A applies the stated rule. B substitutes a label for the rule. C lacks validation. D contradicts exposure evidence.

2. **C.** C preserves uncertainty. A, B, and D assert conclusions the record does not establish.

3. **B.** B addresses the independent path. A assumes a dependency absent from the scenario. C invents intent. D invents automation.

4. **D.** D addresses security and the service dependency. A risks an unreviewed outage. B preserves unjustified access. C assumes behavior not supplied.

</details>

Review correct guesses too. State the deciding evidence and explain the nearest alternative before trying a changed condition.
