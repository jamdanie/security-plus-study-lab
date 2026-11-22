# DoS, DDoS, reflection, and amplification

[Contents](../study/contents.md) · [Visual exercise](../labs/28-reflection-evidence/README.md)

Partial SY0-701 2.4. These terms describe different properties and can apply together.

| Term | Question it answers |
|---|---|
| Denial of service (DoS) | Is availability being disrupted? |
| Distributed denial of service (DDoS) | Is the denial-of-service traffic coming from distributed sources? |
| Reflection | Are intermediaries sending replies toward a victim using a spoofed source address? |
| Amplification | Is the response traffic larger than the triggering requests? |

MITRE describes reflection through intermediary servers and amplification through larger replies. DNS and NTP are examples of protocols used in such attacks. A protocol name alone does not prove an attack.

## Draw the distinction

A fictional scenario states that an attacker puts the victim's address into requests sent to several reflectors. Those reflectors return much larger responses to the victim, overwhelming its connection.

Reflection explains the direction of replies. Amplification explains the size increase. Multiple traffic sources support the distributed description in this stated scenario. These labels do not compete for one exclusive category.

If a question asks for several labels, check each against the evidence instead of assuming one label rules out the others. Use the wording and choices provided; do not add a mechanism that the scenario never establishes.

## Response has to match the bottleneck

If the access link is already saturated, a filter behind that link may be too late to protect its capacity. MITRE discusses upstream filtering through providers. Coordinate response through the organization's plan.

## Check yourself

A service slows during a popular event. Does that observation alone prove DDoS?

<details>
<summary>Answer</summary>

No. Increased legitimate demand and other faults can also reduce availability. Investigate traffic, capacity, and service evidence before attributing an attack. The observation states an effect, not its cause.

</details>

Sources: [MITRE ATT&CK T1498.002](https://attack.mitre.org/techniques/T1498/002/) and [CISA, Understanding and Responding to DDoS Attacks](https://www.cisa.gov/sites/default/files/publications/understanding-and-responding-to-ddos-attacks_508c.pdf). Scenarios here are original.

[Review questions](../practice-tests/availability-and-access-18.md) · [Cards](../anki/availability-and-access.txt)
