# Cloud security: who is responsible for this setting?

Start with the service and the specific task. "It is in the cloud" does not identify who must secure every layer.

## Service models

| Model | Expanded name | Typical customer focus |
|---|---|---|
| IaaS | Infrastructure as a Service | Guest operating system, installed software, access, and workload settings |
| PaaS | Platform as a Service | Deployed application, data, access, and exposed platform settings |
| SaaS | Software as a Service | Users, data sharing, tenant settings, and supported access controls |

Providers protect underlying facilities and infrastructure. Customer duties vary by service and agreement. Check the actual responsibility matrix rather than assuming this introductory table covers every product.

## Worked decision

A small business runs a rented virtual machine. The provider maintains the physical host. A guest operating-system patch is missing, and the workload is customer-managed.

The missing patch is in a layer the customer operates. Ask the customer workload owner to test and deploy it through the change process. A provider's physical maintenance does not establish that the guest system was patched.

Now change the scenario: the business uses a provider-managed application. The provider maintains its application stack, but a customer administrator enables public sharing of a sensitive folder. Review that tenant sharing configuration. Buying a managed application does not remove the need to manage authorized users and sharing.

## Close alternatives

Encryption can protect stored bytes while access rules still allow an unwanted reader to obtain decrypted content. Provider infrastructure security does not establish that a customer's sharing choices are appropriate.

For exam scenarios, locate the responsibility boundary and the requested outcome before choosing the control. A more managed service can move some duties to the provider; it does not mean every duty disappears.

## Ready to move on?

Explain who patches the guest system in the stated virtual-machine example, then explain why that answer does not settle permissions in a managed application.

Try the [responsibility exercise](../labs/10-cloud-responsibility/README.md) and [practice questions](../practice-tests/cloud-05.md).

Objective connection: partial SY0-701 3.1 preparation. [Exam alignment](../study/exam-alignment.md).

## Sources

- [Microsoft: Shared responsibility in the cloud](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility).
- [AWS: Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/).

These fictional examples are original. Service-specific documentation takes precedence over this simplified model.
