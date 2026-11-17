# Quick comparisons

Use this as a route back to the explanation, not a substitute for it. The distinctions summarize this repository's worked examples.

| Pair | First distinction | Check the scenario for | Read |
|---|---|---|---|
| Authentication / authorization | Identity check / permitted action | Did sign-in fail, or was a resource action denied? | [Access](../study-guides/identity-and-access.md) |
| Hashing / encryption | Content digest / recoverable secrecy using a key | Is the request to compare bytes or protect disclosure? | [Cryptography](../study-guides/cryptography-choices.md) |
| Signature / encryption | Verify signed content and key origin / conceal content | Does the document need to remain public? | [Cryptography](../study-guides/cryptography-choices.md) |
| Salt / work factor | Distinguish derivations / increase cost per guess | Is the concern precomputation reuse or guessing cost? | [Password storage](../concepts/password-storage.md) |
| RPO / RTO | Data recovery point / recovery duration | What are the outage, usable data, and restoration times? | [Recovery](../study-guides/backup-and-recovery.md) |
| Threat / vulnerability / risk | Potential harm source / weakness / likelihood and consequence in context | What asset, exposure, and impact are stated? | [Risk](../study-guides/risk-management.md) |
| Containment / eradication | Limit spread / remove cause or foothold | Does isolation alone remove persistence? | [Response](../study-guides/incident-response.md) |
| Detection / prevention | Identify activity / block the unwanted action | Does the described component only alert? | [Controls](../study-guides/security-controls.md) |
| Policy / procedure | Broad obligation / operational steps | Does the team need direction or a task sequence? | [Governance](../study-guides/security-governance.md) |
| VLAN / traffic policy | Layer 2 separation / permitted routed communication | What rule enforces the boundary? | [Networks](../study-guides/network-segmentation.md) |
| Poisoning / escalation | Corrupt relied-on information / gain permissions | Which changed state is actually observed? | [Attack evidence](../study-guides/attack-patterns.md) |
| Patch installation / validated remediation | Job outcome / evidence the weakness is addressed | Has a suitable follow-up check occurred? | [Vulnerabilities](../study-guides/vulnerability-management.md) |

RPO means recovery point objective; RTO means recovery time objective; VLAN means virtual local area network.

## Use a comparison

A statement that a backup restored successfully does not establish that stolen information was never disclosed. Identify the property the action supports and avoid extending it beyond the evidence.

For each pair, invent a small change to the scenario that would make the other concept relevant. Then try [Requirement review 12](../practice-tests/requirement-review-12.md).

[Contents](contents.md)
