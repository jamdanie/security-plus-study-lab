# Exercise 42: check access after departure

[Identity guide](../../study-guides/identity-and-access.md) · [Contents](../../study/contents.md)

Offline fictional exercise. Partial SY0-701 4.6. Ready to try.

## Policy and records

The fictional organization requires all listed access paths to be revoked when a worker leaves. The review occurs after the departure time.

| Access path | Supplied status |
|---|---|
| Main identity account | Disabled |
| Independent local application account | Active |
| Physical entry badge | Active |
| Personal API token issued to the worker | Active |
| Shared service account used by a running application | Ownership and dependency review pending |

Identify the incomplete actions. The local application and personal token are explicitly independent of the main account in this scenario.

<details>
<summary>Worked review</summary>

The main account is disabled, but the independent local account, badge, and personal token still require revocation through the authorized process. Verify the resulting denial or invalidation with appropriate checks.

Review the shared service account's dependencies, ownership, and credential exposure before changing it. Remove the departing person's ability to use it and use an approved transition process. Do not blindly delete a running application's account.

Disabling one identity does not prove every independent path is closed. The table does not establish that the worker used any path maliciously.

</details>

## Draw the paths

Place the worker at the center and draw each listed access path. Mark its status and the next evidence needed. For the service account, show both the person and the application so the operational dependency is visible.

A simulator may not model tokens or identity lifecycles. Use the supplied records when it does not, and label the task as an offline policy review.

[Questions](../../practice-tests/maintenance-and-offboarding-23.md) · [Learning notes](../../study/hands-on-notes.md).
