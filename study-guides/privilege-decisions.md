# Least privilege and separation of duties

[Contents](../study/contents.md) · [Access exercise](../labs/31-temporary-access/README.md)

Partial SY0-701 4.6. A person can need an administrative action without needing permanent access to every administrative function.

| Concept | Decision it helps make |
|---|---|
| Least privilege | Which permissions are necessary for the assigned work? |
| Time-limited access | When should an approved temporary grant expire? |
| Separation of duties | Which sensitive actions require different responsible people or roles? |
| Access review | Does the existing grant still match the work and approval? |

The federal [Privileged Identity Playbook](https://www.idmanagement.gov/playbooks/pam/) discusses limiting privileged functions and duration, tracking accounts, and reviewing activity. These examples are original study scenarios, not federal policy requirements for every organization.

## Worked example

A technician must restart one lab service for an approved maintenance window. The fictional policy permits that action only during the window and prohibits approving one's own grant.

A broad permanent administrator role exceeds the stated task. An appropriately scoped, temporary grant better matches the requirement. Independent approval addresses the separate approval condition.

A short expiry does not fix an overly broad permission during its active period. A narrow permission does not satisfy a requirement for independent approval. Check scope, time, and approval separately.

## What authentication does not settle

Successful MFA verifies an authentication requirement; it does not decide which administrative actions a role may perform. A familiar employee can still hold a grant that no longer matches their job.

## Check yourself

Someone moves from support to payroll. Their old support-admin grant remains active. Does the new job automatically justify keeping it?

<details>
<summary>Worked answer</summary>

No. Review the current work, approvals, and remaining permissions. Remove grants that are no longer justified through the established process. The job change is a reason to review, not evidence that every old grant remains appropriate.

</details>

[Questions 19](../practice-tests/permissions-and-data-19.md) · [Cards](../anki/permissions-and-data.txt)
