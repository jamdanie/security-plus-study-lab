# Exercise 12: match the control to the requested outcome

Status: ready to try. Fictional offline exercise.

A small office wants to restrict unauthorized server-room entry and review attempted access.

## Separate the components

1. A locked cage physically prevents access to equipment.
2. Software records a denied badge attempt and sends an alert.
3. A policy requires approval before badges are issued.
4. Staff verify an approved request against an identity checklist.
5. A notice warns visitors against unauthorized entry.

For each component, identify its implementation category. Then describe its intended purpose without assuming that it performs other functions.

<details>
<summary>Suggested analysis</summary>

1. Physical and preventive in the stated role.
2. Technical and detective; the described recording and alerting do not themselves block entry.
3. Managerial and directive: it establishes required behavior.
4. Operational: people carry out the process. Its verification step supports preventing unauthorized issuance.
5. Physical in its presentation and deterrent in its stated function. If it also states a mandatory rule, that wording can have a directive role; the prompt here emphasizes warning.

A real badge system can contain preventive mechanisms too. The exercise asks about the separate components described.

</details>

## Explain a limit

Would adding only the alert satisfy a requirement to prevent entry? Explain why detection and prevention are different outcomes, and identify which component you would verify for the blocking requirement.

[Guide and sources](../../study-guides/security-controls.md).
