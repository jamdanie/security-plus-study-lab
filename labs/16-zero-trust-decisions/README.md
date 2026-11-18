# Exercise 16: explain an access decision

[Read first](../../study-guides/zero-trust.md) · [Contents](../../study/contents.md)

Offline fictional exercise. Partial SY0-701 1.2. Status: ready to try.

## Policy and requests

Support staff may read assigned tickets from compliant managed devices. Only payroll staff may read payroll. Devices failing compliance cannot access either resource.

| Request | Role | Device | Resource |
|---|---|---|---|
| A | Support | Compliant, managed | Assigned ticket |
| B | Support | Compliant, managed | Payroll |
| C | Payroll | Fails compliance | Payroll |
| D | Payroll | Compliant, managed | Payroll |

For each request, record allow or deny and the exact policy condition. Then explain why moving B onto the office network does or does not change your answer.

Finally, identify which component makes the decision and which enforces it in the NIST conceptual model.

<details>
<summary>Worked answer and checks</summary>

A: allow the permitted read. B: deny because the role lacks payroll permission. C: deny because the device fails a required condition. D: allow the permitted read.

B remains denied on the office network. This policy does not grant permission from network location.

The policy engine makes the decision; the policy enforcement point enforces the connection outcome. The policy administrator establishes or terminates the path.

Check that your explanation names the failed condition. “Zero trust blocks it” alone does not explain the difference between B and C.

</details>

## Save your result

Keep a four-row decision table and one paragraph explaining B. If you change the policy, label the new assumption and reevaluate the requests.

[Follow-up questions](../../practice-tests/trust-and-suppliers-14.md)
