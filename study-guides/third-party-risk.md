# Third-party risk: check what the supplier will actually do

[Contents](../study/contents.md) · [Exercise](../labs/17-supplier-review/README.md) · [Questions](../practice-tests/trust-and-suppliers-14.md)

Partial SY0-701 connection: 5.3, third-party risk assessment and management.

## Start with the service

A supplier that handles public images has a different exposure from one that stores employee records. Identify the data, access, dependencies, and business impact before choosing assessment evidence.

NIST SP 800-161 Rev. 1 provides guidance on managing cybersecurity supply chain risk. Use its assessment and monitoring guidance as supporting reading; the decisions below are fictional study examples.

## Follow the relationship

| Stage | A useful question | Evidence to request |
|---|---|---|
| Selection | Can this service meet our security requirements? | Assessment responses and supporting evidence relevant to its scope |
| Agreement | Who does what when something fails? | Written responsibilities, notification terms, and service requirements |
| Operation | Has the exposure changed? | Reviews of changed access, service scope, incidents, and agreed measures |
| Exit | Can we leave without losing control of data? | Export procedure, access removal, and agreed retention/deletion evidence |

A completed questionnaire is input to a decision. If a response says backups are tested, ask what evidence supports that statement and whether it covers the service being purchased.

## Documents with different jobs

A service-level agreement (SLA) sets agreed service expectations and measures. A nondisclosure agreement (NDA) addresses confidentiality obligations. A statement of work (SOW) describes the work and deliverables. Read the actual terms: a document's title alone does not prove it meets a particular requirement.

## Worked example

A fictional team needs a hosted records service with recovery within eight hours. The supplier advertises 99.9% availability but provides no recovery commitment.

Ask for recovery responsibilities, achievable recovery targets, and relevant test evidence. Availability percentage and recovery time answer different questions. Choosing the service solely from that percentage leaves the stated recovery requirement unresolved.

## Common confusion

Using a supplier does not remove the customer's need to understand and manage its own risks. A report about one product or an earlier period may not cover the proposed service. Monitoring continues after selection because access and services can change.

## Check yourself

A supplier adds a subcontractor that will process the same sensitive records. Should the next review focus only on price?

<details>
<summary>Worked answer</summary>

No. Review the changed data flow, access, contractual requirements, and supporting security evidence. Identify who approves the change and what risks remain. A cheaper price does not answer those questions.

</details>

## Reference

[NIST SP 800-161 Rev. 1, updated publication](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final). Examples and questions here are original; they are not contract language.
