# Exercise 10: assign responsibility before choosing a fix

Status: ready to try. This is an offline fictional scenario, with no cloud account or spending required.

A business uses a customer-managed virtual machine and a separate provider-managed document application. For this scenario, its agreement assigns guest operating-system patching to the customer, physical host maintenance to the provider, and document-sharing choices to the customer's tenant administrator.

## Review the findings

| Finding | What you need to decide |
|---|---|
| The virtual machine's guest operating system is missing a security patch | Who coordinates the patch? |
| A physical host needs a firmware update | Who maintains that layer? |
| A sensitive document folder permits public-link access | Which configuration needs review? |
| A former employee retains document access | Who handles the customer account's removal? |

Answer before opening the suggested analysis. Explain how you would verify the correction, not only whom you would notify.

<details>
<summary>Suggested analysis</summary>

The customer workload owner coordinates guest patching and verifies remediation and service functions. The provider maintains the physical host under the stated agreement.

The tenant administrator reviews public-link settings and removes unnecessary former-employee access. Verify effective access using appropriate allowed and denied checks. Do not assume encryption fixes an overbroad sharing rule.

The agreement makes these assignments explicit. In another service, inspect its terms and control boundaries before assigning the same duties.

</details>

## Change the requirement

The business moves from a customer-managed virtual machine to a platform where the provider explicitly manages the operating system. Which patching duty changes, and which data-access duties still need review?

Explain that the operating-system responsibility moves under the stated service terms. The customer's data-sharing and identity decisions still require attention.

[Guide and sources](../../study-guides/cloud-responsibility.md).
