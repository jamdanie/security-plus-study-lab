# Identity and access: who are you, and what can you do?

## Start with two questions

"Who are you?" is an authentication question. "Can you do this action on this resource?" is an authorization question.

A receptionist can successfully sign in to a clinic system and still be denied access to payroll. The successful login establishes neither a payroll role nor permission to open every record.

## Worked decision

An employee transfers from billing to scheduling. Scheduling needs appointment access but not billing exports.

1. Keep the person's identity unless the organization's process requires a replacement.
2. Remove billing-only grants, including inherited group access.
3. Assign the approved scheduling permissions.
4. Verify actual allowed and denied actions, rather than checking only the role label.

Resetting the password addresses a credential. It does not by itself remove old permissions. Deleting all access would stop the new job too. A permission review fits the stated change.

## Compare the close alternatives

| Situation | Relevant action |
|---|---|
| Password may be exposed | Follow credential and session-response procedures |
| Employee changes tasks | Review effective permissions and role membership |
| Employee leaves | Deprovision access and check sessions and other access paths |

More than one action may be needed in a real incident. Identify what the question actually establishes before choosing.

## Ready to move on?

Explain why a successful login can be followed by a denied action. Then describe how an old group membership could defeat a role change. Try the [applied questions](../practice-tests/applied-review-04.md).

Objective connection: partial preparation for SY0-701 1.2 and 4.6. [Coverage map](../study/exam-alignment.md).


Identity and access management (IAM) covers how identities and their access are created, used, reviewed, and removed.

Authentication checks a claimed identity. Authorization decides whether that identity can perform a particular action. Signing in successfully does not mean you should have access to every file.

For example, a student signs into a course site. The sign-in checks who the student is. The permission check determines whether that student can read course material or change someone else's grade. This is a made-up example, not a description of a particular university system.

## Least privilege and access models

Least privilege means giving an identity the access needed for its task. Review that access when the task or role changes.

| Model | How an access decision is organized | Practice example |
|---|---|---|
| Role-based access control (RBAC) | Permissions are assigned through roles | A tutor can read the answer guide; a learner can read practice files |
| Attribute-based access control (ABAC) | Policy evaluates attributes of the subject, resource, action, and environment | Allow an assigned tutor to read a class file only during an approved session |

A role or attribute only helps when the application actually checks the policy. Hiding a button does not enforce authorization. Check the requested resource and action on every request, and deny access when no rule allows it.

## Account lifecycle

Provisioning creates an account and assigns approved access. An access review checks whether the permissions are still needed. Deprovisioning removes access when it is no longer needed; depending on the system, that can include active sessions, tokens, and related accounts.

A shared account makes it harder to connect actions to a specific person. Separate identities improve accountability, provided logging and identity controls are in place.

## Check your understanding

If a former tutor can still open the answer guide after becoming a learner, the problem may be leftover authorization. Resetting a password alone does not remove those permissions.

Try the [access-review exercise](../labs/02-access-review/README.md). It uses a fictional permissions table and requires no administrator access.

## Sources

- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html): least privilege, access models, deny by default, and checking authorization on each request.
- [Textbook and project references](../resources/README.md). This is original supporting material, not copied textbook questions.
