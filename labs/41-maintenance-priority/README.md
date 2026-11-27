# Exercise 41: choose the next maintenance action

[Findings](findings.csv) · [Vulnerability guide](../../study-guides/vulnerability-management.md)

Offline fictional exercise. Partial SY0-701 4.3. Ready to try. Identifiers and severity labels do not refer to real products or vulnerabilities.

## Decision rule

The owner asks you to investigate applicable findings with confirmed exploitation and internet exposure first. Then assess other findings using exposure, business impact, and technical severity. Do not ignore a finding simply because it falls later in the queue.

Which record goes first under that rule? What should you verify before proposing a change?

<details>
<summary>Worked decision</summary>

LAB-A goes first because the supplied evidence meets both priority conditions. LAB-B's critical label does not override the rule by itself.

Verify the affected asset and version, whether the finding applies, current exposure, approved treatment options, dependencies, and the change/rollback plan. The dataset supports a priority decision; it does not prove that a patch has been applied or that the asset is already compromised.

No exploitation evidence was supplied for B or C. That is not proof they cannot be exploited. Assess their remaining risk and schedule follow-up.

</details>

## Change the evidence

Suppose LAB-A is verified not applicable to the installed version. Document that evidence and reassess the queue. Do not preserve a priority solely because an earlier record said it was urgent.

CISA encourages risk-based prioritization using known-exploitation information: [official CISA bulletin](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/42dab68). This exercise's queue rule is invented and is not a federal remediation deadline.

Draw each asset's exposure boundary, then annotate the evidence beside it. [Review questions](../../practice-tests/maintenance-and-offboarding-23.md).
