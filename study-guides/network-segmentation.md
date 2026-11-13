# Network segmentation: separate devices, then control the connections

## Start with the traffic requirement

Ask: "Which source should reach which destination, using which service?"

A guest network and a staff network can be separate VLANs while routing still permits traffic between them. VLAN means virtual local area network. The security decision depends on the enforced traffic policy too.

## Worked decision

A server accepts staff HTTPS connections. Guests must not reach it. HTTPS means Hypertext Transfer Protocol Secure; this example uses Transmission Control Protocol (TCP) destination port 443.

Assume first-match processing for new connections:

| Order | Source | Destination | Service | Decision |
|---|---|---|---|---|
| 1 | Any | Application server | TCP 443 | Permit |
| 2 | Guest network | Application server | Any | Deny |
| 3 | Any | Any | Any | Deny |

A guest's TCP 443 request matches rule 1, so rule 2 never decides that request. Restrict rule 1's source to the staff network, then retest both allowed and prohibited traffic.

Moving the guest deny above the broad permit blocks guests, but still allows every other source through that broad permit. If only staff should be allowed, narrowing the source directly matches the requirement.

## Avoid the shortcut

A rule that allows too much is not repaired by renaming a VLAN. A firewall also does not automatically encrypt traffic. Choose the mechanism that enforces the actual boundary.

Rule behavior depends on the platform. These examples deliberately state first-match evaluation; do not assume every product behaves identically.

## Ready to move on?

Trace one permitted request and one denied request through every relevant rule. Explain why an "allow HTTPS" rule can still violate an access requirement. Try the [applied questions](../practice-tests/applied-review-04.md).

Objective connection: partial preparation for SY0-701 2.5, 3.2, and 4.5. [Coverage map](../study/exam-alignment.md).


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
