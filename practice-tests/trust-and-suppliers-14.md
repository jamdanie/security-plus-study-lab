# Trust and suppliers 14

Six original questions. Partial SY0-701 1.2 (questions 1–3) and 5.3 (4–6). This targeted set is not a weighted mock exam.

[Zero trust guide](../study-guides/zero-trust.md) · [Supplier guide](../study-guides/third-party-risk.md) · [Contents](../study/contents.md)

Choose one answer before opening the explanations.

## Questions

1. A support employee passes MFA on a compliant laptop. Policy reserves payroll for payroll staff. What best meets the policy?
   - A. Allow because MFA succeeded.
   - B. Allow because the device is managed.
   - C. Deny because the role lacks payroll permission.
   - D. Allow after connecting to the office network.

2. In the NIST zero trust conceptual model, which component makes the access decision?
   - A. Policy enforcement point.
   - B. Policy engine.
   - C. Backup server.
   - D. Policy administrator.

3. A required device check changes from compliant to noncompliant during access. What response best follows a policy requiring compliance throughout access?
   - A. Keep access because the first login succeeded.
   - B. Grant a broader role.
   - C. Ignore the change on the internal network.
   - D. Reevaluate access and enforce the changed decision.

4. A customer needs restoration within eight hours. Which evidence most directly addresses the requirement?
   - A. A relevant recovery test and an agreed recovery commitment.
   - B. An availability percentage alone.
   - C. A confidentiality agreement alone.
   - D. A product logo.

5. A supplier gives a new subcontractor access to customer records. What should the customer do?
   - A. Stop all supplier reviews after purchase.
   - B. Review changed access, data flow, requirements, and evidence.
   - C. Assume the original questionnaire covers every future change.
   - D. Review only the new price.

6. The team needs proof it can retrieve usable records when leaving a service. Which action best addresses this?
   - A. Watch an import demonstration.
   - B. Check only that employees use MFA.
   - C. Test an export and evaluate its format against the exit requirement.
   - D. Read the supplier's marketing statement.

<details>
<summary>Answers and why each option succeeds or fails</summary>

1. **C.** The role does not permit payroll access. A verifies identity but does not assign permissions. B meets one device condition but does not create a role. D changes location without changing authorization.

2. **B.** The policy engine decides. A enforces the outcome. C has no access-decision role in this model. D establishes or terminates the communication path following the decision.

3. **D.** The stated policy requires reevaluation when the condition changes. A ignores that requirement. B expands permission without justification. C treats location as an exception the policy did not provide.

4. **A.** It addresses recovery capability and the agreed requirement. B concerns availability and does not establish restoration time. C concerns confidentiality. D provides no recovery evidence.

5. **B.** The changed relationship needs assessment against requirements. A ends oversight prematurely. C assumes evidence covers an unreviewed change. D ignores the changed security exposure.

6. **C.** An export test addresses retrieval and usability. A tests the opposite direction. B addresses identity verification. D is a claim without the requested demonstration.

</details>

## Use your result

Review correct guesses as well as errors. For each, write the requirement and why the nearest alternative fails. Change one condition and explain whether your answer changes.

References and supporting explanations are linked in the two guides. A score on six questions does not establish exam readiness.
