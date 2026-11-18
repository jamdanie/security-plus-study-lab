# Zero trust: decide access to the resource

[Contents](../study/contents.md) · [Exercise](../labs/16-zero-trust-decisions/README.md) · [Questions](../practice-tests/trust-and-suppliers-14.md)

Partial SY0-701 connection: 1.2, fundamental security concepts.

## What it means

An internal network address alone should not authorize access. NIST SP 800-207 describes zero trust without implicit trust based only on location or device ownership. Authentication and authorization still matter when someone is already inside the network.

## Work through an example

This fictional policy allows a technician to read assigned support tickets from a compliant managed device. It does not allow payroll access.

| Request | Decision under this policy | Reason |
|---|---|---|
| Assigned ticket, compliant managed laptop | Allow the permitted read | User, device, resource, and action meet policy |
| Payroll, same laptop | Deny | A compliant device does not grant a payroll role |
| Assigned ticket, device fails compliance | Deny pending remediation | The required device condition fails |

The policy supplies these outcomes. Zero trust does not require every organization to use this exact device rule.

## Terms that help

Authentication checks identity. Authorization decides permitted actions. Least privilege limits those actions to the work required.

In NIST's model, the policy engine makes the access decision. The policy administrator establishes or terminates the communication path. The policy enforcement point enables, monitors, and terminates the connection. A conceptual model can have these roles even when a product combines components.

The control plane carries access decisions and setup instructions. The data plane carries the resource traffic. Keeping the roles straight helps explain how a denied decision becomes a blocked connection.

## What people mix up

A VPN provides a protected connection; it does not establish that every application should accept every connected account. Multifactor authentication strengthens identity verification; it does not assign a payroll role.

Changing context can require reevaluation. This does not mean users must manually enter a password for every packet.

## Check yourself

An employee passes MFA on a managed laptop but requests a database outside their role. What should the access decision consider?

<details>
<summary>Worked answer</summary>

Check authorization for that database and requested action. Successful authentication and device compliance do not create permission. Under a policy that excludes this employee's role, deny access and record the decision.

</details>

## Reference

[NIST SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final), especially sections 2 and 3. The ticket scenario is original practice material.
