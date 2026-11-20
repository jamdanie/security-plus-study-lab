# Exercise 25: review a guest-network policy

[Segmentation guide](../../study-guides/network-segmentation.md) · [Contents](../../study/contents.md)

Offline fictional policy review. Partial SY0-701 3.2 and 4.5. Ready to try.

## Stated rules

The guest zone may reach the designated DNS resolver using UDP destination port 53 and the designated public training site using TCP destination port 443. Guest access to the payroll zone is forbidden. Deny other guest-initiated flows.

This is a simplified new-flow decision task, not a complete production firewall configuration. Do not infer return-traffic handling, TCP-based DNS, or application inspection.

| Flow | Source zone | Destination | Protocol and destination port |
|---|---|---|---|
| A | Guest | Designated DNS resolver | UDP 53 |
| B | Guest | Payroll zone | TCP 443 |
| C | Guest | Designated public training site | TCP 443 |
| D | Guest | Unlisted external site | TCP 443 |
| E | Guest | Designated DNS resolver | TCP 53 |

Decide allow or deny from the stated policy. Explain why the port number alone is insufficient.

<details>
<summary>Worked decisions</summary>

A and C are allowed. B violates the payroll restriction. D names an unapproved destination. E uses a protocol not permitted by this exercise's rule.

B, C, and D use the same port but have different destinations. TCP 443 does not by itself establish business authorization or trustworthy content.

A real deployment needs requirements for return traffic, DNS behavior, rule order, logging, and validation. Add those through an approved design rather than guessing them into this task.

</details>

## Optional visual extension

Draw the guest, payroll, resolver, and public-site zones. Mark allowed and denied paths with labels. If you use Packet Tracer, verify which features your chosen devices support before implementing a copy of the design.

Keep the policy decision table even if the simulator cannot model every condition. [Review questions](../../practice-tests/data-center-decisions-17.md).
