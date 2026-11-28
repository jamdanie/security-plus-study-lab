# Exercise 44: review an automated change

[Change rehearsal](../23-change-rehearsal/README.md) · [Contents](../../study/contents.md)

Offline fictional exercise. Partial SY0-701 4.7. Ready to try. No executable script or live-system change is included.

## Proposed job

A scheduled job receives a list of device IDs and disables an unused service. The approved scope is lab-a and lab-b only. It should stop and report a scope error if any input device is unapproved. A preview must show intended changes before the approved run.

Input: lab-a, lab-b, production-c.

The proposed implementation says: “Use an all-systems administrator account. Ignore unknown IDs. Mark the ticket complete when the job starts.”

Identify the policy violation and missing checks.

<details>
<summary>Worked review</summary>

The input contains production-c, which is outside the approved scope. Under this exercise's stop rule, the job must report the scope error before changing any device.

Use only the permissions required for the approved task. Preview the exact targets and actions. Record approval, execution results, errors, and post-change verification. A start message does not establish that the job finished or that required service functions still work.

Ignoring unknown IDs conflicts with the stated stop-and-report requirement. A production implementation needs explicit failure handling and recovery behavior appropriate to its environment.

</details>

## Change the result

Suppose a later approved run completes lab-a but fails on lab-b. How should the result be recorded?

<details>
<summary>Changed answer</summary>

Record partial completion with per-device results. Do not mark the whole scope complete. Follow the approved retry or recovery process and verify the final state. Do not assume repeating a job is harmless; understand what repeated execution will do.

</details>

Draw input validation, preview, approved execution, and verification as decision steps. If a simulator lacks automation controls, keep this as an offline design review.

[Questions](../../practice-tests/evidence-and-automation-24.md) · [Learning notes](../../study/hands-on-notes.md).
