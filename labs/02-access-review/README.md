# Exercise 2: review access before approving it

Status: ready to try. No personal completion results have been recorded.

This is a paper exercise using fictional accounts. You do not need to change your computer's permissions.

## Scenario

A study group shares practice material. Learners need to read practice files. Tutors need to read practice files and the answer guide. The maintainer manages group membership and can read both resources. Only the maintainer needs permission to delete shared files.

Review this current access table:

| Account | Current job | Practice files | Answer guide | Delete shared files | Manage membership |
|---|---|---|---|---|---|
| Avery | Learner | Read | Read | No | No |
| Morgan | Tutor | Read | Read | Yes | No |
| Riley | Maintainer | Read | Read | Yes | Yes |
| Casey | Left the group | Read | Read | No | No |

## Your task

Before opening the suggested answer, list the permissions you would remove and explain each decision. Decide what should happen when a new account requests an action that has no allow rule.

Then consider a role change: Morgan becomes a learner. Which permissions should remain? Which access should be removed?

## Suggested answer

<details>
<summary>Open after reviewing the table</summary>

- Remove Avery's access to the answer guide because the learner task does not require it.
- Remove Morgan's delete permission because tutors do not need it.
- Riley's listed access matches the stated maintainer task.
- Remove Casey's access because Casey left the group. Check active sessions and any other access paths too.
- Deny requests without an explicit allow rule.
- When Morgan becomes a learner, retain practice-file read access and remove answer-guide access. Delete permission should already have been removed.

</details>

## Connect it to the concepts

Explain which part is authorization, how role-based access control could simplify this table, and why an account review is still needed even when roles are used.

A role change should update effective permissions. Adding a new role while leaving old grants in place can preserve access the user no longer needs.

## Record your own work

After completing it, describe one permission you changed, the task that justified your decision, and one question you would ask if the task requirements were unclear. There is no need to post real account names or access lists.

Read the [identity and access guide](../../study-guides/identity-and-access.md) for definitions and sources.
