# Exercise 4: find the rule that defeats the policy

Status: ready to try. Personal completion results have not been recorded.

This is an offline exercise with fictional addresses. It does not change your firewall or contact any systems.

## Scenario and assumptions

Staff devices use 192.168.10.0/24. Guests use 192.168.20.0/24. An internal application server is 192.168.30.10.

The policy says staff may initiate HTTPS connections to the server on TCP destination port 443. Guests may not initiate connections to the server. For this simplified exercise, all other new connections must be denied.

TCP means Transmission Control Protocol. HTTPS means Hypertext Transfer Protocol Secure. A /24 prefix here covers addresses from .0 through .255 in the specified subnet.

Assume rules are checked from top to bottom and the first matching rule decides the result. Evaluate only new connection requests, not return packets or established sessions.

## Current rules

| Order | Source | Destination | Protocol | Destination port | Action |
|---|---|---|---|---|---|
| 1 | Any | 192.168.30.10 | TCP | 443 | Permit |
| 2 | 192.168.20.0/24 | 192.168.30.10 | Any | Any | Deny |
| 3 | Any | Any | Any | Any | Deny |

Before opening the answer, decide whether each request is permitted and identify the first matching rule:

| Request | Source | Destination | Protocol | Destination port |
|---|---|---|---|---|
| A | 192.168.10.25 | 192.168.30.10 | TCP | 443 |
| B | 192.168.20.25 | 192.168.30.10 | TCP | 443 |
| C | 192.168.20.25 | 192.168.30.10 | TCP | 22 |
| D | 192.168.10.25 | 192.168.30.10 | TCP | 22 |

## Repair the policy

Change the smallest part of the rules needed to make them match the stated policy. Then evaluate all four requests again. Explain why adding a VLAN would not fix this rule mistake by itself.

<details>
<summary>Suggested answer</summary>

A and B are permitted by rule 1. C is denied by rule 2. D is denied by rule 3.

B violates the intended guest restriction. Rule 2 cannot block B because rule 1 matches first.

Change rule 1's source from Any to 192.168.10.0/24. After the change, A is permitted by rule 1, B and C are denied by rule 2, and D is denied by rule 3.

With the corrected rule 1 and the final deny, rule 2 is redundant for the permit/deny outcomes in this simplified exercise. It can still make the guest restriction explicit. Whether to retain it depends on documentation and logging needs.

A VLAN separates broadcast domains. The Layer 3 enforcement policy still has to restrict traffic between them.

</details>

## Record your reasoning

After trying the exercise, document the request that broke the policy, the matching rule, your correction, and your retest results. Expected answers are not evidence that you personally ran a lab.

## Limits

This is not vendor configuration syntax. Real firewall reviews also consider direction, interfaces, zones, IPv6, connection state, address translation, logging, and required supporting services.

[Read the segmentation guide and its sources](../../study-guides/network-segmentation.md).
