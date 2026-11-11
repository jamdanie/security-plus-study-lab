# Network segmentation: separate devices, then control the connections

A virtual local area network (VLAN) creates a separate Layer 2 broadcast domain. Devices in different VLANs generally need a Layer 3 device to communicate. That could be a router or a multilayer switch.

The security question is what traffic that device permits. Creating two VLANs does not automatically define a restrictive policy between them. If routing permits broad communication, devices can still reach services across the boundary.

## A simple example

Imagine a fictional study space with staff laptops, guest devices, and a shared server. Guests need the internet, but they do not need the staff server.

| Segment | Intended use | Example policy |
|---|---|---|
| Staff | Work devices | Permit the specific server service needed for work |
| Guest | Visitor devices | Permit approved internet services; block internal resources |
| Server | Shared application | Accept only approved traffic from approved sources |
| Management | Administrative devices | Permit management traffic only from designated administrators |

The table describes goals, not a complete production configuration. Real environments also need dependencies such as name resolution and time synchronization.

## Read a traffic rule

A rule can match a source, destination, protocol, and destination port. An access control list (ACL) contains permit or deny entries. A firewall may also track connection state and inspect other properties.

TCP means Transmission Control Protocol. UDP means User Datagram Protocol. HTTPS means Hypertext Transfer Protocol Secure and commonly uses TCP destination port 443. A port number alone does not prove which application is running or whether its traffic is safe.

For a first-match rule set, evaluation stops at the first matching rule. A broad permit above a specific deny can make the deny ineffective. Rule processing varies by product, so check the platform's actual behavior.

## Default deny

Default deny means traffic without an explicit allow rule is blocked. It gives you a reason to identify required connections before opening access. It still needs testing so legitimate work is not interrupted.

Stateful firewalls can permit return traffic for an allowed connection based on connection tracking. A stateless ACL does not automatically do that simply because the first packet was permitted. The exercise below evaluates new connection requests only.

Try the [firewall rule-review exercise](../labs/04-firewall-rule-review/README.md).

## Sources

- [NIST: Deny by Default](https://csrc.nist.gov/glossary/term/deny_by_default).
- [NIST SP 800-41 Revision 1: Guidelines on Firewalls and Firewall Policy](https://csrc.nist.gov/pubs/sp/800/41/r1/final).
- [CISA and partner agencies: Enhanced Visibility and Hardening Guidance for Communications Infrastructure](https://www.cisa.gov/sites/default/files/2024-12/joint-guidance-enhanced-visibility-hardening-guide-for-comms-infrastructure-508c.pdf), discussion of segmentation, VLANs, and access controls.

These are original study notes. Exam-objective mapping has not been confirmed.
